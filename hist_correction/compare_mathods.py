import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np

def linear_correction(image):
    img = check_Grayscale(image)
    H, W = img.shape[:2]
    min_val = np.min(img)
    max_val = np.max(img)

    for i in range(H):
        for j in range(W):
            img[i, j] = ((img[i, j] - min_val) / (max_val - min_val)) * 255

    return img

def equalize_Hist_cv(img):
    GrayImage = check_Grayscale(img)
    return(cv.equalizeHist(GrayImage))

def histogram_equalization(img):
    image = check_Grayscale(img)
    # Розрахунок гістограми
    hist, _ = np.histogram(image.flatten(), 256, [0, 256])
    cdf = hist.cumsum()  # розрахунок кумулятивної суми гістограми
    cdf = (cdf - cdf.min())*255/(cdf.max()-cdf.min())  # нормалізація CDF
    cdf = cdf.astype('uint8')  # перетворення типу на 'uint8'

    # Застосування CDF для виконання еквалізації гістограми
    img_equalized = cv.LUT(image, cdf)

    return img_equalized

def adaptive_histogram_equalization_cv(img):
    image = check_Grayscale(img)
    clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))

    # Застосування адаптивного вирівнювання гістограми
    clahe_image = clahe.apply(image)
    return clahe_image

def adaptive_histogram_equalization(image, grid_size=(8, 8)):
    image = check_Grayscale(image)
    h, w = image.shape
    # Крок 1: Розбиття зображення на блоки
    block_h = h // grid_size[0]
    block_w = w // grid_size[1]

    # Створюємо порожню матрицю для нового зображення
    equalized_image = np.zeros_like(image)

    def manual_histogram_equalization(block):
        # Аналог глобального вирівнювання гістограми для кожного блоку
        hist = np.zeros(256)
        for pixel in block.flatten():
                hist[pixel] += 1

        cdf = hist.cumsum()
        cdf_normalized = (cdf - cdf.min()) * 255 / (cdf.max() - cdf.min())

        equalized_block = np.interp(block.flatten(), range(0, 256), cdf_normalized).reshape(block.shape).astype(np.uint8)
        
        return equalized_block

    # Проходимо по кожному блоку і застосовуємо вирівнювання гістограми
    for i in range(0, h, block_h):
        for j in range(0, w, block_w):
            # Виділяємо блок зображення
            block = image[i:i+block_h, j:j+block_w]

            # Викликаємо функцію для вирівнювання гістограми для блоку
            block_equalized = manual_histogram_equalization(block)

            # Записуємо оброблений блок назад у результуюче зображення
            equalized_image[i:i+block_h, j:j+block_w] = block_equalized

    return equalized_image

def check_Grayscale(img):
    if len(img.shape) == 2:
        out = np.copy(img)
    else:
        out = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    return out

def histogram(img):
    return cv.calcHist([img], [0], None, [256], [0, 256])



def compareMathods(image):
    rows = 2
    columns = 4

    fig = plt.figure(figsize=(10, 7))

    # ----------Input------------

    b, g, r = cv.split(image)
    rgb_img = cv.merge([r, g, b])
    plt.gray()
    fig.add_subplot(rows, columns, 1)
    plt.imshow(rgb_img)
    plt.axis('off')
    plt.title("Input")

    fig.add_subplot(rows, columns, 5)
    plt.hist(image.ravel(), 256, [0, 256])


    # ----------Result Linear Correction------------
    result = linear_correction(image)
    fig.add_subplot(rows, columns, 2)
    plt.imshow(result, cmap='gray')
    plt.axis('off')
    plt.title("Linear Correction")

    fig.add_subplot(rows, columns, 6)
    plt.hist(result.ravel(), 256, [0, 256])

    # ----------Result Histogram Equalization------------
    result = histogram_equalization(image)
    fig.add_subplot(rows, columns, 3)
    plt.imshow(result, cmap='gray')
    plt.axis('off')
    plt.title("Histogram Equalization")

    fig.add_subplot(rows, columns, 7)
    plt.hist(result.ravel(), 256, [0, 256])


    # ----------Result Adaptive Histogram Equalization------------
    # result = adaptive_histogram_equalization(image)
    result = adaptive_histogram_equalization_cv(image)
    fig.add_subplot(rows, columns, 4)
    plt.imshow(result, cmap='gray')
    plt.axis('off')
    plt.title("Adaptive Histogram Equalization")

    fig.add_subplot(rows, columns, 8)
    plt.hist(result.ravel(), 256, [0, 256])


    fig.tight_layout()
    plt.show()
