import requests
import json


def c_payload(cookie_dict={}):
	cookies_x = {
	    'T': 'TI169891842149300161944937865135939588577615020537527148270186391420',
	    '_pxvid': 'c6c61fc1-7964-11ee-8e5a-1d67ccbdf2e0',
	    'dpr': '1.25',
	    '_fbp': 'fb.1.1700471257731.638459595',
	    '_gcl_aw': 'GCL.1700633033.CjwKCAiAx_GqBhBQEiwAlDNAZjBByEKtFUYtnzmB8uiqQ7Grf7_Z07cvK_m5x0f6FAJdZEU5ftur9xoCCBoQAvD_BwE',
	    '_gac_UA-172010654-1': '1.1700633034.CjwKCAiAx_GqBhBQEiwAlDNAZjBByEKtFUYtnzmB8uiqQ7Grf7_Z07cvK_m5x0f6FAJdZEU5ftur9xoCCBoQAvD_BwE',
	    '_ga_B9RGC9GN63': 'GS1.1.1702722512.1.1.1702722682.54.0.0',
	    'DID': 'clr1pup252bqp0x0wejpe1ajo',
	    'ULSN': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJjb29raWUiLCJhdWQiOiJmbGlwa2FydCIsImlzcyI6ImF1dGguZmxpcGthcnQuY29tIiwiY2xhaW1zIjp7ImdlbiI6IjEiLCJ1bmlxdWVJZCI6IlVVSTI0MDIxNDEyNTQxMjc4NE85TU9OTE0iLCJma0RldiI6bnVsbH0sImV4cCI6MTcyMzY3NTQ1MiwiaWF0IjoxNzA3ODk1NDUyLCJqdGkiOiIzZmIzYjAxZS02MzU2LTRjM2ItYTg3Yi1lNDQ3ZWNmMWJiYzEifQ.qbw3LDnvt96oOTYcrXvedJeOeJteVaWqgwkYlaKjyuw',
	    'ud': '7.FKluYsbjMSc0eLZOxg8QnowhzVZwLF7DV8Krb7TrukAYp-sew-t8uSo4wvYhTU_A56AyHK9B91iv9CQ8gsvGss9XYeRVB336vXnyYf2BWu6qOPEhW6PTgknyWlVk6t40zDBZqI_ghooutPdUhuHTQJq2aw5ZW1CfxOStGBkySf34cmST4cOWDvrCJoVFGjNKV4Oeiq4GSw-7yRllRJy868MzI1TQODRX6bwTZ9xx2c2jtSf9lZbO31CbwUyIpc3L_syjKcKQqciGn8TmYT0vi3fApsx3PSyWNBBQ4-mvSCrhtl0Gr9yGY-PbyD4ZAzOKvwrsmemKIhhsRlR-KuIIQ9aDmI3aEVVxXa8XcEmMWVMnc1J9PdzjkATofj4vC2kObv8FGfpyWXqlDVBo0IRoxMkZiPx6XB-7OczT38AWuXjzu6xLD-xm7mpw3AUrVSaqz-fy2hqD_SFl8AMqUCcyacRVODNAeCidDpCkug9Ix1hEMw9HiSFBZH0yWixwMf9M54a4-aRjGfh3_4yqq16khnPa3KGtxPYKjugscH4TazwEDnuqr359GBQmfwDym0btFkGqqPj8Udm-dCQbeM2VosOeLxpW0Ef1F0Cl7Ur8inaN0JcvwfoPDvAJ4p9R82naZmPaz_ndA_2g-qiiR0n7Vs6PMX3tybk7PV4Nj9V2b4ZkIhKrwDQHxkl42_VDAIObvbVV_wrxZ28OsbG0Qx6Aa5HQtV6TSpSfRTl_zsqV7G5yJ2QrCZllRWM7Q9K1GVpJ1IAXtAp8Z2JTA8NIW3eltQ',
	    'vh': '730',
	    'vw': '1536',
	    'K-ACTION': 'null',
	    '_ga_0RGM1K38MN': 'GS1.2.1708195526.2.1.1708195657.0.0.0',
	    '_ga_C00F4Q43Q7': 'GS1.2.1708196044.1.0.1708196044.0.0.0',
	    '_ga_2P94RMW04V': 'GS1.2.1708196121.6.1.1708196143.0.0.0',
	    '_gcl_au': '1.1.856723108.1708257205',
	    'at': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjhlM2ZhMGE3LTJmZDMtNGNiMi05MWRjLTZlNTMxOGU1YTkxZiJ9.eyJleHAiOjE3MDgyNzQzOTIsImlhdCI6MTcwODI3MjU5MiwiaXNzIjoia2V2bGFyIiwianRpIjoiZThjOTFkYzMtOWE4ZC00OTg2LTlkYWYtMTEyZjcyYWQyMzFjIiwidHlwZSI6IkFUIiwiZElkIjoiVEkxNjk4OTE4NDIxNDkzMDAxNjE5NDQ5Mzc4NjUxMzU5Mzk1ODg1Nzc2MTUwMjA1Mzc1MjcxNDgyNzAxODYzOTE0MjAiLCJiSWQiOiJHWENIUU4iLCJrZXZJZCI6IlZJNkM1MjJERkVERERCNDdCMDk0REJBQjhGQjgyNTM3Q0MiLCJ0SWQiOiJtYXBpIiwiZWFJZCI6IlNNdkZSa21lZkVqSWNQcmhSZVBXWk9keU1aTnFfSTdkUlYzQURGZ2t5TWUxbGljUTNJZ1M2UT09IiwidnMiOiJMSSIsInoiOiJIWUQiLCJtIjp0cnVlLCJnZW4iOjR9.ODpn_amJ66t-Boskps_beDpfOd9xBdN326kq6jYTby8',
	    'rt': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjhlM2ZhMGE3LTJmZDMtNGNiMi05MWRjLTZlNTMxOGU1YTkxZiJ9.eyJleHAiOjE3MjM5OTczOTIsImlhdCI6MTcwODI3MjU5MiwiaXNzIjoia2V2bGFyIiwianRpIjoiZTQ1ZTFkODAtMTFjMy00YzVkLWE1MzMtNmNlM2Q5N2VhNzc1IiwidHlwZSI6IlJUIiwiZElkIjoiVEkxNjk4OTE4NDIxNDkzMDAxNjE5NDQ5Mzc4NjUxMzU5Mzk1ODg1Nzc2MTUwMjA1Mzc1MjcxNDgyNzAxODYzOTE0MjAiLCJiSWQiOiJHWENIUU4iLCJrZXZJZCI6IlZJNkM1MjJERkVERERCNDdCMDk0REJBQjhGQjgyNTM3Q0MiLCJ0SWQiOiJtYXBpIiwibSI6eyJ0eXBlIjoibiJ9LCJ2IjoiRDZMRDdCIn0.NF50zj3IM9y93utDF90ZzLnAPybAAtQsraZYb3l4QTo',
	    'vd': 'VI6C522DFEDDDB47B094DBAB8FB82537CC-1707110391153-10.1708272592.1708272592.162289670',
	    'S': 'd1t12PyY/fzk/dz8/Pyd6KD8WP/+Uyk1zJrst/wXo40G6I+EqRhwSYBsskMrUgRPCc/q8ZY7Zv8f6xuOM+91OMnxy4A==',
	    'SN': 'VI6C522DFEDDDB47B094DBAB8FB82537CC.TOK635F5023E626455C82262BA71755319E.1708272593.LI',
	    'AMCV_17EB401053DAF4840A490D4C%40AdobeOrg': '-227196251%7CMCIDTS%7C19772%7CMCMID%7C88087235322683450901903204835359161911%7CMCAAMLH-1708320735%7C12%7CMCAAMB-1708877389%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1708279789s%7CNONE%7CMCAID%7CNONE',
	    '_px3': '4771c52436ca023ea2f7835e8f8429c1a4c613406185470abb54faa5f1f7a9e7:kHndcSe3dt2F7Z3DAbMn8aW59sa6FRocZChSbwlzeqk9mgOOMyNLav7VHvNBrK3ntN9A8Q92V4MR9JDK5xPRtg==:1000:JI1SatQl27Cc2YPWFSqcpSfhnCSlyJfmQ5SXe2AZeNPyfhjCoOF8qdX7hSrTdNOjlspTdGCL9ttRtCzeEL56BxrJAyYX9jr4EjUbqfbGFBHdDctsUawFSiZ2PBgz3ukjiM9DyRRQ6G1c93ld7Snrv2jqPHsltX0LgJsZYemLHJJYLTX1NBPPld4b4glNWdqNNsGfT8/MYBsyEdPy7Qu3VIwOVN8A4C68MNaN5+hB5d8=',
	    '_gid': 'GA1.2.871295025.1708345542',
	    'AMCV_55CFEDA0570C3FA17F000101%40AdobeOrg': '-227196251%7CMCIDTS%7C19773%7CMCMID%7C83672356534473986601461754159478791217%7CMCAAMLH-1708950352%7C7%7CMCAAMB-1708950352%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1708352752s%7CNONE%7CMCAID%7CNONE',
	    'mp_9ea3bc9a23c575907407cf80efd56524_mixpanel': '%7B%22distinct_id%22%3A%20%22ACCABA3F2470AD442FAA32E10D0E76B735F%22%2C%22%24device_id%22%3A%20%2218bf5c79f2b403-04403e63bfeec8-26031051-144000-18bf5c79f2ca33%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fseller.flipkart.com%2Fsell-online%2Fmulti-select%22%2C%22%24initial_referring_domain%22%3A%20%22seller.flipkart.com%22%2C%22%24user_id%22%3A%20%22ACCABA3F2470AD442FAA32E10D0E76B735F%22%2C%22%24search_engine%22%3A%20%22google%22%7D',
	    '_ga': 'GA1.1.1819741834.1700633034',
	    's_nr': '1708345632930-Repeat',
	    '_ga_TVF0VCMCT3': 'GS1.1.1708351242.104.0.1708351242.60.0.0',
	    '_ga_0SJLGHBL81': 'GS1.1.1708351242.104.0.1708351242.0.0.0',
	    '_csrf': 'ccpa2WrEO2TU6tjfATKNZ4u6',
	    'TENANT': 'BSS',
	    'BSS_SID': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImQxZWI3YWU1LTllNmUtNGMxNi04ZjM1LTVlYWJhOGNiYzMyZCJ9.eyJleHAiOjE3MDgzNzUzMTgsImlhdCI6MTcwODM3MzUxOCwiaXNzIjoia2V2bGFyIiwianRpIjoiMTI5NmE5ZTQtZDQ3NC00NjY4LWI4YWQtNWY2ODQ1ZjBlMjNiIiwidHlwZSI6IkFUIiwiZElkIjoiY2xyMXB1cDI1MmJxcDB4MHdlanBlMWFqbyIsImJJZCI6IldNSExERiIsImtldklkIjoiVklCNDk0MjVBQUJEMDA0RTNEQjgwRjgyQUNFMjY0MUZCRSIsInRJZCI6ImFkc191aSIsImVhSWQiOiJEYmh3SlVVcVZ6eVJQX2RLZHJQSFhkSUl1X3hxOEVuS0VJWXA1Sjd3d2x4aTFadnJsQ2pqTFE9PSIsInZzIjoiTEkiLCJ6IjoiQ0giLCJtIjpmYWxzZSwiZ2VuIjo0fQ.4nZc5bgniD6xXra-yM_NWXuDN66e-wS8SMkB2yYh6aI',
	    'CURRENT_TENANT': 'BSS',
	    'BSS_UDT': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6Im1hcmtldHBsYWNlc0BiZWxsYXZpdGFvcmdhbmljLmNvbSIsImZpcnN0TmFtZSI6IklEQU0gTmF0dXJhbCBXZWxsbmVzcyBQdnQgTHRkIiwibW9iaWxlIjoiOTgyMTU4ODk5NSIsInN0YXRlIjoiVkVSSUZJRUQiLCJzdWNjZXNzIjp0cnVlLCJ0ZW5hbnQiOiJCU1MiLCJhYWNjb3VudCI6e30sImlhdCI6MTcwODM3MzUxOCwiZXhwIjoxNzA4Mzc0MTE4fQ.Dxia3z6RMNNG44PQpAk9L4zV7O9fAsjZ34AhGm7XSuA',
	    '_ga_ZPGRNTNNRT': 'GS1.1.1708373483.50.1.1708373637.0.0.0',
	    'nonce': 'ss-2215205667',
	}

	for key in cookie_dict.keys():
	    if key in cookies_x:
	        cookies_x[key] = cookie_dict[key]

	headers = {
	    'Accept-Language': 'en-US,en;q=0.9',
	    'Cache-Control': 'no-cache',
	    'Connection': 'keep-alive',
	    # 'Cookie': 'T=TI169891842149300161944937865135939588577615020537527148270186391420; _pxvid=c6c61fc1-7964-11ee-8e5a-1d67ccbdf2e0; dpr=1.25; _fbp=fb.1.1700471257731.638459595; _gcl_aw=GCL.1700633033.CjwKCAiAx_GqBhBQEiwAlDNAZjBByEKtFUYtnzmB8uiqQ7Grf7_Z07cvK_m5x0f6FAJdZEU5ftur9xoCCBoQAvD_BwE; _gac_UA-172010654-1=1.1700633034.CjwKCAiAx_GqBhBQEiwAlDNAZjBByEKtFUYtnzmB8uiqQ7Grf7_Z07cvK_m5x0f6FAJdZEU5ftur9xoCCBoQAvD_BwE; _ga_B9RGC9GN63=GS1.1.1702722512.1.1.1702722682.54.0.0; DID=clr1pup252bqp0x0wejpe1ajo; ULSN=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJjb29raWUiLCJhdWQiOiJmbGlwa2FydCIsImlzcyI6ImF1dGguZmxpcGthcnQuY29tIiwiY2xhaW1zIjp7ImdlbiI6IjEiLCJ1bmlxdWVJZCI6IlVVSTI0MDIxNDEyNTQxMjc4NE85TU9OTE0iLCJma0RldiI6bnVsbH0sImV4cCI6MTcyMzY3NTQ1MiwiaWF0IjoxNzA3ODk1NDUyLCJqdGkiOiIzZmIzYjAxZS02MzU2LTRjM2ItYTg3Yi1lNDQ3ZWNmMWJiYzEifQ.qbw3LDnvt96oOTYcrXvedJeOeJteVaWqgwkYlaKjyuw; ud=7.FKluYsbjMSc0eLZOxg8QnowhzVZwLF7DV8Krb7TrukAYp-sew-t8uSo4wvYhTU_A56AyHK9B91iv9CQ8gsvGss9XYeRVB336vXnyYf2BWu6qOPEhW6PTgknyWlVk6t40zDBZqI_ghooutPdUhuHTQJq2aw5ZW1CfxOStGBkySf34cmST4cOWDvrCJoVFGjNKV4Oeiq4GSw-7yRllRJy868MzI1TQODRX6bwTZ9xx2c2jtSf9lZbO31CbwUyIpc3L_syjKcKQqciGn8TmYT0vi3fApsx3PSyWNBBQ4-mvSCrhtl0Gr9yGY-PbyD4ZAzOKvwrsmemKIhhsRlR-KuIIQ9aDmI3aEVVxXa8XcEmMWVMnc1J9PdzjkATofj4vC2kObv8FGfpyWXqlDVBo0IRoxMkZiPx6XB-7OczT38AWuXjzu6xLD-xm7mpw3AUrVSaqz-fy2hqD_SFl8AMqUCcyacRVODNAeCidDpCkug9Ix1hEMw9HiSFBZH0yWixwMf9M54a4-aRjGfh3_4yqq16khnPa3KGtxPYKjugscH4TazwEDnuqr359GBQmfwDym0btFkGqqPj8Udm-dCQbeM2VosOeLxpW0Ef1F0Cl7Ur8inaN0JcvwfoPDvAJ4p9R82naZmPaz_ndA_2g-qiiR0n7Vs6PMX3tybk7PV4Nj9V2b4ZkIhKrwDQHxkl42_VDAIObvbVV_wrxZ28OsbG0Qx6Aa5HQtV6TSpSfRTl_zsqV7G5yJ2QrCZllRWM7Q9K1GVpJ1IAXtAp8Z2JTA8NIW3eltQ; vh=730; vw=1536; K-ACTION=null; _ga_0RGM1K38MN=GS1.2.1708195526.2.1.1708195657.0.0.0; _ga_C00F4Q43Q7=GS1.2.1708196044.1.0.1708196044.0.0.0; _ga_2P94RMW04V=GS1.2.1708196121.6.1.1708196143.0.0.0; _gcl_au=1.1.856723108.1708257205; at=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjhlM2ZhMGE3LTJmZDMtNGNiMi05MWRjLTZlNTMxOGU1YTkxZiJ9.eyJleHAiOjE3MDgyNzQzOTIsImlhdCI6MTcwODI3MjU5MiwiaXNzIjoia2V2bGFyIiwianRpIjoiZThjOTFkYzMtOWE4ZC00OTg2LTlkYWYtMTEyZjcyYWQyMzFjIiwidHlwZSI6IkFUIiwiZElkIjoiVEkxNjk4OTE4NDIxNDkzMDAxNjE5NDQ5Mzc4NjUxMzU5Mzk1ODg1Nzc2MTUwMjA1Mzc1MjcxNDgyNzAxODYzOTE0MjAiLCJiSWQiOiJHWENIUU4iLCJrZXZJZCI6IlZJNkM1MjJERkVERERCNDdCMDk0REJBQjhGQjgyNTM3Q0MiLCJ0SWQiOiJtYXBpIiwiZWFJZCI6IlNNdkZSa21lZkVqSWNQcmhSZVBXWk9keU1aTnFfSTdkUlYzQURGZ2t5TWUxbGljUTNJZ1M2UT09IiwidnMiOiJMSSIsInoiOiJIWUQiLCJtIjp0cnVlLCJnZW4iOjR9.ODpn_amJ66t-Boskps_beDpfOd9xBdN326kq6jYTby8; rt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjhlM2ZhMGE3LTJmZDMtNGNiMi05MWRjLTZlNTMxOGU1YTkxZiJ9.eyJleHAiOjE3MjM5OTczOTIsImlhdCI6MTcwODI3MjU5MiwiaXNzIjoia2V2bGFyIiwianRpIjoiZTQ1ZTFkODAtMTFjMy00YzVkLWE1MzMtNmNlM2Q5N2VhNzc1IiwidHlwZSI6IlJUIiwiZElkIjoiVEkxNjk4OTE4NDIxNDkzMDAxNjE5NDQ5Mzc4NjUxMzU5Mzk1ODg1Nzc2MTUwMjA1Mzc1MjcxNDgyNzAxODYzOTE0MjAiLCJiSWQiOiJHWENIUU4iLCJrZXZJZCI6IlZJNkM1MjJERkVERERCNDdCMDk0REJBQjhGQjgyNTM3Q0MiLCJ0SWQiOiJtYXBpIiwibSI6eyJ0eXBlIjoibiJ9LCJ2IjoiRDZMRDdCIn0.NF50zj3IM9y93utDF90ZzLnAPybAAtQsraZYb3l4QTo; vd=VI6C522DFEDDDB47B094DBAB8FB82537CC-1707110391153-10.1708272592.1708272592.162289670; S=d1t12PyY/fzk/dz8/Pyd6KD8WP/+Uyk1zJrst/wXo40G6I+EqRhwSYBsskMrUgRPCc/q8ZY7Zv8f6xuOM+91OMnxy4A==; SN=VI6C522DFEDDDB47B094DBAB8FB82537CC.TOK635F5023E626455C82262BA71755319E.1708272593.LI; AMCV_17EB401053DAF4840A490D4C%40AdobeOrg=-227196251%7CMCIDTS%7C19772%7CMCMID%7C88087235322683450901903204835359161911%7CMCAAMLH-1708320735%7C12%7CMCAAMB-1708877389%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1708279789s%7CNONE%7CMCAID%7CNONE; _px3=4771c52436ca023ea2f7835e8f8429c1a4c613406185470abb54faa5f1f7a9e7:kHndcSe3dt2F7Z3DAbMn8aW59sa6FRocZChSbwlzeqk9mgOOMyNLav7VHvNBrK3ntN9A8Q92V4MR9JDK5xPRtg==:1000:JI1SatQl27Cc2YPWFSqcpSfhnCSlyJfmQ5SXe2AZeNPyfhjCoOF8qdX7hSrTdNOjlspTdGCL9ttRtCzeEL56BxrJAyYX9jr4EjUbqfbGFBHdDctsUawFSiZ2PBgz3ukjiM9DyRRQ6G1c93ld7Snrv2jqPHsltX0LgJsZYemLHJJYLTX1NBPPld4b4glNWdqNNsGfT8/MYBsyEdPy7Qu3VIwOVN8A4C68MNaN5+hB5d8=; _gid=GA1.2.871295025.1708345542; AMCV_55CFEDA0570C3FA17F000101%40AdobeOrg=-227196251%7CMCIDTS%7C19773%7CMCMID%7C83672356534473986601461754159478791217%7CMCAAMLH-1708950352%7C7%7CMCAAMB-1708950352%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1708352752s%7CNONE%7CMCAID%7CNONE; mp_9ea3bc9a23c575907407cf80efd56524_mixpanel=%7B%22distinct_id%22%3A%20%22ACCABA3F2470AD442FAA32E10D0E76B735F%22%2C%22%24device_id%22%3A%20%2218bf5c79f2b403-04403e63bfeec8-26031051-144000-18bf5c79f2ca33%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fseller.flipkart.com%2Fsell-online%2Fmulti-select%22%2C%22%24initial_referring_domain%22%3A%20%22seller.flipkart.com%22%2C%22%24user_id%22%3A%20%22ACCABA3F2470AD442FAA32E10D0E76B735F%22%2C%22%24search_engine%22%3A%20%22google%22%7D; _ga=GA1.1.1819741834.1700633034; s_nr=1708345632930-Repeat; _ga_TVF0VCMCT3=GS1.1.1708351242.104.0.1708351242.60.0.0; _ga_0SJLGHBL81=GS1.1.1708351242.104.0.1708351242.0.0.0; _csrf=ccpa2WrEO2TU6tjfATKNZ4u6; TENANT=BSS; BSS_SID=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImQxZWI3YWU1LTllNmUtNGMxNi04ZjM1LTVlYWJhOGNiYzMyZCJ9.eyJleHAiOjE3MDgzNzUzMTgsImlhdCI6MTcwODM3MzUxOCwiaXNzIjoia2V2bGFyIiwianRpIjoiMTI5NmE5ZTQtZDQ3NC00NjY4LWI4YWQtNWY2ODQ1ZjBlMjNiIiwidHlwZSI6IkFUIiwiZElkIjoiY2xyMXB1cDI1MmJxcDB4MHdlanBlMWFqbyIsImJJZCI6IldNSExERiIsImtldklkIjoiVklCNDk0MjVBQUJEMDA0RTNEQjgwRjgyQUNFMjY0MUZCRSIsInRJZCI6ImFkc191aSIsImVhSWQiOiJEYmh3SlVVcVZ6eVJQX2RLZHJQSFhkSUl1X3hxOEVuS0VJWXA1Sjd3d2x4aTFadnJsQ2pqTFE9PSIsInZzIjoiTEkiLCJ6IjoiQ0giLCJtIjpmYWxzZSwiZ2VuIjo0fQ.4nZc5bgniD6xXra-yM_NWXuDN66e-wS8SMkB2yYh6aI; CURRENT_TENANT=BSS; BSS_UDT=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6Im1hcmtldHBsYWNlc0BiZWxsYXZpdGFvcmdhbmljLmNvbSIsImZpcnN0TmFtZSI6IklEQU0gTmF0dXJhbCBXZWxsbmVzcyBQdnQgTHRkIiwibW9iaWxlIjoiOTgyMTU4ODk5NSIsInN0YXRlIjoiVkVSSUZJRUQiLCJzdWNjZXNzIjp0cnVlLCJ0ZW5hbnQiOiJCU1MiLCJhYWNjb3VudCI6e30sImlhdCI6MTcwODM3MzUxOCwiZXhwIjoxNzA4Mzc0MTE4fQ.Dxia3z6RMNNG44PQpAk9L4zV7O9fAsjZ34AhGm7XSuA; _ga_ZPGRNTNNRT=GS1.1.1708373483.50.1.1708373637.0.0.0; nonce=ss-2215205667',
	    'Origin': 'https://advertising.flipkart.com',
	    'Pragma': 'no-cache',
	    'Referer': 'https://advertising.flipkart.com/ad-account/campaigns?baccount=N5J3WN87DKC4&aaccount=IZJL4R3KCMHR',
	    'Sec-Fetch-Dest': 'empty',
	    'Sec-Fetch-Mode': 'cors',
	    'Sec-Fetch-Site': 'same-origin',
	    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
	    'accept': '*/*',
	    'apollographql-client-name': 'Flipkart-Ads',
	    'apollographql-client-version': '1.0.0',
	    'content-type': 'application/json',
	    'downlink': '10',
	    'dpr': '1.25',
	    'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
	    'sec-ch-ua-mobile': '?0',
	    'sec-ch-ua-platform': '"Windows"',
	    'viewport-width': '923',
	    'x-aaccount': 'IZJL4R3KCMHR',
	    'x-baccount': 'N5J3WN87DKC4',
	    'x-csrf-token': 'ltaGEqIm-_6NH8jpydBJOm1HIaBzuW6gR15c',
	    'x-sourceurl': 'https://advertising.flipkart.com/ad-account/campaigns?baccount=N5J3WN87DKC4&aaccount=IZJL4R3KCMHR',
	    'x-tenant': 'BSS',
	}

	json_data = {
	    'operationName': 'GetConsolidatedCampaignReport',
	    'variables': {
	        'dateRange': {
	            'endDate': '2024-02-20',
	            'startDate': '2024-02-06',
	        },
	        'pageLevelFilter': [],
	        'queries': [
	            {
	                'query': {
	                    'filters': [
	                        {
	                            'comparator': [
	                                'IZJL4R3KCMHR',
	                            ],
	                            'field': {
	                                'entity_type': 'DIMENSION',
	                                'function': 'VALUE',
	                                'name': 'advertiser_id',
	                            },
	                            'operator': 'IN',
	                            'view_id': '671',
	                        },
	                    ],
	                    'group_by': [
	                        {
	                            'function': 'VALUE',
	                            'name': 'campaign_id',
	                        },
	                        {
	                            'function': 'VALUE',
	                            'name': 'campaign_start_and_end_date',
	                        },
	                        {
	                            'function': 'VALUE',
	                            'name': 'campaign_budget',
	                        },
	                        {
	                            'function': 'VALUE',
	                            'name': 'campaign_name',
	                        },
	                        {
	                            'function': 'VALUE',
	                            'name': 'advertiser_id',
	                        },
	                        {
	                            'function': 'VALUE',
	                            'name': 'campaign_status',
	                        },
	                        {
	                            'function': 'VALUE',
	                            'name': 'campaign_type',
	                        },
	                        {
	                            'function': 'VALUE',
	                            'name': 'campaign_start_date',
	                        },
	                        {
	                            'function': 'VALUE',
	                            'name': 'campaign_end_date',
	                        },
	                        {
	                            'function': 'VALUE',
	                            'name': 'marketplace',
	                        },
	                        {
	                            'function': 'VALUE',
	                            'name': 'campaign_budget_type',
	                        },
	                    ],
	                    'metrics': [
	                        {
	                            'function': 'SUM',
	                            'name': 'cost',
	                        },
	                        {
	                            'function': 'SUM',
	                            'name': 'remaining_budget',
	                        },
	                        {
	                            'function': 'SUM',
	                            'name': 'views',
	                        },
	                        {
	                            'function': 'SUM',
	                            'name': 'clicks',
	                        },
	                        {
	                            'function': 'VALUE',
	                            'name': 'total_converted_units',
	                        },
	                        {
	                            'function': 'VALUE',
	                            'name': 'total_converted_revenue',
	                        },
	                        {
	                            'function': 'VALUE',
	                            'name': 'roi',
	                        },
	                        {
	                            'function': 'VALUE',
	                            'name': 'CTR',
	                        },
	                        {
	                            'function': 'VALUE',
	                            'name': 'cvr',
	                        },
	                        {
	                            'function': 'VALUE',
	                            'name': 'campaign_allowed_actions',
	                        },
	                    ],
	                    'order_by': {
	                        'fields': [
	                            {
	                                'entity_type': 'METRIC',
	                                'function': 'SUM',
	                                'name': 'views',
	                            },
	                        ],
	                        'type': 'DESC',
	                    },
	                    'page_size': 600,
	                    'type': 'TABULAR',
	                    'view_id': '671',
	                },
	                'queryId': 'tabular-123',
	            },
	        ],
	        'requestId': '1234',
	        'timeGranularity': 'DAY',
	        'adProducts': [
	            'BRAND_PLA',
	            'BRAND_PCA',
	        ],
	        'marketPlaces': [
	            'FLIPKART',
	            'GROCERY',
	        ],
	    },
	    'query': 'query GetConsolidatedCampaignReport($dateRange: URFDateRange!, $timeGranularity: String, $budgetRecommended: Boolean, $requestId: ID!, $pageLevelFilter: [URFFilter!]!, $queries: [URFQuerySet!]!, $adProducts: [String!]!, $marketPlaces: [String!]!) {\n  getConsolidatedCampaignReport(dateRange: $dateRange, timeGranularity: $timeGranularity, budgetRecommended: $budgetRecommended, requestId: $requestId, pageLevelFilter: $pageLevelFilter, queries: $queries, adProducts: $adProducts, marketPlaces: $marketPlaces) {\n    code\n    columns {\n      entityType\n      name\n      type\n      metadata {\n        HAS_MULTISOURCE\n        __typename\n      }\n      __typename\n    }\n    rows {\n      values\n      __typename\n    }\n    __typename\n  }\n}\n',
	}

	response = requests.post('https://advertising.flipkart.com/api', cookies = cookies_x, headers=headers, json=json_data)
	ans = json.loads(response.text)
	rows = (ans["data"]["getConsolidatedCampaignReport"]["rows"])
	for row in rows:
	    values = row.get('values', None)
	    if values:
	        campaign_status = values[0]  # Accessing the status
	        campaign_name = values[1]
	        campaign_start_and_end_date = values[2]
	        brand = values[5]
	        product_code = values[9]
	        imp_code = values[10]
	        print(f"campaign_status: {campaign_status}, campaign_name: {campaign_name}, campaign_start_and_end_date: {campaign_start_and_end_date}")