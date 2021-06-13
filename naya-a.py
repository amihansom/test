import pyupbit
import time
import datetime

from requests.models import parse_header_links


################
##### 함수 #####

# 돌파매매용 목표가 조회.
# ticker = 코인명
def cal_target(ticker):
    # 코인 데이타 불러오기
    df = pyupbit.get_ohlcv(ticker, "day")
    # 어제 값 가져오기
    yesterday = df.iloc[-2]
    # 오늘 값 가져오기
    today = df.iloc[-1]
    # 어제 값의 변동성 값 구하기 = 어제 최고가 - 어제 최저가
    yesterday_range = yesterday['high'] - yesterday['low']
    # 금일 변동폭 = 금일 시작가 + 변동폭 * 0.5
    target = today['open'] + yesterday_range * 0.5
    return target

# 20 이동평균선 조회.
def get_ma20(ticker):
    # interval 받는 시간 "minute1", "minute5", "minute10", "minute20", "minute60"(1시간), "minute240"(4시간), "day", "week" 등등
    df = pyupbit.get_ohlcv(ticker, interval="minute60", count=20)
    ma20 = df['close'].rolling(20).mean().iloc[-1]
    return ma20
    


#엑세스키, 시크릿키 가져오기
access = "aFU3balSDNODIEENihFta23gfpF1aqgeduofjFnA"
secret = "LGQiWDaQWx9UDI4AqgS6rk41h55LrnoqCq9of3nL"



# 코인명 가져오기
coin1 = "BTC"
coin2 = "ETH"
coin3 = "ADA"
coin4 = "DOGE"
coin5 = "XRP"

coin6 = "DOT"
coin7 = "BCH"
coin8 = "LTC"
coin9 = "LINK"
coin10 = "THETA"

coin11 = "XLM"
coin12 = "ETC"
coin13 = "TRX"
coin14 = "EOS"
coin15 = "NEO"

coin16 = "BSV"
coin17 = "CRO"
coin18 = "IOTA"
coin19 = "ATOM"
coin20 = "XTZ"

coin21 = "HBAR"
coin22 = "CHZ"
coin23 = "XEM"
coin24 = "ZIL"
coin25 = "ENJ"

coin26 = "BTG"
coin27 = "BAT"
coin28 = "MANA"
coin29 = "STX"
coin30 = "SC"

coin31 = "ZRX"
coin32 = "OMG"
coin33 = "IOST"
coin34 = "ANKR"
coin35 = "FLOW"

coin36 = "ICX"
coin37 = "LSK"
coin38 = "BCHA"
coin39 = "SNT"
coin40 = "PUNDIX"




# 엑세스키, 시크릿키 로그인 시도
# class instance, object
upbit = pyupbit.Upbit(access, secret)



# 원화코인 변수 설정
krw_coin1 = "KRW-" + coin1
krw_coin2 = "KRW-" + coin2
krw_coin3 = "KRW-" + coin3
krw_coin4 = "KRW-" + coin4
krw_coin5 = "KRW-" + coin5
krw_coin6 = "KRW-" + coin6
krw_coin7 = "KRW-" + coin7
krw_coin8 = "KRW-" + coin8
krw_coin9 = "KRW-" + coin9
krw_coin10 = "KRW-" + coin10
krw_coin11 = "KRW-" + coin11
krw_coin12 = "KRW-" + coin12
krw_coin13 = "KRW-" + coin13
krw_coin14 = "KRW-" + coin14
krw_coin15 = "KRW-" + coin15
krw_coin16 = "KRW-" + coin16
krw_coin17 = "KRW-" + coin17
krw_coin18 = "KRW-" + coin18
krw_coin19 = "KRW-" + coin19
krw_coin20 = "KRW-" + coin20
krw_coin21 = "KRW-" + coin21
krw_coin22 = "KRW-" + coin22
krw_coin23 = "KRW-" + coin23
krw_coin24 = "KRW-" + coin24
krw_coin25 = "KRW-" + coin25
krw_coin26 = "KRW-" + coin26
krw_coin27 = "KRW-" + coin27
krw_coin28 = "KRW-" + coin28
krw_coin29 = "KRW-" + coin29
krw_coin30 = "KRW-" + coin30
krw_coin31 = "KRW-" + coin31
krw_coin32 = "KRW-" + coin32
krw_coin33 = "KRW-" + coin33
krw_coin34 = "KRW-" + coin34
krw_coin35 = "KRW-" + coin35
krw_coin36 = "KRW-" + coin36
krw_coin37 = "KRW-" + coin37
krw_coin38 = "KRW-" + coin38
krw_coin39 = "KRW-" + coin39
krw_coin40 = "KRW-" + coin40



# 금일매수가능 불가
op_mode1 = False
op_mode2 = False
op_mode3 = False
op_mode4 = False
op_mode5 = False
op_mode6 = False
op_mode7 = False
op_mode8 = False
op_mode9 = False
op_mode10 = False
op_mode11 = False
op_mode12 = False
op_mode13 = False
op_mode14 = False
op_mode15 = False
op_mode16 = False
op_mode17 = False
op_mode18 = False
op_mode19 = False
op_mode20 = False
op_mode21 = False
op_mode22 = False
op_mode23 = False
op_mode24 = False
op_mode25 = False
op_mode26 = False
op_mode27 = False
op_mode28 = False
op_mode29 = False
op_mode30 = False
op_mode31 = False
op_mode32 = False
op_mode33 = False
op_mode34 = False
op_mode35 = False
op_mode36 = False
op_mode37 = False
op_mode38 = False
op_mode39 = False
op_mode40 = False






print("")
print("")
print("---------- ---------- ---------- ---------- ----------")
print(" -----=====     매매시작전 보유 코인 현황     =====----- ")
print("---------- ---------- ---------- ---------- ----------")
print("")
print("")


######################################################################################################################################################
######################################################################################################################################################
######################################################################################################################################################


########################
##### 보유 코인 현황 ####

##### 1. 코인
# 보유수량 불러오기
krw_balance1 = upbit.get_balance(krw_coin1)
# 코인 현재가 불러오기
price1 = pyupbit.get_current_price(krw_coin1)
# 보유코인 원화금액으로 계산하기
bp1 = price1 * krw_balance1
# 코인 현황 출력.
print(f"1. 코인명 : {coin1}  |  현재가 = ￦{price1}  |  보유수량 = {krw_balance1}  |  평가금액 = ￦{bp1}")
# 코인 보유 유무
if bp1 > 10100:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode1 = False

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 보유중  |  매수가능 - {op_mode1} - 매수불가")
    print("")
else:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode1 = True

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 없음  |  매수가능 - {op_mode1} - 매수가능")
    print("")
time.sleep(1)


##### 2. 코인
# 보유수량 불러오기
krw_balance2 = upbit.get_balance(krw_coin2)
# 코인 현재가 불러오기
price2 = pyupbit.get_current_price(krw_coin2)
# 보유코인 원화금액으로 계산하기
bp2 = price2 * krw_balance2
# 코인 현황 출력.
print(f"2. 코인명 : {coin2}  |  현재가 = ￦{price2}  |  보유수량 = {krw_balance2}  |  평가금액 = ￦{bp2}")
# 코인 보유 유무
if bp2 > 10100:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode2 = False

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 보유중  |  매수가능 - {op_mode2} - 매수불가")
    print("")
else:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode2 = True

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 없음  |  매수가능 - {op_mode2} - 매수가능")
    print("")
time.sleep(1)


##### 3. 코인
# 보유수량 불러오기
krw_balance3 = upbit.get_balance(krw_coin3)
# 코인 현재가 불러오기
price3 = pyupbit.get_current_price(krw_coin3)
# 보유코인 원화금액으로 계산하기
bp3 = price3 * krw_balance3
# 코인 현황 출력.
print(f"3. 코인명 : {coin3}  |  현재가 = ￦{price3}  |  보유수량 = {krw_balance3}  |  평가금액 = ￦{bp3}")
# 코인 보유 유무
if bp3 > 10100:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode3 = False

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 보유중  |  매수가능 - {op_mode3} - 매수불가")
    print("")
else:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode3 = True

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 없음  |  매수가능 - {op_mode3} - 매수가능")
    print("")
time.sleep(1)


##### 4. 코인
# 보유수량 불러오기
krw_balance4 = upbit.get_balance(krw_coin4)
# 코인 현재가 불러오기
price4 = pyupbit.get_current_price(krw_coin4)
# 보유코인 원화금액으로 계산하기
bp4 = price4 * krw_balance4
# 코인 현황 출력.
print(f"4. 코인명 : {coin4}  |  현재가 = ￦{price4}  |  보유수량 = {krw_balance4}  |  평가금액 = ￦{bp4}")
# 코인 보유 유무
if bp4 > 10100:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode4 = False
    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 보유중  |  매수가능 - {op_mode4} - 매수불가")
    print("")
else:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode4 = True

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 없음  |  매수가능 - {op_mode4} - 매수가능")
    print("")
time.sleep(1)


##### 5. 코인
# 보유수량 불러오기
krw_balance5 = upbit.get_balance(krw_coin5)
# 코인 현재가 불러오기
price5 = pyupbit.get_current_price(krw_coin5)
# 보유코인 원화금액으로 계산하기
bp5 = price5 * krw_balance5
# 코인 현황 출력.
print(f"5. 코인명 : {coin5}  |  현재가 = ￦{price5}  |  보유수량 = {krw_balance5}  |  평가금액 = ￦{bp5}")
# 코인 보유 유무
if bp5 > 10100:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode5 = False

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 보유중  |  매수가능 - {op_mode5} - 매수불가")
    print("")
else:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode5 = True

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 없음  |  매수가능 - {op_mode5} - 매수가능")
    print("")
time.sleep(1)


##### 6. 코인
# 보유수량 불러오기
krw_balance6 = upbit.get_balance(krw_coin6)
# 코인 현재가 불러오기
price6 = pyupbit.get_current_price(krw_coin6)
# 보유코인 원화금액으로 계산하기
bp6 = price6 * krw_balance6
# 코인 현황 출력.
print(f"6. 코인명 : {coin6}  |  현재가 = ￦{price6}  |  보유수량 = {krw_balance6}  |  평가금액 = ￦{bp6}")
# 코인 보유 유무
if bp6 > 10100:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode6 = False

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 보유중  |  매수가능 - {op_mode6} - 매수불가")
    print("")
else:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode6 = True

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 없음  |  매수가능 - {op_mode6} - 매수가능")
    print("")
time.sleep(1)


##### 7. 코인
# 보유수량 불러오기
krw_balance7 = upbit.get_balance(krw_coin7)
# 코인 현재가 불러오기
price7 = pyupbit.get_current_price(krw_coin7)
# 보유코인 원화금액으로 계산하기
bp7 = price7 * krw_balance7
# 코인 현황 출력.
print(f"7. 코인명 : {coin7}  |  현재가 = ￦{price7}  |  보유수량 = {krw_balance7}  |  평가금액 = ￦{bp7}")
# 코인 보유 유무
if bp7 > 10100:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode7 = False

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 보유중  |  매수가능 - {op_mode7} - 매수불가")
    print("")
else:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode7 = True

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 없음  |  매수가능 - {op_mode7} - 매수가능")
    print("")
time.sleep(1)


##### 8. 코인
# 보유수량 불러오기
krw_balance8 = upbit.get_balance(krw_coin8)
# 코인 현재가 불러오기
price8 = pyupbit.get_current_price(krw_coin8)
# 보유코인 원화금액으로 계산하기
bp8 = price8 * krw_balance8
# 코인 현황 출력.
print(f"8. 코인명 : {coin8}  |  현재가 = ￦{price8}  |  보유수량 = {krw_balance8}  |  평가금액 = ￦{bp8}")
# 코인 보유 유무
if bp8 > 10100:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode8 = False

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 보유중  |  매수가능 - {op_mode8} - 매수불가")
    print("")
else:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode8 = True

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 없음  |  매수가능 - {op_mode8} - 매수가능")
    print("")
time.sleep(1)


##### 9. 코인
# 보유수량 불러오기
krw_balance9 = upbit.get_balance(krw_coin9)
# 코인 현재가 불러오기
price9 = pyupbit.get_current_price(krw_coin9)
# 보유코인 원화금액으로 계산하기
bp9 = price9 * krw_balance9
# 코인 현황 출력.
print(f"9. 코인명 : {coin9}  |  현재가 = ￦{price9}  |  보유수량 = {krw_balance9}  |  평가금액 = ￦{bp9}")
# 코인 보유 유무
if bp9 > 10100:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode9 = False

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 보유중  |  매수가능 - {op_mode9} - 매수불가")
    print("")
else:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode9 = True

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 없음  |  매수가능 - {op_mode9} - 매수가능")
    print("")
time.sleep(1)


##### 10. 코인
# 보유수량 불러오기
krw_balance10 = upbit.get_balance(krw_coin10)
# 코인 현재가 불러오기
price10 = pyupbit.get_current_price(krw_coin10)
# 보유코인 원화금액으로 계산하기
bp10 = price10 * krw_balance10
# 코인 현황 출력.
print(f"10. 코인명 : {coin10}  |  현재가 = ￦{price10}  |  보유수량 = {krw_balance10}  |  평가금액 = ￦{bp10}")
# 코인 보유 유무
if bp10 > 10100:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode10 = False

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 보유중  |  매수가능 - {op_mode10} - 매수불가")
    print("")
else:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode10 = True

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 없음  |  매수가능 - {op_mode10} - 매수가능")
    print("")
time.sleep(1)


######################################################################################################################################################
######################################################################################################################################################
######################################################################################################################################################


##### 11. 코인
# 보유수량 불러오기
krw_balance11 = upbit.get_balance(krw_coin11)
# 코인 현재가 불러오기
price11 = pyupbit.get_current_price(krw_coin11)
# 보유코인 원화금액으로 계산하기
bp11 = price11 * krw_balance11
# 코인 현황 출력.
print(f"11. 코인명 : {coin11}  |  현재가 = ￦{price11}  |  보유수량 = {krw_balance11}  |  평가금액 = ￦{bp11}")
# 코인 보유 유무
if bp11 > 10100:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode11 = False

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 보유중  |  매수가능 - {op_mode11} - 매수불가")
    print("")
else:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode11 = True

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 없음  |  매수가능 - {op_mode11} - 매수가능")
    print("")
time.sleep(1)


##### 12. 코인
# 보유수량 불러오기
krw_balance12 = upbit.get_balance(krw_coin12)
# 코인 현재가 불러오기
price12 = pyupbit.get_current_price(krw_coin12)
# 보유코인 원화금액으로 계산하기
bp12 = price12 * krw_balance12
# 코인 현황 출력.
print(f"12. 코인명 : {coin12}  |  현재가 = ￦{price12}  |  보유수량 = {krw_balance12}  |  평가금액 = ￦{bp12}")
# 코인 보유 유무
if bp12 > 10100:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode12 = False

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 보유중  |  매수가능 - {op_mode12} - 매수불가")
    print("")
else:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode12 = True

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 없음  |  매수가능 - {op_mode12} - 매수가능")
    print("")
time.sleep(1)


##### 13. 코인
# 보유수량 불러오기
krw_balance13 = upbit.get_balance(krw_coin13)
# 코인 현재가 불러오기
price13 = pyupbit.get_current_price(krw_coin13)
# 보유코인 원화금액으로 계산하기
bp13 = price13 * krw_balance13
# 코인 현황 출력.
print(f"13. 코인명 : {coin13}  |  현재가 = ￦{price13}  |  보유수량 = {krw_balance13}  |  평가금액 = ￦{bp13}")
# 코인 보유 유무
if bp13 > 10100:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode13 = False

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 보유중  |  매수가능 - {op_mode13} - 매수불가")
    print("")
else:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode13 = True

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 없음  |  매수가능 - {op_mode13} - 매수가능")
    print("")
time.sleep(1)


##### 14. 코인
# 보유수량 불러오기
krw_balance14 = upbit.get_balance(krw_coin14)
# 코인 현재가 불러오기
price14 = pyupbit.get_current_price(krw_coin14)
# 보유코인 원화금액으로 계산하기
bp14 = price14 * krw_balance14
# 코인 현황 출력.
print(f"14. 코인명 : {coin14}  |  현재가 = ￦{price14}  |  보유수량 = {krw_balance14}  |  평가금액 = ￦{bp14}")
# 코인 보유 유무
if bp14 > 10100:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode14 = False
    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 보유중  |  매수가능 - {op_mode14} - 매수불가")
    print("")
else:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode14 = True

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 없음  |  매수가능 - {op_mode14} - 매수가능")
    print("")
time.sleep(1)


##### 15. 코인
# 보유수량 불러오기
krw_balance15 = upbit.get_balance(krw_coin15)
# 코인 현재가 불러오기
price15 = pyupbit.get_current_price(krw_coin15)
# 보유코인 원화금액으로 계산하기
bp15 = price15 * krw_balance15
# 코인 현황 출력.
print(f"15. 코인명 : {coin15}  |  현재가 = ￦{price15}  |  보유수량 = {krw_balance15}  |  평가금액 = ￦{bp15}")
# 코인 보유 유무
if bp15 > 10100:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode15 = False

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 보유중  |  매수가능 - {op_mode15} - 매수불가")
    print("")
else:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode15 = True

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 없음  |  매수가능 - {op_mode15} - 매수가능")
    print("")
time.sleep(1)


##### 16. 코인
# 보유수량 불러오기
krw_balance16 = upbit.get_balance(krw_coin16)
# 코인 현재가 불러오기
price16 = pyupbit.get_current_price(krw_coin16)
# 보유코인 원화금액으로 계산하기
bp16 = price16 * krw_balance16
# 코인 현황 출력.
print(f"16. 코인명 : {coin16}  |  현재가 = ￦{price16}  |  보유수량 = {krw_balance16}  |  평가금액 = ￦{bp16}")
# 코인 보유 유무
if bp16 > 10100:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode16 = False

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 보유중  |  매수가능 - {op_mode16} - 매수불가")
    print("")
else:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode16 = True

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 없음  |  매수가능 - {op_mode16} - 매수가능")
    print("")
time.sleep(1)


##### 17. 코인
# 보유수량 불러오기
krw_balance17 = upbit.get_balance(krw_coin17)
# 코인 현재가 불러오기
price17 = pyupbit.get_current_price(krw_coin17)
# 보유코인 원화금액으로 계산하기
bp17 = price17 * krw_balance17
# 코인 현황 출력.
print(f"17. 코인명 : {coin17}  |  현재가 = ￦{price17}  |  보유수량 = {krw_balance17}  |  평가금액 = ￦{bp17}")
# 코인 보유 유무
if bp17 > 10100:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode17 = False

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 보유중  |  매수가능 - {op_mode17} - 매수불가")
    print("")
else:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode17 = True

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 없음  |  매수가능 - {op_mode17} - 매수가능")
    print("")
time.sleep(1)


##### 18. 코인
# 보유수량 불러오기
krw_balance18 = upbit.get_balance(krw_coin18)
# 코인 현재가 불러오기
price18 = pyupbit.get_current_price(krw_coin18)
# 보유코인 원화금액으로 계산하기
bp18 = price18 * krw_balance18
# 코인 현황 출력.
print(f"18. 코인명 : {coin18}  |  현재가 = ￦{price18}  |  보유수량 = {krw_balance18}  |  평가금액 = ￦{bp18}")
# 코인 보유 유무
if bp18 > 10100:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode18 = False

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 보유중  |  매수가능 - {op_mode18} - 매수불가")
    print("")
else:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode18 = True

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 없음  |  매수가능 - {op_mode18} - 매수가능")
    print("")
time.sleep(1)


##### 19. 코인
# 보유수량 불러오기
krw_balance19 = upbit.get_balance(krw_coin19)
# 코인 현재가 불러오기
price19 = pyupbit.get_current_price(krw_coin19)
# 보유코인 원화금액으로 계산하기
bp19 = price19 * krw_balance19
# 코인 현황 출력.
print(f"19. 코인명 : {coin19}  |  현재가 = ￦{price19}  |  보유수량 = {krw_balance19}  |  평가금액 = ￦{bp19}")
# 코인 보유 유무
if bp19 > 10100:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode19 = False

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 보유중  |  매수가능 - {op_mode19} - 매수불가")
    print("")
else:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode19 = True

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 없음  |  매수가능 - {op_mode19} - 매수가능")
    print("")
time.sleep(1)


##### 20. 코인
# 보유수량 불러오기
krw_balance20 = upbit.get_balance(krw_coin20)
# 코인 현재가 불러오기
price20 = pyupbit.get_current_price(krw_coin20)
# 보유코인 원화금액으로 계산하기
bp20 = price20 * krw_balance20
# 코인 현황 출력.
print(f"20. 코인명 : {coin20}  |  현재가 = ￦{price20}  |  보유수량 = {krw_balance20}  |  평가금액 = ￦{bp20}")
# 코인 보유 유무
if bp20 > 10100:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode20 = False

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 보유중  |  매수가능 - {op_mode20} - 매수불가")
    print("")
else:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode20 = True

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 없음  |  매수가능 - {op_mode20} - 매수가능")
    print("")
time.sleep(1)


######################################################################################################################################################
######################################################################################################################################################
######################################################################################################################################################


##### 21. 코인
# 보유수량 불러오기
krw_balance21 = upbit.get_balance(krw_coin21)
# 코인 현재가 불러오기
price21 = pyupbit.get_current_price(krw_coin21)
# 보유코인 원화금액으로 계산하기
bp21 = price21 * krw_balance21
# 코인 현황 출력.
print(f"21. 코인명 : {coin21}  |  현재가 = ￦{price21}  |  보유수량 = {krw_balance21}  |  평가금액 = ￦{bp21}")
# 코인 보유 유무
if bp21 > 10100:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode21 = False

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 보유중  |  매수가능 - {op_mode21} - 매수불가")
    print("")
else:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode21 = True

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 없음  |  매수가능 - {op_mode21} - 매수가능")
    print("")
time.sleep(1)


##### 22. 코인
# 보유수량 불러오기
krw_balance22 = upbit.get_balance(krw_coin22)
# 코인 현재가 불러오기
price22 = pyupbit.get_current_price(krw_coin22)
# 보유코인 원화금액으로 계산하기
bp22 = price22 * krw_balance22
# 코인 현황 출력.
print(f"22. 코인명 : {coin22}  |  현재가 = ￦{price22}  |  보유수량 = {krw_balance22}  |  평가금액 = ￦{bp22}")
# 코인 보유 유무
if bp22 > 10100:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode22 = False

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 보유중  |  매수가능 - {op_mode22} - 매수불가")
    print("")
else:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode22 = True

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 없음  |  매수가능 - {op_mode22} - 매수가능")
    print("")
time.sleep(1)


##### 23. 코인
# 보유수량 불러오기
krw_balance23 = upbit.get_balance(krw_coin23)
# 코인 현재가 불러오기
price23 = pyupbit.get_current_price(krw_coin23)
# 보유코인 원화금액으로 계산하기
bp23 = price23 * krw_balance23
# 코인 현황 출력.
print(f"23. 코인명 : {coin23}  |  현재가 = ￦{price23}  |  보유수량 = {krw_balance23}  |  평가금액 = ￦{bp23}")
# 코인 보유 유무
if bp23 > 10100:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode23 = False

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 보유중  |  매수가능 - {op_mode23} - 매수불가")
    print("")
else:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode23 = True

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 없음  |  매수가능 - {op_mode23} - 매수가능")
    print("")
time.sleep(1)


##### 24. 코인
# 보유수량 불러오기
krw_balance24 = upbit.get_balance(krw_coin24)
# 코인 현재가 불러오기
price24 = pyupbit.get_current_price(krw_coin24)
# 보유코인 원화금액으로 계산하기
bp24 = price24 * krw_balance24
# 코인 현황 출력.
print(f"24. 코인명 : {coin24}  |  현재가 = ￦{price24}  |  보유수량 = {krw_balance24}  |  평가금액 = ￦{bp24}")
# 코인 보유 유무
if bp24 > 10100:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode24 = False
    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 보유중  |  매수가능 - {op_mode24} - 매수불가")
    print("")
else:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode24 = True

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 없음  |  매수가능 - {op_mode24} - 매수가능")
    print("")
time.sleep(1)


##### 25. 코인
# 보유수량 불러오기
krw_balance25 = upbit.get_balance(krw_coin25)
# 코인 현재가 불러오기
price25 = pyupbit.get_current_price(krw_coin25)
# 보유코인 원화금액으로 계산하기
bp25 = price25 * krw_balance25
# 코인 현황 출력.
print(f"25. 코인명 : {coin25}  |  현재가 = ￦{price25}  |  보유수량 = {krw_balance25}  |  평가금액 = ￦{bp25}")
# 코인 보유 유무
if bp25 > 10100:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode25 = False

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 보유중  |  매수가능 - {op_mode25} - 매수불가")
    print("")
else:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode25 = True

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 없음  |  매수가능 - {op_mode25} - 매수가능")
    print("")
time.sleep(1)


##### 26. 코인
# 보유수량 불러오기
krw_balance26 = upbit.get_balance(krw_coin26)
# 코인 현재가 불러오기
price26 = pyupbit.get_current_price(krw_coin26)
# 보유코인 원화금액으로 계산하기
bp26 = price26 * krw_balance26
# 코인 현황 출력.
print(f"26. 코인명 : {coin26}  |  현재가 = ￦{price26}  |  보유수량 = {krw_balance26}  |  평가금액 = ￦{bp26}")
# 코인 보유 유무
if bp26 > 10100:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode26 = False

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 보유중  |  매수가능 - {op_mode26} - 매수불가")
    print("")
else:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode26 = True

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 없음  |  매수가능 - {op_mode26} - 매수가능")
    print("")
time.sleep(1)


##### 27. 코인
# 보유수량 불러오기
krw_balance27 = upbit.get_balance(krw_coin27)
# 코인 현재가 불러오기
price27 = pyupbit.get_current_price(krw_coin27)
# 보유코인 원화금액으로 계산하기
bp27 = price27 * krw_balance27
# 코인 현황 출력.
print(f"27. 코인명 : {coin27}  |  현재가 = ￦{price27}  |  보유수량 = {krw_balance27}  |  평가금액 = ￦{bp27}")
# 코인 보유 유무
if bp27 > 10100:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode27 = False

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 보유중  |  매수가능 - {op_mode27} - 매수불가")
    print("")
else:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode27 = True

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 없음  |  매수가능 - {op_mode27} - 매수가능")
    print("")
time.sleep(1)


##### 28. 코인
# 보유수량 불러오기
krw_balance28 = upbit.get_balance(krw_coin28)
# 코인 현재가 불러오기
price28 = pyupbit.get_current_price(krw_coin28)
# 보유코인 원화금액으로 계산하기
bp28 = price28 * krw_balance28
# 코인 현황 출력.
print(f"28. 코인명 : {coin28}  |  현재가 = ￦{price28}  |  보유수량 = {krw_balance28}  |  평가금액 = ￦{bp28}")
# 코인 보유 유무
if bp28 > 10100:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode28 = False

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 보유중  |  매수가능 - {op_mode28} - 매수불가")
    print("")
else:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode28 = True

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 없음  |  매수가능 - {op_mode28} - 매수가능")
    print("")
time.sleep(1)


##### 29. 코인
# 보유수량 불러오기
krw_balance29 = upbit.get_balance(krw_coin29)
# 코인 현재가 불러오기
price29 = pyupbit.get_current_price(krw_coin29)
# 보유코인 원화금액으로 계산하기
bp29 = price29 * krw_balance29
# 코인 현황 출력.
print(f"29. 코인명 : {coin29}  |  현재가 = ￦{price29}  |  보유수량 = {krw_balance29}  |  평가금액 = ￦{bp29}")
# 코인 보유 유무
if bp29 > 10100:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode29 = False

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 보유중  |  매수가능 - {op_mode29} - 매수불가")
    print("")
else:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode29 = True

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 없음  |  매수가능 - {op_mode29} - 매수가능")
    print("")
time.sleep(1)


##### 30. 코인
# 보유수량 불러오기
krw_balance30 = upbit.get_balance(krw_coin30)
# 코인 현재가 불러오기
price30 = pyupbit.get_current_price(krw_coin30)
# 보유코인 원화금액으로 계산하기
bp30 = price30 * krw_balance30
# 코인 현황 출력.
print(f"30. 코인명 : {coin30}  |  현재가 = ￦{price30}  |  보유수량 = {krw_balance30}  |  평가금액 = ￦{bp30}")
# 코인 보유 유무
if bp30 > 10100:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode30 = False

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 보유중  |  매수가능 - {op_mode30} - 매수불가")
    print("")
else:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode30 = True

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 없음  |  매수가능 - {op_mode30} - 매수가능")
    print("")
time.sleep(1)


######################################################################################################################################################
######################################################################################################################################################
######################################################################################################################################################


##### 31. 코인
# 보유수량 불러오기
krw_balance31 = upbit.get_balance(krw_coin31)
# 코인 현재가 불러오기
price31 = pyupbit.get_current_price(krw_coin31)
# 보유코인 원화금액으로 계산하기
bp31 = price31 * krw_balance31
# 코인 현황 출력.
print(f"31. 코인명 : {coin31}  |  현재가 = ￦{price31}  |  보유수량 = {krw_balance31}  |  평가금액 = ￦{bp31}")
# 코인 보유 유무
if bp31 > 10100:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode31 = False

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 보유중  |  매수가능 - {op_mode31} - 매수불가")
    print("")
else:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode31 = True

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 없음  |  매수가능 - {op_mode31} - 매수가능")
    print("")
time.sleep(1)


##### 32. 코인
# 보유수량 불러오기
krw_balance32 = upbit.get_balance(krw_coin32)
# 코인 현재가 불러오기
price32 = pyupbit.get_current_price(krw_coin32)
# 보유코인 원화금액으로 계산하기
bp32 = price32 * krw_balance32
# 코인 현황 출력.
print(f"32. 코인명 : {coin32}  |  현재가 = ￦{price32}  |  보유수량 = {krw_balance32}  |  평가금액 = ￦{bp32}")
# 코인 보유 유무
if bp32 > 10100:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode32 = False

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 보유중  |  매수가능 - {op_mode32} - 매수불가")
    print("")
else:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode32 = True

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 없음  |  매수가능 - {op_mode32} - 매수가능")
    print("")
time.sleep(1)


