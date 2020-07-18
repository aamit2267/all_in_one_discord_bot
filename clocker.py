import discord
from discord.ext import commands
from discord.utils import get
from datetime import datetime
import asyncio
import time

bot=commands.Bot(command_prefix="<")
TOKEN='NzI4OTA3NTkwNDA2NTA0NTQw.XwwFsQ.qOnQd1Dt-2K_tlglBO9FMAHURqc'
bot.remove_command("help")


@bot.event
async def on_ready():
	while True:
		await bot.change_presence(activity=discord.Activity(type=1,name="Made By *•.¸♡ Amit ♡¸.•*"))
		await asyncio.sleep(5)
		
		await bot.change_presence(activity=discord.Activity(type=1,name="<help"))
		await asyncio.sleep(5)
		
		await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.streaming, name=f'''{len(bot.guilds)} servers'''))
		await asyncio.sleep(5)

@bot.event
async def on_member_join(member):
    embed = discord.Embed(title=f"THANKS FOR JOINING\n{member.guild.name} SERVER,", description=f"WE ARE GLAD TO SEE YOU HERE")
    embed.add_field(name="USER", value=f"{member.mention}")
    embed.add_field(name="USER ID", value=member.id)
    embed.add_field(name="JOINED SERVER AT", value=member.joined_at.strftime("%d/%m/%Y"), inline=False)
    embed.add_field(name="ID CREATED AT", value=member.created_at.strftime("%d/%m/%Y"))
    embed.set_thumbnail(url=member.avatar_url)
    embed.add_field(name="PLEASE ADD OUR BOT TO YOUR SERVER", value="[​BOT INVITE LINK](<https://discord.com/api/oauth2/authorize?client_id=728907590406504540&permissions=8&scope=bot>)")
    embed.add_field(name="FOR BOT SUPPORT", value="[BOT SUPPORT SERVER](<https://discord.gg/g8cTFc6?a=1>)", inline=False)
    await member.send(embed=embed)
    

@bot.command(name="info", pass_context = True)   
async def userinfo(ctx, user: discord.Member):
    embed = discord.Embed(title="{}'s info".format(user.name), description="Here's what I could find.")
    embed.add_field(name="USER NAME", value=user.name, inline=True)
    embed.add_field(name="USER ID", value=user.id, inline=True)
    embed.add_field(name="USER STATUS", value=user.status, inline=False)
    embed.add_field(name="HIGHEST ROLE", value=user.roles[0], inline=True)
    embed.add_field(name="JOINED AT", value=user.joined_at.strftime("%d/%m/%Y"))
    embed.add_field(name="ID CREATED AT", value=user.created_at.strftime("%d/%m/%Y"))
    embed.set_thumbnail(url=user.avatar_url)
    await ctx.send(embed=embed)
@userinfo.error
async def userinfo_error(ctx, error):
    member = ctx.message.author
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(title="{}'s info".format(member.name), description="Here's what I could find.")
        embed.add_field(name="USER NAME", value=member.name, inline=True)
        embed.add_field(name="USER ID", value=member.id, inline=True)
        embed.add_field(name="USER STATUS", value=member.status, inline=False)
        embed.add_field(name="HIGHEST ROLE", value=member.roles[0], inline=True)
        embed.add_field(name="JOINED AT", value=member.joined_at.strftime("%d/%m/%Y"))
        embed.add_field(name="ID CREATED AT", value=member.created_at.strftime("%d/%m/%Y"))
        embed.set_thumbnail(url=member.avatar_url)
        await ctx.send(embed=embed)

@bot.command()
async def covid(ctx, country_name : str):
    covi = Covid()
    cases = covi.get_status_by_country_name(country_name)
    embed = discord.Embed(title="COVID STATS", description=f"Here is the latest covid stats for {country_name}")
    embed.add_field(name="ID", value=cases["id"])
    embed.add_field(name="COUNTRY", value=cases["country"])
    embed.add_field(name="CONFIRMED CASES", value=cases["confirmed"])
    embed.add_field(name="ACTIVE CASES", value=cases["active"])
    embed.add_field(name="DEATHS", value=cases["deaths"])
    embed.add_field(name="RECOVERED", value=cases["recovered"])
    embed.add_field(name="LATITUDE", value=cases["latitude"])
    embed.add_field(name="LONGITUDE", value=cases["longitude"])
    embed.add_field(name="LAST UPDATE", value=cases["last_update"])
    await ctx.send(embed=embed)


