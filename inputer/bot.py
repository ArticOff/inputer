import inputer

bot = inputer.bot('ArticBot', 'bot')
color = inputer.Color

if bot.on_ready():

    bot.send('/help')