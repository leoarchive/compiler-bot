import os


class Language:
    def __init__(self, language):
        self.language = language

    async def highlight(self, ctx, arg):
        await ctx.send(f'>>> ```{self.language}\n{arg}\n```')

    async def compiler(self, ctx, arg):
        open('temp\main.txt', 'w').close()
        open('temp\output.txt', 'w').close()

        if self.language == 'c':
            open('temp\main.c', 'w').close()
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
            open('temp\main.c', 'w').close()

        elif self.language == 'python':
            open('temp\main.py', 'w').close()
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
            open('temp\main.py', 'w').close()

        elif self.language == 'js':
            open('temp\main.js', 'w').close()
            open('temp\main.js', 'w').write(arg)

            os.system("node temp\main.js >> temp\main.txt")
            if os.stat("temp\main.txt").st_size == 0:
                os.system("node temp\main.js 2> temp\main.txt")
            open('temp\main.js', 'w').close()

    async def output(self, ctx, arg):
        output = open('temp\output.txt', 'r').read()
        main = open('temp\main.txt', 'r').read()
        if os.stat("temp\output.txt").st_size > 0 and os.stat("temp\main.txt").st_size == 0:
            await ctx.send(f'>>> ```{self.language}\n{arg}\n```**warning**\n``` {output} ```')
        elif os.stat("temp\output.txt").st_size > 0 and os.stat("temp\main.txt").st_size > 0:
            await ctx.send(f'>>> ```{self.language}\n{arg}\n```**compiled** ```{main}```**with code**```{output}```')
        elif os.stat("temp\main.txt").st_size == 0:
            await ctx.send(f'>>> ```{self.language}\n{arg}\n```**compiled**')
        else:
            await ctx.send(f'>>> ```{self.language}\n{arg}\n```**compiled** ```{main}```')
        open('temp\output.txt', 'r').close()
        open('temp\main.txt', 'r').close()