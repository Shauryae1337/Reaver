from ast import Return
import http
import subprocess
import os
import time
import sys

#get working directory 
wd = os.getcwd()

print("""
  ___         _        _ _ _             __       _   _         _      _   _           
 |_ _|_ _  __| |_ __ _| | (_)_ _  __ _  / _|___  | | | |_ __ __| |__ _| |_(_)_ _  __ _ 
  | || ' \(_-|  _/ _` | | | | ' \/ _` | > _|_ _| | |_| | '_ / _` / _` |  _| | ' \/ _` |
 |___|_||_/__/\__\__,_|_|_|_|_||_\__, | \_____|   \___/| .__\__,_\__,_|\__|_|_||_\__, |
                                 |___/                 |_|                       |___/ 
                                                    
                                                      Script by Shaurya |  Reaver v0.1  
""")


#installin github and pip for script kiddies  :) 
subprocess.run(["sudo","apt-get","install","git","-y"])
subprocess.run(["sudo","apt-get","install","python3-pip","-y"])

#installing nmap & checking version
subprocess.run(["sudo","apt-get","install","nmap","-y"])
#subprocess.run(["nmap","--version"])

#installing nikto & checking version
subprocess.run(["sudo","apt-get","install","nikto","-y"])
#subprocess.run(["nikto"])

#installing wpscan, ruby, & checking version
subprocess.run(["sudo","apt","install","ruby-full","-y"])
subprocess.run(["sudo","gem","install","wpscan"])
#subprocess.run(["wpscan","--version"])

#installing nuclie and dependencies
subprocess.run(["sudo","apt-get","install","golang","-y"])
subprocess.run(["git","clone","https://github.com/projectdiscovery/nuclei.git"])

#get current directory to get into nuclie folder
os.chdir(wd+"/nuclei/v2/cmd/nuclei")
subprocess.run(["go","build"])
subprocess.run(["sudo","mv","nuclei","/usr/local/bin/"])
#subprocess.run(["nuclei","-version"])
os.chdir(wd)
#subprocess.Popen("ls")

#installing assetfinder for subdomain search
subprocess.run(["go","install","-v","github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest"])
subprocess.run(["sudo","cp","/root/go/bin/assetfinder","/usr/local/bin/"])
os.chdir("..")
subprocess.run(["sudo","cp","go/bin/assetfinder","/usr/local/bin/"])
os.chdir(wd)

#installing amass and configuration
subprocess.run(["go","install","-v","github.com/OWASP/Amass/v3/...@master"])
os.chdir("..")
#subprocess.Popen("ls")
subprocess.run(["sudo","cp","go/bin/amass","/usr/local/bin/"])
os.chdir(wd)
#subprocess.Popen("ls")
#subprocess.run(["amass"])

#installing Subdomainizer
subprocess.run(["git","clone","https://github.com/nsonaniya2010/SubDomainizer.git"])
os.chdir(wd+"/SubDomainizer")
subprocess.run(["pip3","install","-r","requirements.txt"])
os.chdir(wd)
#subprocess.Popen("ls")
#subprocess.run([""])

#installing httprobe
subprocess.run(["go","install","github.com/tomnomnom/httprobe@latest"])
os.chdir("..")
subprocess.run(["sudo","cp","go/bin/httprobe","/usr/local/bin/"])
os.chdir(wd)
#subprocess.Popen("ls")
#subprocess.run(["httprobe","-h"])

#installing httpx
subprocess.run(["go","install","-v","github.com/projectdiscovery/httpx/cmd/httpx@latest"])
os.chdir("..")
subprocess.run(["sudo","cp","go/bin/httpx","/usr/local/bin/"])
os.chdir(wd)
#subprocess.run(["httpx","-h"])

#installing wafw00f
subprocess.run(["git","clone","https://github.com/EnableSecurity/wafw00f"])
os.chdir(wd+"/wafw00f")
subprocess.run(["sudo","python3","setup.py","install"])
#subprocess.run(["wafw00f","-l"])
os.chdir(wd)

#installing subjack
subprocess.run(["go","install","github.com/haccer/subjack@latest"])
os.chdir("..")
subprocess.run(["sudo","cp","go/bin/subjack","/usr/local/bin/"])
subprocess.run(["sudo","mkdir","-p","src/github.com/haccer/subjack"])

#subprocess.run(["subjack","-h"])
os.chdir(wd)

#installing dnsx
subprocess.run(["go","install","-v","github.com/projectdiscovery/dnsx/cmd/dnsx@latest"])
os.chdir("..")
subprocess.run(["sudo","cp","go/bin/dnsx","/usr/local/bin/"])
#subprocess.run(["dnsx","-h"])
os.chdir(wd)

