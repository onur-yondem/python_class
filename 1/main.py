class Error(Exception):
    pass

class QuestionCountError(Error):
    pass


class Ogrenci:

    def __init__(self, ogrenci_adi, ogrenci_soyadi, ogrenci_sinifi):
        self.ogrenciAdi = ogrenci_adi
        self.ogrenciSoyadi = ogrenci_soyadi
        self.ogrenciSinif = ogrenci_sinifi

    def print_student_score(self):
        print(f"Öğrenci Adı: {self.ogrenciAdi} \n Öğrenci Soyadı: {self.ogrenciSoyadi} \n Öğrenci Sınıfı: {self.ogrenciSinif}")

class Soru:

    def net_sayisi(correct_answer, wrong_answer):
        try:
            if isinstance(correct_answer, int) and isinstance(wrong_answer, int):
                if correct_answer + wrong_answer == 50:
                    total_correct_answer = correct_answer - int(wrong_answer / 4)

                    return total_correct_answer

                else:
                    raise QuestionCountError

            else:
                raise TypeError

        except(QuestionCountError):
            print("Toplam soru sayısı 50 olmalıdır")

        except(TypeError):
            print("Girilen değerler integer olmalıdır")

    def Hesapla(net_sayisi):
        try:
            score = net_sayisi * 2
            print("Puan: " + str(score))

        except TypeError:
            print("Girilen değerler integer olmalıdır")


ogrenci1 = Ogrenci("Onur","Yöndem","5")
ogrenci1.print_student_score()
Soru.Hesapla(Soru.net_sayisi(30,20))





