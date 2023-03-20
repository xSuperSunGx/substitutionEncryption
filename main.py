# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Strg+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
alphabetlist = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']





def encrypt(plaintext, cipher):
    plaintext = plaintext.upper()
    cipher = cipher.upper()
    ciphertext = ""
    for i in range(len(plaintext)):
        if plaintext[i] in alphabetlist:
            ciphertext += alphabetlist[(alphabetlist.index(plaintext[i]) + alphabetlist.index(cipher[i % len(cipher)])) % 26]
        else:
            ciphertext += plaintext[i]
    return ciphertext

if __name__ == '__main__':

    print(encrypt(input("Enter plaintext: "), input("Enter cipher: ")))

#   while True:
#        print((lambda x: (alphabetlist[(alphabetlist.index(x[0].upper()) - alphabetlist.index(x[1].upper())) % 26]))(input("Enter first letter: ")))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
