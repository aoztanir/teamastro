import discord
import datetime 
from covid19_data import JHU
import random as rando

import praw
from discord.voice_client import VoiceClient
import youtube_dl
import random
import wikipedia
import os

import asyncio
from googlesearch import search

from youtubesearchpython import VideosSearch

from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
from datetime import datetime
import pytz 
import time
# from pyowm import OWM
import requests, json
from discord.ext import commands
import pafy
import keep_alive
from threading import Thread
import pyjokes


ctxSave=None

QueList = []
TaskList = []

# filtered_words = ["word1","word2"]




intents = discord.Intents.default()
intents.members = True

#Prefixes
def get_prefix(client, message):
  try:
    with open('prefixes.json', 'r') as f:
      prefixes = json.load(f)
    try:
      return prefixes[str(message.guild.id)]
    except:
      with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

      prefixes[str(message.guild.id)] = '.'

      with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)
      return prefixes[str(message.guild.id)]
  except:
    pass

# sERVER SHARDING AUTOSHARD IS CHANGED WITHOUT IT || fixed

client = commands.AutoShardedBot(shard_count=1, command_prefix=(get_prefix), intents = intents)


@client.event
async def on_ready():
    # if skip == True:
    #     skip = False
    gameover1=True

    await client.change_presence(status=discord.Status.idle, activity=discord.Game(name = '🚀https://teamastro.ml/'))

    print('ASTRO IS READY')
    print(str(client.shards))
    print(str(client.latencies))




import json
@client.event
async def on_message(msg):


  with open("mutedUsers.json","r") as f:
    users = json.load(f)

 
  try:
    for server in users[str(msg.author.id)]["mute"]:
      if server==msg.guild.id:
        embed = discord.Embed(title="My Apologies "+msg.author.name+" You Have Been Muted.", colour=discord.Color.gold(), timestamp=datetime.utcnow())
        embed.set_author(name="Astro", url="https://teamastro.ml/", icon_url=f"{client.user.avatar_url}")

        embed.set_thumbnail(url=f"{client.user.avatar_url}")

        embed.set_footer(text="Team Astro", icon_url=f"{client.user.avatar_url}")
        embed.add_field(name="You Have Been Muted By A Mod, Thus You Cannot Speak.", value="Talk To A Mod For More Info", inline=False)
        try:
          await msg.author.send(embed=embed)
        except:
          pass
        await msg.delete()
        return
  except:
    pass
  with open("mutedUsers.json","w") as f:
    json.dump(users,f)
  
  if msg.author.id==503649934625472544:
    try:
      pass
      # await msg.channel.send("😐")
    except:
      pass
      # await msg.delete
      return

  # if "lol" in msg.content.lower() or "lmao" in msg.content.lower() or "lmfao" in msg.content.lower():

  words=[]
  with open("swearWords.json","r") as f:
    users = json.load(f)
  try:
    for word in users[str(msg.guild.id)]["words"]:
      if word in msg.content.lower():
        words.append(word)
  except:
    pass
  
  if len(words)>0:
    embed = discord.Embed(title="In Order To Create A more Appropriate Environment, Astro Has Deleted Your Message", colour=discord.Color.gold(), timestamp=datetime.utcnow())
    embed.set_author(name="Astro", url="https://teamastro.ml/", icon_url=f"{client.user.avatar_url}")

    embed.set_thumbnail(url=f"{client.user.avatar_url}")

    embed.set_footer(text="Team Astro", icon_url=f"{client.user.avatar_url}")

    for element in words:
      embed.add_field(name="Your Message contained:", value="'"+element.title()+"'", inline=False)
    embed.add_field(name="Astro is hoping to make chats and channels a safer and better place for all!", value="Learn more at https://teamastro.ml", inline=False)
    wordslist=""
    i=0
    try:
      for element in users[str(msg.guild.id)]["words"]:
        i=i+1
        if i==len(users[str(msg.guild.id)]["words"]):
          wordslist = wordslist +element.title()
        else:
          wordslist = wordslist +element.title()+", "
    except:
      pass
    embed.add_field(name="Refraining from using the words below, as messages containing any of these words will be automatically deleted.", value=wordslist, inline=False)

    profaneAmount=0
    import profanity
    for element in words:
      if profanity.contains_profanity(element):
        profaneAmount+=1;
    
    if profaneAmount>0:
      if profanity.contains_profanity(msg.content):
        try:
          await msg.author.send(embed=embed)
        except:
          pass
        await msg.delete()
    else:
      try:
        await msg.author.send(embed=embed)
      except:
        pass
      await msg.delete()


    
    try:
      await msg.author.send(embed=embed)
    except:
      pass
    # await msg.author.send("Hello, In an effort to create a less toxic environment, Astro is moderating words that are deemed explicit or innapropriate by the server. Please know that this is meant to detoxify an environment!") #NON embed
    # await msg.delete()
  
  await client.process_commands(msg)




import discord
from discord.ext import commands
import random


player1 = ""
player2 = ""
turn = ""
gameover1 = True

board = []

winningConditions = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]




@client.command(aliases=['listMute','muted','Muted','Listmute'])
async def listmute(ctx):
  with open("mutedUsers.json","r") as f:
    users = json.load(f)
  embed = discord.Embed(title="Currently Muted Users In "+ctx.guild.name, colour=discord.Color.gold(), timestamp=datetime.utcnow())
  embed.set_author(name="Astro", url="https://teamastro.ml/", icon_url=f"{client.user.avatar_url}")

  embed.set_thumbnail(url=f"{client.user.avatar_url}")

  embed.set_footer(text="Team Astro", icon_url=f"{client.user.avatar_url}")

  try:
    for userobj in users:
      for server in users[str(userobj)]["mute"]:
        if server==ctx.guild.id:
          user = await client.fetch_user(int(userobj))
          embed.add_field(name=user.name, value="Status: Mute", inline=False)
  except:
    pass
  await ctx.send(embed=embed)





@client.command(aliases=['unMute','Unmute'])
@commands.has_permissions(administrator=True)
async def unmute(ctx, memb: discord.Member, time=None):
  if memb.guild_permissions.administrator:
    await ctx.send("> Mods Cannot Mute/Unmute or Unmute Mods/Admins.")
    return
  if (ctx.guild.owner == memb):
    await ctx.send("> You Cannot Mute/Unmute A Mod/Admin Or An Owner.")
    return
  print("hi")
  if time != None:
    print("time used")
    seconds = 0
    try:
      if time.lower().endswith("d"):
          seconds += int(time[:-1]) * 60 * 60 * 24
          counter = f"{seconds // 60 // 60 // 24} days"
      if time.lower().endswith("h"):
          seconds += int(time[:-1]) * 60 * 60
          counter = f"{seconds // 60 // 60} hours"
      elif time.lower().endswith("m"):
          seconds += int(time[:-1]) * 60
          counter = f"{seconds // 60} minutes"
      elif time.lower().endswith("s"):
          seconds += int(time[:-1])
          counter = f"{seconds} seconds"
    except:
      return
    await ctx.send(memb.mention+" Is Unmuted For "+counter.title()+" By "+ctx.author.mention)
    await unMute_person(memb, ctx.guild.id)
    print(seconds)
    await asyncio.sleep(seconds)
    print(seconds)
    await unMute_person(memb, ctx.guild.id)
    await ctx.send(memb.mention+" Has Been Muted Once Again.")
    return
  print("unmuted")
  print(ctx.guild.id)
  await unMute_person(memb, ctx.guild.id)
  await ctx.send(memb.mention+" Has Been Unmuted By "+ctx.author.mention)
  # await ctx.send("muted")




