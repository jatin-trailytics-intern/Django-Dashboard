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

fetched_data = []  # Move fetched_data declaration outside of try block

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

        query = f"SELECT * FROM keyword_data WHERE `DATE` BETWEEN '{start_date}' AND '{end_date}'"

        start_time = time.time()

        cursor.execute(query)
        rows = cursor.fetchall()

        end_time = time.time()

        for row in rows:
            roas = float(row['sales']) / row['clicks'] if row['clicks'] != 0 else None

            row_data = {
                'keyword_name': row['keyword_name'],
                'keyword_id': str(row['keyword_id']),
                'keyword_bid': str(row['keyword_bid']),
                'keyword_status': row['keyword_status'],
                'ad_group_id': row['ad_group_id'],
                'ad_group_name': row['ad_group_name'],
                'keyword_type': row['keyword_type'],
                'match_type': row['match_type'],
                'impressions': str(row['impressions']),
                'clicks': str(row['clicks']),
                'spends': str(row['spends']),
                'sales': str(row['sales']),
                'orders': str(row['orders']),
                'campaign_id': str(row['campaign_id']),
                'campaign_name': row['campaign_name'],
                'campaign_type': row['campaign_type'],
                'date': row['DATE'].isoformat(),
                'roas': roas,
                'created_on': row['created_on'].isoformat(),
            }
            fetched_data.append(row_data)

        print(fetched_data[0])
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

# Return the fetched data list