##### 33. 코인
# 보유수량 불러오기
krw_balance33 = upbit.get_balance(krw_coin33)
# 코인 현재가 불러오기
price33 = pyupbit.get_current_price(krw_coin33)
# 보유코인 원화금액으로 계산하기
bp33 = price33 * krw_balance33
# 코인 현황 출력.
print(f"33. 코인명 : {coin33}  |  현재가 = ￦{price33}  |  보유수량 = {krw_balance33}  |  평가금액 = ￦{bp33}")
# 코인 보유 유무
if bp33 > 10100:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode33 = False

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 보유중  |  매수가능 - {op_mode33} - 매수불가")
    print("")
else:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode33 = True

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 없음  |  매수가능 - {op_mode33} - 매수가능")
    print("")
time.sleep(1)


##### 34. 코인
# 보유수량 불러오기
krw_balance34 = upbit.get_balance(krw_coin34)
# 코인 현재가 불러오기
price34 = pyupbit.get_current_price(krw_coin34)
# 보유코인 원화금액으로 계산하기
bp34 = price34 * krw_balance34
# 코인 현황 출력.
print(f"34. 코인명 : {coin34}  |  현재가 = ￦{price34}  |  보유수량 = {krw_balance34}  |  평가금액 = ￦{bp34}")
# 코인 보유 유무
if bp34 > 10100:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode34 = False
    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 보유중  |  매수가능 - {op_mode34} - 매수불가")
    print("")
else:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode34 = True

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 없음  |  매수가능 - {op_mode34} - 매수가능")
    print("")
time.sleep(1)


##### 35. 코인
# 보유수량 불러오기
krw_balance35 = upbit.get_balance(krw_coin35)
# 코인 현재가 불러오기
price35 = pyupbit.get_current_price(krw_coin35)
# 보유코인 원화금액으로 계산하기
bp35 = price35 * krw_balance35
# 코인 현황 출력.
print(f"35. 코인명 : {coin35}  |  현재가 = ￦{price35}  |  보유수량 = {krw_balance35}  |  평가금액 = ￦{bp35}")
# 코인 보유 유무
if bp35 > 10100:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode35 = False

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 보유중  |  매수가능 - {op_mode35} - 매수불가")
    print("")
else:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode35 = True

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 없음  |  매수가능 - {op_mode35} - 매수가능")
    print("")
time.sleep(1)


##### 36. 코인
# 보유수량 불러오기
krw_balance36 = upbit.get_balance(krw_coin36)
# 코인 현재가 불러오기
price36 = pyupbit.get_current_price(krw_coin36)
# 보유코인 원화금액으로 계산하기
bp36 = price36 * krw_balance36
# 코인 현황 출력.
print(f"36. 코인명 : {coin36}  |  현재가 = ￦{price36}  |  보유수량 = {krw_balance36}  |  평가금액 = ￦{bp36}")
# 코인 보유 유무
if bp36 > 10100:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode36 = False

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 보유중  |  매수가능 - {op_mode36} - 매수불가")
    print("")
else:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode36 = True

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 없음  |  매수가능 - {op_mode36} - 매수가능")
    print("")
time.sleep(1)


##### 37. 코인
# 보유수량 불러오기
krw_balance37 = upbit.get_balance(krw_coin37)
# 코인 현재가 불러오기
price37 = pyupbit.get_current_price(krw_coin37)
# 보유코인 원화금액으로 계산하기
bp37 = price37 * krw_balance37
# 코인 현황 출력.
print(f"37. 코인명 : {coin37}  |  현재가 = ￦{price37}  |  보유수량 = {krw_balance37}  |  평가금액 = ￦{bp37}")
# 코인 보유 유무
if bp37 > 10100:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode37 = False

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 보유중  |  매수가능 - {op_mode37} - 매수불가")
    print("")
else:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode37 = True

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 없음  |  매수가능 - {op_mode37} - 매수가능")
    print("")
time.sleep(1)


##### 38. 코인
# 보유수량 불러오기
krw_balance38 = upbit.get_balance(krw_coin38)
# 코인 현재가 불러오기
price38 = pyupbit.get_current_price(krw_coin38)
# 보유코인 원화금액으로 계산하기
bp38 = price38 * krw_balance38
# 코인 현황 출력.
print(f"38. 코인명 : {coin38}  |  현재가 = ￦{price38}  |  보유수량 = {krw_balance38}  |  평가금액 = ￦{bp38}")
# 코인 보유 유무
if bp38 > 10100:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode38 = False

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 보유중  |  매수가능 - {op_mode38} - 매수불가")
    print("")
else:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode38 = True

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 없음  |  매수가능 - {op_mode38} - 매수가능")
    print("")
time.sleep(1)


##### 39. 코인
# 보유수량 불러오기
krw_balance39 = upbit.get_balance(krw_coin39)
# 코인 현재가 불러오기
price39 = pyupbit.get_current_price(krw_coin39)
# 보유코인 원화금액으로 계산하기
bp39 = price39 * krw_balance39
# 코인 현황 출력.
print(f"39. 코인명 : {coin39}  |  현재가 = ￦{price39}  |  보유수량 = {krw_balance39}  |  평가금액 = ￦{bp39}")
# 코인 보유 유무
if bp39 > 10100:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode39 = False

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 보유중  |  매수가능 - {op_mode39} - 매수불가")
    print("")
else:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode39 = True

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 없음  |  매수가능 - {op_mode39} - 매수가능")
    print("")
time.sleep(1)


##### 40. 코인
# 보유수량 불러오기
krw_balance40 = upbit.get_balance(krw_coin40)
# 코인 현재가 불러오기
price40 = pyupbit.get_current_price(krw_coin40)
# 보유코인 원화금액으로 계산하기
bp40 = price40 * krw_balance40
# 코인 현황 출력.
print(f"40. 코인명 : {coin40}  |  현재가 = ￦{price40}  |  보유수량 = {krw_balance40}  |  평가금액 = ￦{bp40}")
# 코인 보유 유무
if bp40 > 10100:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode40 = False

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 보유중  |  매수가능 - {op_mode40} - 매수불가")
    print("")
else:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode40 = True

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 없음  |  매수가능 - {op_mode40} - 매수가능")
    print("")
time.sleep(1)


######################################################################################################################################################
######################################################################################################################################################
######################################################################################################################################################


# 총 평가금액 계산
# 매수가능금액 불러오기
krw = upbit.get_balance("KRW")
##### 매수가능금액을 평균구하기
# 보유코인 합.
total_bp1 = krw + bp1 + bp2 + bp3 + bp4 + bp5 + bp6 + bp7 + bp8 + bp9 + bp10
total_bp2 = bp11 + bp12 + bp13 + bp14 + bp15 + bp16 + bp17 + bp18 + bp19 + bp20
total_bp3 = bp21 + bp22 + bp23 + bp24 + bp25 + bp26 + bp27 + bp28 + bp29 + bp30
total_bp4 = bp31 + bp32 + bp33 + bp34 + bp35 + bp36 + bp37 + bp38 + bp39 + bp40

total_bp0 = total_bp1 + total_bp2 + total_bp3 + total_bp4
# 보유코인 나누기
total_sum1 = total_bp1 / 5
total_sum2 = total_bp2 / 5
total_sum3 = total_bp3 / 5
total_sum4 = total_bp4 / 5
# 매수가능 평균가.
buy_krw = (total_sum1 + total_sum2 + total_sum3  + total_sum4) / 4


print(f" 총 평가금액 : ￦{total_bp0}")
print(f" 매수 평균가 : ￦{buy_krw}")



######################################################################################################################################################
######################################################################################################################################################
######################################################################################################################################################


print("")
print("")
print("---------- ---------- ---------- ---------- ----------")
print("-----=====           자동 매매 시작          =====----- ")
print("---------- ---------- ---------- ---------- ----------")
print("")
print("")


######################################################################################################################################################
######################################################################################################################################################
######################################################################################################################################################

