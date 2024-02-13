import easyocr


def text_recognition(file_path):
    reader = easyocr.Reader(["en"])
    result = reader.readtext(file_path, detail=0, allowlist='0123456789')

    return result


def recognized(file_path):
    # file_path = 'img/test/2_big.png'
    texst = (text_recognition(file_path=file_path))

    return texst
