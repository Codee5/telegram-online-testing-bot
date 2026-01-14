from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
import aiosqlite

from config import ADMIN_IDS
from states import TestCreationStates
from database import DB_NAME

router = Router()


@router.message(lambda message: message.from_user.id in ADMIN_IDS and mes-sage.text == "Создать тест")
async def start_test_creation(message: Message, state: FSMContext) -> None:
    """
    Начало создания теста.
    """
    await message.answer("Введите название теста:")
    await state.set_state(TestCreationStates.waiting_for_title)