#installing xsstrike
subprocess.run(["git","clone","https://github.com/s0md3v/XSStrike"])
os.chdir(wd+"/XSStrike")
subprocess.run(["pip3","install","-r","requirements.txt"])
#subprocess.run(["python3","xsstrike.py","-h"])
os.chdir(wd)

subprocess.run(["clear"])


print("""
  ____                                       
 |  _ \    ___    __ _  __   __   ___   _ __ 
 | |_) |  / _ \  / _` | \ \ / /  / _ \ | '__|
 |  _ <  |  __/ | (_| |  \ V /  |  __/ | |   
 |_| \_\  \___|  \__,_|   \_/    \___| |_|   
                              
 Script by Shaurya |  Reaver v0.1 
 
""")

print("""Enter the domain without https:// or wwww

""")

def typingPrint(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05)
  
def typingInput(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05)
  value = input()  
  return value  

    
domain = input()

print("The target domain is ",domain)

url="https://" + domain

def myping(host):
    response = os.system("ping -c 1 " + host)
    
    if response == 0:
        print("""
        
        The target domain is active
        
        """)
        print(""" 
        Tools Available for Scanning

        1.  Complete Scan (Recommended)
        2.  Nmap 
        3.  Nikto
        4.  Nuclie
        5.  Assetfinder
        6.  Wpscan
        7.  :) Will Add Later
        8.  httprobe
        9.  httpx
        10. wafw00f
        11. subjack
        12. dnsx
        13. XSStrike
        14. Exit


        Enter the option number you would like to use

        """)
          
        option = input()
        print("Executing", option ,"on",domain)
        if option == '1':
          all()


        elif option == '2':
          print()
          nmap()
        elif option == '3':
          print()
          nikto()
        elif option == '4':
          print()
          nuclie()
        elif option == '5':
          print()
          assetfinder()
        elif option =='6':
          print()
          wpscan()
        elif option =='7':
          print("I know you're Looking for Rabbit holes but my friend but")
          time.sleep(1)
          time.sleep(1)
          print(""" 
          ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⢛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠛⠛⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠉⣡⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⡘⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⡿⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⣤⣷⣭⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠋⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠈⠛⠋⠩⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⡿⠀⠉⢢⣀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣷⠙⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠓⠶⠂⠀⠘⢎⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡿⢣⣿⣿⡿⠛⠛⠛⢿⣿⣿⣿⡏⠠⢀⣀⠀⠄⠀⢈⣼⣿⡿⠛⠛⠻⢿⣿⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠚⠀⣾⣿⣿⠳⡆⢀⠀⢸⣿⣿⣿⣇⠀⠈⠉⠁⠀⡠⠊⣿⣿⡇⠀⠀⠀⠀⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⢻⣿⡆⠁⠹⠀⢸⣿⣿⣿⣧⣽⣦⣤⣤⣮⣶⣾⣿⣿⡇⠀⠀⠀⠀⣿⣿⣿⣇⢻⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡼⠃⣾⣿⣧⠀⠀⢦⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠲⢤⠀⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⠿⠿⠿⠷⣄⡈⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⠖⠛⠛⡛⠿⢇⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠔⣫⠀⠀⠀⠀⠀⠀⠨⢃⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠈⣥⣀⠉⠢⢄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠊⠀⠈⠀⠀⠸⡀⠀⣀⣤⢏⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡹⢲⣄⠀⠀⠀⠉⠃⠀⠃⠉⠢⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠟⠛⠲⠤⡤⡲⠀⠀⣀⣵⣾⣿⣿⡆⢂⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢇⢣⣿⣿⣿⣦⣀⠀⠈⠑⣕⢴⠒⠛⡛⢧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠋⠀⢴⠀⠪⠞⣹⣧⣾⣿⣿⣿⣿⣿⣿⣈⡾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣨⣾⣿⣿⣿⣿⣿⣷⣤⣺⡄⠓⠃⠀⠈⢻⢱⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡼⠃⠀⠀⣠⠖⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄⠀⠀⠀⠀⢀⢣⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡸⠁⠀⠴⠚⠁⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⡄⠸⠄⢃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣴⣅⡀⢠⣢⠑⠆⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⢡⢠⢀⡠⠧⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡟⠀⡄⣩⣳⢧⡄⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣤⡔⢣⣣⡄⡀⠘⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡎⠀⢀⣗⠁⠁⣼⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⢗⡃⢠⠘⡄⠀⠀⠀

⠀⠀⠀⠀⠀⠀⠀
          """)
          time.sleep(1)
          typingPrint("""
             Wake up to reality! Nothing ever goes as planned in this accursed world.
            The longer you live, the more you realize that the only things that truly
                 exist in this reality are merely pain, suffering and futility.
               Listen, everywhere you look in this world, wherever there is light,
              there will always be shadows to be found as well. As long as there is
             a concept of victors, the vanquished will also exist. The selfish intent
           of wanting to preserve peace, initiates war and hatred is born in order to
          protect love. There are nexuses causal relationships that cannot be separated.
          """)
          time.sleep(1)
          exit()
        elif option =='8':
          print()
          httprobe()
        elif option =='9':
          print()
          httpx()
        elif option =='10':
          print()
          wafw00f()
        elif option =='11':
          print()
          subjack()
        elif option =='12':
          print()
          dnsx()
        elif option =='13':
          print()
          xsstrike()
        elif option =='14':
          print()
          exit()

        return True
    else:
        print("Host seems to be down")
        return False
        
