import cv2


def find_difference(baseline: str, current: str) -> bool:
    different_images = False

    image1 = cv2.imread(baseline)
    image2 = cv2.imread(current)
    assert image1 is not None, 'BaseLine não encontrado'
    assert image2 is not None, 'Nova Imagem não encontrada'

    difference = cv2.subtract(image1, image2)

    Conv_hsv_Gray = cv2.cvtColor(difference, cv2.COLOR_BGR2GRAY)

    Conv_hsv_Gray[Conv_hsv_Gray != 0] = 255

    ret, mask = cv2.threshold(Conv_hsv_Gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)

    if cv2.countNonZero(Conv_hsv_Gray):
        image_2 = current.split('/')
        print(f'Imagem {image_2[-1]} está diferente do modelo atual')
        different_images = True
        image2[mask != 255] = [128, 114, 225]
        cv2.imwrite(f'../ScreenShot/Divergence/Diferenca_{image_2[-1]}', image2)
    else:
        print('Imagens Ok!')
    return different_images


find_difference('../ScreenShot/imagem1.png', '../ScreenShot/imagem2.png')