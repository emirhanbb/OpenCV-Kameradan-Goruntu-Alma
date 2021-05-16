# Python OpenCV İle Kameradan Görüntü Alma

Herkese merhaba. Kısa bir süre önce geliştirmem gereken bir proje için python ile görüntü işlemeye başladım. Bu yüzden opencv kütüphanesi ile ilerlemeye karar verdim. Bu yazıda kameradan anlık olarak görüntü almayı sizlere anlatacağım.

Aşağıdaki kod ile kameradan anlık olarak görüntü alabilirsiniz. Şimdi kodu anlatayım.

**cv2.VideoCapture(0):** Bu kısımda 0 değeri girmemizin sebebi bilgisayarımıza dahili olan kamerayı kullanmak istediğimiz için. 1 Yaparsak USB, 2 yaparsak mevcut bir video üzerinden işlem yapılmaktadır.

Sonsuz döngü oluşturma sebebimiz kameradan sürekli anlık olarak fotoğraf alacağız, eğer bunu sürekli hale getirirsek video gibi görünecektir.

if bloğu kısmında **cv2.waitKey(50)** yaparak while göngüsünün 50milisaniyede bir dönmesini sağlamış olduk. ord(‘q’) ise klavyeden q tuşuna basılınca kamera penceresinin kapanması için yapıldı.

**kamera.release():** kameramızı kapatmak için.

**cv2.destroyAllWindows():** bütüm opencv pencerelerini kapatmak için.

## Kurulum

OpenCV'yi projenize dahil etmeniz gerekiyor.

```sh
pip install opencv-python
```

