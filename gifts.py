from time import sleep
import fun


def open_loc_daily_gifts():
    link_gifts = fun.locCenterImg('img/b_gifts.png', confidence=0.9)
    if not link_gifts:
        fun.exit_to_zero_screen()
        link_gifts = fun.locCenterImg('img/b_gifts.png', confidence=0.9)
        fun.mouse_move_to_click(link_gifts, 0.1)
        fun.mouse_move_to_click(link_gifts, 0.1)

def open_daily_gift():
    b_gift_open = fun.locCenterImg('img/b_gift_open.png', confidence=0.9)
    while b_gift_open:
        fun.mouse_move_to_click(b_gift_open, 0.2)
        b_thanks = fun.locCenterImg('img/b_thanks.png', confidence=0.9)
        while not b_thanks:
            sleep(0.2)
            b_thanks = fun.locCenterImg('img/b_thanks.png', confidence=0.9)
        fun.mouse_move_to_click(b_thanks, 0.2)
        b_give = fun.locCenterImg('img/b_give.png', confidence=0.9)
        while not b_give:
            sleep(0.2)
            b_give = fun.locCenterImg('img/b_give.png', confidence=0.9)
        fun.mouse_move_to_click(b_give, 0.2)
        b_gift_open = fun.locCenterImg('img/b_gift_open.png', confidence=0.9)


# open_loc_daily_gifts()
# open_daily_gift()