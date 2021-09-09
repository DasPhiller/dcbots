import discord
from discord.ext import commands
import requests
import random

bot = discord.Bot()


@bot.event
async def on_ready():
    print("Started")


# Ping
@bot.command(guilds_ids=[873953940532756530])
async def ping(ctx):
    """Zeigt den bot ping"""
    await ctx.respond(f"Ping: {round(bot.latency * 1000)}ms")


# Server Command
@bot.command(guilds_ids=[873953940532756530])
async def server(ctx):
    """Zeigt informatioen über den Server"""
    await ctx.respond("IP: mcsrv.16nergames.at:25588" + '\n' + "Version: 1.17.1", ephemeral=True)


@bot.command(guilds_ids=[873953940532756530])
async def meme(ctx):
    """Zeigt ein meme"""
    # Request:
    response = requests.get('https://evergene.io/api/memes/')
    json_response = response.json()
    imageurl = json_response['url']

    # Message
    embed = discord.Embed(title="Here you go:")
    embed.set_image(url=imageurl)
    await ctx.respond(embed=embed)


# Question
@bot.command(guilds_ids=[873953940532756530])
async def question(ctx, *, question):
    """Stelle eine Frage"""
    response = ['Yes', 'No', 'Maybe', 'Probably', 'Probably not']
    response_embed = discord.Embed(title="Question \"" + str(question) + "\" Answer: " + str(random.choice(response)), color=0x1affbe)
    response_embed.set_author(name=str(ctx.author))
    await ctx.respond(embed=response_embed)


# Google
@bot.command(guilds_ids=[873953940532756530])
async def google(ctx, *, search_them):
    """Google etwas"""

    while ' ' in search_them:
        search_them = search_them.replace(' ', '+')

    await ctx.respond("https://google.com/search?q=" + search_them, ephemeral=True)


# Changelog
@bot.command(guilds_ids=[873953940532756530])
async def changelog(ctx):
    """Zeigt den Changelog"""
    with open('tokens/changelog.txt', 'r') as file:
        Changelog = file.read()
    embed=discord.Embed(title="Changelog", description=Changelog, color=0x14c5c8)
    embed.set_footer(text="Made by PHIL_GAMER_YT")
    await ctx.respond(embed=embed)

