weight = float(input('Ваш вес '))
height = float(input('Ваш рост '))

imt = weight / (height * height)
if imt < 18.5:
    print('Недостаточная масса')
elif imt > 25:
    print('Избыточная масса')
else:
    print('Оптимальная масса')
print('конец')













