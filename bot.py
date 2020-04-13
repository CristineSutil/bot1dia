#import requests
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                         RegexHandler, ConversationHandler)
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove


STATE1 = 1
STATE2 = 2
#STATE3 = 3
#STATE4 = 4

def welcome(update, context):
    try:
        username = update.message.from_user.username
        firstName = update.message.from_user.first_name
        lastName = update.message.from_user.last_name
        message = 'Olá, ' + firstName + '!' + 'Olá sou Drinha Aninha Bot, Estou aqui pra te ajudar?'
        context.bot.send_message(chat_id=update.effective_chat.id, text=message)
    except Exception as e:
        print(str(e))


def coronaquestions(update, context):
    try:
        message = """Escolha uma opção abaixo para começarmos: \n
            1 - O que é Coronavirus\n
            2 - Como podemos nos previnir\n
            3 - Você sabia\n"""
        update.message.reply_text(message, reply_markup=ReplyKeyboardMarkup([], one_time_keyboard=True)) 
        return STATE1
    except Exception as e:
        print(str(e))


def inputCoronaquestions(update, context):
    coronaquestions = update.message.text
    print(coronaquestions)
    if (coronaquestions == "1" 
    or coronaquestions == "O que é Coronavirus"
    or coronaquestions =="Coronavirus"
    or coronaquestions == "virus"):
        message = """colocar o que eu quero na resposta 1"""
        context.bot.send_message(chat_id=update.effective_chat.id, text=message)
        return STATE2
    elif (coronaquestions == "2" 
    or coronaquestions == "Como podemos nos previnir"
    or coronaquestions =="prevenção"
    or coronaquestions == "previnir"):
       message = """colocar o que eu quero na resposta 2"""
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)
    return STATE2

def inputCoronaquestions2(update, context):
    message = "Muito obrigada! Em breve teremos novidades :)"
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)


def cancel(update, context):
    return ConversationHandler.END


def main():
    try:
        # token = os.getenv('TELEGRAM_BOT_TOKEN', None)
        token = '1142922385:AAHHif6VHp9QZK7kKucZWhmbkxn7wl81KhI'
        updater = Updater(token=token, use_context=True)

        updater.dispatcher.add_handler(CommandHandler('start', welcome))

        conversation_handler = ConversationHandler(
            entry_points=[CommandHandler('coronaquestions', coronaquestions)],
            states={
                STATE1: [MessageHandler(Filters.text, inputCoronaquestions)],
                STATE2: [MessageHandler(Filters.text, inputCoronaquestions2)]
            },
            fallbacks=[CommandHandler('cancel', cancel)])
        updater.dispatcher.add_handler(conversation_handler)

        print(str(updater))
        updater.start_polling()
        updater.idle()
    except Exception as e:
        print(str(e))


if __name__ == "__main__":
    main()

