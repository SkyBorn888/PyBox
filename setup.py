import os
import sys

ver3 = 'version-3'
ver2 = 'version-2'
ver = 'version-default'
uninstall = 'uninstall'
install = 'install'
args = sys.argv
status = 'status'
manual = 'manual'


### Install

def Install(ver2, ver3):

    if args[2] == ver2:
        print('python2 setup')
        os.system('~/PyBox/setup/install version-2')
        print('\n ### Done ### \n')
        sys.exit()
    elif args[2] == ver3:
        print('python3 setup')
        os.system('~/PyBox/setup/install version-3')
        print('\n ### Done ### \n')
        sys.exit()
    elif args[2] == ver:
        print('python setup')
        os.system('~/PyBox/setup/install version-default')
        print('\n ### Done ### \n')
        sys.exit()
    else:
        Manual()
        print(" ")
        print("###### Not found " + str(args[2]) + " options ######")
        sys.exit()



### Uninstall

def Uninstall():

    os.system('~/PyBox/setup/uninstall')

    #print('\n ### complete ### \n') 
    sys.exit()

### what venv using version of python

def Status():
    isthere3 = os.path.isfile("~/PyBox/pyboxenv/bin/python3")
    isthere2 = os.path.isfile("~/PyBox/pyboxenv/bin/python2")
    if isthere3 == True:
        print("python3")
    elif isthere2 == True:
        print("python2")
    else:
        print("")
        print("Please wait a update")
        
def Manual(): 
    f = open('manual.txt', 'r', encoding='UTF-8')
    words = f.read() ##feature/Update-2
    print(words)
    f.close()


try:

    if str(args[1]) == install:
        Install(ver2, ver3)

    elif str(args[1]) == uninstall:
        Uninstall()

    elif str(args[1]) == status:
        Status()
    
    elif str(args[1]) == manual:
        Manual()
    else:
        Manual()

except KeyboardInterrupt:

    print('stop')
    sys.exit()