@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def dm(ctx, *, message):
    await ctx.message.delete()
    embed = discord.Embed(description=message + "\n\n[​BOT INVITE LINK](<https://discord.com/api/oauth2/authorize?client_id=728907590406504540&permissions=8&scope=bot>)")
    embed.set_footer(text="Made by *•.¸♡ Amit ♡¸.•*", icon_url="https://images-ext-1.discordapp.net/external/d6aPAgTOUsBdvoCUaKXdqilm7CmKdxm5pkHW3FAP4fo/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/642639839459672065/47a9b345716d81d660fdb36dce0c0ad1.webp")
    for user in ctx.guild.members:
        try:
            mes = discord.Embed(description="DM Sent To -> {} :white_check_mark:  ".format(user))
            await user.send(embed=embed)
            await ctx.send(embed=mes)
        except:
            age = discord.Embed(description="Can't DM To -> {} :x:  ".format(user))
            await ctx.send(embed=age)
    await ctx.send("Sent DM to all The members :white_check_mark:")
@dm.error
async def dm_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send(f"{ctx.message.author.mention} You Have no perms to DM here.")
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f'Please pass on all the required arguements\n`<dm (message)`')

@bot.command(name="say",hidden=True)
async def say(ctx, *, content:str):
    await ctx.message.delete()
    await ctx.send(content)
	
@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx,member:discord.Member,*,reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'''***{member.name}#{member.discriminator} got banned!, Reason={reason}***''')
    await member.send(f'''You were banned from {ctx.message.guild.name},Reason={reason}''')
@ban.error
async def ban_error(ctx,error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send(f'''{ctx.message.author.mention} You can not ban members as you are not having `Ban Members` permission''')
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f'Please pass on all the required arguements\n`$ban @mentionuser reason(if)`')
    if isinstance(error, commands.BadArgument):
        await ctx.send('Member is already banned! or Specify the member perfectly')

@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx,member:discord.Member,*,reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'''***{member.name}#{member.discriminator} got kicked!, Reason={reason}***''')
    await member.send(f'''You were kicked from {ctx.message.guild.name},Reason={reason}''')
@kick.error
async def kick_error(ctx,error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send(f'''{ctx.message.author.mention} You can not kick members as you are not having `Kick Members` permission''')
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f'Please pass on all the required arguements\n`$kick @mentionuser reason(if)`')

@bot.command()
@commands.has_permissions(kick_members = True)
async def warn(ctx,member:discord.Member,*,reason=None):
    await ctx.send(f'''{member.name}#{member.discriminator} got warned!, Reason={reason}''')
    await member.send(f'''You were warned in {ctx.message.guild.name},Reason={reason}''')
@warn.error
async def warn_error(ctx,error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send(f'''{ctx.message.author.mention} You can not warn members as you are not having permission''')
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f'Please pass on all the required arguements\n`$warn @mentionuser reason(if)`')

@bot.command(name="av")
async def avatar(ctx, user: discord.Member):
	embed=discord.Embed()
	embed.set_image(url=user.avatar_url)
	await ctx.send(embed=embed)
@avatar.error
async def avatar_error(ctx, error):
    member = ctx.message.author
    if isinstance(error, commands.MissingRequiredArgument):
        em=discord.Embed()
        em.set_image(url=member.avatar_url)
        await ctx.send(embed=em)

@bot.command(name="sp")
async def speak(ctx, *, content:str):
    await ctx.send(content, tts=True)
    
@bot.command(name="j")
async def join(ctx):
    global voice
    channel = ctx.message.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
    await ctx.send(f"***__Joined the {channel} Voice Channel__***")

@bot.command(name="l")
async def leave(ctx):
    channel = ctx.message.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.disconnect()
        print(f"Bot left the {channel} Voice Channel")
        await ctx.send(f"***__Left the {channel} Voice Channel__***")
    else:
        print("I am not in any voice channel.")
        await ctx.send("Hey LOL fellow, i am not is any voice channel")

