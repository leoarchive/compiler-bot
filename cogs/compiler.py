from discord.ext import commands


from cogs.languages import c
from cogs.languages import py
from cogs.languages import js
from cogs.others import vim

jslang = js
vim_ = vim
clang = c
python = py


class Compiler(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def compile(self, ctx):
        await ctx.send('languages\n'
                       '`c` `python` `js`')

    @commands.command()
    async def c(self, ctx, *, arg):
        await clang.compiler(ctx, arg)

    @commands.command()
    async def python(self, ctx, *, arg):
        await python.compiler(ctx, arg)

    @commands.command()
    async def js(self, ctx, *, arg):
        await jslang.compiler(ctx, arg)

    @commands.command()
    async def highlight(self, ctx):
        await ctx.send('`vimhl` `chl` `pyhl` `jshl`')

    @commands.command()
    async def pyhl(self, ctx, *, arg):
        await python.highlight(ctx, arg)

    @commands.command()
    async def jshl(self, ctx, *, arg):
        await jslang.highlight(ctx, arg)

    @commands.command()
    async def chl(self, ctx, *, arg):
        await clang.highlight(ctx, arg)


def setup(client):
    client.add_cog(Compiler(client))
