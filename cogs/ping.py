from fluxer import Cog

class Ping(Cog):
    def __init__(self, bot):
        super().__init__(bot)

    @Cog.listener(name="on_ready")
    async def on_ready(self):
        print(f"{self.__class__.__name__} cog is ready.")

    @Cog.command()
    async def ping(self, ctx):
        await ctx.reply("Pong!")

async def setup(bot):
    await bot.add_cog(Ping(bot))