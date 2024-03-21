import mysql.connector
import requests
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

REFRESH_TOKEN = "Atzr|IwEBII3rfEevtipGGJsx_StgDRsBE-4lTdkPbkw0OYDRfkkWqD7Nu5Ujz5js1BZscsWyxW1OGPo9LxTtVBQM-V-uFHeo27utIdl1-je6E74K8Q12MsFAXEZBqSkyPMsUIemF2BKR3FMw7rRJPh15MdolcpipySgmKyiUb3c4qVqbUY6tXmT5mM2bAHKjxU8gV1CvpxwUDCDhWdeVxScRhz5-vJehqm7-2jN-T4s4yi-wWxGs6Q04UvB4Pa1Mk8vNelZQHiRdZfz0IZTLuWza2sQXeivgCHUam4ARgMmX4DQuWZf6HxePQzww2giQ472Nr-dmrAcsiMeUxYqm1Z9GQn7Pdm7il_67mn95wOpVF082X9E6UUfKxWy7CJ8dvTN-B8Eo0T4o-UEeWmjgyzpuYTFSGy7hCqtxM0YnanmK9LWwPxyyL_5xqcBhi96RRS2EtqQEbCNieebrO3nLgd7oILRKwdnAHOTzmPzA8nUnpNd0wJUAmQ"
CLIENT_ID = "amzn1.application-oa2-client.542a565d61904101afc00555ce336340"
CLIENT_SECRET = "amzn1.oa2-cs.v1.7a0a5a1d89a149722fe8d033b3115d661c25076a70817f1ef0ce9886a8a20681"

def get_access_token():
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
    }
    
    data = {
        'grant_type': 'refresh_token',
        'client_id': CLIENT_ID,
        'refresh_token': REFRESH_TOKEN,
        'client_secret': CLIENT_SECRET
    }
    
    response = requests.post('https://api.amazon.com/auth/o2/token', headers=headers, data=data)
    r_json = response.json()
    return r_json.get("access_token")

