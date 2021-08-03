import discord
from discord import client
from discord.ext import commands
import requests
import re
from bs4 import BeautifulSoup

bot = commands.Bot(command_prefix='$')

@bot.event
async def on_ready():
    print('bot is online')

@bot.command()
async def 通貨(ctx):
    response = requests.get("https://poedb.tw/price")
    soup = BeautifulSoup(response.text, "html.parser")
    count = 0
    listx = ['']
    for x in soup.find_all("tr"):
        count = count+1
        listx.append(x.text)

    str1 = listx[1]
    str2 = str1[16:]
    str2 = re.sub('x','C\n',str2)
    await ctx.send('資料來源流亡編年史')
    await ctx.send(str2)
@bot.command()
async def 聖甲蟲(ctx):
    response = requests.get("https://poedb.tw/price?c=scarabs")
    soup = BeautifulSoup(response.text, "html.parser")
    count = 0
    listx = ['']
    for x in soup.find_all("tr"):
        count = count+1
        listx.append(x.text)

    str1 = listx[1]
    str2 = str1[4:]
    str2 = re.sub('x','C\n',str2)
    await ctx.send('資料來源流亡編年史')
    await ctx.send(str2)

@bot.command()
async def 化石(ctx):
    response = requests.get("https://poedb.tw/price?c=fossils")
    soup = BeautifulSoup(response.text, "html.parser")
    count = 0
    listx = ['']
    for x in soup.find_all("tr"):
        count = count+1
        listx.append(x.text)

    str1 = listx[1]
    str2 = str1[4:]
    str2 = re.sub('x','C\n',str2)
    await ctx.send('資料來源流亡編年史')
    await ctx.send(str2)





bot.run('輸入你的Discord機器人密鑰')