import mysql.connector
import json
from decimal import Decimal
from datetime import datetime
import time

class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return float(obj)
        elif isinstance(obj, datetime):
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

        start_date = datetime.strptime('2024-02-10', '%Y-%m-%d')
        end_date = datetime.strptime('2024-02-15', '%Y-%m-%d')

        query = "SELECT ad_group_id, ad_group_name, campaign_name, campaign_type, product_name, SUM(impressions) AS total_impressions, SUM(clicks) AS total_clicks, SUM(spends) AS total_spends, SUM(sales) AS total_sales FROM product_data WHERE `DATE` BETWEEN %s AND %s GROUP BY ad_group_id, ad_group_name, campaign_name, campaign_type, product_name"
        start_time = time.time()

        cursor.execute(query, (start_date, end_date))
        rows = cursor.fetchall()

        end_time = time.time()

        fetched_data = []
        for row in rows:
            roas = float(row['total_sales']) / float(row['total_clicks']) if float(row['total_clicks']) != 0 else None
            
            row_data = {
                'product_name': str(row['product_name']),
                'campaign_name': str(row['campaign_name']),
                'ad_group_name': str(row['ad_group_name']),
                'campaign_type': str(row['campaign_type']),
                'total_impressions': str(row['total_impressions']),
                'total_clicks': str(row['total_clicks']),
                'total_spends': str(row['total_spends']), 
                'total_sales': str(row['total_sales']),
                'ctr': float(row['total_clicks']) / float(row['total_impressions']) if float(row['total_impressions']) != 0 else None,
                'roas': roas,
            }
            fetched_data.append(row_data)

     
        print(fetched_data)
        print(type(fetched_data))
        print(len(fetched_data))
        
        elapsed_time = end_time - start_time
        print("Time taken to fetch data:", elapsed_time, "seconds")

except mysql.connector.Error as error:
    print("Error while connecting to MySQL", error)

finally:
    # Closing the cursor and database connection
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
