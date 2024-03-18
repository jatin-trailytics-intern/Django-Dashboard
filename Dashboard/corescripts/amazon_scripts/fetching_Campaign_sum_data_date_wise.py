import mysql.connector
import json
from decimal import Decimal
from datetime import date, datetime
import time

class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return float(obj)
        elif isinstance(obj, (date, datetime)):
            return obj.isoformat()
        else:
            return super().default(obj)

try:
    
    connection = mysql.connector.connect(
        host="tr-wp-database.cfqdq6ohjn0p.us-east-1.rds.amazonaws.com",
        port="3306",
        user="aatif",
        password="Trailytics@789",
        database="amazon_ads_api"
    )

    if connection.is_connected():
        print("Connected to MySQL database")

        cursor = connection.cursor(dictionary=True) 

      
        start_date = '2024-02-10'
        end_date = '2024-02-20'

        query = f"""
        SELECT
            date,
            SUM(clicks) AS total_clicks,
            SUM(impressions) AS total_impressions,
            SUM(spends) AS total_spends,
            SUM(sales) AS total_sales,
            SUM(orders) AS total_orders,
            SUM(sales) / SUM(clicks) AS roas,
            SUM(clicks) / SUM(impressions) AS cvr,
            SUM(spends) / SUM(clicks) AS cpc,
            SUM(sales) / SUM(orders) AS aov,
            SUM(ctr) AS total_ctr
        FROM
            campaign_data3
        WHERE
            date BETWEEN '{start_date}' AND '{end_date}'
        GROUP BY
            date
        """

        start_time = time.time()

        cursor.execute(query)

        rows = cursor.fetchall()

        data_list = [row for row in rows]

        end_time = time.time()

        fetched_data = []
        for row_data in data_list:
            row_data_without_types = {key: str(value) for key, value in row_data.items()}
            fetched_data.append(row_data_without_types)

        print(fetched_data)

        



except mysql.connector.Error as error:
    print("Error while connecting to MySQL", error)

finally:
  
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
