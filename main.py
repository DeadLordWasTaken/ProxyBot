import asyncio
import discord
import requests
import random
from discord import Embed, File
from discord.ext import commands
from PIL import Image
from io import BytesIO

token = ""

client = commands.Bot(command_prefix='+')
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
    embed.add_field(name="kick", value="Kick a member from the server", inline=False)
    embed.add_field(name="ban", value="Ban a member from the server", inline=False)
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

@client.command(aliases=["Ban", "BAN"])
@commands.has_permissions(administrator=True)
async def ban(ctx, member : discord.Member, reason=None):
  """Bans a user"""
  if reason == None:
      messageok = f"You have been banned from {ctx.guild.name} for: ``{reason}``"
      await member.send(messageok)
      await member.ban(reason=reason)
      em1 = embed=discord.Embed(title="✅ Member Banned.", colour=0xff0000)
      msg = await ctx.send(embed=em1)
      await msg.edit(embed=em1)
      em2 = embed=discord.Embed(title="✅ Member Banned.", colour=0x77ff00)
      await msg.edit(embed=em2)
      em3 = embed=discord.Embed(title=" Member Banned.", colour=0xffaa00)
      await msg.edit(embed=em3)
      em4 = embed=discord.Embed(title=" Member Banned.", colour=0x00ddff)
      await msg.edit(embed=em4)
      em5 = embed=discord.Embed(title=" Member Banned.", colour=0x0033ff)
      await msg.edit(embed=em5)
      em6 = embed=discord.Embed(title=" Member Banned.", colour=0xff00dd)
      await msg.edit(embed=em6)
@ban.error
async def ban_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
      embed=discord.Embed()
      embed.title="Missing Permissions."
      embed.description=f"You Do Not Have **Permissions** To Ban This Member."
      embed.color=0xff0000
      await ctx.send(embed=embed)

@client.command()
async def kick(ctx, user:discord.User):
    await ctx.guild.ban(user)
    await asyncio.sleep(1)
    await ctx.guild.unban(user)
    em1 = embed=discord.Embed(title="✅ Member Kicked.", colour=0xff0000)
    msg = await ctx.send(embed=em1)
    await msg.edit(embed=em1)
    em2 = embed=discord.Embed(title=" Member Kicked.", colour=0x77ff00)
    await msg.edit(embed=em2)
    em3 = embed=discord.Embed(title=" Member Kicked.", colour=0xffaa00)
    await msg.edit(embed=em3)
    em4 = embed=discord.Embed(title=" Member Kicked.", colour=0x00ddff)
    await msg.edit(embed=em4)
    em5 = embed=discord.Embed(title=" Member Kicked.", colour=0x0033ff)
    await msg.edit(embed=em5)
    em6 = embed=discord.Embed(title=" Member Kicked.", colour=0xff00dd)
    await msg.edit(embed=em6)
@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
      embed=discord.Embed()
      embed.title="Missing Permissions."
      embed.description=f"You Do Not Have **Permissions** To kick This Member."
      embed.color=0xff0000
      await ctx.send(embed=embed)

@client.command()
async def slap(ctx, user: discord.Member = None):
    if user == None:
        user = ctx.author
    slap = Image.open("slap.jpg")
    asset = user.avatar_url_as(size = 128)
    data = BytesIO(await asset.read())
    pfp = Image.open(data)
    pfp = pfp.resize((87,87)) # 107 x 98
    slap.paste(pfp, (85,43))
    slap.save("slap.png")
    await ctx.send(file = discord.File("slap.png"))


client.run(token)
