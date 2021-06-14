import pyupbit
import time
import datetime



#############################################
#############################################
##### 4시간봉으로 28일이동평균선 자동 매매 #####
#############################################
#############################################



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

# 28 이동평균선 조회.
def get_ma20(ticker):
    # interval 받는 시간 "minute1", "minute5", "minute10", "minute20", "minute60"(1시간), "minute240"(4시간), "day", "week" 등등
    df = pyupbit.get_ohlcv(ticker, interval="minute240", count=28)
    ma20 = df['close'].rolling(28).mean().iloc[-1]
    return ma20





#엑세스키, 시크릿키 가져오기
access = "s9mx5YF3TtInoUqUM3D8x464PUamTpUxZxRg35zj"
secret = "DfBQ4UXJMyaD172GD4rpwGIQ1zxBuxIMgpRvW4ZI"


# 매수금액 가져오기
#buy_krw = int(lines[5].strip())

# 코인매매갯수 가져오기
#trade_coinX = int(lines[7].strip())


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



##### 업비트 로그인 시도 #####
# class instance, object
upbit = pyupbit.Upbit(access, secret)


# 매수금액설정
#buy_krw = 4000000
# 잔고원화 매수 가능금액 확인용 설정
#hold_krw = buy_krw * 1.01
#print("")
#print("---------- ---------- ---------- ---------- ----------")
#print("")
#print(f"매수시매수금액 = ￦{buy_krw}  |  조건검색시 잔고비교금액 = ￦{hold_krw}")
#print("")


# 코인 매매 갯수 변수 설정
#trade_coinX = 16
#print(f"매수할 코인 갯수 = {trade_coinX} 개")
#print("")
#print("---------- ---------- ---------- ---------- ----------")
#print("")



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



print("")
print("")
print("---------- ---------- ---------- ---------- ----------")
print(" -----=====     매매시작전 보유 코인 현황     =====----- ")
print("---------- ---------- ---------- ---------- ----------")
print("")
print("")


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


##### 보유 코인 조회 끝 #####
############################




######################################################################################################################################################
######################################################################################################################################################
######################################################################################################################################################


print("")
print("")
print("---------- ---------- ---------- ---------- ----------")
print(" -----=====          자동 매매 시작          =====----- ")
print("---------- ---------- ---------- ---------- ----------")
print("")
print("")


######################################################################################################################################################
######################################################################################################################################################
######################################################################################################################################################




