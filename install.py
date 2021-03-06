'''
The MIT License (MIT)

Copyright (c) 2014 NTHUOJ team

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

import getpass

# Setting nthuoj.ini
host = raw_input("Mysql host: ")
db = raw_input("Mysql database: ")
user = raw_input("Please input your mysql user: ")
pwd = getpass.getpass()

# Re-write nthuoj.ini file
iniFile = open("nthuoj.ini", "w")
iniFile.write("[client]\n")
iniFile.write("host = %s\n" % host)
iniFile.write("database = %s\n" % db)
iniFile.write("user = %s\n" % user)
iniFile.write("password = %s\n" % pwd)
iniFile.write("default-character-set = utf8\n")
iniFile.close()


# Install needed library

