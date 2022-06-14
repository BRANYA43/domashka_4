INCREASE = 1.1
count_day = 0
distance = int(input('Введіть число скільки пробіг в перший день спортсмен (км): '))
search_distance = int(input('Введіть число скільки повинен пробігти спортсмен (км): '))

while distance < search_distance:
    distance *= INCREASE
    count_day += 1

print(f'Спортсмен досяг відмітки {search_distance}(км) у {count_day + 1} день.')
