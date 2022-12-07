from flask import Flask

#Flaskのインスタンスを作成
app = Flask(__name__)

#ルーティングの指定
@app.route('/')
def index():
    return "Hello World !! ????"

#実行
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)