# Lauren Lessne

def menu():

    print("""
Menu
-------------
1. Encode
2. Decode
3. Quit""")
    pass

def encode(password):
    list = [i for i in password]
    list = (map(int, list))
    encode = [x+3 for x in list]
    encodeFINAL = ''.join(str(i) for i in encode)
    return encodeFINAL

def decode(encoded):
# Partner Code


if __name__ == '__main__':

    menu()

    while True:
        option = input("\nPlease enter an option: ")

        if option == "1":
            password = input("Please enter your password to encode: ")
            print("Your password has been encoded and stored!")

        if option == "2":
            print("The encoded password is " + encode(password) +", and the original password is", password +".")

        if option == "3":
            break







