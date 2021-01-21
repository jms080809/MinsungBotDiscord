import discord
import asyncio
import math
import datetime
import time
from discord.ext import commands
import os
import random


TOKEN = "NzgxMzU0NDI2NzY1NDEwMzE0.X78bBA.c1bTeOKTyd1obYiFbfJQR55AJMc"
token = 'NzcyMzYxOTUwMjE0NjE5MTU3.X55kHg.zhFdqYg87UH_1rrV-ixMYn1FB8Y'


bot = commands.Bot(command_prefix="!")


@bot.event
async def on_ready():
    print("Bot Has been ONLINEd!")
    await bot.change_presence(activity=discord.Game('!와 함께'), status=discord.Status.dnd)


async def 테스트(ctx):
    await ctx.send("아주좋아...\nhttps://tenor.com/view/tyra-banks-hair-flip-sass-gif-5363134")


@bot.command()
async def 핑(ctx):
    await ctx.send('핑 = 약 {}초'.format(math.ceil(bot.latency)))


@bot.command()
async def 핑핑(ctx):
    await ctx.send('핑 = {}초'.format(bot.latency))


@bot.command()
async def 임베드(ctx):
    embed = discord.Embed(colour=discord.Colour.green(),
                          title='제목데수네', description='에엥ㅇ따')
    await ctx.send(embed=embed)


@bot.command()
async def 프로필(message):
    date = datetime.datetime.utcfromtimestamp(
        ((int(message.author.id) >> 22) + 1420070400000) / 1000)
    embed = discord.Embed(colour=0x6f4f28)
    embed.add_field(name="이름", value=message.author.name, inline=False)
    embed.add_field(name='가입일', value=str(date.year) + '/' +
                    str(date.month) + '/' + str(date.day), inline=False)
    embed.add_field(name='ID', value=message.author.id, inline=False)
    embed.set_thumbnail(url=message.author.avatar_url)
    await message.send(embed=embed)


@bot.command()
async def 핑핑이(ctx):
    await ctx.send("https://tenor.com/view/omg-wide-eyes-meow-wow-stunned-gif-15553490")


@bot.command()
async def 시진핑핑이(ctx):
    await ctx.send('https://ext.fmkorea.com/files/attach/new/20190629/486616/1811747998/1945658380/b3fadf45e34bc25637462e285d9c80c6.png')
    time.sleep(2)
    await ctx.send('?')
    time.sleep(1)
    await ctx.send('뭐 이런걸 만들었대')


@bot.command()
async def 샷건(ctx):

    for i in range(1):
        await ctx.send('https://tenor.com/view/bed-slap-hand-gif-16938090')
        await ctx.send('https://tenor.com/view/%EB%AD%89%EC%95%8C-%EC%83%B7%EA%B1%B4-%EB%B0%94%EB%B3%B4-gif-18353073')
        await ctx.send('https://tenor.com/view/%EA%B0%90%EC%8A%A4%ED%8A%B8-gamst-%EC%83%B7%EA%B1%B4-mad-angry-gif-17042099')
        await ctx.send('https://tenor.com/view/%EA%B0%90%EC%8A%A4%ED%8A%B8-%EC%83%B7%EA%B1%B4-gamst-hysterical-eyeglasses-gif-17041752')
        time.sleep(0.5)
        await ctx.send('아싯팔 초능력 맛좀 볼래?', tts=True)


@bot.command()
async def r샷건(ctx):

    for i in range(1):
        await ctx.send('https://tenor.com/view/bed-slap-hand-gif-16938090')
        await ctx.send('https://tenor.com/view/%EB%AD%89%EC%95%8C-%EC%83%B7%EA%B1%B4-%EB%B0%94%EB%B3%B4-gif-18353073')
        await ctx.send('https://tenor.com/view/%EA%B0%90%EC%8A%A4%ED%8A%B8-gamst-%EC%83%B7%EA%B1%B4-mad-angry-gif-17042099')
        await ctx.send('https://tenor.com/view/%EA%B0%90%EC%8A%A4%ED%8A%B8-%EC%83%B7%EA%B1%B4-gamst-hysterical-eyeglasses-gif-17041752')
        time.sleep(0.5)
        await ctx.send('?래볼 좀맛 력능초 팔싯아', tts=True)


