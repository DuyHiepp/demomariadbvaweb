

# CODE THU THẬP THÔNG TIN TỪ CẢM BIẾN VÀ KẾT NỐI ĐẾN MARIADB



import mysql.connector
import random
from time import sleep

# Kết nối đến MariaDB
try:
    conn = mysql.connector.connect(
        user="newuser",
        password="buditlon2",
        host="localhost",
        port=3306,
        database="Hiepluvmin"
    )
except mysql.connector.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    exit(1)

# Tạo một con trỏ 
cur = conn.cursor()

def get_led_status():
    try:
        cur.execute("SELECT led FROM data ORDER BY id DESC LIMIT 1")
        result = cur.fetchone()
        return result[0] if result else False
    except mysql.connector.Error as e:
        print(f"Error: {e}")
        return False

def insert_data(nhietdo, doam, led):
    try:
        cur.execute("INSERT INTO data (nhietdo, doam, led) VALUES (%s, %s, %s)",
                    (nhietdo, doam, led))
        conn.commit()
    except mysql.connector.Error as e:
        print(f"Error: {e}")

while True:
    # tạo giá trị đầu vào
    nhietdo = round(random.uniform(20.0, 30.0), 2)
    doam = round(random.uniform(30.0, 70.0), 2)
    led = get_led_status()

    # Ghi dữ liệu vào cơ sở dữ liệu
    insert_data(nhietdo, doam, led)
    print(f"Giá trị: Temp={nhietdo}°C, doam={doam}%, LED={led}")
    print()

    sleep(5)

# Đóng kết nối
conn.close()
