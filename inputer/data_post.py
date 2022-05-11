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

def get_account_data():
    with open('database.json', encoding='utf-8') as f:
        user = json.load(f)
        f.close()
    return user

class open_account:
    def __init__(self, username: str, password: str):
        id = random.randint(1, 10000)
        badge = '[MEMBER]'

        self.username = username
        self.password = password 
        self.id = id
        self.badge = badge

        user = get_account_data()

        if str(self.username) in user:
            return print('ERROR: this account already exists.')

        else:
            
            if len(self.password) <= 8:
                return print('ERROR: The password must be more than 8 characters long. (It is {} characters long)'.format(len(self.password)))
                
            else:
                user[str(self.username)] = {}
                user[str(self.username)]['id'] = str(self.id)
                user[str(self.username)]['username'] = self.username
                user[str(self.username)]['password'] = self.password
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

class login_account:
    def __init__(self, username: str, password: str):

        user = get_account_data()

        if user[username]['username'] == username or user[username]['password'] == password:
            self.__username__ = username
            self.__password__ = password 
            self.__id__ = user[username]['id']
            self.__badge__ = user[username]['badge']
        else:
            print('ERROR: wrong password or username.')
            exit()

    def get_id(self, username: str):
        user = get_account_data()
        return user[username]['id']

    def get_badge(self, username: str):
        user = get_account_data()
        return user[username]['badge']

    def get_username(self, username: str):
        user = get_account_data()
        return user[username]['username']