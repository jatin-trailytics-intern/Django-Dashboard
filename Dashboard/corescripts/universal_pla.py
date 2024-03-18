import requests
import json
from channel import *

def master_command(cook={}):
    cookies = {
        'T': 'TI169891842149300161944937865135939588577615020537527148270186391420',
        '_pxvid': 'c6c61fc1-7964-11ee-8e5a-1d67ccbdf2e0',
        'dpr': '1.25',
        '_fbp': 'fb.1.1700471257731.638459595',
        '_ga_B9RGC9GN63': 'GS1.1.1702722512.1.1.1702722682.54.0.0',
        'DID': 'clr1pup252bqp0x0wejpe1ajo',
        'ULSN': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJjb29raWUiLCJhdWQiOiJmbGlwa2FydCIsImlzcyI6ImF1dGguZmxpcGthcnQuY29tIiwiY2xhaW1zIjp7ImdlbiI6IjEiLCJ1bmlxdWVJZCI6IlVVSTI0MDIxNDEyNTQxMjc4NE85TU9OTE0iLCJma0RldiI6bnVsbH0sImV4cCI6MTcyMzY3NTQ1MiwiaWF0IjoxNzA3ODk1NDUyLCJqdGkiOiIzZmIzYjAxZS02MzU2LTRjM2ItYTg3Yi1lNDQ3ZWNmMWJiYzEifQ.qbw3LDnvt96oOTYcrXvedJeOeJteVaWqgwkYlaKjyuw',
        'vh': '730',
        'vw': '1536',
        '_ga_0RGM1K38MN': 'GS1.2.1708195526.2.1.1708195657.0.0.0',
        '_ga_C00F4Q43Q7': 'GS1.2.1708196044.1.0.1708196044.0.0.0',
        '_ga_2P94RMW04V': 'GS1.2.1708196121.6.1.1708196143.0.0.0',
        '_gcl_au': '1.1.856723108.1708257205',
        'K-ACTION': 'null',
        'ud': '3.-hCuLDZfVJf9kwEcWhK4arj09yD35YGA9WD7yo1zRPr-6c1rmX2_xdHegqPpB3V8IXYz3NsAnP3SBWNaEKufBfykm01W9EISet6O__tpbwLut1-EZphHbJ0c9MzW0rczeRXhalfDVODMz8JTNMlQlgc9FtPFTSU9rNePFCXS_okASoEjAhPorkspIuB6dUcZtsYfTSEOj6D6fCfEhHGTX040PuZMdyiyk409VK7VDUArNQCXrRjfusSZdRR_dSa_IYardO48M5GyGz8FGpTkPTBYE_1zDB-5NXEc93lP2wklWoHEa-Dtp_7e6v2PvoLYEnO9q9WRO923E1MzbxEsgQzTal18ocz6m1QhVKcLAkifQY1CVPvSCEDYAhYysg7Cifn25pVGYReJE-wqKz__XeZKWQ6m9S5ylJWi8ZCNic_rQWkW8tl4jP7uwPxupbq0hBk3YeSRAVvcjX09zDY5qn4jmi-pJicw3oOin6BBwh5j4AEuCE1_UBhyu1FzQ6HXVin354_zqMKmt5Ez4awQztwLbxHMqBrzPLNw1nVv-mMH56A0UIV523BaT7wlgFXFKDY9PgZuquXJtkpqqSSPK3sdeoBmL_SsoP5XdHnW3U3lvtJigEiuV1-2In3wufWsqsHYvXC8tj7Vr6X8srs_3ehJ7eFh0ZMdB7QsQTCynabS2sW3gILSeLC2-NwmdaemzanTaScNERb6Z6uBV6aYgxLtiUZZci5cqwxPaCVTIRHxdKh90EtL6MagI-T8KaMNUkYxg3mOLw4UnS1OIQr5vw',
        'AMCV_17EB401053DAF4840A490D4C%40AdobeOrg': '-227196251%7CMCIDTS%7C19795%7CMCMID%7C88087235322683450901903204835359161911%7CMCAAMLH-1710338105%7C12%7CMCAAMB-1710813620%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1710216020s%7CNONE%7CMCAID%7CNONE',
        'at': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjhlM2ZhMGE3LTJmZDMtNGNiMi05MWRjLTZlNTMxOGU1YTkxZiJ9.eyJleHAiOjE3MTAzMDM1MDEsImlhdCI6MTcxMDMwMTcwMSwiaXNzIjoia2V2bGFyIiwianRpIjoiOTgxYWNjOWMtZGE5MS00OTE2LThmYmMtOTUxMjNmNDQ5ODBhIiwidHlwZSI6IkFUIiwiZElkIjoiVEkxNjk4OTE4NDIxNDkzMDAxNjE5NDQ5Mzc4NjUxMzU5Mzk1ODg1Nzc2MTUwMjA1Mzc1MjcxNDgyNzAxODYzOTE0MjAiLCJiSWQiOiJTWVdVSloiLCJrZXZJZCI6IlZJNkM1MjJERkVERERCNDdCMDk0REJBQjhGQjgyNTM3Q0MiLCJ0SWQiOiJtYXBpIiwiZWFJZCI6IlNNdkZSa21lZkVqSWNQcmhSZVBXWk9keU1aTnFfSTdkUlYzQURGZ2t5TWUxbGljUTNJZ1M2UT09IiwidnMiOiJMSSIsInoiOiJIWUQiLCJtIjp0cnVlLCJnZW4iOjR9.M7iAS--yV9f2CqRxOyyIJSuo6jhjGKNV8WGE0qkaTW4',
        'rt': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjhlM2ZhMGE3LTJmZDMtNGNiMi05MWRjLTZlNTMxOGU1YTkxZiJ9.eyJleHAiOjE3MjYxOTkzMDEsImlhdCI6MTcxMDMwMTcwMSwiaXNzIjoia2V2bGFyIiwianRpIjoiNmFiMzM2ZTMtODhjYi00OTQ5LTljNTAtNWI2NTU0MDViOWI3IiwidHlwZSI6IlJUIiwiZElkIjoiVEkxNjk4OTE4NDIxNDkzMDAxNjE5NDQ5Mzc4NjUxMzU5Mzk1ODg1Nzc2MTUwMjA1Mzc1MjcxNDgyNzAxODYzOTE0MjAiLCJiSWQiOiJTWVdVSloiLCJrZXZJZCI6IlZJNkM1MjJERkVERERCNDdCMDk0REJBQjhGQjgyNTM3Q0MiLCJ0SWQiOiJtYXBpIiwibSI6eyJ0eXBlIjoibiJ9LCJ2IjoiQ1RBVVJMIn0.tlN-N45mURlkqikAoNxxXgtLFngU9XUnFR9OitBt7TY',
        'vd': 'VI6C522DFEDDDB47B094DBAB8FB82537CC-1707110391153-43.1710301701.1710301701.161994701',
        'S': 'd1t12fhAXNGc/P2M/ED8/Pz8YP5R1C2QLptKLX45nMO0fPoszL18MfCR2oiJUPJpcjVoXbOSe+gCGx2r6cyEFxAneSA==',
        'SN': 'VI6C522DFEDDDB47B094DBAB8FB82537CC.TOK635F5023E626455C82262BA71755319E.1710301727.LI',
        '_px3': '05ac7a05aeac365311b734b3fcdc13a8fae35ecd6ef85f1a1cbb01a843d80b5b:mAQxF/myDQOiIQtg35ie6cHy+LrsyGhI3wgW51W1Po9iS7Qmd7YE9XnVEpK8FTgpVPEyOqpvuHQf5OfyFHJuRg==:1000:FztBa6xGQwRMA3en1v9VcblVQVug5PDlOHDwfTJ7pKFnXb1gKjSu7FaIFtYoWPqOoSlG6LSyW+SRwJhzXNMMUPBR9d/6rCA7so/FAgxo4J7pGweqiar8kRy/5Fn11peQE6L4IU5JumxFX444rq87mZVe+KNfM5yoDDYYYoUqCbDPZi01dMh/VtjiIz1lL/AFDCXVYY+Mjh26w5Mg+ig1G6P2gESj97G/6dx4VBLvMO0=',
        '_gid': 'GA1.2.1420968950.1710404921',
        'AMCV_55CFEDA0570C3FA17F000101%40AdobeOrg': '-227196251%7CMCIDTS%7C19797%7CMCMID%7C83672356534473986601461754159478791217%7CMCAAMLH-1710923132%7C12%7CMCAAMB-1711023538%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1710425938s%7CNONE%7CMCAID%7CNONE',
        'mp_9ea3bc9a23c575907407cf80efd56524_mixpanel': '%7B%22distinct_id%22%3A%20%22ACCABA3F2470AD442FAA32E10D0E76B735F%22%2C%22%24device_id%22%3A%20%2218bf5c79f2b403-04403e63bfeec8-26031051-144000-18bf5c79f2ca33%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fseller.flipkart.com%2Fsell-online%2Fmulti-select%22%2C%22%24initial_referring_domain%22%3A%20%22seller.flipkart.com%22%2C%22%24user_id%22%3A%20%22ACCABA3F2470AD442FAA32E10D0E76B735F%22%2C%22%24search_engine%22%3A%20%22google%22%7D',
        '_ga_0SJLGHBL81': 'GS1.1.1710418738.13.1.1710418799.0.0.0',
        '_ga_TVF0VCMCT3': 'GS1.1.1710418738.134.1.1710418799.60.0.0',
        's_nr': '1710418799593-Repeat',
        '_ga': 'GA1.1.1819741834.1700633034',
        'CURRENT_TENANT': 'BSS',
        '_csrf': 'EmhbKG1CaciKlzp5J0JFI1tU',
        'TENANT': 'BSS',
        '_ga_ZPGRNTNNRT': 'GS1.1.1710434033.128.1.1710437614.0.0.0',
        'BSS_SID': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjA1MGRjYzRjLTE0MGYtNDNkYy1iYTUzLTM2NTY3MTQ3MWVlZSJ9.eyJleHAiOjE3MTA0MzkzMzQsImlhdCI6MTcxMDQzNzUzNCwiaXNzIjoia2V2bGFyIiwianRpIjoiYTI5ZTM1YzYtYjQ0ZS00ZTRiLWEyZDItNDM2ZGI0ZTQ0NTYwIiwidHlwZSI6IkFUIiwiZElkIjoiY2xyMXB1cDI1MmJxcDB4MHdlanBlMWFqbyIsImJJZCI6IjRQVERTUSIsImtldklkIjoiVkkwRTY3N0NGOUI5RTM0QUE5OTI3N0IxNTkyOEE0NTJGRiIsInRJZCI6ImFkc191aSIsImVhSWQiOiJEelFjYkRsbnItWWJIaUhZVUpvT2JpdnNPUHk0bUhuOER6c2xLRkxYeUZsMTB0X3RweVdubmc9PSIsInZzIjoiTEkiLCJ6IjoiQ0giLCJtIjpmYWxzZSwiZ2VuIjo0fQ.htxH7-7h3gq_q3ILAEl5GPYQSq_vZ0tUBWufmpJE_NY',
        'BSS_UDT': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6Im1hcmtldHBsYWNlc0BiZWxsYXZpdGFvcmdhbmljLmNvbSIsImZpcnN0TmFtZSI6IklEQU0gTmF0dXJhbCBXZWxsbmVzcyBQdnQgTHRkIiwibW9iaWxlIjoiOTgyMTU4ODk5NSIsInN0YXRlIjoiVkVSSUZJRUQiLCJ2YWxpZFNlc3Npb24iOnRydWUsInRlbmFudCI6IkJTUyIsImlhdCI6MTcxMDQzNzcyMCwiZXhwIjoxNzEwNDM4MzIwfQ.csXvVHe9ZdSIPY4qktwaOgBOIoDKHUt3UwezQ2XAxaE',
        'nonce': 'ss-3080163506',
    }

    for key in cook.keys():
        if key in cookies:
            cookies[key] = cook[key]


    headers = {
        'Accept-Language': 'en-US,en;q=0.9',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        # 'Cookie': 'T=TI169891842149300161944937865135939588577615020537527148270186391420; _pxvid=c6c61fc1-7964-11ee-8e5a-1d67ccbdf2e0; dpr=1.25; _fbp=fb.1.1700471257731.638459595; _ga_B9RGC9GN63=GS1.1.1702722512.1.1.1702722682.54.0.0; DID=clr1pup252bqp0x0wejpe1ajo; ULSN=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJjb29raWUiLCJhdWQiOiJmbGlwa2FydCIsImlzcyI6ImF1dGguZmxpcGthcnQuY29tIiwiY2xhaW1zIjp7ImdlbiI6IjEiLCJ1bmlxdWVJZCI6IlVVSTI0MDIxNDEyNTQxMjc4NE85TU9OTE0iLCJma0RldiI6bnVsbH0sImV4cCI6MTcyMzY3NTQ1MiwiaWF0IjoxNzA3ODk1NDUyLCJqdGkiOiIzZmIzYjAxZS02MzU2LTRjM2ItYTg3Yi1lNDQ3ZWNmMWJiYzEifQ.qbw3LDnvt96oOTYcrXvedJeOeJteVaWqgwkYlaKjyuw; vh=730; vw=1536; _ga_0RGM1K38MN=GS1.2.1708195526.2.1.1708195657.0.0.0; _ga_C00F4Q43Q7=GS1.2.1708196044.1.0.1708196044.0.0.0; _ga_2P94RMW04V=GS1.2.1708196121.6.1.1708196143.0.0.0; _gcl_au=1.1.856723108.1708257205; K-ACTION=null; ud=3.-hCuLDZfVJf9kwEcWhK4arj09yD35YGA9WD7yo1zRPr-6c1rmX2_xdHegqPpB3V8IXYz3NsAnP3SBWNaEKufBfykm01W9EISet6O__tpbwLut1-EZphHbJ0c9MzW0rczeRXhalfDVODMz8JTNMlQlgc9FtPFTSU9rNePFCXS_okASoEjAhPorkspIuB6dUcZtsYfTSEOj6D6fCfEhHGTX040PuZMdyiyk409VK7VDUArNQCXrRjfusSZdRR_dSa_IYardO48M5GyGz8FGpTkPTBYE_1zDB-5NXEc93lP2wklWoHEa-Dtp_7e6v2PvoLYEnO9q9WRO923E1MzbxEsgQzTal18ocz6m1QhVKcLAkifQY1CVPvSCEDYAhYysg7Cifn25pVGYReJE-wqKz__XeZKWQ6m9S5ylJWi8ZCNic_rQWkW8tl4jP7uwPxupbq0hBk3YeSRAVvcjX09zDY5qn4jmi-pJicw3oOin6BBwh5j4AEuCE1_UBhyu1FzQ6HXVin354_zqMKmt5Ez4awQztwLbxHMqBrzPLNw1nVv-mMH56A0UIV523BaT7wlgFXFKDY9PgZuquXJtkpqqSSPK3sdeoBmL_SsoP5XdHnW3U3lvtJigEiuV1-2In3wufWsqsHYvXC8tj7Vr6X8srs_3ehJ7eFh0ZMdB7QsQTCynabS2sW3gILSeLC2-NwmdaemzanTaScNERb6Z6uBV6aYgxLtiUZZci5cqwxPaCVTIRHxdKh90EtL6MagI-T8KaMNUkYxg3mOLw4UnS1OIQr5vw; AMCV_17EB401053DAF4840A490D4C%40AdobeOrg=-227196251%7CMCIDTS%7C19795%7CMCMID%7C88087235322683450901903204835359161911%7CMCAAMLH-1710338105%7C12%7CMCAAMB-1710813620%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1710216020s%7CNONE%7CMCAID%7CNONE; at=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjhlM2ZhMGE3LTJmZDMtNGNiMi05MWRjLTZlNTMxOGU1YTkxZiJ9.eyJleHAiOjE3MTAzMDM1MDEsImlhdCI6MTcxMDMwMTcwMSwiaXNzIjoia2V2bGFyIiwianRpIjoiOTgxYWNjOWMtZGE5MS00OTE2LThmYmMtOTUxMjNmNDQ5ODBhIiwidHlwZSI6IkFUIiwiZElkIjoiVEkxNjk4OTE4NDIxNDkzMDAxNjE5NDQ5Mzc4NjUxMzU5Mzk1ODg1Nzc2MTUwMjA1Mzc1MjcxNDgyNzAxODYzOTE0MjAiLCJiSWQiOiJTWVdVSloiLCJrZXZJZCI6IlZJNkM1MjJERkVERERCNDdCMDk0REJBQjhGQjgyNTM3Q0MiLCJ0SWQiOiJtYXBpIiwiZWFJZCI6IlNNdkZSa21lZkVqSWNQcmhSZVBXWk9keU1aTnFfSTdkUlYzQURGZ2t5TWUxbGljUTNJZ1M2UT09IiwidnMiOiJMSSIsInoiOiJIWUQiLCJtIjp0cnVlLCJnZW4iOjR9.M7iAS--yV9f2CqRxOyyIJSuo6jhjGKNV8WGE0qkaTW4; rt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjhlM2ZhMGE3LTJmZDMtNGNiMi05MWRjLTZlNTMxOGU1YTkxZiJ9.eyJleHAiOjE3MjYxOTkzMDEsImlhdCI6MTcxMDMwMTcwMSwiaXNzIjoia2V2bGFyIiwianRpIjoiNmFiMzM2ZTMtODhjYi00OTQ5LTljNTAtNWI2NTU0MDViOWI3IiwidHlwZSI6IlJUIiwiZElkIjoiVEkxNjk4OTE4NDIxNDkzMDAxNjE5NDQ5Mzc4NjUxMzU5Mzk1ODg1Nzc2MTUwMjA1Mzc1MjcxNDgyNzAxODYzOTE0MjAiLCJiSWQiOiJTWVdVSloiLCJrZXZJZCI6IlZJNkM1MjJERkVERERCNDdCMDk0REJBQjhGQjgyNTM3Q0MiLCJ0SWQiOiJtYXBpIiwibSI6eyJ0eXBlIjoibiJ9LCJ2IjoiQ1RBVVJMIn0.tlN-N45mURlkqikAoNxxXgtLFngU9XUnFR9OitBt7TY; vd=VI6C522DFEDDDB47B094DBAB8FB82537CC-1707110391153-43.1710301701.1710301701.161994701; S=d1t12fhAXNGc/P2M/ED8/Pz8YP5R1C2QLptKLX45nMO0fPoszL18MfCR2oiJUPJpcjVoXbOSe+gCGx2r6cyEFxAneSA==; SN=VI6C522DFEDDDB47B094DBAB8FB82537CC.TOK635F5023E626455C82262BA71755319E.1710301727.LI; _px3=05ac7a05aeac365311b734b3fcdc13a8fae35ecd6ef85f1a1cbb01a843d80b5b:mAQxF/myDQOiIQtg35ie6cHy+LrsyGhI3wgW51W1Po9iS7Qmd7YE9XnVEpK8FTgpVPEyOqpvuHQf5OfyFHJuRg==:1000:FztBa6xGQwRMA3en1v9VcblVQVug5PDlOHDwfTJ7pKFnXb1gKjSu7FaIFtYoWPqOoSlG6LSyW+SRwJhzXNMMUPBR9d/6rCA7so/FAgxo4J7pGweqiar8kRy/5Fn11peQE6L4IU5JumxFX444rq87mZVe+KNfM5yoDDYYYoUqCbDPZi01dMh/VtjiIz1lL/AFDCXVYY+Mjh26w5Mg+ig1G6P2gESj97G/6dx4VBLvMO0=; _gid=GA1.2.1420968950.1710404921; AMCV_55CFEDA0570C3FA17F000101%40AdobeOrg=-227196251%7CMCIDTS%7C19797%7CMCMID%7C83672356534473986601461754159478791217%7CMCAAMLH-1710923132%7C12%7CMCAAMB-1711023538%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1710425938s%7CNONE%7CMCAID%7CNONE; mp_9ea3bc9a23c575907407cf80efd56524_mixpanel=%7B%22distinct_id%22%3A%20%22ACCABA3F2470AD442FAA32E10D0E76B735F%22%2C%22%24device_id%22%3A%20%2218bf5c79f2b403-04403e63bfeec8-26031051-144000-18bf5c79f2ca33%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fseller.flipkart.com%2Fsell-online%2Fmulti-select%22%2C%22%24initial_referring_domain%22%3A%20%22seller.flipkart.com%22%2C%22%24user_id%22%3A%20%22ACCABA3F2470AD442FAA32E10D0E76B735F%22%2C%22%24search_engine%22%3A%20%22google%22%7D; _ga_0SJLGHBL81=GS1.1.1710418738.13.1.1710418799.0.0.0; _ga_TVF0VCMCT3=GS1.1.1710418738.134.1.1710418799.60.0.0; s_nr=1710418799593-Repeat; _ga=GA1.1.1819741834.1700633034; CURRENT_TENANT=BSS; _csrf=EmhbKG1CaciKlzp5J0JFI1tU; TENANT=BSS; _ga_ZPGRNTNNRT=GS1.1.1710434033.128.1.1710437614.0.0.0; BSS_SID=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjA1MGRjYzRjLTE0MGYtNDNkYy1iYTUzLTM2NTY3MTQ3MWVlZSJ9.eyJleHAiOjE3MTA0MzkzMzQsImlhdCI6MTcxMDQzNzUzNCwiaXNzIjoia2V2bGFyIiwianRpIjoiYTI5ZTM1YzYtYjQ0ZS00ZTRiLWEyZDItNDM2ZGI0ZTQ0NTYwIiwidHlwZSI6IkFUIiwiZElkIjoiY2xyMXB1cDI1MmJxcDB4MHdlanBlMWFqbyIsImJJZCI6IjRQVERTUSIsImtldklkIjoiVkkwRTY3N0NGOUI5RTM0QUE5OTI3N0IxNTkyOEE0NTJGRiIsInRJZCI6ImFkc191aSIsImVhSWQiOiJEelFjYkRsbnItWWJIaUhZVUpvT2JpdnNPUHk0bUhuOER6c2xLRkxYeUZsMTB0X3RweVdubmc9PSIsInZzIjoiTEkiLCJ6IjoiQ0giLCJtIjpmYWxzZSwiZ2VuIjo0fQ.htxH7-7h3gq_q3ILAEl5GPYQSq_vZ0tUBWufmpJE_NY; BSS_UDT=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6Im1hcmtldHBsYWNlc0BiZWxsYXZpdGFvcmdhbmljLmNvbSIsImZpcnN0TmFtZSI6IklEQU0gTmF0dXJhbCBXZWxsbmVzcyBQdnQgTHRkIiwibW9iaWxlIjoiOTgyMTU4ODk5NSIsInN0YXRlIjoiVkVSSUZJRUQiLCJ2YWxpZFNlc3Npb24iOnRydWUsInRlbmFudCI6IkJTUyIsImlhdCI6MTcxMDQzNzcyMCwiZXhwIjoxNzEwNDM4MzIwfQ.csXvVHe9ZdSIPY4qktwaOgBOIoDKHUt3UwezQ2XAxaE; nonce=ss-3080163506',
        'Origin': 'https://advertising.flipkart.com',
        'Pragma': 'no-cache',
        'Referer': 'https://advertising.flipkart.com/ad-account/campaigns/pla/HZOFVP2QQ57C/edit?baccount=N5J3WN87DKC4&aaccount=IZJL4R3KCMHR',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
        'accept': '*/*',
        'apollographql-client-name': 'Flipkart-Ads',
        'apollographql-client-version': '1.0.0',
        'content-type': 'application/json',
        'downlink': '10',
        'dpr': '1.25',
        'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'viewport-width': '911',
        'x-aaccount': 'IZJL4R3KCMHR',
        'x-baccount': 'N5J3WN87DKC4',
        'x-csrf-token': 'VelKlynI-ZDYQc8eFE5QM0eyl0SrvUS4nIaI',
        'x-sourceurl': 'https://advertising.flipkart.com/ad-account/campaigns/pla/HZOFVP2QQ57C/edit?baccount=N5J3WN87DKC4&aaccount=IZJL4R3KCMHR',
        'x-tenant': 'BSS',
    }

    json_data = {
        'operationName': 'GetCampaign',
        'variables': {
            'seller': False,
            'adProduct': 'BRAND_PLA',
            'id': 'HZOFVP2QQ57C',
        },
        'query': 'query GetCampaign($id: String!, $adProduct: String!, $seller: Boolean! = false) {\n  getCampaignForId(id: $id, adProduct: $adProduct) {\n    ... on CampaignPLAResponse {\n      campaignInfo {\n        id\n        type\n        name\n        status\n        uiStatus\n        currency\n        paymentType\n        budget\n        budgetType\n        fsnIds\n        startDate\n        endDate\n        costModel\n        marketplace\n        pacing\n        withPreferredSellers\n        preferredSellerIds\n        preferredSellerNames\n        businessZones\n        tillBudgetEnds\n        fsnMeta {\n          id\n          title\n          image\n          minListingPrice\n          maxListingPrice\n          listingCurrency\n          brand\n          storeList\n          __typename\n        }\n        __typename\n      }\n      adGroups {\n        id\n        name\n        status\n        productCount\n        commodityId\n        cost\n        budget\n        targeting {\n          type\n          pages\n          excludeKeywords {\n            q\n            r\n            __typename\n          }\n          includeKeywords {\n            q\n            r\n            matchType\n            __typename\n          }\n          __typename\n        }\n        storePaths\n        fsnBanners {\n          id\n          fsnId\n          __typename\n        }\n        costVariation {\n          ...PlacementsFragment\n          __typename\n        }\n        __typename\n      }\n      brandIds\n      preferredSellers {\n        alias\n        sellerId\n        __typename\n      }\n      placementsMetaInfo {\n        ...PlacementsMetaInfoFragement\n        __typename\n      }\n      __typename\n    }\n    ... on CampaignPCAResponse {\n      campaignInfo {\n        id\n        type\n        name\n        status\n        uiStatus\n        currency\n        paymentType\n        budget\n        budgetType\n        startDate\n        endDate\n        costModel\n        marketplace\n        __typename\n      }\n      adGroups {\n        id\n        name\n        status\n        uiStatus\n        startDate\n        endDate\n        cost\n        budget\n        excludeKeywords\n        marketplace\n        showAdInBroadMatchStores\n        costVariation {\n          ...PlacementsFragment\n          __typename\n        }\n        allowedActions\n        pacing\n        targeting {\n          type\n          pages\n          excludeKeywords {\n            q\n            r\n            __typename\n          }\n          includeKeywords {\n            q\n            r\n            matchType\n            __typename\n          }\n          __typename\n        }\n        contents {\n          contentId\n          creativeBanners {\n            creativeId\n            creativeName\n            creativeTemplateId\n            uiStatus\n            status\n            allowedActions\n            referenceId\n            mediaId\n            creativeType\n            assets {\n              macro\n              value\n              type\n              origin\n              assetId\n              subAssets {\n                macro\n                value\n                type\n                __typename\n              }\n              __typename\n            }\n            isSelected\n            id\n            language\n            __typename\n          }\n          collectionUrl\n          landingPageUrl\n          collectionId\n          collectionType\n          brands\n          stores {\n            storeId\n            storeName\n            __typename\n          }\n          rejectedCount\n          isPreferredSeller\n          creativeTemplateId\n          __typename\n        }\n        __typename\n      }\n      brandIds\n      placementsMetaInfo {\n        ...PlacementsMetaInfoFragement\n        __typename\n      }\n      __typename\n    }\n    ... on CampaignDisplayAdsResponse {\n      campaignInfo {\n        id\n        type\n        name\n        status\n        uiStatus\n        currency\n        paymentType\n        budget\n        startDate\n        endDate\n        costModel\n        marketplace\n        pacing\n        budgetType\n        adFormat\n        publisher\n        __typename\n      }\n      adGroups {\n        id\n        name\n        status\n        uiStatus\n        startDate\n        endDate\n        cost\n        budget\n        allowedActions\n        marketplace\n        pacing\n        contents {\n          contentId\n          creativeBanners {\n            creativeId\n            creativeName\n            uiStatus\n            status\n            allowedActions\n            referenceId\n            mediaId\n            videoMediaStatus\n            creativeType\n            assets {\n              macro\n              value\n              type\n              origin\n              subAssets {\n                macro\n                value\n                type\n                __typename\n              }\n              isSystemAsset\n              __typename\n            }\n            isSelected\n            id\n            __typename\n          }\n          collectionUrl\n          collectionId\n          collectionType\n          brands\n          stores {\n            storeId\n            storeName\n            __typename\n          }\n          rejectedCount\n          isUrlSystemCreated\n          landingPageUrl\n          status\n          isPreferredSeller\n          __typename\n        }\n        frequencyCapping {\n          interval\n          value\n          numberOfIntervals\n          __typename\n        }\n        customScheduling\n        channels\n        userTargetingExpression {\n          groupId\n          type\n          values\n          publisherSpecific\n          __typename\n        }\n        contextTargetingExpression {\n          groupId\n          type\n          values\n          publisherSpecific\n          __typename\n        }\n        __typename\n      }\n      brandIds\n      __typename\n    }\n    __typename\n  }\n  getAdAccountDetails @skip(if: $seller) {\n    marketplaceConfigurationResponse {\n      marketplaceList\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment PlacementsFragment on CostVariationType {\n  placements {\n    absoluteCost\n    percentage\n    type\n    pageType\n    __typename\n  }\n  __typename\n}\n\nfragment PlacementsMetaInfoFragement on PlacementsMeta {\n  type\n  title\n  detail\n  pageType\n  __typename\n}\n',
    }

    response = requests.post('https://advertising.flipkart.com/api', cookies=cookies, headers=headers, json=json_data)
    print(response.text)

    x = json.loads(response.text)
    names = (x["data"]["getCampaignForId"]["adGroups"][0]["name"])
    fsn_ids = (x["data"]["getCampaignForId"]["campaignInfo"]["fsnIds"])
    pla_pca = (x["data"]["getCampaignForId"]["campaignInfo"]["type"])
    name = (x["data"]["getCampaignForId"]["campaignInfo"]["name"])
    budget = (x["data"]["getCampaignForId"]["campaignInfo"]["budget"])
    start_date =  (x["data"]["getCampaignForId"]["campaignInfo"]["startDate"][:10])
    end_date = (x["data"]["getCampaignForId"]["campaignInfo"]["endDate"])
    cost_model = (x["data"]["getCampaignForId"]["campaignInfo"]["costModel"])
    ads_grps =  (x["data"]["getCampaignForId"]["adGroups"][0]["id"])
    cost =  (x["data"]["getCampaignForId"]["adGroups"][0]["cost"])
    store_path =  (x["data"]["getCampaignForId"]["adGroups"][0]["storePaths"])
    data  =  (x["data"]["getCampaignForId"]["adGroups"][0]["costVariation"]["placements"])

    placements = []

    for item in data:
        placement = {
            'absoluteCost': item['absoluteCost'],
            'type': item['type'],
            'percentage': item['percentage']
        }
        placements.append(placement)

    # print(name)


    headers = {
        'Accept-Language': 'en-US,en;q=0.9',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        # 'Cookie': 'T=TI169891842149300161944937865135939588577615020537527148270186391420; _pxvid=c6c61fc1-7964-11ee-8e5a-1d67ccbdf2e0; dpr=1.25; _fbp=fb.1.1700471257731.638459595; _ga_B9RGC9GN63=GS1.1.1702722512.1.1.1702722682.54.0.0; DID=clr1pup252bqp0x0wejpe1ajo; ULSN=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJjb29raWUiLCJhdWQiOiJmbGlwa2FydCIsImlzcyI6ImF1dGguZmxpcGthcnQuY29tIiwiY2xhaW1zIjp7ImdlbiI6IjEiLCJ1bmlxdWVJZCI6IlVVSTI0MDIxNDEyNTQxMjc4NE85TU9OTE0iLCJma0RldiI6bnVsbH0sImV4cCI6MTcyMzY3NTQ1MiwiaWF0IjoxNzA3ODk1NDUyLCJqdGkiOiIzZmIzYjAxZS02MzU2LTRjM2ItYTg3Yi1lNDQ3ZWNmMWJiYzEifQ.qbw3LDnvt96oOTYcrXvedJeOeJteVaWqgwkYlaKjyuw; vh=730; vw=1536; _ga_0RGM1K38MN=GS1.2.1708195526.2.1.1708195657.0.0.0; _ga_C00F4Q43Q7=GS1.2.1708196044.1.0.1708196044.0.0.0; _ga_2P94RMW04V=GS1.2.1708196121.6.1.1708196143.0.0.0; _gcl_au=1.1.856723108.1708257205; K-ACTION=null; ud=3.-hCuLDZfVJf9kwEcWhK4arj09yD35YGA9WD7yo1zRPr-6c1rmX2_xdHegqPpB3V8IXYz3NsAnP3SBWNaEKufBfykm01W9EISet6O__tpbwLut1-EZphHbJ0c9MzW0rczeRXhalfDVODMz8JTNMlQlgc9FtPFTSU9rNePFCXS_okASoEjAhPorkspIuB6dUcZtsYfTSEOj6D6fCfEhHGTX040PuZMdyiyk409VK7VDUArNQCXrRjfusSZdRR_dSa_IYardO48M5GyGz8FGpTkPTBYE_1zDB-5NXEc93lP2wklWoHEa-Dtp_7e6v2PvoLYEnO9q9WRO923E1MzbxEsgQzTal18ocz6m1QhVKcLAkifQY1CVPvSCEDYAhYysg7Cifn25pVGYReJE-wqKz__XeZKWQ6m9S5ylJWi8ZCNic_rQWkW8tl4jP7uwPxupbq0hBk3YeSRAVvcjX09zDY5qn4jmi-pJicw3oOin6BBwh5j4AEuCE1_UBhyu1FzQ6HXVin354_zqMKmt5Ez4awQztwLbxHMqBrzPLNw1nVv-mMH56A0UIV523BaT7wlgFXFKDY9PgZuquXJtkpqqSSPK3sdeoBmL_SsoP5XdHnW3U3lvtJigEiuV1-2In3wufWsqsHYvXC8tj7Vr6X8srs_3ehJ7eFh0ZMdB7QsQTCynabS2sW3gILSeLC2-NwmdaemzanTaScNERb6Z6uBV6aYgxLtiUZZci5cqwxPaCVTIRHxdKh90EtL6MagI-T8KaMNUkYxg3mOLw4UnS1OIQr5vw; AMCV_17EB401053DAF4840A490D4C%40AdobeOrg=-227196251%7CMCIDTS%7C19795%7CMCMID%7C88087235322683450901903204835359161911%7CMCAAMLH-1710338105%7C12%7CMCAAMB-1710813620%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1710216020s%7CNONE%7CMCAID%7CNONE; at=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjhlM2ZhMGE3LTJmZDMtNGNiMi05MWRjLTZlNTMxOGU1YTkxZiJ9.eyJleHAiOjE3MTAzMDM1MDEsImlhdCI6MTcxMDMwMTcwMSwiaXNzIjoia2V2bGFyIiwianRpIjoiOTgxYWNjOWMtZGE5MS00OTE2LThmYmMtOTUxMjNmNDQ5ODBhIiwidHlwZSI6IkFUIiwiZElkIjoiVEkxNjk4OTE4NDIxNDkzMDAxNjE5NDQ5Mzc4NjUxMzU5Mzk1ODg1Nzc2MTUwMjA1Mzc1MjcxNDgyNzAxODYzOTE0MjAiLCJiSWQiOiJTWVdVSloiLCJrZXZJZCI6IlZJNkM1MjJERkVERERCNDdCMDk0REJBQjhGQjgyNTM3Q0MiLCJ0SWQiOiJtYXBpIiwiZWFJZCI6IlNNdkZSa21lZkVqSWNQcmhSZVBXWk9keU1aTnFfSTdkUlYzQURGZ2t5TWUxbGljUTNJZ1M2UT09IiwidnMiOiJMSSIsInoiOiJIWUQiLCJtIjp0cnVlLCJnZW4iOjR9.M7iAS--yV9f2CqRxOyyIJSuo6jhjGKNV8WGE0qkaTW4; rt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjhlM2ZhMGE3LTJmZDMtNGNiMi05MWRjLTZlNTMxOGU1YTkxZiJ9.eyJleHAiOjE3MjYxOTkzMDEsImlhdCI6MTcxMDMwMTcwMSwiaXNzIjoia2V2bGFyIiwianRpIjoiNmFiMzM2ZTMtODhjYi00OTQ5LTljNTAtNWI2NTU0MDViOWI3IiwidHlwZSI6IlJUIiwiZElkIjoiVEkxNjk4OTE4NDIxNDkzMDAxNjE5NDQ5Mzc4NjUxMzU5Mzk1ODg1Nzc2MTUwMjA1Mzc1MjcxNDgyNzAxODYzOTE0MjAiLCJiSWQiOiJTWVdVSloiLCJrZXZJZCI6IlZJNkM1MjJERkVERERCNDdCMDk0REJBQjhGQjgyNTM3Q0MiLCJ0SWQiOiJtYXBpIiwibSI6eyJ0eXBlIjoibiJ9LCJ2IjoiQ1RBVVJMIn0.tlN-N45mURlkqikAoNxxXgtLFngU9XUnFR9OitBt7TY; vd=VI6C522DFEDDDB47B094DBAB8FB82537CC-1707110391153-43.1710301701.1710301701.161994701; S=d1t12fhAXNGc/P2M/ED8/Pz8YP5R1C2QLptKLX45nMO0fPoszL18MfCR2oiJUPJpcjVoXbOSe+gCGx2r6cyEFxAneSA==; SN=VI6C522DFEDDDB47B094DBAB8FB82537CC.TOK635F5023E626455C82262BA71755319E.1710301727.LI; _px3=05ac7a05aeac365311b734b3fcdc13a8fae35ecd6ef85f1a1cbb01a843d80b5b:mAQxF/myDQOiIQtg35ie6cHy+LrsyGhI3wgW51W1Po9iS7Qmd7YE9XnVEpK8FTgpVPEyOqpvuHQf5OfyFHJuRg==:1000:FztBa6xGQwRMA3en1v9VcblVQVug5PDlOHDwfTJ7pKFnXb1gKjSu7FaIFtYoWPqOoSlG6LSyW+SRwJhzXNMMUPBR9d/6rCA7so/FAgxo4J7pGweqiar8kRy/5Fn11peQE6L4IU5JumxFX444rq87mZVe+KNfM5yoDDYYYoUqCbDPZi01dMh/VtjiIz1lL/AFDCXVYY+Mjh26w5Mg+ig1G6P2gESj97G/6dx4VBLvMO0=; _gid=GA1.2.1420968950.1710404921; AMCV_55CFEDA0570C3FA17F000101%40AdobeOrg=-227196251%7CMCIDTS%7C19797%7CMCMID%7C83672356534473986601461754159478791217%7CMCAAMLH-1710923132%7C12%7CMCAAMB-1711023538%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1710425938s%7CNONE%7CMCAID%7CNONE; mp_9ea3bc9a23c575907407cf80efd56524_mixpanel=%7B%22distinct_id%22%3A%20%22ACCABA3F2470AD442FAA32E10D0E76B735F%22%2C%22%24device_id%22%3A%20%2218bf5c79f2b403-04403e63bfeec8-26031051-144000-18bf5c79f2ca33%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fseller.flipkart.com%2Fsell-online%2Fmulti-select%22%2C%22%24initial_referring_domain%22%3A%20%22seller.flipkart.com%22%2C%22%24user_id%22%3A%20%22ACCABA3F2470AD442FAA32E10D0E76B735F%22%2C%22%24search_engine%22%3A%20%22google%22%7D; _ga_0SJLGHBL81=GS1.1.1710418738.13.1.1710418799.0.0.0; _ga_TVF0VCMCT3=GS1.1.1710418738.134.1.1710418799.60.0.0; s_nr=1710418799593-Repeat; _ga=GA1.1.1819741834.1700633034; CURRENT_TENANT=BSS; _csrf=EmhbKG1CaciKlzp5J0JFI1tU; TENANT=BSS; BSS_SID=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImQxZWI3YWU1LTllNmUtNGMxNi04ZjM1LTVlYWJhOGNiYzMyZCJ9.eyJleHAiOjE3MTA0MzgxODMsImlhdCI6MTcxMDQzNjM4MywiaXNzIjoia2V2bGFyIiwianRpIjoiMDM0NDQ0Y2UtMDZkNi00Njc2LTk0MDItOTU0OTUyN2M1YTZmIiwidHlwZSI6IkFUIiwiZElkIjoiY2xyMXB1cDI1MmJxcDB4MHdlanBlMWFqbyIsImJJZCI6IjZHSUhMTiIsImtldklkIjoiVkkwRTY3N0NGOUI5RTM0QUE5OTI3N0IxNTkyOEE0NTJGRiIsInRJZCI6ImFkc191aSIsImVhSWQiOiJEYmh3SlVVcVZ6eVJQX2RLZHJQSFhkSUl1X3hxOEVuS0VJWXA1Sjd3d2x4aTFadnJsQ2pqTFE9PSIsInZzIjoiTEkiLCJ6IjoiQ0giLCJtIjpmYWxzZSwiZ2VuIjo0fQ.mgrhrwFHxEJUz8-pv23mIuKQf52XCWmYT0cAEAntjbw; BSS_UDT=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6Im1hcmtldHBsYWNlc0BiZWxsYXZpdGFvcmdhbmljLmNvbSIsImZpcnN0TmFtZSI6IklEQU0gTmF0dXJhbCBXZWxsbmVzcyBQdnQgTHRkIiwibW9iaWxlIjoiOTgyMTU4ODk5NSIsInN0YXRlIjoiVkVSSUZJRUQiLCJ2YWxpZFNlc3Npb24iOnRydWUsInRlbmFudCI6IkJTUyIsImlhdCI6MTcxMDQzNzEwOSwiZXhwIjoxNzEwNDM3NzA5fQ.hEK-g_UtwLYJKP9ARESVZiUFtKzG18m4r4jConbRQ54; nonce=ss-1076996115; _ga_ZPGRNTNNRT=GS1.1.1710434033.128.1.1710437607.0.0.0',
        'Origin': 'https://advertising.flipkart.com',
        'Pragma': 'no-cache',
        'Referer': 'https://advertising.flipkart.com/ad-account/campaigns/pla/HZOFVP2QQ57C/edit?baccount=N5J3WN87DKC4&aaccount=IZJL4R3KCMHR&step=3',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
        'accept': '*/*',
        'apollographql-client-name': 'Flipkart-Ads',
        'apollographql-client-version': '1.0.0',
        'content-type': 'application/json',
        'downlink': '10',
        'dpr': '1.25',
        'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'viewport-width': '911',
        'x-aaccount': 'IZJL4R3KCMHR',
        'x-baccount': 'N5J3WN87DKC4',
        'x-csrf-token': 'VelKlynI-ZDYQc8eFE5QM0eyl0SrvUS4nIaI',
        'x-sourceurl': 'https://advertising.flipkart.com/ad-account/campaigns/pla/HZOFVP2QQ57C/edit?baccount=N5J3WN87DKC4&aaccount=IZJL4R3KCMHR&step=3',
        'x-tenant': 'BSS',
    }

    json_data = {
        'operationName': 'UpdateCampaign',
        'variables': {
            'data': {
                'campaignInfo': {
                    'type': pla_pca,
                    'name': name,
                    'budget': budget,
                    'budgetType': 'TOTAL_BUDGET',
                    'startDate': 1710324537000,
                    'endDate': end_date,
                    'costModel': cost_model,
                    'pacing': 'NONE',
                    'fsnIds':fsn_ids,
                    'marketplace': 'FLIPKART',
                    'preferredSellerIds': [],
                    'withPreferredSellers': False,
                },
                'adGroups': [
                    {
                        'id': ads_grps,
                        'name': names,
                        'commodityId': 509,
                        'costModel': cost_model,
                        'cost': cost,
                        'budget': None,
                        'costVariation': {
                            'placements': placements,
                        },
                        'storePaths': [
                            'g9b/ema/5la/yzb/',
                        ],
                        'targeting': [
                            {
                                'type': 'PAGE_TARGETING',
                                'pages': [
                                    'HOMEPAGE',
                                    'SEARCH_PAGE',
                                    'BROWSE_PAGE',
                                    'PRODUCT_PAGE',
                                ],
                                'excludeKeywords': None,
                                'includeKeywords': None,
                            },
                        ],
                        'fsnIds': fsn_ids,
                    },
                ],
            },
            'id': 'HZOFVP2QQ57C',
        },
        'query': 'mutation UpdateCampaign($data: SavePLACampaignPayload!, $id: String!) {\n  updatePLACampaign(data: $data, id: $id) {\n    ...CampaignPLAFragment\n    __typename\n  }\n}\n\nfragment CampaignPLAFragment on CampaignPLAResponse {\n  campaignInfo {\n    id\n    type\n    paymentType\n    currency\n    costModel\n    pacing\n    status\n    uiStatus\n    marketplace\n    name\n    budget\n    grossBudget\n    budgetType\n    startDate\n    endDate\n    allowedActions\n    __typename\n  }\n  adGroups {\n    id\n    name\n    status\n    productCount\n    commodityId\n    cost\n    budget\n    targeting {\n      type\n      pages\n      excludeKeywords {\n        q\n        r\n        __typename\n      }\n      includeKeywords {\n        q\n        r\n        matchType\n        __typename\n      }\n      __typename\n    }\n    storePaths\n    fsnBanners {\n      id\n      fsnId\n      __typename\n    }\n    costVariation {\n      ...PlacementsFragment\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment PlacementsFragment on CostVariationType {\n  placements {\n    absoluteCost\n    percentage\n    type\n    pageType\n    __typename\n  }\n  __typename\n}\n',
    }

    response = requests.post('https://advertising.flipkart.com/api', cookies=cookies, headers=headers, json=json_data)
    print(response.text)


# master_command(cookie_generator()[0])