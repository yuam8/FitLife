# Проект FitLife - MVP версия 1.0
WATER_PER_KG = 30    # Константа потребления воды на кг тела
user_name = input('Здравствуйте, как Вас зовут? ')
user_age = int(input('Очень приятно познакомиться, сколько Вам лет? '))
user_weight = float(input('Подскажите Ваш вес в кг '))
user_height = float(input('Подскажите Ваш рост в м через точку '))


# Функция для расчета ИМТ
def _calc_bmi(weight, height):
    bmi = weight / (height ** 2)
    return round(bmi,1)


#  Функция для расчета количества потребления воды, от массы тела
def _calc_water_l(weight, wpk):
    wpk = WATER_PER_KG
    water_ml = weight * wpk
    round((water_ml / 1000), 2)
    return round((water_ml / 1000), 2)


liters_per_day = _calc_water_l(user_weight, WATER_PER_KG)
bmi = _calc_bmi(user_weight, user_height)

print(f"Отчет для Вас, {user_name}. ({user_age} лет)")
print('Ваш индекс массы тела (ИМТ):', bmi)
print('Вам рекомендуется выпивать', end=' ')
print(f'{liters_per_day} л. воды в день')
print('Расчет окончен, будьте здоровы!')
