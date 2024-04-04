from discord_slash import SlashCommand
from discord_slash.utils.manage_commands import create_option
from discord_slash import SlashCommand, SlashContext
import discord
from discord.ext import commands



bot = commands.Bot(command_prefix='!', description="ayuda bot") #Prefijo para el comando !trono
bot.remove_command("help") 
slash = SlashCommand(bot, sync_commands=True)

# Definimos la función que será llamada cuando se ejecute el comando /ping
@slash.slash(
    name="ping",
    description="Comando para obtener el ping del bot."
)
async def _ping(ctx: SlashContext):
    # Calculamos el ping
    ping = round(bot.latency * 1000) # Convertimos el ping de segundos a milisegundos y lo redondeamos
    
    # Enviamos la respuesta al canal donde se ejecutó el comando
    await ctx.send(f"Pong! El ping del bot es {ping}ms")


@bot.event
async def on_ready():
    print("BOT listo!")


bot.run("")