@client.command(aliases=['Mute','silence','Silence'])
@commands.has_permissions(administrator=True)
async def mute(ctx, memb: discord.Member, time=None):
  if (ctx.guild.owner == memb):
    await ctx.send("> You Cannot Mute/Unmute A Mod/Admin Or An Owner.")
    return
  if memb.guild_permissions.administrator:
    await ctx.send("Mods Cannot Mute Mods/Admins.")
    return
  print("hi")
  if time != None:
    print("time used")
    seconds = 0
    try:
      if time.lower().endswith("d"):
          seconds += int(time[:-1]) * 60 * 60 * 24
          counter = f"{seconds // 60 // 60 // 24} days"
      if time.lower().endswith("h"):
          seconds += int(time[:-1]) * 60 * 60
          counter = f"{seconds // 60 // 60} hours"
      elif time.lower().endswith("m"):
          seconds += int(time[:-1]) * 60
          counter = f"{seconds // 60} minutes"
      elif time.lower().endswith("s"):
          seconds += int(time[:-1])
          counter = f"{seconds} seconds"
    except:
      return
    await ctx.send(memb.mention+" Has Been Muted By "+ctx.author.mention+" For "+counter.title())
    await mute_person(memb, ctx.guild.id)
    print(seconds)
    await asyncio.sleep(seconds)
    print(seconds)
    await unMute_person(memb, ctx.guild.id)
    await ctx.send(memb.mention+" Has Been Unmuted And Can Speak Now Because The Mute Countdown Has Elapsed.")
    return
  print("muted")
  print(ctx.guild.id)
  await mute_person(memb, ctx.guild.id)
  await ctx.send(memb.mention+" Has Been Muted By "+ctx.author.mention)
  # await ctx.send("muted")


  


@client.command()
async def tictactoe(ctx, p1: discord.Member, p2: discord.Member):
    global count
    global player1
    global player2
    global turn
    global gameover1

    if gameover1:
        global board
        board = [":white_large_square:", ":white_large_square:", ":white_large_square:",
                 ":white_large_square:", ":white_large_square:", ":white_large_square:",
                 ":white_large_square:", ":white_large_square:", ":white_large_square:"]
        turn = ""
        gameover1 = False
        count = 0

        player1 = p1
        player2 = p2

        # print the board
        line = ""
        for x in range(len(board)):
            if x == 2 or x == 5 or x == 8:
                line += " " + board[x]
                await ctx.send(line)
                line = ""
            else:
                line += " " + board[x]

        # determine who goes first
        num = random.randint(1, 2)
        if num == 1:
            turn = player1
            await ctx.send("It is <@" + str(player1.id) + ">'s turn.")
        elif num == 2:
            turn = player2
            await ctx.send("It is <@" + str(player2.id) + ">'s turn.")
    else:
        await ctx.send("A game is already in progress! Finish it before starting a new one.")

@client.command()
async def place(ctx, pos: int):
    global turn
    global player1
    global player2
    global board
    global count
    global gameover1

    if not gameover1:
        mark = ""
        if turn == ctx.author:
            if turn == player1:
                mark = ":regional_indicator_x:"
            elif turn == player2:
                mark = ":o2:"
            if 0 < pos < 10 and board[pos - 1] == ":white_large_square:" :
                board[pos - 1] = mark
                count += 1

                # print the board
                line = ""
                for x in range(len(board)):
                    if x == 2 or x == 5 or x == 8:
                        line += " " + board[x]
                        await ctx.send(line)
                        line = ""
                    else:
                        line += " " + board[x]

                checkWinner(winningConditions, mark)
                print(count)

                if gameover1 == True:
                    await ctx.send(mark + " wins!")
                elif count >= 9:
                    gameover1 = True
                    await ctx.send("It's a tie!")

                # switch turns
                if turn == player1:
                    turn = player2
                elif turn == player2:
                    turn = player1
            else:
                await ctx.send("Be sure to choose an integer between 1 and 9 (inclusive) and an unmarked tile.")
        else:
            await ctx.send("It is not your turn.")
    else:
        await ctx.send("Please start a new game using the !tictactoe command.")


def checkWinner(winningConditions, mark):
    global gameover1
    for condition in winningConditions:
        if board[condition[0]] == mark and board[condition[1]] == mark and board[condition[2]] == mark:
            gameover1 = True

@client.command(aliases=['cleartictactoe','stoptictatoe','stoptictactoegame'])
async def endtictactoegame(ctx):
  global gameover1
  gameover1 = True
  await ctx.send("Game ended!")



client.remove_command("help")

@client.command()
async def help(ctx):
  embed = discord.Embed(title="Commands", colour=discord.Color.gold(), timestamp=datetime.utcnow())

  embed.set_author(name="Astro", url="https://teamastro.ml/", icon_url=f"{client.user.avatar_url}")


  embed.set_footer(text="Team Astro", icon_url=f"{client.user.avatar_url}")

  embed.add_field(name="Music 🎵", value="Play,\nPause,\nPlayurl,\nResume,\nSkip,\nLyrics,\nQueue,\nListqueue,\nRemove,\nClearqueue", inline=True)
  embed.add_field(name="Moderation 📶", value="Kick,\nBan,\nInvite,\nAuto Moderation Features,\nMute,\nUnmute,\nMuted", inline=True)
  embed.add_field(name="Games 🎯", value="8ball,\nTictactoe,\nRock Paper Scissors(playrps),\nDungeon Crawler", inline=True)
  embed.add_field(name="Productivity/Work ⚒", value="Reminder,\nTimer,\nPolltimes,\nPoll,\nSearchyt,\nYoutube,\nGoogle,\nGooglelinks,\nWiki,\nAgenda,\nMeeting,\nTasks,\nListtasks,\nCleartasks,\nTeamtask,\nListteamtasks,\nDeletetask\nListteamtasks", inline=True)
  embed.add_field(name="Live Data 📈", value="Time,\nWeather,\nCovid,\nUserinfo", inline=True)
  embed.add_field(name="Fun 🎉", value="Meme,\nTictactoe,\nReddit,\nJoke,\n**| THE DUNGEON GAME |**", inline=True)

  await ctx.send(embed=embed)
  



@client.command(aliases=['Setup','quickstart','beginSetup'])
async def setup(ctx):
  await on_guild_join(ctx.guild)

@client.event
async def on_guild_remove(guild): #when the bot is removed from the guild
    with open('prefixes.json', 'r') as f: #read the file
      prefixes = json.load(f)

    prefixes.pop(str(guild.id)) #find the guild.id that bot was removed from

    with open('prefixes.json', 'w') as f: #deletes the guild.id as well as its prefix
      json.dump(prefixes, f, indent=4)



@client.event
async def on_guild_join(guild):
  with open('prefixes.json', 'r') as f: #read the prefix.json file
    prefixes = json.load(f) #load the json file

    prefixes[str(guild.id)] = '.'#default prefix

    with open('prefixes.json', 'w') as f: #write in the prefix.json "message.guild.id": "bl!"
      json.dump(prefixes, f, indent=4) #the indent is to make everything look a bit neater
    
    for channel in guild.text_channels:
        if channel.permissions_for(guild.me).send_messages:
            await channel.send('> Hi, I am Astro! Thanks For Inviting Me To '+guild.name+'!'+" To Start Using Me, I Have To Walk You Through My Set Up Process! I have sent a DM to the owner of the server, to begin the setup process! For A Full List Of My Commands use the help command!".title())
            try:
              await guild.owner.send('> Hi, I am Astro! Thanks For Inviting Me To '+guild.name+'!'+" To Start Using Me, I Have To Walk You Through My Set Up Process! Type The Server Name To Proceed!")
            except:
              await channel.send('> '+guild.owner.mention+" Doesnt Seem to Be Accepting Messages...")
            msg = await client.wait_for('message')
            while(msg.content.lower()!=guild.name.lower() ):
              msg = await client.wait_for('message')
            await guild.owner.send("> Excellent!")
            await asyncio.sleep(1)

            await guild.owner.send("> 1. Start by letting me know what words you would like to moderate in your server. These words will be automatically deleted if sent. Words should be seperated by a ', '. In addition to that, include your server name at the beginning of your msg(eg: <server name> word1, word2, word3) Do not worry, you can always change this later by using the setup command to walk through this process again!".title())
            
            swearWordsMsg= await client.wait_for('message')
            while(guild.name.lower() not in swearWordsMsg.content.lower()):
              msg = await client.wait_for('message')
            swearWordsMsgContent=swearWordsMsg.content.replace(guild.name.lower()+" ",'')

            swearWordsArr = swearWordsMsgContent.split(", ")
            await add_server_swear(guild.id , swearWordsArr)
            await guild.owner.send("Cool! Your Moderated Words Are Now: "+str(swearWordsArr))
            # await guild.owner.send("> 2. Give Astro Admin. In Order to do this, create a new role and check the admin box at the bottom under the permissions section. Then add that role to Astro. If you already have the role created, skip the first step. In Order for proto to moderate it needs admin!".title())
            await asyncio.sleep(1)
            await guild.owner.send("Thats all for now! Remember, Use The .Setup Command To Walk through this again, and change your setup.".title())
            return

            
        break

