# Ensuring bettre security by not providing decryption tool. So that eac time the text has to be changed to cipher then validated.
# Reason 1: The position of the charecter must affect the password.

def encrypt (text):
    result = ""
    for i in range(len(text)):
        s=len(text)+i+text.index(text[i])
        char = text[i]
        encrpy=[]
        if (char.isupper()):
            encrpy=(str(bin((ord(char) + s-65) % 26 + 65))).split("0b")
            result +=("".join(encrpy)) 
        elif(char.islower()):
            encrpy=(str(bin((ord(char) + s - 97) % 26 + 97))).split("0b")
            result +=("".join(encrpy))
            #result += str(bin((ord(char) + s - ord('a')) % 26 + ord('a')))
        else:
            encrpy=(str(bin((ord(char) + s - 32) % 33 + 32))).split("0b")
            result +=("".join(encrpy))            
    return result

text=input("Enter text to get encript code: ")
s = len(text)
print ("Plain Text : " + text)
cipher=encrypt(text)
print ("Cipher: " + cipher)
input()

"""if (char.isupper()):
            result += chr((ord(char) + s-ord('A')) % 26 + 65)
        else:
            result += chr((ord(char) + s - ord('a')) % 26 + 97)
"""
