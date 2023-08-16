
print("Welcme to the world of cryptography only for hackers")

def main():
    print()
    print("Choose one option")
    choice = int(input("1. Encryption\n2. Decryption\nChoose(1,2): "))
    if choice == 1:
        encryption()
    elif choice == 2:
        decryption()
    else:
        print("Wrong Choice")


def encryption():
    print("encription")
    msg=input("Enter your message  :      ")
    key=int(input("Enter Key 1-94: "))
    et=""
    for i in range (len(msg)):
        temp=(ord(msg[i])+key)
        if(temp>126):
            temp=temp-127+32
            
        et+=chr(temp)    
    print("encripted : "+ et)
    main()

    


def decryption():
    print("decryption")
    print("only lower or upper case idiots ")
    en_msg=input("Enter the ecnyp. text  : ")
    dec_key=int(input("Enter Key 1-94 : "))
    dt=""
    for i in range (len(en_msg)):
        temp=(ord(en_msg[i])-dec_key)
        if(temp<32):
            temp=temp+127-32
            
        dt+=chr(temp)    
    print("decrypted : "+ dt)
    main()




    
    

        
if __name__ == "__main__":
    main()
