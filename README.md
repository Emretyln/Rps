Sections related to a python project of Aygaz python bootcamp.
Project criterias are listed below.
Also we used pycharm IDE
tr-tr

Proje: Taş, Kağıt, Makas Oyunu
Genel Bakış:
Bu projenin amacı, taş, kağıt, makas oyunu tasarlamaktır. Bu proje sayesinde sadece Python diline değil, aynı zamanda kodlamanın temel kurallarına da
hakimiyetinizi geliştireceksiniz. Proje kodunuzu PEP-8 kurallarına göre yazmak ve proje icin yaratıcılığınızı ön plana çıkarmak önemlidir.
Projenin Amaçları:
• Döngüler, koşullu ifadeler ve kullanıcı girişi gibi temel Python kavramlarını uygulamak.
• Mantıksal düşünme yeteneğinizi geliştirerek esnekliğe uyum sağlamak.
Projenin Ana Hatları:
• Taş, kağıt, makas oyunu için bir fonksiyon oluşturacaksınız ve bu fonksiyonu tas_kagit_makas_ADINIZ_SOYADINIZ şeklinde
adlandıracaksınız.
• Fonksiyonunuz sorunsuz çalışmalı ve Python terminali üzerinden tas_kagit_makas_ADINIZ_SOYADINIZ() şeklinde çalıştırılabilir
olmalıdır.
• Oyun birden fazla turdan oluşacak ve ilk iki turu kazanan oyunun galibi olacaktır.
• Her oyundan sonra hem kullanıcıya hem de bilgisayara başka bir oyun oynamak isteyip istemediği sorulacak. Eğer iki taraf da oynamak
isterse oyun tekrarlanacaktır. (Bilgisayara nazik davranmayı unutmayın! ) 😊
• Unutmayın! Kodunuz çalışmazsa projeniz değerlendirmeye alınmayacaktır.
Projeyi Oluştururken İzlenmesi Gerekenler:
1. Oyun Tanıtımı:
• Oyunun kurallarını açıklayan bir karşılama mesajı oluşturun.
• Kullanıcıya oyunun nasıl oynanacağını veya oyundan nasıl çıkılacağını bildirin.
• Oyunun turları üç seçenekten oluşmalıdır: Oyuncu kazanabilir, bilgisayar kazanabilir veya beraberlik olabilir.
• İlk iki turu kazanan oyunu kazanır.
2. Oyun Kurulumu:
• Taş, kağıt ve makas seçeneklerinden oluşan bir liste tanımlayın. Daha fazlasi can yakmaz. Unutmayin, hayal gücünüz size öne
tasir.
• Oynanan oyun sayısı, oynanan tur sayısı, oyuncu galibiyetleri ve bilgisayar galibiyetleri için sayaçlar başlatın.
3. Oyunun Ana Döngüsü:
• Oyunu oynanabilir kılmak için bir while döngüsü kullanın.
• Bu döngü içinde, her yeni oyun için tur ve galibiyet sayaçlarını sıfırlayın.
4. Turların Döngüsü:
• Oyuncu veya bilgisayar iki tur kazanana kadar başka bir while döngüsü kullanın.
• Oyuncudan üç seçenekten birini yapmasını isteyin, geçersiz bir opsiyon seçerse, yeniden bir seçenek girmesini isteyin.
• Bilgisayarın seçimini rastgele oluşturun (ipucu: random modülünü kullanabilirsiniz).
• Seçimleri aldıktan sonra turun kazananını belirlemek için mantıksal operasyonlar veya temel if-else ifadelerini kullanın.
• İlk iki turu kazanan oyunu kazanacağından galibiyet sayaçlarını güncellemeyi unutmayın.
• Her turun sonucunu ekrana yazdırın (ipucu: print() fonksiyonu tam da bu iş için).
5. Oyun Galibini Belirleyin:
• Turların döngüsü bittikten sonra (bir oyuncu iki tur kazandığında), oyunun genel galibini belirleyin ve uygun mesajı gösterin.
6. Devam Etme İsteği:
• Kullanıcıya başka bir oyun oynamak isteyip istemediğini sorun.
• Bilgisayarın da oyuna devam etmek isteyip istemediğini sorun (rastgele bir cevap oluşturabilirsiniz).
• Her iki taraf da oyuna devam etmek istiyorsa oyun devam etsin; fakat iki taraftan biri devam etmek istemiyorsa oyun bitsin (ipucu:
bunun için break kullanabilirsiniz).
• Her durum için uygun bir mesaj gösterin
