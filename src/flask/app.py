from flask import Flask, render_template, jsonify
import sqlite3

app = Flask(__name__)

def get_tables():
    connection = sqlite3.connect("data.db")
    sql_query = "SELECT name FROM sqlite_master WHERE type ='table'"
    cursor = connection.cursor()
    cursor.execute(sql_query)
    lst = cursor.fetchall()
    connection.close()
    return lst

@app.route('/')
def home():
    lst = get_tables()
    print(lst)
    # lst = [item for item in lst]
    return render_template('base.html', lst =lst)

@app.route('/table/<string:table_name>')
def table(table_name):
    connection = sqlite3.connect("data.db")
    sql_query = f"SELECT * from {table_name}"
    cursor = connection.cursor()
    cursor.execute(sql_query)
    lst = cursor.fetchall()
    connection.close()
    return jsonify(lst)



if __name__ == "__main__":
    app.run()