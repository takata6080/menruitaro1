from flask import Flask, request, abort
# from config
# from flask.ext.sqlalchemy import SQLAlchemy
# from flask import render_template, request

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, ImageMessage, ImageSendMessage, VideoSendMessage, StickerSendMessage, AudioSendMessage,Event
)

import os
import random
import sub

# import psycopg2 
# import psycopg2.extras
import os



app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
# db = SQLAlchemy(app)

#環境変数取得
LINE_CHANNEL_ACCESS_TOKEN = os.environ["LINE_CHANNEL_ACCESS_TOKEN"]
LINE_CHANNEL_SECRET = os.environ["LINE_CHANNEL_SECRET"]

line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(LINE_CHANNEL_SECRET)

# モデル作成
# class MyCity(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.String(80))
#     hnt_member = db.Column(db.String(80))

#     def __init__(self, user_id, hnt_member):
#         self.user_id = user_id
#         self.hnt_member = hnt_member


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
    text_message = sub.return_message(event.message.text)
    
    returnMessage = []
    for message in text_message:
        returnMessage.append(TextSendMessage(text=message))
    FQDN = 'https://git.heroku.com/menruitaro1.git'
    # line_bot_api.reply_message(event.reply_token,returnMessage)
    line_bot_api.reply_message(
        event.reply_token,
        ImageSendMessage(
            original_content_url = FQDN + '/images/' + 'tomita' + '.jpg',
            preview_image_url = FQDN + '/images/' + 'tomita' + '.jpg'
        )    
    )

# @handler.add(Event, timestamp=ImageMessage)
# def handle_image(event):

#     main_image_path = "images/main.jpg"
#     preview_image_path = "images/preview.jpg"

#     # 画像の送信
#     image_message = ImageSendMessage(
#         preview_image_url=f"https://menruitaro1.herokuapp.com/{preview_image_path}"
#     )

#     line_bot_api.reply_message(event.reply_token, image_message)

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

    # #postgreSQLに接続（接続情報は環境変数、PG_XXX）
    # connection = psycopg2.connect(\ 
    #     host=os.environ.get('PG_HOST'),\ 
    #     user=os.environ.get('PG_USER'),\ 
    #     password=os.environ.get('PG_PASS'),\ 
    #     database=os.environ.get('PG_DBNM'),\ 
    #     port=int(os.environ.get('PG_PORT'))) 

    # #クライアントプログラムのエンコードを設定（DBの文字コードから自動変換してくれる）
    # connection.set_client_encoding('utf-8') 

    # #select結果を辞書形式で取得するように設定 
    # connection.cursor_factory=psycopg2.extras.DictCursor

    # #カーソルの取得
    # cursor = connection.cursor() 

    # #SQL文設定(%はバインド変数）
    # sql = 'select name, work from m_user where id = %(target_id)s'

    # #SQL実行
    # target_id = 1
    # cursor.execute(sql, {'target_id': (target_id,)}) 

    # #取得結果を出力　★辞書形式　row['name']　辞書形式でなければ、row[0]、orz
    # results = cursor.fetchall() 
    # for row in results: 
    #     print(row['name'])
    #     print(row['work'])

    # #カーソルをとじる
    # cursor.close() 

    # #切断
    # connection.close() 