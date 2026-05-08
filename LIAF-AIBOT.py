import discord
from discord.ext import commands
import google.generativeai as genai


TOKEN = 'your_token'
TARGET_USER_ID = 1239704208056385586 
GEMINI_API_KEY = 'YOUR_GEMINI_API_KEY'


genai.configure(api_key=GEMINI_API_KEY)
ai_model = genai.GenerativeModel('gemini-1.5-flash')

SYSTEM_PROMPT = (
    "You are a sarcastic assistant. A specific user is talking, and you need to "
    "give a witty, funny, and sharp roast based on what they said. "
    "Keep it under 2 sentences and don't be truly hateful—keep it a 'friendly' roast."
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
            prompt = f"{SYSTEM_PROMPT}\n\nUser said: {message.content}"
            response = ai_model.generate_content(prompt)
            
           
            await message.reply(f"{response.text} {message.author.mention}")
        except Exception as e:
           
            print(f"AI Error: {e}")
            await message.reply(f"I'd roast you, but even the AI thinks you're not worth the tokens. {message.author.mention}")

    await bot.process_commands(message)

bot.run(TOKEN)