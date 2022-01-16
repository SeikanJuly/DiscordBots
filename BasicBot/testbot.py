import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
#for 1.5 discord.py change


Token = "OTI5NzY2NTEyNjgyNzQ1OTY2.YdsGig.F1bxTFLXZ5QwCIUqJWQFJv4jZsI"
#this is testbot token

bot = commands.Bot(command_prefix="!", intents = intents)

@bot.event
async def on_ready():
  print("ViviBot is online! ")

@bot.event
async def on_member_join(member):
  print(F"{member} joined!")
  channeltest = bot.get_channel(928921597023223861)
  await channeltest.send(F"歡迎 {member} 加入加密幣!\n如您還不知道加密幣的活動內容請參考 <#930063858696093768>")

@bot.event
async def on_member_remove(member):
  print(F"{member} left.")
  channeltest = bot.get_channel(928921597023223861)
  await channeltest.send(F"{member} left.")

bot.run(Token)