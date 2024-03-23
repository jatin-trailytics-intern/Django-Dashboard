import mysql.connector
import json
import requests
from decimal import Decimal
from datetime import date, datetime

class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return float(obj)
        elif isinstance(obj, (date, datetime)):
            return obj.isoformat()
        else:
            return super().default(obj)

def get_access_token():
    REFRESH_TOKEN = "Atzr|IwEBII3rfEevtipGGJsx_StgDRsBE-4lTdkPbkw0OYDRfkkWqD7Nu5Ujz5js1BZscsWyxW1OGPo9LxTtVBQM-V-uFHeo27utIdl1-je6E74K8Q12MsFAXEZBqSkyPMsUIemF2BKR3FMw7rRJPh15MdolcpipySgmKyiUb3c4qVqbUY6tXmT5mM2bAHKjxU8gV1CvpxwUDCDhWdeVxScRhz5-vJehqm7-2jN-T4s4yi-wWxGs6Q04UvB4Pa1Mk8vNelZQHiRdZfz0IZTLuWza2sQXeivgCHUam4ARgMmX4DQuWZf6HxePQzww2giQ472Nr-dmrAcsiMeUxYqm1Z9GQn7Pdm7il_67mn95wOpVF082X9E6UUfKxWy7CJ8dvTN-B8Eo0T4o-UEeWmjgyzpuYTFSGy7hCqtxM0YnanmK9LWwPxyyL_5xqcBhi96RRS2EtqQEbCNieebrO3nLgd7oILRKwdnAHOTzmPzA8nUnpNd0wJUAmQ"
    CLIENT_ID = "amzn1.application-oa2-client.542a565d61904101afc00555ce336340"
    CLIENT_SECRET = "amzn1.oa2-cs.v1.7a0a5a1d89a149722fe8d033b3115d661c25076a70817f1ef0ce9886a8a20681"

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
REFRESH_TOKEN = "Atzr|IwEBII3rfEevtipGGJsx_StgDRsBE-4lTdkPbkw0OYDRfkkWqD7Nu5Ujz5js1BZscsWyxW1OGPo9LxTtVBQM-V-uFHeo27utIdl1-je6E74K8Q12MsFAXEZBqSkyPMsUIemF2BKR3FMw7rRJPh15MdolcpipySgmKyiUb3c4qVqbUY6tXmT5mM2bAHKjxU8gV1CvpxwUDCDhWdeVxScRhz5-vJehqm7-2jN-T4s4yi-wWxGs6Q04UvB4Pa1Mk8vNelZQHiRdZfz0IZTLuWza2sQXeivgCHUam4ARgMmX4DQuWZf6HxePQzww2giQ472Nr-dmrAcsiMeUxYqm1Z9GQn7Pdm7il_67mn95wOpVF082X9E6UUfKxWy7CJ8dvTN-B8Eo0T4o-UEeWmjgyzpuYTFSGy7hCqtxM0YnanmK9LWwPxyyL_5xqcBhi96RRS2EtqQEbCNieebrO3nLgd7oILRKwdnAHOTzmPzA8nUnpNd0wJUAmQ"
CLIENT_ID = "amzn1.application-oa2-client.542a565d61904101afc00555ce336340"
CLIENT_SECRET = "amzn1.oa2-cs.v1.7a0a5a1d89a149722fe8d033b3115d661c25076a70817f1ef0ce9886a8a20681"

# def list_sponsored_brands_targets(profile_id, access_token):
#     headers = {
#         'Amazon-Advertising-API-ClientId': CLIENT_ID,
#         'Authorization': access_token,
#         'Amazon-Advertising-API-Scope': profile_id,
#     }
#     response = requests.get('https://advertising-api-eu.amazon.com/sb/keywords', headers=headers)
#     if response.status_code == 200:
#         return response.json()
#     else:
#         print("Failed to fetch Sponsored Brands targets:", response.status_code, response.text)
#         return None

