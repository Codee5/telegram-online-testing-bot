from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def get_main_keyboard() -> ReplyKeyboardMarkup:
    """
    Основная клавиатура пользователя.
    """
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Пройти тест")],
            [KeyboardButton(text="Создать тест")]
        ],
        resize_keyboard=True
    )
    return keyboard
