import os


async def highlight(ctx, arg):
    await ctx.send('>>> ```c\n' + arg + '\n```')


async def compiler(ctx, arg):
    open('temp\main.txt', 'w').close()
    open('temp\output.txt', 'w').close()
    open('temp\main.c', 'w').write(arg)

    for arq in open('temp\main.c'):
        if 'system' in arq:
            await ctx.send('>>> **compiled failed**\n```css\n [system detected]\n```')
            return

    os.system("gcc -o temp\main temp\main.c 2> temp\output.txt")
    if os.stat("temp\output.txt").st_size == 0:
        os.system("temp\main >> temp\main.txt")
        if os.stat("temp\main.txt").st_size == 0:
            os.system("temp\main 2> temp\main.txt")
        os.system("echo %errorlevel% >> temp\output.txt")
        open('temp\main.txt', 'a').write(' ')

        await ctx.send('>>> ' + '```c\n' + arg + '\n```' +
                       '**compiled successfully**\n'
                       '```' + open('temp\main.txt', 'r').read() + '\n```' +
                       '**with code**\n'
                       '```' + open('temp\output.txt', 'r').read() + '\n```')
    else:
        await ctx.send('>>> ' + '```c\n' + arg + '\n```' +
                       '**compiled error**\n```' +
                       open('temp\output.txt', 'r').read() + '```')
