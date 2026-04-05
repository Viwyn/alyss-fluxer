from fluxer import Cog, User

class Pfp(Cog):
    def __init__(self, bot):
        super().__init__(bot)

    @Cog.listener(name="on_ready")
    async def on_ready(self):
        print(f"{self.__class__.__name__} cog is ready.")

    @Cog.command()
    async def pfp(self, ctx, user: User = None):
        user = user or ctx.author
        await ctx.reply(user.avatar_url)

async def setup(bot):
    await bot.add_cog(Pfp(bot))