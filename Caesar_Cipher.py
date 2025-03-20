# Caesar Cipher

choice=input("Welcome to the Caesar Cipher!\nIf you want to decrypt a password press 1, If you want to encrypt press 2.")

if choice=='1':
    encrypted_text=input("Write the encrypted text:")
    div=int(input("Type the number of digits you want to shift:"))
    liste1=list(encrypted_text)#alınan kelimeyi harflere böldü
    
    for i in range(0,len(liste1)):
       if liste1[i].isalpha():  # Sadece harfleri kaydır
            ascii_offset = ord('A') if liste1[i].isupper() else ord('a')
            liste1[i] = chr((ord(liste1[i]) - ascii_offset - div) % 26 + ascii_offset)

    print("Here's the decrypted password:" , ''.join(liste1)) #listedeki elemanları yan yana yazdırma metodu


elif choice=='2':
    decrypted_text=input("Write the text you want to encrypt:")
    div=int(input("Type the number of digits you want to shift:"))
    liste2=list(decrypted_text) #alınan kelimeyi harflere böldü

    for i in range(0,len(liste2)):
         if liste2[i].isalpha():  # Sadece harfleri kaydır
            ascii_offset = ord('A') if liste2[i].isupper() else ord('a')
            liste2[i] = chr((ord(liste2[i]) - ascii_offset + div) % 26 + ascii_offset)
    
    print("Here's the decrypted password:" , ''.join(liste2)) #listedeki elemanları yan yana yazdırma metodu
