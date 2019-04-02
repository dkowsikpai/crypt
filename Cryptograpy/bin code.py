i=1
while True:
    binary=input("Enter your binary string "+ str(i)+": ")
    if binary.isdigit():
        print(int(binary,2))
        i+=1
    else:
        break
print("See you !!!")
input()
