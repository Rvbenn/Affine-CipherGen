

def encrypt():
    plaintxt = input("enter message to encrypt: ")
    keynum1 = int(input("enter a number for the encryption key: "))
    keynum2 = int(input("enter a final number for the encryption key: "))

    #the key consists of two numbers :-)

    i = 0
    listOfPositions = []
     #listOfPositions represents the list of numbers correlating to the position of the letters in the alphabet
    
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    plaintxt2 = plaintxt.replace(" ", "")
    plaintxt2 = plaintxt2.lower()

    for letter in plaintxt2:
        position = alphabet.index(letter)
        listOfPositions.append(position)



    for pos in range(len(listOfPositions)):
        listOfPositions[pos] = listOfPositions[pos] * keynum1



    for _ in range(len(listOfPositions)):
        listOfPositions[_] = listOfPositions[_] + keynum2


    for h in range(len(listOfPositions)):
        listOfPositions[h] = listOfPositions[h]%26
    

    cyphertext = ""
    for newPosition in listOfPositions:
        cyphertext= cyphertext + (alphabet[newPosition])
    print(cyphertext)



def info():
    information = """

THE AFFINE CIPHER is a monoalphabetic substitution cipher.The affine cipher is a method of encryption that uses a pair of integers as
the encryption key. The character set being used, in this case the English alphabet, is assigned numerical values from 0 to n-1, where n is the size of the
character set.Some pairs of integers from this set are not valid as affine encryption keys. To encrypt a message using the affine cipher, the message is first
represented as a series of numbers using the conversion table. These numbers are then multiplied by the first number in the encryption key and the second
number in the key is added to each of them. The resulting numbers are then converted back into their corresponding letters using the following conversion
table to obtain the ciphertext. The cipher is vulnerable against many attacks, including those that work against other substitution ciphers.

0 1 2 3 4 5 6 7 8 9 10 11 12
A B C D E F G H I J  K L  M

13 14 15 16 17 18 19 20 21 22 23 24 25
N  O  P  Q  R  S  T  U  V  W  X  Y  Z



Sources:
https://math.asu.edu/sites/default/files/affine.pdf
https://www.uobabylon.edu.iq/eprints/publication_11_21990_649.pdf

"""
    print(information)



def menu():
    print("This is a simple program that can encode a message of your choice, using the affine cypher")

    print_menu ={
        " ":"",
        "option a":"  encrypt a message using affine",
        "option b":"  open info about the affine cypher + sources",
        "":""}

    for i in print_menu:
        print(i, print_menu[i])

    choice = input("enter your choice: ")
    ab = "ab"
    choice = choice.lower()
    
    if len(choice) > 1:
        print("this input only accepts a or b, sorry!")
        choice = input("enter your choice: ")
    while choice not in ab:
        print("this input only accepts a or b, sorry!")
        choice = input("enter your choice: ")
    
    if choice == "a":
        encrypt()
    elif choice == "b":
        info()
   
menu()
    

        
        
        
        
        
        
