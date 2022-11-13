from telegram.ext import Updater, MessageHandler, Filters
from bot_commands import *
from config import TOKEN


def main():
    updater = Updater(TOKEN)

    updater.dispatcher.add_handler(MessageHandler(Filters.regex("/start"), start_bot))
    updater.dispatcher.add_handler(MessageHandler(Filters.regex("задать еще вопрос"), question))
    updater.dispatcher.add_handler(MessageHandler(Filters.regex("остановить магию"), stop_bot))
    updater.dispatcher.add_handler(MessageHandler(Filters.regex("включить магию"), start_bot))
    updater.dispatcher.add_handler(MessageHandler(Filters.text, sphere_answer))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
