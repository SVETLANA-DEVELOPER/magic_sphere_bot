from telegram import Update
from telegram.ext import CallbackContext


def log_command(update: Update, context: CallbackContext) -> None:
    with open('users_info.csv', 'a') as f:
        f.write(f'{update.effective_user.first_name}, {update.effective_user.last_name}, {update.message.date},'
                f'{update.message.text}\n')
        