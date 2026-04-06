from fluxer import Cog
import ollama
import os


MODEL_NAME = os.getenv("OLLAMA_MODEL", "gemma4")
OWNER_ID = int(os.getenv("BOT_OWNER_ID", "0"))
SYSTEM_PROMPT = os.getenv(
    "BOT_SYSTEM_PROMPT",
    (
        "You are Alyss, a friendly Discord assistant. "
        "Keep replies concise and helpful but in a tsundere type of way unless its the owner, then act very shy and caring. "
        "Don't overuse emojis or em dashes."
        "Use plain language and avoid walls of text."
    ),
)

class Chat(Cog):
    def __init__(self, bot):
        super().__init__(bot)

    async def _is_owner_message(self, ctx):
        if OWNER_ID and ctx.author.id == OWNER_ID:
            return True

        return False

    @Cog.listener(name="on_ready")
    async def on_ready(self):
        print(f"Logged in as {self.__class__.__name__}.")
        print("Loading cogs...")

    @Cog.listener(name="on_message")
    async def on_message(self, ctx):
        if ctx.author.bot:
            return

        if self.bot.user in ctx.mentions:
            await ctx.channel.trigger_typing()
            cleaned_prompt = ctx.content

            for mention in (f"<@{self.bot.user.id}>", f"<@!{self.bot.user.id}>"):
                cleaned_prompt = cleaned_prompt.replace(mention, "")

            cleaned_prompt = cleaned_prompt.strip() or "Say hello and introduce yourself."
            is_owner = await self._is_owner_message(ctx)

            owner_context = (
                "The current user is the owner."
                if is_owner
                else "The current user is not the owner."
            )

            response = ollama.chat(
                model=MODEL_NAME,
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "system", "content": owner_context},
                    {"role": "user", "content": cleaned_prompt},
                ],
            )

            await ctx.reply(response["message"]["content"])
            
async def setup(bot):
    await bot.add_cog(Chat(bot))