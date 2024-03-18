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

def campagin_data(start_date='2024-02-11', end_date='2024-02-15'):
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
            print(start_date, end_date)
            # start_date = '2024-02-10'
            # end_date = '2024-02-20'

            query = f"SELECT * FROM campaign_data3 WHERE `DATE` BETWEEN '{start_date}' AND '{end_date}'"

            start_time = time.time()

            cursor.execute(query)
            rows = cursor.fetchall()

            end_time = time.time()

            fetched_data = []
            for row in rows:                
                roas = float(row['sales']) / row['clicks'] if row['clicks'] != 0 else ""
                cvr = row['clicks'] / row['impressions'] if row['impressions'] != 0 else ""
                cpc = float(row['spends']) / row['clicks'] if row['clicks'] != 0 else ""
                aov = float(row['sales']) / row['orders'] if row['orders'] != 0 else ""

                row_data = {
                    'campaign_id': str(row['campaign_id']),
                    'campaign_name': str(row['campaign_name']),
                    'cpstatus': str(row['campaign_status']),
                    'campaign_budget': str(row['campaign_budget']),
                    'campaign_type':str(row['campaign_type']),  
                    'views': str(row['impressions']),
                    'clicks': str(row['clicks']),
                    'spends': str(row['spends']), 
                    'total_converted_revenue': str(row['sales']),
                    'total_converted_units': str(row['orders']),
                    'campaign_start_and_end_date': row['date'].isoformat(),
                    'roas': roas,
                    'cvr': cvr,
                    'cpc': cpc,
                    'CTR': str(row['ctr']),
                    'aov': aov
                }
                fetched_data.append(row_data)
            print(start_date, end_date)
            print(len(fetched_data))
            return fetched_data
               
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



# print(campagin_data(start_date='2024-02-13', end_date='2024-02-14'))