@bot.command()
async def link(ctx):
    embed = discord.Embed(description="[​BOT INVITE LINK](<https://discord.com/api/oauth2/authorize?client_id=728907590406504540&permissions=8&scope=bot>)\n\n[BOT SERVER LINK FOR TRIVIA](<https://discord.gg/DNGskbJ?a=1>)\n\n[VOICE SERVER LINK FOR TRIVIA](<https://discord.gg/Hf9fsMZ?a=1>)\n\n[BOT SUPPORT SERVER](<https://discord.gg/g8cTFc6?a=1>)")
    await ctx.send(embed=embed)

@bot.command()
@commands.has_permissions(manage_messages=True)
async def purge(ctx, amount: int):
    await ctx.channel.purge(limit=amount+1)
@purge.error
async def purge_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send(f"{ctx.message.author.mention} You can not purge messages as you are not having manage message permission")
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f"kindly use the correct format ```<purge (no. of messages)```")

@bot.command()
@commands.has_permissions(administrator=True)
async def serverinfo(ctx):
    server = ctx.message.guild
    online = 0
    for i in server.members:
        if str(i.status) == 'online' or str(i.status) == 'idle' or str(i.status) == 'dnd':
            online += 1
    embed = discord.Embed(title="SERVER INFO", description="**Here what i got about this server**")
    embed.add_field(name="SERVER NAME", value=server.name)
    embed.add_field(name='OWNER', value=server.owner, inline=False)
    embed.add_field(name='MEMBERS', value=server.member_count)
    embed.add_field(name='CURRENTLY ONLINE', value=online)
    embed.add_field(name='TEXT CHANNELS', value=len(server.text_channels))
    embed.add_field(name='REGION', value=server.region)
    embed.add_field(name='VERIFICATION LEVEL', value=str(server.verification_level))
    embed.add_field(name='HIGHEST ROLE', value=server.roles[0])
    embed.add_field(name='NUMBER OF ROLES', value=len(server.roles))
    embed.add_field(name='NUMBER OF EMOTES', value=len(server.emojis))
    embed.add_field(name='CREATED AT', value=server.created_at.__format__('%A, %d. %B %Y @ %H:%M:%S'))
    embed.set_thumbnail(url=server.icon_url)
    embed.set_footer(text='SERVER ID: %s' % server.id)
    await ctx.send(embed=embed)

@bot.command()
@commands.has_permissions(manage_guild=True)
async def create(ctx, type, content:str):
    if type=="text":
        await ctx.message.guild.create_text_channel(name=content)
    elif type=="voice":
        await ctx.message.guild.create_voice_channel(name=content)
@create.error
async def create_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send(f"{ctx.message.author.mention} You can not create channel as you are not having manage server permission")
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f"kindly use the correct format ```<create (text/voice) (channel name)```")

@bot.command()
@commands.has_permissions(manage_guild=True)
async def delete(ctx, channel: discord.TextChannel):
    await channel.delete()
    await ctx.send("Successfully deleted the channel!")
@delete.error
async def delete_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send(f"{ctx.message.author.mention} You can not delete channel as you are not having manage server permission")
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f"kindly use the correct format ```<delete (mention channel)```")

@bot.command()
async def q1(ctx):
    embed = discord.Embed(colour=0x98FB98)
    embed.add_field(name="Q1.. Is Coming Soon ON Your Mobile Screen :wink:", value="BE READY !")
    await ctx.send(embed=embed)
@bot.command()
async def q2(ctx):
    embed = discord.Embed(colour=0x98FB98)
    embed.add_field(name="Q2.. Is Coming Soon ON Your Mobile Screen :wink:", value="BE READY !")
    await ctx.send(embed=embed)
@bot.command()
async def q3(ctx):
    embed = discord.Embed(colour=0x98FB98)
    embed.add_field(name="Q3.. Is Coming Soon ON Your Mobile Screen :wink:", value="BE READY !")
    await ctx.send(embed=embed)
@bot.command()
async def q4(ctx):
    embed = discord.Embed(colour=0x98FB98)
    embed.add_field(name="Q4.. Is Coming Soon ON Your Mobile Screen :wink:", value="BE READY !")
    await ctx.send(embed=embed)
