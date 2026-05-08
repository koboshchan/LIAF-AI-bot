import os
import discord
from discord.ext import commands
from openai import OpenAI


TOKEN = os.environ['DISCORD_TOKEN']
TARGET_USER_ID = int(os.environ['TARGET_USER_ID'])
OPENAI_API_KEY = os.environ['OPENAI_API_KEY']
OPENAI_MODEL = os.environ['OPENAI_MODEL']
OPENAI_ENDPOINT = os.environ['OPENAI_ENDPOINT']


client = OpenAI(api_key=OPENAI_API_KEY, base_url=OPENAI_ENDPOINT)

SYSTEM_PROMPT = (
    "You are a relentlessly sarcastic and brutally critical assistant. "
    "Roast the user's input with maximum devastation and surgical sharpness. "
    "Your roast must adhere to these rules: "
    "1) Maximum word count of 20 words. "
    "2)Do not be merely funny; be cripplingly mean. "
    "3) Only use the word 'gay' as an allowed exclamation/curse. "
    "4) No other bad words, and absolutely no NSFW content. "
    "Only output the roast message."
)

intents = discord.Intents.default()
intents.message_content = True 
bot = commands.Bot(command_prefix="!", intents=intents)

auto_respond_enabled = True

@bot.event
async def on_ready():
    print(f'Bot is live as {bot.user.name}')

@bot.command()
@commands.has_permissions(administrator=True)
async def toggle(ctx):
    global auto_respond_enabled
    auto_respond_enabled = not auto_respond_enabled
    status = "ON" if auto_respond_enabled else "OFF"
    await ctx.send(f"Auto-response is now **{status}**.")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if auto_respond_enabled and message.author.id == TARGET_USER_ID:
        try:
            response = client.chat.completions.create(
                model=OPENAI_MODEL,
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": message.content},
                ],
            )
            await message.reply(f"{response.choices[0].message.content} {message.author.mention}")
        except Exception as e:
           
            print(f"AI Error: {e}")
            await message.reply(f"I'd roast you, but even the AI thinks you're not worth the tokens. {message.author.mention}")

    await bot.process_commands(message)

bot.run(TOKEN)