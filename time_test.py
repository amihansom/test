import pyupbit
import time
import datetime

from requests.models import parse_header_links


#########################
##### 시간 테스트중 #####
while True:
    # 현재 시간 불러오기
    now = datetime.datetime.now()
        
    # 매도시간 now - 조건문 08시 59분 00~59초
    #if now.minute == 0:
    # 특정시간
    #if now.hour == 11 and now.minute == 0:
    #if now.hour == 13 or now.hour == 14 or now.hour == 16 or now.hour == 18 or now.hour == 20 or now.hour == 23:
    #    if  now.minute == 0 or now.minute == 30:
    # 4시간마다
    #if now.hour == 0 or now.hour == 4 or now.hour == 8 or now.hour == 12 or now.hour == 16 or now.hour == 20 and now.minute == 30:
    # 특정시간에만
    #if now.hour == 3 and now.minute == 30 and 50 <= now.second <= 59:
    print(f"{now} | 시간 테스트중")
    print("")

    time.sleep(1)