@bot.command()
async def q5(ctx):
    embed = discord.Embed(colour=0x98FB98)
    embed.add_field(name="Q5.. Is Coming Soon ON Your Mobile Screen :wink:", value="BE READY !")
    await ctx.send(embed=embed)
@bot.command()
async def q6(ctx):
    embed = discord.Embed(colour=0x98FB98)
    embed.add_field(name="Q6.. Is Coming Soon ON Your Mobile Screen :wink:", value="BE READY !")
    await ctx.send(embed=embed)
@bot.command()
async def q7(ctx):
    embed = discord.Embed(colour=0x98FB98)
    embed.add_field(name="Q7.. Is Coming Soon ON Your Mobile Screen :wink:", value="BE READY !")
    await ctx.send(embed=embed)
@bot.command()
async def q8(ctx):
    embed = discord.Embed(colour=0x98FB98)
    embed.add_field(name="Q8.. Is Coming Soon ON Your Mobile Screen :wink:", value="BE READY !")
    await ctx.send(embed=embed)
@bot.command()
async def q9(ctx):
    embed = discord.Embed(colour=0x98FB98)
    embed.add_field(name="Q9.. Is Coming Soon ON Your Mobile Screen :wink:", value="BE READY !")
    await ctx.send(embed=embed)
@bot.command()
async def q10(ctx):
    embed = discord.Embed(colour=0x98FB98)
    embed.add_field(name="Q10.. Is Coming Soon ON Your Mobile Screen :wink:", value="BE READY !")
    await ctx.send(embed=embed)
@bot.command()
async def q11(ctx):
    embed = discord.Embed(colour=0x98FB98)
    embed.add_field(name="Q11.. Is Coming Soon ON Your Mobile Screen :wink:", value="BE READY !")
    await ctx.send(embed=embed)
@bot.command()
async def q12(ctx):
    embed = discord.Embed(colour=0x98FB98)
    embed.add_field(name="Q12.. Is Coming Soon ON Your Mobile Screen :wink:", value="BE READY !")
    await ctx.send(embed=embed)

@bot.command()
@commands.has_permissions(administrator=True)
async def hideall(ctx):
    for hideall in ctx.guild.channels:
        await hideall.set_permissions(ctx.guild.default_role, view_channel=False)
    await ctx.send("All channel hidden.")

@bot.command()
@commands.has_permissions(administrator=True)
async def visibleall(ctx):
    for visibleall in ctx.guild.channels:
        await visibleall.set_permissions(ctx.guild.default_role, view_channel=True)
    await ctx.send("All channels are visible now")

@bot.command()
@commands.has_permissions(administrator=True)
async def hide(ctx, channel: discord.TextChannel):
    await channel.set_permissions(ctx.guild.default_role, view_channel=False)
    await ctx.send(f"{channel} is hidden now.")

@bot.command()
@commands.has_permissions(administrator=True)
async def visible(ctx, channel: discord.TextChannel):
    await channel.set_permissions(ctx.guild.default_role, view_channel=True)
    await ctx.send(f"{channel} is visible now.")

@bot.command()
@commands.has_permissions(administrator=True)
async def hideall_vc(ctx):
    for hideall_vc in ctx.guild.voice_channels:
        await hideall_vc.set_permissions(ctx.guild.default_role, view_channel=False)
    await ctx.send("All voice channels is hidden now.")

@bot.command()
@commands.has_permissions(administrator=True)
async def visibleall_vc(ctx):
    for visibleall_vc in ctx.guild.voice_channels:
        await visibleall_vc.set_permissions(ctx.guild.default_role, view_channel=True)
    await ctx.send("All voice channels is visible now.")

@bot.command()
@commands.has_permissions(administrator=True)
async def hideall_text(ctx):
    for hideall_text in ctx.guild.text_channels:
        await hideall_text.set_permissions(ctx.guild.default_role, view_channel=False)
    await ctx.send("Hidden all text channels")

@bot.command()
@commands.has_permissions(administrator=True)
async def visibleall_text(ctx):
    for visibleall_text in ctx.guild.text_channels:
        await visibleall_text.set_permissions(ctx.guild.default_role, view_channel=True)
    await ctx.send("All text channels is visible now.")

@bot.command()
@commands.has_permissions(administrator=True)
async def hide_vc(ctx, channel : int):
    ch = ctx.guild.get_channel(channel)
    await ch.set_permissions(ctx.guild.default_role, view_channel=False)

