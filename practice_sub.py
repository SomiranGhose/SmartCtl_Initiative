import subprocess
import os

def smartcontrol():
    control = input("Do you need help to run : \t")
    if control == "1":
        with open("Smartcli Wrapper Info.txt", "w") as p:
            displayhelp = subprocess.run(["smartctl", "--usage"], stdout=p, stderr=subprocess.PIPE, text=True)
            print("\t\t\t\t\tPlease check for the Smartcli Wrapper Info.txt for cli usage of SmartCLI \n \n \t ")
            return control


def smarttestschema():
    test = input("\t\nScan for drives in the env: \t")
    if test == "1":
        display = subprocess.run(["smartctl","--health","1"], stdout=subprocess.PIPE , stderr=subprocess.PIPE,text=True)
        print(display)
        return test
    elif test == "2":
        display = subprocess.run(["smartctl","-c"], stdout=subprocess.PIPE , stderr=subprocess.PIPE,text=True)
        print(display)
        return test
        
def main():
    print("Cli Tool")
    while True:
        smartcontrol()
        smarttestschema()
        
        
        




        '''with open ("Smartoutput.txt" , "w") as f:
            results = subprocess.run(["smartctl","--scan-open"] , stderr=subprocess.PIPE , stdout=f , text=True)'''
            
if __name__ == "__main__":
    main()
