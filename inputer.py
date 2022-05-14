import client, data_post

class bot:
    def __init__(self, name: str, password: str):
        
        self.name = name
        self.password = password

        user = data_post.get_account_data()
        

        if user[self.name]:
            if user[self.name]['bot']:
                bot = data_post.login_account(self.name, self.password, True)
            else:
                print('ERROR: You can\'t connect to a user')
                return exit()
        else:
            data_post.open_account(self.name, self.password, True)
            bot = data_post.login_account(self.name, self.password, True)

        self.bot = bot

    def on_ready(self, message: str = 'ready!'):
        print(message)
        return True

    def send(self, message: str):

        _badge = self.bot.get_badge(self.name)
        badge = client.verify_badge(_badge)

        return print('{} {}: {}'.format(badge, self.name, message))