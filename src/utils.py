import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f"✅ {bot.user} está online!")

class JoinButtonView(discord.ui.View):
    def __init__(self, script):
        super().__init__()
        self.script = script

    @discord.ui.button(label="Entrar no servidor 🎮", style=discord.ButtonStyle.green)
    async def join_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(
            f"💻 Copie e cole esse script pra entrar:\n```lua\n{self.script}\n```",
            ephemeral=True
        )

@bot.command()
async def servidor(ctx):
    # Exemplo de uso — normalmente tu pegaria isso de `extract_server_info(event)`
    server_info = {
        "name": "Servidor ChilliHub",
        "script": 'game:GetService("TeleportService"):TeleportToPlaceInstance(1234567890, "jobid_aqui")'
    }

    embed = discord.Embed(
        title=f"🌐 {server_info['name']}",
        description="Clique abaixo pra entrar no servidor!",
        color=discord.Color.blurple()
    )

    view = JoinButtonView(server_info['script'])
    await ctx.send(embed=embed, view=view)

bot.run("MTQzNjg0NzgyNzU3NjY4ODg0MQ.GdZAdP.tyHznCkmcWD5QKjjQk6mWtT-cRQuWrvjpuQHSM")
