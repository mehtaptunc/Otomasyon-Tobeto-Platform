# Test Senaryosu 

Adı :Takvim işlevselliğinin  kontrolü

Açıklama : Takvimde haftalık olarak dersleri görüntüleyebilmeli , hangi gün ve hangi saatte eğitim olduğunu , eğitim içeriği ve eğitmen bilgisi hakkında bilgileri takvimdeki günler tablosunda görüntüleyebilmelidir.

Ön Koşul : Test ortamı çalışır ve hazır durumda olmalıdır.  Tobeto anasayfasına sayfasına girilmiş olmalıdır, sol alt kısmındaki takvim simgesine tıklayarak "Eğitim ve Etkinlik Takvimi" sayfasına erişebilmelidir.

# Case 1: Filtresiz tüm eğitimlerin takvim üzerinde gösterilmesi
              Adım1: Tobeto anasayfaya gir.
              İnput: https://tobeto.com/giris
              Adım2: Sol alt kısmındaki takvim simgesine tıkla.
              Adım3: Açılan pop–up da eğitim durumu  check box larının hepsini işaretle.

Beklenen Sonuç :  Takvim üzerinde eğitimler, eğitim saat , tarihleri ve eğitmenler  görüntülenebilmelidir.

![image](https://github.com/mehtaptunc/Otomasyon-Tobeto-Platform/assets/134071818/d2b3dc2a-e72d-4aa0-a5ea-3a7920afe6f7)

# Case 2: Eğitim arama filtresinin kontrolü
	           Adım1: Tobeto anasayfaya gir.
             İnput: https://tobeto.com/giris
             Adım2: Sol alt kısmındaki takvim simgesine tıkla.
             Adım3: Açılan pop–up da eğitim durumu  check box larının hepsini işaretle.
             Adım4:Eğitim arama inputu içerisine bulmak istediğin eğitimi gir.
             İnput: test,.net,mobil
Beklenen Sonuç :  Filtrelenen eğitim takvim üzerinde görüntülenmelidir.

![image](https://github.com/mehtaptunc/Otomasyon-Tobeto-Platform/assets/134071818/6cdf8849-4629-4994-bb06-9691b76a0415)

# Case 3: Eğitmen arama filtresinin kontrolü
	           Adım1: Tobeto anasayfaya gir.
             İnput: https://tobeto.com/giris
             Adım2: Sol alt kısmındaki takvim simgesine tıkla.
             Adım3: Açılan pop–up da eğitim durumu  check box larının hepsini işaretle.
             Adım4:Eğitmen arama inputu içerisine bulmak istediğin eğitmeni gir.
             İnput: Engin Demiroğ,Ahmet Çetinkaya,Gürkan İlişen
Beklenen Sonuç :  Filtrelenen eğitmen takvim üzerinde görüntülenmelidir.

![image](https://github.com/mehtaptunc/Otomasyon-Tobeto-Platform/assets/134071818/498ff67e-ab86-44fe-88a5-71f5dd8c4ef2)

# Case 4: Eğitmen ve eğitim arama filtrelerinin birlikte kontrolü
       	     Adım1: Tobeto anasayfaya gir.
             İnput: https://tobeto.com/giris
             Adım2: Sol alt kısmındaki takvim simgesine tıkla.
             Adım3: Açılan pop–up da eğitim durumu  check box larının hepsini işaretle.
             Adım4:Eğitmen arama inputu içerisine bulmak istediğin eğitmeni gir.
             İnput: Engin Demiroğ
             Adım5:Eğitim arama inputu içerisine bulmak istediğin eğitimi gir.
             İnput: analist
Beklenen Sonuç :  İşaretlenen ve yazılan filtrelere göre eğitimler takvim üzerinde görüntülenebilmelidir.

![image](https://github.com/mehtaptunc/Otomasyon-Tobeto-Platform/assets/134071818/234241d0-39ef-41e2-9485-4bbb9c3502aa)

# Case 5: Tarih yönlendirme butonlarının kontrolü
	            Adım1: Tobeto anasayfaya gir.
              İnput: https://tobeto.com/giris
              Adım2: Sol alt kısmındaki takvim simgesine tıkla.
              Adım3: Bugün butonuna tıkla.
             
Beklenen Sonuç :  Güncel tarihin olduğu ay takvim üzerinde görüntülenebilmeli ve bu aya  ait eğitimler takvimde  görüntülenebilmelidir.

 # Case 6: Ay  seçiminde takvimin değişmesinin kontrolü
              Adım1: Tobeto anasayfaya gir.
              İnput: https://tobeto.com/giris
              Adım2: Sol alt kısmındaki takvim simgesine tıkla.
              Adım3: Takvimin sağ üst köşesinde bulunan ay butonuna tıkla.
              
Beklenen Sonuç :  O aya ait tüm eğitimler takvimde görüntülenebilmelidir.

# Case 7: Takvim pop-up ‘nın kapatılmasının kontrolü
	             Adım1: Tobeto anasayfaya gir.
               İnput: https://tobeto.com/giri
              Adım2: Sol alt kısmındaki takvim simgesine tıkla.
              Adım3: Sağ üst köşede bulunan kapatma simgesine tıkla.

Beklenen Sonuç :  Takvim kapanarak simge haline gelmelidir









