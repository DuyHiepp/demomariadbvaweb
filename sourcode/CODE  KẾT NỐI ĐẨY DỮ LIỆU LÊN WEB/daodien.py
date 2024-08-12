from flask import Flask, request, jsonify, render_template
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    connection = mysql.connector.connect(
        host='localhost',
        database='Hiepluvmin',
        user='newuser',
        password='buditlon2'
    )
    return connection

@app.route('/')
def index():
    return render_template("slide.html")

@app.route('/data')
def data():
    query = "SELECT nhietdo, doam, NOW() as time FROM data ORDER BY id DESC LIMIT 10"
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return jsonify(result)

@app.route('/led', methods=['POST'])
def led():
    state = request.args.get('state')
    connection = get_db_connection()
    cursor = connection.cursor()
    # Update the latest record to set LED state
    cursor.execute("UPDATE data SET led=%s ORDER BY id DESC LIMIT 1", (state,))
    connection.commit()
    
    # Retrieve the current LED status
    cursor.execute("SELECT led FROM data ORDER BY id DESC LIMIT 1")
    led_status = cursor.fetchone()['led']
    
    cursor.close()
    connection.close()
    
    # Return LED status as "ON" or "OFF"
    return "ON" if led_status == "1" else "OFF"

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
