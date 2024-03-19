import requests
import argparse
import json

parser = argparse.ArgumentParser(description='campaign details')
parser.add_argument('--p1', action="store", dest='para1', default="")
parser.add_argument('--p2', action="store", dest='para2', default="")
parser.add_argument('--p3', action="store", dest='para3', default="")

args = parser.parse_args()

print(args.para1, args.para2, args.para3)

# Global variables
REFRESH_TOKEN = "Atzr|IwEBII3rfEevtipGGJsx_StgDRsBE-4lTdkPbkw0OYDRfkkWqD7Nu5Ujz5js1BZscsWyxW1OGPo9LxTtVBQM-V-uFHeo27utIdl1-je6E74K8Q12MsFAXEZBqSkyPMsUIemF2BKR3FMw7rRJPh15MdolcpipySgmKyiUb3c4qVqbUY6tXmT5mM2bAHKjxU8gV1CvpxwUDCDhWdeVxScRhz5-vJehqm7-2jN-T4s4yi-wWxGs6Q04UvB4Pa1Mk8vNelZQHiRdZfz0IZTLuWza2sQXeivgCHUam4ARgMmX4DQuWZf6HxePQzww2giQ472Nr-dmrAcsiMeUxYqm1Z9GQn7Pdm7il_67mn95wOpVF082X9E6UUfKxWy7CJ8dvTN-B8Eo0T4o-UEeWmjgyzpuYTFSGy7hCqtxM0YnanmK9LWwPxyyL_5xqcBhi96RRS2EtqQEbCNieebrO3nLgd7oILRKwdnAHOTzmPzA8nUnpNd0wJUAmQ"
CLIENT_ID = "amzn1.application-oa2-client.542a565d61904101afc00555ce336340"
CLIENT_SECRET = "amzn1.oa2-cs.v1.7a0a5a1d89a149722fe8d033b3115d661c25076a70817f1ef0ce9886a8a20681"
SCOPE = "566062612927990"

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

def update_campaign_status(api_type, campaign_id, status):
    access_token = get_access_token()
    
    if api_type == 'sp':
        endpoint = 'https://advertising-api-eu.amazon.com/sp/campaigns'
        headers = {
            'Amazon-Advertising-API-ClientId': CLIENT_ID,
            'Authorization': 'Bearer ' + access_token, 
            'Amazon-Advertising-API-Scope': SCOPE,
            'Accept': 'application/vnd.spCampaign.v3+json',
            'Content-Type': 'application/vnd.spCampaign.v3+json',
        }
        data = {
            "campaignId": campaign_id,
            "state": status
            #"name": "string",
            #"targetingType": "AUTO",
            #"budget": {
              #  "budgetType": "DAILY",
              #  "budget": 0.1
               # },
        }
    elif api_type == 'sb':
        endpoint = 'https://advertising-api-eu.amazon.com/sb/v4/campaigns'
        headers = {
            'Amazon-Advertising-API-ClientId': CLIENT_ID,
            'Authorization': 'Bearer ' + access_token, 
            'Amazon-Advertising-API-Scope': SCOPE,
            'Accept': 'application/vnd.sbcampaignresource.v4+json',
            'Content-Type': 'application/vnd.sbcampaignresource.v4+json',

        }
        data = {
            "campaigns": [
                {
                    "campaignId": campaign_id,
                    "state": status
                    #"name": "string",
                    #"budget": newbudget,
                    #"startDate": "string",
                }
            ]
        }
    elif api_type == 'sd':
        endpoint = 'https://advertising-api-eu.amazon.com/sd/campaigns'
        headers = {
            'Amazon-Advertising-API-ClientId': CLIENT_ID,
            'Authorization': 'Bearer ' + access_token, 
            'Amazon-Advertising-API-Scope': SCOPE,
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        data = [
            {
                "campaignId": campaign_id,
                "state": status
                #"name":"whatever name",
                #"budget":"new budget",
                #budgetType:"typeof budget",
            }
        ]
    else:
        print("Invalid API type.")
        return
    
    response = requests.put(endpoint, headers=headers, data=json.dumps(data))

    if response.status_code == 207:
        print(f"Campaign status updated successfully for {api_type.upper()} API.")
    else:
        print(f"Error updating campaign status for {api_type.upper()} API. Status code:", response.status_code)
        print("Error message:", response.text)

update_campaign_status(args.para1, args.para2, args.para3)
print("I can be called")
# for sd --> sd campaignid enabled/paused
# for sb --> sb campaignid ENABLED/PAUSED
# for sp --> sp campaignId ENABLED/PAUSED
