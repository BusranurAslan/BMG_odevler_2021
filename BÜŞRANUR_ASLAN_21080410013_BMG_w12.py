#verilen tabloyu sınav_sonuc listesi olarak tanımladım
sinav_sonuc = {'isimler':['ayse K.','Ahmet M.','Nuri C.','Nawar T.','Suzan T.','Ala B.'],
'cinsiyet':['K','E','E','E','K','K'],
'mat':[60,40,97,45,56,93 ],
'turkce':[70,30,23,80,78,46]}

#isimler, cinsiyet,matematik , türkçe puanlarını ekrana yazdırdım
print(sinav_sonuc['isimler'])
print(sinav_sonuc['cinsiyet'])
print(sinav_sonuc['mat'])
print(sinav_sonuc['turkce'])

kadinlarin_turkce_notlari = []
erkeklerin_turkce_notlari = []
count_k = 0
count_e = 0
k_mat = 0
e_mat = 0
k_turk = 0
e_turk = 0

#gereken hesaplamalar için döngü halinde yazdım
for i in range(len(sinav_sonuc['cinsiyet'])):
    if sinav_sonuc['cinsiyet'][i] == 'K':
        count_k +=1
        k_mat = k_mat + sinav_sonuc['mat'][i]
        k_turk = k_turk + sinav_sonuc['turkce'][i]
        kadinlarin_turkce_notlari.append(sinav_sonuc['turkce'][i])
    else :
        count_e += 1
        e_mat = e_mat + sinav_sonuc['mat'][i]
        e_turk = e_turk + sinav_sonuc['turkce'][i]
        erkeklerin_turkce_notlari.append(sinav_sonuc['turkce'][i])

#Matematik sınav sonucunu kadın ve erkekler için ayrı ayrı ortalamalarını aldım
#türkçe sınavının sınıf ortalamasını tek printf içinde aldım
print(f"Erkek Matatematik Ortalamasi: {e_mat/count_e}\n\
Kadinlarin Matematik Ortalamasi: {k_mat/count_k}\n\
Turkce Dersinin Ortalamasi : {(k_turk + e_turk)/(count_e + count_k)}") 

#Kadın ve erkeklerin max ders notlarını ekrana yazdırdım
print("Kadinlarin En Yuksek Turkce Notu : ", max(kadinlarin_turkce_notlari))
print("Erkeklerin En Yuksek Turkce Notu : ", max(erkeklerin_turkce_notlari))
