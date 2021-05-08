from discord.ext import commands

from cogs.others import vim
from cogs.languages import languages

vim_ = vim
c = languages.Language('c')
python = languages.Language('python')
javascript = languages.Language('js')


class Compiler(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def compile(self, ctx):
        await ctx.send('languages\n'
                       '`c` `python` `js`')

    @commands.command()
    async def c(self, ctx, *, arg):
        await c.compiler(ctx, arg)

    @commands.command()
    async def python(self, ctx, *, arg):
        await python.compiler(ctx, arg)

    @commands.command()
    async def js(self, ctx, *, arg):
        await javascript.compiler(ctx, arg)

    @commands.command()
    async def highlight(self, ctx):
        await ctx.send('`vimhl` `chl` `pyhl` `jshl`')

    @commands.command()
    async def chl(self, ctx, *, arg):
        await c.highlight(ctx, arg)

    @commands.command()
    async def pythonhl(self, ctx, *, arg):
        await python.highlight(ctx, arg)

    @commands.command()
    async def jshl(self, ctx, *, arg):
        await javascript.highlight(ctx, arg)


def setup(client):
    client.add_cog(Compiler(client))
