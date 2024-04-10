
def menu():

    print("""
Menu
-------------
1. Encode
2. Decode
3. Quit""")

def encode():



if __name__ == '__main__':


    while True:
        option = input("Please enter an option: ")

        if option == 1:
            password = input("Please enter your password to encode: ")
            print("Your password has been encoded and stored!")

        if option == 2:
            print("The encoded password is", encode(password) + ", and the original password is" + password)

        if option == 3:
            break



