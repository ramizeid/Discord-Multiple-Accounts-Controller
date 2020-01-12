import discord
from discord.ext import commands
import datetime
from discord import Webhook, AsyncWebhookAdapter
import aiohttp
import time
import os

# ---------------------------------------------------------
client = commands.Bot(command_prefix='.', self_bot=True)
client.remove_command('help')
start_time = datetime.datetime.utcnow()

TOKEN = 'TOKEN'


# ---------------------------------------
# Bot Initialization
# ---------------------------------------
@client.event
async def on_ready():
    print('Bot is ready.')


# ---------------------------------------
# Change Accounts Command
# ---------------------------------------
accounts = open("accounts.txt").read().splitlines()

accounts_dict = {}

for i in accounts:
    split = i.split(':')
    user = split[0]
    user_token = split[1][1:]

    accounts_dict[user] = user_token

@client.command()
async def account(ctx, *, msg):
    for i in accounts_dict:
        if msg.lower() == i.lower():
            new_token = accounts_dict[i]
            await ctx.send('Account found!')

    token_file = open('token.txt', "w")
    token_file.write(new_token)

    print(new_token)


# ---------------------------------------
# Servers List Command
# ---------------------------------------
@client.command()
async def servers(ctx):
    servers_list = open('servers.txt').read().splitlines()
    current_user = open('current_user.txt').read()

    servers_embed = discord.Embed(
        title=f"{current_user}'s servers",
        color=discord.Color.red(),
        timestamp=datetime.datetime.utcnow()
    )

    for server in servers_list:
        if servers_list.index(server) <= 50:
            server_split_list = server.split('-')
            server_name = server_split_list[0].rstrip(' ')
            server_id = server_split_list[1].lstrip(' ')
            servers_embed.add_field(name=server_name, value=server_id, inline=True)

    await ctx.send(embed=servers_embed)

    if len(servers_list) > 50:
        servers_embed = discord.Embed(
            title=f"{current_user}'s servers",
            color=discord.Color.red(),
            timestamp=datetime.datetime.utcnow()
        )

        for server in servers_list:
            if 50 < servers_list.index(server) <= 100:
                server_split_list = server.split('-')
                server_name = server_split_list[0].rstrip(' ')
                server_id = server_split_list[1].lstrip(' ')
                servers_embed.add_field(name=server_name, value=server_id, inline=True)

        await ctx.send(embed=servers_embed)

client.run(TOKEN, bot=False)