os.chdir(wd)
#subprocess.Popen("ls")
def nmap():
    subprocess.run(["sudo","nmap","-p-","-sS","-T4","-v","-A",domain,"-oN","nmap.txt"])
def nikto():
    subprocess.run(["nikto","-h",domain,"-o","nikto.txt"])
def nuclie():
    subprocess.run(["nuclei","-u",url,"-o","nuclie.txt"])
def assetfinder():
    command1 = "assetfinder "
    command2 = " > subdomains.txt"
    output = subprocess.check_output(["bash", "-c",command1+domain+command2])




def httprobe():
    assetfinder()
    command = "cat subdomains.txt | httprobe > https.txt"
    output = subprocess.check_output(["bash", "-c", command])

def httpx():
    assetfinder()
    httprobe()
    command = "httpx -status-code -tech-detect -title -ct -location -server -ip -cname -list https.txt -json sitescan.json -o sitescan.txt" 
    output = subprocess.check_output(["bash", "-c", command])

def wafw00f():
    assetfinder()
    subprocess.run(["wafw00f","-i","subdomains.txt","-o","waf.txt"])
def subjack():
    assetfinder()
    command = "subjack -w subdomains.txt -v > subjack.txt"
    output = subprocess.check_output(["bash", "-c", command])

def dnsx():
    assetfinder()
    command = "dnsx -resp -a -aaaa -cname -mx -soa -txt -l subdomains.txt > dnsx.txt"
    output = subprocess.check_output(["bash", "-c", command])

def xsstrike():
    httprobe()
    subprocess.run(["cp","https.txt","XSStrike/subdomains.txt"])
    os.chdir(wd+"/XSStrike")
    
    command="python3 xsstrike.py --crawl -l 8 -t 20 --seeds subdomains.txt > xsstrike.txt"
    output = subprocess.check_output(["bash", "-c", command])
    os.chdir(wd)
    subprocess.run(["cp","XSStrike/xsstrike.txt","xsstrike.txt"])


def wpscan():
    print("Enter the wpscan api token to enumerate vulnerabilities, or leave empty to proceed without token")
    token = input()
    if len(token) > 5:
      subprocess.run(["wpscan","--api-token",token,"--url",domain,"-o","wpscan.txt"])
      return True
    else:
      print("Proceeding without Token")
      subprocess.run(["wpscan","--url",domain,"-o","wpscan.txt"])
      return False

def all():
          nmap()
          nikto()
          assetfinder()
          httprobe()
          httpx()
          wafw00f()
          subjack()
          dnsx()
          xsstrike()
          wpscan()
          subprocess.run(["clear"])
          print("""
  ____                                       
 |  _ \    ___    __ _  __   __   ___   _ __ 
 | |_) |  / _ \  / _` | \ \ / /  / _ \ | '__|
 |  _ <  |  __/ | (_| |  \ V /  |  __/ | |   
 |_| \_\  \___|  \__,_|   \_/    \___| |_|   
                              
 Script by Shaurya |  Reaver v0.1 
 
""")

          print("""Generating Report in """)
          time.sleep(1)
          typingPrint("3..")
          time.sleep(1)
          typingPrint("3..")
          time.sleep(1)
          report()
          


    
def exit():
    command = "exit"
    output = subprocess.check_output(["bash", "-c", command])

myping(domain)


filenames = ['nmap.txt', 'nikto.txt', 'nuclie.txt','subdomains.txt','https.txt', 'subjack.txt', 'sitescan.txt','waf.txt','subjack.txt', 'dnsx.txt','xsstrike.txt','wpscan.txt']
  

with open('report.txt', 'w') as outfile:
  

    for names in filenames:
  
        with open(names) as infile:
  
            
            outfile.write(infile.read())
  
        outfile.write("\n")

def report():
    command = "cat report.txt"
    output = subprocess.check_output(["bash", "-c", command])



