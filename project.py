#by:Haoran He
#Email:  hrGuTou@gmail.com


alphabet = 'abcdefghijklmnopqrstuvwxyz'  #preset string for the convenience to track the number of the alphabets and shift the alphabets

def encrypt(n,sk):  #This function is to encrypt the original file, it accepts two parameters, which n is the number of shift, sk is the special character
                    # encrypt the file with n number of shift and skip the special character
                    # Any whitespaces, numbers, punctuation marks and UTF8 symbols will be skipped

    fo = open("key.txt", "w")
    fo.write(str(n) + "\n" + sk)
    fo.close()

    fi = open("original.txt", "r")
    originaltext = fi.read()
    originaltext = originaltext.lower()
    result = ''
    for a in originaltext :
        if a == sk:
            result += a.upper()
        elif a.isalpha():
                result += alphabet[(alphabet.index(a) + n) % 25]
        else:
            result += a

    out = open("encrypted.txt" , "w")
    out.write(result)
    out.close()

def decrypt():      #This function is to decrypt the encrypted file with the key.txt file.
                            #It will read the n and sk, the special character in the key.txt and perform reverse encryption
                            #So the output will be the same as the original file
    fi = open("key.txt","r")
    n = int(fi.readline())
    sk = fi.readline()
    fi.close()
    file = open("encrypted.txt", "r")
    txt = file.read()
    txt = txt.lower()
    result = ''
    for a in txt :
        if a.isalpha() and (a != sk):
            result += alphabet[(alphabet.index(a) - n) % 25]      #This is the algorithm that shift each character back based on the n (explain on next page), then store it in the string "result" char by char
        else:
            result += a     #any non alphabet characters and special characters will stay the same and copy directly into the result string

    out = open("decrypted.txt", "w")
    out.write(result)
    out.close()

from random import *

n = randint(-1,25)          #get a random number ranged from -1 to 25 for n shifting
sk = alphabet[randint(0,25)]        #get a random special character that will not be encrypted or decrypted, it will stay the same

encrypt(n,sk)       #call the encrypting function to encrypt
decrypt()           #call the decrypting function to decrypt.
