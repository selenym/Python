#Morce Code Translator

#2 boyutlu dizi şeklinde eşleştirmeli olarak mors kodlarını yazdık.
morse_codes = [[".-","A"],["-...","B"],["-.-.","C"],["-..","D"],[".","E"],["..-.","F"],["--.","G"],
             ["....","H"],["..","I"],[".---","J"],["-.-","K"],[".-..","L"],["--","M"],["-.","N"],
             ["---","O"],[".--.","P"],["--.-","Q"],[".-.","R"],["...","S"],["-","T"],["..-","U"],
             ["...-","V"],[".--","W"],["-..-","X"],["-.--","Y"],["--..","Z"],[".-.-.-","."],
             ["--..--",","],["..--..","?"],["/"," "]]

#Mors kodunu texte çeviren fonksiyon
def cevap():
    password=input("Write the morse code:")
    control=list(password.split(" ")) #Mors kodunu boşluklardan ayrıdık ve kontrol edeceğimiz diziye ekledik.
    cevap= [None]*len(control) #Cevirdiğimiz mors kodlarını tutmak için liste oluşturduk.
    
    for i in range(0,len(morse_codes)):
        for j in range(0,len(control)):
            if control[j]==morse_codes[i][0]: #Eşleşen kodları kontrol eder.
                cevap[j]=morse_codes[i][1] #Kodu harfe çevirir.
                
    print("sifre:" , ''.join(cevap)) #Listeyi yan yana yazdıran metod.

#Texti mors koduna çeviren fonksiyon
def morse():
    password=input("Write the text:")
    control=list(password.upper()) #Once texti büyük harfe çevirdik. Sonra texti harflere ayırdık ve kontrol edeceğimiz diziye çevirdik.
    cevap= [None]*len(control) #Cevirdiğimiz harfleri tutmak için liste oluşturduk.
    
    for i in range(0,len(morse_codes)):
        for j in range(0,len(control)):
            if control[j]==morse_codes[i][1]: #Eşleşen harfleri kontrol eder.
                cevap[j]=morse_codes[i][0] #Harfi koda çevirir.

    print("sifre:" , ' '.join(cevap)) #Araya bosluk koyarak listeyi yan yana yazdıran metod. 

choice=input(("Welcome to the Morse Code Translator!\nIf you want to encrypt a morse code write 1. If you wamt to turn your text into morse code write 2:"))

if choice=='1':
    cevap()
else:
    morse()