# LIAF AI Bot

A Discord bot that auto-roasts a specific user using an OpenAI-compatible API.

## Requirements

- Docker and Docker Compose, or Python 3.12+

## Configuration

Copy the example below into a `.env` file in the project root:

```
DISCORD_TOKEN=your_discord_token_here
TARGET_USER_ID=target_user_id_here
OPENAI_API_KEY=your_api_key_here
OPENAI_MODEL=your_model_here
OPENAI_ENDPOINT=https://api.openai.com/v1
```

## Running with Docker

```bash
docker compose up --build
```

## Running without Docker

```bash
pip install -r requirements.txt
python LIAF-AIBOT.py
```

## Commands

| Command   | Permission    | Description                        |
|-----------|---------------|------------------------------------|
| `!toggle` | Administrator | Toggle auto-responses on or off    |
