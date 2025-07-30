import fun
import my_OCR
import baza_dannyx as b_d


def get_screenshot_energy():
    energy_task: str = 'img/test/test_tasks/energy_value/'

    line1 = fun.get_areas_energy_1()
    line2 = fun.get_areas_energy_2()
    line3 = fun.get_areas_energy_3()
    fun.foto(path_name=f'{b_d.energy_task_value}line1.png', region=line1)
    fun.foto(path_name=f'{b_d.energy_task_value}line2.png', region=line2)
    fun.foto(path_name=f'{b_d.energy_task_value}line3.png', region=line3)

def poz():
    path_energy_task = b_d.energy_task_value

    price_3 = my_OCR.recognized(f'{path_energy_task}line_3.png')
    print(f'{price_3=}')
poz()