@bot.command()
async def 행성(message):
    embed = discord.Embed(title='행성(Strange_ameba)', color=0x437299)
    embed.add_field(name='출처:한국외계생명체연구조합', value='약 M자광년 떨어진 행성에서 온 외계생명체이다. 첫 발견은 경상도 부근에서 이XX씨가 2008년 처음 발견하여 알려지게 되었다. 지능은 딱히 없는 듯 하나, 생김새가 아메바를 닮았다. 자웅동체이며, 번식을 할때 머리에 M자탈모가 생기며, 3년에 한번꼴로 번식을 하는데 드문 경우로 MMORPG탈모가 날 때가 있다. 생명체는 인간에게는 해가 되지 않지만, 그 외모에 걸맞지 않은 징그러운 번식활동때문에 민간인이 통제하기 어렵다 판단하여 국제외계생명준수협회에 의해 임시 격리 상태중. 이 생명을 국제에 맡길지 SCP에 맡길지 현재 국제토론중이다. ')
    embed.set_image(
        url='https://cdn.discordapp.com/avatars/605966157530529802/8f71e4f7a2ff8281a31e633bbaef9d40.png?size=128')
    await message.send(embed=embed)

#'약 M자광년 떨어진 행성에서 온 외계생명체이다. 지능은 딱히 없는 듯 하나, 생김새가 아메바를 닮았다. 자웅동체이며, 번식을 할때 머리에 M자탈모가 생기며, 3년에 한번꼴로 번식을 하는데 드문 경우로 MMORPG탈모가 날 때가 있다. 생명체는 인간에게는 해가 되지 않지만, 국제외계생명준수협회에 의해 구속 상태중. '


@bot.command()
async def 게이(message):
    embed = discord.Embed(description=':Are you gay?(당신은 게이입니까?)',
                          tts=True, color=0x437299, inline=True)
    await message.send(embed=embed)
    await message.channel.send('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR3Wp4D1zG1P633VRXmllX38Nwun4DvXXTEcg&usqp=CAU')


@bot.command()
async def 봇(message):
    date = datetime.datetime.utcfromtimestamp(
        ((int(message.author.id) >> 22) + 1420070400000) / 1000)
    embed = discord.Embed(colour=0x6f4f28)
    embed.add_field(name="이름", value='국밥', inline=False)
    embed.add_field(name='가입일', value=str(date.year) + '/' +
                    str(date.month) + '/' + str(date.day), inline=False)
    embed.add_field(name='ID', value='에엥ㅇ따봇', inline=False)
    embed.set_thumbnail(
        url='https://cdn.discordapp.com/avatars/781354426765410314/3c6099ede71bf90faf37e2fe2c16823c.png?size=128')
    await message.send(embed=embed)


@bot.command()
async def 성부자령D(message):
    await message.channel.send('https://cdn.discordapp.com/attachments/774887554817458182/790759127269244938/M.gif')


@bot.command()
async def 어몽(message):
    tag = "<@{}>".format(message.author.id)
    await message.send('.      　。　　　　•　    　ﾟ　　。')
    time.sleep(1)
    await message.send('　　.　　　.　　　  　　.　　　　　。　　   。　.')
    time.sleep(1)
    await message.send(' 　.　　      。　       ඞ   。　    .    •')
    time.sleep(1)
    await message.send(f' •        {tag} 는 임포스터였습니다 　 。　.')
    time.sleep(1)
    await message.send('　 　　。　　　　　　ﾟ　　　.　　　　　.')
    time.sleep(1)
    await message.send(',　　　　.　 .　　       .               。')


