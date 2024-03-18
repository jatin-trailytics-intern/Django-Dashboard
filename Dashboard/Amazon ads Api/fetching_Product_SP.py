import requests
import json
import gzip
import csv
import time

REFRESH_TOKEN = "Atzr|IwEBII3rfEevtipGGJsx_StgDRsBE-4lTdkPbkw0OYDRfkkWqD7Nu5Ujz5js1BZscsWyxW1OGPo9LxTtVBQM-V-uFHeo27utIdl1-je6E74K8Q12MsFAXEZBqSkyPMsUIemF2BKR3FMw7rRJPh15MdolcpipySgmKyiUb3c4qVqbUY6tXmT5mM2bAHKjxU8gV1CvpxwUDCDhWdeVxScRhz5-vJehqm7-2jN-T4s4yi-wWxGs6Q04UvB4Pa1Mk8vNelZQHiRdZfz0IZTLuWza2sQXeivgCHUam4ARgMmX4DQuWZf6HxePQzww2giQ472Nr-dmrAcsiMeUxYqm1Z9GQn7Pdm7il_67mn95wOpVF082X9E6UUfKxWy7CJ8dvTN-B8Eo0T4o-UEeWmjgyzpuYTFSGy7hCqtxM0YnanmK9LWwPxyyL_5xqcBhi96RRS2EtqQEbCNieebrO3nLgd7oILRKwdnAHOTzmPzA8nUnpNd0wJUAmQ"
CLIENT_ID = "amzn1.application-oa2-client.542a565d61904101afc00555ce336340"
CLIENT_SECRET = "amzn1.oa2-cs.v1.7a0a5a1d89a149722fe8d033b3115d661c25076a70817f1ef0ce9886a8a20681"

# Step 1: Get a new access token
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
    return r_json.get("access_token")

# Step 2: Create Report of date and defined metrics
def create_report(refresh_token, client_id, client_secret):
    access_token = get_access_token(refresh_token, client_id, client_secret)
    if access_token is None:
        print("Failed to obtain access token.")
        return None
    
    headers = {
        'Content-Type': 'application/vnd.createasyncreportrequest.v3+json',
        'Amazon-Advertising-API-ClientId': client_id,
        'Amazon-Advertising-API-Scope': '566062612927990',  # profile id
        'Authorization': access_token,
    }

    data = {
        "name": "SP Product report ",
        "startDate": "2024-02-28",
        "endDate": "2024-02-28",
        "configuration": {
            "adProduct": "SPONSORED_PRODUCTS",
            "groupBy": ["advertiser"],
            "columns": [
                "impressions", 
"clicks", 
"cost", 
"purchases1d", 
"purchases7d", 
"purchases14d", 
"purchases30d", 
"purchasesSameSku1d", 
"purchasesSameSku7d", 
"purchasesSameSku14d", 
"purchasesSameSku30d", 
"unitsSoldClicks1d", 
"unitsSoldClicks7d", 
"unitsSoldClicks14d", 
"unitsSoldClicks30d", 
"sales1d", 
"sales7d", 
"sales14d", 
"sales30d", 
# "attributedSalesSameSku1d", 
# "attributedSalesSameSku7d", 
# "attributedSalesSameSku14d", 
# "attributedSalesSameSku30d", 
"unitsSoldSameSku1d", 
"unitsSoldSameSku7d", 
"unitsSoldSameSku14d", 
"unitsSoldSameSku30d", 
"startDate", 
"endDate",  
"costPerClick", 
"clickThroughRate",
"campaignName", 
"campaignId", 
"campaignStatus", 
"campaignBudgetAmount", 
"campaignBudgetType", 
"campaignBudgetCurrencyCode", 
"adGroupName", 
"adGroupId", 
"acosClicks7d", 
"acosClicks14d", 
"roasClicks7d", 
"roasClicks14d",
"portfolioId",

            ],
            "reportTypeId": "spAdvertisedProduct",
            "timeUnit": "SUMMARY",
            "format": "GZIP_JSON"
        }
    }

    response = requests.post('https://advertising-api-eu.amazon.com/reporting/reports', headers=headers, json=data)
    if response.status_code == 200:
        report_creation_response = json.loads(response.text)
        report_id = report_creation_response.get('reportId')
        print(f"Report created with ID: {report_id}")
        return report_id
    else:
        print("Failed to create report:", response.status_code)
        print("Response text:", response.text)  # Print response text for debugging
        return None

# Function to extract URL from response
def extract_url(response_json):
    response_dict = json.loads(response_json)
    return response_dict.get('url')

# Function to fetch and convert report to JSON
def fetch_and_convert_to_json(gzip_url):
    response = requests.get(gzip_url)
    if response.status_code == 200:
        decompressed_content = gzip.decompress(response.content)
        return json.loads(decompressed_content)
    else:
        print("Failed to fetch the gzip file:", response.status_code)
        return None

# Function to get and convert report
def get_and_convert_report(refresh_token, client_id, client_secret, report_id):
    access_token = get_access_token(refresh_token, client_id, client_secret)
    if access_token is None:
        print("Failed to obtain access token.")
        return None
    
    headers = {
        'Content-Type': 'application/vnd.createasyncreportrequest.v3+json',
        'Amazon-Advertising-API-ClientId': client_id,
        'Amazon-Advertising-API-Scope': '566062612927990',  # profile id
        'Authorization': access_token,
    }

    # Wait for 15 minutes before downloading the report
    print("Waiting for 15 minutes before downloading the report...")
    time.sleep(900)

    response = requests.get(f'https://advertising-api-eu.amazon.com/reporting/reports/{report_id}', headers=headers)
    if response.status_code == 200:
        url = extract_url(response.text)
        if url:
            json_data = fetch_and_convert_to_json(url)
            return json_data
        else:
            print("Failed to extract URL from the report response.")
            print("Response text:", response.text)  # Print response text for debugging
            return None
    else:
        print("Failed to fetch the report:", response.status_code)
        print("Response text:", response.text)  # Print response text for debugging
        return None


def main():
    report_id = create_report(REFRESH_TOKEN, CLIENT_ID, CLIENT_SECRET)
    if report_id:
        print("Report ID:", report_id)
        report_data = get_and_convert_report(REFRESH_TOKEN, CLIENT_ID, CLIENT_SECRET, report_id)
        if report_data:
            print(report_data)
            # convert_to_csv(report_data)

if __name__ == "__main__":
    main()
