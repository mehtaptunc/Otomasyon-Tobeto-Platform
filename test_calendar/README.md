# Test Senaryosu 
Adı :Takvim işlevselliğinin  kontrolü
Açıklama : Takvimde haftalık olarak dersleri görüntüleyebilmeli , hangi gün ve hangi saatte eğitim olduğunu , eğitim içeriği ve eğitmen bilgisi hakkında bilgileri takvimdeki günler tablosunda görüntüleyebilmelidir.
Ön Koşul : Test ortamı çalışır ve hazır durumda olmalıdır.  Tobeto anasayfasına sayfasına girilmiş olmalıdır, sol alt kısmındaki takvim simgesine tıklayarak "Eğitim ve Etkinlik Takvimi" sayfasına erişebilmelidir.

# Case 1: Takvim başlığının gösterilmesi 
    Adım1: Tobeto anasayfaya gir.
    İnput: https://tobeto.com/giris
    Adım2: Sol alt kısmındaki takvim simgesine tıkla.
    Adım3: Açılan pop–up da eğitim durumu  check box larının hepsini işaretle.
Beklenen Sonuç:" Eğitim ve Etkinlik Takvimi' olarak bekleniyor."

![alt text](image.png)

# Case 2: Filtresiz tüm eğitimlerin takvim üzerinde gösterilmesi
	Adım1: Tobeto anasayfaya gir.
    İnput: https://tobeto.com/giris
    Adım2: Sol alt kısmındaki takvim simgesine tıkla.
    Adım3: Açılan pop–up da eğitim durumu  check box larının hepsini işaretle.
Beklenen Sonuç :  Takvim üzerinde eğitimler, eğitim saat , tarihleri ve eğitmenler  görüntülenebilmelidir.

![alt text](image-1.png)

# Case 3: Eğitim arama filtresinin kontrolü
	Adım1: Tobeto anasayfaya gir.
    İnput: https://tobeto.com/giris
    Adım2: Sol alt kısmındaki takvim simgesine tıkla.
    Adım3: Açılan pop–up da eğitim durumu  check box larının hepsini işaretle.
    Adım4:Eğitim arama inputu içerisine bulmak istediğin eğitimi gir.
    İnput: test
Beklenen Sonuç :  Filtrelenen eğitim takvim üzerinde görüntülenmelidir.

![alt text](image-2.png)

# Case 4: Eğitmen arama filtresinin kontrolü
	Adım1: Tobeto anasayfaya gir.
    İnput: https://tobeto.com/giris
    Adım2: Sol alt kısmındaki takvim simgesine tıkla.
    Adım3: Açılan pop–up da eğitim durumu  check box larının hepsini işaretle.
    Adım4:Eğitmen arama inputu içerisine bulmak istediğin eğitmeni gir.
    İnput: Engin Demiroğ
Beklenen Sonuç :  Filtrelenen eğitmen takvim üzerinde görüntülenmelidir.

![alt text](image-3.png)


# Case 5: Eğitmen ve eğitim arama filtrelerinin birlikte kontrolü
	Adım1: Tobeto anasayfaya gir.
    İnput: https://tobeto.com/giris
    Adım2: Sol alt kısmındaki takvim simgesine tıkla.
    Adım3: Açılan pop–up da eğitim durumu  check box larının hepsini işaretle.
    Adım4:Eğitmen arama inputu içerisine bulmak istediğin eğitmeni gir.
    İnput: Engin Demiroğ
    Adım5:Eğitim arama inputu içerisine bulmak istediğin eğitimi gir.
    İnput: analist
Beklenen Sonuç :  İşaretlenen ve yazılan filtrelere göre eğitimler takvim üzerinde görüntülenebilmelidir.

![alt text](image-4.png)

# Case 6: Tarih yönlendirme butonlarının kontrolü
	Adım1: Tobeto anasayfaya gir.
    İnput: https://tobeto.com/giris
    Adım2: Sol alt kısmındaki takvim simgesine tıkla.
    Adım3: Bugün butonuna tıkla.  
Beklenen Sonuç :  Güncel tarihin olduğu ay takvim üzerinde görüntülenebilmeli ve bu aya  ait eğitimler takvimde  görüntülenebilmelidir.

    Adım4:Bugün butonu yanın da olan sağ ya da sol butonuna tıkla. 
Beklenen Sonuç :  Sağ butona tıklandıysa bir sonraki ay, sol butona tıklandıysa bir önceki aya  ait eğitimler görüntülenebilmelidir.
         
    Adım5: Takvimin sağ üst köşesinde bulunan ay butonuna tıkla.      
Beklenen Sonuç :  O aya ait tüm eğitimler takvimde görüntülenebilmelidir.

![alt text](image-5.png)


# Case 7: Takvim pop-up ‘nın kapatılmasının kontrolü
	Adım1: Tobeto anasayfaya gir.
    İnput: https://tobeto.com/giri
    Adım2: Sol alt kısmındaki takvim simgesine tıkla.
    Adım3: Sağ üst köşede bulunan kapatma simgesine tıkla.
Beklenen Sonuç :  Takvim kapanarak simge haline gelmelidir.
