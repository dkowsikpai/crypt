def encrypt(text,s):
    result = ""
    # transverse the plain text
    for i in range(len(text)):
        char = text[i]
        # Encrypt uppercase characters in plain text
        if (char.isupper()):
            #result += chr((ord(char) + s-65) % 26 + 65)
            result += chr((ord(char) + s))
            # Encrypt lowercase characters in plain text
        else:
            #result += chr((ord(char) + s - 97) % 26 + 97)
            result += chr((ord(char) + s))
    return result

def decrypt(text,s):
    result = ""
    # transverse the plain text
    for i in range(len(text)):
        char = text[i]
        # Encrypt uppercase characters in plain text
        if (char.isupper()):
            #result += chr((ord(char) + s-65) % 26 + 65)
            result += chr((ord(char) - s))
            # Encrypt lowercase characters in plain text
        else:
            #result += chr((ord(char) + s - 97) % 26 + 97)
            result += chr((ord(char) - s))
    return result



#check the above function
#text = "CEASER CIPHER DEMO"
text=input("Enter text to get decript code: ")
s = len(text)
print ("Plain Text : " + text)
#print ("Shift pattern : " + str(s))

cipher=encrypt(text,s)
print ("Cipher: " + cipher)
print ("Decrypt: "+ decrypt(cipher,s))
