from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('9IYtaIHvbU5mMxDMLgRg4hqwYdyWMu5lXq551oiJ/ALJ6ePlAs01IGmloiSfitBuE5nEeXQ4lDpCoea/E4W4Q9sfa14g9w3XfE7rWO+oyvcBjz0XSjELtQ+0qq1NvQHJBGvUZ1veTT4ZIsb1Hpl/9gdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('ea8003179336738ce12fdd69264dbfb0')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):

    msg = event.message.text
    reply = 'Damn~~~~'
    if msg == ['hi', 'Hi']:
        reply = 'fuck'
    elif '吃飯' in msg:
        reply = '賈霸阿'
    elif ['幹', '乾'] in msg:
        reply = 'watch your mouth!'



    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text= reply))


if __name__ == "__main__":
    app.run()