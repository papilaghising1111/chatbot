from utility.utility import *

def main():
    while True:
        ip = input('Papila: ')
        # if user types "exit", the bot will terminate the program.
        if(ip=="exit"):
            exit(0)
        print('Bot: ' + get_response(ip))
        print("\n")
    

if __name__ == "__main__":
    main()