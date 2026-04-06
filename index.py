import fluxer
import os
from dotenv import load_dotenv

load_dotenv()

intents = fluxer.Intents.default()
intents.message_content = True
bot = fluxer.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    for i in os.listdir("cogs"):
        if i.endswith(".py"):
            await bot.load_extension(f"cogs.{i[:-3]}")

    print(f"Bot is ready! Logged in as {bot.user.username}")

if __name__ == "__main__":
    TOKEN = os.getenv("BOT_TOKEN")
    bot.run(TOKEN)