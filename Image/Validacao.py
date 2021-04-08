import random

import cv2


class CompareImage(object):

    def __init__(self, image_1_path, image_2_path):
        self.minimum_commutative_image_diff = 1
        self.image_1_path = image_1_path
        self.image_2_path = image_2_path

    def compare_image(self):
        image_1 = cv2.imread(self.image_1_path, 0)
        image_2 = cv2.imread(self.image_2_path, 0)
        commutative_image_diff = self.get_image_difference(image_1, image_2)

        if commutative_image_diff < self.minimum_commutative_image_diff:
            print("Matched")
            return round(commutative_image_diff, 3) * 100
            # return commutative_image_diff
        return 10000 #//random.random()

    @staticmethod
    def get_image_difference(image_1, image_2):
        first_image_hist = cv2.calcHist([image_1], [0], None, [256], [0, 256])
        second_image_hist = cv2.calcHist([image_2], [0], None, [256], [0, 256])

        img_hist_diff = cv2.compareHist(first_image_hist, second_image_hist, cv2.HISTCMP_BHATTACHARYYA)
        img_template_probability_match = cv2.matchTemplate(first_image_hist, second_image_hist, cv2.TM_CCOEFF_NORMED)[0][0]
        img_template_diff = 1 - img_template_probability_match

        # taking only 10% of histogram diff, since it's less accurate than template method
        commutative_image_diff = (img_hist_diff / 10) + img_template_diff
        return commutative_image_diff

    @staticmethod
    def find_difference(current: str, baseline: str) -> bool:
        different_images = False

        image2 = cv2.imread(baseline)
        image1 = cv2.imread(current)
        assert image1 is not None, 'Nova Imagem não encontrada'
        assert image2 is not None, 'BaseLine não encontrado'

        difference = cv2.subtract(image1, image2)

        Conv_hsv_Gray = cv2.cvtColor(difference, cv2.COLOR_BGR2GRAY)

        Conv_hsv_Gray[Conv_hsv_Gray != 0] = 255

        ret, mask = cv2.threshold(Conv_hsv_Gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)

        if cv2.countNonZero(Conv_hsv_Gray):
            image_2 = current.split('/')
            print(f'Imagem {image_2[-1]} está diferente do modelo atual')
            different_images = True
            image2[mask != 255] = [128, 114, 225]
            cv2.imwrite(f'./ScreenShot/Divergence/{image_2[-1]}', image2)
        else:
            print('Imagens Ok!')
        return different_images


# if __name__ == '__main__':
#     compare_image = CompareImage('../ScreenShot/Login/PlantList.png', 'Login/Home.png')
#     image_difference = compare_image.compare_image()
#     print(image_difference)