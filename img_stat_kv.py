import pyautogui as pg
import fun

kv_reload = fun.locCenterImg('img/kv/kv_reload.png', confidence=0.9)
print("kv_reload = ", kv_reload)
if kv_reload:
    x, y = kv_reload
    pg.moveTo(x, y, duration=1)
    x -= 225
    y -= 25
    pg.moveTo(x, y, duration=1)
    x_sh, y_sh = x, y
    x_sh += 225
    y_sh += 270
    pg.moveTo(x_sh, y_sh, duration=1)
    fun.foto('img/kv/tests/kv_.png', _region=(x, y, 225, 270))