def list_sponsored_brands_ad_groups(access_token, client_id, profile_id):
    headers = {
        'Amazon-Advertising-API-ClientId': client_id,
        'Amazon-Advertising-API-Scope': profile_id,
        'Authorization': access_token,
        'Accept': 'application/vnd.sbadgroupresource.v4+json',
        'Content-Type': 'application/vnd.sbadgroupresource.v4+json',
    }
    response = requests.post('https://advertising-api-eu.amazon.com/sb/v4/adGroups/list', headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch Sponsored Brands ad groups:", response.status_code, response.text)
        return None

def list_sponsored_products_ad_groups(access_token, client_id, profile_id):
    headers = {
        'Amazon-Advertising-API-ClientId': client_id,
        'Amazon-Advertising-API-Scope': profile_id,
        'Authorization':  access_token,
        'Accept': 'application/vnd.spAdGroup.v3+json',
        'Content-Type': 'application/vnd.spAdGroup.v3+json',
    }
    response = requests.post('https://advertising-api-eu.amazon.com/sp/adGroups/list', headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch Sponsored Products ad groups:", response.status_code, response.text)
        return None

def list_sponsored_display_ad_groups(access_token, client_id, profile_id):
    headers = {
        'Amazon-Advertising-API-ClientId': client_id,
        'Amazon-Advertising-API-Scope': profile_id,
        'Authorization': access_token,
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = requests.get('https://advertising-api-eu.amazon.com/v2/sd/adGroups', headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch Sponsored Display ad groups:", response.status_code, response.text)
        return None

def extract_data(ad_groups, campaign_type):
    extracted_data = []
    for ad_group in ad_groups:
        data = {
            'name': ad_group.get('name', ''),
            'adGroupId': ad_group.get('adGroupId', ''),
            'campaignId': ad_group.get('campaignId', ''),
            'state': ad_group.get('state', ''),  
            'campaign_type': campaign_type
        }
        extracted_data.append(data)
    return extracted_data


def merge_data(fetched_data, api_data):
    merged_data = []
    
    
    fetched_ad_groups = {(entry['ad_group_id'], entry['ad_group_name']) for entry in fetched_data}
    
    
    for api_entry in api_data:
        if (api_entry['adGroupId'], api_entry['name']) in fetched_ad_groups:
           
            for db_entry in fetched_data:
                if (db_entry['ad_group_id'], db_entry['ad_group_name']) == (api_entry['adGroupId'], api_entry['name']):
                   
                    merged_entry = {
                        'ad_group_id': api_entry['adGroupId'],
                        'ad_group_name': api_entry['name'],
                        'campaign_id': db_entry['campaign_id'],
                        'campaign_name': db_entry['campaign_name'],
                        'campaign_type': api_entry['campaign_type'],
                        'state': api_entry['state'],
                        'impressions': db_entry['impressions'],
                        # 'clicks': db_entry['clicks'],
                        'spends': db_entry['spends'],
                        'sales': db_entry['sales'],
                        # 'orders': db_entry['orders'],
                        'roas': db_entry['roas'],
                        'ctr': db_entry['ctr']
                    }
                    merged_data.append(merged_entry)
                    break
        else:
           
            merged_entry = {
                'ad_group_id': api_entry['adGroupId'],
                'ad_group_name': api_entry['name'],
                'campaign_id': api_entry['campaignId'],  
                'campaign_name': '',  
                'campaign_type': api_entry['campaign_type'],
                'state': api_entry['state'],
                'impressions': 0,
                # 'clicks': 0,
                'spends': 0,
                'sales': 0,
                # 'orders': 0,
                'roas': 0.0,
                'ctr': 0.0
            }
            merged_data.append(merged_entry)
            merged_data.sort(key=lambda x: ( int(x['impressions']), float(x['spends']), float(x['sales']),  float(x['roas']), float(x['ctr'])), reverse=True)


    return merged_data


    # # Append remaining entries from fetched_data if any
    # for db_entry in fetched_data:
    #     if (db_entry['ad_group_id'], db_entry['ad_group_name']) not in [(entry['ad_group_id'], entry['ad_group_name']) for entry in merged_data]:
    #         merged_data.append(db_entry)

    # return merged_data



# def main():
def adsGroupData():
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
            end_date = datetime.strptime('2024-03-09', '%Y-%m-%d')
            query = f"""
SELECT
    ad_group_id,
    ad_group_name,
    campaign_id,
    campaign_name,
    campaign_type,
    SUM(impressions) AS total_impressions,
    SUM(clicks) AS total_clicks,
    SUM(spends) AS total_spends,
    SUM(sales) AS total_sales,
    SUM(orders) AS total_orders,
    SUM(sales) / NULLIF(SUM(clicks), 0) AS roas,
    SUM(clicks) / NULLIF(SUM(impressions), 0) AS ctr
FROM adgroup_data 
WHERE `adgroup_date` BETWEEN '{start_date}' AND '{end_date}'
GROUP BY ad_group_id, ad_group_name, campaign_id
"""



            cursor.execute(query)
            rows = cursor.fetchall()


            fetched_data = []
            for row in rows:
                clicks = row.get('total_clicks')
                impressions = row.get('total_impressions')

                # Handle None or 0 values for clicks and impressions
                if clicks is not None and impressions is not None and clicks != 0:
                    roas = Decimal(row['total_sales']) / row['total_clicks']
                    ctr = (row['total_clicks'] / row['total_impressions']) * 100

                else:
                    roas = 0.0
                    ctr = 0.0

                row_data = {
                    'campaign_id': str(row['campaign_id']),
                    'campaign_name': str(row['campaign_name']),
                    'ad_group_id': str(row['ad_group_id']),
                    'ad_group_name': str(row['ad_group_name']),
                    'impressions': str(row['total_impressions']),
                    'clicks': str(clicks),
                    'spends': str(row['total_spends']),
                    'sales': str(row['total_sales']),
                    'orders': str(row['total_orders']),
                    'campaign_type': str(row['campaign_type']),
                    'roas': float(roas),  # Convert roas to float
                    'ctr': float(ctr),
                }
                fetched_data.append(row_data)

            # print(fetched_data)

            # Close cursor after fetching data from database
            cursor.close()

            # Call API to get ad group data
            access_token = get_access_token()
            profile_id = "566062612927990"  # Replace with your actual profile ID

            merged_ad_groups = []  # Initialize an empty list to store merged ad groups

            # Fetch ad groups for Sponsored Brands
            sb_ad_groups = list_sponsored_brands_ad_groups(access_token, CLIENT_ID, profile_id)
            if sb_ad_groups:
                sb_data = extract_data(sb_ad_groups.get('adGroups', []), 'SB')
                merged_ad_groups.extend(sb_data)  # Append to the merged list

            # Fetch ad groups for Sponsored Products
            sp_ad_groups = list_sponsored_products_ad_groups(access_token, CLIENT_ID, profile_id)
            if sp_ad_groups:
                sp_data = extract_data(sp_ad_groups.get('adGroups', []), 'SP')
                merged_ad_groups.extend(sp_data)  # Append to the merged list

            # Fetch ad groups for Sponsored Display
            sd_ad_groups = list_sponsored_display_ad_groups(access_token, CLIENT_ID, profile_id)
            if sd_ad_groups:
                sd_data = extract_data(sd_ad_groups, 'SD')
                merged_ad_groups.extend(sd_data)  # Append to the merged list

            # Merge fetched data from database and API
            merged_data = merge_data(fetched_data, merged_ad_groups)
            
            
        
            
            print("Merged ad groups:")
            return merged_data
           

    except mysql.connector.Error as error:
        print("Error while connecting to MySQL", error)
    except Exception as e:
        print("Error:", e)
    finally:
        # Closing the database connection
        if 'connection' in locals() and connection.is_connected():
            connection.close()
            print("MySQL connection is closed")


# print(adsGroupData())
