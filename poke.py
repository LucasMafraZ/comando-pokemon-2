#O comando seleciona aleatoriamente um incial de pokemon 
#há chance de aparecer um incial shiny D_D
@bot.command()
async def pokemon(ctx):
    img_name = random.choice(os.listdir('pokemon'))
    with open(f'pokemon/{img_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

