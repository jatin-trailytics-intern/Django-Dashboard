import pymysql
from decimal import Decimal


def amzPortfolio(start_date, end_date):
    DB_CONFIG = {
        'host': 'tr-wp-database.cfqdq6ohjn0p.us-east-1.rds.amazonaws.com',
        'user': 'aatif',
        'password': 'Trailytics@789',
        'db': 'amazon_ads_api',
        'port': 3306,  
        'connect_timeout': 1000,
        'autocommit': True
    }

    connection = pymysql.connect(**DB_CONFIG)
    cursor = connection.cursor(pymysql.cursors.DictCursor)

    start_date = '2024-02-10'
    end_date = '2024-02-20'
    sql = f"""
    SELECT Portfolio, 
        SUM(Impressions) AS TotalImpressions,
        SUM(Clicks) AS TotalClicks,
        SUM(Spend_INR) AS TotalSpend_INR,
        SUM(Orders) AS TotalOrders,
        SUM(Sales_INR) AS TotalSales_INR,
        SUM(CTR) AS TotalCTR
    FROM portfolio_data
    WHERE date BETWEEN '{start_date}' AND '{end_date}'
    GROUP BY Portfolio;
    """

    cursor.execute(sql)
    rows = cursor.fetchall()

    cursor.close()
    connection.close()

    data_list = []

    for row in rows:
        
        for key, value in row.items():
            if isinstance(value, Decimal):
                row[key] = float(value)  
        
        data_list.append(row)

    print(data_list)
    print(len(data_list))

    return data_list