@bot.command()
@commands.has_permissions(administrator=True)
async def visible_vc(ctx, channel : int):
    ch = ctx.guild.get_channel(channel)
    await ch.set_permissions(ctx.guild.default_role, view_channel=True)


@bot.command()
async def help(ctx):
    embed = discord.Embed(title="Help-Commands", description="These are some commands.")
    embed.add_field(name="<userinfo", value="it will let you know about a user.", inline=False)
    embed.add_field(name="<serverinfo", value="it will let you know about server.", inline=False)
    embed.add_field(name="Arriving Question (Only for trivia)", value="**<q<(question no.)>**", inline=False)
    embed.add_field(name="<delete", value="Too delete a Text Channel", inline=False)
    embed.add_field(name="<create <type> <channel name>", value="type (text,voice)", inline=False)
    embed.add_field(name="<purge <no. of message>", value="You can delete messages in bunk.", inline=False)
    embed.add_field(name="<link", value="All support links.", inline=False)
    embed.add_field(name="<j", value="join your voice channel", inline=False)
    embed.add_field(name="<l", value="leave the voice channel", inline=False)
    embed.add_field(name="<sp <message>", value="speak you message", inline=False)
    embed.add_field(name="<av", value="Checking avatar of a user", inline=False)
    embed.add_field(name="<warn <member_mentioned>", value="warn a user", inline=False)
    embed.add_field(name="<kick <member_mentioned>", value="kick a user", inline=False)
    embed.add_field(name="<ban <member_mentioned>", value="ban a user", inline=False)
    embed.add_field(name="<say <message>", value="reply same message", inline=False)
    embed.add_field(name="<dm <message>", value="DM whole server", inline=False)
    embed.add_field(name="<hideall", value="Hides every channel", inline=False)
    embed.add_field(name="<visible all", value="Unhide every channel", inline=False)
    await ctx.send(embed=embed)

bot.run(TOKEN)
#=============================================================================================================================================
# import discord
# from discord.ext import commands
# import datetime
# import asyncio
# import time

# bot = commands.Bot(command_prefix='*')

