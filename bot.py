from discord.ext import commands
import os
import json


with open('config.json') as f:
    config = json.load(f)

bot = commands.Bot(config["prefix"])


def check_whitelist(ctx):
    return str(ctx.message.author.id) in config["whitelist"]


@bot.event
async def on_ready():
    print('All ready {0.user}'.format(bot))


@bot.command(aliases=["load"])
@commands.check(check_whitelist)
async def load_extension(ctx, extension):
    bot.load_extension(f'cogs.{extension}')
    await ctx.send(f"Extension {extension} loaded successfully!")


@bot.command(aliases=["unload"])
@commands.check(check_whitelist)
async def unload_extension(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    await ctx.send(f"Extension {extension} unloaded successfully!")


@bot.command(aliases=["reload"])
@commands.check(check_whitelist)
async def reload_extension(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    bot.load_extension(f'cogs.{extension}')
    await ctx.send(f"Extension {extension} reloaded successfully!")



[bot.load_extension(f'cogs.{cog[:-3]}') for cog in os.listdir('./cogs/') if cog.endswith('.py')]


bot.run(config["token"])
