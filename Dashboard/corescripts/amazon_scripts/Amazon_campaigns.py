import mysql.connector
import json
from decimal import Decimal
from datetime import datetime
import time
import requests

class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return float(obj)
        elif isinstance(obj, datetime):
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

            start_date = datetime.strptime('2024-02-29', '%Y-%m-%d')
            end_date = datetime.strptime('2024-02-29', '%Y-%m-%d')
            query = f"""
        SELECT
            campaign_id,
            campaign_name,
            SUM(impressions) AS impressions,
            SUM(clicks) AS clicks,
            SUM(spends) AS spends,
            SUM(sales) AS sales,
            SUM(orders) AS orders,
            SUM(sales) / NULLIF(SUM(clicks), 0) AS roas,
            SUM(clicks) / NULLIF(SUM(impressions), 0) AS cvr,
            SUM(spends) / NULLIF(SUM(clicks), 0) AS cpc,
            SUM(sales) / NULLIF(SUM(orders), 0) AS aov,
            SUM(ctr) AS ctr
        FROM campaign_data3
        WHERE `date` BETWEEN '{start_date}' AND '{end_date}'
        GROUP BY campaign_id, campaign_name
    """

            start_time = time.time()

            cursor.execute(query)
            rows = cursor.fetchall()

            end_time = time.time()

            fetched_data = []
            for row in rows:
                roas = float(row['sales']) / float(row['clicks']) if float(row['clicks']) != 0 else None
                cvr = row['clicks'] / row['impressions'] if row['impressions'] != 0 else None
                cpc = float(row['spends']) / float(row['clicks']) if float(row['clicks']) != 0 else None
                aov = float(row['sales']) / float(row['orders']) if float(row['orders']) != 0 else None

                
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
                    'aov': aov,
                    'ctr': str(row['ctr'])  
                }
                fetched_data.append(row_data)

            REFRESH_TOKEN = "Atzr|IwEBII3rfEevtipGGJsx_StgDRsBE-4lTdkPbkw0OYDRfkkWqD7Nu5Ujz5js1BZscsWyxW1OGPo9LxTtVBQM-V-uFHeo27utIdl1-je6E74K8Q12MsFAXEZBqSkyPMsUIemF2BKR3FMw7rRJPh15MdolcpipySgmKyiUb3c4qVqbUY6tXmT5mM2bAHKjxU8gV1CvpxwUDCDhWdeVxScRhz5-vJehqm7-2jN-T4s4yi-wWxGs6Q04UvB4Pa1Mk8vNelZQHiRdZfz0IZTLuWza2sQXeivgCHUam4ARgMmX4DQuWZf6HxePQzww2giQ472Nr-dmrAcsiMeUxYqm1Z9GQn7Pdm7il_67mn95wOpVF082X9E6UUfKxWy7CJ8dvTN-B8Eo0T4o-UEeWmjgyzpuYTFSGy7hCqtxM0YnanmK9LWwPxyyL_5xqcBhi96RRS2EtqQEbCNieebrO3nLgd7oILRKwdnAHOTzmPzA8nUnpNd0wJUAmQ"
            CLIENT_ID = "amzn1.application-oa2-client.542a565d61904101afc00555ce336340"
            CLIENT_SECRET = "amzn1.oa2-cs.v1.7a0a5a1d89a149722fe8d033b3115d661c25076a70817f1ef0ce9886a8a20681"
            
            access_token = get_access_token(REFRESH_TOKEN, CLIENT_ID, CLIENT_SECRET)
            profile_id = get_profile_id(access_token, CLIENT_ID)
            
            sd_campaigns = get_sponsored_display_campaigns(access_token, CLIENT_ID, profile_id)
            sp_campaigns = get_sponsored_product_campaigns(access_token, CLIENT_ID, profile_id)
            sb_campaigns = get_sponsored_brands_campaigns(access_token, CLIENT_ID, profile_id)
            
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
            
            # Create a dictionary to store metrics for each campaign
            campaign_metrics = {}
            
            # Populate the dictionary with metrics from the fetched rows
            for row in fetched_data:
                campaign_id = row['campaign_id']
                campaign_name = row['campaign_name']
                campaign_metrics[(campaign_id, campaign_name)] = {
                    'impressions': int(row['impressions']),
                    'clicks': int(row['clicks']),
                    'spends': float(row['spends']),
                    'sales': float(row['sales']),
                    'orders': int(row['orders']),
                    'roas': float(row['roas']) if row['roas'] is not None else 0,
                    'cvr': float(row['cvr']) if row['cvr'] is not None else 0,
                    'cpc': float(row['cpc']) if row['cpc'] is not None else 0,
                    'aov': float(row['aov']) if row['aov'] is not None else 0,
                    'ctr': float(row['ctr']) if row['ctr'] is not None and row['ctr'] != 'None' else 0
                }
            
            # Iterate over campaigns fetched from API calls
            for campaign_data in all_campaigns:
                if campaign_data['campaign_type'] == 'SD' or campaign_data['campaign_type'] == 'SB':
                    campaign_data['cpstatus'] = campaign_data['cpstatus'].upper()
                campaign_id = campaign_data['campaign_id']
                campaign_name = campaign_data['campaign_name']
                campaign_key = (campaign_id, campaign_name)

                # Check if campaign exists in the dictionary
                if campaign_key in campaign_metrics:
                    # Update metrics with values from the dictionary
                    campaign_data.update(campaign_metrics[campaign_key])
                else:
                    # If campaign does not exist, set all metrics to 0
                    campaign_data.update({
                        'impressions': 0,
                        'clicks': 0,
                        'spends': 0,
                        'sales': 0,
                        'orders': 0,
                        'roas': 0,
                        'cvr': 0,
                        'cpc': 0,
                        'aov': 0,
                        'ctr': 0.0
                    })
            
            # Merge campaigns with the same ID and name
            merged_campaigns = {}
            for campaign_data in all_campaigns:
                campaign_key = (campaign_data['campaign_id'], campaign_data['campaign_name'])
                if campaign_key in merged_campaigns:
                    # Add metrics to existing campaign
                    merged_campaigns[campaign_key]['impressions'] += campaign_data['impressions']
                    merged_campaigns[campaign_key]['clicks'] += campaign_data['clicks']
                    merged_campaigns[campaign_key]['spends'] += campaign_data['spends']
                    merged_campaigns[campaign_key]['sales'] += campaign_data['sales']
                    merged_campaigns[campaign_key]['orders'] += campaign_data['orders']
                    merged_campaigns[campaign_key]['roas'] += campaign_data['roas']
                    merged_campaigns[campaign_key]['cvr'] += campaign_data['cvr']
                    merged_campaigns[campaign_key]['cpc'] += campaign_data['cpc']
                    merged_campaigns[campaign_key]['aov'] += campaign_data['aov']
                    merged_campaigns[campaign_key]['ctr'] += campaign_data['ctr']
                    
                else:
                    # Initialize merged campaign with metrics
                    merged_campaigns[campaign_key] = campaign_data
            
            # Convert merged campaigns back to list
            merged_campaigns_list = list(merged_campaigns.values())
            
            print(len(merged_campaigns_list))
            for i in range(len(merged_campaigns_list)):
                merged_campaigns_list[i]['views'] = merged_campaigns_list[i].pop("impressions")
                merged_campaigns_list[i]['total_converted_revenue'] = merged_campaigns_list[i].pop("sales")
                merged_campaigns_list[i]['total_converted_units'] = merged_campaigns_list[i].pop("orders")
                merged_campaigns_list[i]['cpc'] = merged_campaigns_list[i].pop("cpc")
                merged_campaigns_list[i]['CTR'] = merged_campaigns_list[i].pop("ctr")
                merged_campaigns_list[i]['aov'] = merged_campaigns_list[i].pop("aov")
                print(merged_campaigns_list[i])
                merged_campaigns_list[i]['cpstatus'] = merged_campaigns_list[i].pop("cpstatus")
                merged_campaigns_list[i]['campaign_type'] = merged_campaigns_list[i].pop("campaign_type")
                print(merged_campaigns_list[i])

            return merged_campaigns_list

            elapsed_time = end_time - start_time
            print("Time taken to fetch data:", elapsed_time, "seconds")

    except mysql.connector.Error as error:
        print("Error while connecting to MySQL", error)

    finally:
        
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")




print(amzcampagin())
