#Задание 1
seconds = int(input('Введите количество секунд:'))
hours = seconds//3600
minutes = round((seconds % 3600) / 60)
remaining_seconds = seconds % 60
print(f'В указанном количестве секунд ({seconds}):\nЧасов: '
      f'{hours}\nМинут: {minutes} \nСекунд: {remaining_seconds}')

#Задание 2
geg_celsius = int(input('Введите градусы по шкале Цельсия:'))
geg_kelvin = 273.15 + geg_celsius
geg_fahrenheit = round(geg_celsius * 1.8 + 32)
geg_reomure = round(geg_celsius * 0.8)
print(f'В указанном количестве градусов цельсия:'
      f' ({geg_celsius}):\nГрадусов Кельвина: {geg_kelvin}'
      f'\nГрадусов Фаренгейта: {geg_fahrenheit} \nГрадусов Реомюра: {geg_reomure}')