async def add_server_swear(server, swearWordsArr):

  with open("swearWords.json","r") as f:
    users = json.load(f)
  if str(server) in users:
    for element in swearWordsArr:
      users[str(server)]["words"]=swearWordsArr
  else:
    users[str(server)]= {}
    users[str(server)]["words"]=swearWordsArr
  with open("swearWords.json","w") as f:
    json.dump(users,f)


async def mute_person(user, server):
  if user.id==809609861456723988:
    return
  with open("mutedUsers.json","r") as f:
    users = json.load(f)
  if str(user.id) in users:
    if server not in users[str(user.id)]["mute"]:
      users[str(user.id)]["mute"].append(server)
  else:
    users[str(user.id)]= {}
    users[str(user.id)]["mute"]=[]
    users[str(user.id)]["mute"].append(server)
  with open("mutedUsers.json","w") as f:
    json.dump(users,f)
  print("hi")
  # return True

async def unMute_person(user, server):
  with open("mutedUsers.json","r") as f:
    users = json.load(f)
  print(users[str(user.id)]["mute"])
  print("given server "+str(server))
  users[str(user.id)]["mute"].remove(server)

  with open("mutedUsers.json","w") as f:
    json.dump(users,f)
  # return True




mainshop = [ #MESSAGE TO CODE READERS |||| THIS FEAUTURE IS COMING SOON, DID NOT HAVE ENOUGH TIME TO IMPLEMENT AT HACKATHON.
            #useless items
            {"name":"Mi 11 Ultra","price":10000000000000,"description":"Useless","damage":0},
            {"name":"Laptop","price":1000,"description":"Useless","damage":0},
            {"name":"PC","price":10000,"description":"Useless","damage":0},


            

            #weapons
            {"name":"Knife","price":20000,"description":"Weapon","damage":5},
            {"name":"Wooden Sword","price":1000,"description":"Weapon","damage":10},
            {"name":"Stone Sword","price":4000,"description":"Weapon","damage":20},
            {"name":"Iron Sword","price":10000,"description":"Weapon","damage":40},
            {"name":"Steel Sword","price":15000,"description":"Weapon","damage":60},
            {"name":"Daggers","price":20000,"description":"Weapon","damage":75},
            {"name":"Diamond Sword","price":30000,"description":"Weapon","damage":90},
            {"name":"Pistol","price":50000,"description":"Weapon","damage":110},
            {"name":"Deagle","price":100000,"description":"Weapon","damage":155},
            {"name":"Rifle","price":200000,"description":"Weapon","damage":175},
            {"name":"Gandalf Staff","price":1000000000000,"description":"Weapon","damage":300},
            {"name":"Sauron Ring","price":1000000000000000,"description":"Weapon","damage":499},

            #armor

            {"name":"Mini","price":500,"description":"Armor","damage":0,"armor":25},
            {"name":"50 pot","price":4000,"description":"Armor","damage":0,"armor":50},
            {"name":"100 shield","price":15000,"description":"Armor","damage":0,"armor":100},
            



            #healables
            {"name":"Bandage","price":250,"description":"Healable","damage":-10,"armor":0},
            {"name":"Mini Med Kit","price":1000,"description":"Healable","damage":-25,"armor":0},
            {"name":"Med Kit","price":2500,"description":"Healable","damage":-100,"armor":0},    
            {"name":"Holy Grail","price":1000000000000000000,"description":"Healable","damage":-499,"armor":0},
            ]


import asyncio



@client.command(case_insensitive = True, aliases = ["meeting", "summary", "meetingSummary", 'summarizeMeeting'])
@commands.bot_has_permissions(attach_files = True, embed_links = True)
async def _meetingSummary(ctx,*, question):
  author = ctx.message.author
  author_name = author.name
  print(question)
  if " " not in question and ", " not in question and "," not in question:
    await ctx.send("> You have not included the topics/items from the meeting. Remember seperate your topics like so: topic1, topic2, topic3, etc... Make sure to use commas. ")
    return
  questiona = question
  if "," in question and ", " not in question:
    questiona = question.replace(',', ', ')

  questionArr = questiona.split(", ")
  
  questiona = ""
  for i in range(len(questionArr)):
    if i != len(questionArr)-1:
      questiona = questiona + questionArr[i]+", "
    else:
      questiona = questiona + questionArr[i]
  await ctx.send(author.mention+" Please give the summary for this meeting.")
  msg = await client.wait_for('message')
  summary = msg.content
  await ctx.send("@everyone")
  embed=discord.Embed(title="Meeting Summary From " +author_name.title(), description= "Topics/Summary", color=0xFF5733, timestamp=datetime.utcnow())

  embed.set_author(name="Astro", url="https://teamastro.ml/", icon_url=f"{client.user.avatar_url}")

    # Add rs/608778878835621900/76e69643d799ee584dd46afa91127105.webp")

  embed.set_thumbnail(url="https://cdn.iconscout.com/icon/free/png-256/meeting-1543488-1305981.png")
  i=0
  for element in questionArr:
    i=i+1
    embed.add_field(name="Topic "+str(i)+":", value= str(element).title() , inline=False)

  embed.add_field(name="Summary:", value= summary , inline=False)
  # embed.add_field(name="URL:", value = final_url , inline=False) 

  await ctx.send(embed = embed)




@client.command(case_insensitive = True, aliases = ["timer", "Timer", "timeit"])
@commands.bot_has_permissions(attach_files = True, embed_links = True)
async def _timer(ctx, time):
    reminder = ""
    print(time)
    print(reminder)
    user = ctx.message.author
    embed = discord.Embed(color=0x55a7f7, timestamp=datetime.utcnow())
    embed.set_footer(text="Team Astro | https://teamastro.ml/", icon_url=f"{client.user.avatar_url}")
    embed.set_footer(text="Team Astro", icon_url=f"{client.user.avatar_url}")
    seconds = 0
    if reminder is None:
        embed.add_field(name='Warning', value='Please specify what do you want me to remind you about.') # Error message
    if time.lower().endswith("d"):
        seconds += int(time[:-1]) * 60 * 60 * 24
        counter = f"{seconds // 60 // 60 // 24} days"
    if time.lower().endswith("h"):
        seconds += int(time[:-1]) * 60 * 60
        counter = f"{seconds // 60 // 60} hours"
    elif time.lower().endswith("m"):
        seconds += int(time[:-1]) * 60
        counter = f"{seconds // 60} minutes"
    elif time.lower().endswith("s"):
        seconds += int(time[:-1])
        counter = f"{seconds} seconds"
    if seconds == 0:
        embed.add_field(name='No Duration',
                        value='Please specify a proper duration, send `help` for more information.')
    elif seconds < 1:
        embed.add_field(name='Too Short Duration',
                        value='You have specified a too short duration!\nMinimum duration is 5 minutes.')
    elif seconds > 7776000:
        embed.add_field(name='Too Long Duration', value='You have specified a too long duration!\nMaximum duration is 90 days.')
    else:
        rem = str(f"Timer for {counter} set!")
        embed.add_field(name='Timer Set', value=rem)
        await ctx.send(embed=embed)
        await asyncio.sleep(seconds)
        desc = str(f"Your timer for {counter} has finished.")
        embeded=discord.Embed(title="Timer ",colour=discord.Color.gold(), url="https://timer.com", description=desc, timestamp=datetime.utcnow())

        # Add author, thumbnail, fields, and footer to the embed
        embeded.set_author(name="Astro", url="https://teamastro.ml/", icon_url=f"{client.user.avatar_url}")

        embeded.set_thumbnail(url="https://cdn4.iconfinder.com/data/icons/small-n-flat/24/calendar-512.png")

        embeded.add_field(name="Timer:" , value=counter, inline=False) 
        await ctx.send(embed=embeded)
        return
    await ctx.send(embed=embed)



