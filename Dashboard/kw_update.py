import requests
import json
import pymysql

DB_HOST = "tr-wp-database.cfqdq6ohjn0p.us-east-1.rds.amazonaws.com"
DB_USER = "shivam"
DB_PASSWORD = "Trailytics@789"
DB_DATABASE =  "amazon_ads_api"
DB_PORT = 3306
connection = pymysql.connect(
    host=DB_HOST,
    user=DB_USER,
    password=DB_PASSWORD,
    db=DB_DATABASE,
    port=DB_PORT,
    connect_timeout=1000,
    autocommit=True
)

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
    'CURRENT_TENANT': 'BSS',
    'AMCV_17EB401053DAF4840A490D4C%40AdobeOrg': '-227196251%7CMCIDTS%7C19803%7CMCMID%7C88087235322683450901903204835359161911%7CMCAAMLH-1711370283%7C12%7CMCAAMB-1711535846%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1710938246s%7CNONE%7CMCAID%7CNONE',
    'S': 'd1t12P2AkKQt9Ez8/fT8PP2k/RaqC3I0GSWMIuvetzRFw0i+4DygShEPYXDFPp3GYoMnuXXBNqttLBucCv3X8kr/htg==',
    'at': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjNhNzdlZTgxLTRjNWYtNGU5Ni04ZmRlLWM3YWMyYjVlOTA1NSJ9.eyJleHAiOjE3MTA5NDMwMDIsImlhdCI6MTcxMDk0MTIwMiwiaXNzIjoia2V2bGFyIiwianRpIjoiYjRjOTAwMWEtZWYzOS00OTQ4LTlmZTQtZjkzY2Q2YmQyYzE0IiwidHlwZSI6IkFUIiwiZElkIjoiVEkxNjk4OTE4NDIxNDkzMDAxNjE5NDQ5Mzc4NjUxMzU5Mzk1ODg1Nzc2MTUwMjA1Mzc1MjcxNDgyNzAxODYzOTE0MjAiLCJiSWQiOiJXMVE2TkwiLCJrZXZJZCI6IlZJNkM1MjJERkVERERCNDdCMDk0REJBQjhGQjgyNTM3Q0MiLCJ0SWQiOiJtYXBpIiwiZWFJZCI6ImJlMHVRSWdQSVRwMlpxYW5OTmhobkdIamhSdi1QMVhOTmNURnloQS16QVNBWU40QlZ2NF9Odz09IiwidnMiOiJMSSIsInoiOiJIWUQiLCJtIjp0cnVlLCJnZW4iOjR9.SPHHwfWdG4P6zfLs0NJZPZVMHm2MU3uFcsq4dh0PgjY',
    'rt': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjNhNzdlZTgxLTRjNWYtNGU5Ni04ZmRlLWM3YWMyYjVlOTA1NSJ9.eyJleHAiOjE3MjY4Mzg4MDIsImlhdCI6MTcxMDk0MTIwMiwiaXNzIjoia2V2bGFyIiwianRpIjoiM2Q3MzI0NDEtMGEyZi00Y2FjLTk1MjQtZDZiNzU2ZmVkYmE4IiwidHlwZSI6IlJUIiwiZElkIjoiVEkxNjk4OTE4NDIxNDkzMDAxNjE5NDQ5Mzc4NjUxMzU5Mzk1ODg1Nzc2MTUwMjA1Mzc1MjcxNDgyNzAxODYzOTE0MjAiLCJiSWQiOiJXMVE2TkwiLCJrZXZJZCI6IlZJNkM1MjJERkVERERCNDdCMDk0REJBQjhGQjgyNTM3Q0MiLCJ0SWQiOiJtYXBpIiwibSI6eyJ0eXBlIjoibiJ9LCJ2IjoiQ0dPS0tBIn0.0i7wLqxD-9cOQ5NK-C2YS92LPWrwiM77QLnc0HcaKnU',
    'vd': 'VI6C522DFEDDDB47B094DBAB8FB82537CC-1707110391153-46.1710941202.1710941202.162220005',
    'SN': 'VI6C522DFEDDDB47B094DBAB8FB82537CC.TOK635F5023E626455C82262BA71755319E.1710941210.LI',
    '_px3': '7e81b72a8d81f65048b2e580804a9906c2c2fb26fde4c7aabd214bcb1ed0a25a:i6m859ehtdI3oDAbiEJ3MsMpIEtgSxV8e57zfiA/XA0mkavG72n5wgXcjaC6IRyumQ0tiVe8ENKlq1HObq4TPA==:1000:vo7aCy8Bx7RFZ0YQiBSsD3rHhMmaxiMa8wueHGloRUHyTRrTQYfaDC0okTf98vbrHJc8BC7dZpvYxFyqe6zn8y/IxKzX6pfEmaP/Sllyu0B19OF2a2W1ghVOyn0pJAjoVZq9FOn4OWKO+bxZFXQyRerjoFi14FmgKBqNBy9K6RGWeiKVFVrbfxpdYtLwLuBTVeQWa7WWGI8iAZmwIVJ4+i7zsIW+qyrujWub4AF5pEo=',
    'AMCV_55CFEDA0570C3FA17F000101%40AdobeOrg': '-227196251%7CMCIDTS%7C19804%7CMCMID%7C83672356534473986601461754159478791217%7CMCAAMLH-1711603203%7C12%7CMCAAMB-1711603203%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1711005603s%7CNONE%7CMCAID%7CNONE',
    'mp_9ea3bc9a23c575907407cf80efd56524_mixpanel': '%7B%22distinct_id%22%3A%20%22ACCABA3F2470AD442FAA32E10D0E76B735F%22%2C%22%24device_id%22%3A%20%2218bf5c79f2b403-04403e63bfeec8-26031051-144000-18bf5c79f2ca33%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fseller.flipkart.com%2Fsell-online%2Fmulti-select%22%2C%22%24initial_referring_domain%22%3A%20%22seller.flipkart.com%22%2C%22%24user_id%22%3A%20%22ACCABA3F2470AD442FAA32E10D0E76B735F%22%2C%22%24search_engine%22%3A%20%22google%22%7D',
    '_ga': 'GA1.1.1819741834.1700633034',
    '_ga_TVF0VCMCT3': 'GS1.1.1710998391.145.1.1710998431.20.0.0',
    '_ga_0SJLGHBL81': 'GS1.1.1710998391.24.1.1710998431.0.0.0',
    's_nr': '1710998431595-Repeat',
    '_csrf': '91qWeSw-th1diAv6F4OTYv20',
    'TENANT': 'BSS',
    'BSS_SID': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImQxZWI3YWU1LTllNmUtNGMxNi04ZjM1LTVlYWJhOGNiYzMyZCJ9.eyJleHAiOjE3MTExMjQ1OTMsImlhdCI6MTcxMTEyMjc5MywiaXNzIjoia2V2bGFyIiwianRpIjoiMGFjYThhYmUtMTAyOS00N2NjLWFjZjMtODBmMGZlMmE2MTU5IiwidHlwZSI6IkFUIiwiZElkIjoiY2xyMXB1cDI1MmJxcDB4MHdlanBlMWFqbyIsImJJZCI6IlBVRkZQNCIsImtldklkIjoiVklBREFBMDM0RDUyQTA0Q0MwQjc1QUNGNTc3NDE4QUMzMSIsInRJZCI6ImFkc191aSIsImVhSWQiOiJEYmh3SlVVcVZ6eVJQX2RLZHJQSFhkSUl1X3hxOEVuS0VJWXA1Sjd3d2x4aTFadnJsQ2pqTFE9PSIsInZzIjoiTEkiLCJ6IjoiQ0giLCJtIjpmYWxzZSwiZ2VuIjo0fQ.JFX1O3bQopF24SmCzTx5N_SpiSVdi3gmUvF6nHl_XHw',
    'BSS_UDT': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6Im1hcmtldHBsYWNlc0BiZWxsYXZpdGFvcmdhbmljLmNvbSIsImZpcnN0TmFtZSI6IklEQU0gTmF0dXJhbCBXZWxsbmVzcyBQdnQgTHRkIiwibW9iaWxlIjoiOTgyMTU4ODk5NSIsInN0YXRlIjoiVkVSSUZJRUQiLCJ2YWxpZFNlc3Npb24iOnRydWUsInRlbmFudCI6IkJTUyIsImlhdCI6MTcxMTEyMjc5MywiZXhwIjoxNzExMTIzMzkzfQ.bxKKoZzuOyUP8-TpoIUw77b3sGalQa09EChO7v_QkJs',
    '_ga_ZPGRNTNNRT': 'GS1.1.1711122787.166.1.1711122802.0.0.0',
    'nonce': 'ss-1908197693',
}

