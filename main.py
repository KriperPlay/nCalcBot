import telebot
from telebot import types
from math import pi

TOKEN = ""
permitted_words = ['0','1','2','3','4','5','6','7','8','9','-','+','/','*','.','(',')',' ', '<','>','=','p','i']
pi2 = str(pi)[0:4]

bot = telebot.TeleBot(TOKEN)

def calc_full(expession: str) -> str:
    true_words = 0
    try:
        for word in expession:
            if word in permitted_words:
                true_words += 1
        if true_words == len(expession):
            return f"{expession} => {eval(expession)}"
        else:
            return f"{expession} => SyntaxError!"

    except SyntaxError:
        return f"{expession} => SyntaxError!"
    except TypeError:
        return f"{expession} => SyntaxError!"
    except ZeroDivisionError:
        return f"{expession} => ZeroDivisionError!"
    except NameError:
        return f"{expession} => SyntaxError!"

def calc(expession: str) -> str:
    true_words = 0
    try:
        for word in expession:
            if word in permitted_words:
                true_words += 1
        if true_words == len(expession):
            return f"{eval(expession)}"
        else:
            return "SyntaxError!"

    except SyntaxError:
        return "SyntaxError!"
    except TypeError:
        return "SyntaxError!"
    except ZeroDivisionError:
        return "ZeroDivisionError!"
    except NameError:
        return "SyntaxError!"

@bot.inline_handler(lambda query: len(query.query) > 0)
def query_text(inline_query):
    try:
        result = calc_full(inline_query.query)
        result2 = calc(inline_query.query)
        r = types.InlineQueryResultArticle('1', result, types.InputTextMessageContent(result))
        r2 = types.InlineQueryResultArticle('2', result2, types.InputTextMessageContent(result2))
        bot.answer_inline_query(inline_query.id, [r,r2])
    except Exception as e:
        print(e)

@bot.inline_handler(lambda query: len(query.query) == 0)
def default_query(inline_query):
    try:
        r = types.InlineQueryResultArticle('1', 'nothing', types.InputTextMessageContent('nothing'))
        bot.answer_inline_query(inline_query.id, [r])
    except Exception as e:
        print(e)

if __name__ == "__main__":
    bot.infinity_polling()\

