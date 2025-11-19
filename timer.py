import time
from tkinter import *
from tkinter import ttk

next_day = 24 * 3600
now_tim = 100


def timer():
    global next_day, now_tim
    if now_tim > 0:
        gady_hours = now_tim // 3600
        gady_minutes = (now_tim - gady_hours * 3600) // 60
        gady_seconds = now_tim % 60
        timer_gady_label.config(text=f"{gady_hours:02d}:{gady_minutes:02d}:{gady_seconds:02d}")
        now_tim -= 1
        root.after(1000, timer)

def set_timer():
    global next_day, now_tim

    now_tim = int(time.time() + next_day) - int(time.time())
    print(f'{next_day=}')
    print(f'{now_tim=}')
    # timer()

root = Tk()
root.geometry('500x100+1000+50')

timer_gady_label = ttk.Label()
timer_gady_label.config(text="00:00:00", font=("Helvetica", 23))  # , font=("Helvetica", 12)
timer_gady_label.place(x=0, y=5)

ttk.Button(text='Start', command=set_timer).place(x=10, y=60)

timer()

root.mainloop()



# def start_timer():
#
#     b_d.time_flag = True
#     hours = 0
#     minutes = 0
#     seconds = 0
#     b_d.remaining_time = hours * 3600 + minutes * 60 + seconds
#     update_timer()
#
#
# # Function to update the timer
# def update_timer():
#     if b_d.time_flag:
#         hours = b_d.remaining_time // 3600
#         minutes = (b_d.remaining_time - hours * 3600) // 60
#         seconds = b_d.remaining_time % 60
#
#         timer_gady_label.config(text=f"{hours:02d}:{minutes:02d}:{seconds:02d}")
#         b_d.remaining_time += 1
#         root.after(1000, update_timer)  # Update every 1000 milliseconds (1 second)
#
#
# def stop_timer():
#     b_d.time_flag = False
#     print(f'{b_d.remaining_time=}')
#
#
# # Function to stop the timer
# def clear_timer():
#     b_d.remaining_time = 0
#     b_d.time_flag = True