headers = {
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    # 'Cookie': 'T=TI169891842149300161944937865135939588577615020537527148270186391420; _pxvid=c6c61fc1-7964-11ee-8e5a-1d67ccbdf2e0; dpr=1.25; _fbp=fb.1.1700471257731.638459595; _ga_B9RGC9GN63=GS1.1.1702722512.1.1.1702722682.54.0.0; DID=clr1pup252bqp0x0wejpe1ajo; ULSN=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJjb29raWUiLCJhdWQiOiJmbGlwa2FydCIsImlzcyI6ImF1dGguZmxpcGthcnQuY29tIiwiY2xhaW1zIjp7ImdlbiI6IjEiLCJ1bmlxdWVJZCI6IlVVSTI0MDIxNDEyNTQxMjc4NE85TU9OTE0iLCJma0RldiI6bnVsbH0sImV4cCI6MTcyMzY3NTQ1MiwiaWF0IjoxNzA3ODk1NDUyLCJqdGkiOiIzZmIzYjAxZS02MzU2LTRjM2ItYTg3Yi1lNDQ3ZWNmMWJiYzEifQ.qbw3LDnvt96oOTYcrXvedJeOeJteVaWqgwkYlaKjyuw; vh=730; vw=1536; _ga_0RGM1K38MN=GS1.2.1708195526.2.1.1708195657.0.0.0; _ga_C00F4Q43Q7=GS1.2.1708196044.1.0.1708196044.0.0.0; _ga_2P94RMW04V=GS1.2.1708196121.6.1.1708196143.0.0.0; _gcl_au=1.1.856723108.1708257205; K-ACTION=null; ud=3.-hCuLDZfVJf9kwEcWhK4arj09yD35YGA9WD7yo1zRPr-6c1rmX2_xdHegqPpB3V8IXYz3NsAnP3SBWNaEKufBfykm01W9EISet6O__tpbwLut1-EZphHbJ0c9MzW0rczeRXhalfDVODMz8JTNMlQlgc9FtPFTSU9rNePFCXS_okASoEjAhPorkspIuB6dUcZtsYfTSEOj6D6fCfEhHGTX040PuZMdyiyk409VK7VDUArNQCXrRjfusSZdRR_dSa_IYardO48M5GyGz8FGpTkPTBYE_1zDB-5NXEc93lP2wklWoHEa-Dtp_7e6v2PvoLYEnO9q9WRO923E1MzbxEsgQzTal18ocz6m1QhVKcLAkifQY1CVPvSCEDYAhYysg7Cifn25pVGYReJE-wqKz__XeZKWQ6m9S5ylJWi8ZCNic_rQWkW8tl4jP7uwPxupbq0hBk3YeSRAVvcjX09zDY5qn4jmi-pJicw3oOin6BBwh5j4AEuCE1_UBhyu1FzQ6HXVin354_zqMKmt5Ez4awQztwLbxHMqBrzPLNw1nVv-mMH56A0UIV523BaT7wlgFXFKDY9PgZuquXJtkpqqSSPK3sdeoBmL_SsoP5XdHnW3U3lvtJigEiuV1-2In3wufWsqsHYvXC8tj7Vr6X8srs_3ehJ7eFh0ZMdB7QsQTCynabS2sW3gILSeLC2-NwmdaemzanTaScNERb6Z6uBV6aYgxLtiUZZci5cqwxPaCVTIRHxdKh90EtL6MagI-T8KaMNUkYxg3mOLw4UnS1OIQr5vw; CURRENT_TENANT=BSS; AMCV_17EB401053DAF4840A490D4C%40AdobeOrg=-227196251%7CMCIDTS%7C19803%7CMCMID%7C88087235322683450901903204835359161911%7CMCAAMLH-1711370283%7C12%7CMCAAMB-1711535846%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1710938246s%7CNONE%7CMCAID%7CNONE; S=d1t12P2AkKQt9Ez8/fT8PP2k/RaqC3I0GSWMIuvetzRFw0i+4DygShEPYXDFPp3GYoMnuXXBNqttLBucCv3X8kr/htg==; at=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjNhNzdlZTgxLTRjNWYtNGU5Ni04ZmRlLWM3YWMyYjVlOTA1NSJ9.eyJleHAiOjE3MTA5NDMwMDIsImlhdCI6MTcxMDk0MTIwMiwiaXNzIjoia2V2bGFyIiwianRpIjoiYjRjOTAwMWEtZWYzOS00OTQ4LTlmZTQtZjkzY2Q2YmQyYzE0IiwidHlwZSI6IkFUIiwiZElkIjoiVEkxNjk4OTE4NDIxNDkzMDAxNjE5NDQ5Mzc4NjUxMzU5Mzk1ODg1Nzc2MTUwMjA1Mzc1MjcxNDgyNzAxODYzOTE0MjAiLCJiSWQiOiJXMVE2TkwiLCJrZXZJZCI6IlZJNkM1MjJERkVERERCNDdCMDk0REJBQjhGQjgyNTM3Q0MiLCJ0SWQiOiJtYXBpIiwiZWFJZCI6ImJlMHVRSWdQSVRwMlpxYW5OTmhobkdIamhSdi1QMVhOTmNURnloQS16QVNBWU40QlZ2NF9Odz09IiwidnMiOiJMSSIsInoiOiJIWUQiLCJtIjp0cnVlLCJnZW4iOjR9.SPHHwfWdG4P6zfLs0NJZPZVMHm2MU3uFcsq4dh0PgjY; rt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjNhNzdlZTgxLTRjNWYtNGU5Ni04ZmRlLWM3YWMyYjVlOTA1NSJ9.eyJleHAiOjE3MjY4Mzg4MDIsImlhdCI6MTcxMDk0MTIwMiwiaXNzIjoia2V2bGFyIiwianRpIjoiM2Q3MzI0NDEtMGEyZi00Y2FjLTk1MjQtZDZiNzU2ZmVkYmE4IiwidHlwZSI6IlJUIiwiZElkIjoiVEkxNjk4OTE4NDIxNDkzMDAxNjE5NDQ5Mzc4NjUxMzU5Mzk1ODg1Nzc2MTUwMjA1Mzc1MjcxNDgyNzAxODYzOTE0MjAiLCJiSWQiOiJXMVE2TkwiLCJrZXZJZCI6IlZJNkM1MjJERkVERERCNDdCMDk0REJBQjhGQjgyNTM3Q0MiLCJ0SWQiOiJtYXBpIiwibSI6eyJ0eXBlIjoibiJ9LCJ2IjoiQ0dPS0tBIn0.0i7wLqxD-9cOQ5NK-C2YS92LPWrwiM77QLnc0HcaKnU; vd=VI6C522DFEDDDB47B094DBAB8FB82537CC-1707110391153-46.1710941202.1710941202.162220005; SN=VI6C522DFEDDDB47B094DBAB8FB82537CC.TOK635F5023E626455C82262BA71755319E.1710941210.LI; _px3=7e81b72a8d81f65048b2e580804a9906c2c2fb26fde4c7aabd214bcb1ed0a25a:i6m859ehtdI3oDAbiEJ3MsMpIEtgSxV8e57zfiA/XA0mkavG72n5wgXcjaC6IRyumQ0tiVe8ENKlq1HObq4TPA==:1000:vo7aCy8Bx7RFZ0YQiBSsD3rHhMmaxiMa8wueHGloRUHyTRrTQYfaDC0okTf98vbrHJc8BC7dZpvYxFyqe6zn8y/IxKzX6pfEmaP/Sllyu0B19OF2a2W1ghVOyn0pJAjoVZq9FOn4OWKO+bxZFXQyRerjoFi14FmgKBqNBy9K6RGWeiKVFVrbfxpdYtLwLuBTVeQWa7WWGI8iAZmwIVJ4+i7zsIW+qyrujWub4AF5pEo=; AMCV_55CFEDA0570C3FA17F000101%40AdobeOrg=-227196251%7CMCIDTS%7C19804%7CMCMID%7C83672356534473986601461754159478791217%7CMCAAMLH-1711603203%7C12%7CMCAAMB-1711603203%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1711005603s%7CNONE%7CMCAID%7CNONE; mp_9ea3bc9a23c575907407cf80efd56524_mixpanel=%7B%22distinct_id%22%3A%20%22ACCABA3F2470AD442FAA32E10D0E76B735F%22%2C%22%24device_id%22%3A%20%2218bf5c79f2b403-04403e63bfeec8-26031051-144000-18bf5c79f2ca33%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fseller.flipkart.com%2Fsell-online%2Fmulti-select%22%2C%22%24initial_referring_domain%22%3A%20%22seller.flipkart.com%22%2C%22%24user_id%22%3A%20%22ACCABA3F2470AD442FAA32E10D0E76B735F%22%2C%22%24search_engine%22%3A%20%22google%22%7D; _ga=GA1.1.1819741834.1700633034; _ga_TVF0VCMCT3=GS1.1.1710998391.145.1.1710998431.20.0.0; _ga_0SJLGHBL81=GS1.1.1710998391.24.1.1710998431.0.0.0; s_nr=1710998431595-Repeat; _csrf=91qWeSw-th1diAv6F4OTYv20; TENANT=BSS; BSS_SID=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImQxZWI3YWU1LTllNmUtNGMxNi04ZjM1LTVlYWJhOGNiYzMyZCJ9.eyJleHAiOjE3MTExMjQ1OTMsImlhdCI6MTcxMTEyMjc5MywiaXNzIjoia2V2bGFyIiwianRpIjoiMGFjYThhYmUtMTAyOS00N2NjLWFjZjMtODBmMGZlMmE2MTU5IiwidHlwZSI6IkFUIiwiZElkIjoiY2xyMXB1cDI1MmJxcDB4MHdlanBlMWFqbyIsImJJZCI6IlBVRkZQNCIsImtldklkIjoiVklBREFBMDM0RDUyQTA0Q0MwQjc1QUNGNTc3NDE4QUMzMSIsInRJZCI6ImFkc191aSIsImVhSWQiOiJEYmh3SlVVcVZ6eVJQX2RLZHJQSFhkSUl1X3hxOEVuS0VJWXA1Sjd3d2x4aTFadnJsQ2pqTFE9PSIsInZzIjoiTEkiLCJ6IjoiQ0giLCJtIjpmYWxzZSwiZ2VuIjo0fQ.JFX1O3bQopF24SmCzTx5N_SpiSVdi3gmUvF6nHl_XHw; BSS_UDT=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6Im1hcmtldHBsYWNlc0BiZWxsYXZpdGFvcmdhbmljLmNvbSIsImZpcnN0TmFtZSI6IklEQU0gTmF0dXJhbCBXZWxsbmVzcyBQdnQgTHRkIiwibW9iaWxlIjoiOTgyMTU4ODk5NSIsInN0YXRlIjoiVkVSSUZJRUQiLCJ2YWxpZFNlc3Npb24iOnRydWUsInRlbmFudCI6IkJTUyIsImlhdCI6MTcxMTEyMjc5MywiZXhwIjoxNzExMTIzMzkzfQ.bxKKoZzuOyUP8-TpoIUw77b3sGalQa09EChO7v_QkJs; _ga_ZPGRNTNNRT=GS1.1.1711122787.166.1.1711122802.0.0.0; nonce=ss-1908197693',
    'Origin': 'https://advertising.flipkart.com',
    'Pragma': 'no-cache',
    'Referer': 'https://advertising.flipkart.com/ad-account/campaigns/pla/OWL1UYKSNRYR/edit?baccount=N5J3WN87DKC4&aaccount=IZJL4R3KCMHR',
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
    'viewport-width': '856',
    'x-aaccount': 'IZJL4R3KCMHR',
    'x-baccount': 'N5J3WN87DKC4',
    'x-csrf-token': 'ubdDNv5U-tSu_kWP6sc1LOadNU0tsNj_lV9k',
    'x-sourceurl': 'https://advertising.flipkart.com/ad-account/campaigns/pla/OWL1UYKSNRYR/edit?baccount=N5J3WN87DKC4&aaccount=IZJL4R3KCMHR',
    'x-tenant': 'BSS',
}

