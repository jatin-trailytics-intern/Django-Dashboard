import numpy as np
import requests
import json
import pandas as pd
import requests
# from channel import *

def payloadcampagins(cookie_dict={}, start_date='2024-01-01', end_date='2024-02-01'):
    cookies_x = {
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
    'CURRENT_TENANT': 'BSS',
    'AMCV_17EB401053DAF4840A490D4C%40AdobeOrg': '-227196251%7CMCIDTS%7C19795%7CMCMID%7C88087235322683450901903204835359161911%7CMCAAMLH-1710338105%7C12%7CMCAAMB-1710813620%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1710216020s%7CNONE%7CMCAID%7CNONE',
    'AMCV_55CFEDA0570C3FA17F000101%40AdobeOrg': '-227196251%7CMCIDTS%7C19795%7CMCMID%7C83672356534473986601461754159478791217%7CMCAAMLH-1710315071%7C12%7CMCAAMB-1710814295%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1710216695s%7CNONE%7CMCAID%7CNONE',
    'mp_9ea3bc9a23c575907407cf80efd56524_mixpanel': '%7B%22distinct_id%22%3A%20%22ACCABA3F2470AD442FAA32E10D0E76B735F%22%2C%22%24device_id%22%3A%20%2218bf5c79f2b403-04403e63bfeec8-26031051-144000-18bf5c79f2ca33%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fseller.flipkart.com%2Fsell-online%2Fmulti-select%22%2C%22%24initial_referring_domain%22%3A%20%22seller.flipkart.com%22%2C%22%24user_id%22%3A%20%22ACCABA3F2470AD442FAA32E10D0E76B735F%22%2C%22%24search_engine%22%3A%20%22google%22%7D',
    's_nr': '1710209518900-Repeat',
    '_ga': 'GA1.1.1819741834.1700633034',
    '_ga_TVF0VCMCT3': 'GS1.1.1710209487.129.1.1710209519.28.0.0',
    '_ga_0SJLGHBL81': 'GS1.1.1710209487.8.1.1710209519.0.0.0',
    'at': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjhlM2ZhMGE3LTJmZDMtNGNiMi05MWRjLTZlNTMxOGU1YTkxZiJ9.eyJleHAiOjE3MTAzMDM1MDEsImlhdCI6MTcxMDMwMTcwMSwiaXNzIjoia2V2bGFyIiwianRpIjoiOTgxYWNjOWMtZGE5MS00OTE2LThmYmMtOTUxMjNmNDQ5ODBhIiwidHlwZSI6IkFUIiwiZElkIjoiVEkxNjk4OTE4NDIxNDkzMDAxNjE5NDQ5Mzc4NjUxMzU5Mzk1ODg1Nzc2MTUwMjA1Mzc1MjcxNDgyNzAxODYzOTE0MjAiLCJiSWQiOiJTWVdVSloiLCJrZXZJZCI6IlZJNkM1MjJERkVERERCNDdCMDk0REJBQjhGQjgyNTM3Q0MiLCJ0SWQiOiJtYXBpIiwiZWFJZCI6IlNNdkZSa21lZkVqSWNQcmhSZVBXWk9keU1aTnFfSTdkUlYzQURGZ2t5TWUxbGljUTNJZ1M2UT09IiwidnMiOiJMSSIsInoiOiJIWUQiLCJtIjp0cnVlLCJnZW4iOjR9.M7iAS--yV9f2CqRxOyyIJSuo6jhjGKNV8WGE0qkaTW4',
    'rt': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjhlM2ZhMGE3LTJmZDMtNGNiMi05MWRjLTZlNTMxOGU1YTkxZiJ9.eyJleHAiOjE3MjYxOTkzMDEsImlhdCI6MTcxMDMwMTcwMSwiaXNzIjoia2V2bGFyIiwianRpIjoiNmFiMzM2ZTMtODhjYi00OTQ5LTljNTAtNWI2NTU0MDViOWI3IiwidHlwZSI6IlJUIiwiZElkIjoiVEkxNjk4OTE4NDIxNDkzMDAxNjE5NDQ5Mzc4NjUxMzU5Mzk1ODg1Nzc2MTUwMjA1Mzc1MjcxNDgyNzAxODYzOTE0MjAiLCJiSWQiOiJTWVdVSloiLCJrZXZJZCI6IlZJNkM1MjJERkVERERCNDdCMDk0REJBQjhGQjgyNTM3Q0MiLCJ0SWQiOiJtYXBpIiwibSI6eyJ0eXBlIjoibiJ9LCJ2IjoiQ1RBVVJMIn0.tlN-N45mURlkqikAoNxxXgtLFngU9XUnFR9OitBt7TY',
    'vd': 'VI6C522DFEDDDB47B094DBAB8FB82537CC-1707110391153-43.1710301701.1710301701.161994701',
    'S': 'd1t12fhAXNGc/P2M/ED8/Pz8YP5R1C2QLptKLX45nMO0fPoszL18MfCR2oiJUPJpcjVoXbOSe+gCGx2r6cyEFxAneSA==',
    'SN': 'VI6C522DFEDDDB47B094DBAB8FB82537CC.TOK635F5023E626455C82262BA71755319E.1710301727.LI',
    '_px3': '05ac7a05aeac365311b734b3fcdc13a8fae35ecd6ef85f1a1cbb01a843d80b5b:mAQxF/myDQOiIQtg35ie6cHy+LrsyGhI3wgW51W1Po9iS7Qmd7YE9XnVEpK8FTgpVPEyOqpvuHQf5OfyFHJuRg==:1000:FztBa6xGQwRMA3en1v9VcblVQVug5PDlOHDwfTJ7pKFnXb1gKjSu7FaIFtYoWPqOoSlG6LSyW+SRwJhzXNMMUPBR9d/6rCA7so/FAgxo4J7pGweqiar8kRy/5Fn11peQE6L4IU5JumxFX444rq87mZVe+KNfM5yoDDYYYoUqCbDPZi01dMh/VtjiIz1lL/AFDCXVYY+Mjh26w5Mg+ig1G6P2gESj97G/6dx4VBLvMO0=',
    '_csrf': 'Dig_KL5UbbPl-gxLUasdkDjC',
    'TENANT': 'BSS',
    'BSS_SID': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImQxZWI3YWU1LTllNmUtNGMxNi04ZjM1LTVlYWJhOGNiYzMyZCJ9.eyJleHAiOjE3MTAzMTM2MjYsImlhdCI6MTcxMDMxMTgyNiwiaXNzIjoia2V2bGFyIiwianRpIjoiYWNmYTVjY2MtYWI5MS00ZDAxLTk4YWItYjJmM2YzMjM3Y2RlIiwidHlwZSI6IkFUIiwiZElkIjoiY2xyMXB1cDI1MmJxcDB4MHdlanBlMWFqbyIsImJJZCI6Ik9RMElPOCIsImtldklkIjoiVklBMDE4Mzc0MDEwMDQ0RkMyODFGNjRGMENEMkZEMUJEQSIsInRJZCI6ImFkc191aSIsImVhSWQiOiJEYmh3SlVVcVZ6eVJQX2RLZHJQSFhkSUl1X3hxOEVuS0VJWXA1Sjd3d2x4aTFadnJsQ2pqTFE9PSIsInZzIjoiTEkiLCJ6IjoiQ0giLCJtIjpmYWxzZSwiZ2VuIjo0fQ.hsnXMITkXvjNYFKuZzp7HtlsY2c16McmbkmC5Rkol94',
    'BSS_UDT': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6Im1hcmtldHBsYWNlc0BiZWxsYXZpdGFvcmdhbmljLmNvbSIsImZpcnN0TmFtZSI6IklEQU0gTmF0dXJhbCBXZWxsbmVzcyBQdnQgTHRkIiwibW9iaWxlIjoiOTgyMTU4ODk5NSIsInN0YXRlIjoiVkVSSUZJRUQiLCJ2YWxpZFNlc3Npb24iOnRydWUsInRlbmFudCI6IkJTUyIsImlhdCI6MTcxMDMxMjQyNiwiZXhwIjoxNzEwMzEzMDI2fQ.DFSXiLiOd_GK5fGauJBtHEHFIS4w31-FUUXz9GW7ubg',
    '_ga_ZPGRNTNNRT': 'GS1.1.1710311721.114.1.1710312793.0.0.0',
    'nonce': 'ss-3785664152',
    }

    for key in cookie_dict.keys():
        if key in cookies_x:
            cookies_x[key] = cookie_dict[key]


    headers = {
        'Accept-Language': 'en-US,en;q=0.9',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        # 'Cookie': 'T=TI169891842149300161944937865135939588577615020537527148270186391420; _pxvid=c6c61fc1-7964-11ee-8e5a-1d67ccbdf2e0; dpr=1.25; _fbp=fb.1.1700471257731.638459595; _ga_B9RGC9GN63=GS1.1.1702722512.1.1.1702722682.54.0.0; DID=clr1pup252bqp0x0wejpe1ajo; ULSN=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJjb29raWUiLCJhdWQiOiJmbGlwa2FydCIsImlzcyI6ImF1dGguZmxpcGthcnQuY29tIiwiY2xhaW1zIjp7ImdlbiI6IjEiLCJ1bmlxdWVJZCI6IlVVSTI0MDIxNDEyNTQxMjc4NE85TU9OTE0iLCJma0RldiI6bnVsbH0sImV4cCI6MTcyMzY3NTQ1MiwiaWF0IjoxNzA3ODk1NDUyLCJqdGkiOiIzZmIzYjAxZS02MzU2LTRjM2ItYTg3Yi1lNDQ3ZWNmMWJiYzEifQ.qbw3LDnvt96oOTYcrXvedJeOeJteVaWqgwkYlaKjyuw; vh=730; vw=1536; _ga_0RGM1K38MN=GS1.2.1708195526.2.1.1708195657.0.0.0; _ga_C00F4Q43Q7=GS1.2.1708196044.1.0.1708196044.0.0.0; _ga_2P94RMW04V=GS1.2.1708196121.6.1.1708196143.0.0.0; _gcl_au=1.1.856723108.1708257205; K-ACTION=null; ud=3.-hCuLDZfVJf9kwEcWhK4arj09yD35YGA9WD7yo1zRPr-6c1rmX2_xdHegqPpB3V8IXYz3NsAnP3SBWNaEKufBfykm01W9EISet6O__tpbwLut1-EZphHbJ0c9MzW0rczeRXhalfDVODMz8JTNMlQlgc9FtPFTSU9rNePFCXS_okASoEjAhPorkspIuB6dUcZtsYfTSEOj6D6fCfEhHGTX040PuZMdyiyk409VK7VDUArNQCXrRjfusSZdRR_dSa_IYardO48M5GyGz8FGpTkPTBYE_1zDB-5NXEc93lP2wklWoHEa-Dtp_7e6v2PvoLYEnO9q9WRO923E1MzbxEsgQzTal18ocz6m1QhVKcLAkifQY1CVPvSCEDYAhYysg7Cifn25pVGYReJE-wqKz__XeZKWQ6m9S5ylJWi8ZCNic_rQWkW8tl4jP7uwPxupbq0hBk3YeSRAVvcjX09zDY5qn4jmi-pJicw3oOin6BBwh5j4AEuCE1_UBhyu1FzQ6HXVin354_zqMKmt5Ez4awQztwLbxHMqBrzPLNw1nVv-mMH56A0UIV523BaT7wlgFXFKDY9PgZuquXJtkpqqSSPK3sdeoBmL_SsoP5XdHnW3U3lvtJigEiuV1-2In3wufWsqsHYvXC8tj7Vr6X8srs_3ehJ7eFh0ZMdB7QsQTCynabS2sW3gILSeLC2-NwmdaemzanTaScNERb6Z6uBV6aYgxLtiUZZci5cqwxPaCVTIRHxdKh90EtL6MagI-T8KaMNUkYxg3mOLw4UnS1OIQr5vw; CURRENT_TENANT=BSS; AMCV_17EB401053DAF4840A490D4C%40AdobeOrg=-227196251%7CMCIDTS%7C19795%7CMCMID%7C88087235322683450901903204835359161911%7CMCAAMLH-1710338105%7C12%7CMCAAMB-1710813620%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1710216020s%7CNONE%7CMCAID%7CNONE; AMCV_55CFEDA0570C3FA17F000101%40AdobeOrg=-227196251%7CMCIDTS%7C19795%7CMCMID%7C83672356534473986601461754159478791217%7CMCAAMLH-1710315071%7C12%7CMCAAMB-1710814295%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1710216695s%7CNONE%7CMCAID%7CNONE; mp_9ea3bc9a23c575907407cf80efd56524_mixpanel=%7B%22distinct_id%22%3A%20%22ACCABA3F2470AD442FAA32E10D0E76B735F%22%2C%22%24device_id%22%3A%20%2218bf5c79f2b403-04403e63bfeec8-26031051-144000-18bf5c79f2ca33%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fseller.flipkart.com%2Fsell-online%2Fmulti-select%22%2C%22%24initial_referring_domain%22%3A%20%22seller.flipkart.com%22%2C%22%24user_id%22%3A%20%22ACCABA3F2470AD442FAA32E10D0E76B735F%22%2C%22%24search_engine%22%3A%20%22google%22%7D; s_nr=1710209518900-Repeat; _ga=GA1.1.1819741834.1700633034; _ga_TVF0VCMCT3=GS1.1.1710209487.129.1.1710209519.28.0.0; _ga_0SJLGHBL81=GS1.1.1710209487.8.1.1710209519.0.0.0; at=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjhlM2ZhMGE3LTJmZDMtNGNiMi05MWRjLTZlNTMxOGU1YTkxZiJ9.eyJleHAiOjE3MTAzMDM1MDEsImlhdCI6MTcxMDMwMTcwMSwiaXNzIjoia2V2bGFyIiwianRpIjoiOTgxYWNjOWMtZGE5MS00OTE2LThmYmMtOTUxMjNmNDQ5ODBhIiwidHlwZSI6IkFUIiwiZElkIjoiVEkxNjk4OTE4NDIxNDkzMDAxNjE5NDQ5Mzc4NjUxMzU5Mzk1ODg1Nzc2MTUwMjA1Mzc1MjcxNDgyNzAxODYzOTE0MjAiLCJiSWQiOiJTWVdVSloiLCJrZXZJZCI6IlZJNkM1MjJERkVERERCNDdCMDk0REJBQjhGQjgyNTM3Q0MiLCJ0SWQiOiJtYXBpIiwiZWFJZCI6IlNNdkZSa21lZkVqSWNQcmhSZVBXWk9keU1aTnFfSTdkUlYzQURGZ2t5TWUxbGljUTNJZ1M2UT09IiwidnMiOiJMSSIsInoiOiJIWUQiLCJtIjp0cnVlLCJnZW4iOjR9.M7iAS--yV9f2CqRxOyyIJSuo6jhjGKNV8WGE0qkaTW4; rt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjhlM2ZhMGE3LTJmZDMtNGNiMi05MWRjLTZlNTMxOGU1YTkxZiJ9.eyJleHAiOjE3MjYxOTkzMDEsImlhdCI6MTcxMDMwMTcwMSwiaXNzIjoia2V2bGFyIiwianRpIjoiNmFiMzM2ZTMtODhjYi00OTQ5LTljNTAtNWI2NTU0MDViOWI3IiwidHlwZSI6IlJUIiwiZElkIjoiVEkxNjk4OTE4NDIxNDkzMDAxNjE5NDQ5Mzc4NjUxMzU5Mzk1ODg1Nzc2MTUwMjA1Mzc1MjcxNDgyNzAxODYzOTE0MjAiLCJiSWQiOiJTWVdVSloiLCJrZXZJZCI6IlZJNkM1MjJERkVERERCNDdCMDk0REJBQjhGQjgyNTM3Q0MiLCJ0SWQiOiJtYXBpIiwibSI6eyJ0eXBlIjoibiJ9LCJ2IjoiQ1RBVVJMIn0.tlN-N45mURlkqikAoNxxXgtLFngU9XUnFR9OitBt7TY; vd=VI6C522DFEDDDB47B094DBAB8FB82537CC-1707110391153-43.1710301701.1710301701.161994701; S=d1t12fhAXNGc/P2M/ED8/Pz8YP5R1C2QLptKLX45nMO0fPoszL18MfCR2oiJUPJpcjVoXbOSe+gCGx2r6cyEFxAneSA==; SN=VI6C522DFEDDDB47B094DBAB8FB82537CC.TOK635F5023E626455C82262BA71755319E.1710301727.LI; _px3=05ac7a05aeac365311b734b3fcdc13a8fae35ecd6ef85f1a1cbb01a843d80b5b:mAQxF/myDQOiIQtg35ie6cHy+LrsyGhI3wgW51W1Po9iS7Qmd7YE9XnVEpK8FTgpVPEyOqpvuHQf5OfyFHJuRg==:1000:FztBa6xGQwRMA3en1v9VcblVQVug5PDlOHDwfTJ7pKFnXb1gKjSu7FaIFtYoWPqOoSlG6LSyW+SRwJhzXNMMUPBR9d/6rCA7so/FAgxo4J7pGweqiar8kRy/5Fn11peQE6L4IU5JumxFX444rq87mZVe+KNfM5yoDDYYYoUqCbDPZi01dMh/VtjiIz1lL/AFDCXVYY+Mjh26w5Mg+ig1G6P2gESj97G/6dx4VBLvMO0=; _csrf=Dig_KL5UbbPl-gxLUasdkDjC; TENANT=BSS; BSS_SID=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImQxZWI3YWU1LTllNmUtNGMxNi04ZjM1LTVlYWJhOGNiYzMyZCJ9.eyJleHAiOjE3MTAzMTM2MjYsImlhdCI6MTcxMDMxMTgyNiwiaXNzIjoia2V2bGFyIiwianRpIjoiYWNmYTVjY2MtYWI5MS00ZDAxLTk4YWItYjJmM2YzMjM3Y2RlIiwidHlwZSI6IkFUIiwiZElkIjoiY2xyMXB1cDI1MmJxcDB4MHdlanBlMWFqbyIsImJJZCI6Ik9RMElPOCIsImtldklkIjoiVklBMDE4Mzc0MDEwMDQ0RkMyODFGNjRGMENEMkZEMUJEQSIsInRJZCI6ImFkc191aSIsImVhSWQiOiJEYmh3SlVVcVZ6eVJQX2RLZHJQSFhkSUl1X3hxOEVuS0VJWXA1Sjd3d2x4aTFadnJsQ2pqTFE9PSIsInZzIjoiTEkiLCJ6IjoiQ0giLCJtIjpmYWxzZSwiZ2VuIjo0fQ.hsnXMITkXvjNYFKuZzp7HtlsY2c16McmbkmC5Rkol94; BSS_UDT=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6Im1hcmtldHBsYWNlc0BiZWxsYXZpdGFvcmdhbmljLmNvbSIsImZpcnN0TmFtZSI6IklEQU0gTmF0dXJhbCBXZWxsbmVzcyBQdnQgTHRkIiwibW9iaWxlIjoiOTgyMTU4ODk5NSIsInN0YXRlIjoiVkVSSUZJRUQiLCJ2YWxpZFNlc3Npb24iOnRydWUsInRlbmFudCI6IkJTUyIsImlhdCI6MTcxMDMxMjQyNiwiZXhwIjoxNzEwMzEzMDI2fQ.DFSXiLiOd_GK5fGauJBtHEHFIS4w31-FUUXz9GW7ubg; _ga_ZPGRNTNNRT=GS1.1.1710311721.114.1.1710312793.0.0.0; nonce=ss-3785664152',
        'Origin': 'https://advertising.flipkart.com',
        'Pragma': 'no-cache',
        'Referer': 'https://advertising.flipkart.com/ad-account/campaigns?baccount=N5J3WN87DKC&aaccount=IZJL4R3KCMHR',
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
        'viewport-width': '1035',
        'x-aaccount': 'IZJL4R3KCMHR',
        'x-baccount': 'N5J3WN87DKC4',
        'x-csrf-token': '67bDcVfG-6HoWluDoQ65BPLanquLWaQhXxTs',
        'x-sourceurl': 'https://advertising.flipkart.com/ad-account/campaigns?baccount=N5J3WN87DKC4&aaccount=IZJL4R3KCMHR',
        'x-tenant': 'BSS',
    }

    json_data = {
    'operationName': 'GetConsolidatedCampaignReport',
    'variables': {
        'dateRange': {
            'endDate': '2024-03-16',
            'startDate': '2024-03-02',
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

    response = requests.post('https://advertising.flipkart.com/api', cookies=cookies_x, headers=headers, json=json_data)

    # Note: json_data will not be serialized by requests
    # exactly as it was in the original request.
    #data = '{"operationName":"GetConsolidatedCampaignReport","variables":{"dateRange":{"endDate":"2024-03-13","startDate":"2024-02-28"},"pageLevelFilter":[],"queries":[{"query":{"filters":[{"comparator":["IZJL4R3KCMHR"],"field":{"entity_type":"DIMENSION","function":"VALUE","name":"advertiser_id"},"operator":"IN","view_id":"671"}],"group_by":[{"function":"VALUE","name":"campaign_id"},{"function":"VALUE","name":"campaign_start_and_end_date"},{"function":"VALUE","name":"campaign_budget"},{"function":"VALUE","name":"campaign_name"},{"function":"VALUE","name":"advertiser_id"},{"function":"VALUE","name":"campaign_status"},{"function":"VALUE","name":"campaign_type"},{"function":"VALUE","name":"campaign_start_date"},{"function":"VALUE","name":"campaign_end_date"},{"function":"VALUE","name":"marketplace"},{"function":"VALUE","name":"campaign_budget_type"}],"metrics":[{"function":"SUM","name":"cost"},{"function":"SUM","name":"remaining_budget"},{"function":"SUM","name":"views"},{"function":"SUM","name":"clicks"},{"function":"VALUE","name":"total_converted_units"},{"function":"VALUE","name":"total_converted_revenue"},{"function":"VALUE","name":"roi"},{"function":"VALUE","name":"CTR"},{"function":"VALUE","name":"cvr"},{"function":"VALUE","name":"campaign_allowed_actions"}],"order_by":{"fields":[{"entity_type":"METRIC","function":"SUM","name":"views"}],"type":"DESC"},"page_size":600,"type":"TABULAR","view_id":"671"},"queryId":"tabular-123"}],"requestId":"1234","timeGranularity":"DAY","adProducts":["BRAND_PLA","BRAND_PCA","BRAND_DISPLAY_ADS"],"marketPlaces":["FLIPKART","GROCERY"]},"query":"query GetConsolidatedCampaignReport($dateRange: URFDateRange!, $timeGranularity: String, $budgetRecommended: Boolean, $requestId: ID!, $pageLevelFilter: [URFFilter!]!, $queries: [URFQuerySet!]!, $adProducts: [String!]!, $marketPlaces: [String!]!) {\\n  getConsolidatedCampaignReport(dateRange: $dateRange, timeGranularity: $timeGranularity, budgetRecommended: $budgetRecommended, requestId: $requestId, pageLevelFilter: $pageLevelFilter, queries: $queries, adProducts: $adProducts, marketPlaces: $marketPlaces) {\\n    code\\n    columns {\\n      entityType\\n      name\\n      type\\n      metadata {\\n        HAS_MULTISOURCE\\n        __typename\\n      }\\n      __typename\\n    }\\n    rows {\\n      values\\n      __typename\\n    }\\n    __typename\\n  }\\n}\\n"}'
    #response = requests.post('https://advertising.flipkart.com/api', cookies=cookies, headers=headers, data=data)
    x = json.loads(response.text)

    rows = x.get("data", {}).get("getConsolidatedCampaignReport").get('rows')
    columns = x.get("data", {}).get("getConsolidatedCampaignReport").get("columns")
    column = []
    for i in columns:
        column.append(i["name"])

    # Add 'status' column to the list of columns
    column.append("status")

    df = pd.DataFrame(columns=column)

    for i in rows:
        new_row = i["values"]
        # Determine status value based on 'campaign status'
        status = 1 if new_row[column.index("campaign_status")] == "LIVE" else 0
        # Append status value to the new row
        new_row.append(status)
        # Add new row to the DataFrame
        df.loc[len(df)] = new_row

    # print(df)
    df = df.fillna(value=np.nan)
    df = df.replace(np.nan, 0)
    data = {}
    data['campaign_status'] = df['campaign_status'].values.tolist()
    data['campaign_name'] = df['campaign_name'].values.tolist()
    data['campaign_start_and_end_date'] = df['campaign_start_and_end_date'].values.tolist()
    data['campaign_type'] = df['campaign_type'].values.tolist()
    data['campaign_id'] = df['campaign_id'].values.tolist()
    data['campaign_budget'] = df['campaign_budget'].values.tolist()
    data['CTR'] = df['CTR'].values.tolist()
    data['Cost'] = df['cost'].values.tolist()
    data['total_converted_revenue'] = df['total_converted_revenue'].values.tolist()
    data['clicks'] = df['clicks'].values.tolist()
    data['total_converted_units'] = df['total_converted_units'].values.tolist()
    data['roi'] = df['roi'].values.tolist()
    data['views'] = df['views'].values.tolist()
    data['cvr'] = df['cvr'].values.tolist()
    data['Actions'] = df['campaign_allowed_actions'].values.tolist()
    a = df['status'].values.tolist()
    data['cpstatus'] = ["ENABLED" if i==1 else "DISABLED" for i in a]


 

    packet = []
    for i in range(len(data['campaign_status'])):
        packet.append({ k:data[k][i] for k in data.keys() })
    # print(packet)
    return packet



# payloadcampagins(cookie_generator()[0])
