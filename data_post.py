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

import json, random

SpecialSym =['$', '@', '#', '%']

def get_account_data():
    with open('database.json', encoding='utf-8') as f:
        user = json.load(f)
        f.close()
    return user

class open_account:
    def __init__(self, username: str, password: str, bot: bool = False):
        id = random.randint(1, 10000)

        badge = '[MEMBER]'

        if bot:
            badge = '[BOT]'
        else:
            badge = '[MEMBER]'

        self.username = username
        self.password = password
        self.bot = bot
        self.id = id
        self.badge = badge

        user = get_account_data()

        if str(self.username) in user:
            return print('ERROR: This account already exists.')

        if ' ' in str(self.username):
            return print('ERROR: Spaces are not allowed (use "_").')
        
        if not any(char.isdigit() for char in str(self.password)):
            return print('ERROR: Password should have at least one numeral.')
        
        if not any(char.isupper() for char in str(self.password)):
            return print('ERROR: Password should have at least one uppercase letter.')
        
        if not any(char.islower() for char in str(self.password)):
            return print('ERROR: Password should have at least one lowercase letter.')

        if not any(char in SpecialSym for char in str(self.password)):
            return print('ERROR: Password should have at least one of the symbols ($, @, #, %).')

        else:
            
            if len(self.password) <= 8:
                return print('ERROR: The password must be more than 8 characters long. (It is {} characters long)'.format(len(self.password)))
                
            else:
                user[str(self.username)] = {}
                user[str(self.username)]['id'] = str(self.id)
                user[str(self.username)]['username'] = self.username
                user[str(self.username)]['password'] = self.password
                user[str(self.username)]['bot'] = self.bot
                user[str(self.username)]['badge'] = self.badge
                with open('database.json','w', encoding='utf-8') as f:
                    json.dump(user,f,indent=4,separators=(',',': '), ensure_ascii=False)
                    f.close()
                return print('ACCOUNT CREATED: your account {} has been created !\n\nLog in with your login details.'.format(self.username))
    
    def get_id(self):
        return self.id
    
    def get_username(self):
        return self.username

    def get_badge(self):
        return self.badge

    def get_bot(self):
        return self.bot

class login_account:
    def __init__(self, username: str, password: str, module: bool = False):

        user = get_account_data()


        if module:
            if user[username]['username'] == username:
                if user[username]['password'] == password:
                    self.__username__ = username
                    self.__password__ = password
                    self.__bot__ = user[username]['bot']
                    self.__id__ = user[username]['id']
                    self.__badge__ = user[username]['badge']
                else:
                    print('ERROR: wrong password.')
                    return exit()
            else:
                print('ERROR: wrong username.')
                return exit()
        else:
            if user[username]['bot']:
                print('ERROR: You can\'t connect to a bot')
                return exit()
            else:
                if user[username]['username'] == username:
                    if user[username]['password'] == password:
                        self.__username__ = username
                        self.__password__ = password
                        self.__bot__ = user[username]['bot']
                        self.__id__ = user[username]['id']
                        self.__badge__ = user[username]['badge']
                    else:
                        print('ERROR: wrong password.')
                        return exit()
                else:
                    print('ERROR: wrong username.')
                    return exit()

    def get_id(self, username: str):
        user = get_account_data()
        return user[username]['id']

    def get_badge(self, username: str):
        user = get_account_data()
        return user[username]['badge']

    def get_username(self, username: str):
        user = get_account_data()
        return user[username]['username']

    def if_bot(self, username: str):
        user = get_account_data()
        return user[username]['bot']