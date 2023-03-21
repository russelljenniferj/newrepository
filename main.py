def print_menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")


def encode(passcode):
    encoded = ""
    passcode = str(passcode)
    for i in passcode:
        i = int(i)
        i += 3
        i = str(i)
        encoded += i
    return encoded


def decode(encoded):  # partner fills this in
    pass


def main():
    encoded = ""
    passcode = None
    while True:
        print_menu()
        option = int(input("Please enter an option: "))
        if option == 1:
            passcode = int(input("Please enter your password to encode: "))
            encoded = encode(passcode)
            print("Your password has been encoded and stored!")
        if option == 2:
            encoded = encode(passcode)
            decoded = decode(encoded)
            print(f"The encoded password is {encoded}, and the original password is {passcode}.")
        if option == 3:
            break


if __name__=="__main__":
    main()
