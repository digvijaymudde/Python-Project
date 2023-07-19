import os
import psutil
import time
from sys import *
import os

def ProcessDisplay(log_dir = "digvijay"):
    listprocess = []

    if not os.path.exists(log_dir):
        try:
            os.mkdir(log_dir)
        except:
            pass

    seperator = "-"*80
    log_path = os.path.join(log_dir,"digvijay%s.log")
    f = open(log_path,'w')
    f.write(seperator + "\n")
    f.write("Digvijay Infosystem process Logger : " "\n")
    f.write(seperator + "\n")

    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid','name','username'])
            vms = proc.memory_info().vms / (1024 * 1024)
            pinfo['vms']=vms
            listprocess.append(pinfo);
        except(psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
            pass

    for element in listprocess:
        f.write("%s\n"% element)

def main():
    print("--------------Marvellous Infosystem Automations-------------------")
    print("Automation script started with name : ",argv[0])

    if(len(argv)!=2):
        print("Error : Insufficent Arguments")
        print("Use -h for help and -u for range of the script")
        exit()

    if(argv[1] == "-h") or (argv[1] == "-H"):
        print("Help : This script is help to perform Log record of running process")
        exit()

    if((argv[1] == "-u") or (argv[1]=="-U")):
        print("Usage : ApplicationName absolutepath ")

        exit()

    try:
        ProcessDisplay(argv[1])
    except ValueError:
        print("Not valid")
    except Exception:
        print("Not valid")


if __name__ =="__main__":
    main()
