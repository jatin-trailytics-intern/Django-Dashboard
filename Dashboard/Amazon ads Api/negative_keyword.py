import requests

REFRESH_TOKEN = "Atzr|IwEBII3rfEevtipGGJsx_StgDRsBE-4lTdkPbkw0OYDRfkkWqD7Nu5Ujz5js1BZscsWyxW1OGPo9LxTtVBQM-V-uFHeo27utIdl1-je6E74K8Q12MsFAXEZBqSkyPMsUIemF2BKR3FMw7rRJPh15MdolcpipySgmKyiUb3c4qVqbUY6tXmT5mM2bAHKjxU8gV1CvpxwUDCDhWdeVxScRhz5-vJehqm7-2jN-T4s4yi-wWxGs6Q04UvB4Pa1Mk8vNelZQHiRdZfz0IZTLuWza2sQXeivgCHUam4ARgMmX4DQuWZf6HxePQzww2giQ472Nr-dmrAcsiMeUxYqm1Z9GQn7Pdm7il_67mn95wOpVF082X9E6UUfKxWy7CJ8dvTN-B8Eo0T4o-UEeWmjgyzpuYTFSGy7hCqtxM0YnanmK9LWwPxyyL_5xqcBhi96RRS2EtqQEbCNieebrO3nLgd7oILRKwdnAHOTzmPzA8nUnpNd0wJUAmQ"
CLIENT_ID = "amzn1.application-oa2-client.542a565d61904101afc00555ce336340"
CLIENT_SECRET = "amzn1.oa2-cs.v1.7a0a5a1d89a149722fe8d033b3115d661c25076a70817f1ef0ce9886a8a20681"
CAMPAIGN_ID = "504505596112828"  

def get_access_token(refresh_token):
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
    }
    
    data = {
      'grant_type': 'refresh_token',
      'client_id': CLIENT_ID,
      'refresh_token': refresh_token,
      'client_secret': CLIENT_SECRET
    }
    
    response = requests.post('https://api.amazon.com/auth/o2/token', headers=headers, data=data)
    r_json = response.json()
    return r_json["access_token"]

def fetch_negative_keywords(access_token, campaign_id=None):
    
    endpoint_url = "https://advertising-api-eu.amazon.com/sp/negativeKeywords/list"
    headers = {
        "Authorization": access_token,
        "Amazon-Advertising-API-ClientId": CLIENT_ID,
        'Amazon-Advertising-API-Scope': '566062612927990',
        "Content-Type": "application/json"
    }
    data = {
        "campaignIdFilter": {
            "include": [campaign_id] if campaign_id else []
        }
    }

    response = requests.post(endpoint_url, headers=headers, data=data)

    if response.status_code == 200:
     
        negative_keywords = response.json()
        return negative_keywords
    else:
        print(f"Failed to fetch negative keywords. Status code: {response.status_code}")
        return None

access_token = get_access_token(REFRESH_TOKEN)

if access_token:
    negative_keywords = fetch_negative_keywords(access_token, campaign_id=CAMPAIGN_ID)
    if negative_keywords:
        print("Negative Keywords:")
        for keyword in negative_keywords:
            print(keyword)
