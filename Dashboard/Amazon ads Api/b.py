import requests
import json
import gzip
import time

REFRESH_TOKEN = "Atzr|IwEBII3rfEevtipGGJsx_StgDRsBE-4lTdkPbkw0OYDRfkkWqD7Nu5Ujz5js1BZscsWyxW1OGPo9LxTtVBQM-V-uFHeo27utIdl1-je6E74K8Q12MsFAXEZBqSkyPMsUIemF2BKR3FMw7rRJPh15MdolcpipySgmKyiUb3c4qVqbUY6tXmT5mM2bAHKjxU8gV1CvpxwUDCDhWdeVxScRhz5-vJehqm7-2jN-T4s4yi-wWxGs6Q04UvB4Pa1Mk8vNelZQHiRdZfz0IZTLuWza2sQXeivgCHUam4ARgMmX4DQuWZf6HxePQzww2giQ472Nr-dmrAcsiMeUxYqm1Z9GQn7Pdm7il_67mn95wOpVF082X9E6UUfKxWy7CJ8dvTN-B8Eo0T4o-UEeWmjgyzpuYTFSGy7hCqtxM0YnanmK9LWwPxyyL_5xqcBhi96RRS2EtqQEbCNieebrO3nLgd7oILRKwdnAHOTzmPzA8nUnpNd0wJUAmQ"
CLIENT_ID = "amzn1.application-oa2-client.542a565d61904101afc00555ce336340"
CLIENT_SECRET = "amzn1.oa2-cs.v1.7a0a5a1d89a149722fe8d033b3115d661c25076a70817f1ef0ce9886a8a20681"
# REPORT_ID = "ec5cdc67-d043-4f56-981b-42c8dd0a84ff"  # Replace with your report ID

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

def extract_value(data_list, key):
    for item in data_list:
        if key in item:
            return item[key]
    return None

def fetch_report_id(access_token, profile_id):
    headers = {
        'Content-Type': 'application/vnd.createasyncreportrequest.v3+json',
        'Amazon-Advertising-API-ClientId': CLIENT_ID,
        'Amazon-Advertising-API-Scope': profile_id,
        'Authorization': access_token,
    }

    data = {
        "name": "SP campaigns report 7/5-7/10",
        "startDate": "2024-02-02",
        "endDate": "2024-02-10",
        "configuration": {
            "adProduct": "SPONSORED_PRODUCTS",
            "groupBy": ["campaign", "adGroup"],
            "columns": ["campaignId", "adGroupId", "impressions","ctc" ,"clicks", "cost", "purchases1d", "purchases7d", "purchases14d", "purchases30d", "spend","startDate", "endDate","campaignBudget,campaignRuleBasedBudget,applicableBudgetRuleId,applicableBudgetRuleName"],
            "reportTypeId": "campaignPerformanceReport",
            "timeUnit": "SUMMARY",
            "format": "GZIP_JSON"
            
        }
    }

    response = requests.post('https://advertising-api-eu.amazon.com/reporting/reports', headers=headers, json=data)
    r_json = response.json()
    return r_json.get("reportId")

def extract_url(response_json):
    response_dict = json.loads(response_json)
    return response_dict.get('url')

def fetch_and_convert_to_json(gzip_url):
    response = requests.get(gzip_url)
    if response.status_code == 200:
        decompressed_content = gzip.decompress(response.content)
        return json.loads(decompressed_content)
    else:
        print("Failed to fetch the gzip file:", response.status_code)
        return None

def get_and_convert_report(refresh_token, client_id, client_secret, report_id):
    access_token = get_access_token(refresh_token)
    headers = {
        'Content-Type': 'application/vnd.createasyncreportrequest.v3+json',
        'Amazon-Advertising-API-ClientId': client_id,
        'Amazon-Advertising-API-Scope': '566062612927990',  # profile id
        'Authorization': access_token,
    }
    response = requests.get(f'https://advertising-api-eu.amazon.com/reporting/reports/{report_id}', headers=headers)
    if response.status_code == 200:
        url = extract_url(response.text)
        if url:
            json_data = fetch_and_convert_to_json(url)
            return json_data
        else:
            print("Failed to extract URL from the report response.")
            return None
    else:
        print("Failed to fetch the report:", response.status_code)
        return None

def main():
    access_token = get_access_token(REFRESH_TOKEN)
    
    headers = {
        'Amazon-Advertising-API-ClientId': CLIENT_ID,
        'Authorization': access_token,
    }

    response = requests.get("https://advertising-api-eu.amazon.com/v2/profiles", headers=headers)
    
    output_data = json.loads(response.text)
    profile_id = extract_value(output_data, 'profileId')
    
    if profile_id is not None:
        print("Profile ID:", profile_id)
        report_id = fetch_report_id(access_token, str(profile_id))
        print("Report ID:", report_id)
        
        # Adding a 15-minute delay
        print("Waiting for 15 minutes before fetching the report...")
        time.sleep(900)  # 15 minutes delay
        
        report_data = get_and_convert_report(REFRESH_TOKEN, CLIENT_ID, CLIENT_SECRET, report_id)
        if report_data:
            print(report_data)
            for entry in report_data:
                spend = entry.get('spend')
                purchases30d = entry.get('purchases30d')
                roas=purchases30d/spend
                if spend is not None and purchases30d is not None:
                    print({'spend': spend, 'purchases30d': purchases30d})
                    print(roas)
    else:
        print("Key 'profileId' not found in the list of dictionaries.")

if __name__ == "__main__":
    main()
