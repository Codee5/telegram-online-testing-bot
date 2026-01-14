import aiosqlite

DB_NAME = "tests.db"


async def init_db() -> None:
    """
    Инициализация базы данных.
    Создание таблиц при первом запуске системы.
    """
    async with aiosqlite.connect(DB_NAME) as database:
        await database.execute("""
        CREATE TABLE IF NOT EXISTS tests (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL
        )
        """)

        await database.execute("""
        CREATE TABLE IF NOT EXISTS questions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            test_id INTEGER NOT NULL,
            text TEXT NOT NULL,
            correct_answer TEXT NOT NULL,
            FOREIGN KEY (test_id) REFERENCES tests (id)
        )
        """)

        await database.execute("""
        CREATE TABLE IF NOT EXISTS results (
            user_id INTEGER NOT NULL,
            test_id INTEGER NOT NULL,
            score INTEGER NOT NULL
        )
        """)
        await database.commit()
