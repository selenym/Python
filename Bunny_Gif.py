#Gerekli kütüphaneyi içe aktarıyoruz. 
#Bu modül görüntü okuma ve yazma işlemleri için kullanılır.
import imageio.v3 as iio

# GIF oluşturmak için kullanılacak resim dosyalarının adlarını içeren bir liste oluşturuyoruz.
filenames = ['bunny_1.jpg', 'bunny_2.jpg']
# Resimleri saklayacağımız boş bir liste oluşturuyoruz.
images = [ ]

# Belirtilen dosya adlarını tek tek işleyerek listeye ekliyoruz.
for filename in filenames:
  #iio.imread() fonksiyonu, dosya adını parametre olarak alır, resmi okur ve döndürür.
  #Daha sonra append() komutuyla okunan resmi images listesine ekliyoruz.
  images.append(iio.imread(filename))

# iio.imwrite() fonksiyonu ile görüntüleri birleştirerek GIF formatında kaydediyoruz.
# 'bunny.gif' adıyla bir GIF dosyası oluşturuluyor.
# duration = 500 → Her kare 500 milisaniye (0.5 saniye) boyunca gösterilecek.
# loop = 0 → GIF sonsuz döngü halinde tekrar oynatılacak.
  iio.imwrite('bunny.gif', images, duration = 500, loop = 0)
