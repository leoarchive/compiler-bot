from discord.ext import commands


from cogs.languages import c
from cogs.languages import py
from cogs.others import vim

vim_ = vim
clang = c
python = py

class Compiler(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def highlight(self, ctx):
        await ctx.send('`vimhl` `chl` `pyhl`')

    @commands.command()
    async def pyhl(self, ctx, *, arg):
        await python.highlight(ctx, arg)

    @commands.command()
    async def vimhl(self, ctx, *, arg):
        await vim_.highlight(ctx, arg)

    @commands.command()
    async def chl(self, ctx, *, arg):
        await clang.highlight(ctx, arg)

    @commands.command()
    async def compile(self, ctx):
        await ctx.send('`c` `python` `js`')

    @commands.command()
    async def c(self, ctx, *, arg):
        await clang.compiler(ctx, arg)

    @commands.command()
    async def python(self, ctx, *, arg):
        await python.compiler(ctx, arg)


def setup(client):
    client.add_cog(Compiler(client))
