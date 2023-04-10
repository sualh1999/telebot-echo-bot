from flask import Flask
import tg
from tg import telegram
app = Flask(__name__)

@app.route('/')
def ping ():
  return "PONG"

@app.route('/<que>')
def search(que):
    tg.telegram(que)

if __name__ == "__main__":
    app.debug= True
    app.run(host='0.0.0.0',port=8400)
