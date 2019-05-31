from flaskr import app
from flaskr.db import get_db
from flask import request
from flask import jsonify


@app.route("/health", methods=["GET"])
def health_check():
    return "health check successfully"


@app.route("/show", methods=["GET"])
def index():
    db = get_db()
    db_res = db.execute(
        "SELECT dutch, example, note FROM dictionary ORDER BY random() LIMIT 10"
    ).fetchall()
    print(db_res)
    word_list = []
    for res in db_res:
        dic = {"word": res["dutch"], "example": res["example"]}
        word_list.append(dic)
    return jsonify({"db_res": word_list})


@app.route("/add", methods=["POST"])
def add_word():
    db = get_db()
    if "note" not in request.json.keys():
        request.json["note"] = "N/A"
    print(request.json)
    db.execute(
        "INSERT INTO dictionary (dutch, example, note)" " VALUES (?, ?, ?)",
        (request.json["nederlands"], request.json["voorbeeld"], request.json["note"]),
    )
    db.commit()
    print("commit")
    return "commit"
