from discord.ext import commands

import c


client = commands.Bot('~')
clang = c


@client.event
async def on_ready():
    print('All ready {0.user}'.format(client))


@client.command()
async def c(ctx, *, arg):
    await clang.compiler(ctx, arg)


@client.command()
async def syntax(ctx, *, arg):
    await ctx.send('select syntax\n'
                   '`vim` `c` `python`')
    if ctx.message.content.startswith == 'vim':
        await v(ctx, arg)
    elif ctx.message.content == 'c':
        await clang.syntax(ctx, arg)


async def v(ctx, arg):
    await ctx.message.delete()
    await ctx.send('```vim\n' + arg + '\n```')


@client.command()
async def vim(ctx, *, arg):
    await ctx.message.delete()
    await ctx.send('```vim\n' + arg + '\n```')


client.run('token')
