from aiogram.fsm.state import StatesGroup, State


class TestCreationStates(StatesGroup):
    """
    Состояния создания теста преподавателем.
    """
    waiting_for_title = State()
    waiting_for_question = State()
    waiting_for_correct_answer = State()


class TestPassingStates(StatesGroup):
    """
    Состояния прохождения теста учащимся.
    """
    waiting_for_answer = State()    
