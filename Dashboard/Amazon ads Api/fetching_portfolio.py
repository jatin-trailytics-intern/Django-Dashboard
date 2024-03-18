import requests

# Your authentication credentials
REFRESH_TOKEN = "Atzr|IwEBII3rfEevtipGGJsx_StgDRsBE-4lTdkPbkw0OYDRfkkWqD7Nu5Ujz5js1BZscsWyxW1OGPo9LxTtVBQM-V-uFHeo27utIdl1-je6E74K8Q12MsFAXEZBqSkyPMsUIemF2BKR3FMw7rRJPh15MdolcpipySgmKyiUb3c4qVqbUY6tXmT5mM2bAHKjxU8gV1CvpxwUDCDhWdeVxScRhz5-vJehqm7-2jN-T4s4yi-wWxGs6Q04UvB4Pa1Mk8vNelZQHiRdZfz0IZTLuWza2sQXeivgCHUam4ARgMmX4DQuWZf6HxePQzww2giQ472Nr-dmrAcsiMeUxYqm1Z9GQn7Pdm7il_67mn95wOpVF082X9E6UUfKxWy7CJ8dvTN-B8Eo0T4o-UEeWmjgyzpuYTFSGy7hCqtxM0YnanmK9LWwPxyyL_5xqcBhi96RRS2EtqQEbCNieebrO3nLgd7oILRKwdnAHOTzmPzA8nUnpNd0wJUAmQ"
CLIENT_ID = "amzn1.application-oa2-client.542a565d61904101afc00555ce336340"
CLIENT_SECRET = "amzn1.oa2-cs.v1.7a0a5a1d89a149722fe8d033b3115d661c25076a70817f1ef0ce9886a8a20681"


def get_access_token(refresh_token):
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
    }
    
    data = {
      'grant_type': 'refresh_token',
      'client_id': CLIENT_ID,
      'refresh_token': refresh_token,
      'client_secret': CLIENT_SECRET,
      'scope': 'advertising::campaign_management'
    }
    
    response = requests.post('https://api.amazon.com/auth/o2/token', headers=headers, data=data)
    if response.status_code == 200:
        return response.json()["access_token"]
    else:
        print("Failed to fetch access token:", response.text)
        return None

def fetch_portfolio_list(access_token):
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Amazon-Advertising-API-ClientId': CLIENT_ID,
        'Amazon-Advertising-API-Scope': '566062612927990',
        "Content-Type": "application/json",
    }
    
    response = requests.get('https://advertising-api-eu.amazon.com/v2/portfolios', headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch portfolio list:", response.text)
        return None

if __name__ == "__main__":
    # Fetch the access token
    access_token = get_access_token(REFRESH_TOKEN)
    
    if access_token:
        # Fetch portfolio list
        portfolio_list = fetch_portfolio_list(access_token)
        
        if portfolio_list:
            print("Portfolio List:")
            print(portfolio_list)
        else:
            print("Failed to fetch portfolio list.")
    else:
        print("Failed to fetch access token.")
