class Insan:
    def __init__(self):
        self.ad = "Onur"
        self.soyad = "Yöndem"
        self.yas = "26"
        self.ulke = "Türkiye"
        self.sehir = "Edirne"
        self.yetenekler = []

    def kisi_bilgileri(self):
        kisi_bilgileri = f"Ad: {self.ad} \n " \
                         f"Soyad: {self.soyad} \n " \
                         f"Yaş: {self.yas} \n " \
                         f"Ülke: {self.ulke} \n " \
                         f"Şehir: {self.sehir} \n " \
                         f"Yetenekler: {self.yetenekler}"
        print(kisi_bilgileri)
        return kisi_bilgileri

    def yetenek_ekle(self,*abilities):
        for ability in abilities:
            self.yetenekler.append(ability)

        print(self.yetenekler)
        return self.yetenekler

onur = Insan()
onur.yetenek_ekle("python","bisiklet",21321,"sadada","")
onur.kisi_bilgileri()