@bot.command()
async def 흠(ctx):
    await ctx.send('''
      ⢀⣀⣀⣀
⠀⠀⠀⠰⡿⠿⠛⠛⠻⠿⣷
⠀⠀⠀⠀⠀⠀⣀⣄⡀⠀⠀⠀⠀⢀⣀⣀⣤⣄⣀⡀
⠀⠀⠀⠀⠀⢸⣿⣿⣷⠀⠀⠀⠀⠛⠛⣿⣿⣿⡛⠿⠷
⠀⠀⠀⠀⠀⠘⠿⠿⠋⠀⠀⠀⠀⠀⠀⣿⣿⣿⠇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠁

⠀⠀⠀⠀⣿⣷⣄⠀⢶⣶⣷⣶⣶⣤⣀
⠀⠀⠀⠀⣿⣿⣿⠀⠀⠀⠀⠀⠈⠙⠻⠗
⠀⠀⠀⣰⣿⣿⣿⠀⠀⠀⠀⢀⣀⣠⣤⣴⣶⡄
⠀⣠⣾⣿⣿⣿⣥⣶⣶⣿⣿⣿⣿⣿⠿⠿⠛⠃
⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄
⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡁
⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁
⠀⠀⠛⢿⣿⣿⣿⣿⣿⣿⡿⠟
⠀⠀⠀⠀⠀⠉⠉⠉''')


@bot.command()
async def 배곰(message):
    await message.channel.send('''  ┻┳|―-∩
    ┳┻|　　ヽ
    ┻┳|　● |
    ┳┻|▼) _ノ
    ┻┳|￣　)
    ┳ﾐ(￣ ／
    ┻┳T￣
    ''')
    time.sleep(1)
    await message.channel.send('''  ┻┳|-∩
    ┳┻|　ヽ
    ┻┳|● |
    ┳┻|) _ノ
    ┻┳|￣)
    ┳ﾐ(￣／
    ┻┳T
    ''')
    time.sleep(1)
    await message.channel.send('''  ┻┳|∩
    ┳┻|ヽ
    ┻┳| |
    ┳┻| _ノ
    ┻┳|)
    ┳ﾐ(／
    ┻┳T
    ''')
    time.sleep(1)
    await message.channel.send('''  ┻┳|
    ┳┻|
    ┻┳|
    ┳┻|
    ┻┳|
    ┳ﾐ(
    ┻┳T
    ''')
    time.sleep(1)


@bot.command()
async def 시발(message):
    await message.channel.send('https://scontent-ssn1-1.xx.fbcdn.net/v/t31.0-8/19944455_1964843147084009_5607198638293051316_o.jpg?_nc_cat=105&ccb=2&_nc_sid=9267fe&_nc_ohc=Lh08E-xZdcIAX-U7GSZ&_nc_ht=scontent-ssn1-1.xx&oh=c3b6c002eee4dc5c8fb6f809acb2e375&oe=60073C8C')


@bot.command()
async def 자폭(ctx):
    await ctx.send('https://i.ytimg.com/vi/2TDHrDFQKqc/hqdefault.jpg')
    await ctx.send('깜놀해서 사망')


@bot.command()
async def 오류(ctx):
    await ctx.send('오류 has been planted')


@bot.command()
async def 개발자(ctx):
    paginator = commands.Paginator()
    paginator.add_line('이것이')
    paginator.add_line('개발자 댓글창')
    paginator.add_line('이렇게 씀')
    paginator.add_line(
        '''    paginator = commands.Paginator()
    paginator.add_line('이것이')
    paginator.add_line('개발자 댓글창')
    paginator.add_line('이렇게 씀')
    for page in paginator.pages:
        await ctx.send(page)'''
    )
    for page in paginator.pages:
        await ctx.send(page)


