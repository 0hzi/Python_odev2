# Aldığı isim soy isim ile listeye öğrenci ekleyen+
# Aldığı isim soy isim ile eşleşen değeri listeden kaldıran+
# Listeye birden fazla öğrenci eklemeyi mümkün kılan+
# Listedeki tüm öğrencileri tek tek ekrana yazdıran+
# Öğrencinin listedeki index numarası öğrenci numarası olarak kabul edildiğini düşünerek öğrencinin numarasını öğrenmeyi mümkün kılan+
# Listeden birden fazla öğrenci silmeyi mümkün kılan (döngü kullanınız)+
#fonksiyonları geliştiriniz ve her bir fonksiyonu en az bir kere çağırarak konsolda test ediniz+



ogrenciler = [] 
def ogrencisecme():#-->ogrencileri listeye eklediğimiz fonksiyon
      ogrenci = input("Eklemek istediginiz ogrencinin adini soyadini giriniz:")
      ogrenciler.append(ogrenci)
      print("ogrenci eklendi")
      if len(ogrenciler) > 1:
         for i in range(len(ogrenciler)-1):
            if ogrenciler[i]==ogrenci:
               ogrenciler.pop()
               print(f"{ogrenci} isimli ogrenci zaten bulunmaktadir")
               break
            else:
               print("ogrenci eklendi")

def ogrencicikar():#-->ogrencileri listeden cikardigimiz fonksiyon
   cikar = "1"
   while cikar != "0":
      cikar = input("Cikarmak istedigin ogrencinin adini soyadini giriniz(islemi bitirmek icin 0 giriniz):")
      if cikar == "0":
         break
      else:
         ogrenciler.remove(cikar)

def numaraogren():#-->ogrencilerin numaralarını öğrendiğimiz fonskiyon
    for i in range(len(ogrenciler)):
         ogrenci = input("Ogrenci isim soyisim giriniz:")
         print(ogrenciler.index(ogrenci))
         break

def listele():#-->ogrencileri yazdırdığımız fonskiyon
   print(ogrenciler)

def cikis():#-->programı kapattığımız fonskiyon
   print("Cikis yapildi")
   x="2"

x="1"
#--> C dilinde switch case var burdaki karşılığını bilmediğimden while ile yaptım
while x == "1":
   secim = input("1-Ogrenci ekle\n2-Ogrenci cikar\n3-Numara Ogren\n4-Ogrencileri listele\n5-Cikis yap\nislem:")
   if secim == "1":
      ogrencisecme()
   elif secim == "2":
      ogrencicikar()
   elif secim == "3":
      numaraogren()
   elif secim == "4":
      listele()
   elif secim == "5":
      cikis()
      break
   else:
      print("Gecerli bir islem seciniz")