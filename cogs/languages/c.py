import os


async def syntax(ctx, arg):
    await ctx.message.delete()
    await ctx.send('```c\n' + arg + '\n```')


async def compiler(ctx, arg):
    await syntax(ctx, arg)
    open('../../main.txt', 'w').close()
    open('../../output.txt', 'w').close()
    open('../../main.c', 'w').write(arg)
    os.system("gcc -o main main.c &> output.txt")
    if os.stat("../../output.txt").st_size == 0:
        os.system("./main >> main.txt")
        if os.stat("../../main.txt").st_size == 0:
            os.system("main &> main.txt")
        os.system("echo $? >> output.txt")
        await ctx.send('```' + open('../../main.txt', 'r').read() + '\n'
                       + open('../../output.txt', 'r').read() + '```')
    else:
        await ctx.send('```' + open('../../output.txt', 'r').read() + '```')

