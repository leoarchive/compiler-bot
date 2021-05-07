import os


async def highlight(ctx, arg):
    await ctx.message.delete()
    await ctx.send('```c\n' + arg + '\n```')


async def compiler(ctx, arg):
    await highlight(ctx, arg)
    open('temp\main.txt', 'w').close()
    open('temp\main.py', 'w').write(arg)
    os.system("python temp\main.py >> temp\main.txt")
    if os.stat("temp\main.txt").st_size == 0:
        os.system("python temp\main.py 2> temp\main.txt")
    await ctx.send('```' + open('temp\main.txt', 'r').read() + '```')