@client.command(case_insensitive = True, aliases = ["remind", "remindme", "remind_me"])
@commands.bot_has_permissions(attach_files = True, embed_links = True)
async def reminder(ctx, time, *, reminder):
    print(time)
    print(reminder)
    user = ctx.message.author
    embed = discord.Embed(color=0x55a7f7, timestamp=datetime.utcnow())
    embed.set_footer(text="Team Astro", icon_url=f"{client.user.avatar_url}")
    embed.set_footer(text="Team Astro", icon_url=f"{client.user.avatar_url}")
    seconds = 0
    if reminder is None:
        embed.add_field(name='Warning', value='Please specify what do you want me to remind you about.') # Error message
    if time.lower().endswith("d"):
        seconds += int(time[:-1]) * 60 * 60 * 24
        counter = f"{seconds // 60 // 60 // 24} days"
    if time.lower().endswith("h"):
        seconds += int(time[:-1]) * 60 * 60
        counter = f"{seconds // 60 // 60} hours"
    elif time.lower().endswith("m"):
        seconds += int(time[:-1]) * 60
        counter = f"{seconds // 60} minutes"
    elif time.lower().endswith("s"):
        seconds += int(time[:-1])
        counter = f"{seconds} seconds"
    if seconds == 0:
        embed.add_field(name='No Duration',
                        value='Please specify a proper duration, send `help` for more information.')
    elif seconds < 1:
        embed.add_field(name='Too Short Duration',
                        value='You have specified a too short duration!\nMinimum duration is 5 minutes.')
    elif seconds > 7776000:
        embed.add_field(name='Too Long Duration', value='You have specified a too long duration!\nMaximum duration is 90 days.')
    else:
        rem = str(f"Astro will remind you about '{reminder}'' in {counter}.")
        embed.add_field(name='Reminder Set', value=rem)
        await ctx.send(embed=embed)
        await asyncio.sleep(seconds)
        desc = str(f"You asked me to remind you about '{reminder}' {counter} ago.")
        embeded=discord.Embed(title="Reminder ",colour=discord.Color.gold(), url="https://timer.com", description=desc, timestamp=datetime.utcnow())

        # Add author, thumbnail, fields, and footer to the embed
        embeded.set_author(name="Astro", url="https://teamastro.ml/", icon_url=f"{client.user.avatar_url}")

        embeded.set_thumbnail(url="https://cdn4.iconfinder.com/data/icons/small-n-flat/24/calendar-512.png")

        embeded.add_field(name="Reminder:" , value=reminder.title(), inline=False) 
        await ctx.send(embed=embeded)
        return
    await ctx.send(embed=embed)

@client.command(aliases = [ 'Kick'])
@commands.has_permissions(kick_members = True)
@commands.has_permissions(kick_members = True)
async def kick(ctx, member : discord.Member, *, reason="No reason provided" ):
  try:
    await member.send("You have been kicked because: " + reason + ". Join here again: https://discord.gg/5vRAW6wRX8")
  except:
    pass
  await member.kick(reason=reason)
  await ctx.send(f'> {member.mention} Has Been Kicked By '+ctx.author.mention)

@client.command(aliases = ['ban', 'Ban'])
@commands.has_permissions(ban_members = True)
# @commands.has_permissions(ban_members = True)
async def _ban(ctx, member : discord.Member, *, reason="No reason provided" ):
  try:
    await member.send(member.mention+" You Have Been Banned From "+ctx.guild.name+". Reason: " + str(reason) + ". Contact an Admin or Mod or whoever banned you to join again".title())
  except:
    pass
  await ctx.guild.ban(member, reason=reason)
  await ctx.send(f'> {member.mention} Has Been Banned By '+ctx.author.mention)

@client.command(aliases=['inv','Invite','Inv'])
async def invite(ctx, userToInvite: discord.Member):
  # try:
  # userToInvite=userToInvite.replace("#",'')
  link = await ctx.channel.create_invite(max_age = 300)
  # print(userToInvite)
  # target_user = await client.fetch_user(userToInvite)
  # print(target_user.name)
  await userToInvite.send(str(link))
  await ctx.send(str(userToInvite.mention+" Has Been Invited By "+ ctx.author.mention))
  # except:
  #   await ctx.send(ctx.author.mention+" Please Give The User's Tag Like so #1111")




@client.command()
async def joke(ctx):
  await ctx.send(pyjokes.get_joke() + " 😂😂😂")


@client.command(aliases= ['hi','sup','whatsup', 'Hi', 'Sup', 'HI'])
async def _hi(ctx):
  await ctx.send('> Sup...')


@client.command(aliases = ['meme','reddit','imgur','Meme','Reddit', 'Imgur'])
async def _meme( ctx, *, sub):
  reddit = praw.Reddit(client_id = 'b6zkTf4V07VdCA',
                     client_secret = 'RrI3uvddWXLNj-CneA4Pot65hl36Pw', 
                     user_agent = 'aoztanirBot')
  print(sub) 
  # subreddit = self.reddit.subreddit(sub.replace(' ', ''))
  print(sub) 
  # posts = subreddit.hot(limit=10)
  try:
    meme = reddit.subreddit(sub.replace(" ", '')).random()
  except:
    await ctx.send("> Subreddit/images on subreddit not found...")

  if meme.over_18:
    # channel_nsfw = await self.is_nsfw(ctx.message.channel)
    if ctx.channel.is_nsfw():
      pass
    else:
      await ctx.send("> You are not in an NSFW channel.")
      return
  print(meme.url)
  embed=discord.Embed(title=str(meme.title).title()+" From r/"+sub+" By: "+str(meme.author).title(),colour=discord.Color.gold(), url="https://reddit.com", description="Here is your image:", timestamp=datetime.utcnow())

  # Add author, thumbnail, fields, and footer to the embed
  embed.set_author(name="Astro", url="https://teamastro.ml/", icon_url=f"{client.user.avatar_url}")

  embed.set_thumbnail(url="https://external-preview.redd.it/iDdntscPf-nfWKqzHRGFmhVxZm4hZgaKe5oyFws-yzA.png?auto=webp&s=38648ef0dc2c3fce76d5e1d8639234d8da0152b2")
  embed.set_image(url=meme.url)

  embed.add_field(name="Image Link:" , value=str(meme.url), inline=False) 

  embed.add_field(name="Image Stats:", value="🚀 "+ str(meme.upvote_ratio*100)+"% | 👍 "+str(meme.score)+" | 💭 "+str(meme.num_comments), inline=False)
  await ctx.send(embed=embed)

  

@client.command(aliases= ['unban', 'Unban'])
@commands.has_permissions(ban_members = True)
@commands.has_permissions(ban_members = True)
async def _unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'{user.mention} Has Been Unbanned By '+ctx.author.mention)

@client.event
async def on_member_join(ctx, member):
    # print(f'{member} has joined the ship :D !')
    await ctx.send(f'{member} Has Joined The Server.')

@client.event
async def on_member_remove(ctx, member):
    # print(f'{member} went out the airlock :D !')
    await ctx.send(f'{member} Has Left The Server.')

@client.command()
async def ping(ctx):
    await ctx.send(f'> Pong! {round(client.latency*100)}ms!')





#FUNCTIONAL ||||||||| CANNOT RUN WHILE TRYING TO TEST ERRORS SO LEFT IT COMMENTED.
# @client.event
# async def on_command_error(ctx, error):
#     if isinstance(error, discord.ext.commands.MissingRequiredArgument):
#       await ctx.send("> Please include all required parts of a command. For example when using the clear command type the number of msgs to clear.\n > **In addition if using the play command to resume songs     ||||    DO NOT DO THIS. USE THE RESUME COMMAND INSTEAD**")
  
@client.command()
async def bye(ctx):
  await ctx.send("Bye!")


@client.command(aliases = ["news", "headlines","News","Headlines", 'headline', 'Headline'])
async def _news(ctx, amount):
    # await ctx.send("How many headlines?")
    # msg = await client.wait_for('message')
    hNum = int(amount)
    if hNum > 16:
        await ctx.send("Headline amounts cannot be over 15")
        return
    news_url="https://news.google.com/news/rss"
    Client=urlopen(news_url)
    xml_page=Client.read()
    Client.close()
    soup_page=soup(xml_page,"lxml")
    news_list=soup_page.findAll("item")
    hNum=int(hNum)
    try:
        hNum += 1
    except TypeError:
        hNum=6

    embed=discord.Embed(title="Your "+str(hNum)+ " Headlines Are Ready!",colour=discord.Color.gold(), url="https://news.google.com", description="Here are your headlines:", timestamp=datetime.utcnow())

    # Add author, thumbnail, fields, and footer to the embed
    embed.set_author(name="Astro", url="https://teamastro.ml/", icon_url=f"{client.user.avatar_url}")

    embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/0/0b/Google_News_icon.png")

    headlineNum = 0
    for news in news_list[:int(hNum-1)]:
      headlineNum = headlineNum+1
      embed.add_field(name="Headline "+ str(headlineNum) , value=str(news.title.text), inline=False) 

    await ctx.send(embed=embed)
    
    # for news in news_list[:int(hNum-1)]:
    #     await ctx.send(news.title.text)