@bot.command()
async def 꼬불(ctx):
    for i in range(5):
        await ctx.send('''
     꼬불꼬불꼬불꼬불
  꼬불꼬불꼬불꼬불
   꼬불꼬불꼬불꼬불
    꼬불꼬불꼬불꼬불
     꼬불꼬불꼬불꼬불
      꼬불꼬불꼬불꼬불
       꼬불꼬불꼬불꼬불
       꼬불꼬불꼬불꼬불
       꼬불꼬불꼬불꼬불
      꼬불꼬불꼬불꼬불
     꼬불꼬불꼬불꼬불
    꼬불꼬불꼬불꼬불
   꼬불꼬불꼬불꼬불
  꼬불꼬불꼬불꼬불
 꼬불꼬불꼬불꼬불
꼬불꼬불꼬불꼬불
꼬불꼬불꼬불꼬불
꼬불꼬불꼬불꼬불
 꼬불꼬불꼬불꼬불
  꼬불꼬불꼬불꼬불
   꼬불꼬불꼬불꼬불
    꼬불꼬불꼬불꼬불
     꼬불꼬불꼬불꼬불
      꼬불꼬불꼬불꼬불
       꼬불꼬불꼬불꼬불
       꼬불꼬불꼬불꼬불
       꼬불꼬불꼬불꼬불
      꼬불꼬불꼬불꼬불
     꼬불꼬불꼬불꼬불
    꼬불꼬불꼬불꼬불
   꼬불꼬불꼬불꼬불
  꼬불꼬불꼬불꼬불
 꼬불꼬불꼬불꼬불
꼬불꼬불꼬불꼬불
꼬불꼬불꼬불꼬불      
  꼬불꼬불꼬불꼬불
   꼬불꼬불꼬불꼬불
    꼬불꼬불꼬불꼬불
     꼬불꼬불꼬불꼬불
      꼬불꼬불꼬불꼬불
       꼬불꼬불꼬불꼬불
       꼬불꼬불꼬불꼬불
       꼬불꼬불꼬불꼬불
      꼬불꼬불꼬불꼬불
     꼬불꼬불꼬불꼬불
    꼬불꼬불꼬불꼬불
   꼬불꼬불꼬불꼬불
  꼬불꼬불꼬불꼬불
 꼬불꼬불꼬불꼬불
꼬불꼬불꼬불꼬불
꼬불꼬불꼬불꼬불
꼬불꼬불꼬불꼬불
 꼬불꼬불꼬불꼬불
  꼬불꼬불꼬불꼬불
   꼬불꼬불꼬불꼬불
    꼬불꼬불꼬불꼬불
     꼬불꼬불꼬불꼬불
      꼬불꼬불꼬불꼬불
       꼬불꼬불꼬불꼬불
       꼬불꼬불꼬불꼬불
       꼬불꼬불꼬불꼬불
      꼬불꼬불꼬불꼬불
     꼬불꼬불꼬불꼬불
    꼬불꼬불꼬불꼬불
   꼬불꼬불꼬불꼬불
  꼬불꼬불꼬불꼬불
 꼬불꼬불꼬불꼬불
꼬불꼬불꼬불꼬불
꼬불꼬불꼬불꼬불      
  꼬불꼬불꼬불꼬불
   꼬불꼬불꼬불꼬불
    꼬불꼬불꼬불꼬불
     꼬불꼬불꼬불꼬불
      꼬불꼬불꼬불꼬불
       꼬불꼬불꼬불꼬불
       꼬불꼬불꼬불꼬불
       꼬불꼬불꼬불꼬불
      꼬불꼬불꼬불꼬불
     꼬불꼬불꼬불꼬불
    꼬불꼬불꼬불꼬불
   꼬불꼬불꼬불꼬불
  꼬불꼬불꼬불꼬불
 꼬불꼬불꼬불꼬불
꼬불꼬불꼬불꼬불
꼬불꼬불꼬불꼬불
꼬불꼬불꼬불꼬불
 꼬불꼬불꼬불꼬불
  꼬불꼬불꼬불꼬불
   꼬불꼬불꼬불꼬불
    꼬불꼬불꼬불꼬불
     꼬불꼬불꼬불꼬불
      꼬불꼬불꼬불꼬불
       꼬불꼬불꼬불꼬불
       꼬불꼬불꼬불꼬불
       꼬불꼬불꼬불꼬불
      꼬불꼬불꼬불꼬불
     꼬불꼬불꼬불꼬불
    꼬불꼬불꼬불꼬불
   꼬불꼬불꼬불꼬불
  꼬불꼬불꼬불꼬불
 꼬불꼬불꼬불꼬불
꼬불꼬불꼬불꼬불
꼬불꼬불꼬불꼬불      

        ''')
    time.sleep(1)