json_data = {
    'operationName': 'GetCampaign',
    'variables': {
        'seller': False,
        'adProduct': 'BRAND_PLA',
        'id': 'OWL1UYKSNRYR',
    },
    'query': 'query GetCampaign($id: String!, $adProduct: String!, $seller: Boolean! = false) {\n  getCampaignForId(id: $id, adProduct: $adProduct) {\n    ... on CampaignPLAResponse {\n      campaignInfo {\n        id\n        type\n        name\n        status\n        uiStatus\n        currency\n        paymentType\n        budget\n        budgetType\n        fsnIds\n        startDate\n        endDate\n        costModel\n        marketplace\n        pacing\n        withPreferredSellers\n        preferredSellerIds\n        preferredSellerNames\n        businessZones\n        tillBudgetEnds\n        fsnMeta {\n          id\n          title\n          image\n          minListingPrice\n          maxListingPrice\n          listingCurrency\n          brand\n          storeList\n          __typename\n        }\n        __typename\n      }\n      adGroups {\n        id\n        name\n        status\n        productCount\n        commodityId\n        cost\n        budget\n        targeting {\n          type\n          pages\n          excludeKeywords {\n            q\n            r\n            __typename\n          }\n          includeKeywords {\n            q\n            r\n            matchType\n            __typename\n          }\n          __typename\n        }\n        storePaths\n        fsnBanners {\n          id\n          fsnId\n          __typename\n        }\n        costVariation {\n          ...PlacementsFragment\n          __typename\n        }\n        __typename\n      }\n      brandIds\n      preferredSellers {\n        alias\n        sellerId\n        __typename\n      }\n      placementsMetaInfo {\n        ...PlacementsMetaInfoFragement\n        __typename\n      }\n      __typename\n    }\n    ... on CampaignPCAResponse {\n      campaignInfo {\n        id\n        type\n        name\n        status\n        uiStatus\n        currency\n        paymentType\n        budget\n        budgetType\n        startDate\n        endDate\n        costModel\n        marketplace\n        __typename\n      }\n      adGroups {\n        id\n        name\n        status\n        uiStatus\n        startDate\n        endDate\n        cost\n        budget\n        excludeKeywords\n        marketplace\n        showAdInBroadMatchStores\n        costVariation {\n          ...PlacementsFragment\n          __typename\n        }\n        allowedActions\n        pacing\n        targeting {\n          type\n          pages\n          excludeKeywords {\n            q\n            r\n            __typename\n          }\n          includeKeywords {\n            q\n            r\n            matchType\n            __typename\n          }\n          __typename\n        }\n        contents {\n          contentId\n          creativeBanners {\n            creativeId\n            creativeName\n            creativeTemplateId\n            uiStatus\n            status\n            allowedActions\n            referenceId\n            mediaId\n            creativeType\n            assets {\n              macro\n              value\n              type\n              origin\n              assetId\n              subAssets {\n                macro\n                value\n                type\n                __typename\n              }\n              __typename\n            }\n            isSelected\n            id\n            language\n            __typename\n          }\n          collectionUrl\n          landingPageUrl\n          collectionId\n          collectionType\n          brands\n          stores {\n            storeId\n            storeName\n            __typename\n          }\n          rejectedCount\n          isPreferredSeller\n          creativeTemplateId\n          __typename\n        }\n        __typename\n      }\n      brandIds\n      placementsMetaInfo {\n        ...PlacementsMetaInfoFragement\n        __typename\n      }\n      __typename\n    }\n    ... on CampaignDisplayAdsResponse {\n      campaignInfo {\n        id\n        type\n        name\n        status\n        uiStatus\n        currency\n        paymentType\n        budget\n        startDate\n        endDate\n        costModel\n        marketplace\n        pacing\n        budgetType\n        adFormat\n        publisher\n        __typename\n      }\n      adGroups {\n        id\n        name\n        status\n        uiStatus\n        startDate\n        endDate\n        cost\n        budget\n        allowedActions\n        marketplace\n        pacing\n        contents {\n          contentId\n          creativeBanners {\n            creativeId\n            creativeName\n            uiStatus\n            status\n            allowedActions\n            referenceId\n            mediaId\n            videoMediaStatus\n            creativeType\n            assets {\n              macro\n              value\n              type\n              origin\n              subAssets {\n                macro\n                value\n                type\n                __typename\n              }\n              isSystemAsset\n              __typename\n            }\n            isSelected\n            id\n            __typename\n          }\n          collectionUrl\n          collectionId\n          collectionType\n          brands\n          stores {\n            storeId\n            storeName\n            __typename\n          }\n          rejectedCount\n          isUrlSystemCreated\n          landingPageUrl\n          status\n          isPreferredSeller\n          __typename\n        }\n        frequencyCapping {\n          interval\n          value\n          numberOfIntervals\n          __typename\n        }\n        customScheduling\n        channels\n        userTargetingExpression {\n          groupId\n          type\n          values\n          publisherSpecific\n          __typename\n        }\n        contextTargetingExpression {\n          groupId\n          type\n          values\n          publisherSpecific\n          __typename\n        }\n        __typename\n      }\n      brandIds\n      __typename\n    }\n    __typename\n  }\n  getAdAccountDetails @skip(if: $seller) {\n    marketplaceConfigurationResponse {\n      marketplaceList\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment PlacementsFragment on CostVariationType {\n  placements {\n    absoluteCost\n    percentage\n    type\n    pageType\n    __typename\n  }\n  __typename\n}\n\nfragment PlacementsMetaInfoFragement on PlacementsMeta {\n  type\n  title\n  detail\n  pageType\n  __typename\n}\n',
}

