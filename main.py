import os
import asyncio
import traceback
import sys
from discord.ext import commands
from discord.ext import tasks
from discord.commands import Option
import discord
import os
import random
import requests

from discord.ext.commands.errors import BadLiteralArgument

#TOKEN = os.environ['TOKEN']

    

zulu = commands.Bot(command_prefix = 'z.')

@zulu.event
async def on_ready():
    await zulu.change_presence(activity=discord.Game(name="z.cmds for a list of commands."))
    print('{0.user} is ready'.format(zulu))
    

@zulu.event
async def on_command_error(ctx, error):
     if isinstance(error, commands.CommandNotFound):
      NotFound = discord.Embed(
            title = 'I use slash commands now',
            description = 'I have evolved with discord, i no longer use prefix commands as discord have made a new fancy feature called slash commands, press the `/` key see!',
            colour = discord.Colour.blue()

      )
      NotFound.set_footer(text='I am the best discord bot, you cannot change my mind as i was coded to say this.')


      await ctx.send(embed=NotFound)
      if isinstance(error, commands.MissingPermissions):
        NoPerms = discord.Embed(
            title = 'No permissions!',
            description = 'You do not have permission to do that command!',
            colour = discord.Colour.red()

        )
        NoPerms.set_footer(text='You can\'t do that command')
        NoPerms.set_author(name='You need Permission to run that command.')
        await ctx.send(embed=NoPerms)
      if isinstance(error, UnboundLocalError):
        return
      else:
        raise error

#embed for help command.
helpembed = discord.Embed(
  title = 'Commands List',
  description = 'Here is a list of commands.',
  colour = discord.Colour.blue()
    
  )

helpembed.set_footer(text='This is the best discord bot')
helpembed.set_author(name='ZuluBot commands:')
helpembed.add_field(name='Ping!', value='Shows the ping of the bot')
helpembed.add_field(name='Help', value='Shows this command.')

@zulu.slash_command(guild_ids=[798180194049196032, 764981968579461130])  # create a slash command for the supplied guilds
async def help(ctx):
    """Sends the help command"""  # the command description can be supplied as the docstring
    await ctx.respond(f"Hello <@{ctx.author.id}>!,", embed=helpembed)

@zulu.slash_command(guild_ids=[798180194049196032, 764981968579461130])  # create a slash command for the supplied guilds
async def hello(ctx):
    """Say hello to the bot"""  # the command description can be supplied as the docstring
    await ctx.respond(f"Hello {ctx.author}!")


@zulu.slash_command(guild_ids=[798180194049196032, 764981968579461130])
async def ping(ctx):
  pingtime = round(zulu.latency * 1000)
  pingembed = discord.Embed(
  title = 'Pong!',
  description = 'Ping time:' + (str(pingtime)) + 'ms',
  colour = discord.Colour.blue()

  )

  pingembed.set_footer(text='This is the best discord bot')
 
  await ctx.respond(embed=pingembed)
    
@zulu.slash_command(guild_ids=[798180194049196032, 764981968579461130])
async def srvstatus(
    ctx,
    ip: Option(str, "Enter the server IP", required=True),
):
    r = requests.get(f'https://api.mcsrvstat.us/2/{ip}')
    server_json = r.json()

    await ctx.respond(embed=temprespond)



zulu.run("ODc0MDEyMDg5NzA0OTA2NzUz.YRAxMA.iu6ee1kre4GCqigvTTD1f2gCTgI")
