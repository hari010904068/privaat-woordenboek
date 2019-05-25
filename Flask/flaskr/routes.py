from flaskr import app
from flaskr.db import get_db
from flask import request

@app.route('/health', methods=['GET'])
def health_check():
    return "health check successfully"

@app.route('/show', methods=['GET'])
def index():
    db = get_db()
    db_res = db.execute("SELECT nederlands, example FROM dictionary ORDER BY random() LIMIT 10").fetchall()
    word_list = []
    for res in db_res:
        dic = {"word": res["nederlands"], "example": res["example"]}
        word_list.append(dic)
    return {"db_res":word_list}

@app.route('/add', methods=['POST'])
def add_word():
    db = get_db()
    db.execute("INSERT INTO dictionary (nederlands, example, rate)" " VALUES (?, ?, ?)",
        (request.json["nederlands"], request.json["example"], 0))
    db.commit()
    return "commit"