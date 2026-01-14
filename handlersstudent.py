from aiogram import Router
from aiogram.types import Message
import aiosqlite

from database import DB_NAME

router = Router()


@router.message(lambda message: message.text == "Пройти тест")
async def start_test(message: Message) -> None:
    """
    Начало прохождения теста.
    """
    async with aiosqlite.connect(DB_NAME) as database:
        async with database.execute("""
            SELECT tests.id, tests.title, questions.text, ques-tions.correct_answer
            FROM tests
            JOIN questions ON tests.id = questions.test_id
            LIMIT 1
        """) as cursor:
            record = await cursor.fetchone()

    if record is None:
        await message.answer("Доступных тестов нет.")
        return

    test_id, title, question_text, correct_answer = record

    message.bot.test_id = test_id
    message.bot.correct_answer = correct_answer

    await message.answer(f"Тест: {title}\n\n{question_text}")


@router.message()
async def process_answer(message: Message) -> None:
    """
    Проверка ответа учащегося.
    """
    correct_answer = getattr(message.bot, "correct_answer", None)
    test_id = getattr(message.bot, "test_id", None)

    if correct_answer is None:
        return

    score = 1 if message.text.strip().lower() == correct_answer.lower() else 0

    async with aiosqlite.connect(DB_NAME) as database:
        await database.execute(
            "INSERT INTO results (user_id, test_id, score) VALUES (?, ?, ?)",
            (message.from_user.id, test_id, score)
        )
        await database.commit()

    await message.answer(f"Ваш результат: {score} из 1") 
