import asyncio
import discord
import requests
import random
from discord import Embed, File
from discord.ext import commands
from PIL import Image
from io import BytesIO

token = "token"

client = commands.Bot(command_prefix='-')
client.remove_command('help')

@client.command()
async def help(ctx):
    embed = Embed(title="All Commands", description=None)
    embed.add_field(name="+help", value="Displays all available commands", inline=False)
    embed.add_field(name="+http", value="Sends fresh http proxy list", inline=False)
    embed.add_field(name="+https", value="Sends fresh https proxy list", inline=False)
    embed.add_field(name="+socks4", value="Sends fresh socks4 proxy list", inline=False)
    embed.add_field(name="+socks5", value="Sends fresh socsk5 proxy list", inline=False)
    embed.add_field(name="+all", value="Sends fresh http, https, socks4 and socks5 proxy list", inline=False)
    embed.add_field(name="howgay", value="Checks how gay you are from 0-100%", inline=False)
    embed.add_field(name="our", value="Communist our image", inline=False)
    embed.add_field(name="slap", value="Slaps you", inline=False)
    await ctx.send(embed=embed)

@client.command()
async def http(ctx):
    f = open("Data/http-proxies.txt", "a+")
    f.truncate(0)
    r = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=http&timeout=5000')
    proxies = []
    for proxy in r.text.split('\n'):
        proxy = proxy.strip()
        if proxy:
            proxies.append(proxy)
    for p in proxies:
        f.write((p)+"\n")
    await ctx.send(file=File("Data/http-proxies.txt"))

@client.command()
async def https(ctx):
    f = open("Data/https-proxies.txt", "a+")
    f.truncate(0)
    r = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=https&timeout=5000')
    proxies = []
    for proxy in r.text.split('\n'):
        proxy = proxy.strip()
        if proxy:
            proxies.append(proxy)
    for p in proxies:
        f.write((p)+"\n")
    await ctx.send(file=File("Data/https-proxies.txt"))

@client.command()
async def socks4(ctx):
    f = open("Data/socks4-proxies.txt", "a+")
    f.truncate(0)
    r = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=socks4&timeout=5000')
    proxies = []
    for proxy in r.text.split('\n'):
        proxy = proxy.strip()
        if proxy:
            proxies.append(proxy)
    for p in proxies:
        f.write((p)+"\n")
    await ctx.send(file=File("Data/socks4-proxies.txt"))

@client.command()
async def socks5(ctx):
    f = open("Data/socks5-proxies.txt", "a+")
    f.truncate(0)
    r = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=socks5&timeout=5000')
    proxies = []
    for proxy in r.text.split('\n'):
        proxy = proxy.strip()
        if proxy:
            proxies.append(proxy)
    for p in proxies:
        f.write((p)+"\n")
    await ctx.send(file=File("Data/socks5-proxies.txt"))

@client.command()
async def all(ctx):
    f = open("Data/all-proxies.txt", "a+")
    f.truncate(0)
    r = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=all&timeout=5000')
    proxies = []
    for proxy in r.text.split('\n'):
        proxy = proxy.strip()
        if proxy:
            proxies.append(proxy)
    for p in proxies:
        f.write((p)+"\n")
    await ctx.send(file=File("Data/all-proxies.txt"))

@client.command()
async def howgay(ctx, member: discord.Member = None):
        member = member or ctx.author
        response=[random.randint(0,100)]
        embed=discord.Embed(title='gay r8 machine',
        description=f"\n{member.mention} is {random.choice(response)}% gay!!  :rainbow_flag:",color  = 0xdb7bff)
        await ctx.send(embed=embed)


@client.command()
async def slap(ctx, user: discord.Member = None):
    if user == None:
        user = ctx.author
    slap = Image.open("./slap/slap.jpg")
    asset = user.avatar_url_as(size = 128)
    data = BytesIO(await asset.read())
    pfp = Image.open(data)
    pfp = pfp.resize((87,87)) # 107 x 98
    slap.paste(pfp, (85,43))
    slap.save("./slap/slap.png")
    await ctx.send(file = discord.File("./slap/slap.png"))

@client.command()
async def our(ctx, user: discord.Member = None):
    if user == None:
        user = ctx.author
    our = Image.open("./our/our.png")
    asset = ctx.guild.icon_url_as(size = 128)
    data = BytesIO(await asset.read())
    pfp = Image.open(data)
    pfp = pfp.resize((301,265)) # 301 x 265
    our.paste(pfp, (895,443))
    our.save("./our/our.png")
    await ctx.send(file = discord.File("./our/our.png"))

client.run(token)