response = requests.post('https://advertising.flipkart.com/api', cookies=cookies, headers=headers, json=json_data)



y = json_data['variables']['id']
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
        'percentage': item['percentage'],
        'campaignId': y
    }
    placements.append(placement)
print(placements)


def needed():
    return placements

# print(y)
# exit()
cursor = connection.cursor()

sql_update = "UPDATE fk_pla SET Absolute_Cost = %s WHERE Campaign_ID = %s AND `Placement_Type` = %s"

print("********************************************************************************")
for placement in placements:
    if placement['type'] == 'HOME_PAGE':
        placement['absoluteCost'] = 3.38

        # Assuming campaign_id is assigned a value somewhere in your code
        campaign_id = y
        placement_type = 'Home Page'  # Placement type determined based on condition
        cursor.execute(sql_update, (placement['absoluteCost'], campaign_id, placement_type))
print(placements)
connection.commit()

# Close the cursor and connection
cursor.close()
connection.close()
exit()
        




#----------------------------------------------------------------------------------------------------------------------------------------------------------------



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
    'CURRENT_TENANT': 'BSS',
    'AMCV_17EB401053DAF4840A490D4C%40AdobeOrg': '-227196251%7CMCIDTS%7C19803%7CMCMID%7C88087235322683450901903204835359161911%7CMCAAMLH-1711370283%7C12%7CMCAAMB-1711535846%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1710938246s%7CNONE%7CMCAID%7CNONE',
    'S': 'd1t12P2AkKQt9Ez8/fT8PP2k/RaqC3I0GSWMIuvetzRFw0i+4DygShEPYXDFPp3GYoMnuXXBNqttLBucCv3X8kr/htg==',
    'at': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjNhNzdlZTgxLTRjNWYtNGU5Ni04ZmRlLWM3YWMyYjVlOTA1NSJ9.eyJleHAiOjE3MTA5NDMwMDIsImlhdCI6MTcxMDk0MTIwMiwiaXNzIjoia2V2bGFyIiwianRpIjoiYjRjOTAwMWEtZWYzOS00OTQ4LTlmZTQtZjkzY2Q2YmQyYzE0IiwidHlwZSI6IkFUIiwiZElkIjoiVEkxNjk4OTE4NDIxNDkzMDAxNjE5NDQ5Mzc4NjUxMzU5Mzk1ODg1Nzc2MTUwMjA1Mzc1MjcxNDgyNzAxODYzOTE0MjAiLCJiSWQiOiJXMVE2TkwiLCJrZXZJZCI6IlZJNkM1MjJERkVERERCNDdCMDk0REJBQjhGQjgyNTM3Q0MiLCJ0SWQiOiJtYXBpIiwiZWFJZCI6ImJlMHVRSWdQSVRwMlpxYW5OTmhobkdIamhSdi1QMVhOTmNURnloQS16QVNBWU40QlZ2NF9Odz09IiwidnMiOiJMSSIsInoiOiJIWUQiLCJtIjp0cnVlLCJnZW4iOjR9.SPHHwfWdG4P6zfLs0NJZPZVMHm2MU3uFcsq4dh0PgjY',
    'rt': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjNhNzdlZTgxLTRjNWYtNGU5Ni04ZmRlLWM3YWMyYjVlOTA1NSJ9.eyJleHAiOjE3MjY4Mzg4MDIsImlhdCI6MTcxMDk0MTIwMiwiaXNzIjoia2V2bGFyIiwianRpIjoiM2Q3MzI0NDEtMGEyZi00Y2FjLTk1MjQtZDZiNzU2ZmVkYmE4IiwidHlwZSI6IlJUIiwiZElkIjoiVEkxNjk4OTE4NDIxNDkzMDAxNjE5NDQ5Mzc4NjUxMzU5Mzk1ODg1Nzc2MTUwMjA1Mzc1MjcxNDgyNzAxODYzOTE0MjAiLCJiSWQiOiJXMVE2TkwiLCJrZXZJZCI6IlZJNkM1MjJERkVERERCNDdCMDk0REJBQjhGQjgyNTM3Q0MiLCJ0SWQiOiJtYXBpIiwibSI6eyJ0eXBlIjoibiJ9LCJ2IjoiQ0dPS0tBIn0.0i7wLqxD-9cOQ5NK-C2YS92LPWrwiM77QLnc0HcaKnU',
    'vd': 'VI6C522DFEDDDB47B094DBAB8FB82537CC-1707110391153-46.1710941202.1710941202.162220005',
    'SN': 'VI6C522DFEDDDB47B094DBAB8FB82537CC.TOK635F5023E626455C82262BA71755319E.1710941210.LI',
    '_px3': '7e81b72a8d81f65048b2e580804a9906c2c2fb26fde4c7aabd214bcb1ed0a25a:i6m859ehtdI3oDAbiEJ3MsMpIEtgSxV8e57zfiA/XA0mkavG72n5wgXcjaC6IRyumQ0tiVe8ENKlq1HObq4TPA==:1000:vo7aCy8Bx7RFZ0YQiBSsD3rHhMmaxiMa8wueHGloRUHyTRrTQYfaDC0okTf98vbrHJc8BC7dZpvYxFyqe6zn8y/IxKzX6pfEmaP/Sllyu0B19OF2a2W1ghVOyn0pJAjoVZq9FOn4OWKO+bxZFXQyRerjoFi14FmgKBqNBy9K6RGWeiKVFVrbfxpdYtLwLuBTVeQWa7WWGI8iAZmwIVJ4+i7zsIW+qyrujWub4AF5pEo=',
    '_csrf': 'Hxm3Qzn325NQw7gPHYh4hbdj',
    'TENANT': 'BSS',
    'moe_uuid': '2b61a549-6d9c-4c19-9ab4-f2a5c0a7ed90',
    'AMCVS_55CFEDA0570C3FA17F000101%40AdobeOrg': '1',
    'AMCV_55CFEDA0570C3FA17F000101%40AdobeOrg': '-227196251%7CMCIDTS%7C19804%7CMCMID%7C83672356534473986601461754159478791217%7CMCAAMLH-1711603203%7C12%7CMCAAMB-1711603203%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1711005603s%7CNONE%7CMCAID%7CNONE',
    's_sq': 'flipkartsellerprod%3D%2526c.%2526a.%2526activitymap.%2526page%253Dseller%25253A%252520home%252520page%2526link%253DBella%252520vita%252520organic%252520Luxury%252520Unisex%252520Perfume%252520Gift%252520Set%252520-%2525204x20%252520ML%252520Eau%252520de%252520Parfum%252520-%25252080%252520ml%252520%252528For%252520Men%252520%252526%252520Women%252529%252520SKU%252520ID%25253A%2525208906150340428%252520%2525E2%252582%2525B9%25252035%25252C7%2526region%253Dearn-more-product-details-table%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253Dseller%25253A%252520home%252520page%2526pidt%253D1%2526oid%253DfunctionBr%252528%252529%25257B%25257D%2526oidt%253D2%2526ot%253DTR',
    'mp_9ea3bc9a23c575907407cf80efd56524_mixpanel': '%7B%22distinct_id%22%3A%20%22ACCABA3F2470AD442FAA32E10D0E76B735F%22%2C%22%24device_id%22%3A%20%2218bf5c79f2b403-04403e63bfeec8-26031051-144000-18bf5c79f2ca33%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fseller.flipkart.com%2Fsell-online%2Fmulti-select%22%2C%22%24initial_referring_domain%22%3A%20%22seller.flipkart.com%22%2C%22%24user_id%22%3A%20%22ACCABA3F2470AD442FAA32E10D0E76B735F%22%2C%22%24search_engine%22%3A%20%22google%22%7D',
    '_ga': 'GA1.1.1819741834.1700633034',
    '_ga_TVF0VCMCT3': 'GS1.1.1710998391.145.1.1710998431.20.0.0',
    '_ga_0SJLGHBL81': 'GS1.1.1710998391.24.1.1710998431.0.0.0',
    's_nr': '1710998431595-Repeat',
    'BSS_SID': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjA1MGRjYzRjLTE0MGYtNDNkYy1iYTUzLTM2NTY3MTQ3MWVlZSJ9.eyJleHAiOjE3MTEwODY1ODMsImlhdCI6MTcxMTA4NDc4MywiaXNzIjoia2V2bGFyIiwianRpIjoiZTgyMjA1YWUtOWY2YS00MDkxLThjODQtZDk2ZTUzZTMwNzkyIiwidHlwZSI6IkFUIiwiZElkIjoiY2xyMXB1cDI1MmJxcDB4MHdlanBlMWFqbyIsImJJZCI6IllaV1UzWiIsImtldklkIjoiVklBREFBMDM0RDUyQTA0Q0MwQjc1QUNGNTc3NDE4QUMzMSIsInRJZCI6ImFkc191aSIsImVhSWQiOiJEelFjYkRsbnItWWJIaUhZVUpvT2JpdnNPUHk0bUhuOER6c2xLRkxYeUZsMTB0X3RweVdubmc9PSIsInZzIjoiTEkiLCJ6IjoiQ0giLCJtIjpmYWxzZSwiZ2VuIjo0fQ.et4ilxS7O_Gpo19_AcA9wix2Dofopce9cCiDqYPV33o',
    'BSS_UDT': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6Im1hcmtldHBsYWNlc0BiZWxsYXZpdGFvcmdhbmljLmNvbSIsImZpcnN0TmFtZSI6IklEQU0gTmF0dXJhbCBXZWxsbmVzcyBQdnQgTHRkIiwibW9iaWxlIjoiOTgyMTU4ODk5NSIsInN0YXRlIjoiVkVSSUZJRUQiLCJ2YWxpZFNlc3Npb24iOnRydWUsInRlbmFudCI6IkJTUyIsImlhdCI6MTcxMTA4NTM5NywiZXhwIjoxNzExMDg1OTk3fQ.VEAFHY5IDdMcwjsTuZEKltP00mM64aNFMFkVFEHo5BI',
    '_ga_ZPGRNTNNRT': 'GS1.1.1711084777.163.1.1711085749.0.0.0',
    'nonce': 'ss-4082920680',
}

