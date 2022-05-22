import inputer

bot = inputer.bot('ArticBot', 'bot')

if bot.on_ready():

    bot.send('hi')