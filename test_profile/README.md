# PROFİLİNİ OLUŞTUR
# Test Senaryosu 
Adı : Kullanıcı Profili Oluşturma

Açıklama : Kullanıcıların :“Kişisel Bilgilerim”, “Deneyimlerim”, “Eğitim Hayatım”, “Yetkinliklerim”, “Sertifikalarım”, “Medya Hesaplarım”, “Yabancı Dillerim” ve “Ayarlar” başlıklarına erişebilmelerinin testi yapılacaktır.

Ön Koşul : Test ortamı çalışır ve hazır durumda olmalıdır. Kullanıcının kayıtlı ve geçerli  hesabı bulunmalıdır. Tobeto web sayfasına gidilmelidir.
https://tobeto.com/profilim/profilimi-duzenle/kisisel-bilgilerim

# Case 1 :  Profil başlıklarının  kontrolü 
       Adım 1: Call Test(Test Senaryosu 1-Case1 :Başarılı Giriş Kontrolü)
       Adım 2: ‘Profilimi Oluştur’ modülünde ‘Başla’ butonuna tıkla.
  Beklenen Sonuç: ‘Kişisel Bilgilerim’ başlığının olduğu alanının açılması.

  ![image](https://github.com/mehtaptunc/Otomasyon-Tobeto-Platform/assets/134071818/b0807f2a-e01a-4b2c-90a6-eaf1330d0945)

      Adım 3:” Deneyimlerim” başlığına tıkla.

Beklenen Sonuç: ‘Deneyimlerim’ başlığının olduğu alanının açılması.

![image](https://github.com/mehtaptunc/Otomasyon-Tobeto-Platform/assets/134071818/4dca99bc-e2d8-4c98-bc48-23f0f5202d1f)

    Adım 4:” Yetkinliklerim” başlığına tıkla.
Beklenen Sonuç: ‘Yetkinliklerim’ başlığının olduğu alanının açılması.

![image](https://github.com/mehtaptunc/Otomasyon-Tobeto-Platform/assets/134071818/ea1ad0e2-8328-43ea-94b7-eec046ea58b5)

# Case 12:  Kişisel Bilgilerin Başarılı Güncellenmesi
    Adım 1: Call Test(Test Senaryosu 1-Case1 :Başarılı Giriş Kontrolü)
    Adım 2: ‘Profilimi Oluştur’ modülünde ‘Başla’ butonuna tıkla.
    Adım 3: “Adınız” alanına adını gir.
    input: Demet
    Adım 4: “Soyadınız” alanına soyadını gir.
    input: Koç
    Adım5: Telefon numarası kısmından ülke kodu alanından inputu seç.
    input: Türkiye
    Adım6: “Telefon Numaranız” alanına numara gir.
    input: +90 555 665 26 55
    Adım7: “Doğum Tarihiniz” alanına inputu gir ya da takvim işaretine tıkla takvimden seç.       
    input: 12.12.1990
    Adım8: “T.C. Kimlik No” yanlış gir 
    input1: 44444444444
    Adım9:  ‘Ülke’ alanını gir.
    input2:Türkiye
    Adım10: “İl” alanına tıkla ve listeden ili seç.
    input: İstanbul
    Adım11: “İlçe” alanına tıkla ve listeden ilçeyi seç.
    input: Ümraniye
    Adım12: “Mahalle / Sokak” alanına bilgileri gir.
    input: Murat Mah. Sancar Sok.
    Adım 13: “Hakkımda” alanına bilgileri gir.
    input: Yazılım Test mühendisliği alanında Tobetoda eğitim alıyorum.
    Adım 14: Kaydet butonuna tıklayın.
  Beklenen Sonuç : "• Kimlik bilgilerinizi hatalı girdiniz." şeklinde bir bildirim ekranda  görülmelidir.

  # Case 3:  Profil resmi ekle kontrolü
    Adım 1: Call Test(Test Senaryosu 1-Case1 :Başarılı Giriş Kontrolü)
    Adım 2: ‘Profilimi Oluştur’ modülünde ‘Başla’ butonuna tıkla.
    Adım 3: Görsel yükleme butonuna tıkla.
Beklenen Sonuç: Ekranda sırasıyla ‘Sürükleyerek bırak’, ‘yapıştır’ ve ‘gözat’ seçeneklerinin sunulduğu pencerenin açılması.

![image](https://github.com/mehtaptunc/Otomasyon-Tobeto-Platform/assets/134071818/1dfd814b-778e-4fa8-9f87-a29ec674311b)




  
    