@client.command(aliases = ["googlelinks", "Googlelinks","googleLinks","searchLinks", "searchlinks", "Searchlinks"])
async def _googleLinks(ctx, *, searchstr: str):
  query = searchstr
  embed=discord.Embed(title="Your 10 Results Are Ready!",colour=discord.Color.gold(), url="https://google.com", description="Here are your results:", timestamp=datetime.utcnow())

    # Add author, thumbnail, fields, and footer to the embed
  embed.set_author(name="Astro", url="https://teamastro.ml/", icon_url=f"{client.user.avatar_url}")

  embed.set_thumbnail(url="http://assets.stickpng.com/images/5847f9cbcef1014c0b5e48c8.png")

  headlineNum = 0
  for j in search(query, tld="co.in", num=10, stop=10, pause=2):
    headlineNum = headlineNum+1
    embed.add_field(name="Result "+ str(headlineNum) + ":", value=str(j), inline=False) 

  await ctx.send(embed=embed)
  # for j in search(query, tld="co.in", num=10, stop=10, pause=2): 
  #     await ctx.send(j) 

@client.command(aliases = ["google","Google", "search", "Search"])
async def _google(ctx, *, searchstr: str):
  query = searchstr
  results = []
  for j in search(query, tld="co.in", num=10, stop=10, pause=2): 
      results.append(j)
    
  embed=discord.Embed(title="Your Result Is Ready!",colour=discord.Color.gold(), url="https://google.com", description="Below is a link that could help you out", timestamp=datetime.utcnow())

    # Add author, thumbnail, fields, and footer to the embed
  embed.set_author(name="Astro", url="https://teamastro.ml/", icon_url=f"{client.user.avatar_url}")

  embed.set_thumbnail(url="http://assets.stickpng.com/images/5847f9cbcef1014c0b5e48c8.png")
  embed.add_field(name="The 1st URL Found on Google:" , value=results[0], inline=False)
  embed.add_field(name="To Get 10 Links:" , value="Use the googlelinks command with your query!", inline=False)

  await ctx.send(embed=embed)
  # await ctx.send("Here is a link that could help you out: " +results[0]+ "\nUse the googlelinks with the same query command for 10 similar links!")

@client.command()
# @commands.has_permissions(administrator=True, manage_messages=True)
async def clear(ctx):
  await ctx.send("Please use ..clear or a keyword in front of clear instead of just clear, this is to prevent the clearing of messages unintentionally.")

@client.command(aliases = ['keyword', 'Keywords','keywords','Keyword', 'prefixes', 'Prefixes'])
async def _keyword(ctx):
  await ctx.send("> KEYWORDS/COMMAND PREFIXES:   '.',  'pls', 'astro', '', ' '. ")


@client.command(aliases = [".clear", ".Clear", "pls clear", 'Pls clear'])
@commands.has_permissions(administrator=True, manage_messages=True)
async def _clear(ctx, *, amount):
    await ctx.channel.purge(limit = int(amount)+1)


@client.command(aliases = ['time', 'Time','now', 'Now'])
async def _time(ctx, inside, city):
  # city.replace('in', '');
  print(city)
  if "europe" in city.lower() or "athens" in city.lower():
    city = "Europe/Athens"
  if "asia" in city.lower() or "kolkata" in city.lower():
    city = "Asia/Kolkata"
  if "america" in city.lower() or "new york" in city.lower() or "new_york" in city.lower() or "newyork" in city.lower():
    city = "America/New_York"
  if "us" in city.lower() or "central" in city.lower():
    city = "US/Central"
  if "africa" in city.lower() or "maseru" in city.lower():
    city = "Africa/Maseru"

  try:
    xyz = pytz.timezone(city)
  except:
    await ctx.send("You have not named a valid time zone, please try again and name one of these Asia/Kolkata, America/New_York, Africa/Maseru, US/Central, Europe/Athens.")
  current_time = datetime.now(xyz) 
  print(current_time)  
    #### Create the initial embed object ####
  embed=discord.Embed(title="Current Time", url="https://time.is/", description="This time is the current time in "+ str(xyz), color=discord.Color.gold(), timestamp=datetime.utcnow())

  # Add author, thumbnail, fields, and footer to the embed
  embed.set_author(name="Astro", url="https://teamastro.ml/", icon_url=f"{client.user.avatar_url}")

  embed.set_thumbnail(url="https://www.patriotsoftware.com/wp-content/uploads/2017/06/time-and-half-1.jpg")

  embed.add_field(name="Time in "+ str(xyz), value=str(current_time.hour)+":"+str(current_time.minute), inline=False) 

  await ctx.send(embed=embed)


@client.command(aliases = ['weather', 'Weather','Temperature', 'temperature'])
async def _weather(ctx, *, city):  #temps
    api_key = "d4b4b3505a923d073e0e9ffd3cd1a606"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    city_name = city[3:]
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url) 
    x = response.json() 
    if x["cod"] != "404":
        y = x["main"]
        current_temperature = y["temp"]
        current_pressure = y["pressure"]
        current_humidiy = y["humidity"]
        z = x["weather"] 
        weather_description = z[0]["description"]
        
        embed=discord.Embed(title="Weather In "+city_name.title(), url="https://weather.com", description="Weather information for "+city_name.title(), color=discord.Color.gold(), timestamp=datetime.utcnow())

      # Add author, thumbnail, fields, and footer to the embed
        embed.set_author(name="Astro", url="https://teamastro.ml/", icon_url=f"{client.user.avatar_url}")

        embed.set_thumbnail(url="https://icons-for-free.com/iconfiles/png/512/fog+foggy+weather+icon-1320196634851598977.png")

        embed.add_field(name="Temperature(F):", value= str(int((current_temperature-273.15) * (9/5) +32)) + " Degrees(F)", inline=False) 
        embed.add_field(name="Atmospheric Pressure(hPa)", value= str(current_pressure) +" hPa", inline=False)
        embed.add_field(name="Humidity Percentage", value=str(current_humidiy) + "%", inline=False)
        embed.add_field(name="Weather Description:", value=str(weather_description).title(), inline=False)

        # embed.set_footer(text="This is the footer. It contains text at the  bottom of the embed")
        await ctx.send(embed=embed)

    else:
        await ctx.send(" City Not Found ")

@client.command(aliases = ['wiki', 'Wiki'])
async def _wiki(ctx, *, topic):
  #wiki api to parse
    ny = wikipedia.page(topic)
    
    
    embed=discord.Embed(title="Wikipedia Results For "+topic.title(), url="https://wikipedia.com", description="This is the result of your query.", color=discord.Color.gold(), timestamp=datetime.utcnow())

  # Add author, thumbnail, fields, and footer to the embed
    embed.set_author(name="Astro", url="https://teamastro.ml/", icon_url=f"{client.user.avatar_url}")

    embed.set_thumbnail(url="http://pngimg.com/uploads/wikipedia/wikipedia_PNG12.png")

    embed.add_field(name="Wikipedia Result:", value=ny.content[:500]+"...", inline=False) 

    await ctx.send(embed=embed)



@client.command()
async def listqueue(ctx):
    await ctx.send(QueList)

