img1='img/default/station_master/tasks_gady/t1.png'

img1_alt_split = img1.split('.')
img1_alt_split[0] += 'event'
img1_alt ='.'.join(img1_alt_split)
print(img1_alt)
# img1_alt.join(img1_name_mod, img1_alt_split[1])
# print(img1_alt)