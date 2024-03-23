import os
import pymysql
import decimal
from datetime import datetime


def flipKeywords():
    DB_HOST = "tr-wp-database.cfqdq6ohjn0p.us-east-1.rds.amazonaws.com"
    DB_USER = "shivam"
    DB_PASSWORD = "Trailytics@789"
    DB_DATABASE = "amazon_ads_api"
    DB_PORT = 3306

    connection = pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        db=DB_DATABASE,
        port=DB_PORT,
        connect_timeout=1000,
        autocommit=True
    )

    cursor = connection.cursor()
    collect_data = []
    start_date = '2024-03-02'
    end_date = '2024-03-02'
    campaign_data_list = ["OWL1UYKSNRYR", "8VN5DXLKJN8A"]  # List of campaign IDs
    for campaign_data in campaign_data_list:
        sql = "SELECT * FROM fk_pla WHERE DATE(date) BETWEEN %s AND %s AND `campaign_ID` = %s"
        cursor.execute(sql, (start_date, end_date, campaign_data))  
        results = cursor.fetchall()

        columns = [column[0] for column in cursor.description]
        data = []
        for row in results:
            row_data = {}
            for i in range(len(columns)):
                if isinstance(row[i], decimal.Decimal):
                    row_data[columns[i]] = float(row[i])
                elif isinstance(row[i], datetime):
                    row_data[columns[i]] = row[i].strftime('%Y-%m-%d %H:%M:%S')
                else:
                    row_data[columns[i]] = row[i]
                row_data['category'] = "PLA"
            data.append(row_data)

        # print("Campaign ID:", campaign_data)
        # print(data)
        collect_data += data
    return collect_data



# result = flipKeywords()
# for i in result:
#     print(i, "\n")
