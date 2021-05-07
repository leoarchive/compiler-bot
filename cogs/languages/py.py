import os


async def highlight(ctx, arg):
    await ctx.send('>>> ```python\n' + arg + '\n```')


async def compiler(ctx, arg):
    open('temp\main.txt', 'w').close()
    open('temp\main.py', 'w').write(arg)

    for arq in open('temp\main.py'):
        if 'os' in arq:
            await ctx.send('>>> **compiled failed**\n```css\n [os detected]\n```')
            return
        elif 'while True' in arq:
            await ctx.send('>>> **compiled failed**\n```css\n [infinite loop detected]\n```')
            return

    os.system("python temp\main.py >> temp\main.txt")
    if os.stat("temp\main.txt").st_size == 0:
        os.system("python temp\main.py 2> temp\main.txt")

    if os.stat("temp\main.txt").st_size == 0:
        await ctx.send('>>> ```python\n' + arg + '\n```' +
                       '\n**compiled successfully**')
    else:
        await ctx.send('>>> ```python\n' + arg + '\n```' +
                     '**compiled** ```' +
                     open('temp\main.txt', 'r').read() + '```')