headers = {
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    # 'Cookie': 'T=TI169891842149300161944937865135939588577615020537527148270186391420; _pxvid=c6c61fc1-7964-11ee-8e5a-1d67ccbdf2e0; dpr=1.25; _fbp=fb.1.1700471257731.638459595; _ga_B9RGC9GN63=GS1.1.1702722512.1.1.1702722682.54.0.0; DID=clr1pup252bqp0x0wejpe1ajo; ULSN=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJjb29raWUiLCJhdWQiOiJmbGlwa2FydCIsImlzcyI6ImF1dGguZmxpcGthcnQuY29tIiwiY2xhaW1zIjp7ImdlbiI6IjEiLCJ1bmlxdWVJZCI6IlVVSTI0MDIxNDEyNTQxMjc4NE85TU9OTE0iLCJma0RldiI6bnVsbH0sImV4cCI6MTcyMzY3NTQ1MiwiaWF0IjoxNzA3ODk1NDUyLCJqdGkiOiIzZmIzYjAxZS02MzU2LTRjM2ItYTg3Yi1lNDQ3ZWNmMWJiYzEifQ.qbw3LDnvt96oOTYcrXvedJeOeJteVaWqgwkYlaKjyuw; vh=730; vw=1536; _ga_0RGM1K38MN=GS1.2.1708195526.2.1.1708195657.0.0.0; _ga_C00F4Q43Q7=GS1.2.1708196044.1.0.1708196044.0.0.0; _ga_2P94RMW04V=GS1.2.1708196121.6.1.1708196143.0.0.0; _gcl_au=1.1.856723108.1708257205; K-ACTION=null; ud=3.-hCuLDZfVJf9kwEcWhK4arj09yD35YGA9WD7yo1zRPr-6c1rmX2_xdHegqPpB3V8IXYz3NsAnP3SBWNaEKufBfykm01W9EISet6O__tpbwLut1-EZphHbJ0c9MzW0rczeRXhalfDVODMz8JTNMlQlgc9FtPFTSU9rNePFCXS_okASoEjAhPorkspIuB6dUcZtsYfTSEOj6D6fCfEhHGTX040PuZMdyiyk409VK7VDUArNQCXrRjfusSZdRR_dSa_IYardO48M5GyGz8FGpTkPTBYE_1zDB-5NXEc93lP2wklWoHEa-Dtp_7e6v2PvoLYEnO9q9WRO923E1MzbxEsgQzTal18ocz6m1QhVKcLAkifQY1CVPvSCEDYAhYysg7Cifn25pVGYReJE-wqKz__XeZKWQ6m9S5ylJWi8ZCNic_rQWkW8tl4jP7uwPxupbq0hBk3YeSRAVvcjX09zDY5qn4jmi-pJicw3oOin6BBwh5j4AEuCE1_UBhyu1FzQ6HXVin354_zqMKmt5Ez4awQztwLbxHMqBrzPLNw1nVv-mMH56A0UIV523BaT7wlgFXFKDY9PgZuquXJtkpqqSSPK3sdeoBmL_SsoP5XdHnW3U3lvtJigEiuV1-2In3wufWsqsHYvXC8tj7Vr6X8srs_3ehJ7eFh0ZMdB7QsQTCynabS2sW3gILSeLC2-NwmdaemzanTaScNERb6Z6uBV6aYgxLtiUZZci5cqwxPaCVTIRHxdKh90EtL6MagI-T8KaMNUkYxg3mOLw4UnS1OIQr5vw; CURRENT_TENANT=BSS; AMCV_17EB401053DAF4840A490D4C%40AdobeOrg=-227196251%7CMCIDTS%7C19803%7CMCMID%7C88087235322683450901903204835359161911%7CMCAAMLH-1711370283%7C12%7CMCAAMB-1711535846%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1710938246s%7CNONE%7CMCAID%7CNONE; S=d1t12P2AkKQt9Ez8/fT8PP2k/RaqC3I0GSWMIuvetzRFw0i+4DygShEPYXDFPp3GYoMnuXXBNqttLBucCv3X8kr/htg==; at=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjNhNzdlZTgxLTRjNWYtNGU5Ni04ZmRlLWM3YWMyYjVlOTA1NSJ9.eyJleHAiOjE3MTA5NDMwMDIsImlhdCI6MTcxMDk0MTIwMiwiaXNzIjoia2V2bGFyIiwianRpIjoiYjRjOTAwMWEtZWYzOS00OTQ4LTlmZTQtZjkzY2Q2YmQyYzE0IiwidHlwZSI6IkFUIiwiZElkIjoiVEkxNjk4OTE4NDIxNDkzMDAxNjE5NDQ5Mzc4NjUxMzU5Mzk1ODg1Nzc2MTUwMjA1Mzc1MjcxNDgyNzAxODYzOTE0MjAiLCJiSWQiOiJXMVE2TkwiLCJrZXZJZCI6IlZJNkM1MjJERkVERERCNDdCMDk0REJBQjhGQjgyNTM3Q0MiLCJ0SWQiOiJtYXBpIiwiZWFJZCI6ImJlMHVRSWdQSVRwMlpxYW5OTmhobkdIamhSdi1QMVhOTmNURnloQS16QVNBWU40QlZ2NF9Odz09IiwidnMiOiJMSSIsInoiOiJIWUQiLCJtIjp0cnVlLCJnZW4iOjR9.SPHHwfWdG4P6zfLs0NJZPZVMHm2MU3uFcsq4dh0PgjY; rt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjNhNzdlZTgxLTRjNWYtNGU5Ni04ZmRlLWM3YWMyYjVlOTA1NSJ9.eyJleHAiOjE3MjY4Mzg4MDIsImlhdCI6MTcxMDk0MTIwMiwiaXNzIjoia2V2bGFyIiwianRpIjoiM2Q3MzI0NDEtMGEyZi00Y2FjLTk1MjQtZDZiNzU2ZmVkYmE4IiwidHlwZSI6IlJUIiwiZElkIjoiVEkxNjk4OTE4NDIxNDkzMDAxNjE5NDQ5Mzc4NjUxMzU5Mzk1ODg1Nzc2MTUwMjA1Mzc1MjcxNDgyNzAxODYzOTE0MjAiLCJiSWQiOiJXMVE2TkwiLCJrZXZJZCI6IlZJNkM1MjJERkVERERCNDdCMDk0REJBQjhGQjgyNTM3Q0MiLCJ0SWQiOiJtYXBpIiwibSI6eyJ0eXBlIjoibiJ9LCJ2IjoiQ0dPS0tBIn0.0i7wLqxD-9cOQ5NK-C2YS92LPWrwiM77QLnc0HcaKnU; vd=VI6C522DFEDDDB47B094DBAB8FB82537CC-1707110391153-46.1710941202.1710941202.162220005; SN=VI6C522DFEDDDB47B094DBAB8FB82537CC.TOK635F5023E626455C82262BA71755319E.1710941210.LI; _px3=7e81b72a8d81f65048b2e580804a9906c2c2fb26fde4c7aabd214bcb1ed0a25a:i6m859ehtdI3oDAbiEJ3MsMpIEtgSxV8e57zfiA/XA0mkavG72n5wgXcjaC6IRyumQ0tiVe8ENKlq1HObq4TPA==:1000:vo7aCy8Bx7RFZ0YQiBSsD3rHhMmaxiMa8wueHGloRUHyTRrTQYfaDC0okTf98vbrHJc8BC7dZpvYxFyqe6zn8y/IxKzX6pfEmaP/Sllyu0B19OF2a2W1ghVOyn0pJAjoVZq9FOn4OWKO+bxZFXQyRerjoFi14FmgKBqNBy9K6RGWeiKVFVrbfxpdYtLwLuBTVeQWa7WWGI8iAZmwIVJ4+i7zsIW+qyrujWub4AF5pEo=; _csrf=Hxm3Qzn325NQw7gPHYh4hbdj; TENANT=BSS; moe_uuid=2b61a549-6d9c-4c19-9ab4-f2a5c0a7ed90; AMCVS_55CFEDA0570C3FA17F000101%40AdobeOrg=1; AMCV_55CFEDA0570C3FA17F000101%40AdobeOrg=-227196251%7CMCIDTS%7C19804%7CMCMID%7C83672356534473986601461754159478791217%7CMCAAMLH-1711603203%7C12%7CMCAAMB-1711603203%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1711005603s%7CNONE%7CMCAID%7CNONE; s_sq=flipkartsellerprod%3D%2526c.%2526a.%2526activitymap.%2526page%253Dseller%25253A%252520home%252520page%2526link%253DBella%252520vita%252520organic%252520Luxury%252520Unisex%252520Perfume%252520Gift%252520Set%252520-%2525204x20%252520ML%252520Eau%252520de%252520Parfum%252520-%25252080%252520ml%252520%252528For%252520Men%252520%252526%252520Women%252529%252520SKU%252520ID%25253A%2525208906150340428%252520%2525E2%252582%2525B9%25252035%25252C7%2526region%253Dearn-more-product-details-table%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253Dseller%25253A%252520home%252520page%2526pidt%253D1%2526oid%253DfunctionBr%252528%252529%25257B%25257D%2526oidt%253D2%2526ot%253DTR; mp_9ea3bc9a23c575907407cf80efd56524_mixpanel=%7B%22distinct_id%22%3A%20%22ACCABA3F2470AD442FAA32E10D0E76B735F%22%2C%22%24device_id%22%3A%20%2218bf5c79f2b403-04403e63bfeec8-26031051-144000-18bf5c79f2ca33%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fseller.flipkart.com%2Fsell-online%2Fmulti-select%22%2C%22%24initial_referring_domain%22%3A%20%22seller.flipkart.com%22%2C%22%24user_id%22%3A%20%22ACCABA3F2470AD442FAA32E10D0E76B735F%22%2C%22%24search_engine%22%3A%20%22google%22%7D; _ga=GA1.1.1819741834.1700633034; _ga_TVF0VCMCT3=GS1.1.1710998391.145.1.1710998431.20.0.0; _ga_0SJLGHBL81=GS1.1.1710998391.24.1.1710998431.0.0.0; s_nr=1710998431595-Repeat; BSS_SID=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjA1MGRjYzRjLTE0MGYtNDNkYy1iYTUzLTM2NTY3MTQ3MWVlZSJ9.eyJleHAiOjE3MTEwODY1ODMsImlhdCI6MTcxMTA4NDc4MywiaXNzIjoia2V2bGFyIiwianRpIjoiZTgyMjA1YWUtOWY2YS00MDkxLThjODQtZDk2ZTUzZTMwNzkyIiwidHlwZSI6IkFUIiwiZElkIjoiY2xyMXB1cDI1MmJxcDB4MHdlanBlMWFqbyIsImJJZCI6IllaV1UzWiIsImtldklkIjoiVklBREFBMDM0RDUyQTA0Q0MwQjc1QUNGNTc3NDE4QUMzMSIsInRJZCI6ImFkc191aSIsImVhSWQiOiJEelFjYkRsbnItWWJIaUhZVUpvT2JpdnNPUHk0bUhuOER6c2xLRkxYeUZsMTB0X3RweVdubmc9PSIsInZzIjoiTEkiLCJ6IjoiQ0giLCJtIjpmYWxzZSwiZ2VuIjo0fQ.et4ilxS7O_Gpo19_AcA9wix2Dofopce9cCiDqYPV33o; BSS_UDT=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6Im1hcmtldHBsYWNlc0BiZWxsYXZpdGFvcmdhbmljLmNvbSIsImZpcnN0TmFtZSI6IklEQU0gTmF0dXJhbCBXZWxsbmVzcyBQdnQgTHRkIiwibW9iaWxlIjoiOTgyMTU4ODk5NSIsInN0YXRlIjoiVkVSSUZJRUQiLCJ2YWxpZFNlc3Npb24iOnRydWUsInRlbmFudCI6IkJTUyIsImlhdCI6MTcxMTA4NTM5NywiZXhwIjoxNzExMDg1OTk3fQ.VEAFHY5IDdMcwjsTuZEKltP00mM64aNFMFkVFEHo5BI; _ga_ZPGRNTNNRT=GS1.1.1711084777.163.1.1711085749.0.0.0; nonce=ss-4082920680',
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
    'viewport-width': '856',
    'x-aaccount': 'IZJL4R3KCMHR',
    'x-baccount': 'N5J3WN87DKC4',
    'x-csrf-token': 't4ykydvD-x-gGDjB5-UPf-za9hmBH-zLHd9g',
    'x-sourceurl': 'https://advertising.flipkart.com/ad-account/campaigns/pla/HZOFVP2QQ57C/edit?baccount=N5J3WN87DKC4&aaccount=IZJL4R3KCMHR&step=3',
    'x-tenant': 'BSS',
}

