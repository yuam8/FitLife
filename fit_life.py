# Проект FitLife - MVP версия 1.0
WATER_PER_KG = 30 # Константа потребления воды на кг тела
ML_PER_L = 1000 # Константа перевода мл в л   
user_name = input('Здравствуйте, как Вас зовут? ')


while True:
    try:
        user_age = int(input('Очень приятно познакомиться, сколько Вам лет? '))
        if user_age <= 0 or user_age > 100:
            print('Введите возраст от 0 до 100 лет')
            continue
        break
    except ValueError:
        print('Введите возраст целым числом')
         

while True:
    try:
        user_weight = float(input('Введите Ваш вес в кг используя точку: "81.2" '))
        if user_weight <= 0 or user_weight > 650:
            print('Введите реальный вес')
            continue
        break
    except ValueError:
        print('Вес должен быть от 0 до 650 кг и введен через точку')
            

while True:
    try:
        user_height = float(input('Подскажите Ваш рост в м через точку: "1.89" '))
        if user_height <= 0 or user_height > 3:
            print('Введите реальный рост')
            continue
        break
    except ValueError:
        print('Рост должен быть от 0 до 3 м и введен через точку')



# Функция для расчета ИМТ
def _calc_bmi(weight, height):
    bmi = weight / (height ** 2)
    return round(bmi, 1)


#  Функция для расчета количества потребления воды, от массы тела
def _calc_water_l(weight):
    water_ml = weight * WATER_PER_KG
    return round((water_ml / ML_PER_L), 2)


liters_per_day = _calc_water_l(user_weight)
bmi = _calc_bmi(user_weight, user_height)

print(f"Отчет для Вас, {user_name}. ({user_age} лет)")
print('Ваш индекс массы тела (ИМТ):', bmi)
print('Вам рекомендуется выпивать', end=' ')
print(f'{liters_per_day} л. воды в день')
print('Расчет окончен, будьте здоровы!')