while True:
    # 현재 시간 불러오기
    now = datetime.datetime.now()
    
    ###################################
    ########## 전체 매도 시도 ##########
    if now.hour == 8 and now.minute == 59:# and 20 <= now.second <= 59:   # 매매갯수(1초씩딜레이) 생각해서 초를 정해야 함.
        print("")
        print("==========================")
        print("= 09시 보유 코인 전량 매도 =")
        print("==========================")
        print("")


        ##### 1번코인 매도 시도 #####
        if op_mode1 == False:   # 매수 불가(False)일 경우 - 매도시도
            # 보유수량 불러오기
            krw_balance1 = upbit.get_balance(krw_coin1)
            # 현재가 불러오기
            price1 = pyupbit.get_current_price(krw_coin1)
            # 보유코인 원화금액으로 계산하기
            bp1 = price1 * krw_balance1

            # 보유코인 원화금액 매도시도
            if  bp1 > 10100:   # 보유코인 평가 금액이 10,100원 초과일때 - 매도시도
                # 매도할 코인명 - krw_coin1, 매도할 코인수량 - krw_balance1
                upbit.sell_market_order(krw_coin1, krw_balance1)

                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                op_mode1 = True

                # 1초 딜레이
                #time.sleep(1)
                # 보유수량 불러오기
                krw_balance1 = upbit.get_balance(krw_coin1)
                # 코인 현재가 불러오기
                price1 = pyupbit.get_current_price(krw_coin1)
                # 보유코인 원화금액으로 계산하기
                bp1 = price1 * krw_balance1

                # 보유 및 매수 가능 출력.
                print(f"[ 1. {krw_coin1} 매도완료. ]")
                print(f"매도시간 : {now}  |  코인명 : {coin1}  |  현재가 = ￦{price1}  |  보유수량 = {krw_balance1}  |  평가금액 = ￦{bp1}  |  매수가능 : {op_mode1} - 매수가능")
                print("")

            else:   # 보유코인 평가 금액이 10,100원 이하일때
                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                op_mode1 = True

                # 매수 가능 출력
                print(f"현재시간 : {now}  |  코인명 : {coin1}  |  매수가능 : {op_mode1} - 매수가능")

        # 1초 딜레이.
        #time.sleep(1)
        ##### 1번 코인 매도 완료 #####


        ##### 2번코인 매도 시도 #####
        if op_mode2 == False:   # 매수 불가(False)일 경우 - 매도시도
            # 보유수량 불러오기
            krw_balance2 = upbit.get_balance(krw_coin2)
            # 현재가 불러오기
            price2 = pyupbit.get_current_price(krw_coin2)
            # 보유코인 원화금액으로 계산하기
            bp2 = price2 * krw_balance2

            # 보유코인 원화금액 매도시도
            if  bp2 > 10100:   # 보유코인 평가 금액이 10,100원 초과일때 - 매도시도
                # 매도할 코인명 - krw_coin2, 매도할 코인수량 - krw_balance2
                upbit.sell_market_order(krw_coin2, krw_balance2)

                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                op_mode2 = True

                # 1초 딜레이
                #time.sleep(1)
                # 보유수량 불러오기
                krw_balance2 = upbit.get_balance(krw_coin2)
                # 코인 현재가 불러오기
                price2 = pyupbit.get_current_price(krw_coin2)
                # 보유코인 원화금액으로 계산하기
                bp2 = price2 * krw_balance2

                # 보유 및 매수 가능 출력.
                print(f"[ 2. {krw_coin2} 매도완료. ]")
                print(f"매도시간 : {now}  |  코인명 : {coin2}  |  현재가 = ￦{price2}  |  보유수량 = {krw_balance2}  |  평가금액 = ￦{bp2}  |  매수가능 : {op_mode2} - 매수가능")
                print("")

            else:   # 보유코인 평가 금액이 10,100원 이하일때
                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                op_mode2 = True

                # 매수 가능 출력
                print(f"현재시간 : {now}  |  코인명 : {coin2}  |  매수가능 : {op_mode2} - 매수가능")

        # 1초 딜레이.
        #time.sleep(1)
        ##### 2번 코인 매도 완료 #####


        ##### 3번코인 매도 시도 #####
        if op_mode3 == False:   # 매수 불가(False)일 경우 - 매도시도
            # 보유수량 불러오기
            krw_balance3 = upbit.get_balance(krw_coin3)
            # 현재가 불러오기
            price3 = pyupbit.get_current_price(krw_coin3)
            # 보유코인 원화금액으로 계산하기
            bp3 = price3 * krw_balance3

            # 보유코인 원화금액 매도시도
            if  bp3 > 10100:   # 보유코인 평가 금액이 10,100원 초과일때 - 매도시도
                # 매도할 코인명 - krw_coin3, 매도할 코인수량 - krw_balance3
                upbit.sell_market_order(krw_coin3, krw_balance3)

                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                op_mode3 = True

                # 1초 딜레이
                #time.sleep(1)
                # 보유수량 불러오기
                krw_balance3 = upbit.get_balance(krw_coin3)
                # 코인 현재가 불러오기
                price3 = pyupbit.get_current_price(krw_coin3)
                # 보유코인 원화금액으로 계산하기
                bp3 = price3 * krw_balance3

                # 보유 및 매수 가능 출력.
                print(f"[ 3. {krw_coin3} 매도완료. ]")
                print(f"매도시간 : {now}  |  코인명 : {coin3}  |  현재가 = ￦{price3}  |  보유수량 = {krw_balance3}  |  평가금액 = ￦{bp3}  |  매수가능 : {op_mode3} - 매수가능")
                print("")

            else:   # 보유코인 평가 금액이 10,100원 이하일때
                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                op_mode3 = True

                # 매수 가능 출력
                print(f"현재시간 : {now}  |  코인명 : {coin3}  |  매수가능 : {op_mode3} - 매수가능")

        # 1초 딜레이.
        #time.sleep(1)
        ##### 3번 코인 매도 완료 #####


        ##### 4번코인 매도 시도 #####
        if op_mode4 == False:   # 매수 불가(False)일 경우 - 매도시도
            # 보유수량 불러오기
            krw_balance4 = upbit.get_balance(krw_coin4)
            # 현재가 불러오기
            price4 = pyupbit.get_current_price(krw_coin4)
            # 보유코인 원화금액으로 계산하기
            bp4 = price4 * krw_balance4

            # 보유코인 원화금액 매도시도
            if  bp4 > 10100:   # 보유코인 평가 금액이 10,100원 초과일때 - 매도시도
                # 매도할 코인명 - krw_coin4, 매도할 코인수량 - krw_balance4
                upbit.sell_market_order(krw_coin4, krw_balance4)

                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                op_mode4 = True

                # 1초 딜레이
                #time.sleep(1)
                # 보유수량 불러오기
                krw_balance4 = upbit.get_balance(krw_coin4)
                # 코인 현재가 불러오기
                price4 = pyupbit.get_current_price(krw_coin4)
                # 보유코인 원화금액으로 계산하기
                bp4 = price4 * krw_balance4

                # 보유 및 매수 가능 출력.
                print(f"[ 4. {krw_coin4} 매도완료. ]")
                print(f"매도시간 : {now}  |  코인명 : {coin4}  |  현재가 = ￦{price4}  |  보유수량 = {krw_balance4}  |  평가금액 = ￦{bp4}  |  매수가능 : {op_mode4} - 매수가능")
                print("")

            else:   # 보유코인 평가 금액이 10,100원 이하일때
                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                op_mode4 = True

                # 매수 가능 출력
                print(f"현재시간 : {now}  |  코인명 : {coin4}  |  매수가능 : {op_mode4} - 매수가능")

        # 1초 딜레이.
        #time.sleep(1)
        ##### 4번 코인 매도 완료 #####


        ##### 5번코인 매도 시도 #####
        if op_mode5 == False:   # 매수 불가(False)일 경우 - 매도시도
            # 보유수량 불러오기
            krw_balance5 = upbit.get_balance(krw_coin5)
            # 현재가 불러오기
            price5 = pyupbit.get_current_price(krw_coin5)
            # 보유코인 원화금액으로 계산하기
            bp5 = price5 * krw_balance5

            # 보유코인 원화금액 매도시도
            if  bp5 > 10100:   # 보유코인 평가 금액이 10,100원 초과일때 - 매도시도
                # 매도할 코인명 - krw_coin5, 매도할 코인수량 - krw_balance5
                upbit.sell_market_order(krw_coin5, krw_balance5)

                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                op_mode5 = True

                # 1초 딜레이
                #time.sleep(1)
                # 보유수량 불러오기
                krw_balance5 = upbit.get_balance(krw_coin5)
                # 코인 현재가 불러오기
                price5 = pyupbit.get_current_price(krw_coin5)
                # 보유코인 원화금액으로 계산하기
                bp5 = price5 * krw_balance5

                # 보유 및 매수 가능 출력.
                print(f"[ 5. {krw_coin5} 매도완료. ]")
                print(f"매도시간 : {now}  |  코인명 : {coin5}  |  현재가 = ￦{price5}  |  보유수량 = {krw_balance5}  |  평가금액 = ￦{bp5}  |  매수가능 : {op_mode5} - 매수가능")
                print("")

            else:   # 보유코인 평가 금액이 10,100원 이하일때
                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                op_mode5 = True

                # 매수 가능 출력
                print(f"현재시간 : {now}  |  코인명 : {coin5}  |  매수가능 : {op_mode5} - 매수가능")

        # 1초 딜레이.
        #time.sleep(1)
        ##### 5번 코인 매도 완료 #####


        ##### 6번코인 매도 시도 #####
        if op_mode6 == False:   # 매수 불가(False)일 경우 - 매도시도
            # 보유수량 불러오기
            krw_balance6 = upbit.get_balance(krw_coin6)
            # 현재가 불러오기
            price6 = pyupbit.get_current_price(krw_coin6)
            # 보유코인 원화금액으로 계산하기
            bp6 = price6 * krw_balance6

            # 보유코인 원화금액 매도시도
            if  bp6 > 10100:   # 보유코인 평가 금액이 10,100원 초과일때 - 매도시도
                # 매도할 코인명 - krw_coin6, 매도할 코인수량 - krw_balance6
                upbit.sell_market_order(krw_coin6, krw_balance6)

                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                op_mode6 = True

                # 1초 딜레이
                #time.sleep(1)
                # 보유수량 불러오기
                krw_balance6 = upbit.get_balance(krw_coin6)
                # 코인 현재가 불러오기
                price6 = pyupbit.get_current_price(krw_coin6)
                # 보유코인 원화금액으로 계산하기
                bp6 = price6 * krw_balance6

                # 보유 및 매수 가능 출력.
                print(f"[ 6. {krw_coin6} 매도완료. ]")
                print(f"매도시간 : {now}  |  코인명 : {coin6}  |  현재가 = ￦{price6}  |  보유수량 = {krw_balance6}  |  평가금액 = ￦{bp6}  |  매수가능 : {op_mode6} - 매수가능")
                print("")

            else:   # 보유코인 평가 금액이 10,100원 이하일때
                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                op_mode6 = True

                # 매수 가능 출력
                print(f"현재시간 : {now}  |  코인명 : {coin6}  |  매수가능 : {op_mode6} - 매수가능")

        # 1초 딜레이.
        #time.sleep(1)
        ##### 6번 코인 매도 완료 #####


        ##### 7번코인 매도 시도 #####
        if op_mode7 == False:   # 매수 불가(False)일 경우 - 매도시도
            # 보유수량 불러오기
            krw_balance7 = upbit.get_balance(krw_coin7)
            # 현재가 불러오기
            price7 = pyupbit.get_current_price(krw_coin7)
            # 보유코인 원화금액으로 계산하기
            bp7 = price7 * krw_balance7

            # 보유코인 원화금액 매도시도
            if  bp7 > 10100:   # 보유코인 평가 금액이 10,100원 초과일때 - 매도시도
                # 매도할 코인명 - krw_coin7, 매도할 코인수량 - krw_balance7
                upbit.sell_market_order(krw_coin7, krw_balance7)

                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                op_mode7 = True

                # 1초 딜레이
                #time.sleep(1)
                # 보유수량 불러오기
                krw_balance7 = upbit.get_balance(krw_coin7)
                # 코인 현재가 불러오기
                price7 = pyupbit.get_current_price(krw_coin7)
                # 보유코인 원화금액으로 계산하기
                bp7 = price7 * krw_balance7

                # 보유 및 매수 가능 출력.
                print(f"[ 7. {krw_coin7} 매도완료. ]")
                print(f"매도시간 : {now}  |  코인명 : {coin7}  |  현재가 = ￦{price7}  |  보유수량 = {krw_balance7}  |  평가금액 = ￦{bp7}  |  매수가능 : {op_mode7} - 매수가능")
                print("")

            else:   # 보유코인 평가 금액이 10,100원 이하일때
                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                op_mode7 = True

                # 매수 가능 출력
                print(f"현재시간 : {now}  |  코인명 : {coin7}  |  매수가능 : {op_mode7} - 매수가능")

        # 1초 딜레이.
        #time.sleep(1)
        ##### 7번 코인 매도 완료 #####


        ##### 8번코인 매도 시도 #####
        if op_mode8 == False:   # 매수 불가(False)일 경우 - 매도시도
            # 보유수량 불러오기
            krw_balance8 = upbit.get_balance(krw_coin8)
            # 현재가 불러오기
            price8 = pyupbit.get_current_price(krw_coin8)
            # 보유코인 원화금액으로 계산하기
            bp8 = price8 * krw_balance8

            # 보유코인 원화금액 매도시도
            if  bp8 > 10100:   # 보유코인 평가 금액이 10,100원 초과일때 - 매도시도
                # 매도할 코인명 - krw_coin8, 매도할 코인수량 - krw_balance8
                upbit.sell_market_order(krw_coin8, krw_balance8)

                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                op_mode8 = True

                # 1초 딜레이
                #time.sleep(1)
                # 보유수량 불러오기
                krw_balance8 = upbit.get_balance(krw_coin8)
                # 코인 현재가 불러오기
                price8 = pyupbit.get_current_price(krw_coin8)
                # 보유코인 원화금액으로 계산하기
                bp8 = price8 * krw_balance8

                # 보유 및 매수 가능 출력.
                print(f"[ 8. {krw_coin8} 매도완료. ]")
                print(f"매도시간 : {now}  |  코인명 : {coin8}  |  현재가 = ￦{price8}  |  보유수량 = {krw_balance8}  |  평가금액 = ￦{bp8}  |  매수가능 : {op_mode8} - 매수가능")
                print("")

            else:   # 보유코인 평가 금액이 10,100원 이하일때
                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                op_mode8 = True

                # 매수 가능 출력
                print(f"현재시간 : {now}  |  코인명 : {coin8}  |  매수가능 : {op_mode8} - 매수가능")

        # 1초 딜레이.
        #time.sleep(1)
        ##### 8번 코인 매도 완료 #####


        ##### 9번코인 매도 시도 #####
        if op_mode9 == False:   # 매수 불가(False)일 경우 - 매도시도
            # 보유수량 불러오기
            krw_balance9 = upbit.get_balance(krw_coin9)
            # 현재가 불러오기
            price9 = pyupbit.get_current_price(krw_coin9)
            # 보유코인 원화금액으로 계산하기
            bp9 = price9 * krw_balance9

            # 보유코인 원화금액 매도시도
            if  bp9 > 10100:   # 보유코인 평가 금액이 10,100원 초과일때 - 매도시도
                # 매도할 코인명 - krw_coin9, 매도할 코인수량 - krw_balance9
                upbit.sell_market_order(krw_coin9, krw_balance9)

                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                op_mode9 = True

                # 1초 딜레이
                #time.sleep(1)
                # 보유수량 불러오기
                krw_balance9 = upbit.get_balance(krw_coin9)
                # 코인 현재가 불러오기
                price9 = pyupbit.get_current_price(krw_coin9)
                # 보유코인 원화금액으로 계산하기
                bp9 = price9 * krw_balance9

                # 보유 및 매수 가능 출력.
                print(f"[ 9. {krw_coin9} 매도완료. ]")
                print(f"매도시간 : {now}  |  코인명 : {coin9}  |  현재가 = ￦{price9}  |  보유수량 = {krw_balance9}  |  평가금액 = ￦{bp9}  |  매수가능 : {op_mode9} - 매수가능")
                print("")

            else:   # 보유코인 평가 금액이 10,100원 이하일때
                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                op_mode9 = True

                # 매수 가능 출력
                print(f"현재시간 : {now}  |  코인명 : {coin9}  |  매수가능 : {op_mode9} - 매수가능")

        # 1초 딜레이.
        #time.sleep(1)
        ##### 9번 코인 매도 완료 #####


        ##### 10번코인 매도 시도 #####
        if op_mode10 == False:   # 매수 불가(False)일 경우 - 매도시도
            # 보유수량 불러오기
            krw_balance10 = upbit.get_balance(krw_coin10)
            # 현재가 불러오기
            price10 = pyupbit.get_current_price(krw_coin10)
            # 보유코인 원화금액으로 계산하기
            bp10 = price10 * krw_balance10

            # 보유코인 원화금액 매도시도
            if  bp10 > 10100:   # 보유코인 평가 금액이 10,100원 초과일때 - 매도시도
                # 매도할 코인명 - krw_coin10, 매도할 코인수량 - krw_balance10
                upbit.sell_market_order(krw_coin10, krw_balance10)

                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                op_mode10 = True

                # 1초 딜레이
                #time.sleep(1)
                # 보유수량 불러오기
                krw_balance10 = upbit.get_balance(krw_coin10)
                # 코인 현재가 불러오기
                price10 = pyupbit.get_current_price(krw_coin10)
                # 보유코인 원화금액으로 계산하기
                bp10 = price10 * krw_balance10

                # 보유 및 매수 가능 출력.
                print(f"[ 10. {krw_coin10} 매도완료. ]")
                print(f"매도시간 : {now}  |  코인명 : {coin10}  |  현재가 = ￦{price10}  |  보유수량 = {krw_balance10}  |  평가금액 = ￦{bp10}  |  매수가능 : {op_mode10} - 매수가능")
                print("")

            else:   # 보유코인 평가 금액이 10,100원 이하일때
                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                op_mode10 = True

                # 매수 가능 출력
                print(f"현재시간 : {now}  |  코인명 : {coin10}  |  매수가능 : {op_mode10} - 매수가능")

        # 1초 딜레이.
        #time.sleep(1)
        ##### 10번 코인 매도 완료 #####


        ######################################################################################################################################################
        ######################################################################################################################################################
        ######################################################################################################################################################


        ##### 11번코인 매도 시도 #####
        if op_mode11 == False:   # 매수 불가(False)일 경우 - 매도시도
            # 보유수량 불러오기
            krw_balance11 = upbit.get_balance(krw_coin11)
            # 현재가 불러오기
            price11 = pyupbit.get_current_price(krw_coin11)
            # 보유코인 원화금액으로 계산하기
            bp11 = price11 * krw_balance11

            # 보유코인 원화금액 매도시도
            if  bp11 > 10100:   # 보유코인 평가 금액이 10,100원 초과일때 - 매도시도
                # 매도할 코인명 - krw_coin11, 매도할 코인수량 - krw_balance11
                upbit.sell_market_order(krw_coin11, krw_balance11)

                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                op_mode11 = True

                # 1초 딜레이
                #time.sleep(1)
                # 보유수량 불러오기
                krw_balance11 = upbit.get_balance(krw_coin11)
                # 코인 현재가 불러오기
                price11 = pyupbit.get_current_price(krw_coin11)
                # 보유코인 원화금액으로 계산하기
                bp11 = price11 * krw_balance11

                # 보유 및 매수 가능 출력.
                print(f"[ 11. {krw_coin11} 매도완료. ]")
                print(f"매도시간 : {now}  |  코인명 : {coin11}  |  현재가 = ￦{price11}  |  보유수량 = {krw_balance11}  |  평가금액 = ￦{bp11}  |  매수가능 : {op_mode11} - 매수가능")
                print("")

            else:   # 보유코인 평가 금액이 10,100원 이하일때
                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                op_mode11 = True

                # 매수 가능 출력
                print(f"현재시간 : {now}  |  코인명 : {coin11}  |  매수가능 : {op_mode11} - 매수가능")

        # 1초 딜레이.
        #time.sleep(1)
        ##### 11번 코인 매도 완료 #####


        ##### 12번코인 매도 시도 #####
        if op_mode12 == False:   # 매수 불가(False)일 경우 - 매도시도
            # 보유수량 불러오기
            krw_balance12 = upbit.get_balance(krw_coin12)
            # 현재가 불러오기
            price12 = pyupbit.get_current_price(krw_coin12)
            # 보유코인 원화금액으로 계산하기
            bp12 = price12 * krw_balance12

            # 보유코인 원화금액 매도시도
            if  bp12 > 10100:   # 보유코인 평가 금액이 10,100원 초과일때 - 매도시도
                # 매도할 코인명 - krw_coin12, 매도할 코인수량 - krw_balance12
                upbit.sell_market_order(krw_coin12, krw_balance12)

                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                op_mode12 = True

                # 1초 딜레이
                #time.sleep(1)
                # 보유수량 불러오기
                krw_balance12 = upbit.get_balance(krw_coin12)
                # 코인 현재가 불러오기
                price12 = pyupbit.get_current_price(krw_coin12)
                # 보유코인 원화금액으로 계산하기
                bp12 = price12 * krw_balance12

                # 보유 및 매수 가능 출력.
                print(f"[ 12. {krw_coin12} 매도완료. ]")
                print(f"매도시간 : {now}  |  코인명 : {coin12}  |  현재가 = ￦{price12}  |  보유수량 = {krw_balance12}  |  평가금액 = ￦{bp12}  |  매수가능 : {op_mode12} - 매수가능")
                print("")

            else:   # 보유코인 평가 금액이 10,100원 이하일때
                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                op_mode12 = True

                # 매수 가능 출력
                print(f"현재시간 : {now}  |  코인명 : {coin12}  |  매수가능 : {op_mode12} - 매수가능")

        # 1초 딜레이.
        #time.sleep(1)
        ##### 12번 코인 매도 완료 #####


        ##### 13번코인 매도 시도 #####
        if op_mode13 == False:   # 매수 불가(False)일 경우 - 매도시도
            # 보유수량 불러오기
            krw_balance13 = upbit.get_balance(krw_coin13)
            # 현재가 불러오기
            price13 = pyupbit.get_current_price(krw_coin13)
            # 보유코인 원화금액으로 계산하기
            bp13 = price13 * krw_balance13

            # 보유코인 원화금액 매도시도
            if  bp13 > 10100:   # 보유코인 평가 금액이 10,100원 초과일때 - 매도시도
                # 매도할 코인명 - krw_coin13, 매도할 코인수량 - krw_balance13
                upbit.sell_market_order(krw_coin13, krw_balance13)

                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                op_mode13 = True

                # 1초 딜레이
                #time.sleep(1)
                # 보유수량 불러오기
                krw_balance13 = upbit.get_balance(krw_coin13)
                # 코인 현재가 불러오기
                price13 = pyupbit.get_current_price(krw_coin13)
                # 보유코인 원화금액으로 계산하기
                bp13 = price13 * krw_balance13

                # 보유 및 매수 가능 출력.
                print(f"[ 13. {krw_coin13} 매도완료. ]")
                print(f"매도시간 : {now}  |  코인명 : {coin13}  |  현재가 = ￦{price13}  |  보유수량 = {krw_balance13}  |  평가금액 = ￦{bp13}  |  매수가능 : {op_mode13} - 매수가능")
                print("")

            else:   # 보유코인 평가 금액이 10,100원 이하일때
                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                op_mode13 = True

                # 매수 가능 출력
                print(f"현재시간 : {now}  |  코인명 : {coin13}  |  매수가능 : {op_mode13} - 매수가능")

        # 1초 딜레이.
        #time.sleep(1)
        ##### 13번 코인 매도 완료 #####


        ##### 14번코인 매도 시도 #####
        if op_mode14 == False:   # 매수 불가(False)일 경우 - 매도시도
            # 보유수량 불러오기
            krw_balance14 = upbit.get_balance(krw_coin14)
            # 현재가 불러오기
            price14 = pyupbit.get_current_price(krw_coin14)
            # 보유코인 원화금액으로 계산하기
            bp14 = price14 * krw_balance14

            # 보유코인 원화금액 매도시도
            if  bp14 > 10100:   # 보유코인 평가 금액이 10,100원 초과일때 - 매도시도
                # 매도할 코인명 - krw_coin14, 매도할 코인수량 - krw_balance14
                upbit.sell_market_order(krw_coin14, krw_balance14)

                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                op_mode14 = True

                # 1초 딜레이
                #time.sleep(1)
                # 보유수량 불러오기
                krw_balance14 = upbit.get_balance(krw_coin14)
                # 코인 현재가 불러오기
                price14 = pyupbit.get_current_price(krw_coin14)
                # 보유코인 원화금액으로 계산하기
                bp14 = price14 * krw_balance14

                # 보유 및 매수 가능 출력.
                print(f"[ 14. {krw_coin14} 매도완료. ]")
                print(f"매도시간 : {now}  |  코인명 : {coin14}  |  현재가 = ￦{price14}  |  보유수량 = {krw_balance14}  |  평가금액 = ￦{bp14}  |  매수가능 : {op_mode14} - 매수가능")
                print("")

            else:   # 보유코인 평가 금액이 10,100원 이하일때
                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                op_mode14 = True

                # 매수 가능 출력
                print(f"현재시간 : {now}  |  코인명 : {coin14}  |  매수가능 : {op_mode14} - 매수가능")

        # 1초 딜레이.
        #time.sleep(1)
        ##### 14번 코인 매도 완료 #####


        ##### 15번코인 매도 시도 #####
        if op_mode15 == False:   # 매수 불가(False)일 경우 - 매도시도
            # 보유수량 불러오기
            krw_balance15 = upbit.get_balance(krw_coin15)
            # 현재가 불러오기
            price15 = pyupbit.get_current_price(krw_coin15)
            # 보유코인 원화금액으로 계산하기
            bp15 = price15 * krw_balance15

            # 보유코인 원화금액 매도시도
            if  bp15 > 10100:   # 보유코인 평가 금액이 10,100원 초과일때 - 매도시도
                # 매도할 코인명 - krw_coin15, 매도할 코인수량 - krw_balance15
                upbit.sell_market_order(krw_coin15, krw_balance15)

                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                op_mode15 = True

                # 1초 딜레이
                #time.sleep(1)
                # 보유수량 불러오기
                krw_balance15 = upbit.get_balance(krw_coin15)
                # 코인 현재가 불러오기
                price15 = pyupbit.get_current_price(krw_coin15)
                # 보유코인 원화금액으로 계산하기
                bp15 = price15 * krw_balance15

                # 보유 및 매수 가능 출력.
                print(f"[ 15. {krw_coin15} 매도완료. ]")
                print(f"매도시간 : {now}  |  코인명 : {coin15}  |  현재가 = ￦{price15}  |  보유수량 = {krw_balance15}  |  평가금액 = ￦{bp15}  |  매수가능 : {op_mode15} - 매수가능")
                print("")

            else:   # 보유코인 평가 금액이 10,100원 이하일때
                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                op_mode15 = True

                # 매수 가능 출력
                print(f"현재시간 : {now}  |  코인명 : {coin15}  |  매수가능 : {op_mode15} - 매수가능")

        # 1초 딜레이.
        #time.sleep(1)
        ##### 15번 코인 매도 완료 #####


        ##### 16번코인 매도 시도 #####
        if op_mode16 == False:   # 매수 불가(False)일 경우 - 매도시도
            # 보유수량 불러오기
            krw_balance16 = upbit.get_balance(krw_coin16)
            # 현재가 불러오기
            price16 = pyupbit.get_current_price(krw_coin16)
            # 보유코인 원화금액으로 계산하기
            bp16 = price16 * krw_balance16

            # 보유코인 원화금액 매도시도
            if  bp16 > 10100:   # 보유코인 평가 금액이 10,100원 초과일때 - 매도시도
                # 매도할 코인명 - krw_coin16, 매도할 코인수량 - krw_balance16
                upbit.sell_market_order(krw_coin16, krw_balance16)

                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                op_mode16 = True

                # 1초 딜레이
                #time.sleep(1)
                # 보유수량 불러오기
                krw_balance16 = upbit.get_balance(krw_coin16)
                # 코인 현재가 불러오기
                price16 = pyupbit.get_current_price(krw_coin16)
                # 보유코인 원화금액으로 계산하기
                bp16 = price16 * krw_balance16

                # 보유 및 매수 가능 출력.
                print(f"[ 16. {krw_coin16} 매도완료. ]")
                print(f"매도시간 : {now}  |  코인명 : {coin16}  |  현재가 = ￦{price16}  |  보유수량 = {krw_balance16}  |  평가금액 = ￦{bp16}  |  매수가능 : {op_mode16} - 매수가능")
                print("")

            else:   # 보유코인 평가 금액이 10,100원 이하일때
                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                op_mode16 = True

                # 매수 가능 출력
                print(f"현재시간 : {now}  |  코인명 : {coin16}  |  매수가능 : {op_mode16} - 매수가능")

        # 1초 딜레이.
        #time.sleep(1)
        ##### 16번 코인 매도 완료 #####


        ##### 17번코인 매도 시도 #####
        if op_mode17 == False:   # 매수 불가(False)일 경우 - 매도시도
            # 보유수량 불러오기
            krw_balance17 = upbit.get_balance(krw_coin17)
            # 현재가 불러오기
            price17 = pyupbit.get_current_price(krw_coin17)
            # 보유코인 원화금액으로 계산하기
            bp17 = price17 * krw_balance17

            # 보유코인 원화금액 매도시도
            if  bp17 > 10100:   # 보유코인 평가 금액이 10,100원 초과일때 - 매도시도
                # 매도할 코인명 - krw_coin17, 매도할 코인수량 - krw_balance17
                upbit.sell_market_order(krw_coin17, krw_balance17)

                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                op_mode17 = True

                # 1초 딜레이
                #time.sleep(1)
                # 보유수량 불러오기
                krw_balance17 = upbit.get_balance(krw_coin17)
                # 코인 현재가 불러오기
                price17 = pyupbit.get_current_price(krw_coin17)
                # 보유코인 원화금액으로 계산하기
                bp17 = price17 * krw_balance17

                # 보유 및 매수 가능 출력.
                print(f"[ 17. {krw_coin17} 매도완료. ]")
                print(f"매도시간 : {now}  |  코인명 : {coin17}  |  현재가 = ￦{price17}  |  보유수량 = {krw_balance17}  |  평가금액 = ￦{bp17}  |  매수가능 : {op_mode17} - 매수가능")
                print("")

            else:   # 보유코인 평가 금액이 10,100원 이하일때
                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                op_mode17 = True

                # 매수 가능 출력
                print(f"현재시간 : {now}  |  코인명 : {coin17}  |  매수가능 : {op_mode17} - 매수가능")

        # 1초 딜레이.
        #time.sleep(1)
        ##### 17번 코인 매도 완료 #####


        ##### 18번코인 매도 시도 #####
        if op_mode18 == False:   # 매수 불가(False)일 경우 - 매도시도
            # 보유수량 불러오기
            krw_balance18 = upbit.get_balance(krw_coin18)
            # 현재가 불러오기
            price18 = pyupbit.get_current_price(krw_coin18)
            # 보유코인 원화금액으로 계산하기
            bp18 = price18 * krw_balance18

            # 보유코인 원화금액 매도시도
            if  bp18 > 10100:   # 보유코인 평가 금액이 10,100원 초과일때 - 매도시도
                # 매도할 코인명 - krw_coin18, 매도할 코인수량 - krw_balance18
                upbit.sell_market_order(krw_coin18, krw_balance18)

                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                op_mode18 = True

                # 1초 딜레이
                #time.sleep(1)
                # 보유수량 불러오기
                krw_balance18 = upbit.get_balance(krw_coin18)
                # 코인 현재가 불러오기
                price18 = pyupbit.get_current_price(krw_coin18)
                # 보유코인 원화금액으로 계산하기
                bp18 = price18 * krw_balance18

                # 보유 및 매수 가능 출력.
                print(f"[ 18. {krw_coin18} 매도완료. ]")
                print(f"매도시간 : {now}  |  코인명 : {coin18}  |  현재가 = ￦{price18}  |  보유수량 = {krw_balance18}  |  평가금액 = ￦{bp18}  |  매수가능 : {op_mode18} - 매수가능")
                print("")

            else:   # 보유코인 평가 금액이 10,100원 이하일때
                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                op_mode18 = True

                # 매수 가능 출력
                print(f"현재시간 : {now}  |  코인명 : {coin18}  |  매수가능 : {op_mode18} - 매수가능")

        # 1초 딜레이.
        #time.sleep(1)
        ##### 18번 코인 매도 완료 #####


        ##### 19번코인 매도 시도 #####
        if op_mode19 == False:   # 매수 불가(False)일 경우 - 매도시도
            # 보유수량 불러오기
            krw_balance19 = upbit.get_balance(krw_coin19)
            # 현재가 불러오기
            price19 = pyupbit.get_current_price(krw_coin19)
            # 보유코인 원화금액으로 계산하기
            bp19 = price19 * krw_balance19

            # 보유코인 원화금액 매도시도
            if  bp19 > 10100:   # 보유코인 평가 금액이 10,100원 초과일때 - 매도시도
                # 매도할 코인명 - krw_coin19, 매도할 코인수량 - krw_balance19
                upbit.sell_market_order(krw_coin19, krw_balance19)

                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                op_mode19 = True

                # 1초 딜레이
                #time.sleep(1)
                # 보유수량 불러오기
                krw_balance19 = upbit.get_balance(krw_coin19)
                # 코인 현재가 불러오기
                price19 = pyupbit.get_current_price(krw_coin19)
                # 보유코인 원화금액으로 계산하기
                bp19 = price19 * krw_balance19

                # 보유 및 매수 가능 출력.
                print(f"[ 19. {krw_coin19} 매도완료. ]")
                print(f"매도시간 : {now}  |  코인명 : {coin19}  |  현재가 = ￦{price19}  |  보유수량 = {krw_balance19}  |  평가금액 = ￦{bp19}  |  매수가능 : {op_mode19} - 매수가능")
                print("")

            else:   # 보유코인 평가 금액이 10,100원 이하일때
                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                op_mode19 = True

                # 매수 가능 출력
                print(f"현재시간 : {now}  |  코인명 : {coin19}  |  매수가능 : {op_mode19} - 매수가능")

        # 1초 딜레이.
        #time.sleep(1)
        ##### 19번 코인 매도 완료 #####


        ##### 20번코인 매도 시도 #####
        if op_mode20 == False:   # 매수 불가(False)일 경우 - 매도시도
            # 보유수량 불러오기
            krw_balance20 = upbit.get_balance(krw_coin20)
            # 현재가 불러오기
            price20 = pyupbit.get_current_price(krw_coin20)
            # 보유코인 원화금액으로 계산하기
            bp20 = price20 * krw_balance20

            # 보유코인 원화금액 매도시도
            if  bp20 > 10100:   # 보유코인 평가 금액이 10,100원 초과일때 - 매도시도
                # 매도할 코인명 - krw_coin20, 매도할 코인수량 - krw_balance20
                upbit.sell_market_order(krw_coin20, krw_balance20)

                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                op_mode20 = True

                # 1초 딜레이
                #time.sleep(1)
                # 보유수량 불러오기
                krw_balance20 = upbit.get_balance(krw_coin20)
                # 코인 현재가 불러오기
                price20 = pyupbit.get_current_price(krw_coin20)
                # 보유코인 원화금액으로 계산하기
                bp20 = price20 * krw_balance20

                # 보유 및 매수 가능 출력.
                print(f"[ 20. {krw_coin20} 매도완료. ]")
                print(f"매도시간 : {now}  |  코인명 : {coin20}  |  현재가 = ￦{price20}  |  보유수량 = {krw_balance20}  |  평가금액 = ￦{bp20}  |  매수가능 : {op_mode20} - 매수가능")
                print("")

            else:   # 보유코인 평가 금액이 10,100원 이하일때
                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                op_mode20 = True

                # 매수 가능 출력
                print(f"현재시간 : {now}  |  코인명 : {coin20}  |  매수가능 : {op_mode20} - 매수가능")

        # 1초 딜레이.
        #time.sleep(1)
        ##### 20번 코인 매도 완료 #####


        ######################################################################################################################################################
        ######################################################################################################################################################
        ######################################################################################################################################################


        ##### 21번코인 매도 시도 #####
        if op_mode21 == False:   # 매수 불가(False)일 경우 - 매도시도
            # 보유수량 불러오기
            krw_balance21 = upbit.get_balance(krw_coin21)
            # 현재가 불러오기
            price21 = pyupbit.get_current_price(krw_coin21)
            # 보유코인 원화금액으로 계산하기
            bp21 = price21 * krw_balance21

            # 보유코인 원화금액 매도시도
            if  bp21 > 10100:   # 보유코인 평가 금액이 10,100원 초과일때 - 매도시도
                # 매도할 코인명 - krw_coin21, 매도할 코인수량 - krw_balance21
                upbit.sell_market_order(krw_coin21, krw_balance21)

                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                op_mode21 = True

                # 1초 딜레이
                #time.sleep(1)
                # 보유수량 불러오기
                krw_balance21 = upbit.get_balance(krw_coin21)
                # 코인 현재가 불러오기
                price21 = pyupbit.get_current_price(krw_coin21)
                # 보유코인 원화금액으로 계산하기
                bp21 = price21 * krw_balance21

                # 보유 및 매수 가능 출력.
                print(f"[ 21. {krw_coin21} 매도완료. ]")
                print(f"매도시간 : {now}  |  코인명 : {coin21}  |  현재가 = ￦{price21}  |  보유수량 = {krw_balance21}  |  평가금액 = ￦{bp21}  |  매수가능 : {op_mode21} - 매수가능")
                print("")

            else:   # 보유코인 평가 금액이 10,100원 이하일때
                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                op_mode21 = True

                # 매수 가능 출력
                print(f"현재시간 : {now}  |  코인명 : {coin21}  |  매수가능 : {op_mode21} - 매수가능")

        # 1초 딜레이.
        #time.sleep(1)
        ##### 21번 코인 매도 완료 #####


        ##### 22번코인 매도 시도 #####
        if op_mode22 == False:   # 매수 불가(False)일 경우 - 매도시도
            # 보유수량 불러오기
            krw_balance22 = upbit.get_balance(krw_coin22)
            # 현재가 불러오기
            price22 = pyupbit.get_current_price(krw_coin22)
            # 보유코인 원화금액으로 계산하기
            bp22 = price22 * krw_balance22

            # 보유코인 원화금액 매도시도
            if  bp22 > 10100:   # 보유코인 평가 금액이 10,100원 초과일때 - 매도시도
                # 매도할 코인명 - krw_coin22, 매도할 코인수량 - krw_balance22
                upbit.sell_market_order(krw_coin22, krw_balance22)

                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                op_mode22 = True

                # 1초 딜레이
                #time.sleep(1)
                # 보유수량 불러오기
                krw_balance22 = upbit.get_balance(krw_coin22)
                # 코인 현재가 불러오기
                price22 = pyupbit.get_current_price(krw_coin22)
                # 보유코인 원화금액으로 계산하기
                bp22 = price22 * krw_balance22

                # 보유 및 매수 가능 출력.
                print(f"[ 22. {krw_coin22} 매도완료. ]")
                print(f"매도시간 : {now}  |  코인명 : {coin22}  |  현재가 = ￦{price22}  |  보유수량 = {krw_balance22}  |  평가금액 = ￦{bp22}  |  매수가능 : {op_mode22} - 매수가능")
                print("")

            else:   # 보유코인 평가 금액이 10,100원 이하일때
                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                op_mode22 = True

                # 매수 가능 출력
                print(f"현재시간 : {now}  |  코인명 : {coin22}  |  매수가능 : {op_mode22} - 매수가능")

        # 1초 딜레이.
        #time.sleep(1)
        ##### 22번 코인 매도 완료 #####


        ##### 23번코인 매도 시도 #####
        if op_mode23 == False:   # 매수 불가(False)일 경우 - 매도시도
            # 보유수량 불러오기
            krw_balance23 = upbit.get_balance(krw_coin23)
            # 현재가 불러오기
            price23 = pyupbit.get_current_price(krw_coin23)
            # 보유코인 원화금액으로 계산하기
            bp23 = price23 * krw_balance23

            # 보유코인 원화금액 매도시도
            if  bp23 > 10100:   # 보유코인 평가 금액이 10,100원 초과일때 - 매도시도
                # 매도할 코인명 - krw_coin23, 매도할 코인수량 - krw_balance23
                upbit.sell_market_order(krw_coin23, krw_balance23)

                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                op_mode23 = True

                # 1초 딜레이
                #time.sleep(1)
                # 보유수량 불러오기
                krw_balance23 = upbit.get_balance(krw_coin23)
                # 코인 현재가 불러오기
                price23 = pyupbit.get_current_price(krw_coin23)
                # 보유코인 원화금액으로 계산하기
                bp23 = price23 * krw_balance23

                # 보유 및 매수 가능 출력.
                print(f"[ 23. {krw_coin23} 매도완료. ]")
                print(f"매도시간 : {now}  |  코인명 : {coin23}  |  현재가 = ￦{price23}  |  보유수량 = {krw_balance23}  |  평가금액 = ￦{bp23}  |  매수가능 : {op_mode23} - 매수가능")
                print("")

            else:   # 보유코인 평가 금액이 10,100원 이하일때
                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                op_mode23 = True

                # 매수 가능 출력
                print(f"현재시간 : {now}  |  코인명 : {coin23}  |  매수가능 : {op_mode23} - 매수가능")

        # 1초 딜레이.
        #time.sleep(1)
        ##### 23번 코인 매도 완료 #####


        ##### 24번코인 매도 시도 #####
        if op_mode24 == False:   # 매수 불가(False)일 경우 - 매도시도
            # 보유수량 불러오기
            krw_balance24 = upbit.get_balance(krw_coin24)
            # 현재가 불러오기
            price24 = pyupbit.get_current_price(krw_coin24)
            # 보유코인 원화금액으로 계산하기
            bp24 = price24 * krw_balance24

            # 보유코인 원화금액 매도시도
            if  bp24 > 10100:   # 보유코인 평가 금액이 10,100원 초과일때 - 매도시도
                # 매도할 코인명 - krw_coin24, 매도할 코인수량 - krw_balance24
                upbit.sell_market_order(krw_coin24, krw_balance24)

                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                op_mode24 = True

                # 1초 딜레이
                #time.sleep(1)
                # 보유수량 불러오기
                krw_balance24 = upbit.get_balance(krw_coin24)
                # 코인 현재가 불러오기
                price24 = pyupbit.get_current_price(krw_coin24)
                # 보유코인 원화금액으로 계산하기
                bp24 = price24 * krw_balance24

                # 보유 및 매수 가능 출력.
                print(f"[ 24. {krw_coin24} 매도완료. ]")
                print(f"매도시간 : {now}  |  코인명 : {coin24}  |  현재가 = ￦{price24}  |  보유수량 = {krw_balance24}  |  평가금액 = ￦{bp24}  |  매수가능 : {op_mode24} - 매수가능")
                print("")

            else:   # 보유코인 평가 금액이 10,100원 이하일때
                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                op_mode24 = True

                # 매수 가능 출력
                print(f"현재시간 : {now}  |  코인명 : {coin24}  |  매수가능 : {op_mode24} - 매수가능")

        # 1초 딜레이.
        #time.sleep(1)
        ##### 24번 코인 매도 완료 #####


        ##### 25번코인 매도 시도 #####
        if op_mode25 == False:   # 매수 불가(False)일 경우 - 매도시도
            # 보유수량 불러오기
            krw_balance25 = upbit.get_balance(krw_coin25)
            # 현재가 불러오기
            price25 = pyupbit.get_current_price(krw_coin25)
            # 보유코인 원화금액으로 계산하기
            bp25 = price25 * krw_balance25

            # 보유코인 원화금액 매도시도
            if  bp25 > 10100:   # 보유코인 평가 금액이 10,100원 초과일때 - 매도시도
                # 매도할 코인명 - krw_coin25, 매도할 코인수량 - krw_balance25
                upbit.sell_market_order(krw_coin25, krw_balance25)

                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                op_mode25 = True

                # 1초 딜레이
                #time.sleep(1)
                # 보유수량 불러오기
                krw_balance25 = upbit.get_balance(krw_coin25)
                # 코인 현재가 불러오기
                price25 = pyupbit.get_current_price(krw_coin25)
                # 보유코인 원화금액으로 계산하기
                bp25 = price25 * krw_balance25

                # 보유 및 매수 가능 출력.
                print(f"[ 25. {krw_coin25} 매도완료. ]")
                print(f"매도시간 : {now}  |  코인명 : {coin25}  |  현재가 = ￦{price25}  |  보유수량 = {krw_balance25}  |  평가금액 = ￦{bp25}  |  매수가능 : {op_mode25} - 매수가능")
                print("")

            else:   # 보유코인 평가 금액이 10,100원 이하일때
                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                op_mode25 = True

                # 매수 가능 출력
                print(f"현재시간 : {now}  |  코인명 : {coin25}  |  매수가능 : {op_mode25} - 매수가능")

        # 1초 딜레이.
        #time.sleep(1)
        ##### 25번 코인 매도 완료 #####


        ##### 26번코인 매도 시도 #####
        if op_mode26 == False:   # 매수 불가(False)일 경우 - 매도시도
            # 보유수량 불러오기
            krw_balance26 = upbit.get_balance(krw_coin26)
            # 현재가 불러오기
            price26 = pyupbit.get_current_price(krw_coin26)
            # 보유코인 원화금액으로 계산하기
            bp26 = price26 * krw_balance26

            # 보유코인 원화금액 매도시도
            if  bp26 > 10100:   # 보유코인 평가 금액이 10,100원 초과일때 - 매도시도
                # 매도할 코인명 - krw_coin26, 매도할 코인수량 - krw_balance26
                upbit.sell_market_order(krw_coin26, krw_balance26)

                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                op_mode26 = True

                # 1초 딜레이
                #time.sleep(1)
                # 보유수량 불러오기
                krw_balance26 = upbit.get_balance(krw_coin26)
                # 코인 현재가 불러오기
                price26 = pyupbit.get_current_price(krw_coin26)
                # 보유코인 원화금액으로 계산하기
                bp26 = price26 * krw_balance26

                # 보유 및 매수 가능 출력.
                print(f"[ 26. {krw_coin26} 매도완료. ]")
                print(f"매도시간 : {now}  |  코인명 : {coin26}  |  현재가 = ￦{price26}  |  보유수량 = {krw_balance26}  |  평가금액 = ￦{bp26}  |  매수가능 : {op_mode26} - 매수가능")
                print("")

            else:   # 보유코인 평가 금액이 10,100원 이하일때
                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                op_mode26 = True

                # 매수 가능 출력
                print(f"현재시간 : {now}  |  코인명 : {coin26}  |  매수가능 : {op_mode26} - 매수가능")

        # 1초 딜레이.
        #time.sleep(1)
        ##### 26번 코인 매도 완료 #####


        ##### 27번코인 매도 시도 #####
        if op_mode27 == False:   # 매수 불가(False)일 경우 - 매도시도
            # 보유수량 불러오기
            krw_balance27 = upbit.get_balance(krw_coin27)
            # 현재가 불러오기
            price27 = pyupbit.get_current_price(krw_coin27)
            # 보유코인 원화금액으로 계산하기
            bp27 = price27 * krw_balance27

            # 보유코인 원화금액 매도시도
            if  bp27 > 10100:   # 보유코인 평가 금액이 10,100원 초과일때 - 매도시도
                # 매도할 코인명 - krw_coin27, 매도할 코인수량 - krw_balance27
                upbit.sell_market_order(krw_coin27, krw_balance27)

                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                op_mode27 = True

                # 1초 딜레이
                #time.sleep(1)
                # 보유수량 불러오기
                krw_balance27 = upbit.get_balance(krw_coin27)
                # 코인 현재가 불러오기
                price27 = pyupbit.get_current_price(krw_coin27)
                # 보유코인 원화금액으로 계산하기
                bp27 = price27 * krw_balance27

                # 보유 및 매수 가능 출력.
                print(f"[ 27. {krw_coin27} 매도완료. ]")
                print(f"매도시간 : {now}  |  코인명 : {coin27}  |  현재가 = ￦{price27}  |  보유수량 = {krw_balance27}  |  평가금액 = ￦{bp27}  |  매수가능 : {op_mode27} - 매수가능")
                print("")

            else:   # 보유코인 평가 금액이 10,100원 이하일때
                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                op_mode27 = True

                # 매수 가능 출력
                print(f"현재시간 : {now}  |  코인명 : {coin27}  |  매수가능 : {op_mode27} - 매수가능")

        # 1초 딜레이.
        #time.sleep(1)
        ##### 27번 코인 매도 완료 #####


        ##### 28번코인 매도 시도 #####
        if op_mode28 == False:   # 매수 불가(False)일 경우 - 매도시도
            # 보유수량 불러오기
            krw_balance28 = upbit.get_balance(krw_coin28)
            # 현재가 불러오기
            price28 = pyupbit.get_current_price(krw_coin28)
            # 보유코인 원화금액으로 계산하기
            bp28 = price28 * krw_balance28

            # 보유코인 원화금액 매도시도
            if  bp28 > 10100:   # 보유코인 평가 금액이 10,100원 초과일때 - 매도시도
                # 매도할 코인명 - krw_coin28, 매도할 코인수량 - krw_balance28
                upbit.sell_market_order(krw_coin28, krw_balance28)

                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                op_mode28 = True

                # 1초 딜레이
                #time.sleep(1)
                # 보유수량 불러오기
                krw_balance28 = upbit.get_balance(krw_coin28)
                # 코인 현재가 불러오기
                price28 = pyupbit.get_current_price(krw_coin28)
                # 보유코인 원화금액으로 계산하기
                bp28 = price28 * krw_balance28

                # 보유 및 매수 가능 출력.
                print(f"[ 28. {krw_coin28} 매도완료. ]")
                print(f"매도시간 : {now}  |  코인명 : {coin28}  |  현재가 = ￦{price28}  |  보유수량 = {krw_balance28}  |  평가금액 = ￦{bp28}  |  매수가능 : {op_mode28} - 매수가능")
                print("")

            else:   # 보유코인 평가 금액이 10,100원 이하일때
                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                op_mode28 = True

                # 매수 가능 출력
                print(f"현재시간 : {now}  |  코인명 : {coin28}  |  매수가능 : {op_mode28} - 매수가능")

        # 1초 딜레이.
        #time.sleep(1)
        ##### 28번 코인 매도 완료 #####


        ##### 29번코인 매도 시도 #####
        if op_mode29 == False:   # 매수 불가(False)일 경우 - 매도시도
            # 보유수량 불러오기
            krw_balance29 = upbit.get_balance(krw_coin29)
            # 현재가 불러오기
            price29 = pyupbit.get_current_price(krw_coin29)
            # 보유코인 원화금액으로 계산하기
            bp29 = price29 * krw_balance29

            # 보유코인 원화금액 매도시도
            if  bp29 > 10100:   # 보유코인 평가 금액이 10,100원 초과일때 - 매도시도
                # 매도할 코인명 - krw_coin29, 매도할 코인수량 - krw_balance29
                upbit.sell_market_order(krw_coin29, krw_balance29)

                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                op_mode29 = True

                # 1초 딜레이
                #time.sleep(1)
                # 보유수량 불러오기
                krw_balance29 = upbit.get_balance(krw_coin29)
                # 코인 현재가 불러오기
                price29 = pyupbit.get_current_price(krw_coin29)
                # 보유코인 원화금액으로 계산하기
                bp29 = price29 * krw_balance29

                # 보유 및 매수 가능 출력.
                print(f"[ 29. {krw_coin29} 매도완료. ]")
                print(f"매도시간 : {now}  |  코인명 : {coin29}  |  현재가 = ￦{price29}  |  보유수량 = {krw_balance29}  |  평가금액 = ￦{bp29}  |  매수가능 : {op_mode29} - 매수가능")
                print("")

            else:   # 보유코인 평가 금액이 10,100원 이하일때
                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                op_mode29 = True

                # 매수 가능 출력
                print(f"현재시간 : {now}  |  코인명 : {coin29}  |  매수가능 : {op_mode29} - 매수가능")

        # 1초 딜레이.
        #time.sleep(1)
        ##### 29번 코인 매도 완료 #####


        ##### 30번코인 매도 시도 #####
        if op_mode30 == False:   # 매수 불가(False)일 경우 - 매도시도
            # 보유수량 불러오기
            krw_balance30 = upbit.get_balance(krw_coin30)
            # 현재가 불러오기
            price30 = pyupbit.get_current_price(krw_coin30)
            # 보유코인 원화금액으로 계산하기
            bp30 = price30 * krw_balance30

            # 보유코인 원화금액 매도시도
            if  bp30 > 10100:   # 보유코인 평가 금액이 10,100원 초과일때 - 매도시도
                # 매도할 코인명 - krw_coin30, 매도할 코인수량 - krw_balance30
                upbit.sell_market_order(krw_coin30, krw_balance30)

                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                op_mode30 = True

                # 1초 딜레이
                #time.sleep(1)
                # 보유수량 불러오기
                krw_balance30 = upbit.get_balance(krw_coin30)
                # 코인 현재가 불러오기
                price30 = pyupbit.get_current_price(krw_coin30)
                # 보유코인 원화금액으로 계산하기
                bp30 = price30 * krw_balance30

                # 보유 및 매수 가능 출력.
                print(f"[ 30. {krw_coin30} 매도완료. ]")
                print(f"매도시간 : {now}  |  코인명 : {coin30}  |  현재가 = ￦{price30}  |  보유수량 = {krw_balance30}  |  평가금액 = ￦{bp30}  |  매수가능 : {op_mode30} - 매수가능")
                print("")

            else:   # 보유코인 평가 금액이 10,100원 이하일때
                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                op_mode30 = True

                # 매수 가능 출력
                print(f"현재시간 : {now}  |  코인명 : {coin30}  |  매수가능 : {op_mode30} - 매수가능")

        # 1초 딜레이.
        #time.sleep(1)
        ##### 30번 코인 매도 완료 #####


        ######################################################################################################################################################
        ######################################################################################################################################################
        ######################################################################################################################################################


        ##### 31번코인 매도 시도 #####
        if op_mode31 == False:   # 매수 불가(False)일 경우 - 매도시도
            # 보유수량 불러오기
            krw_balance31 = upbit.get_balance(krw_coin31)
            # 현재가 불러오기
            price31 = pyupbit.get_current_price(krw_coin31)
            # 보유코인 원화금액으로 계산하기
            bp31 = price31 * krw_balance31

            # 보유코인 원화금액 매도시도
            if  bp31 > 10100:   # 보유코인 평가 금액이 10,100원 초과일때 - 매도시도
                # 매도할 코인명 - krw_coin31, 매도할 코인수량 - krw_balance31
                upbit.sell_market_order(krw_coin31, krw_balance31)

                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                op_mode31 = True

                # 1초 딜레이
                #time.sleep(1)
                # 보유수량 불러오기
                krw_balance31 = upbit.get_balance(krw_coin31)
                # 코인 현재가 불러오기
                price31 = pyupbit.get_current_price(krw_coin31)
                # 보유코인 원화금액으로 계산하기
                bp31 = price31 * krw_balance31

                # 보유 및 매수 가능 출력.
                print(f"[ 31. {krw_coin31} 매도완료. ]")
                print(f"매도시간 : {now}  |  코인명 : {coin31}  |  현재가 = ￦{price31}  |  보유수량 = {krw_balance31}  |  평가금액 = ￦{bp31}  |  매수가능 : {op_mode31} - 매수가능")
                print("")

            else:   # 보유코인 평가 금액이 10,100원 이하일때
                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                op_mode31 = True

                # 매수 가능 출력
                print(f"현재시간 : {now}  |  코인명 : {coin31}  |  매수가능 : {op_mode31} - 매수가능")

        # 1초 딜레이.
        #time.sleep(1)
        ##### 31번 코인 매도 완료 #####


        ##### 32번코인 매도 시도 #####
        if op_mode32 == False:   # 매수 불가(False)일 경우 - 매도시도
            # 보유수량 불러오기
            krw_balance32 = upbit.get_balance(krw_coin32)
            # 현재가 불러오기
            price32 = pyupbit.get_current_price(krw_coin32)
            # 보유코인 원화금액으로 계산하기
            bp32 = price32 * krw_balance32

            # 보유코인 원화금액 매도시도
            if  bp32 > 10100:   # 보유코인 평가 금액이 10,100원 초과일때 - 매도시도
                # 매도할 코인명 - krw_coin32, 매도할 코인수량 - krw_balance32
                upbit.sell_market_order(krw_coin32, krw_balance32)

                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                op_mode32 = True

                # 1초 딜레이
                #time.sleep(1)
                # 보유수량 불러오기
                krw_balance32 = upbit.get_balance(krw_coin32)
                # 코인 현재가 불러오기
                price32 = pyupbit.get_current_price(krw_coin32)
                # 보유코인 원화금액으로 계산하기
                bp32 = price32 * krw_balance32

                # 보유 및 매수 가능 출력.
                print(f"[ 32. {krw_coin32} 매도완료. ]")
                print(f"매도시간 : {now}  |  코인명 : {coin32}  |  현재가 = ￦{price32}  |  보유수량 = {krw_balance32}  |  평가금액 = ￦{bp32}  |  매수가능 : {op_mode32} - 매수가능")
                print("")

            else:   # 보유코인 평가 금액이 10,100원 이하일때
                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                op_mode32 = True

                # 매수 가능 출력
                print(f"현재시간 : {now}  |  코인명 : {coin32}  |  매수가능 : {op_mode32} - 매수가능")

        # 1초 딜레이.
        #time.sleep(1)
        ##### 32번 코인 매도 완료 #####


        ##### 33번코인 매도 시도 #####
        if op_mode33 == False:   # 매수 불가(False)일 경우 - 매도시도
            # 보유수량 불러오기
            krw_balance33 = upbit.get_balance(krw_coin33)
            # 현재가 불러오기
            price33 = pyupbit.get_current_price(krw_coin33)
            # 보유코인 원화금액으로 계산하기
            bp33 = price33 * krw_balance33

            # 보유코인 원화금액 매도시도
            if  bp33 > 10100:   # 보유코인 평가 금액이 10,100원 초과일때 - 매도시도
                # 매도할 코인명 - krw_coin33, 매도할 코인수량 - krw_balance33
                upbit.sell_market_order(krw_coin33, krw_balance33)

                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                op_mode33 = True

                # 1초 딜레이
                #time.sleep(1)
                # 보유수량 불러오기
                krw_balance33 = upbit.get_balance(krw_coin33)
                # 코인 현재가 불러오기
                price33 = pyupbit.get_current_price(krw_coin33)
                # 보유코인 원화금액으로 계산하기
                bp33 = price33 * krw_balance33

                # 보유 및 매수 가능 출력.
                print(f"[ 33. {krw_coin33} 매도완료. ]")
                print(f"매도시간 : {now}  |  코인명 : {coin33}  |  현재가 = ￦{price33}  |  보유수량 = {krw_balance33}  |  평가금액 = ￦{bp33}  |  매수가능 : {op_mode33} - 매수가능")
                print("")

            else:   # 보유코인 평가 금액이 10,100원 이하일때
                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                op_mode33 = True

                # 매수 가능 출력
                print(f"현재시간 : {now}  |  코인명 : {coin33}  |  매수가능 : {op_mode33} - 매수가능")

        # 1초 딜레이.
        #time.sleep(1)
        ##### 33번 코인 매도 완료 #####


        ##### 34번코인 매도 시도 #####
        if op_mode34 == False:   # 매수 불가(False)일 경우 - 매도시도
            # 보유수량 불러오기
            krw_balance34 = upbit.get_balance(krw_coin34)
            # 현재가 불러오기
            price34 = pyupbit.get_current_price(krw_coin34)
            # 보유코인 원화금액으로 계산하기
            bp34 = price34 * krw_balance34

            # 보유코인 원화금액 매도시도
            if  bp34 > 10100:   # 보유코인 평가 금액이 10,100원 초과일때 - 매도시도
                # 매도할 코인명 - krw_coin34, 매도할 코인수량 - krw_balance34
                upbit.sell_market_order(krw_coin34, krw_balance34)

                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                op_mode34 = True

                # 1초 딜레이
                #time.sleep(1)
                # 보유수량 불러오기
                krw_balance34 = upbit.get_balance(krw_coin34)
                # 코인 현재가 불러오기
                price34 = pyupbit.get_current_price(krw_coin34)
                # 보유코인 원화금액으로 계산하기
                bp34 = price34 * krw_balance34

                # 보유 및 매수 가능 출력.
                print(f"[ 34. {krw_coin34} 매도완료. ]")
                print(f"매도시간 : {now}  |  코인명 : {coin34}  |  현재가 = ￦{price34}  |  보유수량 = {krw_balance34}  |  평가금액 = ￦{bp34}  |  매수가능 : {op_mode34} - 매수가능")
                print("")

            else:   # 보유코인 평가 금액이 10,100원 이하일때
                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                op_mode34 = True

                # 매수 가능 출력
                print(f"현재시간 : {now}  |  코인명 : {coin34}  |  매수가능 : {op_mode34} - 매수가능")

        # 1초 딜레이.
        #time.sleep(1)
        ##### 34번 코인 매도 완료 #####


        ##### 35번코인 매도 시도 #####
        if op_mode35 == False:   # 매수 불가(False)일 경우 - 매도시도
            # 보유수량 불러오기
            krw_balance35 = upbit.get_balance(krw_coin35)
            # 현재가 불러오기
            price35 = pyupbit.get_current_price(krw_coin35)
            # 보유코인 원화금액으로 계산하기
            bp35 = price35 * krw_balance35

            # 보유코인 원화금액 매도시도
            if  bp35 > 10100:   # 보유코인 평가 금액이 10,100원 초과일때 - 매도시도
                # 매도할 코인명 - krw_coin35, 매도할 코인수량 - krw_balance35
                upbit.sell_market_order(krw_coin35, krw_balance35)

                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                op_mode35 = True

                # 1초 딜레이
                #time.sleep(1)
                # 보유수량 불러오기
                krw_balance35 = upbit.get_balance(krw_coin35)
                # 코인 현재가 불러오기
                price35 = pyupbit.get_current_price(krw_coin35)
                # 보유코인 원화금액으로 계산하기
                bp35 = price35 * krw_balance35

                # 보유 및 매수 가능 출력.
                print(f"[ 35. {krw_coin35} 매도완료. ]")
                print(f"매도시간 : {now}  |  코인명 : {coin35}  |  현재가 = ￦{price35}  |  보유수량 = {krw_balance35}  |  평가금액 = ￦{bp35}  |  매수가능 : {op_mode35} - 매수가능")
                print("")

            else:   # 보유코인 평가 금액이 10,100원 이하일때
                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                op_mode35 = True

                # 매수 가능 출력
                print(f"현재시간 : {now}  |  코인명 : {coin35}  |  매수가능 : {op_mode35} - 매수가능")

        # 1초 딜레이.
        #time.sleep(1)
        ##### 35번 코인 매도 완료 #####


        ##### 36번코인 매도 시도 #####
        if op_mode36 == False:   # 매수 불가(False)일 경우 - 매도시도
            # 보유수량 불러오기
            krw_balance36 = upbit.get_balance(krw_coin36)
            # 현재가 불러오기
            price36 = pyupbit.get_current_price(krw_coin36)
            # 보유코인 원화금액으로 계산하기
            bp36 = price36 * krw_balance36

            # 보유코인 원화금액 매도시도
            if  bp36 > 10100:   # 보유코인 평가 금액이 10,100원 초과일때 - 매도시도
                # 매도할 코인명 - krw_coin36, 매도할 코인수량 - krw_balance36
                upbit.sell_market_order(krw_coin36, krw_balance36)

                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                op_mode36 = True

                # 1초 딜레이
                #time.sleep(1)
                # 보유수량 불러오기
                krw_balance36 = upbit.get_balance(krw_coin36)
                # 코인 현재가 불러오기
                price36 = pyupbit.get_current_price(krw_coin36)
                # 보유코인 원화금액으로 계산하기
                bp36 = price36 * krw_balance36

                # 보유 및 매수 가능 출력.
                print(f"[ 36. {krw_coin36} 매도완료. ]")
                print(f"매도시간 : {now}  |  코인명 : {coin36}  |  현재가 = ￦{price36}  |  보유수량 = {krw_balance36}  |  평가금액 = ￦{bp36}  |  매수가능 : {op_mode36} - 매수가능")
                print("")

            else:   # 보유코인 평가 금액이 10,100원 이하일때
                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                op_mode36 = True

                # 매수 가능 출력
                print(f"현재시간 : {now}  |  코인명 : {coin36}  |  매수가능 : {op_mode36} - 매수가능")

        # 1초 딜레이.
        #time.sleep(1)
        ##### 36번 코인 매도 완료 #####


        ##### 37번코인 매도 시도 #####
        if op_mode37 == False:   # 매수 불가(False)일 경우 - 매도시도
            # 보유수량 불러오기
            krw_balance37 = upbit.get_balance(krw_coin37)
            # 현재가 불러오기
            price37 = pyupbit.get_current_price(krw_coin37)
            # 보유코인 원화금액으로 계산하기
            bp37 = price37 * krw_balance37

            # 보유코인 원화금액 매도시도
            if  bp37 > 10100:   # 보유코인 평가 금액이 10,100원 초과일때 - 매도시도
                # 매도할 코인명 - krw_coin37, 매도할 코인수량 - krw_balance37
                upbit.sell_market_order(krw_coin37, krw_balance37)

                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                op_mode37 = True

                # 1초 딜레이
                #time.sleep(1)
                # 보유수량 불러오기
                krw_balance37 = upbit.get_balance(krw_coin37)
                # 코인 현재가 불러오기
                price37 = pyupbit.get_current_price(krw_coin37)
                # 보유코인 원화금액으로 계산하기
                bp37 = price37 * krw_balance37

                # 보유 및 매수 가능 출력.
                print(f"[ 37. {krw_coin37} 매도완료. ]")
                print(f"매도시간 : {now}  |  코인명 : {coin37}  |  현재가 = ￦{price37}  |  보유수량 = {krw_balance37}  |  평가금액 = ￦{bp37}  |  매수가능 : {op_mode37} - 매수가능")
                print("")

            else:   # 보유코인 평가 금액이 10,100원 이하일때
                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                op_mode37 = True

                # 매수 가능 출력
                print(f"현재시간 : {now}  |  코인명 : {coin37}  |  매수가능 : {op_mode37} - 매수가능")

        # 1초 딜레이.
        #time.sleep(1)
        ##### 37번 코인 매도 완료 #####


        ##### 38번코인 매도 시도 #####
        if op_mode38 == False:   # 매수 불가(False)일 경우 - 매도시도
            # 보유수량 불러오기
            krw_balance38 = upbit.get_balance(krw_coin38)
            # 현재가 불러오기
            price38 = pyupbit.get_current_price(krw_coin38)
            # 보유코인 원화금액으로 계산하기
            bp38 = price38 * krw_balance38

            # 보유코인 원화금액 매도시도
            if  bp38 > 10100:   # 보유코인 평가 금액이 10,100원 초과일때 - 매도시도
                # 매도할 코인명 - krw_coin38, 매도할 코인수량 - krw_balance38
                upbit.sell_market_order(krw_coin38, krw_balance38)

                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                op_mode38 = True

                # 1초 딜레이
                #time.sleep(1)
                # 보유수량 불러오기
                krw_balance38 = upbit.get_balance(krw_coin38)
                # 코인 현재가 불러오기
                price38 = pyupbit.get_current_price(krw_coin38)
                # 보유코인 원화금액으로 계산하기
                bp38 = price38 * krw_balance38

                # 보유 및 매수 가능 출력.
                print(f"[ 38. {krw_coin38} 매도완료. ]")
                print(f"매도시간 : {now}  |  코인명 : {coin38}  |  현재가 = ￦{price38}  |  보유수량 = {krw_balance38}  |  평가금액 = ￦{bp38}  |  매수가능 : {op_mode38} - 매수가능")
                print("")

            else:   # 보유코인 평가 금액이 10,100원 이하일때
                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                op_mode38 = True

                # 매수 가능 출력
                print(f"현재시간 : {now}  |  코인명 : {coin38}  |  매수가능 : {op_mode38} - 매수가능")

        # 1초 딜레이.
        #time.sleep(1)
        ##### 38번 코인 매도 완료 #####


        ##### 39번코인 매도 시도 #####
        if op_mode39 == False:   # 매수 불가(False)일 경우 - 매도시도
            # 보유수량 불러오기
            krw_balance39 = upbit.get_balance(krw_coin39)
            # 현재가 불러오기
            price39 = pyupbit.get_current_price(krw_coin39)
            # 보유코인 원화금액으로 계산하기
            bp39 = price39 * krw_balance39

            # 보유코인 원화금액 매도시도
            if  bp39 > 10100:   # 보유코인 평가 금액이 10,100원 초과일때 - 매도시도
                # 매도할 코인명 - krw_coin39, 매도할 코인수량 - krw_balance39
                upbit.sell_market_order(krw_coin39, krw_balance39)

                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                op_mode39 = True

                # 1초 딜레이
                #time.sleep(1)
                # 보유수량 불러오기
                krw_balance39 = upbit.get_balance(krw_coin39)
                # 코인 현재가 불러오기
                price39 = pyupbit.get_current_price(krw_coin39)
                # 보유코인 원화금액으로 계산하기
                bp39 = price39 * krw_balance39

                # 보유 및 매수 가능 출력.
                print(f"[ 39. {krw_coin39} 매도완료. ]")
                print(f"매도시간 : {now}  |  코인명 : {coin39}  |  현재가 = ￦{price39}  |  보유수량 = {krw_balance39}  |  평가금액 = ￦{bp39}  |  매수가능 : {op_mode39} - 매수가능")
                print("")

            else:   # 보유코인 평가 금액이 10,100원 이하일때
                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                op_mode39 = True

                # 매수 가능 출력
                print(f"현재시간 : {now}  |  코인명 : {coin39}  |  매수가능 : {op_mode39} - 매수가능")

        # 1초 딜레이.
        #time.sleep(1)
        ##### 39번 코인 매도 완료 #####


        ##### 40번코인 매도 시도 #####
        if op_mode40 == False:   # 매수 불가(False)일 경우 - 매도시도
            # 보유수량 불러오기
            krw_balance40 = upbit.get_balance(krw_coin40)
            # 현재가 불러오기
            price40 = pyupbit.get_current_price(krw_coin40)
            # 보유코인 원화금액으로 계산하기
            bp40 = price40 * krw_balance40

            # 보유코인 원화금액 매도시도
            if  bp40 > 10100:   # 보유코인 평가 금액이 10,100원 초과일때 - 매도시도
                # 매도할 코인명 - krw_coin40, 매도할 코인수량 - krw_balance40
                upbit.sell_market_order(krw_coin40, krw_balance40)

                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                op_mode40 = True

                # 1초 딜레이
                #time.sleep(1)
                # 보유수량 불러오기
                krw_balance40 = upbit.get_balance(krw_coin40)
                # 코인 현재가 불러오기
                price40 = pyupbit.get_current_price(krw_coin40)
                # 보유코인 원화금액으로 계산하기
                bp40 = price40 * krw_balance40

                # 보유 및 매수 가능 출력.
                print(f"[ 40. {krw_coin40} 매도완료. ]")
                print(f"매도시간 : {now}  |  코인명 : {coin40}  |  현재가 = ￦{price40}  |  보유수량 = {krw_balance40}  |  평가금액 = ￦{bp40}  |  매수가능 : {op_mode40} - 매수가능")
                print("")

            else:   # 보유코인 평가 금액이 10,100원 이하일때
                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                op_mode40 = True

                # 매수 가능 출력
                print(f"현재시간 : {now}  |  코인명 : {coin40}  |  매수가능 : {op_mode40} - 매수가능")

        # 1초 딜레이.
        #time.sleep(1)
        ##### 40번 코인 매도 완료 #####


        ######################################################################################################################################################
        ######################################################################################################################################################
        ######################################################################################################################################################

        # 한바퀴 1초 딜레이.
        time.sleep(1)

        # 매수가능금액 정하기.
        buy_krw = (upbit.get_balance("KRW")) / (40 / 2)   # 40개 코인 매매

        print("")
        print(f" 매수 평가 금액 : ￦{buy_krw}")
        print("")


        ######################################################################################################################################################
        ######################################################################################################################################################
        ######################################################################################################################################################


    else:   # 매도시간 외의 시간들
        ##################################
        # 매초마다 조건을 확인한 후 매수 시도

        ##### 1번코인 매수 시도 #####
        if op_mode1 == True:    # 매수 가능(True)일 경우 - 매수시도
            # 코인 현재가 불러오기
            price1 = pyupbit.get_current_price(krw_coin1)
            # 코인 목표가 불러오기
            target1 = cal_target(krw_coin1)

            if price1 >= target1:   # 목표가보다 현재가가 높을때
                # 매수가능금액 불러오기
                krw1 = upbit.get_balance("KRW")

                if krw1 > buy_krw:    # 매수가능금액 krw1 이 매수설정금액 buy_krw 보다 많을 경우: 매수
                    if krw1 > 10100:     # 매수가능금액 krw1 이 10,100원 초과일 경우 : 매수
                        # 매수금액은 매수평균가 buy_krw 로
                        upbit.buy_market_order(krw_coin1, buy_krw * 0.99)   # 매수가능금액에서 1%를 빼고

                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode1 = False

                        # 1초 딜레이
                        time.sleep(1)
                        # 보유수량 불러오기
                        krw_balance1 = upbit.get_balance(krw_coin1)
                        # 코인 현재가 불러오기
                        price1 = pyupbit.get_current_price(krw_coin1)
                        # 보유코인 원화금액으로 계산하기
                        bp1 = price1 * krw_balance1

                        # 보유 및 매수 가능 출력.
                        print(f"[ 1. {krw_coin1} 매수완료. ]")
                        print(f"매수시간 : {now}  |  코인명 : {coin1}  |  현재가 = ￦{price1}  |  금일목표가 = ￦{target1}  |  보유수량 = {krw_balance1}  |  평가금액 = ￦{bp1}")
                        print(f"매수가능 - {op_mode1} - 불가")
                        print("")
                    else:
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode1 = False

                        print(f"[ 1. {krw_coin1} 잔고부족으로 매수안함. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin1}  |  현재매수가능 - {op_mode1} - 불가")
                        print("")

                elif krw1 <= buy_krw:   # 매수가능금액 krw1 가 매수평균가 buy_krw 보다 같거나 작을때
                    if krw1 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                        # 매수금액은 매수가능금액인 krw1 로
                        upbit.buy_market_order(krw_coin1, krw1 * 0.99)   # 매수가능금액에서 1%를 빼고

                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode1 = False

                        # 1초 딜레이
                        time.sleep(1)
                        # 보유수량 불러오기
                        krw_balance1 = upbit.get_balance(krw_coin1)
                        # 코인 현재가 불러오기
                        price1 = pyupbit.get_current_price(krw_coin1)
                        # 보유코인 원화금액으로 계산하기
                        bp1 = price1 * krw_balance1

                        # 보유 및 매수 가능 출력.
                        print(f"[ 1. {krw_coin1} 매수완료. ]")
                        print(f"매수시간 : {now}  |  코인명 : {coin1}  |  현재가 = ￦{price1}  |  금일목표가 = ￦{target1}  |  보유수량 = {krw_balance1}  |  평가금액 = ￦{bp1}")
                        print(f"매수가능 - {op_mode1} - 불가")
                        print("")
                    else:
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode1 = False

                        print(f"[ 1. {krw_coin1} 잔고부족으로 매수안함. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin1}  |  현재매수가능 - {op_mode1} - 불가")
                        print("")

        # 1초 딜레이.
        #time.sleep(1)
        ##### 1번 코인 매수 종료 #####
        #############################


        ##### 2번코인 매수 시도 #####
        if op_mode2 == True:    # 매수 가능(True)일 경우 - 매수시도
            # 코인 현재가 불러오기
            price2 = pyupbit.get_current_price(krw_coin2)
            # 코인 목표가 불러오기
            target2 = cal_target(krw_coin2)

            if price2 >= target2:   # 목표가보다 현재가가 높을때
                # 매수가능금액 불러오기
                krw2 = upbit.get_balance("KRW")

                if krw2 > buy_krw:    # 매수가능금액 krw2 이 매수설정금액 buy_krw 보다 많을 경우: 매수
                    if krw2 > 10100:     # 매수가능금액 krw2 이 10,100원 초과일 경우 : 매수
                        # 매수금액은 매수평균가 buy_krw 로
                        upbit.buy_market_order(krw_coin2, buy_krw * 0.99)   # 매수가능금액에서 1%를 빼고

                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode2 = False

                        # 1초 딜레이
                        time.sleep(1)
                        # 보유수량 불러오기
                        krw_balance2 = upbit.get_balance(krw_coin2)
                        # 코인 현재가 불러오기
                        price2 = pyupbit.get_current_price(krw_coin2)
                        # 보유코인 원화금액으로 계산하기
                        bp2 = price2 * krw_balance2

                        # 보유 및 매수 가능 출력.
                        print(f"[ 2. {krw_coin2} 매수완료. ]")
                        print(f"매수시간 : {now}  |  코인명 : {coin2}  |  현재가 = ￦{price2}  |  금일목표가 = ￦{target2}  |  보유수량 = {krw_balance2}  |  평가금액 = ￦{bp2}")
                        print(f"매수가능 - {op_mode2} - 불가")
                        print("")
                    else:
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode2 = False

                        print(f"[ 2. {krw_coin2} 잔고부족으로 매수안함. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin2}  |  현재매수가능 - {op_mode2} - 불가")
                        print("")

                elif krw2 <= buy_krw:   # 매수가능금액 krw2 가 매수평균가 buy_krw 보다 같거나 작을때
                    if krw2 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                        # 매수금액은 매수가능금액인 krw2 로
                        upbit.buy_market_order(krw_coin2, krw2 * 0.99)   # 매수가능금액에서 1%를 빼고

                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode2 = False

                        # 1초 딜레이
                        time.sleep(1)
                        # 보유수량 불러오기
                        krw_balance2 = upbit.get_balance(krw_coin2)
                        # 코인 현재가 불러오기
                        price2 = pyupbit.get_current_price(krw_coin2)
                        # 보유코인 원화금액으로 계산하기
                        bp2 = price2 * krw_balance2

                        # 보유 및 매수 가능 출력.
                        print(f"[ 2. {krw_coin2} 매수완료. ]")
                        print(f"매수시간 : {now}  |  코인명 : {coin2}  |  현재가 = ￦{price2}  |  금일목표가 = ￦{target2}  |  보유수량 = {krw_balance2}  |  평가금액 = ￦{bp2}")
                        print(f"매수가능 - {op_mode2} - 불가")
                        print("")
                    else:
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode2 = False

                        print(f"[ 2. {krw_coin2} 잔고부족으로 매수안함. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin2}  |  현재매수가능 - {op_mode2} - 불가")
                        print("")

        # 1초 딜레이.
        #time.sleep(1)
        ##### 2번 코인 매수 종료 #####
        #############################


        ##### 3번코인 매수 시도 #####
        if op_mode3 == True:    # 매수 가능(True)일 경우 - 매수시도
            # 코인 현재가 불러오기
            price3 = pyupbit.get_current_price(krw_coin3)
            # 코인 목표가 불러오기
            target3 = cal_target(krw_coin3)

            if price3 >= target3:   # 목표가보다 현재가가 높을때
                # 매수가능금액 불러오기
                krw3 = upbit.get_balance("KRW")

                if krw3 > buy_krw:    # 매수가능금액 krw3 이 매수설정금액 buy_krw 보다 많을 경우: 매수
                    if krw3 > 10100:     # 매수가능금액 krw3 이 10,100원 초과일 경우 : 매수
                        # 매수금액은 매수평균가 buy_krw 로
                        upbit.buy_market_order(krw_coin3, buy_krw * 0.99)   # 매수가능금액에서 1%를 빼고

                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode3 = False

                        # 1초 딜레이
                        time.sleep(1)
                        # 보유수량 불러오기
                        krw_balance3 = upbit.get_balance(krw_coin3)
                        # 코인 현재가 불러오기
                        price3 = pyupbit.get_current_price(krw_coin3)
                        # 보유코인 원화금액으로 계산하기
                        bp3 = price3 * krw_balance3

                        # 보유 및 매수 가능 출력.
                        print(f"[ 3. {krw_coin3} 매수완료. ]")
                        print(f"매수시간 : {now}  |  코인명 : {coin3}  |  현재가 = ￦{price3}  |  금일목표가 = ￦{target3}  |  보유수량 = {krw_balance3}  |  평가금액 = ￦{bp3}")
                        print(f"매수가능 - {op_mode3} - 불가")
                        print("")
                    else:
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode3 = False

                        print(f"[ 3. {krw_coin3} 잔고부족으로 매수안함. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin3}  |  현재매수가능 - {op_mode3} - 불가")
                        print("")

                elif krw3 <= buy_krw:   # 매수가능금액 krw3 가 매수평균가 buy_krw 보다 같거나 작을때
                    if krw3 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                        # 매수금액은 매수가능금액인 krw3 로
                        upbit.buy_market_order(krw_coin3, krw3 * 0.99)   # 매수가능금액에서 1%를 빼고

                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode3 = False

                        # 1초 딜레이
                        time.sleep(1)
                        # 보유수량 불러오기
                        krw_balance3 = upbit.get_balance(krw_coin3)
                        # 코인 현재가 불러오기
                        price3 = pyupbit.get_current_price(krw_coin3)
                        # 보유코인 원화금액으로 계산하기
                        bp3 = price3 * krw_balance3

                        # 보유 및 매수 가능 출력.
                        print(f"[ 3. {krw_coin3} 매수완료. ]")
                        print(f"매수시간 : {now}  |  코인명 : {coin3}  |  현재가 = ￦{price3}  |  금일목표가 = ￦{target3}  |  보유수량 = {krw_balance3}  |  평가금액 = ￦{bp3}")
                        print(f"매수가능 - {op_mode3} - 불가")
                        print("")
                    else:
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode3 = False

                        print(f"[ 3. {krw_coin3} 잔고부족으로 매수안함. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin3}  |  현재매수가능 - {op_mode3} - 불가")
                        print("")

        # 1초 딜레이.
        #time.sleep(1)
        ##### 3번 코인 매수 종료 #####
        #############################


        ##### 4번코인 매수 시도 #####
        if op_mode4 == True:    # 매수 가능(True)일 경우 - 매수시도
            # 코인 현재가 불러오기
            price4 = pyupbit.get_current_price(krw_coin4)
            # 코인 목표가 불러오기
            target4 = cal_target(krw_coin4)

            if price4 >= target4:   # 목표가보다 현재가가 높을때
                # 매수가능금액 불러오기
                krw4 = upbit.get_balance("KRW")

                if krw4 > buy_krw:    # 매수가능금액 krw4 이 매수설정금액 buy_krw 보다 많을 경우: 매수
                    if krw4 > 10100:     # 매수가능금액 krw4 이 10,100원 초과일 경우 : 매수
                        # 매수금액은 매수평균가 buy_krw 로
                        upbit.buy_market_order(krw_coin4, buy_krw * 0.99)   # 매수가능금액에서 1%를 빼고

                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode4 = False

                        # 1초 딜레이
                        time.sleep(1)
                        # 보유수량 불러오기
                        krw_balance4 = upbit.get_balance(krw_coin4)
                        # 코인 현재가 불러오기
                        price4 = pyupbit.get_current_price(krw_coin4)
                        # 보유코인 원화금액으로 계산하기
                        bp4 = price4 * krw_balance4

                        # 보유 및 매수 가능 출력.
                        print(f"[ 4. {krw_coin4} 매수완료. ]")
                        print(f"매수시간 : {now}  |  코인명 : {coin4}  |  현재가 = ￦{price4}  |  금일목표가 = ￦{target4}  |  보유수량 = {krw_balance4}  |  평가금액 = ￦{bp4}")
                        print(f"매수가능 - {op_mode4} - 불가")
                        print("")
                    else:
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode4 = False

                        print(f"[ 4. {krw_coin4} 잔고부족으로 매수안함. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin4}  |  현재매수가능 - {op_mode4} - 불가")
                        print("")

                elif krw4 <= buy_krw:   # 매수가능금액 krw4 가 매수평균가 buy_krw 보다 같거나 작을때
                    if krw4 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                        # 매수금액은 매수가능금액인 krw4 로
                        upbit.buy_market_order(krw_coin4, krw4 * 0.99)   # 매수가능금액에서 1%를 빼고

                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode4 = False

                        # 1초 딜레이
                        time.sleep(1)
                        # 보유수량 불러오기
                        krw_balance4 = upbit.get_balance(krw_coin4)
                        # 코인 현재가 불러오기
                        price4 = pyupbit.get_current_price(krw_coin4)
                        # 보유코인 원화금액으로 계산하기
                        bp4 = price4 * krw_balance4

                        # 보유 및 매수 가능 출력.
                        print(f"[ 4. {krw_coin4} 매수완료. ]")
                        print(f"매수시간 : {now}  |  코인명 : {coin4}  |  현재가 = ￦{price4}  |  금일목표가 = ￦{target4}  |  보유수량 = {krw_balance4}  |  평가금액 = ￦{bp4}")
                        print(f"매수가능 - {op_mode4} - 불가")
                        print("")
                    else:
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode4 = False

                        print(f"[ 4. {krw_coin4} 잔고부족으로 매수안함. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin4}  |  현재매수가능 - {op_mode4} - 불가")
                        print("")

        # 1초 딜레이.
        #time.sleep(1)
        ##### 4번 코인 매수 종료 #####
        #############################


        ##### 5번코인 매수 시도 #####
        if op_mode5 == True:    # 매수 가능(True)일 경우 - 매수시도
            # 코인 현재가 불러오기
            price5 = pyupbit.get_current_price(krw_coin5)
            # 코인 목표가 불러오기
            target5 = cal_target(krw_coin5)

            if price5 >= target5:   # 목표가보다 현재가가 높을때
                # 매수가능금액 불러오기
                krw5 = upbit.get_balance("KRW")

                if krw5 > buy_krw:    # 매수가능금액 krw5 이 매수설정금액 buy_krw 보다 많을 경우: 매수
                    if krw5 > 10100:     # 매수가능금액 krw5 이 10,100원 초과일 경우 : 매수
                        # 매수금액은 매수평균가 buy_krw 로
                        upbit.buy_market_order(krw_coin5, buy_krw * 0.99)   # 매수가능금액에서 1%를 빼고

                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode5 = False

                        # 1초 딜레이
                        time.sleep(1)
                        # 보유수량 불러오기
                        krw_balance5 = upbit.get_balance(krw_coin5)
                        # 코인 현재가 불러오기
                        price5 = pyupbit.get_current_price(krw_coin5)
                        # 보유코인 원화금액으로 계산하기
                        bp5 = price5 * krw_balance5

                        # 보유 및 매수 가능 출력.
                        print(f"[ 5. {krw_coin5} 매수완료. ]")
                        print(f"매수시간 : {now}  |  코인명 : {coin5}  |  현재가 = ￦{price5}  |  금일목표가 = ￦{target5}  |  보유수량 = {krw_balance5}  |  평가금액 = ￦{bp5}")
                        print(f"매수가능 - {op_mode5} - 불가")
                        print("")
                    else:
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode5 = False

                        print(f"[ 5. {krw_coin5} 잔고부족으로 매수안함. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin5}  |  현재매수가능 - {op_mode5} - 불가")
                        print("")

                elif krw5 <= buy_krw:   # 매수가능금액 krw5 가 매수평균가 buy_krw 보다 같거나 작을때
                    if krw5 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                        # 매수금액은 매수가능금액인 krw5 로
                        upbit.buy_market_order(krw_coin5, krw5 * 0.99)   # 매수가능금액에서 1%를 빼고

                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode5 = False

                        # 1초 딜레이
                        time.sleep(1)
                        # 보유수량 불러오기
                        krw_balance5 = upbit.get_balance(krw_coin5)
                        # 코인 현재가 불러오기
                        price5 = pyupbit.get_current_price(krw_coin5)
                        # 보유코인 원화금액으로 계산하기
                        bp5 = price5 * krw_balance5

                        # 보유 및 매수 가능 출력.
                        print(f"[ 5. {krw_coin5} 매수완료. ]")
                        print(f"매수시간 : {now}  |  코인명 : {coin5}  |  현재가 = ￦{price5}  |  금일목표가 = ￦{target5}  |  보유수량 = {krw_balance5}  |  평가금액 = ￦{bp5}")
                        print(f"매수가능 - {op_mode5} - 불가")
                        print("")
                    else:
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode5 = False

                        print(f"[ 5. {krw_coin5} 잔고부족으로 매수안함. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin5}  |  현재매수가능 - {op_mode5} - 불가")
                        print("")

        # 1초 딜레이.
        time.sleep(1)
        ##### 5번 코인 매수 종료 #####
        #############################


        ##### 6번코인 매수 시도 #####
        if op_mode6 == True:    # 매수 가능(True)일 경우 - 매수시도
            # 코인 현재가 불러오기
            price6 = pyupbit.get_current_price(krw_coin6)
            # 코인 목표가 불러오기
            target6 = cal_target(krw_coin6)

            if price6 >= target6:   # 목표가보다 현재가가 높을때
                # 매수가능금액 불러오기
                krw6 = upbit.get_balance("KRW")

                if krw6 > buy_krw:    # 매수가능금액 krw6 이 매수설정금액 buy_krw 보다 많을 경우: 매수
                    if krw6 > 10100:     # 매수가능금액 krw6 이 10,100원 초과일 경우 : 매수
                        # 매수금액은 매수평균가 buy_krw 로
                        upbit.buy_market_order(krw_coin6, buy_krw * 0.99)   # 매수가능금액에서 1%를 빼고

                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode6 = False

                        # 1초 딜레이
                        time.sleep(1)
                        # 보유수량 불러오기
                        krw_balance6 = upbit.get_balance(krw_coin6)
                        # 코인 현재가 불러오기
                        price6 = pyupbit.get_current_price(krw_coin6)
                        # 보유코인 원화금액으로 계산하기
                        bp6 = price6 * krw_balance6

                        # 보유 및 매수 가능 출력.
                        print(f"[ 6. {krw_coin6} 매수완료. ]")
                        print(f"매수시간 : {now}  |  코인명 : {coin6}  |  현재가 = ￦{price6}  |  금일목표가 = ￦{target6}  |  보유수량 = {krw_balance6}  |  평가금액 = ￦{bp6}")
                        print(f"매수가능 - {op_mode6} - 불가")
                        print("")
                    else:
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode6 = False

                        print(f"[ 6. {krw_coin6} 잔고부족으로 매수안함. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin6}  |  현재매수가능 - {op_mode6} - 불가")
                        print("")

                elif krw6 <= buy_krw:   # 매수가능금액 krw6 가 매수평균가 buy_krw 보다 같거나 작을때
                    if krw6 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                        # 매수금액은 매수가능금액인 krw6 로
                        upbit.buy_market_order(krw_coin6, krw6 * 0.99)   # 매수가능금액에서 1%를 빼고

                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode6 = False

                        # 1초 딜레이
                        time.sleep(1)
                        # 보유수량 불러오기
                        krw_balance6 = upbit.get_balance(krw_coin6)
                        # 코인 현재가 불러오기
                        price6 = pyupbit.get_current_price(krw_coin6)
                        # 보유코인 원화금액으로 계산하기
                        bp6 = price6 * krw_balance6

                        # 보유 및 매수 가능 출력.
                        print(f"[ 6. {krw_coin6} 매수완료. ]")
                        print(f"매수시간 : {now}  |  코인명 : {coin6}  |  현재가 = ￦{price6}  |  금일목표가 = ￦{target6}  |  보유수량 = {krw_balance6}  |  평가금액 = ￦{bp6}")
                        print(f"매수가능 - {op_mode6} - 불가")
                        print("")
                    else:
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode6 = False

                        print(f"[ 6. {krw_coin6} 잔고부족으로 매수안함. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin6}  |  현재매수가능 - {op_mode6} - 불가")
                        print("")

        # 1초 딜레이.
        #time.sleep(1)
        ##### 6번 코인 매수 종료 #####
        #############################


        ##### 7번코인 매수 시도 #####
        if op_mode7 == True:    # 매수 가능(True)일 경우 - 매수시도
            # 코인 현재가 불러오기
            price7 = pyupbit.get_current_price(krw_coin7)
            # 코인 목표가 불러오기
            target7 = cal_target(krw_coin7)

            if price7 >= target7:   # 목표가보다 현재가가 높을때
                # 매수가능금액 불러오기
                krw7 = upbit.get_balance("KRW")

                if krw7 > buy_krw:    # 매수가능금액 krw7 이 매수설정금액 buy_krw 보다 많을 경우: 매수
                    if krw7 > 10100:     # 매수가능금액 krw7 이 10,100원 초과일 경우 : 매수
                        # 매수금액은 매수평균가 buy_krw 로
                        upbit.buy_market_order(krw_coin7, buy_krw * 0.99)   # 매수가능금액에서 1%를 빼고

                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode7 = False

                        # 1초 딜레이
                        time.sleep(1)
                        # 보유수량 불러오기
                        krw_balance7 = upbit.get_balance(krw_coin7)
                        # 코인 현재가 불러오기
                        price7 = pyupbit.get_current_price(krw_coin7)
                        # 보유코인 원화금액으로 계산하기
                        bp7 = price7 * krw_balance7

                        # 보유 및 매수 가능 출력.
                        print(f"[ 7. {krw_coin7} 매수완료. ]")
                        print(f"매수시간 : {now}  |  코인명 : {coin7}  |  현재가 = ￦{price7}  |  금일목표가 = ￦{target7}  |  보유수량 = {krw_balance7}  |  평가금액 = ￦{bp7}")
                        print(f"매수가능 - {op_mode7} - 불가")
                        print("")
                    else:
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode7 = False

                        print(f"[ 7. {krw_coin7} 잔고부족으로 매수안함. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin7}  |  현재매수가능 - {op_mode7} - 불가")
                        print("")

                elif krw7 <= buy_krw:   # 매수가능금액 krw7 가 매수평균가 buy_krw 보다 같거나 작을때
                    if krw7 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                        # 매수금액은 매수가능금액인 krw7 로
                        upbit.buy_market_order(krw_coin7, krw7 * 0.99)   # 매수가능금액에서 1%를 빼고

                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode7 = False

                        # 1초 딜레이
                        time.sleep(1)
                        # 보유수량 불러오기
                        krw_balance7 = upbit.get_balance(krw_coin7)
                        # 코인 현재가 불러오기
                        price7 = pyupbit.get_current_price(krw_coin7)
                        # 보유코인 원화금액으로 계산하기
                        bp7 = price7 * krw_balance7

                        # 보유 및 매수 가능 출력.
                        print(f"[ 7. {krw_coin7} 매수완료. ]")
                        print(f"매수시간 : {now}  |  코인명 : {coin7}  |  현재가 = ￦{price7}  |  금일목표가 = ￦{target7}  |  보유수량 = {krw_balance7}  |  평가금액 = ￦{bp7}")
                        print(f"매수가능 - {op_mode7} - 불가")
                        print("")
                    else:
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode7 = False

                        print(f"[ 7. {krw_coin7} 잔고부족으로 매수안함. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin7}  |  현재매수가능 - {op_mode7} - 불가")
                        print("")

        # 1초 딜레이.
        #time.sleep(1)
        ##### 7번 코인 매수 종료 #####
        #############################


        ##### 8번코인 매수 시도 #####
        if op_mode8 == True:    # 매수 가능(True)일 경우 - 매수시도
            # 코인 현재가 불러오기
            price8 = pyupbit.get_current_price(krw_coin8)
            # 코인 목표가 불러오기
            target8 = cal_target(krw_coin8)

            if price8 >= target8:   # 목표가보다 현재가가 높을때
                # 매수가능금액 불러오기
                krw8 = upbit.get_balance("KRW")

                if krw8 > buy_krw:    # 매수가능금액 krw8 이 매수설정금액 buy_krw 보다 많을 경우: 매수
                    if krw8 > 10100:     # 매수가능금액 krw8 이 10,100원 초과일 경우 : 매수
                        # 매수금액은 매수평균가 buy_krw 로
                        upbit.buy_market_order(krw_coin8, buy_krw * 0.99)   # 매수가능금액에서 1%를 빼고

                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode8 = False

                        # 1초 딜레이
                        time.sleep(1)
                        # 보유수량 불러오기
                        krw_balance8 = upbit.get_balance(krw_coin8)
                        # 코인 현재가 불러오기
                        price8 = pyupbit.get_current_price(krw_coin8)
                        # 보유코인 원화금액으로 계산하기
                        bp8 = price8 * krw_balance8

                        # 보유 및 매수 가능 출력.
                        print(f"[ 8. {krw_coin8} 매수완료. ]")
                        print(f"매수시간 : {now}  |  코인명 : {coin8}  |  현재가 = ￦{price8}  |  금일목표가 = ￦{target8}  |  보유수량 = {krw_balance8}  |  평가금액 = ￦{bp8}")
                        print(f"매수가능 - {op_mode8} - 불가")
                        print("")
                    else:
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode8 = False

                        print(f"[ 8. {krw_coin8} 잔고부족으로 매수안함. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin8}  |  현재매수가능 - {op_mode8} - 불가")
                        print("")

                elif krw8 <= buy_krw:   # 매수가능금액 krw8 가 매수평균가 buy_krw 보다 같거나 작을때
                    if krw8 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                        # 매수금액은 매수가능금액인 krw8 로
                        upbit.buy_market_order(krw_coin8, krw8 * 0.99)   # 매수가능금액에서 1%를 빼고

                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode8 = False

                        # 1초 딜레이
                        time.sleep(1)
                        # 보유수량 불러오기
                        krw_balance8 = upbit.get_balance(krw_coin8)
                        # 코인 현재가 불러오기
                        price8 = pyupbit.get_current_price(krw_coin8)
                        # 보유코인 원화금액으로 계산하기
                        bp8 = price8 * krw_balance8

                        # 보유 및 매수 가능 출력.
                        print(f"[ 8. {krw_coin8} 매수완료. ]")
                        print(f"매수시간 : {now}  |  코인명 : {coin8}  |  현재가 = ￦{price8}  |  금일목표가 = ￦{target8}  |  보유수량 = {krw_balance8}  |  평가금액 = ￦{bp8}")
                        print(f"매수가능 - {op_mode8} - 불가")
                        print("")
                    else:
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode8 = False

                        print(f"[ 8. {krw_coin8} 잔고부족으로 매수안함. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin8}  |  현재매수가능 - {op_mode8} - 불가")
                        print("")

        # 1초 딜레이.
        #time.sleep(1)
        ##### 8번 코인 매수 종료 #####
        #############################


        ##### 9번코인 매수 시도 #####
        if op_mode9 == True:    # 매수 가능(True)일 경우 - 매수시도
            # 코인 현재가 불러오기
            price9 = pyupbit.get_current_price(krw_coin9)
            # 코인 목표가 불러오기
            target9 = cal_target(krw_coin9)

            if price9 >= target9:   # 목표가보다 현재가가 높을때
                # 매수가능금액 불러오기
                krw9 = upbit.get_balance("KRW")

                if krw9 > buy_krw:    # 매수가능금액 krw9 이 매수설정금액 buy_krw 보다 많을 경우: 매수
                    if krw9 > 10100:     # 매수가능금액 krw9 이 10,100원 초과일 경우 : 매수
                        # 매수금액은 매수평균가 buy_krw 로
                        upbit.buy_market_order(krw_coin9, buy_krw * 0.99)   # 매수가능금액에서 1%를 빼고

                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode9 = False

                        # 1초 딜레이
                        time.sleep(1)
                        # 보유수량 불러오기
                        krw_balance9 = upbit.get_balance(krw_coin9)
                        # 코인 현재가 불러오기
                        price9 = pyupbit.get_current_price(krw_coin9)
                        # 보유코인 원화금액으로 계산하기
                        bp9 = price9 * krw_balance9

                        # 보유 및 매수 가능 출력.
                        print(f"[ 9. {krw_coin9} 매수완료. ]")
                        print(f"매수시간 : {now}  |  코인명 : {coin9}  |  현재가 = ￦{price9}  |  금일목표가 = ￦{target9}  |  보유수량 = {krw_balance9}  |  평가금액 = ￦{bp9}")
                        print(f"매수가능 - {op_mode9} - 불가")
                        print("")
                    else:
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode9 = False

                        print(f"[ 9. {krw_coin9} 잔고부족으로 매수안함. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin9}  |  현재매수가능 - {op_mode9} - 불가")
                        print("")

                elif krw9 <= buy_krw:   # 매수가능금액 krw9 가 매수평균가 buy_krw 보다 같거나 작을때
                    if krw9 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                        # 매수금액은 매수가능금액인 krw9 로
                        upbit.buy_market_order(krw_coin9, krw9 * 0.99)   # 매수가능금액에서 1%를 빼고

                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode9 = False

                        # 1초 딜레이
                        time.sleep(1)
                        # 보유수량 불러오기
                        krw_balance9 = upbit.get_balance(krw_coin9)
                        # 코인 현재가 불러오기
                        price9 = pyupbit.get_current_price(krw_coin9)
                        # 보유코인 원화금액으로 계산하기
                        bp9 = price9 * krw_balance9

                        # 보유 및 매수 가능 출력.
                        print(f"[ 9. {krw_coin9} 매수완료. ]")
                        print(f"매수시간 : {now}  |  코인명 : {coin9}  |  현재가 = ￦{price9}  |  금일목표가 = ￦{target9}  |  보유수량 = {krw_balance9}  |  평가금액 = ￦{bp9}")
                        print(f"매수가능 - {op_mode9} - 불가")
                        print("")
                    else:
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode9 = False

                        print(f"[ 9. {krw_coin9} 잔고부족으로 매수안함. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin9}  |  현재매수가능 - {op_mode9} - 불가")
                        print("")

        # 1초 딜레이.
        #time.sleep(1)
        ##### 9번 코인 매수 종료 #####
        #############################


        ##### 10번코인 매수 시도 #####
        if op_mode10 == True:    # 매수 가능(True)일 경우 - 매수시도
            # 코인 현재가 불러오기
            price10 = pyupbit.get_current_price(krw_coin10)
            # 코인 목표가 불러오기
            target10 = cal_target(krw_coin10)

            if price10 >= target10:   # 목표가보다 현재가가 높을때
                # 매수가능금액 불러오기
                krw10 = upbit.get_balance("KRW")

                if krw10 > buy_krw:    # 매수가능금액 krw10 이 매수설정금액 buy_krw 보다 많을 경우: 매수
                    if krw10 > 10100:     # 매수가능금액 krw10 이 10,100원 초과일 경우 : 매수
                        # 매수금액은 매수평균가 buy_krw 로
                        upbit.buy_market_order(krw_coin10, buy_krw * 0.99)   # 매수가능금액에서 1%를 빼고

                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode10 = False

                        # 1초 딜레이
                        time.sleep(1)
                        # 보유수량 불러오기
                        krw_balance10 = upbit.get_balance(krw_coin10)
                        # 코인 현재가 불러오기
                        price10 = pyupbit.get_current_price(krw_coin10)
                        # 보유코인 원화금액으로 계산하기
                        bp10 = price10 * krw_balance10

                        # 보유 및 매수 가능 출력.
                        print(f"[ 10. {krw_coin10} 매수완료. ]")
                        print(f"매수시간 : {now}  |  코인명 : {coin10}  |  현재가 = ￦{price10}  |  금일목표가 = ￦{target10}  |  보유수량 = {krw_balance10}  |  평가금액 = ￦{bp10}")
                        print(f"매수가능 - {op_mode10} - 불가")
                        print("")
                    else:
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode10 = False

                        print(f"[ 10. {krw_coin10} 잔고부족으로 매수안함. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin10}  |  현재매수가능 - {op_mode10} - 불가")
                        print("")

                elif krw10 <= buy_krw:   # 매수가능금액 krw10 가 매수평균가 buy_krw 보다 같거나 작을때
                    if krw10 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                        # 매수금액은 매수가능금액인 krw10 로
                        upbit.buy_market_order(krw_coin10, krw10 * 0.99)   # 매수가능금액에서 1%를 빼고

                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode10 = False

                        # 1초 딜레이
                        time.sleep(1)
                        # 보유수량 불러오기
                        krw_balance10 = upbit.get_balance(krw_coin10)
                        # 코인 현재가 불러오기
                        price10 = pyupbit.get_current_price(krw_coin10)
                        # 보유코인 원화금액으로 계산하기
                        bp10 = price10 * krw_balance10

                        # 보유 및 매수 가능 출력.
                        print(f"[ 10. {krw_coin10} 매수완료. ]")
                        print(f"매수시간 : {now}  |  코인명 : {coin10}  |  현재가 = ￦{price10}  |  금일목표가 = ￦{target10}  |  보유수량 = {krw_balance10}  |  평가금액 = ￦{bp10}")
                        print(f"매수가능 - {op_mode10} - 불가")
                        print("")
                    else:
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode10 = False

                        print(f"[ 10. {krw_coin10} 잔고부족으로 매수안함. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin10}  |  현재매수가능 - {op_mode10} - 불가")
                        print("")

        # 1초 딜레이.
        time.sleep(1)
        ##### 10번 코인 매수 종료 #####
        #############################


        ######################################################################################################################################################
        ######################################################################################################################################################
        ######################################################################################################################################################


        ##### 11번코인 매수 시도 #####
        if op_mode11 == True:    # 매수 가능(True)일 경우 - 매수시도
            # 코인 현재가 불러오기
            price11 = pyupbit.get_current_price(krw_coin11)
            # 코인 목표가 불러오기
            target11 = cal_target(krw_coin11)

            if price11 >= target11:   # 목표가보다 현재가가 높을때
                # 매수가능금액 불러오기
                krw11 = upbit.get_balance("KRW")

                if krw11 > buy_krw:    # 매수가능금액 krw11 이 매수설정금액 buy_krw 보다 많을 경우: 매수
                    if krw11 > 10100:     # 매수가능금액 krw11 이 10,100원 초과일 경우 : 매수
                        # 매수금액은 매수평균가 buy_krw 로
                        upbit.buy_market_order(krw_coin11, buy_krw * 0.99)   # 매수가능금액에서 1%를 빼고

                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode11 = False

                        # 1초 딜레이
                        time.sleep(1)
                        # 보유수량 불러오기
                        krw_balance11 = upbit.get_balance(krw_coin11)
                        # 코인 현재가 불러오기
                        price11 = pyupbit.get_current_price(krw_coin11)
                        # 보유코인 원화금액으로 계산하기
                        bp11 = price11 * krw_balance11

                        # 보유 및 매수 가능 출력.
                        print(f"[ 11. {krw_coin11} 매수완료. ]")
                        print(f"매수시간 : {now}  |  코인명 : {coin11}  |  현재가 = ￦{price11}  |  금일목표가 = ￦{target11}  |  보유수량 = {krw_balance11}  |  평가금액 = ￦{bp11}")
                        print(f"매수가능 - {op_mode11} - 불가")
                        print("")
                    else:
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode11 = False

                        print(f"[ 11. {krw_coin11} 잔고부족으로 매수안함. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin11}  |  현재매수가능 - {op_mode11} - 불가")
                        print("")

                elif krw11 <= buy_krw:   # 매수가능금액 krw11 가 매수평균가 buy_krw 보다 같거나 작을때
                    if krw11 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                        # 매수금액은 매수가능금액인 krw1 로
                        upbit.buy_market_order(krw_coin11, krw11 * 0.99)   # 매수가능금액에서 1%를 빼고

                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode11 = False

                        # 1초 딜레이
                        time.sleep(1)
                        # 보유수량 불러오기
                        krw_balance11 = upbit.get_balance(krw_coin11)
                        # 코인 현재가 불러오기
                        price11 = pyupbit.get_current_price(krw_coin11)
                        # 보유코인 원화금액으로 계산하기
                        bp11 = price11 * krw_balance11

                        # 보유 및 매수 가능 출력.
                        print(f"[ 11. {krw_coin11} 매수완료. ]")
                        print(f"매수시간 : {now}  |  코인명 : {coin11}  |  현재가 = ￦{price11}  |  금일목표가 = ￦{target11}  |  보유수량 = {krw_balance11}  |  평가금액 = ￦{bp11}")
                        print(f"매수가능 - {op_mode11} - 불가")
                        print("")
                    else:
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode11 = False

                        print(f"[ 11. {krw_coin11} 잔고부족으로 매수안함. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin11}  |  현재매수가능 - {op_mode11} - 불가")
                        print("")

        # 1초 딜레이.
        #time.sleep(1)
        ##### 11번 코인 매수 종료 #####
        #############################


        ##### 12번코인 매수 시도 #####
        if op_mode12 == True:    # 매수 가능(True)일 경우 - 매수시도
            # 코인 현재가 불러오기
            price12 = pyupbit.get_current_price(krw_coin12)
            # 코인 목표가 불러오기
            target12 = cal_target(krw_coin12)

            if price12 >= target12:   # 목표가보다 현재가가 높을때
                # 매수가능금액 불러오기
                krw12 = upbit.get_balance("KRW")

                if krw12 > buy_krw:    # 매수가능금액 krw12 이 매수설정금액 buy_krw 보다 많을 경우: 매수
                    if krw12 > 10100:     # 매수가능금액 krw12 이 10,100원 초과일 경우 : 매수
                        # 매수금액은 매수평균가 buy_krw 로
                        upbit.buy_market_order(krw_coin12, buy_krw * 0.99)   # 매수가능금액에서 1%를 빼고

                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode12 = False

                        # 1초 딜레이
                        time.sleep(1)
                        # 보유수량 불러오기
                        krw_balance12 = upbit.get_balance(krw_coin12)
                        # 코인 현재가 불러오기
                        price12 = pyupbit.get_current_price(krw_coin12)
                        # 보유코인 원화금액으로 계산하기
                        bp12 = price12 * krw_balance12

                        # 보유 및 매수 가능 출력.
                        print(f"[ 12. {krw_coin12} 매수완료. ]")
                        print(f"매수시간 : {now}  |  코인명 : {coin12}  |  현재가 = ￦{price12}  |  금일목표가 = ￦{target12}  |  보유수량 = {krw_balance12}  |  평가금액 = ￦{bp12}")
                        print(f"매수가능 - {op_mode12} - 불가")
                        print("")
                    else:
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode12 = False

                        print(f"[ 12. {krw_coin12} 잔고부족으로 매수안함. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin12}  |  현재매수가능 - {op_mode12} - 불가")
                        print("")

                elif krw12 <= buy_krw:   # 매수가능금액 krw12 가 매수평균가 buy_krw 보다 같거나 작을때
                    if krw12 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                        # 매수금액은 매수가능금액인 krw12 로
                        upbit.buy_market_order(krw_coin12, krw12 * 0.99)   # 매수가능금액에서 1%를 빼고

                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode12 = False

                        # 1초 딜레이
                        time.sleep(1)
                        # 보유수량 불러오기
                        krw_balance12 = upbit.get_balance(krw_coin12)
                        # 코인 현재가 불러오기
                        price12 = pyupbit.get_current_price(krw_coin12)
                        # 보유코인 원화금액으로 계산하기
                        bp12 = price12 * krw_balance12

                        # 보유 및 매수 가능 출력.
                        print(f"[ 12. {krw_coin12} 매수완료. ]")
                        print(f"매수시간 : {now}  |  코인명 : {coin12}  |  현재가 = ￦{price12}  |  금일목표가 = ￦{target12}  |  보유수량 = {krw_balance12}  |  평가금액 = ￦{bp12}")
                        print(f"매수가능 - {op_mode12} - 불가")
                        print("")
                    else:
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode12 = False

                        print(f"[ 12. {krw_coin12} 잔고부족으로 매수안함. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin12}  |  현재매수가능 - {op_mode12} - 불가")
                        print("")

        # 1초 딜레이.
        #time.sleep(1)
        ##### 12번 코인 매수 종료 #####
        #############################


        ##### 13번코인 매수 시도 #####
        if op_mode13 == True:    # 매수 가능(True)일 경우 - 매수시도
            # 코인 현재가 불러오기
            price13 = pyupbit.get_current_price(krw_coin13)
            # 코인 목표가 불러오기
            target13 = cal_target(krw_coin13)

            if price13 >= target13:   # 목표가보다 현재가가 높을때
                # 매수가능금액 불러오기
                krw13 = upbit.get_balance("KRW")

                if krw13 > buy_krw:    # 매수가능금액 krw13 이 매수설정금액 buy_krw 보다 많을 경우: 매수
                    if krw13 > 10100:     # 매수가능금액 krw13 이 10,100원 초과일 경우 : 매수
                        # 매수금액은 매수평균가 buy_krw 로
                        upbit.buy_market_order(krw_coin13, buy_krw * 0.99)   # 매수가능금액에서 1%를 빼고

                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode13 = False

                        # 1초 딜레이
                        time.sleep(1)
                        # 보유수량 불러오기
                        krw_balance13 = upbit.get_balance(krw_coin13)
                        # 코인 현재가 불러오기
                        price13 = pyupbit.get_current_price(krw_coin13)
                        # 보유코인 원화금액으로 계산하기
                        bp13 = price13 * krw_balance13

                        # 보유 및 매수 가능 출력.
                        print(f"[ 13. {krw_coin13} 매수완료. ]")
                        print(f"매수시간 : {now}  |  코인명 : {coin13}  |  현재가 = ￦{price13}  |  금일목표가 = ￦{target13}  |  보유수량 = {krw_balance13}  |  평가금액 = ￦{bp13}")
                        print(f"매수가능 - {op_mode13} - 불가")
                        print("")
                    else:
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode13 = False

                        print(f"[ 13. {krw_coin13} 잔고부족으로 매수안함. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin13}  |  현재매수가능 - {op_mode13} - 불가")
                        print("")

                elif krw13 <= buy_krw:   # 매수가능금액 krw13 가 매수평균가 buy_krw 보다 같거나 작을때
                    if krw13 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                        # 매수금액은 매수가능금액인 krw13 로
                        upbit.buy_market_order(krw_coin13, krw13 * 0.99)   # 매수가능금액에서 1%를 빼고

                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode13 = False

                        # 1초 딜레이
                        time.sleep(1)
                        # 보유수량 불러오기
                        krw_balance13 = upbit.get_balance(krw_coin13)
                        # 코인 현재가 불러오기
                        price13 = pyupbit.get_current_price(krw_coin13)
                        # 보유코인 원화금액으로 계산하기
                        bp13 = price13 * krw_balance13

                        # 보유 및 매수 가능 출력.
                        print(f"[ 13. {krw_coin13} 매수완료. ]")
                        print(f"매수시간 : {now}  |  코인명 : {coin13}  |  현재가 = ￦{price13}  |  금일목표가 = ￦{target13}  |  보유수량 = {krw_balance13}  |  평가금액 = ￦{bp13}")
                        print(f"매수가능 - {op_mode13} - 불가")
                        print("")
                    else:
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode13 = False

                        print(f"[ 13. {krw_coin13} 잔고부족으로 매수안함. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin13}  |  현재매수가능 - {op_mode13} - 불가")
                        print("")

        # 1초 딜레이.
        #time.sleep(1)
        ##### 13번 코인 매수 종료 #####
        #############################


        ##### 14번코인 매수 시도 #####
        if op_mode14 == True:    # 매수 가능(True)일 경우 - 매수시도
            # 코인 현재가 불러오기
            price14 = pyupbit.get_current_price(krw_coin14)
            # 코인 목표가 불러오기
            target14 = cal_target(krw_coin14)

            if price14 >= target14:   # 목표가보다 현재가가 높을때
                # 매수가능금액 불러오기
                krw14 = upbit.get_balance("KRW")

                if krw14 > buy_krw:    # 매수가능금액 krw14 이 매수설정금액 buy_krw 보다 많을 경우: 매수
                    if krw14 > 10100:     # 매수가능금액 krw14 이 10,100원 초과일 경우 : 매수
                        # 매수금액은 매수평균가 buy_krw 로
                        upbit.buy_market_order(krw_coin14, buy_krw * 0.99)   # 매수가능금액에서 1%를 빼고

                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode14 = False

                        # 1초 딜레이
                        time.sleep(1)
                        # 보유수량 불러오기
                        krw_balance14 = upbit.get_balance(krw_coin14)
                        # 코인 현재가 불러오기
                        price14 = pyupbit.get_current_price(krw_coin14)
                        # 보유코인 원화금액으로 계산하기
                        bp14 = price14 * krw_balance14

                        # 보유 및 매수 가능 출력.
                        print(f"[ 14. {krw_coin14} 매수완료. ]")
                        print(f"매수시간 : {now}  |  코인명 : {coin14}  |  현재가 = ￦{price14}  |  금일목표가 = ￦{target14}  |  보유수량 = {krw_balance14}  |  평가금액 = ￦{bp14}")
                        print(f"매수가능 - {op_mode14} - 불가")
                        print("")
                    else:
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode14 = False

                        print(f"[ 14. {krw_coin14} 잔고부족으로 매수안함. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin14}  |  현재매수가능 - {op_mode14} - 불가")
                        print("")

                elif krw14 <= buy_krw:   # 매수가능금액 krw14 가 매수평균가 buy_krw 보다 같거나 작을때
                    if krw14 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                        # 매수금액은 매수가능금액인 krw14 로
                        upbit.buy_market_order(krw_coin14, krw14 * 0.99)   # 매수가능금액에서 1%를 빼고

                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode14 = False

                        # 1초 딜레이
                        time.sleep(1)
                        # 보유수량 불러오기
                        krw_balance14 = upbit.get_balance(krw_coin14)
                        # 코인 현재가 불러오기
                        price14 = pyupbit.get_current_price(krw_coin14)
                        # 보유코인 원화금액으로 계산하기
                        bp14 = price14 * krw_balance14

                        # 보유 및 매수 가능 출력.
                        print(f"[ 14. {krw_coin14} 매수완료. ]")
                        print(f"매수시간 : {now}  |  코인명 : {coin14}  |  현재가 = ￦{price14}  |  금일목표가 = ￦{target14}  |  보유수량 = {krw_balance14}  |  평가금액 = ￦{bp14}")
                        print(f"매수가능 - {op_mode14} - 불가")
                        print("")
                    else:
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode14 = False

                        print(f"[ 14. {krw_coin14} 잔고부족으로 매수안함. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin14}  |  현재매수가능 - {op_mode14} - 불가")
                        print("")

        # 1초 딜레이.
        #time.sleep(1)
        ##### 14번 코인 매수 종료 #####
        #############################


        ##### 15번코인 매수 시도 #####
        if op_mode15 == True:    # 매수 가능(True)일 경우 - 매수시도
            # 코인 현재가 불러오기
            price15 = pyupbit.get_current_price(krw_coin15)
            # 코인 목표가 불러오기
            target15 = cal_target(krw_coin15)

            if price15 >= target15:   # 목표가보다 현재가가 높을때
                # 매수가능금액 불러오기
                krw15 = upbit.get_balance("KRW")

                if krw15 > buy_krw:    # 매수가능금액 krw15 이 매수설정금액 buy_krw 보다 많을 경우: 매수
                    if krw15 > 10100:     # 매수가능금액 krw15 이 10,100원 초과일 경우 : 매수
                        # 매수금액은 매수평균가 buy_krw 로
                        upbit.buy_market_order(krw_coin15, buy_krw * 0.99)   # 매수가능금액에서 1%를 빼고

                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode15 = False

                        # 1초 딜레이
                        time.sleep(1)
                        # 보유수량 불러오기
                        krw_balance15 = upbit.get_balance(krw_coin15)
                        # 코인 현재가 불러오기
                        price15 = pyupbit.get_current_price(krw_coin15)
                        # 보유코인 원화금액으로 계산하기
                        bp15 = price15 * krw_balance15

                        # 보유 및 매수 가능 출력.
                        print(f"[ 15. {krw_coin15} 매수완료. ]")
                        print(f"매수시간 : {now}  |  코인명 : {coin15}  |  현재가 = ￦{price15}  |  금일목표가 = ￦{target15}  |  보유수량 = {krw_balance15}  |  평가금액 = ￦{bp15}")
                        print(f"매수가능 - {op_mode15} - 불가")
                        print("")
                    else:
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode15 = False

                        print(f"[ 15. {krw_coin15} 잔고부족으로 매수안함. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin15}  |  현재매수가능 - {op_mode15} - 불가")
                        print("")

                elif krw15 <= buy_krw:   # 매수가능금액 krw15 가 매수평균가 buy_krw 보다 같거나 작을때
                    if krw15 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                        # 매수금액은 매수가능금액인 krw15 로
                        upbit.buy_market_order(krw_coin15, krw15 * 0.99)   # 매수가능금액에서 1%를 빼고

                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode15 = False

                        # 1초 딜레이
                        time.sleep(1)
                        # 보유수량 불러오기
                        krw_balance15 = upbit.get_balance(krw_coin15)
                        # 코인 현재가 불러오기
                        price15 = pyupbit.get_current_price(krw_coin15)
                        # 보유코인 원화금액으로 계산하기
                        bp15 = price15 * krw_balance15

                        # 보유 및 매수 가능 출력.
                        print(f"[ 15. {krw_coin15} 매수완료. ]")
                        print(f"매수시간 : {now}  |  코인명 : {coin15}  |  현재가 = ￦{price15}  |  금일목표가 = ￦{target15}  |  보유수량 = {krw_balance15}  |  평가금액 = ￦{bp15}")
                        print(f"매수가능 - {op_mode15} - 불가")
                        print("")
                    else:
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode15 = False

                        print(f"[ 15. {krw_coin15} 잔고부족으로 매수안함. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin15}  |  현재매수가능 - {op_mode15} - 불가")
                        print("")

        # 1초 딜레이.
        time.sleep(1)
        ##### 15번 코인 매수 종료 #####
        #############################


        ##### 16번코인 매수 시도 #####
        if op_mode16 == True:    # 매수 가능(True)일 경우 - 매수시도
            # 코인 현재가 불러오기
            price16 = pyupbit.get_current_price(krw_coin16)
            # 코인 목표가 불러오기
            target16 = cal_target(krw_coin16)

            if price16 >= target16:   # 목표가보다 현재가가 높을때
                # 매수가능금액 불러오기
                krw16 = upbit.get_balance("KRW")

                if krw16 > buy_krw:    # 매수가능금액 krw16 이 매수설정금액 buy_krw 보다 많을 경우: 매수
                    if krw16 > 10100:     # 매수가능금액 krw16 이 10,100원 초과일 경우 : 매수
                        # 매수금액은 매수평균가 buy_krw 로
                        upbit.buy_market_order(krw_coin16, buy_krw * 0.99)   # 매수가능금액에서 1%를 빼고

                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode16 = False

                        # 1초 딜레이
                        time.sleep(1)
                        # 보유수량 불러오기
                        krw_balance16 = upbit.get_balance(krw_coin16)
                        # 코인 현재가 불러오기
                        price16 = pyupbit.get_current_price(krw_coin16)
                        # 보유코인 원화금액으로 계산하기
                        bp16 = price16 * krw_balance16

                        # 보유 및 매수 가능 출력.
                        print(f"[ 16. {krw_coin16} 매수완료. ]")
                        print(f"매수시간 : {now}  |  코인명 : {coin16}  |  현재가 = ￦{price16}  |  금일목표가 = ￦{target16}  |  보유수량 = {krw_balance16}  |  평가금액 = ￦{bp16}")
                        print(f"매수가능 - {op_mode16} - 불가")
                        print("")
                    else:
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode16 = False

                        print(f"[ 16. {krw_coin16} 잔고부족으로 매수안함. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin16}  |  현재매수가능 - {op_mode16} - 불가")
                        print("")

                elif krw16 <= buy_krw:   # 매수가능금액 krw16 가 매수평균가 buy_krw 보다 같거나 작을때
                    if krw16 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                        # 매수금액은 매수가능금액인 krw16 로
                        upbit.buy_market_order(krw_coin16, krw16 * 0.99)   # 매수가능금액에서 1%를 빼고

                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode16 = False

                        # 1초 딜레이
                        time.sleep(1)
                        # 보유수량 불러오기
                        krw_balance16 = upbit.get_balance(krw_coin16)
                        # 코인 현재가 불러오기
                        price16 = pyupbit.get_current_price(krw_coin16)
                        # 보유코인 원화금액으로 계산하기
                        bp16 = price16 * krw_balance16

                        # 보유 및 매수 가능 출력.
                        print(f"[ 16. {krw_coin16} 매수완료. ]")
                        print(f"매수시간 : {now}  |  코인명 : {coin16}  |  현재가 = ￦{price16}  |  금일목표가 = ￦{target16}  |  보유수량 = {krw_balance16}  |  평가금액 = ￦{bp16}")
                        print(f"매수가능 - {op_mode16} - 불가")
                        print("")
                    else:
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode16 = False

                        print(f"[ 16. {krw_coin16} 잔고부족으로 매수안함. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin16}  |  현재매수가능 - {op_mode16} - 불가")
                        print("")

        # 1초 딜레이.
        #time.sleep(1)
        ##### 16번 코인 매수 종료 #####
        #############################


        ##### 17번코인 매수 시도 #####
        if op_mode17 == True:    # 매수 가능(True)일 경우 - 매수시도
            # 코인 현재가 불러오기
            price17 = pyupbit.get_current_price(krw_coin17)
            # 코인 목표가 불러오기
            target17 = cal_target(krw_coin17)

            if price17 >= target17:   # 목표가보다 현재가가 높을때
                # 매수가능금액 불러오기
                krw17 = upbit.get_balance("KRW")

                if krw17 > buy_krw:    # 매수가능금액 krw17 이 매수설정금액 buy_krw 보다 많을 경우: 매수
                    if krw17 > 10100:     # 매수가능금액 krw17 이 10,100원 초과일 경우 : 매수
                        # 매수금액은 매수평균가 buy_krw 로
                        upbit.buy_market_order(krw_coin17, buy_krw * 0.99)   # 매수가능금액에서 1%를 빼고

                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode17 = False

                        # 1초 딜레이
                        time.sleep(1)
                        # 보유수량 불러오기
                        krw_balance17 = upbit.get_balance(krw_coin17)
                        # 코인 현재가 불러오기
                        price17 = pyupbit.get_current_price(krw_coin17)
                        # 보유코인 원화금액으로 계산하기
                        bp17 = price17 * krw_balance17

                        # 보유 및 매수 가능 출력.
                        print(f"[ 17. {krw_coin17} 매수완료. ]")
                        print(f"매수시간 : {now}  |  코인명 : {coin17}  |  현재가 = ￦{price17}  |  금일목표가 = ￦{target17}  |  보유수량 = {krw_balance17}  |  평가금액 = ￦{bp17}")
                        print(f"매수가능 - {op_mode17} - 불가")
                        print("")
                    else:
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode17 = False

                        print(f"[ 17. {krw_coin17} 잔고부족으로 매수안함. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin17}  |  현재매수가능 - {op_mode17} - 불가")
                        print("")

                elif krw17 <= buy_krw:   # 매수가능금액 krw17 가 매수평균가 buy_krw 보다 같거나 작을때
                    if krw17 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                        # 매수금액은 매수가능금액인 krw17 로
                        upbit.buy_market_order(krw_coin17, krw17 * 0.99)   # 매수가능금액에서 1%를 빼고

                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode17 = False

                        # 1초 딜레이
                        time.sleep(1)
                        # 보유수량 불러오기
                        krw_balance17 = upbit.get_balance(krw_coin17)
                        # 코인 현재가 불러오기
                        price17 = pyupbit.get_current_price(krw_coin17)
                        # 보유코인 원화금액으로 계산하기
                        bp17 = price17 * krw_balance17

                        # 보유 및 매수 가능 출력.
                        print(f"[ 17. {krw_coin17} 매수완료. ]")
                        print(f"매수시간 : {now}  |  코인명 : {coin17}  |  현재가 = ￦{price17}  |  금일목표가 = ￦{target17}  |  보유수량 = {krw_balance17}  |  평가금액 = ￦{bp17}")
                        print(f"매수가능 - {op_mode17} - 불가")
                        print("")
                    else:
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode17 = False

                        print(f"[ 17. {krw_coin17} 잔고부족으로 매수안함. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin17}  |  현재매수가능 - {op_mode17} - 불가")
                        print("")

        # 1초 딜레이.
        #time.sleep(1)
        ##### 17번 코인 매수 종료 #####
        #############################


        ##### 18번코인 매수 시도 #####
        if op_mode18 == True:    # 매수 가능(True)일 경우 - 매수시도
            # 코인 현재가 불러오기
            price18 = pyupbit.get_current_price(krw_coin18)
            # 코인 목표가 불러오기
            target18 = cal_target(krw_coin18)

            if price18 >= target18:   # 목표가보다 현재가가 높을때
                # 매수가능금액 불러오기
                krw18 = upbit.get_balance("KRW")

                if krw18 > buy_krw:    # 매수가능금액 krw18 이 매수설정금액 buy_krw 보다 많을 경우: 매수
                    if krw18 > 10100:     # 매수가능금액 krw18 이 10,100원 초과일 경우 : 매수
                        # 매수금액은 매수평균가 buy_krw 로
                        upbit.buy_market_order(krw_coin18, buy_krw * 0.99)   # 매수가능금액에서 1%를 빼고

                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode18 = False

                        # 1초 딜레이
                        time.sleep(1)
                        # 보유수량 불러오기
                        krw_balance18 = upbit.get_balance(krw_coin18)
                        # 코인 현재가 불러오기
                        price18 = pyupbit.get_current_price(krw_coin18)
                        # 보유코인 원화금액으로 계산하기
                        bp18 = price18 * krw_balance18

                        # 보유 및 매수 가능 출력.
                        print(f"[ 18. {krw_coin18} 매수완료. ]")
                        print(f"매수시간 : {now}  |  코인명 : {coin18}  |  현재가 = ￦{price18}  |  금일목표가 = ￦{target18}  |  보유수량 = {krw_balance18}  |  평가금액 = ￦{bp18}")
                        print(f"매수가능 - {op_mode18} - 불가")
                        print("")
                    else:
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode18 = False

                        print(f"[ 18. {krw_coin18} 잔고부족으로 매수안함. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin18}  |  현재매수가능 - {op_mode18} - 불가")
                        print("")

                elif krw18 <= buy_krw:   # 매수가능금액 krw18 가 매수평균가 buy_krw 보다 같거나 작을때
                    if krw18 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                        # 매수금액은 매수가능금액인 krw18 로
                        upbit.buy_market_order(krw_coin18, krw18 * 0.99)   # 매수가능금액에서 1%를 빼고

                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode18 = False

                        # 1초 딜레이
                        time.sleep(1)
                        # 보유수량 불러오기
                        krw_balance18 = upbit.get_balance(krw_coin18)
                        # 코인 현재가 불러오기
                        price18 = pyupbit.get_current_price(krw_coin18)
                        # 보유코인 원화금액으로 계산하기
                        bp18 = price18 * krw_balance18

                        # 보유 및 매수 가능 출력.
                        print(f"[ 18. {krw_coin18} 매수완료. ]")
                        print(f"매수시간 : {now}  |  코인명 : {coin18}  |  현재가 = ￦{price18}  |  금일목표가 = ￦{target18}  |  보유수량 = {krw_balance18}  |  평가금액 = ￦{bp18}")
                        print(f"매수가능 - {op_mode18} - 불가")
                        print("")
                    else:
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode18 = False

                        print(f"[ 18. {krw_coin18} 잔고부족으로 매수안함. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin18}  |  현재매수가능 - {op_mode18} - 불가")
                        print("")

        # 1초 딜레이.
        #time.sleep(1)
        ##### 18번 코인 매수 종료 #####
        #############################


        ##### 19번코인 매수 시도 #####
        if op_mode19 == True:    # 매수 가능(True)일 경우 - 매수시도
            # 코인 현재가 불러오기
            price19 = pyupbit.get_current_price(krw_coin19)
            # 코인 목표가 불러오기
            target19 = cal_target(krw_coin19)

            if price19 >= target19:   # 목표가보다 현재가가 높을때
                # 매수가능금액 불러오기
                krw19 = upbit.get_balance("KRW")

                if krw19 > buy_krw:    # 매수가능금액 krw19 이 매수설정금액 buy_krw 보다 많을 경우: 매수
                    if krw19 > 10100:     # 매수가능금액 krw19 이 10,100원 초과일 경우 : 매수
                        # 매수금액은 매수평균가 buy_krw 로
                        upbit.buy_market_order(krw_coin19, buy_krw * 0.99)   # 매수가능금액에서 1%를 빼고

                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode19 = False

                        # 1초 딜레이
                        time.sleep(1)
                        # 보유수량 불러오기
                        krw_balance19 = upbit.get_balance(krw_coin19)
                        # 코인 현재가 불러오기
                        price19 = pyupbit.get_current_price(krw_coin19)
                        # 보유코인 원화금액으로 계산하기
                        bp19 = price19 * krw_balance19

                        # 보유 및 매수 가능 출력.
                        print(f"[ 19. {krw_coin19} 매수완료. ]")
                        print(f"매수시간 : {now}  |  코인명 : {coin19}  |  현재가 = ￦{price19}  |  금일목표가 = ￦{target19}  |  보유수량 = {krw_balance19}  |  평가금액 = ￦{bp19}")
                        print(f"매수가능 - {op_mode19} - 불가")
                        print("")
                    else:
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode19 = False

                        print(f"[ 19. {krw_coin19} 잔고부족으로 매수안함. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin19}  |  현재매수가능 - {op_mode19} - 불가")
                        print("")

                elif krw19 <= buy_krw:   # 매수가능금액 krw19 가 매수평균가 buy_krw 보다 같거나 작을때
                    if krw19 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                        # 매수금액은 매수가능금액인 krw19 로
                        upbit.buy_market_order(krw_coin19, krw19 * 0.99)   # 매수가능금액에서 1%를 빼고

                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode19 = False

                        # 1초 딜레이
                        time.sleep(1)
                        # 보유수량 불러오기
                        krw_balance19 = upbit.get_balance(krw_coin19)
                        # 코인 현재가 불러오기
                        price19 = pyupbit.get_current_price(krw_coin19)
                        # 보유코인 원화금액으로 계산하기
                        bp19 = price19 * krw_balance19

                        # 보유 및 매수 가능 출력.
                        print(f"[ 19. {krw_coin19} 매수완료. ]")
                        print(f"매수시간 : {now}  |  코인명 : {coin19}  |  현재가 = ￦{price19}  |  금일목표가 = ￦{target19}  |  보유수량 = {krw_balance19}  |  평가금액 = ￦{bp19}")
                        print(f"매수가능 - {op_mode19} - 불가")
                        print("")
                    else:
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode19 = False

                        print(f"[ 19. {krw_coin19} 잔고부족으로 매수안함. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin19}  |  현재매수가능 - {op_mode19} - 불가")
                        print("")

        # 1초 딜레이.
        #time.sleep(1)
        ##### 19번 코인 매수 종료 #####
        #############################


        ##### 20번코인 매수 시도 #####
        if op_mode20 == True:    # 매수 가능(True)일 경우 - 매수시도
            # 코인 현재가 불러오기
            price20 = pyupbit.get_current_price(krw_coin20)
            # 코인 목표가 불러오기
            target20 = cal_target(krw_coin20)

            if price20 >= target20:   # 목표가보다 현재가가 높을때
                # 매수가능금액 불러오기
                krw20 = upbit.get_balance("KRW")

                if krw20 > buy_krw:    # 매수가능금액 krw20 이 매수설정금액 buy_krw 보다 많을 경우: 매수
                    if krw20 > 10100:     # 매수가능금액 krw20 이 10,100원 초과일 경우 : 매수
                        # 매수금액은 매수평균가 buy_krw 로
                        upbit.buy_market_order(krw_coin20, buy_krw * 0.99)   # 매수가능금액에서 1%를 빼고

                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode20 = False

                        # 1초 딜레이
                        time.sleep(1)
                        # 보유수량 불러오기
                        krw_balance20 = upbit.get_balance(krw_coin20)
                        # 코인 현재가 불러오기
                        price20 = pyupbit.get_current_price(krw_coin20)
                        # 보유코인 원화금액으로 계산하기
                        bp20 = price20 * krw_balance20

                        # 보유 및 매수 가능 출력.
                        print(f"[ 20. {krw_coin20} 매수완료. ]")
                        print(f"매수시간 : {now}  |  코인명 : {coin20}  |  현재가 = ￦{price20}  |  금일목표가 = ￦{target20}  |  보유수량 = {krw_balance20}  |  평가금액 = ￦{bp20}")
                        print(f"매수가능 - {op_mode20} - 불가")
                        print("")
                    else:
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode20 = False

                        print(f"[ 20. {krw_coin20} 잔고부족으로 매수안함. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin20}  |  현재매수가능 - {op_mode20} - 불가")
                        print("")

                elif krw20 <= buy_krw:   # 매수가능금액 krw20 가 매수평균가 buy_krw 보다 같거나 작을때
                    if krw20 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                        # 매수금액은 매수가능금액인 krw20 로
                        upbit.buy_market_order(krw_coin20, krw20 * 0.99)   # 매수가능금액에서 1%를 빼고

                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode20 = False

                        # 1초 딜레이
                        time.sleep(1)
                        # 보유수량 불러오기
                        krw_balance20 = upbit.get_balance(krw_coin20)
                        # 코인 현재가 불러오기
                        price20 = pyupbit.get_current_price(krw_coin20)
                        # 보유코인 원화금액으로 계산하기
                        bp20 = price20 * krw_balance20

                        # 보유 및 매수 가능 출력.
                        print(f"[ 20. {krw_coin20} 매수완료. ]")
                        print(f"매수시간 : {now}  |  코인명 : {coin20}  |  현재가 = ￦{price20}  |  금일목표가 = ￦{target20}  |  보유수량 = {krw_balance20}  |  평가금액 = ￦{bp20}")
                        print(f"매수가능 - {op_mode20} - 불가")
                        print("")
                    else:
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode20 = False

                        print(f"[ 20. {krw_coin20} 잔고부족으로 매수안함. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin20}  |  현재매수가능 - {op_mode20} - 불가")
                        print("")

        # 1초 딜레이.
        time.sleep(1)
        ##### 20번 코인 매수 종료 #####
        #############################


        ######################################################################################################################################################
        ######################################################################################################################################################
        ######################################################################################################################################################


        ##### 21번코인 매수 시도 #####
        if op_mode21 == True:    # 매수 가능(True)일 경우 - 매수시도
            # 코인 현재가 불러오기
            price21 = pyupbit.get_current_price(krw_coin21)
            # 코인 목표가 불러오기
            target21 = cal_target(krw_coin21)

            if price21 >= target21:   # 목표가보다 현재가가 높을때
                # 매수가능금액 불러오기
                krw21 = upbit.get_balance("KRW")

                if krw21 > buy_krw:    # 매수가능금액 krw21 이 매수설정금액 buy_krw 보다 많을 경우: 매수
                    if krw21 > 10100:     # 매수가능금액 krw21 이 10,100원 초과일 경우 : 매수
                        # 매수금액은 매수평균가 buy_krw 로
                        upbit.buy_market_order(krw_coin21, buy_krw * 0.99)   # 매수가능금액에서 1%를 빼고

                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode21 = False

                        # 1초 딜레이
                        time.sleep(1)
                        # 보유수량 불러오기
                        krw_balance21 = upbit.get_balance(krw_coin21)
                        # 코인 현재가 불러오기
                        price21 = pyupbit.get_current_price(krw_coin21)
                        # 보유코인 원화금액으로 계산하기
                        bp21 = price21 * krw_balance21

                        # 보유 및 매수 가능 출력.
                        print(f"[ 21. {krw_coin21} 매수완료. ]")
                        print(f"매수시간 : {now}  |  코인명 : {coin21}  |  현재가 = ￦{price21}  |  금일목표가 = ￦{target21}  |  보유수량 = {krw_balance21}  |  평가금액 = ￦{bp21}")
                        print(f"매수가능 - {op_mode21} - 불가")
                        print("")
                    else:
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode21 = False

                        print(f"[ 21. {krw_coin21} 잔고부족으로 매수안함. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin21}  |  현재매수가능 - {op_mode21} - 불가")
                        print("")

                elif krw21 <= buy_krw:   # 매수가능금액 krw21 가 매수평균가 buy_krw 보다 같거나 작을때
                    if krw21 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                        # 매수금액은 매수가능금액인 krw21 로
                        upbit.buy_market_order(krw_coin21, krw21 * 0.99)   # 매수가능금액에서 1%를 빼고

                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode21 = False

                        # 1초 딜레이
                        time.sleep(1)
                        # 보유수량 불러오기
                        krw_balance21 = upbit.get_balance(krw_coin21)
                        # 코인 현재가 불러오기
                        price21 = pyupbit.get_current_price(krw_coin21)
                        # 보유코인 원화금액으로 계산하기
                        bp21 = price21 * krw_balance21

                        # 보유 및 매수 가능 출력.
                        print(f"[ 21. {krw_coin21} 매수완료. ]")
                        print(f"매수시간 : {now}  |  코인명 : {coin21}  |  현재가 = ￦{price21}  |  금일목표가 = ￦{target21}  |  보유수량 = {krw_balance21}  |  평가금액 = ￦{bp21}")
                        print(f"매수가능 - {op_mode21} - 불가")
                        print("")
                    else:
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode21 = False

                        print(f"[ 21. {krw_coin21} 잔고부족으로 매수안함. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin21}  |  현재매수가능 - {op_mode21} - 불가")
                        print("")

        # 1초 딜레이.
        #time.sleep(1)
        ##### 21번 코인 매수 종료 #####
        #############################


        ##### 22번코인 매수 시도 #####
        if op_mode22 == True:    # 매수 가능(True)일 경우 - 매수시도
            # 코인 현재가 불러오기
            price22 = pyupbit.get_current_price(krw_coin22)
            # 코인 목표가 불러오기
            target22 = cal_target(krw_coin22)

            if price22 >= target22:   # 목표가보다 현재가가 높을때
                # 매수가능금액 불러오기
                krw22 = upbit.get_balance("KRW")

                if krw22 > buy_krw:    # 매수가능금액 krw22 이 매수설정금액 buy_krw 보다 많을 경우: 매수
                    if krw22 > 10100:     # 매수가능금액 krw22 이 10,100원 초과일 경우 : 매수
                        # 매수금액은 매수평균가 buy_krw 로
                        upbit.buy_market_order(krw_coin22, buy_krw * 0.99)   # 매수가능금액에서 1%를 빼고

                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode22 = False

                        # 1초 딜레이
                        time.sleep(1)
                        # 보유수량 불러오기
                        krw_balance22 = upbit.get_balance(krw_coin22)
                        # 코인 현재가 불러오기
                        price22 = pyupbit.get_current_price(krw_coin22)
                        # 보유코인 원화금액으로 계산하기
                        bp22 = price22 * krw_balance22

                        # 보유 및 매수 가능 출력.
                        print(f"[ 22. {krw_coin22} 매수완료. ]")
                        print(f"매수시간 : {now}  |  코인명 : {coin22}  |  현재가 = ￦{price22}  |  금일목표가 = ￦{target22}  |  보유수량 = {krw_balance22}  |  평가금액 = ￦{bp22}")
                        print(f"매수가능 - {op_mode22} - 불가")
                        print("")
                    else:
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode22 = False

                        print(f"[ 22. {krw_coin22} 잔고부족으로 매수안함. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin22}  |  현재매수가능 - {op_mode22} - 불가")
                        print("")

                elif krw22 <= buy_krw:   # 매수가능금액 krw22 가 매수평균가 buy_krw 보다 같거나 작을때
                    if krw22 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                        # 매수금액은 매수가능금액인 krw22 로
                        upbit.buy_market_order(krw_coin22, krw22 * 0.99)   # 매수가능금액에서 1%를 빼고

                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode22 = False

                        # 1초 딜레이
                        time.sleep(1)
                        # 보유수량 불러오기
                        krw_balance22 = upbit.get_balance(krw_coin22)
                        # 코인 현재가 불러오기
                        price22 = pyupbit.get_current_price(krw_coin22)
                        # 보유코인 원화금액으로 계산하기
                        bp22 = price22 * krw_balance22

                        # 보유 및 매수 가능 출력.
                        print(f"[ 22. {krw_coin22} 매수완료. ]")
                        print(f"매수시간 : {now}  |  코인명 : {coin22}  |  현재가 = ￦{price22}  |  금일목표가 = ￦{target22}  |  보유수량 = {krw_balance22}  |  평가금액 = ￦{bp22}")
                        print(f"매수가능 - {op_mode22} - 불가")
                        print("")
                    else:
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode22 = False

                        print(f"[ 22. {krw_coin22} 잔고부족으로 매수안함. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin22}  |  현재매수가능 - {op_mode22} - 불가")
                        print("")

        # 1초 딜레이.
        #time.sleep(1)
        ##### 22번 코인 매수 종료 #####
        #############################


        ##### 23번코인 매수 시도 #####
        if op_mode23 == True:    # 매수 가능(True)일 경우 - 매수시도
            # 코인 현재가 불러오기
            price23 = pyupbit.get_current_price(krw_coin23)
            # 코인 목표가 불러오기
            target23 = cal_target(krw_coin23)

            if price23 >= target23:   # 목표가보다 현재가가 높을때
                # 매수가능금액 불러오기
                krw23 = upbit.get_balance("KRW")

                if krw23 > buy_krw:    # 매수가능금액 krw23 이 매수설정금액 buy_krw 보다 많을 경우: 매수
                    if krw23 > 10100:     # 매수가능금액 krw23 이 10,100원 초과일 경우 : 매수
                        # 매수금액은 매수평균가 buy_krw 로
                        upbit.buy_market_order(krw_coin23, buy_krw * 0.99)   # 매수가능금액에서 1%를 빼고

                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode23 = False

                        # 1초 딜레이
                        time.sleep(1)
                        # 보유수량 불러오기
                        krw_balance23 = upbit.get_balance(krw_coin23)
                        # 코인 현재가 불러오기
                        price23 = pyupbit.get_current_price(krw_coin23)
                        # 보유코인 원화금액으로 계산하기
                        bp23 = price23 * krw_balance23

                        # 보유 및 매수 가능 출력.
                        print(f"[ 23. {krw_coin23} 매수완료. ]")
                        print(f"매수시간 : {now}  |  코인명 : {coin23}  |  현재가 = ￦{price23}  |  금일목표가 = ￦{target23}  |  보유수량 = {krw_balance23}  |  평가금액 = ￦{bp23}")
                        print(f"매수가능 - {op_mode23} - 불가")
                        print("")
                    else:
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode23 = False

                        print(f"[ 23. {krw_coin23} 잔고부족으로 매수안함. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin23}  |  현재매수가능 - {op_mode23} - 불가")
                        print("")

                elif krw23 <= buy_krw:   # 매수가능금액 krw23 가 매수평균가 buy_krw 보다 같거나 작을때
                    if krw23 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                        # 매수금액은 매수가능금액인 krw23 로
                        upbit.buy_market_order(krw_coin23, krw23 * 0.99)   # 매수가능금액에서 1%를 빼고

                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode23 = False

                        # 1초 딜레이
                        time.sleep(1)
                        # 보유수량 불러오기
                        krw_balance23 = upbit.get_balance(krw_coin23)
                        # 코인 현재가 불러오기
                        price23 = pyupbit.get_current_price(krw_coin23)
                        # 보유코인 원화금액으로 계산하기
                        bp23 = price23 * krw_balance23

                        # 보유 및 매수 가능 출력.
                        print(f"[ 23. {krw_coin23} 매수완료. ]")
                        print(f"매수시간 : {now}  |  코인명 : {coin23}  |  현재가 = ￦{price23}  |  금일목표가 = ￦{target23}  |  보유수량 = {krw_balance23}  |  평가금액 = ￦{bp23}")
                        print(f"매수가능 - {op_mode23} - 불가")
                        print("")
                    else:
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode23 = False

                        print(f"[ 23. {krw_coin23} 잔고부족으로 매수안함. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin23}  |  현재매수가능 - {op_mode23} - 불가")
                        print("")

        # 1초 딜레이.
        #time.sleep(1)
        ##### 23번 코인 매수 종료 #####
        #############################


        ##### 24번코인 매수 시도 #####
        if op_mode24 == True:    # 매수 가능(True)일 경우 - 매수시도
            # 코인 현재가 불러오기
            price24 = pyupbit.get_current_price(krw_coin24)
            # 코인 목표가 불러오기
            target24 = cal_target(krw_coin24)

            if price24 >= target24:   # 목표가보다 현재가가 높을때
                # 매수가능금액 불러오기
                krw24 = upbit.get_balance("KRW")

                if krw24 > buy_krw:    # 매수가능금액 krw24 이 매수설정금액 buy_krw 보다 많을 경우: 매수
                    if krw24 > 10100:     # 매수가능금액 krw24 이 10,100원 초과일 경우 : 매수
                        # 매수금액은 매수평균가 buy_krw 로
                        upbit.buy_market_order(krw_coin24, buy_krw * 0.99)   # 매수가능금액에서 1%를 빼고

                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode24 = False

                        # 1초 딜레이
                        time.sleep(1)
                        # 보유수량 불러오기
                        krw_balance24 = upbit.get_balance(krw_coin24)
                        # 코인 현재가 불러오기
                        price24 = pyupbit.get_current_price(krw_coin24)
                        # 보유코인 원화금액으로 계산하기
                        bp24 = price24 * krw_balance24

                        # 보유 및 매수 가능 출력.
                        print(f"[ 24. {krw_coin24} 매수완료. ]")
                        print(f"매수시간 : {now}  |  코인명 : {coin24}  |  현재가 = ￦{price24}  |  금일목표가 = ￦{target24}  |  보유수량 = {krw_balance24}  |  평가금액 = ￦{bp24}")
                        print(f"매수가능 - {op_mode24} - 불가")
                        print("")
                    else:
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode24 = False

                        print(f"[ 24. {krw_coin24} 잔고부족으로 매수안함. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin24}  |  현재매수가능 - {op_mode24} - 불가")
                        print("")

                elif krw24 <= buy_krw:   # 매수가능금액 krw24 가 매수평균가 buy_krw 보다 같거나 작을때
                    if krw24 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                        # 매수금액은 매수가능금액인 krw24 로
                        upbit.buy_market_order(krw_coin24, krw24 * 0.99)   # 매수가능금액에서 1%를 빼고

                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode24 = False

                        # 1초 딜레이
                        time.sleep(1)
                        # 보유수량 불러오기
                        krw_balance24 = upbit.get_balance(krw_coin24)
                        # 코인 현재가 불러오기
                        price24 = pyupbit.get_current_price(krw_coin24)
                        # 보유코인 원화금액으로 계산하기
                        bp24 = price24 * krw_balance24

                        # 보유 및 매수 가능 출력.
                        print(f"[ 24. {krw_coin24} 매수완료. ]")
                        print(f"매수시간 : {now}  |  코인명 : {coin24}  |  현재가 = ￦{price24}  |  금일목표가 = ￦{target24}  |  보유수량 = {krw_balance24}  |  평가금액 = ￦{bp24}")
                        print(f"매수가능 - {op_mode24} - 불가")
                        print("")
                    else:
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode24 = False

                        print(f"[ 24. {krw_coin24} 잔고부족으로 매수안함. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin24}  |  현재매수가능 - {op_mode24} - 불가")
                        print("")

        # 1초 딜레이.
        #time.sleep(1)
        ##### 24번 코인 매수 종료 #####
        #############################


        ##### 25번코인 매수 시도 #####
        if op_mode25 == True:    # 매수 가능(True)일 경우 - 매수시도
            # 코인 현재가 불러오기
            price25 = pyupbit.get_current_price(krw_coin25)
            # 코인 목표가 불러오기
            target25 = cal_target(krw_coin25)

            if price25 >= target25:   # 목표가보다 현재가가 높을때
                # 매수가능금액 불러오기
                krw25 = upbit.get_balance("KRW")

                if krw25 > buy_krw:    # 매수가능금액 krw25 이 매수설정금액 buy_krw 보다 많을 경우: 매수
                    if krw25 > 10100:     # 매수가능금액 krw25 이 10,100원 초과일 경우 : 매수
                        # 매수금액은 매수평균가 buy_krw 로
                        upbit.buy_market_order(krw_coin25, buy_krw * 0.99)   # 매수가능금액에서 1%를 빼고

                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode25 = False

                        # 1초 딜레이
                        time.sleep(1)
                        # 보유수량 불러오기
                        krw_balance25 = upbit.get_balance(krw_coin25)
                        # 코인 현재가 불러오기
                        price25 = pyupbit.get_current_price(krw_coin25)
                        # 보유코인 원화금액으로 계산하기
                        bp25 = price25 * krw_balance25

                        # 보유 및 매수 가능 출력.
                        print(f"[ 25. {krw_coin25} 매수완료. ]")
                        print(f"매수시간 : {now}  |  코인명 : {coin25}  |  현재가 = ￦{price25}  |  금일목표가 = ￦{target25}  |  보유수량 = {krw_balance25}  |  평가금액 = ￦{bp25}")
                        print(f"매수가능 - {op_mode25} - 불가")
                        print("")
                    else:
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode25 = False

                        print(f"[ 25. {krw_coin25} 잔고부족으로 매수안함. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin25}  |  현재매수가능 - {op_mode25} - 불가")
                        print("")

                elif krw25 <= buy_krw:   # 매수가능금액 krw25 가 매수평균가 buy_krw 보다 같거나 작을때
                    if krw25 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                        # 매수금액은 매수가능금액인 krw25 로
                        upbit.buy_market_order(krw_coin25, krw25 * 0.99)   # 매수가능금액에서 1%를 빼고

                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode25 = False

                        # 1초 딜레이
                        time.sleep(1)
                        # 보유수량 불러오기
                        krw_balance25 = upbit.get_balance(krw_coin25)
                        # 코인 현재가 불러오기
                        price25 = pyupbit.get_current_price(krw_coin25)
                        # 보유코인 원화금액으로 계산하기
                        bp25 = price25 * krw_balance25

                        # 보유 및 매수 가능 출력.
                        print(f"[ 25. {krw_coin25} 매수완료. ]")
                        print(f"매수시간 : {now}  |  코인명 : {coin25}  |  현재가 = ￦{price25}  |  금일목표가 = ￦{target25}  |  보유수량 = {krw_balance25}  |  평가금액 = ￦{bp25}")
                        print(f"매수가능 - {op_mode25} - 불가")
                        print("")
                    else:
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode25 = False

                        print(f"[ 25. {krw_coin25} 잔고부족으로 매수안함. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin25}  |  현재매수가능 - {op_mode25} - 불가")
                        print("")

        # 1초 딜레이.
        time.sleep(1)
        ##### 25번 코인 매수 종료 #####
        #############################


        ##### 26번코인 매수 시도 #####
        if op_mode26 == True:    # 매수 가능(True)일 경우 - 매수시도
            # 코인 현재가 불러오기
            price26 = pyupbit.get_current_price(krw_coin26)
            # 코인 목표가 불러오기
            target26 = cal_target(krw_coin26)

            if price26 >= target26:   # 목표가보다 현재가가 높을때
                # 매수가능금액 불러오기
                krw26 = upbit.get_balance("KRW")

                if krw26 > buy_krw:    # 매수가능금액 krw26 이 매수설정금액 buy_krw 보다 많을 경우: 매수
                    if krw26 > 10100:     # 매수가능금액 krw26 이 10,100원 초과일 경우 : 매수
                        # 매수금액은 매수평균가 buy_krw 로
                        upbit.buy_market_order(krw_coin26, buy_krw * 0.99)   # 매수가능금액에서 1%를 빼고

                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode26 = False

                        # 1초 딜레이
                        time.sleep(1)
                        # 보유수량 불러오기
                        krw_balance26 = upbit.get_balance(krw_coin26)
                        # 코인 현재가 불러오기
                        price26 = pyupbit.get_current_price(krw_coin26)
                        # 보유코인 원화금액으로 계산하기
                        bp26 = price26 * krw_balance26

                        # 보유 및 매수 가능 출력.
                        print(f"[ 26. {krw_coin26} 매수완료. ]")
                        print(f"매수시간 : {now}  |  코인명 : {coin26}  |  현재가 = ￦{price26}  |  금일목표가 = ￦{target26}  |  보유수량 = {krw_balance26}  |  평가금액 = ￦{bp26}")
                        print(f"매수가능 - {op_mode26} - 불가")
                        print("")
                    else:
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode26 = False

                        print(f"[ 26. {krw_coin26} 잔고부족으로 매수안함. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin26}  |  현재매수가능 - {op_mode26} - 불가")
                        print("")

                elif krw26 <= buy_krw:   # 매수가능금액 krw26 가 매수평균가 buy_krw 보다 같거나 작을때
                    if krw26 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                        # 매수금액은 매수가능금액인 krw26 로
                        upbit.buy_market_order(krw_coin26, krw26 * 0.99)   # 매수가능금액에서 1%를 빼고

                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode26 = False

                        # 1초 딜레이
                        time.sleep(1)
                        # 보유수량 불러오기
                        krw_balance26 = upbit.get_balance(krw_coin26)
                        # 코인 현재가 불러오기
                        price26 = pyupbit.get_current_price(krw_coin26)
                        # 보유코인 원화금액으로 계산하기
                        bp26 = price26 * krw_balance26

                        # 보유 및 매수 가능 출력.
                        print(f"[ 26. {krw_coin26} 매수완료. ]")
                        print(f"매수시간 : {now}  |  코인명 : {coin26}  |  현재가 = ￦{price26}  |  금일목표가 = ￦{target26}  |  보유수량 = {krw_balance26}  |  평가금액 = ￦{bp26}")
                        print(f"매수가능 - {op_mode26} - 불가")
                        print("")
                    else:
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode26 = False

                        print(f"[ 26. {krw_coin26} 잔고부족으로 매수안함. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin26}  |  현재매수가능 - {op_mode26} - 불가")
                        print("")

        # 1초 딜레이.
        #time.sleep(1)
        ##### 26번 코인 매수 종료 #####
        #############################


        ##### 27번코인 매수 시도 #####
        if op_mode27 == True:    # 매수 가능(True)일 경우 - 매수시도
            # 코인 현재가 불러오기
            price27 = pyupbit.get_current_price(krw_coin27)
            # 코인 목표가 불러오기
            target27 = cal_target(krw_coin27)

            if price27 >= target27:   # 목표가보다 현재가가 높을때
                # 매수가능금액 불러오기
                krw27 = upbit.get_balance("KRW")

                if krw27 > buy_krw:    # 매수가능금액 krw27 이 매수설정금액 buy_krw 보다 많을 경우: 매수
                    if krw27 > 10100:     # 매수가능금액 krw27 이 10,100원 초과일 경우 : 매수
                        # 매수금액은 매수평균가 buy_krw 로
                        upbit.buy_market_order(krw_coin27, buy_krw * 0.99)   # 매수가능금액에서 1%를 빼고

                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode27 = False

                        # 1초 딜레이
                        time.sleep(1)
                        # 보유수량 불러오기
                        krw_balance27 = upbit.get_balance(krw_coin27)
                        # 코인 현재가 불러오기
                        price27 = pyupbit.get_current_price(krw_coin27)
                        # 보유코인 원화금액으로 계산하기
                        bp27 = price27 * krw_balance27

                        # 보유 및 매수 가능 출력.
                        print(f"[ 27. {krw_coin27} 매수완료. ]")
                        print(f"매수시간 : {now}  |  코인명 : {coin27}  |  현재가 = ￦{price27}  |  금일목표가 = ￦{target27}  |  보유수량 = {krw_balance27}  |  평가금액 = ￦{bp27}")
                        print(f"매수가능 - {op_mode27} - 불가")
                        print("")
                    else:
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode27 = False

                        print(f"[ 27. {krw_coin27} 잔고부족으로 매수안함. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin27}  |  현재매수가능 - {op_mode27} - 불가")
                        print("")

                elif krw27 <= buy_krw:   # 매수가능금액 krw27 가 매수평균가 buy_krw 보다 같거나 작을때
                    if krw27 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                        # 매수금액은 매수가능금액인 krw27 로
                        upbit.buy_market_order(krw_coin27, krw27 * 0.99)   # 매수가능금액에서 1%를 빼고

                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode27 = False

                        # 1초 딜레이
                        time.sleep(1)
                        # 보유수량 불러오기
                        krw_balance27 = upbit.get_balance(krw_coin27)
                        # 코인 현재가 불러오기
                        price27 = pyupbit.get_current_price(krw_coin27)
                        # 보유코인 원화금액으로 계산하기
                        bp27 = price27 * krw_balance27

                        # 보유 및 매수 가능 출력.
                        print(f"[ 27. {krw_coin27} 매수완료. ]")
                        print(f"매수시간 : {now}  |  코인명 : {coin27}  |  현재가 = ￦{price27}  |  금일목표가 = ￦{target27}  |  보유수량 = {krw_balance27}  |  평가금액 = ￦{bp27}")
                        print(f"매수가능 - {op_mode27} - 불가")
                        print("")
                    else:
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode27 = False

                        print(f"[ 27. {krw_coin27} 잔고부족으로 매수안함. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin27}  |  현재매수가능 - {op_mode27} - 불가")
                        print("")

        # 1초 딜레이.
        #time.sleep(1)
        ##### 27번 코인 매수 종료 #####
        #############################


        ##### 28번코인 매수 시도 #####
        if op_mode28 == True:    # 매수 가능(True)일 경우 - 매수시도
            # 코인 현재가 불러오기
            price28 = pyupbit.get_current_price(krw_coin28)
            # 코인 목표가 불러오기
            target28 = cal_target(krw_coin28)

            if price28 >= target28:   # 목표가보다 현재가가 높을때
                # 매수가능금액 불러오기
                krw28 = upbit.get_balance("KRW")

                if krw28 > buy_krw:    # 매수가능금액 krw28 이 매수설정금액 buy_krw 보다 많을 경우: 매수
                    if krw28 > 10100:     # 매수가능금액 krw28 이 10,100원 초과일 경우 : 매수
                        # 매수금액은 매수평균가 buy_krw 로
                        upbit.buy_market_order(krw_coin28, buy_krw * 0.99)   # 매수가능금액에서 1%를 빼고

                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode28 = False

                        # 1초 딜레이
                        time.sleep(1)
                        # 보유수량 불러오기
                        krw_balance28 = upbit.get_balance(krw_coin28)
                        # 코인 현재가 불러오기
                        price28 = pyupbit.get_current_price(krw_coin28)
                        # 보유코인 원화금액으로 계산하기
                        bp28 = price28 * krw_balance28

                        # 보유 및 매수 가능 출력.
                        print(f"[ 28. {krw_coin28} 매수완료. ]")
                        print(f"매수시간 : {now}  |  코인명 : {coin28}  |  현재가 = ￦{price28}  |  금일목표가 = ￦{target28}  |  보유수량 = {krw_balance28}  |  평가금액 = ￦{bp28}")
                        print(f"매수가능 - {op_mode28} - 불가")
                        print("")
                    else:
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode28 = False

                        print(f"[ 28. {krw_coin28} 잔고부족으로 매수안함. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin28}  |  현재매수가능 - {op_mode28} - 불가")
                        print("")

                elif krw28 <= buy_krw:   # 매수가능금액 krw28 가 매수평균가 buy_krw 보다 같거나 작을때
                    if krw28 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                        # 매수금액은 매수가능금액인 krw28 로
                        upbit.buy_market_order(krw_coin28, krw28 * 0.99)   # 매수가능금액에서 1%를 빼고

                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode28 = False

                        # 1초 딜레이
                        time.sleep(1)
                        # 보유수량 불러오기
                        krw_balance28 = upbit.get_balance(krw_coin28)
                        # 코인 현재가 불러오기
                        price28 = pyupbit.get_current_price(krw_coin28)
                        # 보유코인 원화금액으로 계산하기
                        bp28 = price28 * krw_balance28

                        # 보유 및 매수 가능 출력.
                        print(f"[ 28. {krw_coin28} 매수완료. ]")
                        print(f"매수시간 : {now}  |  코인명 : {coin28}  |  현재가 = ￦{price28}  |  금일목표가 = ￦{target28}  |  보유수량 = {krw_balance28}  |  평가금액 = ￦{bp28}")
                        print(f"매수가능 - {op_mode28} - 불가")
                        print("")
                    else:
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode28 = False

                        print(f"[ 28. {krw_coin28} 잔고부족으로 매수안함. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin28}  |  현재매수가능 - {op_mode28} - 불가")
                        print("")

        # 1초 딜레이.
        #time.sleep(1)
        ##### 28번 코인 매수 종료 #####
        #############################


        ##### 29번코인 매수 시도 #####
        if op_mode29 == True:    # 매수 가능(True)일 경우 - 매수시도
            # 코인 현재가 불러오기
            price29 = pyupbit.get_current_price(krw_coin29)
            # 코인 목표가 불러오기
            target29 = cal_target(krw_coin29)

            if price29 >= target29:   # 목표가보다 현재가가 높을때
                # 매수가능금액 불러오기
                krw29 = upbit.get_balance("KRW")

                if krw29 > buy_krw:    # 매수가능금액 krw29 이 매수설정금액 buy_krw 보다 많을 경우: 매수
                    if krw29 > 10100:     # 매수가능금액 krw29 이 10,100원 초과일 경우 : 매수
                        # 매수금액은 매수평균가 buy_krw 로
                        upbit.buy_market_order(krw_coin29, buy_krw * 0.99)   # 매수가능금액에서 1%를 빼고

                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode29 = False

                        # 1초 딜레이
                        time.sleep(1)
                        # 보유수량 불러오기
                        krw_balance29 = upbit.get_balance(krw_coin29)
                        # 코인 현재가 불러오기
                        price29 = pyupbit.get_current_price(krw_coin29)
                        # 보유코인 원화금액으로 계산하기
                        bp29 = price29 * krw_balance29

                        # 보유 및 매수 가능 출력.
                        print(f"[ 29. {krw_coin29} 매수완료. ]")
                        print(f"매수시간 : {now}  |  코인명 : {coin29}  |  현재가 = ￦{price29}  |  금일목표가 = ￦{target29}  |  보유수량 = {krw_balance29}  |  평가금액 = ￦{bp29}")
                        print(f"매수가능 - {op_mode29} - 불가")
                        print("")
                    else:
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode29 = False

                        print(f"[ 29. {krw_coin29} 잔고부족으로 매수안함. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin29}  |  현재매수가능 - {op_mode29} - 불가")
                        print("")

                elif krw29 <= buy_krw:   # 매수가능금액 krw29 가 매수평균가 buy_krw 보다 같거나 작을때
                    if krw29 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                        # 매수금액은 매수가능금액인 krw29 로
                        upbit.buy_market_order(krw_coin29, krw29 * 0.99)   # 매수가능금액에서 1%를 빼고

                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode29 = False

                        # 1초 딜레이
                        time.sleep(1)
                        # 보유수량 불러오기
                        krw_balance29 = upbit.get_balance(krw_coin29)
                        # 코인 현재가 불러오기
                        price29 = pyupbit.get_current_price(krw_coin29)
                        # 보유코인 원화금액으로 계산하기
                        bp29 = price29 * krw_balance29

                        # 보유 및 매수 가능 출력.
                        print(f"[ 29. {krw_coin29} 매수완료. ]")
                        print(f"매수시간 : {now}  |  코인명 : {coin29}  |  현재가 = ￦{price29}  |  금일목표가 = ￦{target29}  |  보유수량 = {krw_balance29}  |  평가금액 = ￦{bp29}")
                        print(f"매수가능 - {op_mode29} - 불가")
                        print("")
                    else:
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode29 = False

                        print(f"[ 29. {krw_coin29} 잔고부족으로 매수안함. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin29}  |  현재매수가능 - {op_mode29} - 불가")
                        print("")

        # 1초 딜레이.
        #time.sleep(1)
        ##### 29번 코인 매수 종료 #####
        #############################


        ##### 30번코인 매수 시도 #####
        if op_mode30 == True:    # 매수 가능(True)일 경우 - 매수시도
            # 코인 현재가 불러오기
            price30 = pyupbit.get_current_price(krw_coin30)
            # 코인 목표가 불러오기
            target30 = cal_target(krw_coin30)

            if price30 >= target30:   # 목표가보다 현재가가 높을때
                # 매수가능금액 불러오기
                krw30 = upbit.get_balance("KRW")

                if krw30 > buy_krw:    # 매수가능금액 krw30 이 매수설정금액 buy_krw 보다 많을 경우: 매수
                    if krw30 > 10100:     # 매수가능금액 krw30 이 10,100원 초과일 경우 : 매수
                        # 매수금액은 매수평균가 buy_krw 로
                        upbit.buy_market_order(krw_coin30, buy_krw * 0.99)   # 매수가능금액에서 1%를 빼고

                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode30 = False

                        # 1초 딜레이
                        time.sleep(1)
                        # 보유수량 불러오기
                        krw_balance30 = upbit.get_balance(krw_coin30)
                        # 코인 현재가 불러오기
                        price30 = pyupbit.get_current_price(krw_coin30)
                        # 보유코인 원화금액으로 계산하기
                        bp30 = price30 * krw_balance30

                        # 보유 및 매수 가능 출력.
                        print(f"[ 30. {krw_coin30} 매수완료. ]")
                        print(f"매수시간 : {now}  |  코인명 : {coin30}  |  현재가 = ￦{price30}  |  금일목표가 = ￦{target30}  |  보유수량 = {krw_balance30}  |  평가금액 = ￦{bp30}")
                        print(f"매수가능 - {op_mode20} - 불가")
                        print("")
                    else:
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode30 = False

                        print(f"[ 30. {krw_coin30} 잔고부족으로 매수안함. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin30}  |  현재매수가능 - {op_mode30} - 불가")
                        print("")

                elif krw30 <= buy_krw:   # 매수가능금액 krw30 가 매수평균가 buy_krw 보다 같거나 작을때
                    if krw30 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                        # 매수금액은 매수가능금액인 krw30 로
                        upbit.buy_market_order(krw_coin30, krw30 * 0.99)   # 매수가능금액에서 1%를 빼고

                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode30 = False

                        # 1초 딜레이
                        time.sleep(1)
                        # 보유수량 불러오기
                        krw_balance30 = upbit.get_balance(krw_coin30)
                        # 코인 현재가 불러오기
                        price30 = pyupbit.get_current_price(krw_coin30)
                        # 보유코인 원화금액으로 계산하기
                        bp30 = price30 * krw_balance30

                        # 보유 및 매수 가능 출력.
                        print(f"[ 30. {krw_coin30} 매수완료. ]")
                        print(f"매수시간 : {now}  |  코인명 : {coin30}  |  현재가 = ￦{price30}  |  금일목표가 = ￦{target30}  |  보유수량 = {krw_balance30}  |  평가금액 = ￦{bp30}")
                        print(f"매수가능 - {op_mode20} - 불가")
                        print("")
                    else:
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode30 = False

                        print(f"[ 30. {krw_coin30} 잔고부족으로 매수안함. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin30}  |  현재매수가능 - {op_mode30} - 불가")
                        print("")

        # 1초 딜레이.
        time.sleep(1)
        ##### 30번 코인 매수 종료 #####
        #############################


        ######################################################################################################################################################
        ######################################################################################################################################################
        ######################################################################################################################################################


        ##### 31번코인 매수 시도 #####
        if op_mode31 == True:    # 매수 가능(True)일 경우 - 매수시도
            # 코인 현재가 불러오기
            price31 = pyupbit.get_current_price(krw_coin31)
            # 코인 목표가 불러오기
            target31 = cal_target(krw_coin31)

            if price31 >= target31:   # 목표가보다 현재가가 높을때
                # 매수가능금액 불러오기
                krw31 = upbit.get_balance("KRW")

                if krw31 > buy_krw:    # 매수가능금액 krw31 이 매수설정금액 buy_krw 보다 많을 경우: 매수
                    if krw31 > 10100:     # 매수가능금액 krw31 이 10,100원 초과일 경우 : 매수
                        # 매수금액은 매수평균가 buy_krw 로
                        upbit.buy_market_order(krw_coin31, buy_krw * 0.99)   # 매수가능금액에서 1%를 빼고

                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode31 = False

                        # 1초 딜레이
                        time.sleep(1)
                        # 보유수량 불러오기
                        krw_balance31 = upbit.get_balance(krw_coin31)
                        # 코인 현재가 불러오기
                        price31 = pyupbit.get_current_price(krw_coin31)
                        # 보유코인 원화금액으로 계산하기
                        bp31 = price31 * krw_balance31

                        # 보유 및 매수 가능 출력.
                        print(f"[ 31. {krw_coin31} 매수완료. ]")
                        print(f"매수시간 : {now}  |  코인명 : {coin31}  |  현재가 = ￦{price31}  |  금일목표가 = ￦{target31}  |  보유수량 = {krw_balance31}  |  평가금액 = ￦{bp31}")
                        print(f"매수가능 - {op_mode31} - 불가")
                        print("")
                    else:
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode31 = False

                        print(f"[ 31. {krw_coin31} 잔고부족으로 매수안함. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin31}  |  현재매수가능 - {op_mode31} - 불가")
                        print("")

                elif krw31 <= buy_krw:   # 매수가능금액 krw31 가 매수평균가 buy_krw 보다 같거나 작을때
                    if krw31 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                        # 매수금액은 매수가능금액인 krw21 로
                        upbit.buy_market_order(krw_coin31, krw31 * 0.99)   # 매수가능금액에서 1%를 빼고

                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode31 = False

                        # 1초 딜레이
                        time.sleep(1)
                        # 보유수량 불러오기
                        krw_balance31 = upbit.get_balance(krw_coin31)
                        # 코인 현재가 불러오기
                        price31 = pyupbit.get_current_price(krw_coin31)
                        # 보유코인 원화금액으로 계산하기
                        bp31 = price31 * krw_balance31

                        # 보유 및 매수 가능 출력.
                        print(f"[ 31. {krw_coin31} 매수완료. ]")
                        print(f"매수시간 : {now}  |  코인명 : {coin31}  |  현재가 = ￦{price31}  |  금일목표가 = ￦{target31}  |  보유수량 = {krw_balance31}  |  평가금액 = ￦{bp31}")
                        print(f"매수가능 - {op_mode31} - 불가")
                        print("")
                    else:
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode31 = False

                        print(f"[ 31. {krw_coin31} 잔고부족으로 매수안함. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin31}  |  현재매수가능 - {op_mode31} - 불가")
                        print("")

        # 1초 딜레이.
        #time.sleep(1)
        ##### 31번 코인 매수 종료 #####
        #############################


        ##### 32번코인 매수 시도 #####
        if op_mode32 == True:    # 매수 가능(True)일 경우 - 매수시도
            # 코인 현재가 불러오기
            price32 = pyupbit.get_current_price(krw_coin32)
            # 코인 목표가 불러오기
            target32 = cal_target(krw_coin32)

            if price32 >= target32:   # 목표가보다 현재가가 높을때
                # 매수가능금액 불러오기
                krw32 = upbit.get_balance("KRW")

                if krw32 > buy_krw:    # 매수가능금액 krw32 이 매수설정금액 buy_krw 보다 많을 경우: 매수
                    if krw32 > 10100:     # 매수가능금액 krw32 이 10,100원 초과일 경우 : 매수
                        # 매수금액은 매수평균가 buy_krw 로
                        upbit.buy_market_order(krw_coin32, buy_krw * 0.99)   # 매수가능금액에서 1%를 빼고

                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode32 = False

                        # 1초 딜레이
                        time.sleep(1)
                        # 보유수량 불러오기
                        krw_balance32 = upbit.get_balance(krw_coin32)
                        # 코인 현재가 불러오기
                        price32 = pyupbit.get_current_price(krw_coin32)
                        # 보유코인 원화금액으로 계산하기
                        bp32 = price32 * krw_balance32

                        # 보유 및 매수 가능 출력.
                        print(f"[ 32. {krw_coin32} 매수완료. ]")
                        print(f"매수시간 : {now}  |  코인명 : {coin32}  |  현재가 = ￦{price32}  |  금일목표가 = ￦{target32}  |  보유수량 = {krw_balance32}  |  평가금액 = ￦{bp32}")
                        print(f"매수가능 - {op_mode32} - 불가")
                        print("")
                    else:
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode32 = False

                        print(f"[ 32. {krw_coin32} 잔고부족으로 매수안함. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin32}  |  현재매수가능 - {op_mode32} - 불가")
                        print("")

                elif krw32 <= buy_krw:   # 매수가능금액 krw32 가 매수평균가 buy_krw 보다 같거나 작을때
                    if krw32 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                        # 매수금액은 매수가능금액인 krw32 로
                        upbit.buy_market_order(krw_coin32, krw32 * 0.99)   # 매수가능금액에서 1%를 빼고

                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode32 = False

                        # 1초 딜레이
                        time.sleep(1)
                        # 보유수량 불러오기
                        krw_balance32 = upbit.get_balance(krw_coin32)
                        # 코인 현재가 불러오기
                        price32 = pyupbit.get_current_price(krw_coin32)
                        # 보유코인 원화금액으로 계산하기
                        bp32 = price32 * krw_balance32

                        # 보유 및 매수 가능 출력.
                        print(f"[ 32. {krw_coin32} 매수완료. ]")
                        print(f"매수시간 : {now}  |  코인명 : {coin32}  |  현재가 = ￦{price32}  |  금일목표가 = ￦{target32}  |  보유수량 = {krw_balance32}  |  평가금액 = ￦{bp32}")
                        print(f"매수가능 - {op_mode32} - 불가")
                        print("")
                    else:
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode32 = False

                        print(f"[ 32. {krw_coin32} 잔고부족으로 매수안함. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin32}  |  현재매수가능 - {op_mode32} - 불가")
                        print("")

        # 1초 딜레이.
        #time.sleep(1)
        ##### 32번 코인 매수 종료 #####
        #############################


        ##### 33번코인 매수 시도 #####
        if op_mode33 == True:    # 매수 가능(True)일 경우 - 매수시도
            # 코인 현재가 불러오기
            price33 = pyupbit.get_current_price(krw_coin33)
            # 코인 목표가 불러오기
            target33 = cal_target(krw_coin33)

            if price33 >= target33:   # 목표가보다 현재가가 높을때
                # 매수가능금액 불러오기
                krw33 = upbit.get_balance("KRW")

                if krw33 > buy_krw:    # 매수가능금액 krw33 이 매수설정금액 buy_krw 보다 많을 경우: 매수
                    if krw33 > 10100:     # 매수가능금액 krw33 이 10,100원 초과일 경우 : 매수
                        # 매수금액은 매수평균가 buy_krw 로
                        upbit.buy_market_order(krw_coin33, buy_krw * 0.99)   # 매수가능금액에서 1%를 빼고

                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode33 = False

                        # 1초 딜레이
                        time.sleep(1)
                        # 보유수량 불러오기
                        krw_balance33 = upbit.get_balance(krw_coin33)
                        # 코인 현재가 불러오기
                        price33 = pyupbit.get_current_price(krw_coin33)
                        # 보유코인 원화금액으로 계산하기
                        bp33 = price33 * krw_balance33

                        # 보유 및 매수 가능 출력.
                        print(f"[ 33. {krw_coin33} 매수완료. ]")
                        print(f"매수시간 : {now}  |  코인명 : {coin33}  |  현재가 = ￦{price33}  |  금일목표가 = ￦{target33}  |  보유수량 = {krw_balance33}  |  평가금액 = ￦{bp33}")
                        print(f"매수가능 - {op_mode33} - 불가")
                        print("")
                    else:
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode33 = False

                        print(f"[ 33. {krw_coin33} 잔고부족으로 매수안함. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin33}  |  현재매수가능 - {op_mode33} - 불가")
                        print("")

                elif krw33 <= buy_krw:   # 매수가능금액 krw33 가 매수평균가 buy_krw 보다 같거나 작을때
                    if krw33 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                        # 매수금액은 매수가능금액인 krw33 로
                        upbit.buy_market_order(krw_coin33, krw33 * 0.99)   # 매수가능금액에서 1%를 빼고

                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode33 = False

                        # 1초 딜레이
                        time.sleep(1)
                        # 보유수량 불러오기
                        krw_balance33 = upbit.get_balance(krw_coin33)
                        # 코인 현재가 불러오기
                        price33 = pyupbit.get_current_price(krw_coin33)
                        # 보유코인 원화금액으로 계산하기
                        bp33 = price33 * krw_balance33

                        # 보유 및 매수 가능 출력.
                        print(f"[ 33. {krw_coin33} 매수완료. ]")
                        print(f"매수시간 : {now}  |  코인명 : {coin33}  |  현재가 = ￦{price33}  |  금일목표가 = ￦{target33}  |  보유수량 = {krw_balance33}  |  평가금액 = ￦{bp33}")
                        print(f"매수가능 - {op_mode33} - 불가")
                        print("")
                    else:
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode33 = False

                        print(f"[ 33. {krw_coin33} 잔고부족으로 매수안함. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin33}  |  현재매수가능 - {op_mode33} - 불가")
                        print("")

        # 1초 딜레이.
        #time.sleep(1)
        ##### 33번 코인 매수 종료 #####
        #############################


        ##### 34번코인 매수 시도 #####
        if op_mode34 == True:    # 매수 가능(True)일 경우 - 매수시도
            # 코인 현재가 불러오기
            price34 = pyupbit.get_current_price(krw_coin34)
            # 코인 목표가 불러오기
            target34 = cal_target(krw_coin34)

            if price34 >= target34:   # 목표가보다 현재가가 높을때
                # 매수가능금액 불러오기
                krw34 = upbit.get_balance("KRW")

                if krw34 > buy_krw:    # 매수가능금액 krw34 이 매수설정금액 buy_krw 보다 많을 경우: 매수
                    if krw34 > 10100:     # 매수가능금액 krw34 이 10,100원 초과일 경우 : 매수
                        # 매수금액은 매수평균가 buy_krw 로
                        upbit.buy_market_order(krw_coin34, buy_krw * 0.99)   # 매수가능금액에서 1%를 빼고

                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode34 = False

                        # 1초 딜레이
                        time.sleep(1)
                        # 보유수량 불러오기
                        krw_balance34 = upbit.get_balance(krw_coin34)
                        # 코인 현재가 불러오기
                        price34 = pyupbit.get_current_price(krw_coin34)
                        # 보유코인 원화금액으로 계산하기
                        bp34 = price34 * krw_balance34

                        # 보유 및 매수 가능 출력.
                        print(f"[ 34. {krw_coin34} 매수완료. ]")
                        print(f"매수시간 : {now}  |  코인명 : {coin34}  |  현재가 = ￦{price34}  |  금일목표가 = ￦{target34}  |  보유수량 = {krw_balance34}  |  평가금액 = ￦{bp34}")
                        print(f"매수가능 - {op_mode34} - 불가")
                        print("")
                    else:
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode34 = False

                        print(f"[ 34. {krw_coin34} 잔고부족으로 매수안함. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin34}  |  현재매수가능 - {op_mode34} - 불가")
                        print("")

                elif krw34 <= buy_krw:   # 매수가능금액 krw34 가 매수평균가 buy_krw 보다 같거나 작을때
                    if krw34 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                        # 매수금액은 매수가능금액인 krw34 로
                        upbit.buy_market_order(krw_coin34, krw34 * 0.99)   # 매수가능금액에서 1%를 빼고

                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode34 = False

                        # 1초 딜레이
                        time.sleep(1)
                        # 보유수량 불러오기
                        krw_balance34 = upbit.get_balance(krw_coin34)
                        # 코인 현재가 불러오기
                        price34 = pyupbit.get_current_price(krw_coin34)
                        # 보유코인 원화금액으로 계산하기
                        bp34 = price34 * krw_balance34

                        # 보유 및 매수 가능 출력.
                        print(f"[ 34. {krw_coin34} 매수완료. ]")
                        print(f"매수시간 : {now}  |  코인명 : {coin34}  |  현재가 = ￦{price34}  |  금일목표가 = ￦{target34}  |  보유수량 = {krw_balance34}  |  평가금액 = ￦{bp34}")
                        print(f"매수가능 - {op_mode34} - 불가")
                        print("")
                    else:
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode34 = False

                        print(f"[ 34. {krw_coin34} 잔고부족으로 매수안함. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin34}  |  현재매수가능 - {op_mode34} - 불가")
                        print("")

        # 1초 딜레이.
        #time.sleep(1)
        ##### 34번 코인 매수 종료 #####
        #############################


        ##### 35번코인 매수 시도 #####
        if op_mode35 == True:    # 매수 가능(True)일 경우 - 매수시도
            # 코인 현재가 불러오기
            price35 = pyupbit.get_current_price(krw_coin35)
            # 코인 목표가 불러오기
            target35 = cal_target(krw_coin35)

            if price35 >= target35:   # 목표가보다 현재가가 높을때
                # 매수가능금액 불러오기
                krw35 = upbit.get_balance("KRW")

                if krw35 > buy_krw:    # 매수가능금액 krw35 이 매수설정금액 buy_krw 보다 많을 경우: 매수
                    if krw35 > 10100:     # 매수가능금액 krw35 이 10,100원 초과일 경우 : 매수
                        # 매수금액은 매수평균가 buy_krw 로
                        upbit.buy_market_order(krw_coin35, buy_krw * 0.99)   # 매수가능금액에서 1%를 빼고

                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode35 = False

                        # 1초 딜레이
                        time.sleep(1)
                        # 보유수량 불러오기
                        krw_balance35 = upbit.get_balance(krw_coin35)
                        # 코인 현재가 불러오기
                        price35 = pyupbit.get_current_price(krw_coin35)
                        # 보유코인 원화금액으로 계산하기
                        bp35 = price35 * krw_balance35

                        # 보유 및 매수 가능 출력.
                        print(f"[ 35. {krw_coin35} 매수완료. ]")
                        print(f"매수시간 : {now}  |  코인명 : {coin35}  |  현재가 = ￦{price35}  |  금일목표가 = ￦{target35}  |  보유수량 = {krw_balance35}  |  평가금액 = ￦{bp35}")
                        print(f"매수가능 - {op_mode35} - 불가")
                        print("")
                    else:
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode35 = False

                        print(f"[ 35. {krw_coin35} 잔고부족으로 매수안함. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin35}  |  현재매수가능 - {op_mode35} - 불가")
                        print("")

                elif krw35 <= buy_krw:   # 매수가능금액 krw35 가 매수평균가 buy_krw 보다 같거나 작을때
                    if krw35 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                        # 매수금액은 매수가능금액인 krw35 로
                        upbit.buy_market_order(krw_coin35, krw35 * 0.99)   # 매수가능금액에서 1%를 빼고

                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode35 = False

                        # 1초 딜레이
                        time.sleep(1)
                        # 보유수량 불러오기
                        krw_balance35 = upbit.get_balance(krw_coin35)
                        # 코인 현재가 불러오기
                        price35 = pyupbit.get_current_price(krw_coin35)
                        # 보유코인 원화금액으로 계산하기
                        bp35 = price35 * krw_balance35

                        # 보유 및 매수 가능 출력.
                        print(f"[ 35. {krw_coin35} 매수완료. ]")
                        print(f"매수시간 : {now}  |  코인명 : {coin35}  |  현재가 = ￦{price35}  |  금일목표가 = ￦{target35}  |  보유수량 = {krw_balance35}  |  평가금액 = ￦{bp35}")
                        print(f"매수가능 - {op_mode35} - 불가")
                        print("")
                    else:
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode35 = False

                        print(f"[ 35. {krw_coin35} 잔고부족으로 매수안함. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin35}  |  현재매수가능 - {op_mode35} - 불가")
                        print("")

        # 1초 딜레이.
        time.sleep(1)
        ##### 35번 코인 매수 종료 #####
        #############################


        ##### 36번코인 매수 시도 #####
        if op_mode36 == True:    # 매수 가능(True)일 경우 - 매수시도
            # 코인 현재가 불러오기
            price36 = pyupbit.get_current_price(krw_coin36)
            # 코인 목표가 불러오기
            target36 = cal_target(krw_coin36)

            if price36 >= target36:   # 목표가보다 현재가가 높을때
                # 매수가능금액 불러오기
                krw36 = upbit.get_balance("KRW")

                if krw36 > buy_krw:    # 매수가능금액 krw36 이 매수설정금액 buy_krw 보다 많을 경우: 매수
                    if krw36 > 10100:     # 매수가능금액 krw36 이 10,100원 초과일 경우 : 매수
                        # 매수금액은 매수평균가 buy_krw 로
                        upbit.buy_market_order(krw_coin36, buy_krw * 0.99)   # 매수가능금액에서 1%를 빼고

                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode36 = False

                        # 1초 딜레이
                        time.sleep(1)
                        # 보유수량 불러오기
                        krw_balance36 = upbit.get_balance(krw_coin36)
                        # 코인 현재가 불러오기
                        price36 = pyupbit.get_current_price(krw_coin36)
                        # 보유코인 원화금액으로 계산하기
                        bp36 = price36 * krw_balance36

                        # 보유 및 매수 가능 출력.
                        print(f"[ 36. {krw_coin36} 매수완료. ]")
                        print(f"매수시간 : {now}  |  코인명 : {coin36}  |  현재가 = ￦{price36}  |  금일목표가 = ￦{target36}  |  보유수량 = {krw_balance36}  |  평가금액 = ￦{bp36}")
                        print(f"매수가능 - {op_mode36} - 불가")
                        print("")
                    else:
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode36 = False

                        print(f"[ 36. {krw_coin36} 잔고부족으로 매수안함. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin36}  |  현재매수가능 - {op_mode36} - 불가")
                        print("")

                elif krw36 <= buy_krw:   # 매수가능금액 krw36 가 매수평균가 buy_krw 보다 같거나 작을때
                    if krw36 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                        # 매수금액은 매수가능금액인 krw36 로
                        upbit.buy_market_order(krw_coin36, krw36 * 0.99)   # 매수가능금액에서 1%를 빼고

                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode36 = False

                        # 1초 딜레이
                        time.sleep(1)
                        # 보유수량 불러오기
                        krw_balance36 = upbit.get_balance(krw_coin36)
                        # 코인 현재가 불러오기
                        price36 = pyupbit.get_current_price(krw_coin36)
                        # 보유코인 원화금액으로 계산하기
                        bp36 = price36 * krw_balance36

                        # 보유 및 매수 가능 출력.
                        print(f"[ 36. {krw_coin36} 매수완료. ]")
                        print(f"매수시간 : {now}  |  코인명 : {coin36}  |  현재가 = ￦{price36}  |  금일목표가 = ￦{target36}  |  보유수량 = {krw_balance36}  |  평가금액 = ￦{bp36}")
                        print(f"매수가능 - {op_mode36} - 불가")
                        print("")
                    else:
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode36 = False

                        print(f"[ 36. {krw_coin36} 잔고부족으로 매수안함. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin36}  |  현재매수가능 - {op_mode36} - 불가")
                        print("")

        # 1초 딜레이.
        #time.sleep(1)
        ##### 36번 코인 매수 종료 #####
        #############################


        ##### 37번코인 매수 시도 #####
        if op_mode37 == True:    # 매수 가능(True)일 경우 - 매수시도
            # 코인 현재가 불러오기
            price37 = pyupbit.get_current_price(krw_coin37)
            # 코인 목표가 불러오기
            target37 = cal_target(krw_coin37)

            if price37 >= target37:   # 목표가보다 현재가가 높을때
                # 매수가능금액 불러오기
                krw37 = upbit.get_balance("KRW")

                if krw37 > buy_krw:    # 매수가능금액 krw37 이 매수설정금액 buy_krw 보다 많을 경우: 매수
                    if krw37 > 10100:     # 매수가능금액 krw37 이 10,100원 초과일 경우 : 매수
                        # 매수금액은 매수평균가 buy_krw 로
                        upbit.buy_market_order(krw_coin37, buy_krw * 0.99)   # 매수가능금액에서 1%를 빼고

                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode37 = False

                        # 1초 딜레이
                        time.sleep(1)
                        # 보유수량 불러오기
                        krw_balance37 = upbit.get_balance(krw_coin37)
                        # 코인 현재가 불러오기
                        price37 = pyupbit.get_current_price(krw_coin37)
                        # 보유코인 원화금액으로 계산하기
                        bp37 = price37 * krw_balance37

                        # 보유 및 매수 가능 출력.
                        print(f"[ 37. {krw_coin37} 매수완료. ]")
                        print(f"매수시간 : {now}  |  코인명 : {coin37}  |  현재가 = ￦{price37}  |  금일목표가 = ￦{target37}  |  보유수량 = {krw_balance37}  |  평가금액 = ￦{bp37}")
                        print(f"매수가능 - {op_mode37} - 불가")
                        print("")
                    else:
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode37 = False

                        print(f"[ 37. {krw_coin37} 잔고부족으로 매수안함. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin37}  |  현재매수가능 - {op_mode37} - 불가")
                        print("")

                elif krw37 <= buy_krw:   # 매수가능금액 krw37 가 매수평균가 buy_krw 보다 같거나 작을때
                    if krw37 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                        # 매수금액은 매수가능금액인 krw37 로
                        upbit.buy_market_order(krw_coin37, krw37 * 0.99)   # 매수가능금액에서 1%를 빼고

                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode37 = False

                        # 1초 딜레이
                        time.sleep(1)
                        # 보유수량 불러오기
                        krw_balance37 = upbit.get_balance(krw_coin37)
                        # 코인 현재가 불러오기
                        price37 = pyupbit.get_current_price(krw_coin37)
                        # 보유코인 원화금액으로 계산하기
                        bp37 = price37 * krw_balance37

                        # 보유 및 매수 가능 출력.
                        print(f"[ 37. {krw_coin37} 매수완료. ]")
                        print(f"매수시간 : {now}  |  코인명 : {coin37}  |  현재가 = ￦{price37}  |  금일목표가 = ￦{target37}  |  보유수량 = {krw_balance37}  |  평가금액 = ￦{bp37}")
                        print(f"매수가능 - {op_mode37} - 불가")
                        print("")
                    else:
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode37 = False

                        print(f"[ 37. {krw_coin37} 잔고부족으로 매수안함. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin37}  |  현재매수가능 - {op_mode37} - 불가")
                        print("")

        # 1초 딜레이.
        #time.sleep(1)
        ##### 37번 코인 매수 종료 #####
        #############################


        ##### 38번코인 매수 시도 #####
        if op_mode38 == True:    # 매수 가능(True)일 경우 - 매수시도
            # 코인 현재가 불러오기
            price38 = pyupbit.get_current_price(krw_coin38)
            # 코인 목표가 불러오기
            target38 = cal_target(krw_coin38)

            if price38 >= target38:   # 목표가보다 현재가가 높을때
                # 매수가능금액 불러오기
                krw38 = upbit.get_balance("KRW")

                if krw38 > buy_krw:    # 매수가능금액 krw38 이 매수설정금액 buy_krw 보다 많을 경우: 매수
                    if krw38 > 10100:     # 매수가능금액 krw38 이 10,100원 초과일 경우 : 매수
                        # 매수금액은 매수평균가 buy_krw 로
                        upbit.buy_market_order(krw_coin38, buy_krw * 0.99)   # 매수가능금액에서 1%를 빼고

                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode38 = False

                        # 1초 딜레이
                        time.sleep(1)
                        # 보유수량 불러오기
                        krw_balance38 = upbit.get_balance(krw_coin38)
                        # 코인 현재가 불러오기
                        price38 = pyupbit.get_current_price(krw_coin38)
                        # 보유코인 원화금액으로 계산하기
                        bp38 = price38 * krw_balance38

                        # 보유 및 매수 가능 출력.
                        print(f"[ 38. {krw_coin38} 매수완료. ]")
                        print(f"매수시간 : {now}  |  코인명 : {coin38}  |  현재가 = ￦{price38}  |  금일목표가 = ￦{target38}  |  보유수량 = {krw_balance38}  |  평가금액 = ￦{bp38}")
                        print(f"매수가능 - {op_mode38} - 불가")
                        print("")
                    else:
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode38 = False

                        print(f"[ 38. {krw_coin38} 잔고부족으로 매수안함. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin38}  |  현재매수가능 - {op_mode38} - 불가")
                        print("")

                elif krw38 <= buy_krw:   # 매수가능금액 krw38 가 매수평균가 buy_krw 보다 같거나 작을때
                    if krw38 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                        # 매수금액은 매수가능금액인 krw38 로
                        upbit.buy_market_order(krw_coin38, krw38 * 0.99)   # 매수가능금액에서 1%를 빼고

                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode38 = False

                        # 1초 딜레이
                        time.sleep(1)
                        # 보유수량 불러오기
                        krw_balance38 = upbit.get_balance(krw_coin38)
                        # 코인 현재가 불러오기
                        price38 = pyupbit.get_current_price(krw_coin38)
                        # 보유코인 원화금액으로 계산하기
                        bp38 = price38 * krw_balance38

                        # 보유 및 매수 가능 출력.
                        print(f"[ 38. {krw_coin38} 매수완료. ]")
                        print(f"매수시간 : {now}  |  코인명 : {coin38}  |  현재가 = ￦{price38}  |  금일목표가 = ￦{target38}  |  보유수량 = {krw_balance38}  |  평가금액 = ￦{bp38}")
                        print(f"매수가능 - {op_mode38} - 불가")
                        print("")
                    else:
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode38 = False

                        print(f"[ 38. {krw_coin38} 잔고부족으로 매수안함. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin38}  |  현재매수가능 - {op_mode38} - 불가")
                        print("")

        # 1초 딜레이.
        #time.sleep(1)
        ##### 38번 코인 매수 종료 #####
        #############################


        ##### 39번코인 매수 시도 #####
        if op_mode39 == True:    # 매수 가능(True)일 경우 - 매수시도
            # 코인 현재가 불러오기
            price39 = pyupbit.get_current_price(krw_coin39)
            # 코인 목표가 불러오기
            target39 = cal_target(krw_coin39)

            if price39 >= target39:   # 목표가보다 현재가가 높을때
                # 매수가능금액 불러오기
                krw39 = upbit.get_balance("KRW")

                if krw39 > buy_krw:    # 매수가능금액 krw39 이 매수설정금액 buy_krw 보다 많을 경우: 매수
                    if krw39 > 10100:     # 매수가능금액 krw39 이 10,100원 초과일 경우 : 매수
                        # 매수금액은 매수평균가 buy_krw 로
                        upbit.buy_market_order(krw_coin39, buy_krw * 0.99)   # 매수가능금액에서 1%를 빼고

                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode39 = False

                        # 1초 딜레이
                        time.sleep(1)
                        # 보유수량 불러오기
                        krw_balance39 = upbit.get_balance(krw_coin39)
                        # 코인 현재가 불러오기
                        price39 = pyupbit.get_current_price(krw_coin39)
                        # 보유코인 원화금액으로 계산하기
                        bp39 = price39 * krw_balance39

                        # 보유 및 매수 가능 출력.
                        print(f"[ 39. {krw_coin39} 매수완료. ]")
                        print(f"매수시간 : {now}  |  코인명 : {coin39}  |  현재가 = ￦{price39}  |  금일목표가 = ￦{target39}  |  보유수량 = {krw_balance39}  |  평가금액 = ￦{bp39}")
                        print(f"매수가능 - {op_mode39} - 불가")
                        print("")
                    else:
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode39 = False

                        print(f"[ 39. {krw_coin39} 잔고부족으로 매수안함. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin39}  |  현재매수가능 - {op_mode39} - 불가")
                        print("")

                elif krw39 <= buy_krw:   # 매수가능금액 krw39 가 매수평균가 buy_krw 보다 같거나 작을때
                    if krw39 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                        # 매수금액은 매수가능금액인 krw39 로
                        upbit.buy_market_order(krw_coin39, krw39 * 0.99)   # 매수가능금액에서 1%를 빼고

                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode39 = False

                        # 1초 딜레이
                        time.sleep(1)
                        # 보유수량 불러오기
                        krw_balance39 = upbit.get_balance(krw_coin39)
                        # 코인 현재가 불러오기
                        price39 = pyupbit.get_current_price(krw_coin39)
                        # 보유코인 원화금액으로 계산하기
                        bp39 = price39 * krw_balance39

                        # 보유 및 매수 가능 출력.
                        print(f"[ 39. {krw_coin39} 매수완료. ]")
                        print(f"매수시간 : {now}  |  코인명 : {coin39}  |  현재가 = ￦{price39}  |  금일목표가 = ￦{target39}  |  보유수량 = {krw_balance39}  |  평가금액 = ￦{bp39}")
                        print(f"매수가능 - {op_mode39} - 불가")
                        print("")
                    else:
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode39 = False

                        print(f"[ 39. {krw_coin39} 잔고부족으로 매수안함. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin39}  |  현재매수가능 - {op_mode39} - 불가")
                        print("")

        # 1초 딜레이.
        #time.sleep(1)
        ##### 39번 코인 매수 종료 #####
        #############################


        ##### 40번코인 매수 시도 #####
        if op_mode40 == True:    # 매수 가능(True)일 경우 - 매수시도
            # 코인 현재가 불러오기
            price40 = pyupbit.get_current_price(krw_coin40)
            # 코인 목표가 불러오기
            target40 = cal_target(krw_coin40)

            if price40 >= target40:   # 목표가보다 현재가가 높을때
                # 매수가능금액 불러오기
                krw40 = upbit.get_balance("KRW")

                if krw40 > buy_krw:    # 매수가능금액 krw40 이 매수설정금액 buy_krw 보다 많을 경우: 매수
                    if krw40 > 10100:     # 매수가능금액 krw40 이 10,100원 초과일 경우 : 매수
                        # 매수금액은 매수평균가 buy_krw 로
                        upbit.buy_market_order(krw_coin40, buy_krw * 0.99)   # 매수가능금액에서 1%를 빼고

                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode40 = False

                        # 1초 딜레이
                        time.sleep(1)
                        # 보유수량 불러오기
                        krw_balance40 = upbit.get_balance(krw_coin40)
                        # 코인 현재가 불러오기
                        price40 = pyupbit.get_current_price(krw_coin40)
                        # 보유코인 원화금액으로 계산하기
                        bp40 = price40 * krw_balance40

                        # 보유 및 매수 가능 출력.
                        print(f"[ 40. {krw_coin40} 매수완료. ]")
                        print(f"매수시간 : {now}  |  코인명 : {coin40}  |  현재가 = ￦{price40}  |  금일목표가 = ￦{target40}  |  보유수량 = {krw_balance40}  |  평가금액 = ￦{bp40}")
                        print(f"매수가능 - {op_mode40} - 불가")
                        print("")
                    else:
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode40 = False

                        print(f"[ 40. {krw_coin40} 잔고부족으로 매수안함. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin40}  |  현재매수가능 - {op_mode40} - 불가")
                        print("")

                elif krw40 <= buy_krw:   # 매수가능금액 krw40 가 매수평균가 buy_krw 보다 같거나 작을때
                    if krw40 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                        # 매수금액은 매수가능금액인 krw40 로
                        upbit.buy_market_order(krw_coin40, krw40 * 0.99)   # 매수가능금액에서 1%를 빼고

                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode40 = False

                        # 1초 딜레이
                        time.sleep(1)
                        # 보유수량 불러오기
                        krw_balance40 = upbit.get_balance(krw_coin40)
                        # 코인 현재가 불러오기
                        price40 = pyupbit.get_current_price(krw_coin40)
                        # 보유코인 원화금액으로 계산하기
                        bp40 = price40 * krw_balance40

                        # 보유 및 매수 가능 출력.
                        print(f"[ 40. {krw_coin40} 매수완료. ]")
                        print(f"매수시간 : {now}  |  코인명 : {coin40}  |  현재가 = ￦{price40}  |  금일목표가 = ￦{target40}  |  보유수량 = {krw_balance40}  |  평가금액 = ￦{bp40}")
                        print(f"매수가능 - {op_mode40} - 불가")
                        print("")
                    else:
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode40 = False

                        print(f"[ 40. {krw_coin40} 잔고부족으로 매수안함. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin40}  |  현재매수가능 - {op_mode40} - 불가")
                        print("")

        # 1초 딜레이.
        time.sleep(1)
        ##### 40번 코인 매수 종료 #####
        #############################


    ######################################################################################################################################################
    ######################################################################################################################################################
    ######################################################################################################################################################