#########################
##### 자동 매매 시작 #####
while True:
    # 현재 시간 불러오기
    now = datetime.datetime.now()

    # 매일 4시간마다
    if now.hour == 1 or now.hour == 5 or now.hour == 9 or now.hour == 13 or now.hour == 17 or now.hour == 21:
        # 0분에
        if now.minute == 0:
            # 총 평가금액 계산
            # 매수가능금액 불러오기
            krw = upbit.get_balance("KRW")
            ##### 매수가능금액을 평균구하기
            # 보유코인 합.
            total_bp1 = krw + bp1 + bp2 + bp3 + bp4 + bp5 + bp6 + bp7 + bp8 + bp9 + bp10
            total_bp2 = bp11 + bp12 + bp13 + bp14 + bp15 + bp16 + bp17 + bp18 + bp19 + bp20
            total_bp3 = bp21 + bp22 + bp23 + bp24 + bp25 + bp26 + bp27 + bp28 + bp29 + bp30
            # 보유코인 나누기
            total_sum1 = total_bp1 / 7
            total_sum2 = total_bp2 / 7
            total_sum3 = total_bp3 / 7
            # 매수가능 평균가.
            buy_krw = (total_sum1 + total_sum2 + total_sum3) / 3


            ###############################
            ##### 매매 : 1번코인 시작. #####
            # 코인 현재가 불러오기
            price1 = pyupbit.get_current_price(krw_coin1)
            # 이평선 조회.
            ma20_1 = get_ma20(krw_coin1)

            # 매수가능금액 불러오기
            krw1 = upbit.get_balance("KRW")

            # 20일 이평선 조건문
            if price1 > ma20_1:     # 20일이평선가격보다 현재가가 높을때는 매수
                if op_mode1 == True:    # 매수 가능(True)일 경우 - 매수시도
                    if krw1 > buy_krw:      # 매수가능금액 krw1 가 매수평균가 buy_krw 보다 클때
                        if krw1 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                            if buy_krw > 10100:     # 매수평균가 buy_krw 가 10,100원 초과일 경우 : 매수
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
                                print(f"매수시간 : {now}  |  코인명 : {coin1}  |  현재가 = ￦{price1}  |  20이평선가 = ￦{ma20_1}  |  보유수량 = {krw_balance1}  |  평가금액 = ￦{bp1}")
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
                            print(f"매수시간 : {now}  |  코인명 : {coin1}  |  현재가 = ￦{price1}  |  20이평선가 = ￦{ma20_1}  |  보유수량 = {krw_balance1}  |  평가금액 = ￦{bp1}")
                            print(f"매수가능 - {op_mode1} - 불가")
                            print("")
                        else:
                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode1 = False

                            print(f"[ 1. {krw_coin1} 잔고부족으로 매수안함. ]")
                            print(f"현재시간 : {now}  |  코인명 : {coin1}  |  현재매수가능 - {op_mode1} - 불가")
                            print("")

            elif price1 < ma20_1:       # 20일이평선보다 현재가가 낮을때는 매도
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
                        time.sleep(1)
                        # 보유수량 불러오기
                        krw_balance1 = upbit.get_balance(krw_coin1)
                        # 코인 현재가 불러오기
                        price1 = pyupbit.get_current_price(krw_coin1)
                        # 보유코인 원화금액으로 계산하기
                        bp1 = price1 * krw_balance1

                        # 보유 및 매수 가능 출력.
                        print(f"[ 1. {krw_coin1} 매도완료. ]")
                        print(f"매도시간 : {now}  |  코인명 : {coin1}  |  현재가 = ￦{price1}  |  20이평선가 = ￦{ma20_1}  |  보유수량 = {krw_balance1}  |  평가금액 = ￦{bp1}  |  매수가능 : {op_mode1} - 매수가능")
                        print("")

                    else:   # 보유코인 평가 금액이 10,100원 이하일때
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode1 = True

            # 1초 딜레이.
            time.sleep(1)
            ##### 1번 코인 매매 종료 #####
            #############################

            ###############################
            ##### 매매 : 2번코인 시작. #####
            # 코인 현재가 불러오기
            price2 = pyupbit.get_current_price(krw_coin2)
            # 이평선 조회.
            ma20_2 = get_ma20(krw_coin2)

            # 매수가능금액 불러오기
            krw2 = upbit.get_balance("KRW")

            # 20일 이평선 조건문
            if price2 > ma20_2:     # 20일이평선가격보다 현재가가 높을때는 매수
                if op_mode2 == True:    # 매수 가능(True)일 경우 - 매수시도
                    if krw2 > buy_krw:      # 매수가능금액 krw2 가 매수평균가 buy_krw 보다 클때
                        if krw2 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                            if buy_krw > 10100:     # 매수평균가 buy_krw 가 10,100원 초과일 경우 : 매수
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
                                print(f"매수시간 : {now}  |  코인명 : {coin2}  |  현재가 = ￦{price2}  |  20이평선가 = ￦{ma20_2}  |  보유수량 = {krw_balance2}  |  평가금액 = ￦{bp2}")
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
                            print(f"매수시간 : {now}  |  코인명 : {coin2}  |  현재가 = ￦{price2}  |  20이평선가 = ￦{ma20_2}  |  보유수량 = {krw_balance2}  |  평가금액 = ￦{bp2}")
                            print(f"매수가능 - {op_mode2} - 불가")
                            print("")
                        else:
                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode2 = False

                            print(f"[ 2. {krw_coin2} 잔고부족으로 매수안함. ]")
                            print(f"현재시간 : {now}  |  코인명 : {coin2}  |  현재매수가능 - {op_mode2} - 불가")
                            print("")

            elif price2 < ma20_2:       # 20일이평선보다 현재가가 낮을때는 매도
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
                        time.sleep(1)
                        # 보유수량 불러오기
                        krw_balance2 = upbit.get_balance(krw_coin2)
                        # 코인 현재가 불러오기
                        price2 = pyupbit.get_current_price(krw_coin2)
                        # 보유코인 원화금액으로 계산하기
                        bp2 = price2 * krw_balance2

                        # 보유 및 매수 가능 출력.
                        print(f"[ 2. {krw_coin2} 매도완료. ]")
                        print(f"매도시간 : {now}  |  코인명 : {coin2}  |  현재가 = ￦{price2}  |  20이평선가 = ￦{ma20_2}  |  보유수량 = {krw_balance2}  |  평가금액 = ￦{bp2}  |  매수가능 : {op_mode2} - 매수가능")
                        print("")

                    else:   # 보유코인 평가 금액이 10,100원 이하일때
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode2 = True

            # 1초 딜레이.
            time.sleep(1)
            ##### 2번 코인 매매 종료 #####
            #############################


            ###############################
            ##### 매매 : 3번코인 시작. #####
            # 코인 현재가 불러오기
            price3 = pyupbit.get_current_price(krw_coin3)
            # 이평선 조회.
            ma20_3 = get_ma20(krw_coin3)

            # 매수가능금액 불러오기
            krw3 = upbit.get_balance("KRW")

            # 20일 이평선 조건문
            if price3 > ma20_3:     # 20일이평선가격보다 현재가가 높을때는 매수
                if op_mode3 == True:    # 매수 가능(True)일 경우 - 매수시도
                    if krw3 > buy_krw:      # 매수가능금액 krw3 가 매수평균가 buy_krw 보다 클때
                        if krw3 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                            if buy_krw > 10100:     # 매수평균가 buy_krw 가 10,100원 초과일 경우 : 매수
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
                                print(f"매수시간 : {now}  |  코인명 : {coin3}  |  현재가 = ￦{price3}  |  20이평선가 = ￦{ma20_3}  |  보유수량 = {krw_balance3}  |  평가금액 = ￦{bp3}")
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

                            time.sleep(1)
                            # 보유수량 불러오기
                            krw_balance3 = upbit.get_balance(krw_coin3)
                            # 코인 현재가 불러오기
                            price3 = pyupbit.get_current_price(krw_coin3)
                            # 보유코인 원화금액으로 계산하기
                            bp3 = price3 * krw_balance3

                            # 보유 및 매수 가능 출력.
                            print(f"[ 3. {krw_coin3} 매수완료. ]")
                            print(f"매수시간 : {now}  |  코인명 : {coin3}  |  현재가 = ￦{price3}  |  20이평선가 = ￦{ma20_3}  |  보유수량 = {krw_balance3}  |  평가금액 = ￦{bp3}  |  매수가능 - {op_mode3} - 불가")
                            print("")

                        else:
                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode3 = False

                            print(f"[ 3. {krw_coin3} 잔고부족으로 매수안함. ]")
                            print(f"현재시간 : {now}  |  코인명 : {coin3}  |  현재매수가능 - {op_mode3} - 불가")
                            print("")

            elif price3 < ma20_3:       # 20일이평선보다 현재가가 낮을때는 매도
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
                        time.sleep(1)
                        # 보유수량 불러오기
                        krw_balance3 = upbit.get_balance(krw_coin3)
                        # 코인 현재가 불러오기
                        price3 = pyupbit.get_current_price(krw_coin3)
                        # 보유코인 원화금액으로 계산하기
                        bp3 = price3 * krw_balance3

                        # 보유 및 매수 가능 출력.
                        print(f"[ 3. {krw_coin3} 매도완료. ]")
                        print(f"매도시간 : {now}  |  코인명 : {coin3}  |  현재가 = ￦{price3}  |  20이평선가 = ￦{ma20_3}  |  보유수량 = {krw_balance3}  |  평가금액 = ￦{bp3}  |  매수가능 : {op_mode3} - 매수가능")
                        print("")

                    else:   # 보유코인 평가 금액이 10,100원 이하일때
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode3 = True

            # 1초 딜레이.
            time.sleep(1)
            ##### 3번 코인 매매 종료 #####
            #############################


            ###############################
            ##### 매매 : 4번코인 시작. #####
            # 코인 현재가 불러오기
            price4 = pyupbit.get_current_price(krw_coin4)
            # 이평선 조회.
            ma20_4 = get_ma20(krw_coin4)

            # 매수가능금액 불러오기
            krw4 = upbit.get_balance("KRW")

            # 20일 이평선 조건문
            if price4 > ma20_4:     # 20일이평선가격보다 현재가가 높을때는 매수
                if op_mode4 == True:    # 매수 가능(True)일 경우 - 매수시도
                    if krw4 > buy_krw:      # 매수가능금액 krw4 가 매수평균가 buy_krw 보다 클때
                        if krw4 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                            if buy_krw > 10100:     # 매수평균가 buy_krw 가 10,100원 초과일 경우 : 매수
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
                                print(f"매수시간 : {now}  |  코인명 : {coin4}  |  현재가 = ￦{price4}  |  20이평선가 = ￦{ma20_4}  |  보유수량 = {krw_balance4}  |  평가금액 = ￦{bp4}")
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

                            time.sleep(1)
                            # 보유수량 불러오기
                            krw_balance4 = upbit.get_balance(krw_coin4)
                            # 코인 현재가 불러오기
                            price4 = pyupbit.get_current_price(krw_coin4)
                            # 보유코인 원화금액으로 계산하기
                            bp4 = price4 * krw_balance4

                            # 보유 및 매수 가능 출력.
                            print(f"[ 4. {krw_coin4} 매수완료. ]")
                            print(f"매수시간 : {now}  |  코인명 : {coin4}  |  현재가 = ￦{price4}  |  20이평선가 = ￦{ma20_4}  |  보유수량 = {krw_balance4}  |  평가금액 = ￦{bp4}  |  매수가능 - {op_mode4} - 불가")
                            print("")

                        else:
                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode4 = False

                            print(f"[ 4. {krw_coin4} 잔고부족으로 매수안함. ]")
                            print(f"현재시간 : {now}  |  코인명 : {coin4}  |  현재매수가능 - {op_mode4} - 불가")
                            print("")

            elif price4 < ma20_4:       # 20일이평선보다 현재가가 낮을때는 매도
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
                        time.sleep(1)
                        # 보유수량 불러오기
                        krw_balance4 = upbit.get_balance(krw_coin4)
                        # 코인 현재가 불러오기
                        price4 = pyupbit.get_current_price(krw_coin4)
                        # 보유코인 원화금액으로 계산하기
                        bp4 = price4 * krw_balance4

                        # 보유 및 매수 가능 출력.
                        print(f"[ 4. {krw_coin4} 매도완료. ]")
                        print(f"매도시간 : {now}  |  코인명 : {coin4}  |  현재가 = ￦{price4}  |  20이평선가 = ￦{ma20_4}  |  보유수량 = {krw_balance4}  |  평가금액 = ￦{bp4}  |  매수가능 : {op_mode4} - 매수가능")
                        print("")

                    else:   # 보유코인 평가 금액이 10,100원 이하일때
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode4 = True

            # 1초 딜레이.
            time.sleep(1)
            ##### 4번 코인 매매 종료 #####
            #############################


            ###############################
            ##### 매매 : 5번코인 시작. #####
            # 코인 현재가 불러오기
            price5 = pyupbit.get_current_price(krw_coin5)
            # 이평선 조회.
            ma20_5 = get_ma20(krw_coin5)

            # 매수가능금액 불러오기
            krw5 = upbit.get_balance("KRW")

            # 20일 이평선 조건문
            if price5 > ma20_5:     # 20일이평선가격보다 현재가가 높을때는 매수
                if op_mode5 == True:    # 매수 가능(True)일 경우 - 매수시도
                    if krw5 > buy_krw:      # 매수가능금액 krw5 가 매수평균가 buy_krw 보다 클때
                        if krw5 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                            if buy_krw > 10100:     # 매수평균가 buy_krw 가 10,100원 초과일 경우 : 매수
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
                                print(f"매수시간 : {now}  |  코인명 : {coin5}  |  현재가 = ￦{price5}  |  20이평선가 = ￦{ma20_5}  |  보유수량 = {krw_balance5}  |  평가금액 = ￦{bp5}")
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

                            time.sleep(1)
                            # 보유수량 불러오기
                            krw_balance5 = upbit.get_balance(krw_coin5)
                            # 코인 현재가 불러오기
                            price5 = pyupbit.get_current_price(krw_coin5)
                            # 보유코인 원화금액으로 계산하기
                            bp5 = price5 * krw_balance5

                            # 보유 및 매수 가능 출력.
                            print(f"[ 5. {krw_coin5} 매수완료. ]")
                            print(f"매수시간 : {now}  |  코인명 : {coin5}  |  현재가 = ￦{price5}  |  20이평선가 = ￦{ma20_5}  |  보유수량 = {krw_balance5}  |  평가금액 = ￦{bp5}  |  매수가능 - {op_mode5} - 불가")
                            print("")

                        else:
                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode5 = False

                            print(f"[ 5. {krw_coin5} 잔고부족으로 매수안함. ]")
                            print(f"현재시간 : {now}  |  코인명 : {coin5}  |  현재매수가능 - {op_mode5} - 불가")
                            print("")

            elif price5 < ma20_5:       # 20일이평선보다 현재가가 낮을때는 매도
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
                        time.sleep(1)
                        # 보유수량 불러오기
                        krw_balance5 = upbit.get_balance(krw_coin5)
                        # 코인 현재가 불러오기
                        price5 = pyupbit.get_current_price(krw_coin5)
                        # 보유코인 원화금액으로 계산하기
                        bp5 = price5 * krw_balance5

                        # 보유 및 매수 가능 출력.
                        print(f"[ 5. {krw_coin5} 매도완료. ]")
                        print(f"매도시간 : {now}  |  코인명 : {coin5}  |  현재가 = ￦{price5}  |  20이평선가 = ￦{ma20_5}  |  보유수량 = {krw_balance5}  |  평가금액 = ￦{bp5}  |  매수가능 : {op_mode5} - 매수가능")
                        print("")

                    else:   # 보유코인 평가 금액이 10,100원 이하일때
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode5 = True

            # 1초 딜레이.
            time.sleep(1)
            ##### 5번 코인 매매 종료 #####
            #############################


            ###############################
            ##### 매매 : 6번코인 시작. #####
            # 코인 현재가 불러오기
            price6 = pyupbit.get_current_price(krw_coin6)
            # 이평선 조회.
            ma20_6 = get_ma20(krw_coin6)

            # 매수가능금액 불러오기
            krw6 = upbit.get_balance("KRW")

            # 20일 이평선 조건문
            if price6 > ma20_6:     # 20일이평선가격보다 현재가가 높을때는 매수
                if op_mode6 == True:    # 매수 가능(True)일 경우 - 매수시도
                    if krw6 > buy_krw:      # 매수가능금액 krw6 가 매수평균가 buy_krw 보다 클때
                        if krw6 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                            if buy_krw > 10100:     # 매수평균가 buy_krw 가 10,100원 초과일 경우 : 매수
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
                                print(f"매수시간 : {now}  |  코인명 : {coin6}  |  현재가 = ￦{price6}  |  20이평선가 = ￦{ma20_6}  |  보유수량 = {krw_balance6}  |  평가금액 = ￦{bp6}")
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

                            time.sleep(1)
                            # 보유수량 불러오기
                            krw_balance6 = upbit.get_balance(krw_coin6)
                            # 코인 현재가 불러오기
                            price6 = pyupbit.get_current_price(krw_coin6)
                            # 보유코인 원화금액으로 계산하기
                            bp6 = price6 * krw_balance6

                            # 보유 및 매수 가능 출력.
                            print(f"[ 6. {krw_coin6} 매수완료. ]")
                            print(f"매수시간 : {now}  |  코인명 : {coin6}  |  현재가 = ￦{price6}  |  20이평선가 = ￦{ma20_6}  |  보유수량 = {krw_balance6}  |  평가금액 = ￦{bp6}  |  매수가능 - {op_mode6} - 불가")
                            print("")

                        else:
                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode6 = False

                            print(f"[ 6. {krw_coin6} 잔고부족으로 매수안함. ]")
                            print(f"현재시간 : {now}  |  코인명 : {coin6}  |  현재매수가능 - {op_mode6} - 불가")
                            print("")

            elif price6 < ma20_6:       # 20일이평선보다 현재가가 낮을때는 매도
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
                        time.sleep(1)
                        # 보유수량 불러오기
                        krw_balance6 = upbit.get_balance(krw_coin6)
                        # 코인 현재가 불러오기
                        price6 = pyupbit.get_current_price(krw_coin6)
                        # 보유코인 원화금액으로 계산하기
                        bp6 = price6 * krw_balance6

                        # 보유 및 매수 가능 출력.
                        print(f"[ 6. {krw_coin6} 매도완료. ]")
                        print(f"매도시간 : {now}  |  코인명 : {coin6}  |  현재가 = ￦{price6}  |  20이평선가 = ￦{ma20_6}  |  보유수량 = {krw_balance6}  |  평가금액 = ￦{bp6}  |  매수가능 : {op_mode6} - 매수가능")
                        print("")

                    else:   # 보유코인 평가 금액이 10,100원 이하일때
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode6 = True

            # 1초 딜레이.
            time.sleep(1)
            ##### 6번 코인 매매 종료 #####
            #############################


            ###############################
            ##### 매매 : 7번코인 시작. #####
            # 코인 현재가 불러오기
            price7 = pyupbit.get_current_price(krw_coin7)
            # 이평선 조회.
            ma20_7 = get_ma20(krw_coin7)

            # 매수가능금액 불러오기
            krw7 = upbit.get_balance("KRW")

            # 20일 이평선 조건문
            if price7 > ma20_7:     # 20일이평선가격보다 현재가가 높을때는 매수
                if op_mode7 == True:    # 매수 가능(True)일 경우 - 매수시도
                    if krw7 > buy_krw:      # 매수가능금액 krw7 가 매수평균가 buy_krw 보다 클때
                        if krw7 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                            if buy_krw > 10100:     # 매수평균가 buy_krw 가 10,100원 초과일 경우 : 매수
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
                                print(f"매수시간 : {now}  |  코인명 : {coin7}  |  현재가 = ￦{price7}  |  20이평선가 = ￦{ma20_7}  |  보유수량 = {krw_balance7}  |  평가금액 = ￦{bp7}")
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

                            time.sleep(1)
                            # 보유수량 불러오기
                            krw_balance7 = upbit.get_balance(krw_coin7)
                            # 코인 현재가 불러오기
                            price7 = pyupbit.get_current_price(krw_coin7)
                            # 보유코인 원화금액으로 계산하기
                            bp7 = price7 * krw_balance7

                            # 보유 및 매수 가능 출력.
                            print(f"[ 7. {krw_coin7} 매수완료. ]")
                            print(f"매수시간 : {now}  |  코인명 : {coin7}  |  현재가 = ￦{price7}  |  20이평선가 = ￦{ma20_7}  |  보유수량 = {krw_balance7}  |  평가금액 = ￦{bp7}  |  매수가능 - {op_mode7} - 불가")
                            print("")

                        else:
                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode7 = False

                            print(f"[ 7. {krw_coin7} 잔고부족으로 매수안함. ]")
                            print(f"현재시간 : {now}  |  코인명 : {coin7}  |  현재매수가능 - {op_mode7} - 불가")
                            print("")

            elif price7 < ma20_7:       # 20일이평선보다 현재가가 낮을때는 매도
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
                        time.sleep(1)
                        # 보유수량 불러오기
                        krw_balance7 = upbit.get_balance(krw_coin7)
                        # 코인 현재가 불러오기
                        price7 = pyupbit.get_current_price(krw_coin7)
                        # 보유코인 원화금액으로 계산하기
                        bp7 = price7 * krw_balance7

                        # 보유 및 매수 가능 출력.
                        print(f"[ 7. {krw_coin7} 매도완료. ]")
                        print(f"매도시간 : {now}  |  코인명 : {coin7}  |  현재가 = ￦{price7}  |  20이평선가 = ￦{ma20_7}  |  보유수량 = {krw_balance7}  |  평가금액 = ￦{bp7}  |  매수가능 : {op_mode7} - 매수가능")
                        print("")

                    else:   # 보유코인 평가 금액이 10,100원 이하일때
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode7 = True

            # 1초 딜레이.
            time.sleep(1)
            ##### 7번 코인 매매 종료 #####
            #############################


            ###############################
            ##### 매매 : 8번코인 시작. #####
            # 코인 현재가 불러오기
            price8 = pyupbit.get_current_price(krw_coin8)
            # 이평선 조회.
            ma20_8 = get_ma20(krw_coin8)

            # 매수가능금액 불러오기
            krw8 = upbit.get_balance("KRW")

            # 20일 이평선 조건문
            if price8 > ma20_8:     # 20일이평선가격보다 현재가가 높을때는 매수
                if op_mode8 == True:    # 매수 가능(True)일 경우 - 매수시도
                    if krw8 > buy_krw:      # 매수가능금액 krw8 가 매수평균가 buy_krw 보다 클때
                        if krw8 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                            if buy_krw > 10100:     # 매수평균가 buy_krw 가 10,100원 초과일 경우 : 매수
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
                                print(f"매수시간 : {now}  |  코인명 : {coin8}  |  현재가 = ￦{price8}  |  20이평선가 = ￦{ma20_8}  |  보유수량 = {krw_balance8}  |  평가금액 = ￦{bp8}")
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

                            time.sleep(1)
                            # 보유수량 불러오기
                            krw_balance8 = upbit.get_balance(krw_coin8)
                            # 코인 현재가 불러오기
                            price8 = pyupbit.get_current_price(krw_coin8)
                            # 보유코인 원화금액으로 계산하기
                            bp8 = price8 * krw_balance8

                            # 보유 및 매수 가능 출력.
                            print(f"[ 8. {krw_coin8} 매수완료. ]")
                            print(f"매수시간 : {now}  |  코인명 : {coin8}  |  현재가 = ￦{price8}  |  20이평선가 = ￦{ma20_8}  |  보유수량 = {krw_balance8}  |  평가금액 = ￦{bp8}  |  매수가능 - {op_mode8} - 불가")
                            print("")

                        else:
                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode8 = False

                            print(f"[ 8. {krw_coin8} 잔고부족으로 매수안함. ]")
                            print(f"현재시간 : {now}  |  코인명 : {coin8}  |  현재매수가능 - {op_mode8} - 불가")
                            print("")

            elif price8 < ma20_8:       # 20일이평선보다 현재가가 낮을때는 매도
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
                        time.sleep(1)
                        # 보유수량 불러오기
                        krw_balance8 = upbit.get_balance(krw_coin8)
                        # 코인 현재가 불러오기
                        price8 = pyupbit.get_current_price(krw_coin8)
                        # 보유코인 원화금액으로 계산하기
                        bp8 = price8 * krw_balance8

                        # 보유 및 매수 가능 출력.
                        print(f"[ 8. {krw_coin8} 매도완료. ]")
                        print(f"매도시간 : {now}  |  코인명 : {coin8}  |  현재가 = ￦{price8}  |  20이평선가 = ￦{ma20_8}  |  보유수량 = {krw_balance8}  |  평가금액 = ￦{bp8}  |  매수가능 : {op_mode8} - 매수가능")
                        print("")

                    else:   # 보유코인 평가 금액이 10,100원 이하일때
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode8 = True

            # 1초 딜레이.
            time.sleep(1)
            ##### 8번 코인 매매 종료 #####
            #############################


            ###############################
            ##### 매매 : 9번코인 시작. #####
            # 코인 현재가 불러오기
            price9 = pyupbit.get_current_price(krw_coin9)
            # 이평선 조회.
            ma20_9 = get_ma20(krw_coin9)

            # 매수가능금액 불러오기
            krw9 = upbit.get_balance("KRW")

            # 20일 이평선 조건문
            if price9 > ma20_9:     # 20일이평선가격보다 현재가가 높을때는 매수
                if op_mode9 == True:    # 매수 가능(True)일 경우 - 매수시도
                    if krw9 > buy_krw:      # 매수가능금액 krw9 가 매수평균가 buy_krw 보다 클때
                        if krw9 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                            if buy_krw > 10100:     # 매수평균가 buy_krw 가 10,100원 초과일 경우 : 매수
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
                                print(f"매수시간 : {now}  |  코인명 : {coin9}  |  현재가 = ￦{price9}  |  20이평선가 = ￦{ma20_9}  |  보유수량 = {krw_balance9}  |  평가금액 = ￦{bp9}")
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

                            time.sleep(1)
                            # 보유수량 불러오기
                            krw_balance9 = upbit.get_balance(krw_coin9)
                            # 코인 현재가 불러오기
                            price9 = pyupbit.get_current_price(krw_coin9)
                            # 보유코인 원화금액으로 계산하기
                            bp9 = price9 * krw_balance9

                            # 보유 및 매수 가능 출력.
                            print(f"[ 9. {krw_coin9} 매수완료. ]")
                            print(f"매수시간 : {now}  |  코인명 : {coin9}  |  현재가 = ￦{price9}  |  20이평선가 = ￦{ma20_9}  |  보유수량 = {krw_balance9}  |  평가금액 = ￦{bp9}  |  매수가능 - {op_mode9} - 불가")
                            print("")

                        else:
                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode9 = False

                            print(f"[ 9. {krw_coin9} 잔고부족으로 매수안함. ]")
                            print(f"현재시간 : {now}  |  코인명 : {coin9}  |  현재매수가능 - {op_mode9} - 불가")
                            print("")

            elif price9 < ma20_9:       # 20일이평선보다 현재가가 낮을때는 매도
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
                        time.sleep(1)
                        # 보유수량 불러오기
                        krw_balance9 = upbit.get_balance(krw_coin9)
                        # 코인 현재가 불러오기
                        price9 = pyupbit.get_current_price(krw_coin9)
                        # 보유코인 원화금액으로 계산하기
                        bp9 = price9 * krw_balance9

                        # 보유 및 매수 가능 출력.
                        print(f"[ 9. {krw_coin9} 매도완료. ]")
                        print(f"매도시간 : {now}  |  코인명 : {coin9}  |  현재가 = ￦{price9}  |  20이평선가 = ￦{ma20_9}  |  보유수량 = {krw_balance9}  |  평가금액 = ￦{bp9}  |  매수가능 : {op_mode9} - 매수가능")
                        print("")

                    else:   # 보유코인 평가 금액이 10,100원 이하일때
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode9 = True

            # 1초 딜레이.
            time.sleep(1)
            ##### 9번 코인 매매 종료 #####
            #############################


            ###############################
            ##### 매매 : 10번코인 시작. #####
            # 코인 현재가 불러오기
            price10 = pyupbit.get_current_price(krw_coin10)
            # 이평선 조회.
            ma20_10 = get_ma20(krw_coin10)

            # 매수가능금액 불러오기
            krw10 = upbit.get_balance("KRW")

            # 20일 이평선 조건문
            if price10 > ma20_10:     # 20일이평선가격보다 현재가가 높을때는 매수
                if op_mode10 == True:    # 매수 가능(True)일 경우 - 매수시도
                    if krw10 > buy_krw:      # 매수가능금액 krw10 가 매수평균가 buy_krw 보다 클때
                        if krw10 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                            if buy_krw > 10100:     # 매수평균가 buy_krw 가 10,100원 초과일 경우 : 매수
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
                                print(f"매수시간 : {now}  |  코인명 : {coin10}  |  현재가 = ￦{price10}  |  20이평선가 = ￦{ma20_10}  |  보유수량 = {krw_balance10}  |  평가금액 = ￦{bp10}")
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

                        time.sleep(1)
                        # 보유수량 불러오기
                        krw_balance10 = upbit.get_balance(krw_coin10)
                        # 코인 현재가 불러오기
                        price10 = pyupbit.get_current_price(krw_coin10)
                        # 보유코인 원화금액으로 계산하기
                        bp10 = price10 * krw_balance10

                        # 보유 및 매수 가능 출력.
                        print(f"[ 10. {krw_coin10} 매수완료. ]")
                        print(f"매수시간 : {now}  |  코인명 : {coin10}  |  현재가 = ￦{price10}  |  20이평선가 = ￦{ma20_10}  |  보유수량 = {krw_balance10}  |  평가금액 = ￦{bp10}  |  매수가능 - {op_mode10} - 불가")
                        print("")

                    else:
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode10 = False

                        print(f"[ 10. {krw_coin10} 잔고부족으로 매수안함. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin10}  |  현재매수가능 - {op_mode10} - 불가")
                        print("")

            elif price10 < ma20_10:       # 20일이평선보다 현재가가 낮을때는 매도
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
                        time.sleep(1)
                        # 보유수량 불러오기
                        krw_balance10 = upbit.get_balance(krw_coin10)
                        # 코인 현재가 불러오기
                        price10 = pyupbit.get_current_price(krw_coin10)
                        # 보유코인 원화금액으로 계산하기
                        bp10 = price10 * krw_balance10

                        # 보유 및 매수 가능 출력.
                        print(f"[ 10. {krw_coin10} 매도완료. ]")
                        print(f"매도시간 : {now}  |  코인명 : {coin10}  |  현재가 = ￦{price10}  |  20이평선가 = ￦{ma20_10}  |  보유수량 = {krw_balance10}  |  평가금액 = ￦{bp10}  |  매수가능 : {op_mode10} - 매수가능")
                        print("")

                    else:   # 보유코인 평가 금액이 10,100원 이하일때
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode10 = True

            # 1초 딜레이.
            time.sleep(1)
            ##### 10번 코인 매매 종료 #####
            #############################


            ######################################################################################################################################################
            ######################################################################################################################################################
            ######################################################################################################################################################
            ######################################################################################################################################################
            ######################################################################################################################################################


            ###############################
            ##### 매매 : 11번코인 시작. #####
            # 코인 현재가 불러오기
            price11 = pyupbit.get_current_price(krw_coin11)
            # 이평선 조회.
            ma20_11 = get_ma20(krw_coin11)

            # 매수가능금액 불러오기
            krw11 = upbit.get_balance("KRW")

            # 20일 이평선 조건문
            if price11 > ma20_11:     # 20일이평선가격보다 현재가가 높을때는 매수
                if op_mode11 == True:    # 매수 가능(True)일 경우 - 매수시도
                    if krw11 > buy_krw:      # 매수가능금액 krw11 가 매수평균가 buy_krw 보다 클때
                        if krw11 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                            if buy_krw > 10100:     # 매수평균가 buy_krw 가 10,100원 초과일 경우 : 매수
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
                                print(f"매수시간 : {now}  |  코인명 : {coin11}  |  현재가 = ￦{price11}  |  20이평선가 = ￦{ma20_11}  |  보유수량 = {krw_balance11}  |  평가금액 = ￦{bp11}")
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
                            # 매수금액은 매수가능금액인 krw11 로
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
                            print(f"매수시간 : {now}  |  코인명 : {coin11}  |  현재가 = ￦{price11}  |  20이평선가 = ￦{ma20_11}  |  보유수량 = {krw_balance11}  |  평가금액 = ￦{bp11}  |  매수가능 - {op_mode11} - 불가")
                            print("")

                        else:
                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode11 = False

                            print(f"[ 11. {krw_coin11} 잔고부족으로 매수안함. ]")
                            print(f"현재시간 : {now}  |  코인명 : {coin11}  |  현재매수가능 - {op_mode11} - 불가")
                            print("")

            elif price11 < ma20_11:       # 20일이평선보다 현재가가 낮을때는 매도
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
                        time.sleep(1)
                        # 보유수량 불러오기
                        krw_balance11 = upbit.get_balance(krw_coin11)
                        # 코인 현재가 불러오기
                        price11 = pyupbit.get_current_price(krw_coin11)
                        # 보유코인 원화금액으로 계산하기
                        bp11 = price11 * krw_balance11

                        # 보유 및 매수 가능 출력.
                        print(f"[ 11. {krw_coin11} 매도완료. ]")
                        print(f"매도시간 : {now}  |  코인명 : {coin11}  |  현재가 = ￦{price11}  |  20이평선가 = ￦{ma20_11}  |  보유수량 = {krw_balance11}  |  평가금액 = ￦{bp11}  |  매수가능 : {op_mode11} - 매수가능")
                        print("")

                    else:   # 보유코인 평가 금액이 10,100원 이하일때
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode11 = True

            # 1초 딜레이.
            time.sleep(1)
            ##### 11번 코인 매매 종료 #####
            #############################

            ###############################
            ##### 매매 : 12번코인 시작. #####
            # 코인 현재가 불러오기
            price12 = pyupbit.get_current_price(krw_coin12)
            # 이평선 조회.
            ma20_12 = get_ma20(krw_coin12)

            # 매수가능금액 불러오기
            krw12 = upbit.get_balance("KRW")

            # 20일 이평선 조건문
            if price12 > ma20_12:     # 20일이평선가격보다 현재가가 높을때는 매수
                if op_mode12 == True:    # 매수 가능(True)일 경우 - 매수시도
                    if krw12 > buy_krw:      # 매수가능금액 krw12 가 매수평균가 buy_krw 보다 클때
                        if krw12 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                            if buy_krw > 10100:     # 매수평균가 buy_krw 가 10,100원 초과일 경우 : 매수
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
                                print(f"매수시간 : {now}  |  코인명 : {coin12}  |  현재가 = ￦{price12}  |  20이평선가 = ￦{ma20_12}  |  보유수량 = {krw_balance12}  |  평가금액 = ￦{bp12}")
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
                            print(f"매수시간 : {now}  |  코인명 : {coin12}  |  현재가 = ￦{price12}  |  20이평선가 = ￦{ma20_12}  |  보유수량 = {krw_balance12}  |  평가금액 = ￦{bp12}  |  매수가능 - {op_mode12} - 불가")
                            print("")

                        else:
                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode12 = False

                            print(f"[ 12. {krw_coin12} 잔고부족으로 매수안함. ]")
                            print(f"현재시간 : {now}  |  코인명 : {coin12}  |  현재매수가능 - {op_mode12} - 불가")
                            print("")

            elif price12 < ma20_12:       # 20일이평선보다 현재가가 낮을때는 매도
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
                        time.sleep(1)
                        # 보유수량 불러오기
                        krw_balance12 = upbit.get_balance(krw_coin12)
                        # 코인 현재가 불러오기
                        price12 = pyupbit.get_current_price(krw_coin12)
                        # 보유코인 원화금액으로 계산하기
                        bp12 = price12 * krw_balance12

                        # 보유 및 매수 가능 출력.
                        print(f"[ 12. {krw_coin12} 매도완료. ]")
                        print(f"매도시간 : {now}  |  코인명 : {coin12}  |  현재가 = ￦{price12}  |  20이평선가 = ￦{ma20_12}  |  보유수량 = {krw_balance12}  |  평가금액 = ￦{bp12}  |  매수가능 : {op_mode12} - 매수가능")
                        print("")

                    else:   # 보유코인 평가 금액이 10,100원 이하일때
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode12 = True

            # 1초 딜레이.
            time.sleep(1)
            ##### 12번 코인 매매 종료 #####
            #############################


            ###############################
            ##### 매매 : 13번코인 시작. #####
            # 코인 현재가 불러오기
            price13 = pyupbit.get_current_price(krw_coin13)
            # 이평선 조회.
            ma20_13 = get_ma20(krw_coin13)

            # 매수가능금액 불러오기
            krw13 = upbit.get_balance("KRW")

            # 20일 이평선 조건문
            if price13 > ma20_13:     # 20일이평선가격보다 현재가가 높을때는 매수
                if op_mode13 == True:    # 매수 가능(True)일 경우 - 매수시도
                    if krw13 > buy_krw:      # 매수가능금액 krw13 가 매수평균가 buy_krw 보다 클때
                        if krw13 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                            if buy_krw > 10100:     # 매수평균가 buy_krw 가 10,100원 초과일 경우 : 매수
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
                                print(f"매수시간 : {now}  |  코인명 : {coin13}  |  현재가 = ￦{price13}  |  20이평선가 = ￦{ma20_13}  |  보유수량 = {krw_balance13}  |  평가금액 = ￦{bp13}")
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

                            time.sleep(1)
                            # 보유수량 불러오기
                            krw_balance13 = upbit.get_balance(krw_coin13)
                            # 코인 현재가 불러오기
                            price13 = pyupbit.get_current_price(krw_coin13)
                            # 보유코인 원화금액으로 계산하기
                            bp13 = price13 * krw_balance13

                            # 보유 및 매수 가능 출력.
                            print(f"[ 13. {krw_coin13} 매수완료. ]")
                            print(f"매수시간 : {now}  |  코인명 : {coin13}  |  현재가 = ￦{price13}  |  20이평선가 = ￦{ma20_13}  |  보유수량 = {krw_balance13}  |  평가금액 = ￦{bp13}  |  매수가능 - {op_mode13} - 불가")
                            print("")

                        else:
                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode13 = False

                            print(f"[ 13. {krw_coin13} 잔고부족으로 매수안함. ]")
                            print(f"현재시간 : {now}  |  코인명 : {coin13}  |  현재매수가능 - {op_mode13} - 불가")
                            print("")

            elif price13 < ma20_13:       # 20일이평선보다 현재가가 낮을때는 매도
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
                        time.sleep(1)
                        # 보유수량 불러오기
                        krw_balance13 = upbit.get_balance(krw_coin13)
                        # 코인 현재가 불러오기
                        price13 = pyupbit.get_current_price(krw_coin13)
                        # 보유코인 원화금액으로 계산하기
                        bp13 = price13 * krw_balance13

                        # 보유 및 매수 가능 출력.
                        print(f"[ 13. {krw_coin13} 매도완료. ]")
                        print(f"매도시간 : {now}  |  코인명 : {coin13}  |  현재가 = ￦{price13}  |  20이평선가 = ￦{ma20_13}  |  보유수량 = {krw_balance13}  |  평가금액 = ￦{bp13}  |  매수가능 : {op_mode13} - 매수가능")
                        print("")

                    else:   # 보유코인 평가 금액이 10,100원 이하일때
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode13 = True

            # 1초 딜레이.
            time.sleep(1)
            ##### 13번 코인 매매 종료 #####
            #############################


            ###############################
            ##### 매매 : 14번코인 시작. #####
            # 코인 현재가 불러오기
            price14 = pyupbit.get_current_price(krw_coin14)
            # 이평선 조회.
            ma20_14 = get_ma20(krw_coin14)

            # 매수가능금액 불러오기
            krw14 = upbit.get_balance("KRW")

            # 20일 이평선 조건문
            if price14 > ma20_14:     # 20일이평선가격보다 현재가가 높을때는 매수
                if op_mode14 == True:    # 매수 가능(True)일 경우 - 매수시도
                    if krw14 > buy_krw:      # 매수가능금액 krw14 가 매수평균가 buy_krw 보다 클때
                        if krw14 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                            if buy_krw > 10100:     # 매수평균가 buy_krw 가 10,100원 초과일 경우 : 매수
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
                                print(f"매수시간 : {now}  |  코인명 : {coin14}  |  현재가 = ￦{price14}  |  20이평선가 = ￦{ma20_14}  |  보유수량 = {krw_balance14}  |  평가금액 = ￦{bp14}")
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

                            time.sleep(1)
                            # 보유수량 불러오기
                            krw_balance14 = upbit.get_balance(krw_coin14)
                            # 코인 현재가 불러오기
                            price14 = pyupbit.get_current_price(krw_coin14)
                            # 보유코인 원화금액으로 계산하기
                            bp14 = price14 * krw_balance14

                            # 보유 및 매수 가능 출력.
                            print(f"[ 14. {krw_coin14} 매수완료. ]")
                            print(f"매수시간 : {now}  |  코인명 : {coin14}  |  현재가 = ￦{price14}  |  20이평선가 = ￦{ma20_14}  |  보유수량 = {krw_balance14}  |  평가금액 = ￦{bp14}  |  매수가능 - {op_mode14} - 불가")
                            print("")

                        else:
                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode14 = False

                            print(f"[ 14. {krw_coin14} 잔고부족으로 매수안함. ]")
                            print(f"현재시간 : {now}  |  코인명 : {coin14}  |  현재매수가능 - {op_mode14} - 불가")
                            print("")

            elif price14 < ma20_14:       # 20일이평선보다 현재가가 낮을때는 매도
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
                        time.sleep(1)
                        # 보유수량 불러오기
                        krw_balance14 = upbit.get_balance(krw_coin14)
                        # 코인 현재가 불러오기
                        price14 = pyupbit.get_current_price(krw_coin14)
                        # 보유코인 원화금액으로 계산하기
                        bp14 = price14 * krw_balance14

                        # 보유 및 매수 가능 출력.
                        print(f"[ 14. {krw_coin14} 매도완료. ]")
                        print(f"매도시간 : {now}  |  코인명 : {coin14}  |  현재가 = ￦{price14}  |  20이평선가 = ￦{ma20_14}  |  보유수량 = {krw_balance14}  |  평가금액 = ￦{bp14}  |  매수가능 : {op_mode14} - 매수가능")
                        print("")

                    else:   # 보유코인 평가 금액이 10,100원 이하일때
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode14 = True

            # 1초 딜레이.
            time.sleep(1)
            ##### 14번 코인 매매 종료 #####
            #############################


            ###############################
            ##### 매매 : 15번코인 시작. #####
            # 코인 현재가 불러오기
            price15 = pyupbit.get_current_price(krw_coin15)
            # 이평선 조회.
            ma20_15 = get_ma20(krw_coin15)

            # 매수가능금액 불러오기
            krw15 = upbit.get_balance("KRW")

            # 20일 이평선 조건문
            if price15 > ma20_15:     # 20일이평선가격보다 현재가가 높을때는 매수
                if op_mode15 == True:    # 매수 가능(True)일 경우 - 매수시도
                    if krw15 > buy_krw:      # 매수가능금액 krw15 가 매수평균가 buy_krw 보다 클때
                        if krw15 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                            if buy_krw > 10100:     # 매수평균가 buy_krw 가 10,100원 초과일 경우 : 매수
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
                                print(f"매수시간 : {now}  |  코인명 : {coin15}  |  현재가 = ￦{price15}  |  20이평선가 = ￦{ma20_15}  |  보유수량 = {krw_balance15}  |  평가금액 = ￦{bp15}")
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

                            time.sleep(1)
                            # 보유수량 불러오기
                            krw_balance15 = upbit.get_balance(krw_coin15)
                            # 코인 현재가 불러오기
                            price15 = pyupbit.get_current_price(krw_coin15)
                            # 보유코인 원화금액으로 계산하기
                            bp15 = price15 * krw_balance15

                            # 보유 및 매수 가능 출력.
                            print(f"[ 15. {krw_coin15} 매수완료. ]")
                            print(f"매수시간 : {now}  |  코인명 : {coin15}  |  현재가 = ￦{price15}  |  20이평선가 = ￦{ma20_15}  |  보유수량 = {krw_balance15}  |  평가금액 = ￦{bp15}  |  매수가능 - {op_mode15} - 불가")
                            print("")

                        else:
                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode15 = False

                            print(f"[ 15. {krw_coin15} 잔고부족으로 매수안함. ]")
                            print(f"현재시간 : {now}  |  코인명 : {coin15}  |  현재매수가능 - {op_mode15} - 불가")
                            print("")

            elif price15 < ma20_15:       # 20일이평선보다 현재가가 낮을때는 매도
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
                        time.sleep(1)
                        # 보유수량 불러오기
                        krw_balance15 = upbit.get_balance(krw_coin15)
                        # 코인 현재가 불러오기
                        price15 = pyupbit.get_current_price(krw_coin15)
                        # 보유코인 원화금액으로 계산하기
                        bp15 = price15 * krw_balance15

                        # 보유 및 매수 가능 출력.
                        print(f"[ 15. {krw_coin15} 매도완료. ]")
                        print(f"매도시간 : {now}  |  코인명 : {coin15}  |  현재가 = ￦{price15}  |  20이평선가 = ￦{ma20_15}  |  보유수량 = {krw_balance15}  |  평가금액 = ￦{bp15}  |  매수가능 : {op_mode15} - 매수가능")
                        print("")

                    else:   # 보유코인 평가 금액이 10,100원 이하일때
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode15 = True

            # 1초 딜레이.
            time.sleep(1)
            ##### 15번 코인 매매 종료 #####
            #############################


            ###############################
            ##### 매매 : 16번코인 시작. #####
            # 코인 현재가 불러오기
            price16 = pyupbit.get_current_price(krw_coin16)
            # 이평선 조회.
            ma20_16 = get_ma20(krw_coin16)

            # 매수가능금액 불러오기
            krw16 = upbit.get_balance("KRW")

            # 20일 이평선 조건문
            if price16 > ma20_16:     # 20일이평선가격보다 현재가가 높을때는 매수
                if op_mode16 == True:    # 매수 가능(True)일 경우 - 매수시도
                    if krw16 > buy_krw:      # 매수가능금액 krw16 가 매수평균가 buy_krw 보다 클때
                        if krw16 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                            if buy_krw > 10100:     # 매수평균가 buy_krw 가 10,100원 초과일 경우 : 매수
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
                                print(f"매수시간 : {now}  |  코인명 : {coin16}  |  현재가 = ￦{price16}  |  20이평선가 = ￦{ma20_16}  |  보유수량 = {krw_balance16}  |  평가금액 = ￦{bp16}")
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

                            time.sleep(1)
                            # 보유수량 불러오기
                            krw_balance16 = upbit.get_balance(krw_coin16)
                            # 코인 현재가 불러오기
                            price16 = pyupbit.get_current_price(krw_coin16)
                            # 보유코인 원화금액으로 계산하기
                            bp16 = price16 * krw_balance16

                            # 보유 및 매수 가능 출력.
                            print(f"[ 16. {krw_coin16} 매수완료. ]")
                            print(f"매수시간 : {now}  |  코인명 : {coin16}  |  현재가 = ￦{price16}  |  20이평선가 = ￦{ma20_16}  |  보유수량 = {krw_balance16}  |  평가금액 = ￦{bp16}  |  매수가능 - {op_mode16} - 불가")
                            print("")

                        else:
                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode16 = False

                            print(f"[ 16. {krw_coin16} 잔고부족으로 매수안함. ]")
                            print(f"현재시간 : {now}  |  코인명 : {coin16}  |  현재매수가능 - {op_mode16} - 불가")
                            print("")

            elif price16 < ma20_16:       # 20일이평선보다 현재가가 낮을때는 매도
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
                        time.sleep(1)
                        # 보유수량 불러오기
                        krw_balance16 = upbit.get_balance(krw_coin16)
                        # 코인 현재가 불러오기
                        price16 = pyupbit.get_current_price(krw_coin16)
                        # 보유코인 원화금액으로 계산하기
                        bp16 = price16 * krw_balance16

                        # 보유 및 매수 가능 출력.
                        print(f"[ 16. {krw_coin16} 매도완료. ]")
                        print(f"매도시간 : {now}  |  코인명 : {coin16}  |  현재가 = ￦{price16}  |  20이평선가 = ￦{ma20_16}  |  보유수량 = {krw_balance16}  |  평가금액 = ￦{bp16}  |  매수가능 : {op_mode16} - 매수가능")
                        print("")

                    else:   # 보유코인 평가 금액이 10,100원 이하일때
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode16 = True

            # 1초 딜레이.
            time.sleep(1)
            ##### 16번 코인 매매 종료 #####
            #############################


            ###############################
            ##### 매매 : 17번코인 시작. #####
            # 코인 현재가 불러오기
            price17 = pyupbit.get_current_price(krw_coin17)
            # 이평선 조회.
            ma20_17 = get_ma20(krw_coin17)

            # 매수가능금액 불러오기
            krw17 = upbit.get_balance("KRW")

            # 20일 이평선 조건문
            if price17 > ma20_17:     # 20일이평선가격보다 현재가가 높을때는 매수
                if op_mode17 == True:    # 매수 가능(True)일 경우 - 매수시도
                    if krw17 > buy_krw:      # 매수가능금액 krw17 가 매수평균가 buy_krw 보다 클때
                        if krw17 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                            if buy_krw > 10100:     # 매수평균가 buy_krw  10,100원 초과일 경우 : 매수
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
                                print(f"매수시간 : {now}  |  코인명 : {coin17}  |  현재가 = ￦{price17}  |  20이평선가 = ￦{ma20_17}  |  보유수량 = {krw_balance17}  |  평가금액 = ￦{bp17}")
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

                            time.sleep(1)
                            # 보유수량 불러오기
                            krw_balance17 = upbit.get_balance(krw_coin17)
                            # 코인 현재가 불러오기
                            price17 = pyupbit.get_current_price(krw_coin17)
                            # 보유코인 원화금액으로 계산하기
                            bp17 = price17 * krw_balance17

                            # 보유 및 매수 가능 출력.
                            print(f"[ 17. {krw_coin17} 매수완료. ]")
                            print(f"매수시간 : {now}  |  코인명 : {coin17}  |  현재가 = ￦{price17}  |  20이평선가 = ￦{ma20_17}  |  보유수량 = {krw_balance17}  |  평가금액 = ￦{bp17}  |  매수가능 - {op_mode17} - 불가")
                            print("")

                        else:
                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode17 = False

                            print(f"[ 17. {krw_coin17} 잔고부족으로 매수안함. ]")
                            print(f"현재시간 : {now}  |  코인명 : {coin17}  |  현재매수가능 - {op_mode17} - 불가")
                            print("")

            elif price17 < ma20_17:       # 20일이평선보다 현재가가 낮을때는 매도
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
                        time.sleep(1)
                        # 보유수량 불러오기
                        krw_balance17 = upbit.get_balance(krw_coin17)
                        # 코인 현재가 불러오기
                        price17 = pyupbit.get_current_price(krw_coin17)
                        # 보유코인 원화금액으로 계산하기
                        bp17 = price17 * krw_balance17

                        # 보유 및 매수 가능 출력.
                        print(f"[ 17. {krw_coin17} 매도완료. ]")
                        print(f"매도시간 : {now}  |  코인명 : {coin17}  |  현재가 = ￦{price17}  |  20이평선가 = ￦{ma20_17}  |  보유수량 = {krw_balance17}  |  평가금액 = ￦{bp17}  |  매수가능 : {op_mode17} - 매수가능")
                        print("")

                else:   # 보유코인 평가 금액이 10,100원 이하일때
                    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                    op_mode17 = True

            # 1초 딜레이.
            time.sleep(1)
            ##### 17번 코인 매매 종료 #####
            #############################


            ###############################
            ##### 매매 : 18번코인 시작. #####
            # 코인 현재가 불러오기
            price18 = pyupbit.get_current_price(krw_coin18)
            # 이평선 조회.
            ma20_18 = get_ma20(krw_coin18)

            # 매수가능금액 불러오기
            krw18 = upbit.get_balance("KRW")

            # 20일 이평선 조건문
            if price18 > ma20_18:     # 20일이평선가격보다 현재가가 높을때는 매수
                if op_mode18 == True:    # 매수 가능(True)일 경우 - 매수시도
                    if krw18 > buy_krw:      # 매수가능금액 krw18 가 매수평균가 buy_krw 보다 클때
                        if krw18 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                            if buy_krw > 10100:     # 매수평균가 buy_krw 가 10,100원 초과일 경우 : 매수
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
                                print(f"매수시간 : {now}  |  코인명 : {coin18}  |  현재가 = ￦{price18}  |  20이평선가 = ￦{ma20_18}  |  보유수량 = {krw_balance18}  |  평가금액 = ￦{bp18}")
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

                            time.sleep(1)
                            # 보유수량 불러오기
                            krw_balance18 = upbit.get_balance(krw_coin18)
                            # 코인 현재가 불러오기
                            price18 = pyupbit.get_current_price(krw_coin18)
                            # 보유코인 원화금액으로 계산하기
                            bp18 = price18 * krw_balance18

                            # 보유 및 매수 가능 출력.
                            print(f"[ 18. {krw_coin18} 매수완료. ]")
                            print(f"매수시간 : {now}  |  코인명 : {coin18}  |  현재가 = ￦{price18}  |  20이평선가 = ￦{ma20_18}  |  보유수량 = {krw_balance18}  |  평가금액 = ￦{bp18}  |  매수가능 - {op_mode18} - 불가")
                            print("")

                        else:
                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode18 = False

                            print(f"[ 18. {krw_coin18} 잔고부족으로 매수안함. ]")
                            print(f"현재시간 : {now}  |  코인명 : {coin18}  |  현재매수가능 - {op_mode18} - 불가")
                            print("")

            elif price18 < ma20_18:       # 20일이평선보다 현재가가 낮을때는 매도
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
                        time.sleep(1)
                        # 보유수량 불러오기
                        krw_balance18 = upbit.get_balance(krw_coin18)
                        # 코인 현재가 불러오기
                        price18 = pyupbit.get_current_price(krw_coin18)
                        # 보유코인 원화금액으로 계산하기
                        bp18 = price18 * krw_balance18

                        # 보유 및 매수 가능 출력.
                        print(f"[ 18. {krw_coin18} 매도완료. ]")
                        print(f"매도시간 : {now}  |  코인명 : {coin18}  |  현재가 = ￦{price18}  |  20이평선가 = ￦{ma20_18}  |  보유수량 = {krw_balance18}  |  평가금액 = ￦{bp18}  |  매수가능 : {op_mode18} - 매수가능")
                        print("")

                    else:   # 보유코인 평가 금액이 10,100원 이하일때
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode18 = True

            # 1초 딜레이.
            time.sleep(1)
            ##### 18번 코인 매매 종료 #####
            #############################


            ###############################
            ##### 매매 : 19번코인 시작. #####
            # 코인 현재가 불러오기
            price19 = pyupbit.get_current_price(krw_coin19)
            # 이평선 조회.
            ma20_19 = get_ma20(krw_coin19)

            # 매수가능금액 불러오기
            krw19 = upbit.get_balance("KRW")

            # 20일 이평선 조건문
            if price19 > ma20_19:     # 20일이평선가격보다 현재가가 높을때는 매수
                if op_mode19 == True:    # 매수 가능(True)일 경우 - 매수시도
                    if krw19 > buy_krw:      # 매수가능금액 krw19 가 매수평균가 buy_krw 보다 클때
                        if krw19 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                            if buy_krw > 10100:     # 매수평균가 buy_krw 가 10,100원 초과일 경우 : 매수
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
                                print(f"매수시간 : {now}  |  코인명 : {coin19}  |  현재가 = ￦{price19}  |  20이평선가 = ￦{ma20_19}  |  보유수량 = {krw_balance19}  |  평가금액 = ￦{bp19}")
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

                            time.sleep(1)
                            # 보유수량 불러오기
                            krw_balance19 = upbit.get_balance(krw_coin19)
                            # 코인 현재가 불러오기
                            price19 = pyupbit.get_current_price(krw_coin19)
                            # 보유코인 원화금액으로 계산하기
                            bp19 = price19 * krw_balance19

                            # 보유 및 매수 가능 출력.
                            print(f"[ 19. {krw_coin19} 매수완료. ]")
                            print(f"매수시간 : {now}  |  코인명 : {coin19}  |  현재가 = ￦{price19}  |  20이평선가 = ￦{ma20_19}  |  보유수량 = {krw_balance19}  |  평가금액 = ￦{bp19}  |  매수가능 - {op_mode19} - 불가")
                            print("")

                        else:
                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode19 = False

                            print(f"[ 19. {krw_coin19} 잔고부족으로 매수안함. ]")
                            print(f"현재시간 : {now}  |  코인명 : {coin19}  |  현재매수가능 - {op_mode19} - 불가")
                            print("")

            elif price19 < ma20_19:       # 20일이평선보다 현재가가 낮을때는 매도
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
                        time.sleep(1)
                        # 보유수량 불러오기
                        krw_balance19 = upbit.get_balance(krw_coin19)
                        # 코인 현재가 불러오기
                        price19 = pyupbit.get_current_price(krw_coin19)
                        # 보유코인 원화금액으로 계산하기
                        bp19 = price19 * krw_balance19

                        # 보유 및 매수 가능 출력.
                        print(f"[ 19. {krw_coin19} 매도완료. ]")
                        print(f"매도시간 : {now}  |  코인명 : {coin19}  |  현재가 = ￦{price19}  |  20이평선가 = ￦{ma20_19}  |  보유수량 = {krw_balance19}  |  평가금액 = ￦{bp19}  |  매수가능 : {op_mode19} - 매수가능")
                        print("")

                    else:   # 보유코인 평가 금액이 10,100원 이하일때
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode19 = True

            # 1초 딜레이.
            time.sleep(1)
            ##### 19번 코인 매매 종료 #####
            #############################


            ###############################
            ##### 매매 : 20번코인 시작. #####
            # 코인 현재가 불러오기
            price20 = pyupbit.get_current_price(krw_coin20)
            # 이평선 조회.
            ma20_20 = get_ma20(krw_coin20)

            # 매수가능금액 불러오기
            krw20 = upbit.get_balance("KRW")

            # 20일 이평선 조건문
            if price20 > ma20_20:     # 20일이평선가격보다 현재가가 높을때는 매수
                if op_mode20 == True:    # 매수 가능(True)일 경우 - 매수시도
                    if krw20 > buy_krw:      # 매수가능금액 krw20 가 매수평균가 buy_krw 보다 클때
                        if krw20 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                            if buy_krw > 10100:     # 매수평균가 buy_krw 가 10,100원 초과일 경우 : 매수
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
                                print(f"매수시간 : {now}  |  코인명 : {coin20}  |  현재가 = ￦{price20}  |  20이평선가 = ￦{ma20_20}  |  보유수량 = {krw_balance20}  |  평가금액 = ￦{bp20}")
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
                            print(f"매수시간 : {now}  |  코인명 : {coin20}  |  현재가 = ￦{price20}  |  20이평선가 = ￦{ma20_20}  |  보유수량 = {krw_balance20}  |  평가금액 = ￦{bp20}  |  매수가능 - {op_mode20} - 불가")
                            print("")

                        else:
                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode20 = False

                            print(f"[ 20. {krw_coin20} 잔고부족으로 매수안함. ]")
                            print(f"현재시간 : {now}  |  코인명 : {coin20}  |  현재매수가능 - {op_mode20} - 불가")
                            print("")

            elif price20 < ma20_20:       # 20일이평선보다 현재가가 낮을때는 매도
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
                        time.sleep(1)
                        # 보유수량 불러오기
                        krw_balance20 = upbit.get_balance(krw_coin20)
                        # 코인 현재가 불러오기
                        price20 = pyupbit.get_current_price(krw_coin20)
                        # 보유코인 원화금액으로 계산하기
                        bp20 = price20 * krw_balance20

                        # 보유 및 매수 가능 출력.
                        print(f"[ 20. {krw_coin20} 매도완료. ]")
                        print(f"매도시간 : {now}  |  코인명 : {coin20}  |  현재가 = ￦{price20}  |  20이평선가 = ￦{ma20_20}  |  보유수량 = {krw_balance20}  |  평가금액 = ￦{bp20}  |  매수가능 : {op_mode20} - 매수가능")
                        print("")

                    else:   # 보유코인 평가 금액이 10,100원 이하일때
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode20 = True

            # 1초 딜레이.
            time.sleep(1)
            ##### 20번 코인 매매 종료 #####
            #############################


            ######################################################################################################################################################
            ######################################################################################################################################################
            ######################################################################################################################################################
            ######################################################################################################################################################
            ######################################################################################################################################################


            ###############################
            ##### 매매 : 21번코인 시작. #####
            # 코인 현재가 불러오기
            price21 = pyupbit.get_current_price(krw_coin21)
            # 이평선 조회.
            ma20_21 = get_ma20(krw_coin21)

            # 매수가능금액 불러오기
            krw21 = upbit.get_balance("KRW")

            # 20일 이평선 조건문
            if price21 > ma20_21:     # 20일이평선가격보다 현재가가 높을때는 매수
                if op_mode21 == True:    # 매수 가능(True)일 경우 - 매수시도
                    if krw21 > buy_krw:      # 매수가능금액 krw21 가 매수평균가 buy_krw 보다 클때
                        if krw21 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                            if buy_krw > 10100:     # 매수평균가 buy_krw 가 10,100원 초과일 경우 : 매수
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
                                print(f"매수시간 : {now}  |  코인명 : {coin21}  |  현재가 = ￦{price21}  |  20이평선가 = ￦{ma20_21}  |  보유수량 = {krw_balance21}  |  평가금액 = ￦{bp21}")
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
                            print(f"매수시간 : {now}  |  코인명 : {coin21}  |  현재가 = ￦{price21}  |  20이평선가 = ￦{ma20_21}  |  보유수량 = {krw_balance21}  |  평가금액 = ￦{bp21}  |  매수가능 - {op_mode21} - 불가")
                            print("")

                        else:
                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode21 = False

                            print(f"[ 21. {krw_coin21} 잔고부족으로 매수안함. ]")
                            print(f"현재시간 : {now}  |  코인명 : {coin21}  |  현재매수가능 - {op_mode21} - 불가")
                            print("")

            elif price21 < ma20_21:       # 20일이평선보다 현재가가 낮을때는 매도
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
                        time.sleep(1)
                        # 보유수량 불러오기
                        krw_balance21 = upbit.get_balance(krw_coin21)
                        # 코인 현재가 불러오기
                        price21 = pyupbit.get_current_price(krw_coin21)
                        # 보유코인 원화금액으로 계산하기
                        bp21 = price21 * krw_balance21

                        # 보유 및 매수 가능 출력.
                        print(f"[ 21. {krw_coin21} 매도완료. ]")
                        print(f"매도시간 : {now}  |  코인명 : {coin21}  |  현재가 = ￦{price21}  |  20이평선가 = ￦{ma20_21}  |  보유수량 = {krw_balance21}  |  평가금액 = ￦{bp21}  |  매수가능 : {op_mode21} - 매수가능")
                        print("")

                    else:   # 보유코인 평가 금액이 10,100원 이하일때
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode21 = True

            # 1초 딜레이.
            time.sleep(1)
            ##### 21번 코인 매매 종료 #####
            #############################


            ###############################
            ##### 매매 : 22번코인 시작. #####
            # 코인 현재가 불러오기
            price22 = pyupbit.get_current_price(krw_coin22)
            # 이평선 조회.
            ma20_22 = get_ma20(krw_coin22)

            # 매수가능금액 불러오기
            krw22 = upbit.get_balance("KRW")

            # 20일 이평선 조건문
            if price22 > ma20_22:     # 20일이평선가격보다 현재가가 높을때는 매수
                if op_mode22 == True:    # 매수 가능(True)일 경우 - 매수시도
                    if krw22 > buy_krw:      # 매수가능금액 krw22 가 매수평균가 buy_krw 보다 클때
                        if krw22 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                            if buy_krw > 10100:     # 매수평균가 buy_krw 가 10,100원 초과일 경우 : 매수
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
                                print(f"매수시간 : {now}  |  코인명 : {coin22}  |  현재가 = ￦{price22}  |  20이평선가 = ￦{ma20_22}  |  보유수량 = {krw_balance22}  |  평가금액 = ￦{bp22}")
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
                            print(f"매수시간 : {now}  |  코인명 : {coin22}  |  현재가 = ￦{price22}  |  20이평선가 = ￦{ma20_22}  |  보유수량 = {krw_balance22}  |  평가금액 = ￦{bp22}  |  매수가능 - {op_mode22} - 불가")
                            print("")

                        else:
                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode22 = False

                            print(f"[ 22. {krw_coin22} 잔고부족으로 매수안함. ]")
                            print(f"현재시간 : {now}  |  코인명 : {coin22}  |  현재매수가능 - {op_mode22} - 불가")
                            print("")

            elif price22 < ma20_22:       # 20일이평선보다 현재가가 낮을때는 매도
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
                        time.sleep(1)
                        # 보유수량 불러오기
                        krw_balance22 = upbit.get_balance(krw_coin22)
                        # 코인 현재가 불러오기
                        price22 = pyupbit.get_current_price(krw_coin22)
                        # 보유코인 원화금액으로 계산하기
                        bp22 = price22 * krw_balance22

                        # 보유 및 매수 가능 출력.
                        print(f"[ 22. {krw_coin22} 매도완료. ]")
                        print(f"매도시간 : {now}  |  코인명 : {coin22}  |  현재가 = ￦{price22}  |  20이평선가 = ￦{ma20_22}  |  보유수량 = {krw_balance22}  |  평가금액 = ￦{bp22}  |  매수가능 : {op_mode22} - 매수가능")
                        print("")

                    else:   # 보유코인 평가 금액이 10,00원 이하일때
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode22 = True

            # 1초 딜레이.
            time.sleep(1)
            ##### 22번 코인 매매 종료 #####
            #############################


            ###############################
            ##### 매매 : 23번코인 시작. #####
            # 코인 현재가 불러오기
            price23 = pyupbit.get_current_price(krw_coin23)
            # 이평선 조회.
            ma20_23 = get_ma20(krw_coin23)

            # 매수가능금액 불러오기
            krw23 = upbit.get_balance("KRW")

            # 20일 이평선 조건문
            if price23 > ma20_23:     # 20일이평선가격보다 현재가가 높을때는 매수
                if op_mode23 == True:    # 매수 가능(True)일 경우 - 매수시도
                    if krw23 > buy_krw:      # 매수가능금액 krw23 가 매수평균가 buy_krw 보다 클때
                        if krw23 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                            if buy_krw > 10100:     # 매수평균가 buy_krw 가 10,100원 초과일 경우 : 매수
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
                                print(f"매수시간 : {now}  |  코인명 : {coin23}  |  현재가 = ￦{price23}  |  20이평선가 = ￦{ma20_23}  |  보유수량 = {krw_balance23}  |  평가금액 = ￦{bp23}")
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

                            time.sleep(1)
                            # 보유수량 불러오기
                            krw_balance23 = upbit.get_balance(krw_coin23)
                            # 코인 현재가 불러오기
                            price23 = pyupbit.get_current_price(krw_coin23)
                            # 보유코인 원화금액으로 계산하기
                            bp23 = price23 * krw_balance23

                            # 보유 및 매수 가능 출력.
                            print(f"[ 23. {krw_coin23} 매수완료. ]")
                            print(f"매수시간 : {now}  |  코인명 : {coin23}  |  현재가 = ￦{price23}  |  20이평선가 = ￦{ma20_23}  |  보유수량 = {krw_balance23}  |  평가금액 = ￦{bp23}  |  매수가능 - {op_mode23} - 불가")
                            print("")

                        else:
                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode23 = False

                            print(f"[ 23. {krw_coin23} 잔고부족으로 매수안함. ]")
                            print(f"현재시간 : {now}  |  코인명 : {coin23}  |  현재매수가능 - {op_mode23} - 불가")
                            print("")

            elif price23 < ma20_23:       # 20일이평선보다 현재가가 낮을때는 매도
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
                        time.sleep(1)
                        # 보유수량 불러오기
                        krw_balance23 = upbit.get_balance(krw_coin23)
                        # 코인 현재가 불러오기
                        price23 = pyupbit.get_current_price(krw_coin23)
                        # 보유코인 원화금액으로 계산하기
                        bp23 = price23 * krw_balance23

                        # 보유 및 매수 가능 출력.
                        print(f"[ 23. {krw_coin23} 매도완료. ]")
                        print(f"매도시간 : {now}  |  코인명 : {coin23}  |  현재가 = ￦{price23}  |  20이평선가 = ￦{ma20_23}  |  보유수량 = {krw_balance23}  |  평가금액 = ￦{bp23}  |  매수가능 : {op_mode23} - 매수가능")
                        print("")

                    else:   # 보유코인 평가 금액이 10,100원 이하일때
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode23 = True

            # 1초 딜레이.
            time.sleep(1)
            ##### 23번 코인 매매 종료 #####
            #############################


            ###############################
            ##### 매매 : 24번코인 시작. #####
            # 코인 현재가 불러오기
            price24 = pyupbit.get_current_price(krw_coin24)
            # 이평선 조회.
            ma20_24 = get_ma20(krw_coin24)

            # 매수가능금액 불러오기
            krw24 = upbit.get_balance("KRW")

            # 20일 이평선 조건문
            if price24 > ma20_24:     # 20일이평선가격보다 현재가가 높을때는 매수
                if op_mode24 == True:    # 매수 가능(True)일 경우 - 매수시도
                    if krw24 > buy_krw:      # 매수가능금액 krw24 가 매수평균가 buy_krw 보다 클때
                        if krw24 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                            if buy_krw > 10100:     # 매수평균가 buy_krw 가 10,100원 초과일 경우 : 매수
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
                                print(f"매수시간 : {now}  |  코인명 : {coin24}  |  현재가 = ￦{price24}  |  20이평선가 = ￦{ma20_24}  |  보유수량 = {krw_balance24}  |  평가금액 = ￦{bp24}")
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

                            time.sleep(1)
                            # 보유수량 불러오기
                            krw_balance24 = upbit.get_balance(krw_coin24)
                            # 코인 현재가 불러오기
                            price24 = pyupbit.get_current_price(krw_coin24)
                            # 보유코인 원화금액으로 계산하기
                            bp24 = price24 * krw_balance24

                            # 보유 및 매수 가능 출력.
                            print(f"[ 24. {krw_coin24} 매수완료. ]")
                            print(f"매수시간 : {now}  |  코인명 : {coin24}  |  현재가 = ￦{price24}  |  20이평선가 = ￦{ma20_24}  |  보유수량 = {krw_balance24}  |  평가금액 = ￦{bp24}  |  매수가능 - {op_mode24} - 불가")
                            print("")

                        else:
                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode24 = False

                            print(f"[ 24. {krw_coin24} 잔고부족으로 매수안함. ]")
                            print(f"현재시간 : {now}  |  코인명 : {coin24}  |  현재매수가능 - {op_mode24} - 불가")
                            print("")

            elif price24 < ma20_24:       # 20일이평선보다 현재가가 낮을때는 매도
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
                        time.sleep(1)
                        # 보유수량 불러오기
                        krw_balance24 = upbit.get_balance(krw_coin24)
                        # 코인 현재가 불러오기
                        price24 = pyupbit.get_current_price(krw_coin24)
                        # 보유코인 원화금액으로 계산하기
                        bp24 = price24 * krw_balance24

                        # 보유 및 매수 가능 출력.
                        print(f"[ 24. {krw_coin24} 매도완료. ]")
                        print(f"매도시간 : {now}  |  코인명 : {coin24}  |  현재가 = ￦{price24}  |  20이평선가 = ￦{ma20_24}  |  보유수량 = {krw_balance24}  |  평가금액 = ￦{bp24}  |  매수가능 : {op_mode24} - 매수가능")
                        print("")

                    else:   # 보유코인 평가 금액이 10,100원 이하일때
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode24 = True

            # 1초 딜레이.
            time.sleep(1)
            ##### 24번 코인 매매 종료 #####
            #############################


            ###############################
            ##### 매매 : 25번코인 시작. #####
            # 코인 현재가 불러오기
            price25 = pyupbit.get_current_price(krw_coin25)
            # 이평선 조회.
            ma20_25 = get_ma20(krw_coin25)

            # 매수가능금액 불러오기
            krw25 = upbit.get_balance("KRW")

            # 20일 이평선 조건문
            if price25 > ma20_25:     # 20일이평선가격보다 현재가가 높을때는 매수
                if op_mode25 == True:    # 매수 가능(True)일 경우 - 매수시도
                    if krw25 > buy_krw:      # 매수가능금액 krw25 가 매수평균가 buy_krw 보다 클때
                        if krw25 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                            if buy_krw > 10100:     # 매수평균가 buy_krw 가 10,100원 초과일 경우 : 매수
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
                                print(f"매수시간 : {now}  |  코인명 : {coin25}  |  현재가 = ￦{price25}  |  20이평선가 = ￦{ma20_25}  |  보유수량 = {krw_balance25}  |  평가금액 = ￦{bp25}")
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

                            time.sleep(1)
                            # 보유수량 불러오기
                            krw_balance25 = upbit.get_balance(krw_coin25)
                            # 코인 현재가 불러오기
                            price25 = pyupbit.get_current_price(krw_coin25)
                            # 보유코인 원화금액으로 계산하기
                            bp25 = price25 * krw_balance25

                            # 보유 및 매수 가능 출력.
                            print(f"[ 25. {krw_coin25} 매수완료. ]")
                            print(f"매수시간 : {now}  |  코인명 : {coin25}  |  현재가 = ￦{price25}  |  20이평선가 = ￦{ma20_25}  |  보유수량 = {krw_balance25}  |  평가금액 = ￦{bp25}  |  매수가능 - {op_mode25} - 불가")
                            print("")

                        else:
                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode25 = False

                            print(f"[ 25. {krw_coin25} 잔고부족으로 매수안함. ]")
                            print(f"현재시간 : {now}  |  코인명 : {coin25}  |  현재매수가능 - {op_mode25} - 불가")
                            print("")

            elif price25 < ma20_25:       # 20일이평선보다 현재가가 낮을때는 매도
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
                        time.sleep(1)
                        # 보유수량 불러오기
                        krw_balance25 = upbit.get_balance(krw_coin25)
                        # 코인 현재가 불러오기
                        price25 = pyupbit.get_current_price(krw_coin25)
                        # 보유코인 원화금액으로 계산하기
                        bp25 = price25 * krw_balance25

                        # 보유 및 매수 가능 출력.
                        print(f"[ 25. {krw_coin25} 매도완료. ]")
                        print(f"매도시간 : {now}  |  코인명 : {coin25}  |  현재가 = ￦{price25}  |  20이평선가 = ￦{ma20_25}  |  보유수량 = {krw_balance25}  |  평가금액 = ￦{bp25}  |  매수가능 : {op_mode25} - 매수가능")
                        print("")

                    else:   # 보유코인 평가 금액이 10,100원 이하일때
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode25 = True

            # 1초 딜레이.
            time.sleep(1)
            ##### 25번 코인 매매 종료 #####
            #############################


            ###############################
            ##### 매매 : 26번코인 시작. #####
            # 코인 현재가 불러오기
            price26 = pyupbit.get_current_price(krw_coin26)
            # 이평선 조회.
            ma20_26 = get_ma20(krw_coin26)

            # 매수가능금액 불러오기
            krw26 = upbit.get_balance("KRW")

            # 20일 이평선 조건문
            if price26 > ma20_26:     # 20일이평선가격보다 현재가가 높을때는 매수
                if op_mode26 == True:    # 매수 가능(True)일 경우 - 매수시도
                    if krw26 > buy_krw:      # 매수가능금액 krw26 가 매수평균가 buy_krw 보다 클때
                        if krw26 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                            if buy_krw > 10100:     # 매수평균가 buy_krw 가 10,100원 초과일 경우 : 매수
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
                                print(f"매수시간 : {now}  |  코인명 : {coin26}  |  현재가 = ￦{price26}  |  20이평선가 = ￦{ma20_26}  |  보유수량 = {krw_balance26}  |  평가금액 = ￦{bp26}")
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

                            time.sleep(1)
                            # 보유수량 불러오기
                            krw_balance26 = upbit.get_balance(krw_coin26)
                            # 코인 현재가 불러오기
                            price26 = pyupbit.get_current_price(krw_coin26)
                            # 보유코인 원화금액으로 계산하기
                            bp26 = price26 * krw_balance26

                            # 보유 및 매수 가능 출력.
                            print(f"[ 26. {krw_coin26} 매수완료. ]")
                            print(f"매수시간 : {now}  |  코인명 : {coin26}  |  현재가 = ￦{price26}  |  20이평선가 = ￦{ma20_26}  |  보유수량 = {krw_balance26}  |  평가금액 = ￦{bp26}  |  매수가능 - {op_mode26} - 불가")
                            print("")

                        else:
                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode26 = False

                            print(f"[ 26. {krw_coin26} 잔고부족으로 매수안함. ]")
                            print(f"현재시간 : {now}  |  코인명 : {coin26}  |  현재매수가능 - {op_mode26} - 불가")
                            print("")

            elif price26 < ma20_26:       # 20일이평선보다 현재가가 낮을때는 매도
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
                        time.sleep(1)
                        # 보유수량 불러오기
                        krw_balance26 = upbit.get_balance(krw_coin26)
                        # 코인 현재가 불러오기
                        price26 = pyupbit.get_current_price(krw_coin26)
                        # 보유코인 원화금액으로 계산하기
                        bp26 = price26 * krw_balance26

                        # 보유 및 매수 가능 출력.
                        print(f"[ 26. {krw_coin26} 매도완료. ]")
                        print(f"매도시간 : {now}  |  코인명 : {coin26}  |  현재가 = ￦{price26}  |  20이평선가 = ￦{ma20_26}  |  보유수량 = {krw_balance26}  |  평가금액 = ￦{bp26}  |  매수가능 : {op_mode26} - 매수가능")
                        print("")

                    else:   # 보유코인 평가 금액이 10,100원 이하일때
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode26 = True

            # 1초 딜레이.
            time.sleep(1)
            ##### 26번 코인 매매 종료 #####
            #############################


            ###############################
            ##### 매매 : 27번코인 시작. #####
            # 코인 현재가 불러오기
            price27 = pyupbit.get_current_price(krw_coin27)
            # 이평선 조회.
            ma20_27 = get_ma20(krw_coin27)

            # 매수가능금액 불러오기
            krw27 = upbit.get_balance("KRW")

            # 20일 이평선 조건문
            if price27 > ma20_27:     # 20일이평선가격보다 현재가가 높을때는 매수
                if op_mode27 == True:    # 매수 가능(True)일 경우 - 매수시도
                    if krw27 > buy_krw:      # 매수가능금액 krw27 가 매수평균가 buy_krw 보다 클때
                        if krw27 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                            if buy_krw > 10100:     # 매수평균가 buy_krw 가 10,100원 초과일 경우 : 매수
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
                                print(f"매수시간 : {now}  |  코인명 : {coin27}  |  현재가 = ￦{price27}  |  20이평선가 = ￦{ma20_27}  |  보유수량 = {krw_balance27}  |  평가금액 = ￦{bp27}")
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

                            time.sleep(1)
                            # 보유수량 불러오기
                            krw_balance27 = upbit.get_balance(krw_coin27)
                            # 코인 현재가 불러오기
                            price27 = pyupbit.get_current_price(krw_coin27)
                            # 보유코인 원화금액으로 계산하기
                            bp27 = price27 * krw_balance27

                            # 보유 및 매수 가능 출력.
                            print(f"[ 27. {krw_coin27} 매수완료. ]")
                            print(f"매수시간 : {now}  |  코인명 : {coin27}  |  현재가 = ￦{price27}  |  20이평선가 = ￦{ma20_27}  |  보유수량 = {krw_balance27}  |  평가금액 = ￦{bp27}  |  매수가능 - {op_mode27} - 불가")
                            print("")

                        else:
                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode27 = False

                            print(f"[ 27. {krw_coin27} 잔고부족으로 매수안함. ]")
                            print(f"현재시간 : {now}  |  코인명 : {coin27}  |  현재매수가능 - {op_mode27} - 불가")
                            print("")

            elif price27 < ma20_27:       # 20일이평선보다 현재가가 낮을때는 매도
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
                        time.sleep(1)
                        # 보유수량 불러오기
                        krw_balance27 = upbit.get_balance(krw_coin27)
                        # 코인 현재가 불러오기
                        price27 = pyupbit.get_current_price(krw_coin27)
                        # 보유코인 원화금액으로 계산하기
                        bp27 = price27 * krw_balance27

                        # 보유 및 매수 가능 출력.
                        print(f"[ 27. {krw_coin27} 매도완료. ]")
                        print(f"매도시간 : {now}  |  코인명 : {coin27}  |  현재가 = ￦{price27}  |  20이평선가 = ￦{ma20_27}  |  보유수량 = {krw_balance27}  |  평가금액 = ￦{bp27}  |  매수가능 : {op_mode27} - 매수가능")
                        print("")

                    else:   # 보유코인 평가 금액이 10,100원 이하일때
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode27 = True

            # 1초 딜레이.
            time.sleep(1)
            ##### 27번 코인 매매 종료 #####
            #############################


            ###############################
            ##### 매매 : 28번코인 시작. #####
            # 코인 현재가 불러오기
            price28 = pyupbit.get_current_price(krw_coin28)
            # 이평선 조회.
            ma20_28 = get_ma20(krw_coin28)

            # 매수가능금액 불러오기
            krw28 = upbit.get_balance("KRW")

            # 20일 이평선 조건문
            if price28 > ma20_28:     # 20일이평선가격보다 현재가가 높을때는 매수
                if op_mode28 == True:    # 매수 가능(True)일 경우 - 매수시도
                    if krw28 > buy_krw:      # 매수가능금액 krw28 가 매수평균가 buy_krw 보다 클때
                        if krw28 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                            if buy_krw > 10100:     # 매수평균가 buy_krw 가 10,100원 초과일 경우 : 매수
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
                                print(f"매수시간 : {now}  |  코인명 : {coin28}  |  현재가 = ￦{price28}  |  20이평선가 = ￦{ma20_28}  |  보유수량 = {krw_balance28}  |  평가금액 = ￦{bp28}")
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

                            time.sleep(1)
                            # 보유수량 불러오기
                            krw_balance28 = upbit.get_balance(krw_coin28)
                            # 코인 현재가 불러오기
                            price28 = pyupbit.get_current_price(krw_coin28)
                            # 보유코인 원화금액으로 계산하기
                            bp28 = price28 * krw_balance28

                            # 보유 및 매수 가능 출력.
                            print(f"[ 28. {krw_coin28} 매수완료. ]")
                            print(f"매수시간 : {now}  |  코인명 : {coin28}  |  현재가 = ￦{price28}  |  20이평선가 = ￦{ma20_28}  |  보유수량 = {krw_balance28}  |  평가금액 = ￦{bp28}  |  매수가능 - {op_mode28} - 불가")
                            print("")

                        else:
                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode28 = False

                            print(f"[ 28. {krw_coin28} 잔고부족으로 매수안함. ]")
                            print(f"현재시간 : {now}  |  코인명 : {coin28}  |  현재매수가능 - {op_mode28} - 불가")
                            print("")

            elif price28 < ma20_28:       # 20일이평선보다 현재가가 낮을때는 매도
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
                        time.sleep(1)
                        # 보유수량 불러오기
                        krw_balance28 = upbit.get_balance(krw_coin28)
                        # 코인 현재가 불러오기
                        price28 = pyupbit.get_current_price(krw_coin28)
                        # 보유코인 원화금액으로 계산하기
                        bp28 = price28 * krw_balance28

                        # 보유 및 매수 가능 출력.
                        print(f"[ 28. {krw_coin28} 매도완료. ]")
                        print(f"매도시간 : {now}  |  코인명 : {coin28}  |  현재가 = ￦{price28}  |  20이평선가 = ￦{ma20_28}  |  보유수량 = {krw_balance28}  |  평가금액 = ￦{bp28}  |  매수가능 : {op_mode28} - 매수가능")
                        print("")

                    else:   # 보유코인 평가 금액이 10,100원 이하일때
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode28 = True

            # 1초 딜레이.
            time.sleep(1)
            ##### 28번 코인 매매 종료 #####
            #############################


            ###############################
            ##### 매매 : 29번코인 시작. #####
            # 코인 현재가 불러오기
            price29 = pyupbit.get_current_price(krw_coin29)
            # 이평선 조회.
            ma20_29 = get_ma20(krw_coin29)

            # 매수가능금액 불러오기
            krw29 = upbit.get_balance("KRW")

            # 20일 이평선 조건문
            if price29 > ma20_29:     # 20일이평선가격보다 현재가가 높을때는 매수
                if op_mode29 == True:    # 매수 가능(True)일 경우 - 매수시도
                    if krw29 > buy_krw:      # 매수가능금액 krw29 가 매수평균가 buy_krw 보다 클때
                        if krw29 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                            if buy_krw > 10100:     # 매수평균가 buy_krw 가 10,100원 초과일 경우 : 매수
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
                                print(f"매수시간 : {now}  |  코인명 : {coin29}  |  현재가 = ￦{price29}  |  20이평선가 = ￦{ma20_29}  |  보유수량 = {krw_balance29}  |  평가금액 = ￦{bp29}")
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

                            time.sleep(1)
                            # 보유수량 불러오기
                            krw_balance29 = upbit.get_balance(krw_coin29)
                            # 코인 현재가 불러오기
                            price29 = pyupbit.get_current_price(krw_coin29)
                            # 보유코인 원화금액으로 계산하기
                            bp29 = price29 * krw_balance29

                            # 보유 및 매수 가능 출력.
                            print(f"[ 29. {krw_coin29} 매수완료. ]")
                            print(f"매수시간 : {now}  |  코인명 : {coin29}  |  현재가 = ￦{price29}  |  20이평선가 = ￦{ma20_29}  |  보유수량 = {krw_balance29}  |  평가금액 = ￦{bp29}  |  매수가능 - {op_mode29} - 불가")
                            print("")

                        else:
                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode29 = False

                            print(f"[ 29. {krw_coin29} 잔고부족으로 매수안함. ]")
                            print(f"현재시간 : {now}  |  코인명 : {coin29}  |  현재매수가능 - {op_mode29} - 불가")
                            print("")

            elif price29 < ma20_29:       # 20일이평선보다 현재가가 낮을때는 매도
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
                        time.sleep(1)
                        # 보유수량 불러오기
                        krw_balance29 = upbit.get_balance(krw_coin29)
                        # 코인 현재가 불러오기
                        price29 = pyupbit.get_current_price(krw_coin29)
                        # 보유코인 원화금액으로 계산하기
                        bp29 = price29 * krw_balance29

                        # 보유 및 매수 가능 출력.
                        print(f"[ 29. {krw_coin29} 매도완료. ]")
                        print(f"매도시간 : {now}  |  코인명 : {coin29}  |  현재가 = ￦{price29}  |  20이평선가 = ￦{ma20_29}  |  보유수량 = {krw_balance29}  |  평가금액 = ￦{bp29}  |  매수가능 : {op_mode29} - 매수가능")
                        print("")

                    else:   # 보유코인 평가 금액이 10,100원 이하일때
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode29 = True

            # 1초 딜레이.
            time.sleep(1)
            ##### 29번 코인 매매 종료 #####
            #############################


            ###############################
            ##### 매매 : 30번코인 시작. #####
            # 코인 현재가 불러오기
            price30 = pyupbit.get_current_price(krw_coin30)
            # 이평선 조회.
            ma20_30 = get_ma20(krw_coin30)

            # 매수가능금액 불러오기
            krw30 = upbit.get_balance("KRW")

            # 20일 이평선 조건문
            if price30 > ma20_30:     # 20일이평선가격보다 현재가가 높을때는 매수
                if op_mode30 == True:    # 매수 가능(True)일 경우 - 매수시도
                    if krw30 > buy_krw:      # 매수가능금액 krw30 가 매수평균가 buy_krw 보다 클때
                        if krw30 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                            if buy_krw > 10100:     # 매수평균가 buy_krw 가 10,100원 초과일 경우 : 매수
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
                                print(f"매수시간 : {now}  |  코인명 : {coin30}  |  현재가 = ￦{price30}  |  20이평선가 = ￦{ma20_30}  |  보유수량 = {krw_balance30}  |  평가금액 = ￦{bp30}")
                                print(f"매수가능 - {op_mode30} - 불가")
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
                            print(f"매수시간 : {now}  |  코인명 : {coin30}  |  현재가 = ￦{price30}  |  20이평선가 = ￦{ma20_30}  |  보유수량 = {krw_balance30}  |  평가금액 = ￦{bp30}  |  매수가능 - {op_mode30} - 불가")
                            print("")

                        else:
                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode30 = False

                            print(f"[ 30. {krw_coin30} 잔고부족으로 매수안함. ]")
                            print(f"현재시간 : {now}  |  코인명 : {coin30}  |  현재매수가능 - {op_mode30} - 불가")
                            print("")

            elif price30 < ma20_30:       # 20일이평선보다 현재가가 낮을때는 매도
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
                        time.sleep(1)
                        # 보유수량 불러오기
                        krw_balance30 = upbit.get_balance(krw_coin30)
                        # 코인 현재가 불러오기
                        price30 = pyupbit.get_current_price(krw_coin30)
                        # 보유코인 원화금액으로 계산하기
                        bp30 = price30 * krw_balance30

                        # 보유 및 매수 가능 출력.
                        print(f"[ 30. {krw_coin30} 매도완료. ]")
                        print(f"매도시간 : {now}  |  코인명 : {coin30}  |  현재가 = ￦{price30}  |  20이평선가 = ￦{ma20_30}  |  보유수량 = {krw_balance30}  |  평가금액 = ￦{bp30}  |  매수가능 : {op_mode30} - 매수가능")
                        print("")

                    else:   # 보유코인 평가 금액이 10,100원 이하일때
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode30 = True

            # 1초 딜레이.
            time.sleep(1)
            ##### 30번 코인 매매 종료 #####
            #############################

            # 60초 딜레이.
            time.sleep(60)


            ######################################################################################################################################################
            ######################################################################################################################################################
            ######################################################################################################################################################
            ######################################################################################################################################################
            ######################################################################################################################################################