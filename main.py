import os
try:
	import discord
	from discord.ext import commands
	from colorama import init, Fore;init()
	import requests
except:
	os.system('pip install -U discord.py-self colorama requests')
	import discord
	from discord.ext import commands
	from colorama import init, Fore;init()
	import requests
import json

with open("config.json", "r", encoding="utf-8-sig") as f:
	config = json.load(f)

LALOL=Fore.RED +"""
██╗░░░░░░█████╗░██╗░░░░░░█████╗░██╗░░░░░
██║░░░░░██╔══██╗██║░░░░░██╔══██╗██║░░░░░
██║░░░░░███████║██║░░░░░██║░░██║██║░░░░░
██║░░░░░██╔══██║██║░░░░░██║░░██║██║░░░░░
███████╗██║░░██║███████╗╚█████╔╝███████╗
╚══════╝╚═╝░░╚═╝╚══════╝░╚════╝░╚══════╝
"""
os.system(f'cls && title Selfbot by LALOL' if os.name == 'nt' else 'clear')
print(LALOL)
print(Fore.GREEN + "Selfbot by LALOL\n" + Fore.RED)

pref=config['Prefix']
bot = commands.Bot(command_prefix=pref, case_insensitive=True, self_bot=True)
version=0.1
bot.remove_command('help')

@bot.event
async def on_ready():
	for filename in os.listdir():
		if filename.endswith('.txt'):
			os.remove(filename)
	print(Fore.MAGENTA + f"Аккаунт: {Fore.YELLOW}{bot.user}{Fore.MAGENTA}\nID: {Fore.YELLOW}{bot.user.id}{Fore.MAGENTA}\nPrefix: {Fore.YELLOW}{pref}{Fore.RED}\n")
@bot.event
async def on_command_error(ctx, error):
	if isinstance(error, commands.MissingRequiredArgument):
		print(Fore.RED + f"[ERROR] Недостаточно аргументов!")
	elif isinstance(error, commands.CommandNotFound):
		print(Fore.RED + f"[ERROR] Данной команды не существует!")
	elif isinstance(error, commands.BadArgument):
		print(Fore.RED + f"[ERROR] Неправильный аргумент!")
	else:
		print(Fore.RED + f"[ERROR] {error}")
@bot.command(aliases=['хелп', 'помощь'])
async def help(ctx, cat=None):
	if cat==None:
		await ctx.message.edit(content=f'**__Selfbot by LALOL__\n\n:screwdriver:`{pref}help Tools` - Полезные команды\n:information_source:`{pref}help Info` - Команды для получения информации\n:joy:`{pref}help Fun` - Развлекательные команды\n\n:robot:`{pref}bot` - Получение ссылки на установку селф бота**')
		return
	cat=cat.lower()
	if cat=='tools':
		await ctx.message.edit(content=f'**__Selfbot by LALOL__\n\n`{pref}status [Тип статуса] [Текст]` - Меняет статус**')
	if cat=='info':
		await ctx.message.edit(content=f'**__Selfbot by LALOL__\n\n`{pref}server` - Информация о сервере\n`{pref}user [ID/Пинг]` - Информация об аккаунте**')
	if cat=='fun':
		await ctx.message.edit(content=f'**__Selfbot by LALOL__\n\n`{pref}troll [ID/Пинг]` - Удаление всех сообщений пользователя\n`{pref}untroll` - Выключение команды troll**')
@bot.command(name='bot', aliases=['selfbot', 'бот', 'селфбот'])
async def __bot(ctx):
	await ctx.message.edit(content='**__Selfbot by LALOL__\n\nСсылка: https://github.com/Its-LALOL/Discord-Selfbot**')
for filename in os.listdir("./cogs"):
	if filename.endswith(".py"):
		bot.load_extension(f"cogs.{filename[:-3]}")
try: bot.run(config["Token"])
except:
	while True:
		input("Invalid Token!")
