##Test Senaryosu 1
Adı : Giriş Paneli Kontrolü
Açıklama : Kullanıcılar e-posta ve şifrelerini girerek sisteme giriş yapabilmelidir.
Ön Koşul : Test ortamı çalışır ve hazır durumda olmalıdır. Tobeto giriş sayfasına girilmiş olmalıdır.
Input: https://tobeto.com/giris


##Case 1 : Başarılı Giriş Kontrolü
Adım 1: Sitenin giriş sayfasına gir.
https://tobeto.com/giris
Adım 2: E-posta bölümüne doğru bir mail adresi gir.
Input: kojacer986@vasteron.com
Adım 3: Şifre bölümüne doğru bir şifre gir.
Input: deneme123
Adım 4: Giriş yap butonuna tıkla.
Beklenen Sonuç : Kullanıcı başarılı bir şekilde “• Giriş başarılı.”ne pop-up ı açılmalı.



##Case 2 : E-posta ve Şifre Girilmediğinde
Adım 1: E-posta veya şifre bölümünü boş bırak.
Input:  e-posta: boş bırak şifre:test123
e-posta: kojacer986@vasteron.com  şifre: boş bırak 
e-posta: boş bırak şifre: boş bırak
Adım 2: Giriş yap butonuna tıkla.
Beklenen Sonuç : Boş bırakılıp giriş yap butonuna tıklandığı durumda kırmızı renkte "Doldurulması zorunlu alan" uyarısı vermelidir.


##Case 3 :  E-posta veya Şifre Hatalı Girildiğinde
Adım 1: E-posta veya şifre bölümündeki bilgileri hatalı gir.
Input:  e-posta: fffffg@.com  (geçersiz)  şifre: 475133
e-posta: kojacer986@.com  şifre: 1237(geçersiz)
e-posta: 45512@gmail.com  (geçersiz) şifre: test123 (geçersiz)
Adım 2: Giriş yap butonuna tıkla.
Beklenen Sonuç: Kullanıcı bilgilerini hatalı girdiyse bir sonraki sayfaya geçiş sağlanmamalıdır. Pop-up şeklinde "Geçersiz e-posta veya şifre" uyarısı verilmelidir. 