@client.command(aliases = ['Percentage','percentage','percent','Percent','amount','Amount'])
async def _percentage(ctx, member: discord.Member,*, question):
  author = ctx.message.author
  author_name = author.name
  if "?" in question:
    question = question.remove("?")
  # await ctx.send(question.title())
  embed=discord.Embed(title="Percentage " + question.title()+" For "+member.name.title(), description= "Asked By: "+str(author_name).title(), color=discord.Color.gold(), timestamp=datetime.utcnow())

    # Add author, thumbnail, fields, and footer to the embed
  embed.set_author(name="Astro", url="https://teamastro.ml/", icon_url=f"{client.user.avatar_url}")

  embed.set_thumbnail(url="https://static.wikia.nocookie.net/fortnite_esports_gamepedia_en/images/f/ff/Onepercent.png/revision/latest?cb=20201110033035")

  embed.add_field(name="Percentage "+ question.title()+":", value = str(rando.randint(1,100))+"%" , inline=False)
  embed.add_field(name="Can I Trust This Answer?", value= "These amounts are 100% correct and are the result of a complex AI algorithm that analyzes your activities on discord." , inline=False)
  # embed.add_field(name="URL:", value = final_url , inline=False) 

  await ctx.send(embed = embed)
@client.command(aliases = ['pollTimes', 'Polltimes','whencanyoucome','when', 'When'])
async def polltimes(ctx, *, question):
  author = ctx.message.author
  author_name = author.name
  if " " not in question and ", " not in question and "," not in question:
    await ctx.send("> You have not included the times. Remember seperate your times like so: 1:30, 1, 2, etc... Make sure to use commas or spaces. ")
    return
  questiona = question
  if "," in question and ", " not in question:
    questiona = question.replace(',', ', ')
  if " " in question and ", " not in question:
    questiona = question.replace(' ', ', ')
  print(questiona)
  questionArr = questiona.split(", ")
  for i in range(len(questionArr)):
    if ":" not in questionArr[i]:
      questionArr[i] = questionArr[i]+":00"
  # questiona = ""
  for i in range(len(questionArr)):
    if i != len(questionArr)-1:
      questiona = questiona + questionArr[i]+", "
    else:
      questiona = questiona + questionArr[i]

  embed=discord.Embed(title="Polling Times: " + questiona.title(), description= "Asked By: "+str(author_name).title(), color=0xFF5733, timestamp=datetime.utcnow())

  embed.set_author(name="Astro", url="https://teamastro.ml/", icon_url=f"{client.user.avatar_url}")

    # Add rs/608778878835621900/76e69643d799ee584dd46afa91127105.webp")

  embed.set_thumbnail(url="https://icons.iconarchive.com/icons/dtafalonso/android-lollipop/512/Clock-icon.png")

  embed.add_field(name="Times:  ", value= questiona.title() , inline=False)
  embed.add_field(name="Remember:", value= "All polling amounts must be subtracted by one for each, since it was reacted to once already by Astro." , inline=False)
  # embed.add_field(name="URL:", value = final_url , inline=False) 

  await ctx.send(embed = embed)
  
  for element in questionArr:
    embed=discord.Embed(title="Time: " + element.title(), color=0xFF5733)
    messageSent = await ctx.send(embed = embed)
    await messageSent.add_reaction("✅")


@client.command()
async def poll(ctx, *, question):
  author = ctx.message.author
  author_name = author.name
  if "?" not in question:
    question = question +"?"
  # await ctx.send(question.title())
  embed=discord.Embed(title="Poll: " + question.title(), description= "Asked By: "+str(author_name).title(), color=0xFF5733, timestamp=datetime.utcnow())

    # Add rs/608778878835621900/76e69643d799ee584dd46afa91127105.webp")

  embed.set_thumbnail(url="https://image.flaticon.com/icons/png/512/1946/1946385.png")
  embed.set_author(name="Astro", url="https://teamastro.ml/", icon_url=f"{client.user.avatar_url}")

  embed.add_field(name="Question:", value= question.title() , inline=False)
  embed.add_field(name="Remember:", value= "Polling amounts must be subtracted by one for each, since it was reacted to once already by Astro." , inline=False)
  # embed.add_field(name="URL:", value = final_url , inline=False) 

  messageSent = await ctx.send(embed = embed)
  await messageSent.add_reaction("✅")
  await messageSent.add_reaction("❌")

@client.command()
async def resume(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        voice.resume()
    else:
        await ctx.send("The audio is not paused.")

def playtheurl(ctx, url):
    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
    except PermissionError:
        
        return

    if not ctx.message.author.voice:
        
        return
    
    else:
        voiceChannel = ctx.message.author.voice.channel
    
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            os.rename(file, "song.mp3")
    voice.play(discord.FFmpegPCMAudio("song.mp3"))


@client.command()
async def playurl(ctx, url : str):
    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
    except PermissionError:
        await ctx.send("Wait for the current playing music to end or use the 'stop' command")
        return

    if not ctx.message.author.voice:
        await ctx.send("You are not connected to a voice channel")
        return
    
    else:
        await ctx.send("Joining...")
        voiceChannel = ctx.message.author.voice.channel
        await voiceChannel.connect()
    
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            os.rename(file, "song.mp3")
    voice.play(discord.FFmpegPCMAudio("song.mp3"))

@client.command()
async def queue(ctx, *, mysong: str):
    result = VideosSearch(mysong.replace(' ',''), limit = 1).result()['result']
    INDEX = 0
    print(result[INDEX]['link'])
    final_url = result[INDEX]['link']

    video = pafy.new(final_url)
    vidLength =  int(video.length)
    print(vidLength)
    if vidLength > 600:
        await ctx.send("This video cannot be added to the queue because it is longer than 10 min.")
        return
    if final_url in QueList:
      await ctx.send("This song has already been added to the queue, wait for it to be played before adding it again.")
      return
    QueList.append(final_url)
    embed=discord.Embed(title="A New Song Has Been Queued, Use The Play Command To Play!", url=final_url, description= mysong.title() +" Has been Queued!", color=0xFF5733, timestamp=datetime.utcnow())

    # Add author, thumbnail, fields, and footer to the embed
    embed.set_author(name="Astro", url="https://teamastro.ml/", icon_url=f"{client.user.avatar_url}")

    embed.set_thumbnail(url="https://cdn.iconscout.com/icon/free/png-512/spotify-11-432546.png")

    embed.add_field(name="Song Name:", value= mysong.title() , inline=False)
    embed.add_field(name="URL:", value = final_url , inline=False) 

    await ctx.send(embed = embed)
    await ctx.send(final_url)
    # await ctx.send("Qued!\nSong Name: " + mysong.title() + ".\nURL: " + final_url)

@client.command()
async def removeSong(ctx, *, mysong: str):
    result = VideosSearch(mysong.replace(' ',''), limit = 1).result()['result']
    INDEX = 0
    print(result[INDEX]['link'])
    final_url = result[INDEX]['link']

    video = pafy.new(final_url)
    vidLength =  int(video.length)
    QueList.remove(final_url)
    await ctx.send(mysong.title() + " has been removed")

@client.command()
async def removeteamtask(ctx, *, mysong: str):
  try:
    TaskList.remove(mysong.title())
  except:
    await ctx.send("Your task list is either empty, or there is nothing under the name provided.")
    
  await ctx.send(mysong.title() + " has been removed")



@client.command()
# @commands.has_permissions(ban_members = True)
async def clearqueue(ctx):
    await ctx.send("Cleared !")
    QueList.clear()

@client.command()
# @commands.has_permissions(ban_members = True)
async def cleartasks(ctx):
    await ctx.send("Cleared !")
    TaskList.clear()


    
    
@client.command()
async def play(ctx, *, mysong: str):
    try:
      voiceChannel = ctx.message.author.voice.channel
      voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    except:
      pass

    try:
        voice_client = ctx.message.guild.voice_client
        await voice_client.disconnect()
    except AttributeError:
        pass

    if not ctx.message.author.voice:
        await ctx.send("> You are not connected to a voice channel.")
        return

    else:
        await ctx.send("Joining...")
        
        await voiceChannel.connect()

    song_there = os.path.isfile("song.mp3")
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    try:
        if song_there:
            os.remove("song.mp3")
    except PermissionError:
        await ctx.send("Next time, please wait for the current playing music to end or use the 'stop' command")
        # return

    if len(mysong) < 2:
        await ctx.send("Please include the title of the song after the .play command or a larger length song. -help for more info")
        return

    if not ctx.message.author.voice:
        await ctx.send("You are not connected to a voice channel")
        return

    else:
        pass

    if mysong == "queue" or mysong =="que":
        if len(QueList)==0:
            await ctx.send("the queue is empty")
            return
    if mysong != "queue" and mysong != "que":
        INDEX = 0

        result = VideosSearch(mysong.replace(' ',''), limit = 1).result()['result']

        print(result[INDEX]['link'])
        final_url = result[INDEX]['link']
        video = pafy.new(final_url)
        vidLength =  int(video.length)

        print(vidLength)
        if vidLength > 600:
            await ctx.send("This video cannot be played because it is longer than 10 min. Select or queue another song...")
            return
    
    if  mysong != "queue" and mysong != "que":
        embed=discord.Embed(title="A New Song Is Playing!", url=final_url, description= mysong.title() +" Is Playing!", color=0xFF5733, timestamp=datetime.utcnow())

        # Add author, thumbnail, fields, and footer to the embed
        embed.set_author(name="Astro", url="https://teamastro.ml/", icon_url=f"{client.user.avatar_url}")

        embed.set_thumbnail(url="https://cdn.iconscout.com/icon/free/png-512/spotify-11-432546.png")

        embed.add_field(name="Song Name:", value= mysong.title() , inline=False)
        embed.add_field(name="URL:", value = final_url , inline=False) 

        await ctx.send(embed = embed)
        await ctx.send(final_url)
        # await ctx.send(final_url)
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([final_url])
        for file in os.listdir("./"):
            if file.endswith(".mp3"):
                os.rename(file, "song.mp3")
        voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
        voice.play(discord.FFmpegPCMAudio("song.mp3"))
    else:
        voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
        embed=discord.Embed(title="The Queue Has Started Playing!", url=QueList[0], description= "Astro will now play songs from the queue, use the skip command to skip songs, and the stop command to stop playing from the queue.", color=0xFF5733, timestamp=datetime.utcnow())

        # Add author, thumbnail, fields, and footer to the embed | example from medium.com on embeds
        embed.set_author(name="Astro", url="https://teamastro.ml/", icon_url=f"{client.user.avatar_url}")

        embed.set_thumbnail(url="https://cdn.iconscout.com/icon/free/png-512/spotify-11-432546.png")

        embed.add_field(name="To See The Queue:", value= "Use the listqueue command." , inline=True)
        embed.add_field(name="To Skip:", value = "Use the Skip Command." , inline=True)
        embed.add_field(name="To Play A New Song:", value = "Use the Play Command." , inline=True)
        embed.add_field(name="To Stop Entirely:", value = "Use the Stop Command." , inline=True) 
        embed.add_field(name="For More Info:", value = "Use the Help Command." , inline=True)   

        await ctx.send(embed = embed)
        await ctx.send(QueList[0])

        global ctxSave
        if ctxSave is None:
            ctxSave = ctx
        isplaying()

skipCount = 0
@client.command()
async def skip(ctx):
    global skipCount
    skipCount = skipCount + 1
    if skipCount % 2 == 0:
        print("this time we are running the pop")
        QueList.pop(0)

    else:
        await ctx.send("Skipping(please type .skip twice to confirm a skip)")
        return
    
    server = ctx.message.guild
    voice_channel = server.voice_client
    voice_channel.stop()
    voice_client = ctx.message.guild.voice_client
    await voice_client.disconnect()
    voiceChannel = ctx.message.author.voice.channel
    await voiceChannel.connect()
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)

    print(skipCount)
    
    if len(QueList) == 0:
        await ctx.send("Queue is empty 😢")
        server = ctx.message.guild
        voice_channel = server.voice_client
        voice_channel.stop()
        voice_client = ctx.message.guild.voice_client
        await voice_client.disconnect()
        return
    else:
        global ctxSave
        if ctxSave:
            ctxSave = ctx
        isplaying()
    # skip2(ctx)

