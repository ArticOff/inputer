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