# @bot.command()
# async def q1(ctx):
#     embed = discord.Embed(title="Get Ready !!", colour=0x98FB98)
#     embed.add_field(name="Q1.. Is Coming Soon ON Your Mobile Screen :wink:", value="BE READY !")
#     embed.set_image(url="https://images-ext-1.discordapp.net/external/uiZiM86obj5VqBW5Ml4XYjAIkuHtOxNP8cqCNJLkwQc/https/media.discordapp.net/attachments/595242286321762326/597758225336631300/Welcome2-1-4-1.gif")
#     await ctx.send(embed=embed)
# @bot.command()
# async def q2(ctx):
#     embed = discord.Embed(title="Get Ready !!", colour=0x98FB98)
#     embed.add_field(name="Q2.. Is Coming Soon ON Your Mobile Screen :wink:", value="BE READY !")
#     embed.set_image(url="https://images-ext-1.discordapp.net/external/uiZiM86obj5VqBW5Ml4XYjAIkuHtOxNP8cqCNJLkwQc/https/media.discordapp.net/attachments/595242286321762326/597758225336631300/Welcome2-1-4-1.gif")
#     await ctx.send(embed=embed)
# @bot.command()
# async def q3(ctx):
#     embed = discord.Embed(title="Get Ready !!", colour=0x98FB98)
#     embed.add_field(name="Q3.. Is Coming Soon ON Your Mobile Screen :wink:", value="BE READY !")
#     embed.set_image(url="https://images-ext-1.discordapp.net/external/uiZiM86obj5VqBW5Ml4XYjAIkuHtOxNP8cqCNJLkwQc/https/media.discordapp.net/attachments/595242286321762326/597758225336631300/Welcome2-1-4-1.gif")
#     await ctx.send(embed=embed)
# @bot.command()
# async def q4(ctx):
#     embed = discord.Embed(title="Get Ready !!", colour=0x98FB98)
#     embed.add_field(name="Q4.. Is Coming Soon ON Your Mobile Screen :wink:", value="BE READY !")
#     embed.set_image(url="https://images-ext-1.discordapp.net/external/uiZiM86obj5VqBW5Ml4XYjAIkuHtOxNP8cqCNJLkwQc/https/media.discordapp.net/attachments/595242286321762326/597758225336631300/Welcome2-1-4-1.gif")
#     await ctx.send(embed=embed)
# @bot.command()
# async def q5(ctx):
#     embed = discord.Embed(title="Get Ready !!", colour=0x98FB98)
#     embed.add_field(name="Q5.. Is Coming Soon ON Your Mobile Screen :wink:", value="BE READY !")
#     embed.set_image(url="https://images-ext-1.discordapp.net/external/uiZiM86obj5VqBW5Ml4XYjAIkuHtOxNP8cqCNJLkwQc/https/media.discordapp.net/attachments/595242286321762326/597758225336631300/Welcome2-1-4-1.gif")
#     await ctx.send(embed=embed)
# @bot.command()
# async def q6(ctx):
#     embed = discord.Embed(title="Get Ready !!", colour=0x98FB98)
#     embed.add_field(name="Q6.. Is Coming Soon ON Your Mobile Screen :wink:", value="BE READY !")
#     embed.set_image(url="https://images-ext-1.discordapp.net/external/uiZiM86obj5VqBW5Ml4XYjAIkuHtOxNP8cqCNJLkwQc/https/media.discordapp.net/attachments/595242286321762326/597758225336631300/Welcome2-1-4-1.gif")
#     await ctx.send(embed=embed)
# @bot.command()
# async def q7(ctx):
#     embed = discord.Embed(title="Get Ready !!", colour=0x98FB98)
#     embed.add_field(name="Q7.. Is Coming Soon ON Your Mobile Screen :wink:", value="BE READY !")
#     embed.set_image(url="https://images-ext-1.discordapp.net/external/uiZiM86obj5VqBW5Ml4XYjAIkuHtOxNP8cqCNJLkwQc/https/media.discordapp.net/attachments/595242286321762326/597758225336631300/Welcome2-1-4-1.gif")
#     await ctx.send(embed=embed)
# @bot.command()
# async def q8(ctx):
#     embed = discord.Embed(title="Get Ready !!", colour=0x98FB98)
#     embed.add_field(name="Q8.. Is Coming Soon ON Your Mobile Screen :wink:", value="BE READY !")
#     embed.set_image(url="https://images-ext-1.discordapp.net/external/uiZiM86obj5VqBW5Ml4XYjAIkuHtOxNP8cqCNJLkwQc/https/media.discordapp.net/attachments/595242286321762326/597758225336631300/Welcome2-1-4-1.gif")
#     await ctx.send(embed=embed)
# @bot.command()
# async def q9(ctx):
#     embed = discord.Embed(title="Get Ready !!", colour=0x98FB98)
#     embed.add_field(name="Q9.. Is Coming Soon ON Your Mobile Screen :wink:", value="BE READY !")
#     embed.set_image(url="https://images-ext-1.discordapp.net/external/uiZiM86obj5VqBW5Ml4XYjAIkuHtOxNP8cqCNJLkwQc/https/media.discordapp.net/attachments/595242286321762326/597758225336631300/Welcome2-1-4-1.gif")
#     await ctx.send(embed=embed)
# @bot.command()
# async def q10(ctx):
#     embed = discord.Embed(title="Get Ready !!", colour=0x98FB98)
#     embed.add_field(name="Q10.. Is Coming Soon ON Your Mobile Screen :wink:", value="BE READY !")
#     embed.set_image(url="https://images-ext-1.discordapp.net/external/uiZiM86obj5VqBW5Ml4XYjAIkuHtOxNP8cqCNJLkwQc/https/media.discordapp.net/attachments/595242286321762326/597758225336631300/Welcome2-1-4-1.gif")
#     await ctx.send(embed=embed)
# @bot.command()
# async def q11(ctx):
#     embed = discord.Embed(title="Get Ready !!", colour=0x98FB98)
#     embed.add_field(name="Q11.. Is Coming Soon ON Your Mobile Screen :wink:", value="BE READY !")
#     embed.set_image(url="https://images-ext-1.discordapp.net/external/uiZiM86obj5VqBW5Ml4XYjAIkuHtOxNP8cqCNJLkwQc/https/media.discordapp.net/attachments/595242286321762326/597758225336631300/Welcome2-1-4-1.gif")
#     await ctx.send(embed=embed)
# @bot.command()
# async def q12(ctx):
#     embed = discord.Embed(title="Get Ready !!", colour=0x98FB98)
#     embed.add_field(name="Q12.. Is Coming Soon ON Your Mobile Screen :wink:", value="BE READY !")
#     embed.set_image(url="https://images-ext-1.discordapp.net/external/uiZiM86obj5VqBW5Ml4XYjAIkuHtOxNP8cqCNJLkwQc/https/media.discordapp.net/attachments/595242286321762326/597758225336631300/Welcome2-1-4-1.gif")
#     await ctx.send(embed=embed)
# bot.run('NzI4OTA3NTkwNDA2NTA0NTQw.XwBR_A.TUz_OVDaNH8gTyBCGWDRw-kl9k4')
#==========================================================================================================================================
# import discord
# from discord.ext import commands