@bot.command()
async def 옹클(message):
    embed = discord.Embed(colour=0x8b00ff, title='온라인 클래스 4반',
                          description='https://oc11.ebssw.kr/sso/loginView.do?loginType=onlineClass&hmpgId=happy2064')
    await message.send(embed=embed)


@bot.command()
async def 온클(message):
    embed = discord.Embed(colour=0x8b00ff, title='온라인 클래스',
                          description='https://oc11.ebssw.kr/onlineClass/search/onlineClassSearchView.do?schulCcode=05977&schCssTyp=online_poc')
    embed.set_image(
        url='https://t1.daumcdn.net/cfile/tistory/997A26485E8D08C416')
    await message.send(embed=embed)
    time.sleep(2)
    random_int = random.randint(1, 5)
    if random_int == 1:
        await message.send('Brave 브라우저를 써보십시오! Google Chrome과 같은 기반이며,\nAdBlock이 포함되어 주옥 같은 광고들로부터 당신을 섹시하게 지켜줍니다!\n또한 간단한 조작으로 Tor 검색이 가능합니다!\n DuckDuckGo와 함께 섹시한 Brave 브라우저를 경험해보세요!\nhttps://brave.com/ko/download/\n[광고]', tts=True)
    elif random_int == 2:
        await message.send('[광고]씨발브바! X 시.바.브.바!(시대가 바뀌면 브라우저도 바뀌다!)\n살짝만 섹si한 웹서핑을 시작해보십시오!\n이 브라우저는 무료로 핸드폰 사이트를 제공하여 직장에서 핸폰하기 서바이벌 쌉가능입니다!\nhttps://whale.naver.com/ko/', tts=True)
    elif random_int == 3:
        await message.send('[광고]다른 국밥집과 차이가 나는 봇을 제공하는\n행신동1빠따순대봇국밥을 경험해보십시오!\n뜨끈한 국밥 든든하게 드십시오!\n당신에 서버에 국밥집을 차리십시오!\nhttps://bit.ly/2M1ubsr', tts=True)
    elif random_int == 4:
        await message.send('[광고]Night_Bot has been planted!\nGo check NightBot and join your SEXY server! This bot Do for Free!\nhttps://discord.com/streamkit', tts=True)
    else:
        await message.send('광고가 불러와지지 않습니다........', tts=True)


