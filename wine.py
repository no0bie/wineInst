import os,sys,time
try:
    a = sys.argv[1]
    if a == "build":
        print("Installing wine")
        time.sleep(2)
        os.system("dpkg --add-architecture i386")
	print("Updating...")
	time.sleep(2)
        os.system("apt-get update")
        os.system("clear")
	print("Upgrading...")
	time.sleep(2)
        os.system("apt-get upgrade")
        os.system("clear")
	print("Installing Wine...")
	time.sleep(2)
        os.system("apt-get install wine")
        os.system("clear")
	print("Installing WineTricks...")
	time.sleep(2)
        os.system("apt-get install winetricks")
        os.system("clear")
	print("Installing Wine32")
	time.sleep(2)
        os.system("apt-get install wine32")
        os.system("clear")
	print("Starting Wine config...")
	time.sleep(2)
        os.system("winecfg")
    elif a == "-s":
        os.system("wget https://www.shellterproject.com/Downloads/Shellter/Latest/shellter.zip")
        os.system("clear")
        os.system("unzip shellter.zip")
        os.system("rm shellter.zip")
    else:
        print("Help Menu")
        print("1 - Before any command type sudo bash then you can use one of the following")
        print("2 - Use python wine.py build to install")
        print("3 - Use python wine.py -s to install shellter")
        

except:
    print("Help Menu")
    print("1 - Before any command type sudo bash then you can use one of the following")
    print("2 - Use python wine.py build to install")
    print("3 - Use python wine.py -s to install shellter")
