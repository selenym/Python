#Adam Asmaca Oyunu

def right_guess(alpha): #Tahmin edilen harf dogruysa "right" donduren, degilse None donduren fonksiyon.
    for i in range(0,len(word)): #Girilen harfi kelimenin icinde kontrol eder.
        if alpha == word[i]: #Eslesen harf varsa eslesen yere harfi koyup oyuncuya gosterir.
            word_control[i]=alpha
            return "right" #Dogruysa "right" donduruyor.
        

def wrong_guess(alpha): #Tahmin edilen harf yanlissa "wrong" donduren, degilse None donduren fonksiyon.
    if right_guess(alpha) == None: #Girilen harf dogru mu ogrenmek icin right_guess() fonksiyonunun ne dondurdugunu kontrol ediyor.
        return "wrong"

print("Welcome to the Hangman Game! Here are the rules:\n1)This game is played with two people.\n2)Player 1 writes the word to be guessed, Player 2 enters the letters and tries to guess the word written by Player 1.\n3)Player 2 has 6 chances.\n")

word=input("Player 1, Enter Your Word:") #1. Oyuncuden kelimeyi alir.
alpha=input("Player2, Enter Your Guess:") #2. Oyuncudan harfleri alir.
list(word) #1. Oyuncudan alinan kelimeyi harflere ayirip listeye donusturur.
word_control = ["_"]*len(word) #Terminale yazdiracagimiz ve oyuncunun gorecegi kelime.
tour = 6 #2. Oyuncunun Can sayisi.

while tour > 0: #Can sayisi 0'dan buyuk oldugu surece oyunu oynamaya devam ediyor.

    if right_guess(alpha) == "right": #Girilen harf dogruysa oyuncuya harfi yerine koyarak yazdiriyor.
        print("Congrats. Right Guess!\n",' '.join(word_control))
        print("Remaining Lives:", tour)

        if "_" not in word_control: #Tum harflerin bulunup bulunmadigini konrol ediyor.
            print("Game Over. Player 2 Win! Player 1 Lost.") #Harflerin hepsi bulunduysa oyuncu kazandi. Donguden cikildi.
            break
        else:
            alpha = input("Enter:") #Tum harfler bulunmadiysa yeni harf girmeye devam edilir.

    elif wrong_guess(alpha) == "wrong": #Girilen harf yanlissa can sayisini 1 eksiltiyor.
        print("Sorry. Wrong Guess!\n",' '.join(word_control)) #Son durumu oyuncuya gosteriyor.
        tour=tour-1
        print("Remaining Lives:", tour)

        if tour == 0: #Can sayisi bitmis mi diye kontrol ediyor. Bittiyse donguden cikiliyor.
            print("Game Over. Player 1 Win! Player 2 Lost.")
            break
        else:
            alpha = input("Enter:") #Bitmediyse Oyuna devam edip yeni bir harf girilmesi isteniyor.
