# remote-control

Hedef bilgisayar üzerinde arduino ve bluetooth modülü ile istediğiniz sitem komutunu ve python kodunu çalıştırmanızı sağlayan bir kod.

## Kurulum
Bu kodu bir şekilde hedef bilgisayar her açıldığında çalıştıracak hale getirmeniz yeterlidir.

## Kullanım
Hedef bilgisayara kurulumu yapın ve HC-05 yada HC-06 gibi bluetooth modülleri ile oluşturacağınız devreyi çalıştırın. Devreyi sizin için tespit edecek ve eğer açıksa bağlanacak. Bağlanıp bağlanmadığını bluetooth modülü üzerindeki led ışık ile anlayabilirsiniz. Sonrasından devrenin bluetooth bağlantısı üzerinden gönderdiği komutları kod çalıştıracaktır.

### Python kodu çalıştırmak

Eğer pthon kodu çalıştırmak istiyorsanız direkt kod satırını seri bluetooth bağlantısı üzerinden göndermeniz yeterlidir.

### Sistem komutları çalıştırmak

Komutun başına `$` karakteri koyup seri bluetooth bağlantısı üzerinden göndermeniz yeterlidir.

## Uyarı

Sorumluluğu üzerime almam bu kodu kullanarak sorumluluğun sizin üzerinizde olduğunu kabul etmiş olursunuz. Bu kod eğlence amaçlı yazılmıştır. Hedef bilgisayarın sahibinin rızası olmadan kullanmanızı tavsiye etmem.