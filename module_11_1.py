from PIL import Image, ImageFilter
import numpy


def picture():
    img_1 = Image.open("img_1.png")
    img_2 = Image.open("img_2.png")

    img_2_2 = img_2.filter(ImageFilter.EDGE_ENHANCE)
    img_2_2.show()

    img_3 = Image.blend(img_1, img_2, 0.4)
    img_3.show()

    img_4 = img_2.filter(ImageFilter.EMBOSS)
    img_4.show()

    img_5 = img_2.crop((200, 200, 1000, 1000))
    img_5 = img_2.resize((200, 200))
    img_5.show()


class Numpy:

    def __init__(self, ranget=0, lists=[]):
        self.chislo = ranget
        self.result = 0
        if ranget != 0:
            self.num = numpy.arange(self.chislo)
        if len(lists) > 0:
            self.num = numpy.array(lists)
        print(f"Входные данные:{self.num}")  # Мне нужна была только одна переменная self.num

    def slojenie(self, a):
        self.result = self.num + a
        print(f"Выходные данные со сложением на {a}, {self.result}")
        print("-------------------------------------------------------------")

    def umnoj(self, n):
        self.result = self.num * n
        print(f"Выходные данные с умножением на {n}, {self.result}")
        print("-------------------------------------------------------------")


Numpy(lists=[5, 3, 2, 554, 32]).umnoj(6)  # Лучше указать ranget или  lists
Numpy(14).slojenie(4)