from random import choice
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import CallbackContext
from log import log_command


def start_bot(update: Update, context: CallbackContext) -> None:
    log_command(update, context)  # Логирует данные пользователя чата (по-идее, лучше сделать с использованием БД)
    keyboard = ReplyKeyboardMarkup([['остановить магию']],
                                   resize_keyboard=True, one_time_keyboard=True)
    greeting = choice([f'Здравствуй, {update.effective_user.first_name}! Я - магическая сфера.\n'
                       f'И я буду отвечать на твои вопросы.\n'
                       f'Напиши вопрос о себе, на который можно ответить "да" или "нет". О чем тебе поведать?',
                       f'Приветствую, {update.effective_user.first_name}! Я - древняя магическая сфера.\n'
                       f'И могу дать ответы на твои вопросы.\n'
                       f'Напиши вопрос о себе, на который можно ответить "да" или "нет".',
                       f'{update.effective_user.first_name}, рада твоему обращению! Я - магическая сфера.\n'
                       f'Я могу подсказать тебе ответ на вопрос.\n'
                       f'Напиши вопрос о себе, на который можно ответить "да" или "нет". Что же ты хочешь узнать?',
                       f'Здравствуй, {update.effective_user.first_name}! \n'
                       f'Возможно, ты уже знаешь, что я - древняя магическая сфера.\n'
                       f'И могу ответить на твои вопросы.\n'
                       f'Напиши вопрос о себе, на который можно ответить "да" или "нет". О чем хочешь узнать?'
                       ])
    update.message.reply_text(f'{greeting}',
                              reply_markup=keyboard)


def question(update: Update, context: CallbackContext) -> None:
    log_command(update, context)
    answer = choice(
        ['Что же ты хочешь узнать? Задай вопрос о себе, на который можно ответить "да" или "нет".',
         'Спрашивай...',
         'Слушаю тебя, мой друг...',
         'Ожидаю твой вопрос...',
         'О чем тебе поведать?'])
    update.message.reply_text(f'{answer}')


def sphere_answer(update, context):
    log_command(update, context)
    keyboard = ReplyKeyboardMarkup([['задать еще вопрос'], ['остановить магию']],
                                   resize_keyboard=True, one_time_keyboard=True)
    ansver = choice(["Бесспорно", "Предрешено", "Никаких сомнений", "Определённо да", "Можешь быть уверен в этом",
                     "Мне кажется - да", "Вероятнее всего", "Хорошие перспективы", "Знаки говорят - да", "Да",
                     "Пока не ясно, попробуй снова", "Сори, но об этом нельзя рассказывать... :)", "Спроси позже",
                     "Лучше не рассказывать", "Сейчас нельзя предсказать",
                     "Сконцентрируйся и спроси опять", "Даже не думай", "Мой ответ - нет", "По моим данным - нет",
                     "Перспективы не очень хорошие", "Весьма сомнительно", "Вполне возможно"])
    update.message.reply_text(f'{ansver}.',
                              reply_markup=keyboard)


def stop_bot(update: Update, context: CallbackContext):
    log_command(update, context)
    keyboard = ReplyKeyboardMarkup([['включить магию']],
                                   resize_keyboard=True, one_time_keyboard=True)
    bye = choice([f'До свидания, {update.effective_user.first_name}! И удачи...',
                  f'{update.effective_user.first_name}, возвращайся, если возникнут вопросы',
                  f'{update.effective_user.first_name}, приходи снова за ответами',
                  f'До свидания, {update.effective_user.first_name}! Буду рада видеть тебя снова! :)'])
    update.message.reply_text(f'{bye}', reply_markup=keyboard)
