import json

from flask import Flask
import pymysql
from urllib.parse import unquote

db = pymysql.connect("localhost", "root", "7Music88", "mydb")
app = Flask(__name__)

@app.route('/get_by_id/<string:id>/')
def user_view(id):

    with db.cursor() as cursor:
        sql = "SELECT * FROM `Result` WHERE id = " + id
        cursor.execute(sql)
        # Выполнить команду запроса (Execute Query).
        last = 0
        for row in cursor:
            return str(row)

@app.route('/get_new_code', methods=['GET'])
def get_new_qr():
        with db.cursor() as cursor:
            sql = "INSERT INTO `Result` (`IsValid`, `Results`) VALUES ('1', '0');"
            cursor.execute(sql)
            db.commit()
            sql = "SELECT * FROM `Result`"
            cursor.execute(sql)
            # Выполнить команду запроса (Execute Query).
            last = 0
            for row in cursor:
                last = row[0]
        return str(last)


@app.route('/set_result/<string:info>/<string:id>', methods=['GET'])
def set_info(info,id):
    with db.cursor() as cursor:
        sql = "UPDATE `Result` SET `Results` = '"+ info +"' WHERE (`id` = 1);"
        cursor.execute(sql)
        db.commit()
    return "Accepted"

if __name__ == '__main__':
    app.run()


