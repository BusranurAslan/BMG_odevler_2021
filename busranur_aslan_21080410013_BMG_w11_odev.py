
#isim Listesini tanımlayınız. 
kisiler=[]


#kisi isimlerini ekrana yazdıralım 
a=input("isim giriniz:")
kisiler.append(a)
b=input("isim giriniz:")
kisiler.append(b)
c=input("isim giriniz:")
kisiler.append(c)
print("Liste:")
print(kisiler)

#Liste uzunlugunu hesaplayalım 
print("Liste uzunlugu:")
uzunluk= len(kisiler)
print(uzunluk)

#Listede 2. kisinin ismini ekrana yazdıralım
print("Listedeki 2. kisi:")
print(kisiler[1])


#Listedeki son ismi  çıkarma ve ekrana yazdırma ve yapma işlemi
kisiler.pop()
print("Listedeki son kisi cıkarıldı,Yeni Liste:")
print(kisiler)