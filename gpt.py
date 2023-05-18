import openai
import requests
import json
import telebot as tb

API_KEY = "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"
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "content-type": "Application/json"
}

TOKEN = "5316314908:AAGNBNR4G175TS_r7UUnH7myPr4QW7CkRm8"
bot = tb.TeleBot(TOKEN)

@bot.message_handler(commands=['t'])
def text(message):
    msg = str(message.text).replace("/t ", "")
    body = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": msg}]
    }

    body = json.dumps(body)
    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, data=body)
    bot.reply_to(message, text=response.json()["choices"][0]["message"]["content"], parse_mode="Markdown")

bot.infinity_polling()