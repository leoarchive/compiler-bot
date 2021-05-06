from discord.ext import commands

bot = commands.Bot('g.')


@bot.event
async def on_ready():
    print('All ready {0.user}'.format(bot))


@bot.command(aliases=["load"])
async def load_extension(ctx, extension):
    bot.load_extension(f'cogs.{extension}')
    await ctx.send(f"Extension {extension} loaded successfully!")


@bot.command(aliases=["unload"])
async def unload_extension(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    await ctx.send(f"Extension {extension} unloaded successfully!")


@bot.command(aliases=["reload"])
async def reload_extension(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    bot.load_extension(f'cogs.{extension}')
    await ctx.send(f"Extension {extension} reloaded successfully!")

[bot.load_extension(f'cogs.{cog[:-3]}') for cog in os.listdir('./cogs/') if cog.endswith('.py')]


bot.run('NTMzODQzNzM3NjU1MjQ2ODQ4.XDqquQ.75BTbLMHezkHwxk70_VJG44JB2I')