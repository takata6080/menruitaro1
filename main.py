from flask import Flask, request, abort
from flask.ext.sqlalchemy import SQLAlchemy
from flask import render_template, request

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, ImageSendMessage, VideoSendMessage, StickerSendMessage, AudioSendMessage
)
import os
import random
import sub

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
db = SQLAlchemy(app)

#環境変数取得
LINE_CHANNEL_ACCESS_TOKEN = os.environ["LINE_CHANNEL_ACCESS_TOKEN"]
LINE_CHANNEL_SECRET = os.environ["LINE_CHANNEL_SECRET"]

line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(LINE_CHANNEL_SECRET)

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
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    returnMessage = sub.return_message(event.message.text)
    line_bot_api.reply_message(event.reply_token,TextSendMessage(text=returnMessage))

# # モデル作成
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True)
#     email = db.Column(db.String(80), unique=True)

#     def __init__(self, username, email):
#         self.username = username
#         self.email = email

#     def __repr__(self):
#         return '<User %r>' % self.username

# class Task(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     tasks = db.Column(db.String(80))
#     user_id = db.Column(db.Integer,db.ForeignKey('user.id'))

#     def __init__(self, tasks, user_id):
#         self.tasks = tasks
#         self.user_id = user_id

#     def __repr__(self):
#         return '<Task %r>' % self.tasks

# # データベースに追加するコード例
# @app.route("/", methods=['POST'])
# def register():
#     if request.method == 'POST':
#         name= request.form['name']
#         email = request.form['email']
#         task = request.form['task']
#         # emailが未登録ならユーザー追加
#         if not db.session.query(User).filter(User.email == email).count():
#             reg = User(name, email)
#             db.session.add(reg)
#             db.session.commit()


#         # タスク追加
#         user_id= User.query.filter_by(User.email == email).first().id
#         task = Task(text, user_id)
#         db.session.add(task)
#         db.session.commit()

#         return render_template('success.html')  return render_template('index.html')

if __name__ == "__main__":
#    app.run()
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)