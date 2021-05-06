import os


async def highlight(ctx, arg):
    await ctx.message.delete()
    await ctx.send('```c\n' + arg + '\n```')


async def compiler(ctx, arg):
    await highlight(ctx, arg)
    open('main.txt', 'w').close()
    open('main.py', 'w').write(arg)
    os.system("python main.py 2> main.txt")
    await ctx.send('```' + open('main.txt', 'r').read() + '```')
