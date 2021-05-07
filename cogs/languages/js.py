import os


async def highlight(ctx, arg):
    await ctx.send('>>> ```js\n' + arg + '\n```')


async def compiler(ctx, arg):
    open('temp\main.txt', 'w').close()
    open('temp\main.js', 'w').write(arg)

    # for arq in open('temp\main.js'):
    #     if 'os' in arq:
    #         await ctx.send('>>> **compiled failed**\n```css\n [os detected]\n```')
    #         return
    #     elif 'while True' in arq:
    #         await ctx.send('>>> **compiled failed**\n```css\n [infinite loop detected]\n```')
    #         return

    os.system("node temp\main.js >> temp\main.txt")
    if os.stat("temp\main.txt").st_size == 0:
        os.system("node temp\main.js 2> temp\main.txt")

    if os.stat("temp\main.txt").st_size == 0:
        await ctx.send('>>> ```js\n' + arg + '\n```' +
                       '\n**compiled successfully**')
    else:
        await ctx.send(
            '>>> ```js\n'
            + arg +
            '\n```' +
            '**compiled** ```' +
            open('temp\main.txt', 'r').read() + '```'
        )