def skip2(ctx):

    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    # QueList.pop(0)
    if len(QueList) == 0:

        return
    else:
        global ctxSave
        if ctxSave is None:
            ctxSave = ctx
        isplaying()



class isplaying(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.daemon = True
        self.start()
    def run(self):
        while len(QueList) != 0:
            playtheurl(ctxSave, QueList[0])
            video = pafy.new(QueList[0])
            vidLength =  int(video.length)
            voice = discord.utils.get(client.voice_clients, guild=ctxSave.guild)
            # while voice.is_playing():
            #     voice = discord.utils.get(client.voice_clients, guild=ctxSave.guild)
            time.sleep(vidLength)
            QueList.pop(0)
        return
            # voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
            # isplaying()
            # QueList.pop(0)

class isplaying2(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.daemon = True
        self.start()
    def run(self):
        while len(QueList) != 0:
            playtheurl(ctxSave, QueList[0])
            video = pafy.new(QueList[0])
            vidLength =  int(video.length)
            voice = discord.utils.get(client.voice_clients, guild=ctxSave.guild)
            while voice.is_playing():
                voice = discord.utils.get(client.voice_clients, guild=ctxSave.guild)
            time.sleep(vidLength)
            QueList.pop(0)
        return
            # voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
            # isplaying()
            # QueList.pop(0)
        

@client.command()
async def pause(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
    else:
        await ctx.send("Currently no audio is playing.")

@client.command(aliases = ['stop', 'Stop' , 'leave', 'Leave'])
async def _stop(ctx):
  #for vc's

    await ctx.send("Stopping...")
    server = ctx.message.guild
    voice_channel = server.voice_client
    voice_channel.stop()
    voice_client = ctx.message.guild.voice_client
    await voice_client.disconnect()


@client.command(aliases=['tracktotal','trackcovidtotal','Covidtotal','Coronatotal','coronatotal','Coronavirustotal','coronavirustotal','Covid19total''trackCovidtotal','CovidTracktotal','covidtotal'])
async def covidTrackertotal(ctx):
  

  # Format: <Data Source>.<Location>.<Statistic>
  # For example to get data from John Hopkins University, review the following example:
  # JHU.China.deaths
  import covid19_data  

  embed=discord.Embed(title="Covid Stats", description= "Covid Statistics Scraped from Johns Hokins Research Center", color=0xFF5733, timestamp=datetime.utcnow())

  # Add author, thumbnail, fields, and footer to the embed
  embed.set_author(name="Astro", url="https://teamastro.ml/", icon_url=f"{client.user.avatar_url}")

  embed.set_thumbnail(url="https://www.psycharchives.org/retrieve/096175aa-f7f2-4970-989d-d934c30b5551")

  embed.add_field(name="The Number of COVID-19 Recoveries: ", value=str(JHU.Total.recovered) , inline=False)
  embed.add_field(name="The Number of Worldwide COVID-19 Cases: ", value = str(JHU.Total.deaths) , inline=False)
  embed.add_field(name="The Number of Worldwide COVID-19 Deaths: ", value = str(JHU.Total.deaths) , inline=False)

  await ctx.send(embed = embed)

  #print stuff for covid nums //dhruv debug agghhhhhhh
  print("The number of COVID-19 recoveries in the US: " + str(JHU.US.recovered))
  print("The number of confirmed COVID-19 cases in Texas: " + str(JHU.Texas.confirmed))
  print("The number of COVID-19 deaths in California: " + str(JHU.California.deaths))
  print("The number of worldwide COVID-19 deaths: " + str(JHU.Total.deaths))
  print("The number of COVID-19 deaths in China: " + str(JHU.China.deaths))
  print("The number of COVID-19 deaths in UK: " + str(JHU.UnitedKingdom.deaths))





async def create_task_user(user):
  with open("tasks.json","r") as f:
    users = json.load(f)
  if str(user.id) in users:
    return False
  else:
    users[str(user.id)]= {}
    users[str(user.id)]["tasks"]=[]
  with open("tasks.json","w") as f:
    json.dump(users,f)
  return True




@client.command(case_insensitive = True, aliases = ["task", "Task", "taskfor"])
async def taskFor(ctx, memb: discord.Member, *, task:str):
  
  await ctx.send("When Is This Task Due?")
  dueDatea = await client.wait_for('message')
  dueDate=dueDatea.content
  taskName="Task: "+task.title()+" | Due: "+dueDate.title()

  embed = discord.Embed(title=memb.name+" Has Been Assigned A New Task!", description = taskName, colour=discord.Color.gold(), timestamp=datetime.utcnow())
  embed.set_author(name="Astro", url="https://teamastro.ml/", icon_url=f"{client.user.avatar_url}")


  await create_task_user(memb)
  with open("tasks.json","r") as f:
    users = json.load(f)
  users[str(memb.id)]["tasks"].append(taskName)
  with open("tasks.json","w") as f:
    json.dump(users,f)
  
  embed.set_thumbnail(url=f"{memb.avatar_url}")

  embed.set_footer(text="Team Astro", icon_url=f"{client.user.avatar_url}")
  embed.add_field(name="All Of Your Tasks Are Listed Below:", value="Tasks Below", inline=False)
  with open("tasks.json","r") as f:
    users = json.load(f)
  for i in range(len(users[str(memb.id)]["tasks"])):
    embed.add_field(name="Task "+str(int(i)+1), value = str(users[str(memb.id)]["tasks"][i]), inline=False)

  try:
    await memb.send(embed=embed)
  except:
    await ctx.send(memb.mention+" is not accepting dm's, so here is their task.")
    await ctx.send(embed=embed)
    return
  await ctx.send(memb.mention+" has been assigned a new task, check your DM for all your tasks.")

@client.command(case_insensitive = True, aliases = ["removeTask", "removetask", "deleteTask"])
async def deletetask(ctx, memb: discord.Member, taskNum=None):
  if taskNum==None:
    await ctx.send("Specify the task number.")
    return
  await create_task_user(memb)
  with open("tasks.json","r") as f:
    users = json.load(f)
  try:
    users[str(memb.id)]["tasks"].pop(int(int(taskNum)-1))
  except:
    await ctx.send("Name a valid number to remove")
    return
  with open("tasks.json","w") as f:
    json.dump(users,f)
  await ctx.send("Removed task number "+str(int(taskNum))+" for " + memb.mention+"!")
  

@client.command(case_insensitive = True, aliases = ["listtasks", "listtask", "listTaskfor"])
async def listTasks(ctx, memb: discord.Member):

  embed = discord.Embed(title="Tasks For "+memb.name, description = "Task List Below", colour=discord.Color.gold(), timestamp=datetime.utcnow())
  embed.set_author(name="Astro", url="https://teamastro.ml/", icon_url=f"{client.user.avatar_url}")

  
  embed.set_thumbnail(url=f"{memb.avatar_url}")

  embed.set_footer(text="Team Astro", icon_url=f"{client.user.avatar_url}")
  embed.add_field(name="All Of "+memb.name+ " Tasks Are Listed Below:", value="Tasks Below", inline=False)
  await create_task_user(memb)
  with open("tasks.json","r") as f:
    users = json.load(f)
  for i in range(len(users[str(memb.id)]["tasks"])):
    embed.add_field(name="Task "+str(int(i)+1), value = str(users[str(memb.id)]["tasks"][i]), inline=False)
  await ctx.send(embed=embed)
  await memb.send(embed=embed)
  























@client.command(case_insensitive = True, aliases = ["taskList", "teamTask", "teamtasks", 'teamTaskList','teamtasklist','teamTasks'])
@commands.bot_has_permissions(attach_files = True, embed_links = True)
async def teamtask(ctx,*, question):
  author = ctx.message.author
  author_name = author.name
  print(question)
  if " " not in question and ", " not in question and "," not in question:
    await ctx.send("> You have not included the topics/items for the task board. Remember seperate your topics like so: topic1, topic2, topic3, etc... Make sure to use commas. ")
    return
  questiona = question
  
  if "," in question and ", " not in question:
    questiona = question.replace(',', ', ')
  # if " " in question and ", " not in question:
  #   questiona = question.replace(' ', ', ')
  questionArr = questiona.split(", ")
  
  questiona = ""
  for i in range(len(questionArr)):
    if i != len(questionArr)-1:
      questiona = questiona + questionArr[i]+", "
    else:
      questiona = questiona + questionArr[i]
  await ctx.send("@everyone")
  embed=discord.Embed(title="Task List Created/Altered By " +author_name.title(), description= "Items", color=0xFF5733, timestamp=datetime.utcnow())

  embed.set_author(name="Astro", url="https://teamastro.ml/", icon_url=f"{client.user.avatar_url}")


  embed.set_thumbnail(url="https://cdn.iconscout.com/icon/free/png-256/meeting-1543488-1305981.png")
  i=0
  for element in questionArr:
    TaskList.append(str(element).title())
  for element in TaskList:
    i=i+1
    embed.add_field(name="Task "+str(i)+":", value= str(element).title() , inline=False)


  await ctx.send(embed = embed)

@client.command()
async def listteamtasks(ctx):
  author = ctx.message.author
  author_name = author.name
  await ctx.send("@everyone")
  embed=discord.Embed(title="Task List Created/Altered By " +author_name.title(), description= "Items", color=0xFF5733, timestamp=datetime.utcnow())

  embed.set_author(name="Astro", url="https://teamastro.ml/", icon_url=f"{client.user.avatar_url}")


  embed.set_thumbnail(url="https://cdn.iconscout.com/icon/free/png-256/meeting-1543488-1305981.png")
  i=0
  for element in TaskList:
    i=i+1
    embed.add_field(name="Task "+str(i)+":", value= str(element).title() , inline=False)

  await ctx.send(embed=embed)
    


@client.command(aliases=['track', 'corona', 'Corona', 'Covid','Covid19','covid19'])
async def covid(ctx, stateName):
  import covid19_data  

  # Format: <Data Source>.<Location>.<Statistic>
  # For example to get data from John Hopkins University, review the following example:
  # JHU.China.deaths

  abrev=False

  try:
    state = covid19_data.dataByName(stateName.replace(' ',''))
  except:
    if True:
      abrev = True
    try:
      state = covid19_data.dataByNameShort(stateName.replace(' ',''))
    except:
      await ctx.send("> State Could Not Be Found")
      return
  if abrev == True:
    embed=discord.Embed(title="Covid Stats For "+stateName.upper(), description= "Covid Statistics Scraped from Johns Hokins Research Center", color=0xFF5733, timestamp=datetime.utcnow())
    # Add author, thumbnail, fields, and footer to the embed
    embed.set_author(name="Astro", url="https://teamastro.ml/", icon_url=f"{client.user.avatar_url}")

    embed.set_thumbnail(url="https://www.psycharchives.org/retrieve/096175aa-f7f2-4970-989d-d934c30b5551")

    embed.add_field(name="The Number of COVID-19 Recoveries in "+stateName.title()+":", value=str(state.recovered) , inline=False)
    embed.add_field(name="The Number of Cases in "+stateName.title(), value = str(state.cases) , inline=False)
    embed.add_field(name="The Number of Deaths in "+stateName.title(), value = str(state.deaths) , inline=False)

    await ctx.send(embed = embed)
    return
  if abrev == False:
    embed=discord.Embed(title="Covid Stats For "+stateName.title(), description= "Covid Statistics Scraped from Johns Hokins Research Center", color=0xFF5733, timestamp=datetime.utcnow())
    # Add author, thumbnail, fields, and footer to the embed
    embed.set_author(name="Astro", url="https://teamastro.ml/", icon_url=f"{client.user.avatar_url}")

    embed.set_thumbnail(url="https://www.psycharchives.org/retrieve/096175aa-f7f2-4970-989d-d934c30b5551")

    embed.add_field(name="The Number of COVID-19 Recoveries in "+stateName.title()+":", value=str(state.recovered) , inline=False)
    embed.add_field(name="The Number of Cases in "+stateName.title(), value = str(state.cases) , inline=False)
    embed.add_field(name="The Number of Deaths in "+stateName.title(), value = str(state.deaths) , inline=False)

    await ctx.send(embed = embed)

#\CODE READERS, THIS IS OUR KEEP_ALIVE FILE... THIS ESSENTIALLY RUNS A SERVER USING FLASK AND KEEPS IT ALIVE ASYNCHRONOUSLY ON A THREAD |||| THIS IS HOW WE KEEP THE BOT RUNNING AND HOSTED ON REPL.IT. FOR MORE INFO GO TO https://teamastro.ml
keep_alive.keep_alive()

#CODE READERS THIS IS HOW WE RUN OUR BOT ON DISCORDS API... THE TOKEN BELOW IS OUR CLIENT TOKEN,

#astro
client.run('ODA5NjA5ODYxNDU2NzIzOTg4.YCXl8A._gbKgreGXHV_uGupJ3gZgEqj3Lg')