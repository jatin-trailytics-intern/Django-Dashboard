import requests
import json
from tabulate import tabulate

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

def print_sponsored_display_campaigns(sponsored_display_campaigns):
    if sponsored_display_campaigns:
        sponsored_display_campaigns_data = []

        for campaign in sponsored_display_campaigns:
            campaign_data_display = {
                "campaignId": campaign.get("campaignId"),
                "name": campaign.get("name"),
                "state": campaign.get("state"),
                "budget": campaign.get("budget"),  # Access budget directly
                # "budgetType": campaign.get("budgetType")  # Access budgetType directly if needed
            }
            sponsored_display_campaigns_data.append(campaign_data_display)

        print("Sponsored Display Campaigns Data:")
        print(tabulate(sponsored_display_campaigns_data, headers="keys", tablefmt="grid"))
    else:
        print("No sponsored display campaigns found.")

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

def print_sponsored_product_campaigns(sponsored_product_campaigns):
    if 'campaigns' in sponsored_product_campaigns:
        campaigns_list = sponsored_product_campaigns['campaigns']
        
        sponsored_product_campaigns_data = []
    
        for campaign in campaigns_list:
            campaign_data = {
                "campaignId": campaign.get("campaignId"),
                "name": campaign.get("name"),
                "state": campaign.get("state"),
                "budget": campaign.get("budget", {}).get("budget"),  # Access nested dictionary
                # "budgetType": campaign.get("budget", {}).get("budgetType")  # Access nested dictionary
            }
            sponsored_product_campaigns_data.append(campaign_data)
    
        print("Sponsored Product Campaigns Data:")
        print(tabulate(sponsored_product_campaigns_data, headers="keys", tablefmt="grid"))
    
    else:
        print("Error: 'campaigns' key not found in sponsored_product_campaigns.")

def get_sponsored_brands_campaigns(access_token, client_id, profile_id):
    headers = {
        'Amazon-Advertising-API-ClientId': client_id,
        'Amazon-Advertising-API-Scope': profile_id,
        'Authorization': access_token,
    }
    response = requests.get('https://advertising-api-eu.amazon.com/sb/campaigns', headers=headers)
    return json.loads(response.text)

def print_sponsored_brands_campaigns(sponsored_brands_campaigns):
    if isinstance(sponsored_brands_campaigns, list):
        sponsored_brands_campaigns_data = []

        for campaign in sponsored_brands_campaigns:
            campaign_data = {}
            campaign_data["campaignId"] = campaign.get("campaignId")
            campaign_data["name"] = campaign.get("name")
            campaign_data["state"] = campaign.get("state")
            campaign_data["budget"] = campaign.get("budget")
            campaign_data["budgetType"] = campaign.get("budgetType")
            campaign_data["servingStatus"] = campaign.get("servingStatus")

            sponsored_brands_campaigns_data.append(campaign_data)

        print("Sponsored Brands Campaigns Data:")
        print(tabulate(sponsored_brands_campaigns_data, headers="keys", tablefmt="grid"))
    else:
        print("Error: Campaign data is not in the expected format.")

def main():
    REFRESH_TOKEN = "Atzr|IwEBII3rfEevtipGGJsx_StgDRsBE-4lTdkPbkw0OYDRfkkWqD7Nu5Ujz5js1BZscsWyxW1OGPo9LxTtVBQM-V-uFHeo27utIdl1-je6E74K8Q12MsFAXEZBqSkyPMsUIemF2BKR3FMw7rRJPh15MdolcpipySgmKyiUb3c4qVqbUY6tXmT5mM2bAHKjxU8gV1CvpxwUDCDhWdeVxScRhz5-vJehqm7-2jN-T4s4yi-wWxGs6Q04UvB4Pa1Mk8vNelZQHiRdZfz0IZTLuWza2sQXeivgCHUam4ARgMmX4DQuWZf6HxePQzww2giQ472Nr-dmrAcsiMeUxYqm1Z9GQn7Pdm7il_67mn95wOpVF082X9E6UUfKxWy7CJ8dvTN-B8Eo0T4o-UEeWmjgyzpuYTFSGy7hCqtxM0YnanmK9LWwPxyyL_5xqcBhi96RRS2EtqQEbCNieebrO3nLgd7oILRKwdnAHOTzmPzA8nUnpNd0wJUAmQ"
    CLIENT_ID = "amzn1.application-oa2-client.542a565d61904101afc00555ce336340"
    CLIENT_SECRET = "amzn1.oa2-cs.v1.7a0a5a1d89a149722fe8d033b3115d661c25076a70817f1ef0ce9886a8a20681"
    
    access_token = get_access_token(REFRESH_TOKEN, CLIENT_ID, CLIENT_SECRET)
    profile_id = get_profile_id(access_token, CLIENT_ID)
    
    sponsored_display_campaigns = get_sponsored_display_campaigns(access_token, CLIENT_ID, profile_id)
    print_sponsored_display_campaigns(sponsored_display_campaigns)
    
    sponsored_product_campaigns = get_sponsored_product_campaigns(access_token, CLIENT_ID, profile_id)
    print_sponsored_product_campaigns(sponsored_product_campaigns)
    
    sponsored_brands_campaigns = get_sponsored_brands_campaigns(access_token, CLIENT_ID, profile_id)
    print_sponsored_brands_campaigns(sponsored_brands_campaigns)

if __name__ == "__main__":
    main()
