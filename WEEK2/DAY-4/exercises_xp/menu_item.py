# ============================================
# PART 1 : menu_item.py
# ============================================

import psycopg2

class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def save(self):
        connection = psycopg2.connect(
            dbname="restaurant",
            user="postgres",
            password="your_password",
            host="localhost",
            port="5432"
        )
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO Menu_Items (item_name, item_price) VALUES (%s, %s)",
            (self.name, self.price)
        )
        connection.commit()
        cursor.close()
        connection.close()

    def delete(self):
        connection = psycopg2.connect(
            dbname="restaurant",
            user="postgres",
            password="your_password",
            host="localhost",
            port="5432"
        )
        cursor = connection.cursor()
        cursor.execute(
            "DELETE FROM Menu_Items WHERE item_name = %s",
            (self.name,)
        )
        connection.commit()
        cursor.close()
        connection.close()

    def update(self, new_name=None, new_price=None):
        connection = psycopg2.connect(
            dbname="restaurant",
            user="postgres",
            password="your_password",
            host="localhost",
            port="5432"
        )
        cursor = connection.cursor()
        if new_name:
            cursor.execute(
                "UPDATE Menu_Items SET item_name = %s WHERE item_name = %s",
                (new_name, self.name)
            )
            self.name = new_name
        if new_price is not None:
            cursor.execute(
                "UPDATE Menu_Items SET item_price = %s WHERE item_name = %s",
                (new_price, self.name)
            )
            self.price = new_price
        connection.commit()
        cursor.close()
        connection.close()
