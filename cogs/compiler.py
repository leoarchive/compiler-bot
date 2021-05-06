import discord
from discord.ext import commands

from .languages import c
clang = c


async def v(ctx, arg):
    await ctx.message.delete()
    await ctx.send('```vim\n' + arg + '\n```')


class Compiler(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def c(self, ctx, *, arg):
        await clang.compiler(ctx, arg)

    @commands.command()
    async def syntax(self, ctx, *, arg):
        await ctx.send('select syntax\n'
                       '`vim` `c` `python`')
        if ctx.message.content.startswith == 'vim':
            await v(ctx, arg)
        elif ctx.message.content == 'c':
            await clang.syntax(ctx, arg)

    @commands.command()
    async def vim(self, ctx, *, arg):
        await ctx.message.delete()
        await ctx.send('```vim\n' + arg + '\n```')


def setup(client):
    client.add_cog(Compiler(client))
