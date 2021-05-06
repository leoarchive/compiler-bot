

async def highlight(ctx, arg):
    await ctx.message.delete()
    await ctx.send('```vim\n' + arg + '\n```')

