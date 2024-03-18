import mysql.connector
import json
from decimal import Decimal
from datetime import date, datetime
import time
import requests

class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return float(obj)
        elif isinstance(obj, (date, datetime)):
            return obj.isoformat()
        else:
            return super().default(obj)

def get_access_token(refresh_token, client_id, client_secret):
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
    }
    data = {
      'grant_type': 'refresh_token',
      'client_id': client_id,
      'refresh_token': refresh_token,
      'client_secret': client_secret
    }
    response = requests.post('https://api.amazon.com/auth/o2/token', headers=headers, data=data)
    r_json = response.json()
    return r_json["access_token"]

def extract_value(data_list, key):
    for item in data_list:
        if key in item:
            return item[key]
    return None

def get_profile_id(access_token, client_id):
    headers = {
        'Amazon-Advertising-API-ClientId': client_id,
        'Authorization': access_token,
    }
    response = requests.get("https://advertising-api-eu.amazon.com/v2/profiles", headers=headers)
    output_data = json.loads(response.text)
    profile_id = extract_value(output_data, 'profileId')
    return str(profile_id)

def get_sponsored_display_campaigns(access_token, client_id, profile_id):
    headers = {
        'Amazon-Advertising-API-ClientId': client_id,
        'Amazon-Advertising-API-Scope': profile_id,
        'Authorization': access_token,
    }
    response = requests.get('https://advertising-api-eu.amazon.com/sd/campaigns', headers=headers)
    return json.loads(response.text)

def get_sponsored_product_campaigns(access_token, client_id, profile_id):
    headers = {
        'Amazon-Advertising-API-ClientId': client_id,
        'Amazon-Advertising-API-Scope': profile_id,
        'Authorization': access_token,
        'Accept': 'application/vnd.spCampaign.v3+json',
        'Content-Type': 'application/vnd.spCampaign.v3+json',
    }
    response = requests.post('https://advertising-api-eu.amazon.com/sp/campaigns/list', headers=headers)
    return json.loads(response.text)

def get_sponsored_brands_campaigns(access_token, client_id, profile_id):
    headers = {
        'Amazon-Advertising-API-ClientId': client_id,
        'Amazon-Advertising-API-Scope': profile_id,
        'Authorization': access_token,
    }
    response = requests.get('https://advertising-api-eu.amazon.com/sb/campaigns', headers=headers)
    return json.loads(response.text)











