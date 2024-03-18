import requests
from corescripts.channel import *
import argparse


parser = argparse.ArgumentParser(description='campagin details')
parser.add_argument('--p1', action="store", dest='para1', default="")
parser.add_argument('--p2', action="store", dest='para2', default="")
parser.add_argument('--p3', action="store", dest='para3', default="")
parser.add_argument('--p4', action="store", dest='para4', default="")

args = parser.parse_args()

print(args.para1, args.para2, args.para3, args.para4)

def pauseplay_campagins(cookie_dict={}, acttion=args.para1, adproduct=args.para2, entity=args.para3, cid=args.para4):
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
        'AMCV_17EB401053DAF4840A490D4C%40AdobeOrg': '-227196251%7CMCIDTS%7C19795%7CMCMID%7C88087235322683450901903204835359161911%7CMCAAMLH-1710338105%7C12%7CMCAAMB-1710813620%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1710216020s%7CNONE%7CMCAID%7CNONE',
        'at': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjhlM2ZhMGE3LTJmZDMtNGNiMi05MWRjLTZlNTMxOGU1YTkxZiJ9.eyJleHAiOjE3MTAzMDM1MDEsImlhdCI6MTcxMDMwMTcwMSwiaXNzIjoia2V2bGFyIiwianRpIjoiOTgxYWNjOWMtZGE5MS00OTE2LThmYmMtOTUxMjNmNDQ5ODBhIiwidHlwZSI6IkFUIiwiZElkIjoiVEkxNjk4OTE4NDIxNDkzMDAxNjE5NDQ5Mzc4NjUxMzU5Mzk1ODg1Nzc2MTUwMjA1Mzc1MjcxNDgyNzAxODYzOTE0MjAiLCJiSWQiOiJTWVdVSloiLCJrZXZJZCI6IlZJNkM1MjJERkVERERCNDdCMDk0REJBQjhGQjgyNTM3Q0MiLCJ0SWQiOiJtYXBpIiwiZWFJZCI6IlNNdkZSa21lZkVqSWNQcmhSZVBXWk9keU1aTnFfSTdkUlYzQURGZ2t5TWUxbGljUTNJZ1M2UT09IiwidnMiOiJMSSIsInoiOiJIWUQiLCJtIjp0cnVlLCJnZW4iOjR9.M7iAS--yV9f2CqRxOyyIJSuo6jhjGKNV8WGE0qkaTW4',
        'rt': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjhlM2ZhMGE3LTJmZDMtNGNiMi05MWRjLTZlNTMxOGU1YTkxZiJ9.eyJleHAiOjE3MjYxOTkzMDEsImlhdCI6MTcxMDMwMTcwMSwiaXNzIjoia2V2bGFyIiwianRpIjoiNmFiMzM2ZTMtODhjYi00OTQ5LTljNTAtNWI2NTU0MDViOWI3IiwidHlwZSI6IlJUIiwiZElkIjoiVEkxNjk4OTE4NDIxNDkzMDAxNjE5NDQ5Mzc4NjUxMzU5Mzk1ODg1Nzc2MTUwMjA1Mzc1MjcxNDgyNzAxODYzOTE0MjAiLCJiSWQiOiJTWVdVSloiLCJrZXZJZCI6IlZJNkM1MjJERkVERERCNDdCMDk0REJBQjhGQjgyNTM3Q0MiLCJ0SWQiOiJtYXBpIiwibSI6eyJ0eXBlIjoibiJ9LCJ2IjoiQ1RBVVJMIn0.tlN-N45mURlkqikAoNxxXgtLFngU9XUnFR9OitBt7TY',
        'vd': 'VI6C522DFEDDDB47B094DBAB8FB82537CC-1707110391153-43.1710301701.1710301701.161994701',
        'S': 'd1t12fhAXNGc/P2M/ED8/Pz8YP5R1C2QLptKLX45nMO0fPoszL18MfCR2oiJUPJpcjVoXbOSe+gCGx2r6cyEFxAneSA==',
        'SN': 'VI6C522DFEDDDB47B094DBAB8FB82537CC.TOK635F5023E626455C82262BA71755319E.1710301727.LI',
        '_px3': '05ac7a05aeac365311b734b3fcdc13a8fae35ecd6ef85f1a1cbb01a843d80b5b:mAQxF/myDQOiIQtg35ie6cHy+LrsyGhI3wgW51W1Po9iS7Qmd7YE9XnVEpK8FTgpVPEyOqpvuHQf5OfyFHJuRg==:1000:FztBa6xGQwRMA3en1v9VcblVQVug5PDlOHDwfTJ7pKFnXb1gKjSu7FaIFtYoWPqOoSlG6LSyW+SRwJhzXNMMUPBR9d/6rCA7so/FAgxo4J7pGweqiar8kRy/5Fn11peQE6L4IU5JumxFX444rq87mZVe+KNfM5yoDDYYYoUqCbDPZi01dMh/VtjiIz1lL/AFDCXVYY+Mjh26w5Mg+ig1G6P2gESj97G/6dx4VBLvMO0=',
        'CURRENT_TENANT': 'BSS',
        '_gid': 'GA1.2.1420968950.1710404921',
        'moe_uuid': '2b61a549-6d9c-4c19-9ab4-f2a5c0a7ed90',
        'AMCVS_55CFEDA0570C3FA17F000101%40AdobeOrg': '1',
        'AMCV_55CFEDA0570C3FA17F000101%40AdobeOrg': '-227196251%7CMCIDTS%7C19797%7CMCMID%7C83672356534473986601461754159478791217%7CMCAAMLH-1710923132%7C12%7CMCAAMB-1711013654%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1710416054s%7CNONE%7CMCAID%7CNONE',
        's_cc': 'true',
        's_ppvl': 'seller%253A%2520home%2520page%2C100%2C100%2C730%2C1536%2C730%2C1536%2C864%2C1.25%2CP',
        's_ppv': 'seller%253A%2520home%2520page%2C100%2C100%2C730%2C1536%2C730%2C1536%2C864%2C1.25%2CP',
        's_sq': 'flipkartsellerprod%3D%2526c.%2526a.%2526activitymap.%2526page%253Dseller%25253A%252520home%252520page%2526link%253DRequest%252520Download%2526region%253Dearn-more-report-download%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253Dseller%25253A%252520home%252520page%2526pidt%253D1%2526oid%253DfunctionBr%252528%252529%25257B%25257D%2526oidt%253D2%2526ot%253DSUBMIT',
        'mp_9ea3bc9a23c575907407cf80efd56524_mixpanel': '%7B%22distinct_id%22%3A%20%22ACCABA3F2470AD442FAA32E10D0E76B735F%22%2C%22%24device_id%22%3A%20%2218bf5c79f2b403-04403e63bfeec8-26031051-144000-18bf5c79f2ca33%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fseller.flipkart.com%2Fsell-online%2Fmulti-select%22%2C%22%24initial_referring_domain%22%3A%20%22seller.flipkart.com%22%2C%22%24user_id%22%3A%20%22ACCABA3F2470AD442FAA32E10D0E76B735F%22%2C%22%24search_engine%22%3A%20%22google%22%7D',
        '_ga_TVF0VCMCT3': 'GS1.1.1710414053.133.0.1710414053.60.0.0',
        '_ga_0SJLGHBL81': 'GS1.1.1710414053.12.0.1710414053.0.0.0',
        's_nr': '1710414053406-Repeat',
        '_csrf': 'Q7TZBrJqdG376S_evdIcdazT',
        'TENANT': 'BSS',
        'BSS_SID': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImQxZWI3YWU1LTllNmUtNGMxNi04ZjM1LTVlYWJhOGNiYzMyZCJ9.eyJleHAiOjE3MTA0MTU4NTUsImlhdCI6MTcxMDQxNDA1NSwiaXNzIjoia2V2bGFyIiwianRpIjoiNmQwYTI0MmUtODI2Yi00NGIwLWI3OTEtZGMxNWIwYjA5MjVkIiwidHlwZSI6IkFUIiwiZElkIjoiY2xyMXB1cDI1MmJxcDB4MHdlanBlMWFqbyIsImJJZCI6IllKU042ViIsImtldklkIjoiVkk4ODY0RUNGQThCNzg0MjdFQUM2ODBCODkzRDM0NzQ2NyIsInRJZCI6ImFkc191aSIsImVhSWQiOiJEYmh3SlVVcVZ6eVJQX2RLZHJQSFhkSUl1X3hxOEVuS0VJWXA1Sjd3d2x4aTFadnJsQ2pqTFE9PSIsInZzIjoiTEkiLCJ6IjoiQ0giLCJtIjpmYWxzZSwiZ2VuIjo0fQ.JHXOAX0CtvSErJ11-qE_tL6P411aPLw8Drl6icVdRQE',
        '_ga': 'GA1.1.1819741834.1700633034',
        '_ga_ZPGRNTNNRT': 'GS1.1.1710414056.123.1.1710414201.0.0.0',
        'BSS_UDT': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6Im1hcmtldHBsYWNlc0BiZWxsYXZpdGFvcmdhbmljLmNvbSIsImZpcnN0TmFtZSI6IklEQU0gTmF0dXJhbCBXZWxsbmVzcyBQdnQgTHRkIiwibW9iaWxlIjoiOTgyMTU4ODk5NSIsInN0YXRlIjoiVkVSSUZJRUQiLCJ2YWxpZFNlc3Npb24iOnRydWUsInRlbmFudCI6IkJTUyIsImlhdCI6MTcxMDQxNDY4OSwiZXhwIjoxNzEwNDE1Mjg5fQ.Z6lqIzGYXy0A1P8rd7wjjA35bgo0UeMaJXJvqlubsSU',
        'nonce': 'ss-3695559003',
    }

    for key in cookie_dict.keys():
        if key in cookies_x:
            cookies_x[key] = cookie_dict[key]


    headers = {
        'Accept-Language': 'en-US,en;q=0.9',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        # 'Cookie': 'T=TI169891842149300161944937865135939588577615020537527148270186391420; _pxvid=c6c61fc1-7964-11ee-8e5a-1d67ccbdf2e0; dpr=1.25; _fbp=fb.1.1700471257731.638459595; _ga_B9RGC9GN63=GS1.1.1702722512.1.1.1702722682.54.0.0; DID=clr1pup252bqp0x0wejpe1ajo; ULSN=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJjb29raWUiLCJhdWQiOiJmbGlwa2FydCIsImlzcyI6ImF1dGguZmxpcGthcnQuY29tIiwiY2xhaW1zIjp7ImdlbiI6IjEiLCJ1bmlxdWVJZCI6IlVVSTI0MDIxNDEyNTQxMjc4NE85TU9OTE0iLCJma0RldiI6bnVsbH0sImV4cCI6MTcyMzY3NTQ1MiwiaWF0IjoxNzA3ODk1NDUyLCJqdGkiOiIzZmIzYjAxZS02MzU2LTRjM2ItYTg3Yi1lNDQ3ZWNmMWJiYzEifQ.qbw3LDnvt96oOTYcrXvedJeOeJteVaWqgwkYlaKjyuw; vh=730; vw=1536; _ga_0RGM1K38MN=GS1.2.1708195526.2.1.1708195657.0.0.0; _ga_C00F4Q43Q7=GS1.2.1708196044.1.0.1708196044.0.0.0; _ga_2P94RMW04V=GS1.2.1708196121.6.1.1708196143.0.0.0; _gcl_au=1.1.856723108.1708257205; K-ACTION=null; ud=3.-hCuLDZfVJf9kwEcWhK4arj09yD35YGA9WD7yo1zRPr-6c1rmX2_xdHegqPpB3V8IXYz3NsAnP3SBWNaEKufBfykm01W9EISet6O__tpbwLut1-EZphHbJ0c9MzW0rczeRXhalfDVODMz8JTNMlQlgc9FtPFTSU9rNePFCXS_okASoEjAhPorkspIuB6dUcZtsYfTSEOj6D6fCfEhHGTX040PuZMdyiyk409VK7VDUArNQCXrRjfusSZdRR_dSa_IYardO48M5GyGz8FGpTkPTBYE_1zDB-5NXEc93lP2wklWoHEa-Dtp_7e6v2PvoLYEnO9q9WRO923E1MzbxEsgQzTal18ocz6m1QhVKcLAkifQY1CVPvSCEDYAhYysg7Cifn25pVGYReJE-wqKz__XeZKWQ6m9S5ylJWi8ZCNic_rQWkW8tl4jP7uwPxupbq0hBk3YeSRAVvcjX09zDY5qn4jmi-pJicw3oOin6BBwh5j4AEuCE1_UBhyu1FzQ6HXVin354_zqMKmt5Ez4awQztwLbxHMqBrzPLNw1nVv-mMH56A0UIV523BaT7wlgFXFKDY9PgZuquXJtkpqqSSPK3sdeoBmL_SsoP5XdHnW3U3lvtJigEiuV1-2In3wufWsqsHYvXC8tj7Vr6X8srs_3ehJ7eFh0ZMdB7QsQTCynabS2sW3gILSeLC2-NwmdaemzanTaScNERb6Z6uBV6aYgxLtiUZZci5cqwxPaCVTIRHxdKh90EtL6MagI-T8KaMNUkYxg3mOLw4UnS1OIQr5vw; AMCV_17EB401053DAF4840A490D4C%40AdobeOrg=-227196251%7CMCIDTS%7C19795%7CMCMID%7C88087235322683450901903204835359161911%7CMCAAMLH-1710338105%7C12%7CMCAAMB-1710813620%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1710216020s%7CNONE%7CMCAID%7CNONE; at=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjhlM2ZhMGE3LTJmZDMtNGNiMi05MWRjLTZlNTMxOGU1YTkxZiJ9.eyJleHAiOjE3MTAzMDM1MDEsImlhdCI6MTcxMDMwMTcwMSwiaXNzIjoia2V2bGFyIiwianRpIjoiOTgxYWNjOWMtZGE5MS00OTE2LThmYmMtOTUxMjNmNDQ5ODBhIiwidHlwZSI6IkFUIiwiZElkIjoiVEkxNjk4OTE4NDIxNDkzMDAxNjE5NDQ5Mzc4NjUxMzU5Mzk1ODg1Nzc2MTUwMjA1Mzc1MjcxNDgyNzAxODYzOTE0MjAiLCJiSWQiOiJTWVdVSloiLCJrZXZJZCI6IlZJNkM1MjJERkVERERCNDdCMDk0REJBQjhGQjgyNTM3Q0MiLCJ0SWQiOiJtYXBpIiwiZWFJZCI6IlNNdkZSa21lZkVqSWNQcmhSZVBXWk9keU1aTnFfSTdkUlYzQURGZ2t5TWUxbGljUTNJZ1M2UT09IiwidnMiOiJMSSIsInoiOiJIWUQiLCJtIjp0cnVlLCJnZW4iOjR9.M7iAS--yV9f2CqRxOyyIJSuo6jhjGKNV8WGE0qkaTW4; rt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjhlM2ZhMGE3LTJmZDMtNGNiMi05MWRjLTZlNTMxOGU1YTkxZiJ9.eyJleHAiOjE3MjYxOTkzMDEsImlhdCI6MTcxMDMwMTcwMSwiaXNzIjoia2V2bGFyIiwianRpIjoiNmFiMzM2ZTMtODhjYi00OTQ5LTljNTAtNWI2NTU0MDViOWI3IiwidHlwZSI6IlJUIiwiZElkIjoiVEkxNjk4OTE4NDIxNDkzMDAxNjE5NDQ5Mzc4NjUxMzU5Mzk1ODg1Nzc2MTUwMjA1Mzc1MjcxNDgyNzAxODYzOTE0MjAiLCJiSWQiOiJTWVdVSloiLCJrZXZJZCI6IlZJNkM1MjJERkVERERCNDdCMDk0REJBQjhGQjgyNTM3Q0MiLCJ0SWQiOiJtYXBpIiwibSI6eyJ0eXBlIjoibiJ9LCJ2IjoiQ1RBVVJMIn0.tlN-N45mURlkqikAoNxxXgtLFngU9XUnFR9OitBt7TY; vd=VI6C522DFEDDDB47B094DBAB8FB82537CC-1707110391153-43.1710301701.1710301701.161994701; S=d1t12fhAXNGc/P2M/ED8/Pz8YP5R1C2QLptKLX45nMO0fPoszL18MfCR2oiJUPJpcjVoXbOSe+gCGx2r6cyEFxAneSA==; SN=VI6C522DFEDDDB47B094DBAB8FB82537CC.TOK635F5023E626455C82262BA71755319E.1710301727.LI; _px3=05ac7a05aeac365311b734b3fcdc13a8fae35ecd6ef85f1a1cbb01a843d80b5b:mAQxF/myDQOiIQtg35ie6cHy+LrsyGhI3wgW51W1Po9iS7Qmd7YE9XnVEpK8FTgpVPEyOqpvuHQf5OfyFHJuRg==:1000:FztBa6xGQwRMA3en1v9VcblVQVug5PDlOHDwfTJ7pKFnXb1gKjSu7FaIFtYoWPqOoSlG6LSyW+SRwJhzXNMMUPBR9d/6rCA7so/FAgxo4J7pGweqiar8kRy/5Fn11peQE6L4IU5JumxFX444rq87mZVe+KNfM5yoDDYYYoUqCbDPZi01dMh/VtjiIz1lL/AFDCXVYY+Mjh26w5Mg+ig1G6P2gESj97G/6dx4VBLvMO0=; CURRENT_TENANT=BSS; _gid=GA1.2.1420968950.1710404921; moe_uuid=2b61a549-6d9c-4c19-9ab4-f2a5c0a7ed90; AMCVS_55CFEDA0570C3FA17F000101%40AdobeOrg=1; AMCV_55CFEDA0570C3FA17F000101%40AdobeOrg=-227196251%7CMCIDTS%7C19797%7CMCMID%7C83672356534473986601461754159478791217%7CMCAAMLH-1710923132%7C12%7CMCAAMB-1711013654%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1710416054s%7CNONE%7CMCAID%7CNONE; s_cc=true; s_ppvl=seller%253A%2520home%2520page%2C100%2C100%2C730%2C1536%2C730%2C1536%2C864%2C1.25%2CP; s_ppv=seller%253A%2520home%2520page%2C100%2C100%2C730%2C1536%2C730%2C1536%2C864%2C1.25%2CP; s_sq=flipkartsellerprod%3D%2526c.%2526a.%2526activitymap.%2526page%253Dseller%25253A%252520home%252520page%2526link%253DRequest%252520Download%2526region%253Dearn-more-report-download%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253Dseller%25253A%252520home%252520page%2526pidt%253D1%2526oid%253DfunctionBr%252528%252529%25257B%25257D%2526oidt%253D2%2526ot%253DSUBMIT; mp_9ea3bc9a23c575907407cf80efd56524_mixpanel=%7B%22distinct_id%22%3A%20%22ACCABA3F2470AD442FAA32E10D0E76B735F%22%2C%22%24device_id%22%3A%20%2218bf5c79f2b403-04403e63bfeec8-26031051-144000-18bf5c79f2ca33%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fseller.flipkart.com%2Fsell-online%2Fmulti-select%22%2C%22%24initial_referring_domain%22%3A%20%22seller.flipkart.com%22%2C%22%24user_id%22%3A%20%22ACCABA3F2470AD442FAA32E10D0E76B735F%22%2C%22%24search_engine%22%3A%20%22google%22%7D; _ga_TVF0VCMCT3=GS1.1.1710414053.133.0.1710414053.60.0.0; _ga_0SJLGHBL81=GS1.1.1710414053.12.0.1710414053.0.0.0; s_nr=1710414053406-Repeat; _csrf=Q7TZBrJqdG376S_evdIcdazT; TENANT=BSS; BSS_SID=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImQxZWI3YWU1LTllNmUtNGMxNi04ZjM1LTVlYWJhOGNiYzMyZCJ9.eyJleHAiOjE3MTA0MTU4NTUsImlhdCI6MTcxMDQxNDA1NSwiaXNzIjoia2V2bGFyIiwianRpIjoiNmQwYTI0MmUtODI2Yi00NGIwLWI3OTEtZGMxNWIwYjA5MjVkIiwidHlwZSI6IkFUIiwiZElkIjoiY2xyMXB1cDI1MmJxcDB4MHdlanBlMWFqbyIsImJJZCI6IllKU042ViIsImtldklkIjoiVkk4ODY0RUNGQThCNzg0MjdFQUM2ODBCODkzRDM0NzQ2NyIsInRJZCI6ImFkc191aSIsImVhSWQiOiJEYmh3SlVVcVZ6eVJQX2RLZHJQSFhkSUl1X3hxOEVuS0VJWXA1Sjd3d2x4aTFadnJsQ2pqTFE9PSIsInZzIjoiTEkiLCJ6IjoiQ0giLCJtIjpmYWxzZSwiZ2VuIjo0fQ.JHXOAX0CtvSErJ11-qE_tL6P411aPLw8Drl6icVdRQE; _ga=GA1.1.1819741834.1700633034; _ga_ZPGRNTNNRT=GS1.1.1710414056.123.1.1710414201.0.0.0; BSS_UDT=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6Im1hcmtldHBsYWNlc0BiZWxsYXZpdGFvcmdhbmljLmNvbSIsImZpcnN0TmFtZSI6IklEQU0gTmF0dXJhbCBXZWxsbmVzcyBQdnQgTHRkIiwibW9iaWxlIjoiOTgyMTU4ODk5NSIsInN0YXRlIjoiVkVSSUZJRUQiLCJ2YWxpZFNlc3Npb24iOnRydWUsInRlbmFudCI6IkJTUyIsImlhdCI6MTcxMDQxNDY4OSwiZXhwIjoxNzEwNDE1Mjg5fQ.Z6lqIzGYXy0A1P8rd7wjjA35bgo0UeMaJXJvqlubsSU; nonce=ss-3695559003',
        'Origin': 'https://advertising.flipkart.com',
        'Pragma': 'no-cache',
        'Referer': 'https://advertising.flipkart.com/ad-account/campaigns?baccount=N5J3WN87DKC4&aaccount=IZJL4R3KCMHR',
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
        'x-csrf-token': 'rdtggAIL-89fWQudM_Zrxai8B4t5h4EDtZ30',
        'x-sourceurl': 'https://advertising.flipkart.com/ad-account/campaigns?baccount=N5J3WN87DKC4&aaccount=IZJL4R3KCMHR',
        'x-tenant': 'BSS',
    }

    json_data = {
        'operationName': 'quickActionCampaignList',
        'variables': {
            # 'action': 'USER_RESUME',
            # 'adProduct': 'BRAND_PLA',
            # 'entity': 'campaign',
            # 'id': 'HZOFVP2QQ57C',
            'action': acttion,
            'adProduct': adproduct,
            'entity': entity,
            'id': cid,
        },
        'query': 'mutation quickActionCampaignList($id: String!, $action: String!, $entity: String!, $adProduct: String!) {\n  quickActionCampaignList(id: $id, action: $action, entity: $entity, adProduct: $adProduct) {\n    success\n    error\n    id\n    uiStatus\n    allowedActions\n    status\n    displayError\n    __typename\n  }\n}\n',
    }

    print(json_data)
    response = requests.post('https://advertising.flipkart.com/api', cookies=cookies_x, headers=headers, json=json_data)
    print(response.text)


pauseplay_campagins(cookie_generator()[0])



















    # Note: json_data will not be serialized by requests
    # exactly as it was in the original request.
    #data = '{"operationName":"quickActionCampaignList","variables":{"action":"USER_RESUME","adProduct":"BRAND_PLA","entity":"campaign","id":"HZOFVP2QQ57C"},"query":"mutation quickActionCampaignList($id: String!, $action: String!, $entity: String!, $adProduct: String!) {\\n  quickActionCampaignList(id: $id, action: $action, entity: $entity, adProduct: $adProduct) {\\n    success\\n    error\\n    id\\n    uiStatus\\n    allowedActions\\n    status\\n    displayError\\n    __typename\\n  }\\n}\\n"}'
    #response = requests.post('https://advertising.flipkart.com/api', cookies=cookies, headers=headers, data=data)