import time
##bir dizide istenilen elemanı bulmak için geçen süreyi hesaplayan algoritma

kontrol=0
dizi=[]
for j in range(0,10000000):
    dizi.append(j)

n=int(input("Bulmak istediğiniz sayiyi yazin:"))
length = int(len(dizi))
#dizinin uzunlugunu buluyoruz

start = time.time()
for i in range(0,int(length/2)):
    if(n==dizi[i]):
        kontrol=1
        print("Aradiginiz elemanin index:", i)
        end_time =time.time()
        print("Gecen sure:",round(end_time-start, 6))
        break

    elif(n==dizi[length-i-1]):
        kontrol=1
        print("Aradiginiz elemanin index:" , length-i-1)
        end_time = time.time()
        print("Gecen sure:", round(end_time-start, 6))
        break

if(kontrol==0):
    end_time = time.time()
    print(end_time-start,"İndex bulunamadi!Tekrar deneyin.")




