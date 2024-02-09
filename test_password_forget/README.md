# Test Senaryosu 

Adı : Şifremi unuttum paneli kontrolü.

Açıklama : Şifresini unutan kullanıcı bu sayfayı kullanarak şifresini yenileyebilmelidir.

Ön Koşul : Test ortamı çalışır ve hazır durumda olmalıdır. Tobeto sifremi-unuttum sayfasına girilmiş olmalıdır.
Input: https://tobeto.com/sifremi-unuttum

# Case 1: Şifre sıfırlama e-postası gönderme.
       Adım1: Tobeto şifremi unuttum sayfasına gir.
	   Adım2: E-posta kısmına geçerli bir e-posta adresi gir.
	   İnput: aaa@gmail.com
	   Adım3: Gönder butonuna tıkla.
Beklenen Sonuç : Kullanıcı gönder tuşuna bastığında girilen e-posta adresi sistemde bulunursa pop up şeklinde ekteki mesajla karşılaşmalıdır. Giriş sayfasına yönlendirilmelidir.

![image](https://github.com/mehtaptunc/Otomasyon-Tobeto-Platform/assets/134071818/3f62e3a9-3bbb-4bee-a17f-be0bb83237b3)

# Case 2: Şifre sıfırlama durumunda hatalı e-posta girilmesi.
	   Adım1: Tobeto şifremi unuttum sayfasına gir.
	   Adım2: E-posta kısmına geçersiz bir e-posta adresi gir.
	   İnput: geçersiz@gmail.com
	   Adım3: Gönder butonuna tıkla.
Beklenen Sonuç : Kullanıcı gönder tuşuna bastığında girilen e-posta adresi geçersiz bir e-posta adresi ise pop up şeklinde ekteki mesajla karşılaşmalıdır.

![image](https://github.com/mehtaptunc/Otomasyon-Tobeto-Platform/assets/134071818/504f6264-ab50-4547-b537-8d1d50cc0e48)

# Pytest Kontrolü

![image](https://github.com/mehtaptunc/Otomasyon-Tobeto-Platform/assets/134071818/51492458-7f81-4c35-89df-39d4aabc5817)




