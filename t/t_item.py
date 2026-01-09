import matplotlib.pyplot as plt
import cv2
import numpy as np
from PIL import Image

import a_test1


def ramki():
    # Загрузка изображения с помощью PIL
    image_pil = Image.open('C:/python/bot_ocr1/img/test/test_tasks/arial_task_1_line_xp.png')

    # Преобразование изображения в массив numpy
    image_np = cv2.cvtColor(np.array(image_pil), cv2.COLOR_RGB2BGR)

    # Преобразование изображения в оттенки серого
    gray = cv2.cvtColor(image_np, cv2.COLOR_BGR2GRAY)

    # Выполнение операции поиска краев
    edges = cv2.Canny(gray, 150, 200)

    # Создание холста для отображения итогового изображения и краев
    fig, axs = plt.subplots(1, 2, figsize=(10, 5))

    # Отображение исходного изображения на холсте
    axs[0].imshow(image_pil)
    axs[0].axis('off')

    # Отображение краев на холсте
    axs[1].imshow(edges, cmap='gray')
    axs[1].axis('off')

    # Сохранение результата в файл
    result_image = Image.fromarray(edges)
    result_image.save('C:/python/bot_ocr1/img/test/test_tasks/edges.png')

    # Отображение результата
    plt.show()
