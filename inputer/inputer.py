import client, data_post

class COLOR:
    violet = '\033[95m'
    cyan = '\033[96m'
    dark_cyan = '\033[36m'
    blue = '\033[94m'
    green = '\033[92m'
    yellow = '\033[93m'
    red = '\033[91m'
    white = '\033[37m'
    black = '\033[30m'
    magenta = '\033[35m'
    bold = '\033[1m'
    dim = '\033[2m'
    normal = '\033[22m'
    underlined = '\033[4m'
    stop = '\033[0m'
    def from_rgb(red: int, green: int, blue: int):
        return "\033[38;2;{};{};{}m".format(red, green, blue)
    def from_hex(hex: str):
        h = hex.lstrip('#')
        rgb = tuple(int(h[i:i+2], 16) for i in (0, 2, 4))
        rgb_format1 = str(rgb).replace(",", ";")
        rgb_format2 = rgb_format1.replace("(", "")
        rgb_format3 = rgb_format2.replace(")", "")
        rgb_format4 = rgb_format3.replace(" ", "")
        return '\033[38;2;{}m'.format(rgb_format4)

Color = COLOR

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
        self.id = user[self.name]['id']

    def on_ready(self, message: str = 'ready!'):
        print(message)
        return True

    def send(self, message: str):

        _badge = self.bot.get_badge(self.name)
        badge = client.verify_badge(_badge)

        return print('{} {}: {}\033[0m'.format(badge, self.name, message))