def amzcampagin():
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

            # Define the date range for the query
            start_date = '2024-01-20'
            end_date = '2024-03-20'

            query = f"SELECT * FROM campaign_data3 WHERE `date` BETWEEN '{start_date}' AND '{end_date}'"

            start_time = time.time()

            cursor.execute(query)
            rows = cursor.fetchall()

            end_time = time.time()

            fetched_data = []
            for row in rows:
                # Calculate derived metrics
                roas = float(row['sales']) / row['clicks'] if row['clicks'] != 0 else None
                cvr = row['clicks'] / row['impressions'] if row['impressions'] != 0 else None
                cpc = float(row['spends']) / row['clicks'] if row['clicks'] != 0 else None
                aov = float(row['sales']) / row['orders'] if row['orders'] != 0 else None
                
                # Format data into dictionary
                row_data = {
                    'campaign_id': str(row['campaign_id']),
                    'campaign_name': str(row['campaign_name']),
                    'impressions': str(row['impressions']),
                    'clicks': str(row['clicks']),
                    'spends': str(row['spends']), 
                    'sales': str(row['sales']),
                    'orders': str(row['orders']),
                    'roas': roas,
                    'cvr': cvr,
                    'cpc': cpc,
                    'aov': aov
                }
                fetched_data.append(row_data)

            # Get Amazon Ads API data
            REFRESH_TOKEN = "Atzr|IwEBII3rfEevtipGGJsx_StgDRsBE-4lTdkPbkw0OYDRfkkWqD7Nu5Ujz5js1BZscsWyxW1OGPo9LxTtVBQM-V-uFHeo27utIdl1-je6E74K8Q12MsFAXEZBqSkyPMsUIemF2BKR3FMw7rRJPh15MdolcpipySgmKyiUb3c4qVqbUY6tXmT5mM2bAHKjxU8gV1CvpxwUDCDhWdeVxScRhz5-vJehqm7-2jN-T4s4yi-wWxGs6Q04UvB4Pa1Mk8vNelZQHiRdZfz0IZTLuWza2sQXeivgCHUam4ARgMmX4DQuWZf6HxePQzww2giQ472Nr-dmrAcsiMeUxYqm1Z9GQn7Pdm7il_67mn95wOpVF082X9E6UUfKxWy7CJ8dvTN-B8Eo0T4o-UEeWmjgyzpuYTFSGy7hCqtxM0YnanmK9LWwPxyyL_5xqcBhi96RRS2EtqQEbCNieebrO3nLgd7oILRKwdnAHOTzmPzA8nUnpNd0wJUAmQ"
            CLIENT_ID = "amzn1.application-oa2-client.542a565d61904101afc00555ce336340"
            CLIENT_SECRET = "amzn1.oa2-cs.v1.7a0a5a1d89a149722fe8d033b3115d661c25076a70817f1ef0ce9886a8a20681"
            
            access_token = get_access_token(REFRESH_TOKEN, CLIENT_ID, CLIENT_SECRET)
            profile_id = get_profile_id(access_token, CLIENT_ID)
            
            # Get all campaign types
            sd_campaigns = get_sponsored_display_campaigns(access_token, CLIENT_ID, profile_id)
            sp_campaigns = get_sponsored_product_campaigns(access_token, CLIENT_ID, profile_id)
            sb_campaigns = get_sponsored_brands_campaigns(access_token, CLIENT_ID, profile_id)
            
            # Combine all campaigns into a single list with specific keys
            all_campaigns = []
            if sd_campaigns:
                all_campaigns.extend([{
                    "campaign_id": campaign.get("campaignId"),
                    "campaign_name": campaign.get("name"),
                    "cpstatus": campaign.get("state"),
                    "campaign_budget": campaign.get("budget"),
                    "campaign_type": "SD"
                } for campaign in sd_campaigns])
            if 'campaigns' in sp_campaigns:
                all_campaigns.extend([{
                    "campaign_id": campaign.get("campaignId"),
                    "campaign_name": campaign.get("name"),
                    "cpstatus": campaign.get("state"),
                    "campaign_budget": campaign.get("budget", {}).get("budget"),
                    "campaign_type": "SP"
                } for campaign in sp_campaigns['campaigns']])
            if isinstance(sb_campaigns, list):
                all_campaigns.extend([{
                    "campaign_id": campaign.get("campaignId"),
                    "campaign_name": campaign.get("name"),
                    "cpstatus": campaign.get("state"),
                    "campaign_budget": campaign.get("budget"),
                    "campaign_type": "SB"
                } for campaign in sb_campaigns])
            
            # Merge campaign data from API with fetched data from MySQL database based on campaign_id and campaign name
            for campaign_data in all_campaigns:
                # Flag to check if a match is found
                found_match = False
                for row in fetched_data:
                    if campaign_data['campaign_type'] == 'SD' and campaign_data['campaign_name'] == row['campaign_name'] and campaign_data['campaign_id'] == row['campaign_id']:
                        # Merge data from API and MySQL
                        campaign_data.update({
                            'impressions': row['impressions'],
                            'clicks': row['clicks'],
                            'spends': row['spends'],
                            'sales': row['sales'],
                            'orders': row['orders'],
                            'roas': row['roas'],
                            'cvr': row['cvr'],
                            'cpc': row['cpc'],
                            'aov': row['aov']
                        })
                        found_match = True
                        break
                    elif campaign_data['campaign_type'] == 'SP' and campaign_data['campaign_name'] == row['campaign_name'] and campaign_data['campaign_id'] == row['campaign_id']:
                        # Merge data from API and MySQL
                        campaign_data.update({
                            'impressions': row['impressions'],
                            'clicks': row['clicks'],
                            'spends': row['spends'],
                            'sales': row['sales'],
                            'orders': row['orders'],
                            'roas': row['roas'],
                            'cvr': row['cvr'],
                            'cpc': row['cpc'],
                            'aov': row['aov']
                        })
                        found_match = True
                        break
                    elif campaign_data['campaign_type'] == 'SB' and campaign_data['campaign_name'] == row['campaign_name'] and campaign_data['campaign_id'] == row['campaign_id']:
                        # Merge data from API and MySQL
                        campaign_data.update({
                            'impressions': row['impressions'],
                            'clicks': row['clicks'],
                            'spends': row['spends'],
                            'sales': row['sales'],
                            'orders': row['orders'],
                            'roas': row['roas'],
                            'cvr': row['cvr'],
                            'cpc': row['cpc'],
                            'aov': row['aov']
                        })
                        found_match = True
                        break
                
                # If no match is found, set all metrics to 0
                if not found_match:
                    campaign_data.update({
                        'impressions': 0,
                        'clicks': 0,
                        'spends': 0,
                        'sales': 0,
                        'orders': 0,
                        'roas': 0,
                        'cvr': 0,
                        'cpc': 0,
                        'aov': 0
                    })
            
            # Print the merged campaign data
            # print(all_campaigns)
                # Convert metrics to integers or floats where appropriate
            for campaign_data in all_campaigns:
                campaign_data['impressions'] = int(campaign_data['impressions'])
                campaign_data['clicks'] = int(campaign_data['clicks'])
                campaign_data['spends'] = float(campaign_data['spends'])
                campaign_data['sales'] = float(campaign_data['sales'])
                campaign_data['orders'] = int(campaign_data['orders'])
                campaign_data['roas'] = float(campaign_data['roas']) if campaign_data['roas'] is not None else 0.0  # Set to 0.0 if 'roas' is None
                campaign_data['cvr'] = float(campaign_data['cvr']) if campaign_data['cvr'] is not None else 0.0
                campaign_data['cpc'] = float(campaign_data['cpc']) if campaign_data['cpc'] is not None else 0.0
                campaign_data['aov'] = float(campaign_data['aov']) if campaign_data['aov'] is not None else 0.0  # Set to 0.0 if 'aov' is None

    # Print the merged campaign data with campaigns having data in metrics first
            sorted_campaigns = sorted(all_campaigns, key=lambda x: (
                x['impressions'] > 0 or
                x['clicks'] > 0 or
                x['spends'] > 0 or
                x['sales'] > 0 or
                x['orders'] > 0 or
                x['roas'] > 0 or
                x['cvr'] > 0 or
                x['cpc'] > 0 or
                x['aov'] > 0
                ), reverse=True)
            # print(sorted_campaigns[0])
            for i in range(len(sorted_campaigns)):
                sorted_campaigns[i]['views'] = sorted_campaigns[i].pop("impressions")
                sorted_campaigns[i]['total_converted_revenue'] = sorted_campaigns[i].pop("sales")
                sorted_campaigns[i]['total_converted_units'] = sorted_campaigns[i].pop("orders")
                sorted_campaigns[i]['cvr'] = sorted_campaigns[i].pop("cvr")
                sorted_campaigns[i]['cpc'] = sorted_campaigns[i].pop("cpc")
                # sorted_campaigns[i]['CTR'] = sorted_campaigns[i].pop("ctr")
                sorted_campaigns[i]['aov'] = sorted_campaigns[i].pop("aov")
                


            return sorted_campaigns

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



# print(amzcampagin()[0], len(amzcampagin()))