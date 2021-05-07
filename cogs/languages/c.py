import os


async def highlight(ctx, arg):
    await ctx.message.delete()
    await ctx.send('```c\n' + arg + '\n```')


async def compiler(ctx, arg):
    await highlight(ctx, arg)
    open('temp\main.txt', 'w').close()
    open('temp\output.txt', 'w').close()
    open('temp\main.c', 'w').write(arg)
    os.system("gcc -o temp\main temp\main.c 2> temp\output.txt")
    if os.stat("temp\output.txt").st_size == 0:
        os.system("temp\main >> temp\main.txt")
        if os.stat("temp\main.txt").st_size == 0:
            os.system("temp\main 2> temp\main.txt")
        os.system("echo %errorlevel% >> temp\output.txt")
        await ctx.send('```' + open('temp\main.txt', 'r').read() + '\n'
                       + open('temp\output.txt', 'r').read() + '```')
    else:
        await ctx.send('```' + open('temp\output.txt', 'r').read() + '```')
