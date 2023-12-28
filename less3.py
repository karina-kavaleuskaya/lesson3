#task 1
some_int_x = 4
some_int_y = 7
some_int_z = 9
print('Сумма данных трех целочисленных переменныч равна:', some_int_x + some_int_y + some_int_z)
print('Разность данных трех целочисленных переменныч равна:', some_int_x - some_int_y - some_int_z)
print('Произведение данных трех целочисленных переменныч равна:', some_int_x * some_int_y * some_int_z)
print('Разность первой переменной и вторую, с добавлением третьей равна:', some_int_x - some_int_y + some_int_z)
print('Деление произведения первой переменной и второй на третью равно:', (some_int_x * some_int_y) / some_int_z)
print('Остаток от суммы первых двух переменных и деления на третью переменную:', (some_int_x + some_int_y) % some_int_z)


#task 2
cat_a = 4
cat_b = 9
print('Плащадь прямоугльного треугольника равна :', (cat_a * cat_b) / 2)
print('Гипотенуза прямоугльного треугольника равна :', ((cat_a ** 2) + (cat_b ** 2)) ** 0.5)


#task 3

some_str_one = "Hello world"
words_one = some_str_one.count(" ") + 1
print('Количество слов в строке',some_str_one, ':', words_one)

some_str_two = "a b c"
words_two = some_str_two.count(" ") + 1
print('Количество слов в строке',some_str_two, ':', words_two)

some_str_three = "test"
words_three = some_str_three.count(" ") + 1
print('Количество слов в строке',some_str_three, ':', words_three)

some_str_four = "test1 test2 test3 test4 test5"
words_four = some_str_four.count(" ") + 1
print('Количество слов в строке',some_str_four, ':', words_four)


#task 4
str = 'hhhhhhhhh'
str_step_one = str.replace('h', 'H', str.count('h') - 1)
str_step_two = str_step_one.replace('H', 'h', 1)
print(str_step_two)



#task 5
str_one = "TEST-STR"
print('Tретий символ', str_one[2])
print('Предпоследний символ', str_one[-2])
print('Первые пять символов строки', str_one[:5])
print('Вся до последних двух символов', str_one[:-2])
print('Все символы с четными индексами', str_one[::2])
print('Все символы с нечетными индексами', str_one[1::2])
print('Все символы в обратном порядке', str_one[::-1])
str_seven = str_one[::-1]
print('Все символы строки через один в обратном порядке, начиная с последнего.', str_seven[::2])
print('Tретий символ', len(str_one))


#task 6
some_int_a = 256
print ('Последняй цифрой числа:', some_int_a, 'является', some_int_a % 10)


#task 7
some_int_b = 999
print ('Дисяток числа:', some_int_b, 'является', some_int_b // 10 % 10)


#task 8
some_int_c = 999
print('Сумма всех чисел ровна:', (some_int_c // 10 // 10 % 10) + (some_int_c // 10 % 10) + (some_int_c % 10))