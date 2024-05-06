from app import App
from cli_interface import banner, help_banner, greetings, create_view, update_view, delete_view
from shema import CategoryExpenseEnum
from utils import get_db, PrintExpense


# Можно выбрать тип базы json/csv
db = get_db('json')
app = App(database=db)

if __name__ == '__main__':
    banner()
    greetings()
    help_banner()

    while True:
        cmd = input('Введите команду(-h помощь): ').split()
        if len(cmd) == 1:
            cmd = cmd[0]
        match cmd:
            case '-a':
                PrintExpense.print_list_expense(app.get_all_list_item())
            case '-ai':
                PrintExpense.print_list_expense(app.get_list_item_by_category(CategoryExpenseEnum.INCOME))
            case '-ae':
                PrintExpense.print_list_expense(app.get_list_item_by_category(CategoryExpenseEnum.CONSUMPTION))
            case '-ba':
                print(f'Текущий баланс: {app.get_current_balance()}')
            case '-bi':
                print(f'Текущий доход: {app.get_total_sum_category(CategoryExpenseEnum.INCOME)}')
            case '-be':
                print(f'Текущий расход: {app.get_total_sum_category(CategoryExpenseEnum.CONSUMPTION)}')
            case '-c':
                create_view(app)
            case '-u':
                update_view(app)
            case '-d':
                delete_view(app)
            case '-sd', search_data:
                print(f'Фильтр по дате')
                PrintExpense.print_list_expense(app.search_by_date(search_data))
            case '-sp', search_price:
                print(f'Фильтр по диапазону сумм: {search_price}')
                PrintExpense.print_list_expense(app.search_by_price(search_price))
            case '-h':
                help_banner()
            case '-q':
                print('Завершение работы, удачи вам и вашим финансам!:)')
                break
            case _:
                print('Неизвестная команда, попробуйте снова')
