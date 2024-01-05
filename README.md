## Test Senaryosu 1
Adı : Giriş Paneli Kontrolü

Açıklama : Kullanıcılar e-posta ve şifrelerini girerek sisteme giriş yapabilmelidir.

Ön Koşul : Test ortamı çalışır ve hazır durumda olmalıdır. Tobeto giriş sayfasına girilmiş olmalıdır.

Input: https://tobeto.com/giris





## Case 1 : Başarılı Giriş Kontrolü

Adım 1: Sitenin giriş sayfasına gir.

https://tobeto.com/giris

Adım 2: E-posta bölümüne doğru bir mail adresi gir.

Input: kojacer986@vasteron.com

Adım 3: Şifre bölümüne doğru bir şifre gir.

Input: deneme123

Adım 4: Giriş yap butonuna tıkla.

Beklenen Sonuç : Kullanıcı başarılı bir şekilde “• Giriş başarılı.”ne pop-up ı açılmalı.

![image](https://github.com/mehtaptunc/Otomasyon-Tobeto-Platform/assets/134071818/f0642bf9-e05d-4b81-8b5c-ddf7d4156647)




## Başarılı  py test kontrolü 





![Ekran Alıntısı PNG 1](https://github.com/mehtaptunc/Otomasyon-Tobeto-Platform/assets/134071818/c1f41b0c-2f37-4d3f-8a13-b39e4fef42b2)




## Case 2 : E-posta ve Şifre Girilmediğinde

Adım 1: E-posta veya şifre bölümünü boş bırak.

Input:  e-posta: boş bırak şifre:test123

e-posta: kojacer986@vasteron.com  şifre: boş bırak 

e-posta: boş bırak şifre: boş bırak

Adım 2: Giriş yap butonuna tıkla.

Beklenen Sonuç : Boş bırakılıp giriş yap butonuna tıklandığı durumda kırmızı renkte "Doldurulması zorunlu alan" uyarısı vermelidir.


![image](https://github.com/mehtaptunc/Otomasyon-Tobeto-Platform/assets/134071818/b857c784-1a14-4fc4-babd-1654d4bf5556)




## Başarılı  py test kontrolü 






![Ekran Alıntısı PNG2](https://github.com/mehtaptunc/Otomasyon-Tobeto-Platform/assets/134071818/3476299d-6492-470e-8269-28e1721169a8)



## Case 3 :  E-posta veya Şifre Hatalı Girildiğinde

Adım 1: E-posta veya şifre bölümündeki bilgileri hatalı gir.

Input:  e-posta: fffffg@.com  (geçersiz)  şifre: 475133

e-posta: kojacer986@.com  şifre: 1237(geçersiz)

e-posta: 45512@gmail.com  (geçersiz) şifre: test123 (geçersiz)

Adım 2: Giriş yap butonuna tıkla.

Beklenen Sonuç: Kullanıcı bilgilerini hatalı girdiyse bir sonraki sayfaya geçiş sağlanmamalıdır. Pop-up şeklinde "Geçersiz e-posta veya şifre" uyarısı verilmelidir. 




![image](https://github.com/mehtaptunc/Otomasyon-Tobeto-Platform/assets/134071818/50308482-c103-496f-ad33-4d64f091aacf)





## Başarılı  py test kontrolü 






![Ekran Alıntısı PNG3](https://github.com/mehtaptunc/Otomasyon-Tobeto-Platform/assets/134071818/b71900e3-2d84-4482-b7ec-39c3a8e67d4d)