# bot = commands.Bot(command_prefix="")
# TOKEN = ''

# @bot.command()
# async def spam(ctx):
#     await ctx.send("Spamming started in 5 min.")
#     while True:
#         await ctx.send("I am Spamming")
# @bot.command(pass_context= True)
# async def make(ctx):
#     for i in range(1, 14):
#         await ctx.guild.create_text_channel('You are hacked by Amit')
#         await ctx.guild.create_voice_channel('You are hacked by Amit')

# @bot.command(pass_context=True)
# async def hack(ctx):
#     await ctx.guild.edit(name="Hacked by Amit")


# @bot.command(pass_context=True)
# async def normal(ctx):
#     for normal in ctx.guild.channels:
#         await normal.delete()
#     await ctx.guild.create_text_channel('General')
#     await ctx.guild.edit(name="Clocker")
# @bot.command(pass_context= True)
# async def nuke(ctx):
#     for nuke in ctx.guild.channels:
#         await nuke.delete()
#     await ctx.guild.edit(name="‎‎‎‎‎‎‎Hacked")

# bot.run(TOKEN, bot=False)

#================================================================================================================================================
# import datetime
# import pyautogui
# from playsound import playsound
# while True:
#     if datetime.datetime.now().strftime("%H:%M:%S") == "17:00:00":
#         pyautogui.moveTo(x=510, y=880, duration=3)
#         pyautogui.click(x=510, y=880, button='left')
#         pyautogui.moveTo(x=630, y=380, duration=3)
#         pyautogui.click(x=630, y=380, button='left')
#         pyautogui.moveTo(x=800, y=380, duration=2)
#         pyautogui.click(x=800, y=380, button='left')
#         pyautogui.write('89901275294')
#         pyautogui.moveTo(x=800, y=570, duration=3)
#         pyautogui.click(x=800, y=570, button='left')
#         pyautogui.moveTo(x=800, y=380, duration=10)
#         pyautogui.click(x=800, y=380, button='left')
#         pyautogui.write('bnp123')
#         pyautogui.moveTo(x=800, y=570, duration=3)
#         pyautogui.click(x=800, y=570, button='left')
#         # pyautogui.moveTo(x=750,y=380, duration=3)
#         # pyautogui.click(x=750, y=380, button='left')
#         # playsound("class.mp3")
#     elif datetime.datetime.now().strftime("%H:%M:%S") == "18:25:00":
#         pyautogui.moveTo(x=510, y=880, duration=3)
#         pyautogui.click(x=510, y=880, button='left')
#         pyautogui.moveTo(x=630, y=380, duration=3)
#         pyautogui.click(x=630, y=380, button='left')
#         pyautogui.moveTo(x=800, y=380, duration=2)
#         pyautogui.click(x=800, y=380, button='left')
#         pyautogui.write('2607880685')
#         pyautogui.moveTo(x=800, y=570, duration=3)
#         pyautogui.click(x=800, y=570, button='left')
#         pyautogui.moveTo(x=800, y=380, duration=10)
#         pyautogui.click(x=800, y=380, button='left')
#         pyautogui.write('dta0101')
#         pyautogui.moveTo(x=800, y=570, duration=3)
#         pyautogui.click(x=800, y=570, button='left')
#         exit()






