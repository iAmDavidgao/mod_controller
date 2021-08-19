#(c)SlideToShutdown

import os
import os.path
import time

def p(a):
    print(a)

def cmd(cmd):
    os.system(cmd)

gameversions = ['1.12.2','1.14.4'] #you need to change it
modir = "C:\\users\\david\\downloads\\mc\\.minecraft\\mods" #You need to change it

os.chdir(modir) #change to the mods dir, you can change it

with open("ver.txt","r") as f:
    data = f.readline()
    cmd("move *.jar "+data)
    #read the latest version and put the mods back
    #notice: this text save the version that entered

for i in gameversions:
    os.chdir(modir+"\\"+i)
    cmd("ren *.jar *.disabled")
    #reset all the mods

os.chdir(modir) #back

cmd("cls")

os.chdir(modir) #back

p("The game versions that you have:")
for i in gameversions:
    print(i)
#show the versions


#according to the input to activate the mods
while True:
    input_ver = input("\033[37m"+"pls enter the available versions that you need>")
    if os.path.exists(input_ver):
        p("\033[32m")
        os.chdir(input_ver)
        cmd("ren *.disabled *.jar")
        cmd("move *.jar ..")
        os.chdir(modir)
        with open("ver.txt","w") as f:
            f.write(input_ver)
        p("\033[36m"+"mission success!")
        time.sleep(2)
        break
    else:
        p("\033[31m"+"this game version is not found.")

