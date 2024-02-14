from aiogram.fsm.state import StatesGroup, State


# Создаем класс, наследуемый от StatesGroup, для группы состояний нашей FSM
class FSMFillForm(StatesGroup):
    # Создаем экземпляры класса State, последовательно
    # перечисляя возможные состояния, в которых будет находиться
    # бот в разные моменты взаимодейтсвия с пользователем
    fill_name = State()         # Состояние ожидания ввода имени
    fill_age = State()          # Состояние ожидания ввода возраста
    fill_gender = State()       # Состояние ожидания ввода пола
