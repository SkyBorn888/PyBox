from ast import arg
import os
import sys

ver3 = 'py3'
ver2 = 'py2'
ver = 'py'
uninstall = 'uninstall'
install = 'install'
args = sys.argv
status = 'status'
manual = 'manual'


### Install

def Install(ver2, ver3):

    if args[2] == ver2:
            print('python2 setup')
            os.system('~/Pydo/setup/install py2')

    elif args[2] == ver3:
            print('python3 setup')
            os.system('~/Pydo/setup/install py3')
    elif args[2] == ver:
            print('python setup')
            os.system('~/Pydo/setup/install py')

    print('\n ### Done ### \n')
    sys.exit()


### Uninstall

def Uninstall():

    os.system('~/Pydo/setup/uninstall')

    print('\n ### complete ### \n') 
    sys.exit()

### what venv using version of python

def Status():
    isthere3 = os.path.isfile("~/Pydo/pydoenv/bin/python3")
    isthere2 = os.path.isfile("~/Pydo/pydoenv/bin/python2")
    if isthere3 == True:
        print("python3")
    elif isthere2 == True:
        print("python2")
    else:
        print("")
        print("Please wait a update")
        
def Manual():
    f = open('manual.txt', 'r', encoding='UTF-8')
    print(f)


try:

    if str(args[1]) == install:
        Install(ver2, ver3)

    elif str(args[1]) == uninstall:
        Uninstall()

    elif str(args[1]) == status:
        Status()
    
    elif str(arg[1]) == manual:
        Manual()
    else:
        Manual()

except KeyboardInterrupt:

    print('stop')
    sys.exit()