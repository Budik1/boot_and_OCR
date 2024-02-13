import easyocr
# ru, en, ro, it, ch_tra, ch_sim, az, vi
def text_recognition(file_path):
    reader = easyocr.Reader(["en"])
    result = reader.readtext(file_path, detail=0, allowlist='0123456789') #

    return result

def recognized(file_path):
    # file_path = 'img/test/2_big.png'
    texst = (text_recognition(file_path=file_path))

    return texst

# txt = main()
# print(txt)
# str_xp68 = (txt[1])
# print(str_xp68)
# if str_xp68 == 'G8':
#     xp68 = 68
# print(xp68)
# txt_str = txt[0]
# print(int(txt_str) + 1)