json_data = {
    'operationName': 'UpdateCampaign',
    'variables': {
        'data': {
            'campaignInfo': {
                'type': 'BRAND_PLA',
                'name': 'Acne Patch Charcoal KW PLA',
                'budget': 1003,
                'budgetType': 'TOTAL_BUDGET',
                'startDate': 1710324537000,
                'endDate': None,
                'costModel': 'CPC',
                'pacing': 'NONE',
                'fsnIds': [
                    'BSTGNQAKP6G6DK8E',
                ],
                'marketplace': 'FLIPKART',
                'preferredSellerIds': [],
                'withPreferredSellers': False,
            },
            'adGroups': [
                {
                    'id': '7WV3BVWBQ4D9',
                    'name': 'Body and Face Skin Care',
                    'commodityId': 509,
                    'costModel': 'CPC',
                    'cost': 2.55,
                    'budget': None,
                    'costVariation': {
                        'placements': [
                            {
                                'absoluteCost': 3.38,
                                'type': 'HOME_PAGE',
                                'percentage': 0,
                            },
                            {
                                'absoluteCost': 2.38,
                                'type': 'SEARCH_PAGE_TOP_SLOT',
                                'percentage': -17,
                            },
                            {
                                'absoluteCost': 2.38,
                                'type': 'SEARCH_PAGE',
                                'percentage': -17,
                            },
                            {
                                'absoluteCost': 2.38,
                                'type': 'BROWSE_PAGE_TOP_SLOT',
                                'percentage': -17,
                            },
                            {
                                'absoluteCost': 2.38,
                                'type': 'BROWSE_PAGE',
                                'percentage': -17,
                            },
                            {
                                'absoluteCost': 2.38,
                                'type': 'PRODUCT_PAGE',
                                'percentage': -17,
                            },
                        ],
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
                    'fsnIds': [
                        'BSTGNQAKP6G6DK8E',
                    ],
                },
            ],
        },
        'id': 'HZOFVP2QQ57C',
    },
    'query': 'mutation UpdateCampaign($data: SavePLACampaignPayload!, $id: String!) {\n  updatePLACampaign(data: $data, id: $id) {\n    ...CampaignPLAFragment\n    __typename\n  }\n}\n\nfragment CampaignPLAFragment on CampaignPLAResponse {\n  campaignInfo {\n    id\n    type\n    paymentType\n    currency\n    costModel\n    pacing\n    status\n    uiStatus\n    marketplace\n    name\n    budget\n    grossBudget\n    budgetType\n    startDate\n    endDate\n    allowedActions\n    __typename\n  }\n  adGroups {\n    id\n    name\n    status\n    productCount\n    commodityId\n    cost\n    budget\n    targeting {\n      type\n      pages\n      excludeKeywords {\n        q\n        r\n        __typename\n      }\n      includeKeywords {\n        q\n        r\n        matchType\n        __typename\n      }\n      __typename\n    }\n    storePaths\n    fsnBanners {\n      id\n      fsnId\n      __typename\n    }\n    costVariation {\n      ...PlacementsFragment\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment PlacementsFragment on CostVariationType {\n  placements {\n    absoluteCost\n    percentage\n    type\n    pageType\n    __typename\n  }\n  __typename\n}\n',
}

response = requests.post('https://advertising.flipkart.com/api', cookies=cookies, headers=headers, json=json_data)

print(response.text)