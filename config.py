invalid_email = 'abrakadabra@mail.ru'
invalid_pass = 'blablabla'

valid_mobile = '89869267058'
invalid_pass = 'Qwerty11111'

name = 'Анна'
surname = 'Дмеири'
region = 'Республика Татарстан'
mobile = '89869267058'
password = 'Qwerty123zzz'


false_mobile_mini = '8986926705'
false_mobile_pass = 'qwerty123zzz'
false_pass = 'приветвсем'
different_pass = "Qwerty123zzx"


class TestData:
    BASE_URL = 'https://b2c.passport.rt.ru/'

    #Заголовки названий элементов
    FORM_AUTH_MAIL = 'Почта'
    AUTH = 'Авторизация'
    RECOVERY = 'Восстановление пароля'
    CHECK = 'Регистрация'
    VERIFICATION_EMAIL = 'Подтверждение email'
    VERIFICATION_INVALID_EMAIL = 'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru'
    VERIFICATION_INVALID_NAME = 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'
    ENTRY_VK = 'Войти'
    OK = 'Одноклассники'
    CHOICE_ACCOUNT = 'Вход'
    MM = 'Войти и разрешить'