# def list_sponsored_products_keywords(profile_id, access_token):
#     headers = {
#         'Amazon-Advertising-API-ClientId': CLIENT_ID,
#         'Authorization': access_token,
#         'Content-Type': 'application/vnd.spKeyword.v3+json',
#         'Amazon-Advertising-API-Scope': profile_id,
#         'Accept': 'application/vnd.spKeyword.v3+json',
#     }
#     response = requests.post('https://advertising-api-eu.amazon.com/sp/keywords/list', headers=headers)
#     if response.status_code == 200:
#         keywords_response = response.json()
#         keywords = keywords_response.get('keywords', [])
#         return keywords
#     else:
#         print("Failed to fetch Sponsored Products keywords:", response.status_code, response.text)
#         return None

# def list_sponsored_display_targets(profile_id, access_token):
#     headers = {
#         'Amazon-Advertising-API-ClientId': CLIENT_ID,
#         'Authorization': access_token,
#         'Content-Type': 'application/json',
#         'Amazon-Advertising-API-Scope': profile_id,
#         'Accept': 'application/json',
#     }
#     response = requests.get('https://advertising-api-eu.amazon.com/sd/targets', headers=headers)
#     if response.status_code == 200:
#         return response.json()
#     else:
#         print("Failed to fetch Sponsored Display targets:", response.status_code, response.text)
#         return None
def list_sponsored_brands_targets(profile_id):
    access_token = get_access_token()
    headers = {
        'Amazon-Advertising-API-ClientId': CLIENT_ID,
        'Authorization': access_token,
        'Amazon-Advertising-API-Scope': profile_id,
    }
    response = requests.get('https://advertising-api-eu.amazon.com/sb/keywords', headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch Sponsored Brands targets:", response.status_code, response.text)
        return None

def list_sponsored_products_keywords(profile_id):
    access_token = get_access_token()
    headers = {
        'Amazon-Advertising-API-ClientId': CLIENT_ID,
        'Authorization': access_token,
        'Content-Type': 'application/vnd.spKeyword.v3+json',
        'Amazon-Advertising-API-Scope': profile_id,
        'Accept': 'application/vnd.spKeyword.v3+json',
    }
    response = requests.post('https://advertising-api-eu.amazon.com/sp/keywords/list', headers=headers)
    if response.status_code == 200:
        keywords_response = response.json()
        keywords = keywords_response.get('keywords', [])
        return keywords
    else:
        print("Failed to fetch Sponsored Products keywords:", response.status_code, response.text)
        return None


def list_sponsored_display_targets(profile_id):
    access_token = get_access_token()
    headers = {
        'Amazon-Advertising-API-ClientId': CLIENT_ID,
        'Authorization': access_token,
        'Content-Type': 'application/json',
        'Amazon-Advertising-API-Scope': profile_id,
        'Accept': 'application/json',
    }
    response = requests.get('https://advertising-api-eu.amazon.com/sd/targets', headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch Sponsored Display targets:", response.status_code, response.text)
        return None


    # Replace with your actual profile ID
    
    
    # print(final_list)
    
def amz_pload():
    profile_id = "566062612927990"  
    
    access_token = get_access_token()

    final_sb_targets = []
    final_sp_keywords = []
    final_sd_targets = []

    # Fetch targets for Sponsored Brands
    sb_targets = list_sponsored_brands_targets(profile_id)
    if sb_targets:
        for target in sb_targets:
            keyword_info = {
                "keyword_name": target.get("keywordText"),
                "keyword_id": target.get("keywordId"),
                "bid": target.get("bid"),
                "status": target.get("state")
            }
            final_sb_targets.append(keyword_info)

    # Fetch keywords for Sponsored Products
    final_sp_keywords = []

    # Fetch keywords for Sponsored Products
    sp_keywords = list_sponsored_products_keywords(profile_id)
    if sp_keywords:
        for keyword in sp_keywords:
            if isinstance(keyword, dict):
                keyword_info = {
                    "keyword_name": keyword.get("keywordText"),
                    "keyword_id": keyword.get("keywordId"),
                    "bid": keyword.get("bid"),
                    "status": keyword.get("state")
                }
                final_sp_keywords.append(keyword_info)
            else:
                print("Invalid format for keyword:", keyword)

    # Fetch targets for Sponsored Display
    sd_targets = list_sponsored_display_targets(profile_id)
    if sd_targets:
        for target in sd_targets:
            keyword_info = {
                "keyword_name": target.get("expression")[0].get("value") if target.get("expression") else None,
                "keyword_id": target.get("targetId"),
                "bid": target.get("bid"),
                "status": target.get("state")
            }
            final_sd_targets.append(keyword_info)
    
    final_list=final_sb_targets+final_sp_keywords+final_sd_targets

    fetched_data = fetch_data_from_database()

    merged_data = merge_data(final_list, fetched_data)
    print(len(merged_data))
    print(type(merged_data))
    return merged_data
    # print(json.dumps(merged_data, cls=CustomEncoder))

def fetch_data_from_database():
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
            end_date = '2024-03-19'

            query = f"""
                SELECT
                    keyword_name,
                    keyword_id,
                    keyword_bid,
                    keyword_status,
                    ad_group_id,
                    ad_group_name,
                    keyword_type,
                    match_type,
                    SUM(impressions) AS impressions,
                    SUM(clicks) AS clicks,
                    SUM(spends) AS spends,
                    SUM(sales) AS sales,
                    SUM(orders) AS orders,
                    campaign_id,
                    campaign_name,
                    campaign_type
                FROM
                    keyword_data
                WHERE
                    `DATE` BETWEEN '{start_date}' AND '{end_date}'
                GROUP BY
                    keyword_id, ad_group_id
            """

            cursor.execute(query)
            rows = cursor.fetchall()

            fetched_data = []

            for row in rows:
                roas = float(row['sales']) / float(row['clicks']) if row['clicks'] != 0 else None  # Convert to float

                row_data = {
                    'keyword_name': row['keyword_name'],
                    'keyword_id': str(row['keyword_id']),
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
                    'roas': roas,
                     
                }
                fetched_data.append(row_data)

    except mysql.connector.Error as error:
        print("Error while connecting to MySQL", error)
        fetched_data = []

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

    return fetched_data



def merge_data(final_list, fetched_data):
    merged_data = []

    # Create a dictionary to store fetched data with keyword_name as key
    fetched_data_dict = {}
    for entry in fetched_data:
        keyword_name = entry['keyword_name']
        if keyword_name not in fetched_data_dict:
            fetched_data_dict[keyword_name] = [entry]
        else:
            fetched_data_dict[keyword_name].append(entry)

    # Iterate through each entry in final_list
    for final_entry in final_list:
        final_keyword_name = str(final_entry['keyword_name'])  # Ensure final_keyword_name is a string

        # Check if keyword_name exists in fetched data dictionary
        if final_keyword_name in fetched_data_dict:
            fetched_entries = fetched_data_dict[final_keyword_name]

            # Iterate through fetched entries for the same keyword name
            for fetched_entry in fetched_entries:
                # Calculate ROAS and CTR
                roas = float(fetched_entry['sales']) / float(fetched_entry['spends']) if float(fetched_entry['spends']) != 0 else 0
                ctr = float(fetched_entry['clicks']) / float(fetched_entry['impressions']) if float(fetched_entry['impressions']) != 0 else 0

                # Format the metrics output to two decimal places
                roas = round(roas, 2)
                ctr = round(ctr, 2)
                sales = round(float(fetched_entry['sales']), 2)
                spends = round(float(fetched_entry['spends']), 2)
                orders = round(float(fetched_entry['orders']), 2)
                impressions = round(float(fetched_entry['impressions']), 2)
                clicks = round(float(fetched_entry['clicks']), 2)

                # Merge the data
                merged_entry = {
                    'keyword_name': final_keyword_name,
                    'keyword_bid': final_entry.get('bid'),  
                    'keyword_status': final_entry.get('status'),  
                    'ad_group_id': fetched_entry['ad_group_id'],
                    'ad_group_name': fetched_entry['ad_group_name'],
                    'keyword_type': fetched_entry['keyword_type'],
                    'match_type': fetched_entry['match_type'],
                    'impressions': impressions,
                    'clicks': clicks,
                    'spends': spends,
                    'sales': sales,
                    'campaign_id': fetched_entry['campaign_id'],
                    'campaign_name': fetched_entry['campaign_name'],
                    'orders': orders,
                    'campaign_type': fetched_entry['campaign_type'],
                    'roas': roas,
                    'ctr': ctr
                }
                merged_data.append(merged_entry)

    return merged_data















# if __name__ == "__main__":
#     print(amz_pload()[1])

