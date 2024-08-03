import subprocess
import msvcrt
import os

def smartcontrol():
    print("Do you need help to run SmartCTL?")
    control = input("Enter '1' for help, or any other key to continue: ")
    if control == "1":
        with open("Smartcli Wrapper Info.txt", "w") as p:
            subprocess.run(["smartctl", "--help"], stdout=p, stderr=subprocess.PIPE, text=True)
        print("\t\t\t\t\tPlease check for the Smartcli Wrapper Info.txt for cli usage of SmartCLI \n \n \t ")
    return control

def smarttestschema():
    print("\nChoose an option:")
    print("1: Scan for drives and check health")
    print("2: Show device information")
    test = input("Enter your choice (1 or 2): ")
    
    if test == "1":
        display = subprocess.run(["smartctl", "--scan"], capture_output=True, text=True)
        print("Available drives:")
        print(display.stdout)
        
        drives = display.stdout.splitlines()
        if drives:
            
            first_drive = drives[0].split()[0]
            health = subprocess.run(["smartctl", "--health", first_drive], capture_output=True, text=True)
            print(f"\nHealth information for {first_drive}:")
            print(health.stdout)
        else:
            print("No drives found.")
    elif test == "2":
        display = subprocess.run(["smartctl", "-i", "/dev/sda"], capture_output=True, text=True)
        print(display.stdout)
    else:
        print("Invalid choice.")
    return test

def wait_for_key():
    print("\nPress ESC to exit or any other key to continue...")
    while True:
        if msvcrt.kbhit():
            key = ord(msvcrt.getch())
            if key == 27:  # ESC key
                return False
            return True

def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear screen
        print("SmartCTL Interactive Menu")
        print("=========================")
        
        smartcontrol()
        smarttestschema()
        
        if not wait_for_key():
            break

    print("Exiting the program.")

if __name__ == "__main__":
    main()