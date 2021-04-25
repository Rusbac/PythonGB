duration = int(input('Введите время в секундах: '))
if duration <= 60:
    print (duration, 'сек' )
elif 3600 > duration > 60:
    res_m = duration / 60
    print (res_m, 'мин')
elif duration > 3600:
    res_h = duration / 3600
    print (res_h, 'час')
elif duration > (60 * 60 * 24):
    res_d = duration / (60 * 60 * 24)
    print (res_d, 'дн')