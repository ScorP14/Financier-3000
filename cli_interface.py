from art import tprint

from app import CreateExpense


def banner():
    tprint("Financier 3000")


def greetings():
    print('Приложение для учета финансов. Поможет сэкономить ваши деньги! :)')


def help_banner():
    print("""
        -a, -ai, -ae:   Показать все записи/доход/расход
        -ba, -bi, -be:  Показать текущий баланс/доход/расход
        -c:             Добавить запись
        -u              Обновить запись 
        -sd <date>      Фильтр по дате
        -sp <int-int>   Фильтр по диапазону сумм 
        -q              Выход
    """)


def create_view(app):
    while True:
        print(f'\nДля создания записи внесите данные. Формата"(Дата, Категория(доход, расход), сумма, Описания)"')
        print('Пример: 2020-10-25, Доход, 15000, Зарплата')
        string_cmd = input('Что бы вернуться назад введите: -b \n')
        if string_cmd.strip().lower() in ['-b']:
            return
        try:
            instance = CreateExpense.parse_and_valid_string_for_db(string_cmd)
        except ValueError:
            print('Данные ведены не верно, попробуйте снова')
            continue
        app.create_item(instance)
        print('Запись успешно добавлена')
        return


def update_view(app):
    while True:
        item_id = input('Введите id записи которую хотите изменить(Что бы вернуться назад введите: -b): ')
        if item_id.strip().lower() in ['-b']:
            return
        try:
            instance = app.get_by_item_id(item_id)
        except KeyError:
            print('Записи с таким id не найдено')
            continue
        print(
            f'Изменить запись: ({instance.date}) {instance.category.title()} - {instance.price}, {instance.descriptions}\n'
            f'Введите новые данные(Что бы вернуться назад введите: -b):'
        )
        cmd = input()
        if cmd.strip().lower() in ['-b']:
            return
        instance = CreateExpense.parse_and_valid_string_for_db(cmd)
        app.update_item(item_id, instance)
        print('Запись успешно изменена')
        return

