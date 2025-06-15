import fun
import find_img as find

pos_slip= [0, 0]
pos_or1 = find.find_info()
pos_slip[0] = pos_or1[0] + 270 + 70
pos_slip[1] = pos_or1[1] + 180
#
fun.mouse_move(pos=pos_slip)