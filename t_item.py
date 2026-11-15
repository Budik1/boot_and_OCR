import find_img
import tools

close = find_img.find_close()
tools.Mouse.move_to_click(pos_click=close, z_p_k=0.5, message='нажал закрыть')
x_close, y_close = close
x_meat = x_close - 100
y_meat = y_close + 100
tools.Mouse.move(pos=(x_meat, y_meat))