# https://oc11.ebssw.kr/sso/loginView.do?loginType=onlineClass&hmpgId=happy2064
@bot.command()
async def 시팔(ctx):
    await ctx.send('''
    #아나운서:
        여러분 안녕하십니까, 9시 민성뉴스입니다.
        사람들과 가족처럼 지내며 살아가는 동물들, 일명 반려동물,
        실수 혹은 고의로 인해 유기되거나 유실되는 사례가 작년에
        비해 더욱 늘어났습니다.
        전민성 기자가 보도합니다.
    #기자:
        농림축산검역본부는 지난해 지자체를 통해 반려동물 보호와 복지관리 실태에 대해 조사한 결과를 (5월)12일 발표했습니다.
        지난해 신규 등록된 반려견은 79만7천81마리로, 전년보다 443.6% 늘었고,
        지난해까지 등록된 반려견 수는 모두 209만2천163마리로 집계되었습니다.
        하지만 그럼에도 구조·보호 사례는 전년보다 12% 증가한 것으로, 
        지난해 구조·보호 조치된 유실 및 유기동물은 13만5천791마리였고,
        2017년에는 10만2천593마리, 2018년에는 12만1천77마리에 이어 계속 늘었습니다.
        이들 동물 중 26.4%는 분양됐으나, 자연사24.8%, 안락사21.8%한 경우도 절반에 가깝습니다.
        소유주에 인도된 경우는 12.1%이었고 보호 중인 사례는 11.8%였습니다.
        사람들에 노력에도 이만큼이나 많은 유실 및 유기동물이 나왔다는 것이 사람들의 노력과 책임이 더욱 필요한 것으로 보입니다.
        그리고 실수로나 고의로나 동물들을 잃어버리거나 유기됬다는 것은 생명에 대한 책임을 지지 못한 것으로,
        반려동물을 가족으로 들이시기전 다시 한번 '내가 이 생명을 책임지고 끝까지 키울수 있을까' 생각하며 책임을 질수 있을지 없을지
        다시 한번 신중히 고민해보는 밑거름이 되겠습니다.
        민성뉴스 전민성 기자였습니다.
    ''', tts=True)


@bot.command()
async def 크리스마스(message):
    embed = discord.Embed(
        title='징글벨', description='jingle bells', colour=discord.Colour.red())
    embed.add_field(name='lylics', value='''
    It's Christmas
    Jingle bells, jingle bells
    Jingle all the way
    Oh, what fun it is to ride
    In a one horse open sleigh
    Hey, jingle bells, jingle bells
    Jingle all the way
    Oh, what fun it is to ride
    In a one horse open sleigh
    Jingle bells, jingle bells
    Jingle all the way
    Oh, what fun it is to ride
    In a one horse open sleigh
    Hey, jingle bells, jingle bells
    Jingle all the way
    Oh, what fun it is to ride
    In a one horse open sleigh
    It's Christmas
    Hey, jingle bells, jingle bells
    Jingle all the way
    Oh, what fun it is to ride
    In a one horse open sleigh
    Hey, jingle bells, jingle bells
    Jingle all the way
    Oh, what fun it is to ride
    In a one horse open sleigh
    It's Christmas
        ''', inline=False)
    await message.send(embed=embed)
    await message.send('2020크리스마스 즐겁게 보내십시오! 안그러면 뚜까맞을 겁니다! 크리스마스 기념으로 기프티콘 선물을 시행합니다! 선착순 1명!', tts=True)
    await message.send('https://cdn.discordapp.com/attachments/774887554817458182/791572623397879818/3c624be4f328ff51.png')


@bot.command()
async def 이공이일(message):
    link = 'https://mega.nz/file/zM8CDYwT#6kcGW-bpnehJ-Is_iI05SctwbNtfLgjb4jueUTKIF9I'
    embed = discord.Embed(
        title="2020 Bye!", description="2020년을 보내고 새 2021년을 맞이하다!", colour=0xffa500)
    embed.set_thumbnail(
        url="https://image.freepik.com/free-vector/happy-new-2021-year-holiday-illustration-with-festive-typographic-composition-new-year_173043-569.jpg")
    embed.add_field(name="새해 맞이하는 기념으로 Wumpus 한국판 출시!",
                    value=f"아래 링크를 클릭해 text base 게임\nWumpus 사냥하기 를 플레이해보세요!\n{link}", inline=True)
    embed.set_image(
        url="https://www.startupn.kr/news/photo/201912/548_527_327.jpg")
    await message.send(embed=embed)

bot.run(TOKEN)
