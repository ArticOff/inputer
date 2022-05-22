"""
The MIT License (MIT)

Copyright (c) 2022-today Artic

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""

import os, sys, subprocess, re, data_post, json, random, datetime

def log_with_no_account():
    username = input('What\'s your username ?\nYou: ')
    if not username:
        username = 'guest_{}'.format(random.randint(1, 10000))
    return username

def log_with_account(username: str, password: str, bot: bool = False):
    data_post.open_account(username, password, bot)

def verify_badge(badge: str):
    if badge == '[DEVELOPER]':
        badge = '\033[94m{}\033[0m'.format(badge)

    elif badge == '[ADMIN]':
        badge = '\033[91m{}\033[0m'.format(badge)
    
    elif badge == '[MODERATOR]':
        badge = '\033[93m{}\033[0m'.format(badge)

    elif badge == '[FRIEND]':
        badge = '\033[95m{}\033[0m'.format(badge)

    elif badge == '[VIP]':
        badge = '\033[92m{}\033[0m'.format(badge)

    elif badge == '[BOT]':
        badge = '\033[96m{}\033[0m'.format(badge)

    elif badge == '[MEMBER]':
        badge = '\033[36m{}\033[0m'.format(badge)

    else:
        badge = '\033[4m{}\033[0m'.format(badge)

    return badge

def verify_bot(bot: bool = False):
    if bot:
        bot = '\033[92myes\033[0m'
    else:
        bot = '\033[91mno\033[0m'

    return bot

class command:
    def id(message: str, _username: str):
        if str(message).split()[0] == '/id':
            user = data_post.get_account_data()
            try:
                name = message.split()[1]
                try:
                    id = user[name]['id']
                    print('\033[35m[SYSTEM]\033[0m: The {}\'s id is {}.'.format(name, id))
                    return message
                except:
                    print('\033[35m[SYSTEM]\033[0m: This person doesn\'t exist.')
                    return message
            except:
                username = user[_username]['username']
                id = user[username]['id']

                print('\033[35m[SYSTEM]\033[0m: The {}\'s id is {}.'.format(username, id))
                return message
        else:
            return message
    def badge(message: str, id: str):
        username = str(message).split()[1]
        user = data_post.get_account_data()
        if id == '1':
            if str(message).split()[0] == '/badge':
                try:
                    username = str(message).split()[1]
                    badge = user[username]['badge']
                    bot = user[str(username)]['bot']
                    try:
                        status = str(message).removeprefix('/badge {} '.format(username)) # str(message).split()[2] 
                        status = '[{}]'.format(status)

                        id = user[username]['id']

                        password = user[username]['password']

                        if badge == status:
                            return print('\033[35m[SYSTEM]\033[0m: The new badge is the same as the old one.')

                        user[str(username)] = {}
                        user[str(username)]['id'] = id
                        user[str(username)]['username'] = str(username)
                        user[str(username)]['password'] = str(password)
                        user[str(username)]['bot'] = bot
                        user[str(username)]['badge'] = status

                        with open('.json/database.json','w', encoding='utf-8') as f:
                            json.dump(user,f,indent=4,separators=(',',': '), ensure_ascii=False)
                            f.close()
                        
                        print('\033[35m[SYSTEM]\033[0m: The badge of {} has been changed to {}.'.format(username, status))
                        return message
                    except:
                        print('\033[35m[SYSTEM]\033[0m: This person doesn\'t exist.')
                        return message
                except:
                    print('\033[35m[SYSTEM]\033[0m: You did not mention anyone.')
                    return message
            else:
                return message
        else:
            print('\033[35m[SYSTEM]\033[0m: You cannot run this command.')
            return message
    def name(message: str, id: str):
        username = str(message).split()[1]
        user = data_post.get_account_data()
        if id == '1':
            if str(message).split()[0] == '/name':
                try:
                    username = str(message).split()[1]
                    badge = user[username]['badge']
                    bot = user[str(username)]['bot']
                    try:
                        name = str(message).split()[2]

                        id = user[username]['id']

                        password = user[username]['password']

                        user[str(username)] = {}
                        user[str(username)]['id'] = id
                        user[str(username)]['username'] = name
                        user[str(username)]['password'] = str(password)
                        user[str(username)]['bot'] = bot
                        user[str(username)]['badge'] = badge
                        with open('.json/database.json','w', encoding='utf-8') as f:
                            json.dump(user,f,indent=4,separators=(',',': '), ensure_ascii=False)
                            f.close()
                        
                        print('\033[35m[SYSTEM]\033[0m: The name of {} has been changed to {}.'.format(username, name))
                        return message
                    except:
                        print('\033[35m[SYSTEM]\033[0m: This person doesn\'t exist ({}).'.format(username))
                        return message
                except:
                    print('\033[35m[SYSTEM]\033[0m: You did not mention anyone.')
                    return message
            else:
                return message
        else:
            print('\033[35m[SYSTEM]\033[0m: You cannot run this command.')
            return message
    def why(message: str):
        if str(message).split()[0] == '/why':
            message = '¯\_(ツ)_/¯'
            return message
        else:
            return message
    def tableflip(message: str):
        if str(message).split()[0] == '/tableflip':
            message = '(╯°□°）╯︵ ┻━┻'
            return message
        else:
            return message
    def unflip(message: str):
        if str(message).split()[0] == '/unflip':
            message = '┬─┬ ノ( ゜-゜ノ)'
            return message
        else:
            return message
    def discord(message: str):
        if str(message).split()[0] == '/discord':
            print('\033[35m[SYSTEM]\033[0m: Here\'s the discord server (https://discord.gg/h7YFnP45jv).')
            return message
        else:
            return message
    def info(message: str, _username: str):
        if str(message).split()[0] == '/info':
            user = data_post.get_account_data()
            try:
                name = message.split()[1]
                try:
                    id = user[name]['id']
                    _badge = user[name]['badge']
                    _bot = user[name]['bot']

                    bot = verify_bot(_bot)
                    badge = verify_badge(_badge)

                    print('\033[35m[SYSTEM]\033[0m: # userinfo - {} #\n'.format(name))
                    print('ID: {}'.format(id))
                    print('BADGE: {}'.format(badge))
                    print('BOT: {}'.format(bot))
                    print('')
                    return message
                except:
                    print('\033[35m[SYSTEM]\033[0m: This person doesn\'t exist.')
                    return message
            except:
                username = user[_username]['username']

                id = user[username]['id']
                _badge = user[username]['badge']
                _bot = user[username]['bot']

                bot = verify_bot(_bot)
                badge = verify_badge(_badge)

                print('\033[35m[SYSTEM]\033[0m: # userinfo - {} #\n'.format(username))
                print('ID: {}'.format(id))
                print('BADGE: {}'.format(badge))
                print('BOT: {}'.format(bot))
                print('')
                return message
        else:
            return message
    def appinfo(message: str):
        if str(message).split()[0] == '/appinfo':
            members = len(data_post.get_account_data())
            print('\033[35m[SYSTEM]\033[0m: # appinfo #\n')
            print('    Developed by Artic')
            print(' Coded in Python (3.9.13)\n')
            print('NUMBER OF MEMBERS: {}'.format(members))
            print('')
            return message
        else:
            return message
    def say(message: str, id: str):
        if id == '1':
            if str(message).split()[0] == '/say':
                return print('\033[35m[SYSTEM]\033[0m: {}'.format(str(message).removeprefix('/say ')))
        else:
            print('\033[35m[SYSTEM]\033[0m: You cannot run this command.')
            return message
    def calculate(message: str):
        if str(message).split()[0] == '/eval':
            try:
                calculation = eval(str(message).removeprefix('/eval '))
                print('\033[35m[SYSTEM]\033[0m: {} = {}'.format(str(message).removeprefix('/eval '), calculation))
            except:
                print('\033[35m[SYSTEM]\033[0m: Unable to solve the calculation.')
            return message
        else:
            return message
    def exe(message: str, id: str):
        if id == '1':
            if str(message).split()[0] == '/exe':
                print('\033[35m[SYSTEM]\033[0m: # IDE #\n')
                try:
                    exec(str(message).removeprefix('/exe '))
                    print('')
                    return message
                except:
                    if '.py' in str(message).removeprefix('/exe '):
                        os.system(str(message.removeprefix('/exe ')))
                        print('')
                        return message
                    else:
                        print('\033[35m[SYSTEM]\033[0m: Unable to execute this code.')
                return message
            else:
                return message
        else:
            print('\033[35m[SYSTEM]\033[0m: You cannot run this command.')
            return message
    def time(message: str):
        if str(message).split()[0] == '/time':
            print('\033[35m[SYSTEM]\033[0m: We are the {}.'.format(datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
            return message
        else:
            return message
    def cmd(message: str, id: str):
        if id == '1':
            if str(message).split()[0] == '/cmd':
                print('\033[35m[SYSTEM]\033[0m: # CMD #\n')
                os.system(str(message).removeprefix('/cmd '))
                print('')
                return message
            else:
                return message
        else:
            print('\033[35m[SYSTEM]\033[0m: You cannot run this command.')
            return message
    def restart(message: str):
        if str(message).split()[0] == '/restart':
            subprocess.run(sys.argv[0], shell=True)
            return quit()
        else:
            return message
    def exit(message: str):
        if str(message).split()[0] == '/exit':
            print('\033[35m[SYSTEM]\033[0m: Thank you for your visit !')
            return sys.exit()
        else:
            return message
    def help(message: str):
        if str(message).split()[0] == '/help':
            print('\033[35m[SYSTEM]\033[0m: # help #\n\n    <> = required | [] = optional\n')
            print('/id [username] - Gives you the user ID.')
            print('/why - Why not ?')
            print('/tableflip - Oh and then?')
            print('/unflip - mmm...')
            print('/discord - The official discord server.')
            print('/exit - Quit the client.')
            print('/info [username] - Gives you the user info.')
            print('/appinfo - Gives you the app info.')
            print('/say - Have the system say sentences.')
            print('/eval <calculation> - Solve the calculations.')
            print('/time - Get the current time.')
            print('/restart - Restart the client.')
            print('/cmd - Interacting with the cmd.')
            print('/exe <code or python file> - Executes the code or a python file.')
            print('/badge <username> <new badge> - Modifies a user\'s badge.')
            print('/name <username> <new name> - Modifies a user\'s name.')
            print('')
            return message
        else:
            return message

def send(id: str, username: str):
    message = input('\nYou: ')
    if not message:
        return print('\033[35m[SYSTEM]\033[0m: You have sent a blank message.')
    elif message.split()[0] == '/id':
        return command.id(message, username)
    elif message.split()[0] == '/badge':
        return command.badge(message, id)
    elif message.split()[0] == '/name':
        return command.name(message, id)
    elif message.split()[0] == '/why':
        return command.why(message)
    elif message.split()[0] == '/tableflip':
        return command.tableflip(message)
    elif message.split()[0] == '/unflip':
        return command.unflip(message)
    elif message.split()[0] == '/discord':
        return command.discord(message)
    elif message.split()[0] == '/info':
        return command.info(message, username)
    elif message.split()[0] == '/appinfo':
        return command.appinfo(message)
    elif message.split()[0] == '/say':
        return command.say(message, id)
    elif message.split()[0] == '/eval':
        return command.calculate(message)
    elif message.split()[0] == '/time':
        return command.time(message)
    elif message.split()[0] == '/restart':
        return command.restart(message)
    elif message.split()[0] == '/cmd':
        return command.cmd(message, id)
    elif message.split()[0] == '/exe':
        return command.exe(message, id)
    elif message.split()[0] == '/exit':
        return command.exit(message)
    elif message.split()[0] == '/help':
        return command.help(message)
    elif message.startswith('/'):
        print('\033[35m[SYSTEM]\033[0m: Unrecognised command ({}).'.format(message.split()[0]))
        return message
    else:
        return message
    
def send_limited():
    message = input('\nYou: ')
    if any(re.findall(pattern=r'(https?://[^\s]+)', string=message)):
        return print('\033[35m[SYSTEM]\033[0m: You may not post links.')
    if not message:
        return print('\033[35m[SYSTEM]\033[0m: You have sent a blank message.')
    elif message.split()[0] == '/exit':
        return command.exit(message)
    elif message.startswith('/'):
        print('\033[35m[SYSTEM]\033[0m: You can only use the commands by logging into an account !\n\nYou can simply issue the command "/exit".\n')
        return message
    return message

def main():
    os.system('cls')
    print('WELCOME TO INPUTER !')
    log_or_rapidlog = input('Do you have an account ? (y/n/create an account: c)\nYou (y/n/c): ')
    if log_or_rapidlog.lower() == 'n':
        user = log_with_no_account()
        os.system('cls')
        print('\033[35m[SYSTEM]\033[0m: Hey {} !'.format(user))
        while True:
            message = send_limited()
            print('\033[96m[GUEST]\033[0m {}: {}'.format(user, message))
    if log_or_rapidlog.lower() == 'c':

        username = input('What\'s your username ?\nYou : ')
        password = input('What\'s your password ?\nYou: ')

        try:
            log_with_account(username, password)
        except:
            sys.exit('ERROR: your account could not be created, try again.')

    if log_or_rapidlog.lower() == 'y':

        _username = input('What\'s your username ?\nYou: ')
        _password = input('What\'s your password ?\nYou: ')

        user = data_post.login_account(_username, _password)
        _badge = user.get_badge(_username)
        username = user.get_username(_username)
        id = user.get_id(username)

        badge = verify_badge(_badge)

        os.system('cls')
        print('\033[35m[SYSTEM]\033[0m: Hey {} !\n\nUse "/help" to get all the commands.'.format(username))
        while True:
            message = send(id, username)
            print('{} {}: {}'.format(badge, username, message))

if __name__ == '__main__':
    main()