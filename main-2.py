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
waiting_time = 0
token_present = False


def delete_token_file_contents():
    open('token.txt', 'w').close()


new_token = open('token.txt').read()
print(new_token)


# ---------------------------------------
# Start
# ---------------------------------------
@client.event
async def on_ready():
    print('Bot is ready.')
    servers_list = []
    servers_file = open('servers.txt', 'w')
    user = open('current_user.txt', 'w')
    user.write(str(client.user))

    for server in client.guilds:
        server_id = server.id
        server = str(server)
        server.rstrip('>')
        server.lstrip('<')

        try:
            servers_file.write(f'{server} - {server_id} \n')
        except:
            print(server)

    servers_list = str(servers_list)
    print(servers_list)

    delete_token_file_contents()
    await client.logout()


# ---------------------------------------
# When token.txt is empty, wait
# ---------------------------------------
while len(new_token) == 0:
    new_token = open('token.txt').read()
    time.sleep(1)
    waiting_time += 1
    print(waiting_time)

client.run(new_token, bot=False)
os.system("main-2.py")


