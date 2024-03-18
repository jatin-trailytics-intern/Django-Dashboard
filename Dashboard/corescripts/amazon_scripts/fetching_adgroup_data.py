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



def adgroups_data(start_date = '2024-02-10', end_date = '2024-02-11'):
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
            query = ("SELECT * FROM adgroup_data WHERE `DATE` BETWEEN %s AND %s")
            cursor.execute(query, (start_date, end_date))
            rows = cursor.fetchall()

            fetched_data = []
            for row in rows:
                roas = float(row['sales']) / row['clicks'] if row['clicks'] != 0 else 0
                ctr = (row['clicks'] / row['impressions']) * 100 if row['impressions'] != 0 else 0
                
                row_data = {
                    'campaign_id': str(row['campaign_id']),
                    'campaign_name': str(row['campaign_name']),
                    'ad_group_id': str(row['ad_group_id']),
                    'ad_group_name': str(row['ad_group_name']),
                    'impressions': str(row['impressions']),
                    'clicks': str(row['clicks']),
                    'spends': str(row['spends']),
                    'sales': str(row['sales']),
                    'orders': str(row['orders']),
                    'campaign_type': str(row['campaign_type']),
                    'date': row['DATE'].isoformat(),
                    'ad_status': str(row['ad_status']),
                    'roas': roas,
                    'ctr':ctr
                    # 'cvr': cvr,
                    # 'cpc': cpc,
                    # 'aov': aov
                }
                fetched_data.append(row_data)

            # Print fetched_data as a list of dictionaries
            return fetched_data

    except mysql.connector.Error as error:
        print("Error while connecting to MySQL", error)

    except Exception as e:
        print("Error:", e)

    finally:
        # Closing the cursor and database connection
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")



print(adgroups_data())