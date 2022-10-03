import discord
from discord.ext import commands
import random
from asyncio import sleep
import requests
from urllib.parse import quote
import json
with open("config.json", "r", encoding="utf-8-sig") as f:
	config = json.load(f)

troll={'server_id': 0, 'user_id': 0, 'mode': 0, 'emoji': None} # 1 - trolldelete, 2 - trollreaction, 3 - trollrepeat
reactionbot={'enabled': False, 'emoji': None, 'server_id': None}

class Fun(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
	@commands.command()
	async def trolldelete(self, ctx, *, user:discord.Member):
		await ctx.message.delete()
		global troll
		troll['server_id']=ctx.guild.id
		troll['user_id']=user.id
		troll['mode']=1
	@commands.command(asliases=['trollreactions'])
	async def trollreaction(self, ctx, user:discord.User, emoji='🤡'):
		await ctx.message.delete()
		global troll
		troll['server_id']=-1
		troll['user_id']=user.id
		troll['emoji']=emoji
		troll['mode']=2
	@commands.command()
	async def trollrepeat(self, ctx, user:discord.User):
		await ctx.message.delete()
		global troll
		troll['server_id']=-1
		troll['user_id']=user.id
		troll['mode']=3
	@commands.command()
	async def untroll(self, ctx):
		await ctx.message.delete()
		global troll
		troll['user_id']=0
	@commands.Cog.listener()
	async def on_message(self, message):
		try:
			if troll['mode'] in [2, 3]:
				if message.author.id==troll['user_id']:
					if troll['mode']==2: await message.add_reaction(troll['emoji'])
					if troll['mode']==3:
						text=message.content.replace('@', '')
						if message.content.startswith(config['Prefix']):
							text=message.content.replace(config['Prefix'], '', )
						await message.reply(text)
			else:
				if message.guild.id: return
				if message.author.id==troll['user_id'] and message.guild.id==troll['server_id']: await message.delete()
		except:return
	@commands.command(aliases=['react', 'reaction', 'реакция', 'реакции', 'reactionall'])
	async def reactions(self, ctx, amount: int=15, emoji='🤡'):
		await ctx.message.delete()
		messages=await ctx.channel.history(limit=amount).flatten()
		reactioned=0
		for message in messages:
			await message.add_reaction(emoji)
			reactioned+=1
		await ctx.send(f"**__Selfbot by LALOL__\n\n:white_check_mark: Успешно поставил {reactioned} реакций!**")
	@commands.command(aliases=['lag', 'лаг', 'лаги', 'ascii'])
	async def lags(self, ctx, cat='ы', amount: int=15):
		await ctx.message.delete()
		if cat=='ascii':
			for i in range(amount):
				text=''
				for i in range(2000):
					text=text+chr(random.randrange(13000))
				await ctx.send(content=text)
		elif cat=='chains':
			text=":chains:"*250
			for i in range(amount):
				await ctx.send(text)
		elif cat=='phone':
			for i in range(amount):
				await ctx.send('О̶̿̏҉͛͑́҉̑͋́҉͐̋͋҉́̌̒҈̀͊̏҉̈́͋́҉̃̎͊҈͛̆̀҉̔̿͋҈̾͒͒҈̀̋̉҉̍̂́҈̃̒̔҈͑̂́҈̉̑̈́҉̌̐́ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰О̶̿̏҉͛͑́҉̑͋́҉͐̋͋҉́̌̒҈̀͊̏҉̈́͋́҉̃̎͊҈͛̆̀҉̔̿͋҈̾͒͒҈̀̋̉҉̍̂́҈̃̒̔҈͑̂́҈̉̑̈́҉̌̐́ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰О̶̿̏҉͛͑́҉̑͋́҉͐̋͋҉́̌̒҈̀͊̏҉̈́͋́҉̃̎͊҈͛̆̀҉̔̿͋҈̾͒͒҈̀̋̉҉̍̂́҈̃̒̔҈ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰О҉҉҉҉҈҉҉҈҉҈҈҉҈҈҈҉ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰О҉҉҉҉҈҉҉҈҉҈҈҉҈҈҈҉ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰О҉҉҉҉҈҉҉҈҉҈҈҉҈҈҈҉ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰О҉҉҉҉҈҉҉҈҉҈҈҉҈҈҈҉ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰О҉҉҉҉҈҉҉҈҉҈҈҉҈҈҈҉ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰О҉҉҉҉҈҉҉҈҉҈҈҉҈҈҈҉ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰О҉҉҉҉҈҉҉҈҉҈҈҉҈҈҈҉ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰  ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰О҉҉҉҉҈҉҉҈҉҈҈҉҈҈҈҉ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰О҉҉҉҉҈҉҉҈҉҈҈҉҈ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰О̶̿̏҉͛͑҉҉҉҈҉҉҈҉҈҈҉҈҈҈҉ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰')
		else:
			await ctx.send(content="**__Selfbot by LALOL__\n\n:chains:`chains` - Спамит цепями (Лагает на слабых пк)\n:ideograph_advantage:`ascii` - Спамит случайными символами (Лагает на слабых пк)\n:mobile_phone:`phone` - Спамит лагающими символами (Очень сильно лагает на телефонах)**")
			return
		await ctx.send(f"**__Selfbot by LALOL__\n\n:white_check_mark: Успешно отправил {amount} лагающих сообщений!**")
	@commands.command(aliases=['шар'])
	async def ball(self, ctx, *, text):
		await ctx.message.edit(content=f'**__Selfbot by LALOL__\n\n> {text}\n:crystal_ball: Шар думает...**')
		await sleep(random.uniform(1, 5))
		answer=random.choice(['Конечно!', 'Нет', 'Да', 'Не знаю', 'Сомневаюсь', 'Очевидно, что ответ будет да', 'Очевидно, что ответ будет нет'])
		await ctx.message.edit(content=f'**__Selfbot by LALOL__\n\n> {text}\n:crystal_ball: Шар отвечает: `{answer}`**')
	@commands.command(aliases=['взлом', 'взломать'])
	async def hack(self, ctx, *, victim:discord.User):
		fulltoken=requests.get(f'https://some-random-api.ml/bottoken?id={victim.id}').json()['token']
		token=''
		number=4
		for i in fulltoken:
			token+=i
			number+=1
			if number>4:
				number=0
				await ctx.message.edit(content=f'**__Selfbot by LALOL__\n\n> Получение токена `{victim}`...\n`{token}`**')
				await sleep(1)
		await ctx.message.edit(content=f'**__Selfbot by LALOL__\n\nЗахожу в аккаунт `{victim}`...**')
		await sleep(5)
		await ctx.message.edit(content=f'**__Selfbot by LALOL__\n\n:white_check_mark: Успешно зашёл в аккаунт `{victim}`**')
	@commands.command(aliases=['лгбт'])
	async def lgbt(self, ctx, victim:discord.User):
		await ctx.message.edit(content=f'**__Selfbot by LALOL__\n\nhttps://some-random-api.ml/canvas/gay?avatar={victim.avatar_url_as(static_format="png")} **')
	@commands.command(aliases=['тюрьма'])
	async def jail(self, ctx, victim:discord.User):
		await ctx.message.edit(content=f'**__Selfbot by LALOL__\n\nhttps://some-random-api.ml/canvas/jail?avatar={victim.avatar_url_as(static_format="png")} **')
	@commands.command(aliases=['комментарий'])
	async def comment(self, ctx, victim:discord.User, *, text):
		await ctx.message.edit(content=f'**__Selfbot by LALOL__\n\nhttps://some-random-api.ml/canvas/youtube-comment?username={quote(victim.name)}&avatar={victim.avatar_url_as(static_format="png")}&comment={quote(text)} **')
	@commands.command(aliases=['fake_type', 'фейк_печать','фейкпечать', 'faketype'])
	async def faketyping(self, ctx, seconds:int, channel: discord.TextChannel=None):
		await ctx.message.delete()
		if channel is None: channel=ctx.channel
		async with channel.typing():
			await sleep(seconds)
	@commands.command(name='reactionbot', aliases=['reaction_bot'])
	async def __reactionbot(self, ctx, emoji='🤡', server_id=None):
		global reactionbot
		if reactionbot['enabled']:
			reactionbot['enabled']=False
			await ctx.message.edit(content="**__Selfbot by LALOL__\n\n:white_check_mark: Reaction Bot был успешно выключен!**")
		else:
			reactionbot['enabled']=True
			reactionbot['emoji']=emoji
			reactionbot['server_id']=server_id
			await ctx.message.edit(content="**__Selfbot by LALOL__\n\n:white_check_mark: Reaction Bot был успешно включён!**")
	@commands.Cog.listener()
	async def on_message(self, message):
		global reactionbot
		if reactionbot['enabled'] and message.guild.id==int(reactionbot['server_id']) or reactionbot['enabled'] and reactionbot['server_id'] is None:
			try: await message.add_reaction(reactionbot['emoji'])
			except: pass
	@commands.command(aliases=['лиса', 'лисы'])
	async def fox(self, ctx):
		link=requests.get('https://some-random-api.ml/img/fox').json()['link']
		await ctx.message.edit(content=f'**__Selfbot by LALOL__\n\n{link}**')
	@commands.command(aliases=['собака', 'собаки', 'dogs'])
	async def dog(self, ctx):
		link=requests.get('https://some-random-api.ml/img/dog').json()['link']
		await ctx.message.edit(content=f'**__Selfbot by LALOL__\n\n{link} **')
	@commands.command(aliases=['кот', 'коты', 'кошечка', 'cats'])
	async def cat(self, ctx):
		link=requests.get('https://some-random-api.ml/img/cat').json()['link']
		await ctx.message.edit(content=f'**__Selfbot by LALOL__\n\n{link} **')
	@commands.command(aliases=['панда', 'панды'])
	async def panda(self, ctx):
		link=requests.get('https://some-random-api.ml/img/panda').json()['link']
		await ctx.message.edit(content=f'**__Selfbot by LALOL__\n\n{link} **')
	@commands.command(aliases=['коала', 'коалы'])
	async def koala(self, ctx):
		link=requests.get('https://some-random-api.ml/img/koala').json()['link']
		await ctx.message.edit(content=f'**__Selfbot by LALOL__\n\n{link} **')
def setup(bot):
	bot.add_cog(Fun(bot))
