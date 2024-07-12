import discord
from discord.ext import commands
Channel_id = 1260792376444715018

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())
user_warnings = 0
rojo = discord.Color.red()
morado = discord.Color.purple()
naranja = discord.Color.orange()
azul = discord.Color.blue()
verde = discord.Color.green()
amarillo = discord.Color.yellow()

@bot.event
async def on_ready():
    channel = bot.get_channel(Channel_id)
    print(f'We have logged in as {bot.user}')
    print('We have succesfully sincronized with the slash commands')
    await channel.send("🟢READY🟢")
    await bot.tree.sync()
    emb = discord.Embed(
        title="Listo!",
        description="Hemos exitosamente sincronizado con los slash commands:",
        color=discord.Color.blue()
    )
    emb.add_field(name="", value=f"""
1. /ping
2. (EN PROGRESO)
""")
    await channel.send(embed=emb)

bot.run("TOKEN")
