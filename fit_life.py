# Проект FitLife - MVP версия 1.0
WATER_PER_KG = 30    # Константа потребления воды на кг тела
user_name = input('Здравствуйте, как Вас зовут? ')
user_age = int(input('Очень приятно познакомиться, сколько Вам лет? '))
user_weight = float(input('Подскажите Ваш вес в кг '))
user_height = float(input('Подскажите Ваш рост в м через точку '))


# Функция для расчета ИМТ
def _calc_bmi(weight, height):
    bmi = weight / (height ** 2)
    bmi = round(bmi, 1)
    return bmi


#  Функция для расчета количества потребления воды, от массы тела
def _calc_water_l(weight, wpk):
    wpk = WATER_PER_KG
    water_ml = weight * wpk
    water_l = round((water_ml / 1000), 2)
    return water_l


print(f"Отчет для Вас, {user_name}. ({user_age} лет)")
print(f'Ваш индекс массы тела (ИМТ): {_calc_bmi(user_weight, user_height)}')
print('Вам рекомендуется выпивать', end=' ')
print(f'{_calc_water_l(user_weight, WATER_PER_KG)} л. воды в день')
print('Расчет окончен, будьте здоровы!')
