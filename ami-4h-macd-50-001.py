import pyupbit
import time
import datetime
import numpy as np

import requests


#############################################
#############################################
#####     4시간봉으로 MACD 자동 매매     #####
#############################################
#############################################



################
##### 함수 #####


#######################
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


####################
# 20 이동평균선 조회.
def get_ma20(ticker):
    # interval 받는 시간 "minute1", "minute5", "minute10", "minute20", "minute60"(1시간), "minute240"(4시간), "day", "week" 등등
    df = pyupbit.get_ohlcv(ticker, interval="minute240", count=30)
    ma20_1 = df['close'].rolling(20).mean().iloc[-1]
    ma20_2 = df['close'].rolling(28).mean().iloc[-2]
    ma20 = ma20_1 - ma20_2
    return ma20


############
# macd 조회.
def get_macd(ticker):
    # 단기 이평 = 12일선.
    # 장기 이평 = 26일선.
    # macd = 단기 이평 - 장기 이평.
    # signal = macd 의 9일선.

    # interval 받는 시간 "minute1", "minute5", "minute10", "minute20", "minute60"(1시간), "minute240"(4시간), "day", "week" 등등
    df = pyupbit.get_ohlcv(ticker, interval="minute240", count=60)

    # 단기 이평 = 12일선
    ma12_1 = df['close'].rolling(12).mean().iloc[-1]
    ma12_2 = df['close'].rolling(12).mean().iloc[-2]
    ma12_3 = df['close'].rolling(12).mean().iloc[-3]
    ma12_4 = df['close'].rolling(12).mean().iloc[-4]
    ma12_5 = df['close'].rolling(12).mean().iloc[-5]
    ma12_6 = df['close'].rolling(12).mean().iloc[-6]
    ma12_7 = df['close'].rolling(12).mean().iloc[-7]
    ma12_8 = df['close'].rolling(12).mean().iloc[-8]
    ma12_9 = df['close'].rolling(12).mean().iloc[-9]
    ma12_10 =  df['close'].rolling(12).mean().iloc[-10]

    # 장기 이평 = 26일선
    ma26_1 = df['close'].rolling(26).mean().iloc[-1]
    ma26_2 = df['close'].rolling(26).mean().iloc[-2]
    ma26_3 = df['close'].rolling(26).mean().iloc[-3]
    ma26_4 = df['close'].rolling(26).mean().iloc[-4]
    ma26_5 = df['close'].rolling(26).mean().iloc[-5]
    ma26_6 = df['close'].rolling(26).mean().iloc[-6]
    ma26_7 = df['close'].rolling(26).mean().iloc[-7]
    ma26_8 = df['close'].rolling(26).mean().iloc[-8]
    ma26_9 = df['close'].rolling(26).mean().iloc[-9]
    ma26_10 = df['close'].rolling(26).mean().iloc[-10]

    # macd = 단기이평 - 장기이평
    macd_1 = ma12_1 - ma26_1
    macd_2 = ma12_2 - ma26_2
    macd_3 = ma12_3 - ma26_3
    macd_4 = ma12_4 - ma26_4
    macd_5 = ma12_5 - ma26_5
    macd_6 = ma12_6 - ma26_6
    macd_7 = ma12_7 - ma26_7
    macd_8 = ma12_8 - ma26_8
    macd_9 = ma12_9 - ma26_9
    macd_10 = ma12_10 - ma26_10

    # signal = macd 9일선
    signal_1 = ( macd_1 + macd_2 + macd_3 + macd_4 + macd_5 + macd_6 + macd_7 + macd_8 + macd_9 ) / 9
    
    # 최종값
    macd = macd_1 - signal_1

    return macd


#########################
# 거래량 동반한 macd 조회.
def get_acc_macd(ticker):
    # 단기 이평 = 12일선.
    # 장기 이평 = 26일선.
    # macd = 단기 이평 - 장기 이평.
    # signal = macd 의 9일선.

    # 링크와 가져오는 캔들 지정 ~minutes/시간 - 1, 5, 10, 20, 60(1시간), 240(4시간), day, week
    url = "https://api.upbit.com/v1/candles/minutes/240"

    # 가져올려는 코인명과, 캔들수
    querystring = {"market":ticker,"count":"60"}

    headers = {"Accept": "application/json"}

    response = requests.request("GET", url, headers=headers, params=querystring)


    data = response.json()


    # 종가받기 60개
    # 0은 현재
    price_0 = data[0]["trade_price"]
    # 1은 전종가. 여기부터
    price_1 = data[1]["trade_price"]
    price_2 = data[2]["trade_price"]
    price_3 = data[3]["trade_price"]
    price_4 = data[4]["trade_price"]
    price_5 = data[5]["trade_price"]
    price_6 = data[6]["trade_price"]
    price_7 = data[7]["trade_price"]
    price_8 = data[8]["trade_price"]
    price_9 = data[9]["trade_price"]
    price_10 = data[10]["trade_price"]
    price_11 = data[11]["trade_price"]
    price_12 = data[12]["trade_price"]
    price_13 = data[13]["trade_price"]
    price_14 = data[14]["trade_price"]
    price_15 = data[15]["trade_price"]
    price_16 = data[16]["trade_price"]
    price_17 = data[17]["trade_price"]
    price_18 = data[18]["trade_price"]
    price_19 = data[19]["trade_price"]
    price_20 = data[20]["trade_price"]
    price_21 = data[21]["trade_price"]
    price_22 = data[22]["trade_price"]
    price_23 = data[23]["trade_price"]
    price_24 = data[24]["trade_price"]
    price_25 = data[25]["trade_price"]
    price_26 = data[26]["trade_price"]
    price_27 = data[27]["trade_price"]
    price_28 = data[28]["trade_price"]
    price_29 = data[29]["trade_price"]
    price_30 = data[30]["trade_price"]
    price_31 = data[31]["trade_price"]
    price_32 = data[32]["trade_price"]
    price_33 = data[33]["trade_price"]
    price_34 = data[34]["trade_price"]
    price_35 = data[35]["trade_price"]


    # 캔들 거래량 60개
    volume_0 = data[0]["candle_acc_trade_volume"]
    # 여기부터
    volume_1 = data[1]["candle_acc_trade_volume"]
    volume_2 = data[2]["candle_acc_trade_volume"]
    volume_3 = data[3]["candle_acc_trade_volume"]
    volume_4 = data[4]["candle_acc_trade_volume"]
    volume_5 = data[5]["candle_acc_trade_volume"]
    volume_6 = data[6]["candle_acc_trade_volume"]
    volume_7 = data[7]["candle_acc_trade_volume"]
    volume_8 = data[8]["candle_acc_trade_volume"]
    volume_9 = data[9]["candle_acc_trade_volume"]
    volume_10 = data[10]["candle_acc_trade_volume"]
    volume_11 = data[11]["candle_acc_trade_volume"]
    volume_12 = data[12]["candle_acc_trade_volume"]
    volume_13 = data[13]["candle_acc_trade_volume"]
    volume_14 = data[14]["candle_acc_trade_volume"]
    volume_15 = data[15]["candle_acc_trade_volume"]
    volume_16 = data[16]["candle_acc_trade_volume"]
    volume_17 = data[17]["candle_acc_trade_volume"]
    volume_18 = data[18]["candle_acc_trade_volume"]
    volume_19 = data[19]["candle_acc_trade_volume"]
    volume_20 = data[20]["candle_acc_trade_volume"]
    volume_21 = data[21]["candle_acc_trade_volume"]
    volume_22 = data[22]["candle_acc_trade_volume"]
    volume_23 = data[23]["candle_acc_trade_volume"]
    volume_24 = data[24]["candle_acc_trade_volume"]
    volume_25 = data[25]["candle_acc_trade_volume"]
    volume_26 = data[26]["candle_acc_trade_volume"]
    volume_27 = data[27]["candle_acc_trade_volume"]
    volume_28 = data[28]["candle_acc_trade_volume"]
    volume_29 = data[29]["candle_acc_trade_volume"]
    volume_30 = data[30]["candle_acc_trade_volume"]
    volume_31 = data[31]["candle_acc_trade_volume"]
    volume_32 = data[32]["candle_acc_trade_volume"]
    volume_33 = data[33]["candle_acc_trade_volume"]
    volume_34 = data[34]["candle_acc_trade_volume"]
    volume_35 = data[35]["candle_acc_trade_volume"]


    ###################################
    ##### 거래량 동반한 macd 산출. #####


    # 캔들 누적거래금액 60개
    acc_trade_price_0 = price_0 * volume_0
    # 여기부터
    acc_trade_price_1 = price_1 * volume_1
    acc_trade_price_2 = price_2 * volume_2
    acc_trade_price_3 = price_3 * volume_3
    acc_trade_price_4 = price_4 * volume_4
    acc_trade_price_5 = price_5 * volume_5
    acc_trade_price_6 = price_6 * volume_6
    acc_trade_price_7 = price_7 * volume_7
    acc_trade_price_8 = price_8 * volume_8
    acc_trade_price_9 = price_9 * volume_9
    acc_trade_price_10 = price_10 * volume_10
    acc_trade_price_11 = price_11 * volume_11
    acc_trade_price_12 = price_12 * volume_12
    acc_trade_price_13 = price_13 * volume_13
    acc_trade_price_14 = price_14 * volume_14
    acc_trade_price_15 = price_15 * volume_15
    acc_trade_price_16 = price_16 * volume_16
    acc_trade_price_17 = price_17 * volume_17
    acc_trade_price_18 = price_18 * volume_18
    acc_trade_price_19 = price_19 * volume_19
    acc_trade_price_20 = price_20 * volume_20
    acc_trade_price_21 = price_21 * volume_21
    acc_trade_price_22 = price_22 * volume_22
    acc_trade_price_23 = price_23 * volume_23
    acc_trade_price_24 = price_24 * volume_24
    acc_trade_price_25 = price_25 * volume_25
    acc_trade_price_26 = price_26 * volume_26
    acc_trade_price_27 = price_27 * volume_27
    acc_trade_price_28 = price_28 * volume_28
    acc_trade_price_29 = price_29 * volume_29
    acc_trade_price_30 = price_30 * volume_30
    acc_trade_price_31 = price_31 * volume_31
    acc_trade_price_32 = price_32 * volume_32
    acc_trade_price_33 = price_33 * volume_33
    acc_trade_price_34 = price_34 * volume_34
    acc_trade_price_35 = price_35 * volume_35



    # 단기 12일 거래량 합산
    acc_volume12_0 = volume_0 + volume_1 + volume_2 + volume_3 + volume_4 + volume_5 + volume_6 + volume_7 + volume_8 + volume_9 + volume_10 + volume_11
    # 여기부터
    acc_volume12_1 = volume_1 + volume_2 + volume_3 + volume_4 + volume_5 + volume_6 + volume_7 + volume_8 + volume_9 + volume_10 + volume_11 + volume_12
    acc_volume12_2 = volume_2 + volume_3 + volume_4 + volume_5 + volume_6 + volume_7 + volume_8 + volume_9 + volume_10 + volume_11 + volume_12 + volume_13
    acc_volume12_3 = volume_3 + volume_4 + volume_5 + volume_6 + volume_7 + volume_8 + volume_9 + volume_10 + volume_11 + volume_12 + volume_13 + volume_14
    acc_volume12_4 = volume_4 + volume_5 + volume_6 + volume_7 + volume_8 + volume_9 + volume_10 + volume_11 + volume_12 + volume_13 + volume_14 + volume_15
    acc_volume12_5 = volume_5 + volume_6 + volume_7 + volume_8 + volume_9 + volume_10 + volume_11 + volume_12 + volume_13 + volume_14 + volume_15 + volume_16
    acc_volume12_6 = volume_6 + volume_7 + volume_8 + volume_9 + volume_10 + volume_11 + volume_12 + volume_13 + volume_14 + volume_15 + volume_16 + volume_17
    acc_volume12_7 = volume_7 + volume_8 + volume_9 + volume_10 + volume_11 + volume_12 + volume_13 + volume_14 + volume_15 + volume_16 + volume_17 + volume_18
    acc_volume12_8 = volume_8 + volume_9 + volume_10 + volume_11 + volume_12 + volume_13 + volume_14 + volume_15 + volume_16 + volume_17 + volume_18 + volume_19
    acc_volume12_9 = volume_9 + volume_10 + volume_11 + volume_12 + volume_13 + volume_14 + volume_15 + volume_16 + volume_17 + volume_18 + volume_19 + volume_20
    # 여기까지


    # 거래량 동반한 단기 12이평선
    acc_ma12_0 = ( acc_trade_price_0 + acc_trade_price_1 + acc_trade_price_2 + acc_trade_price_3 + acc_trade_price_4 + acc_trade_price_5 + acc_trade_price_6 + acc_trade_price_7 + acc_trade_price_8 + acc_trade_price_9 + acc_trade_price_10 + acc_trade_price_11 ) / acc_volume12_0
    # 여기부터
    acc_ma12_1 = ( acc_trade_price_1 + acc_trade_price_2 + acc_trade_price_3 + acc_trade_price_4 + acc_trade_price_5 + acc_trade_price_6 + acc_trade_price_7 + acc_trade_price_8 + acc_trade_price_9 + acc_trade_price_10 + acc_trade_price_11 + acc_trade_price_12 ) / acc_volume12_1
    acc_ma12_2 = ( acc_trade_price_2 + acc_trade_price_3 + acc_trade_price_4 + acc_trade_price_5 + acc_trade_price_6 + acc_trade_price_7 + acc_trade_price_8 + acc_trade_price_9 + acc_trade_price_10 + acc_trade_price_11 + acc_trade_price_12 + acc_trade_price_13 ) / acc_volume12_2
    acc_ma12_3 = ( acc_trade_price_3 + acc_trade_price_4 + acc_trade_price_5 + acc_trade_price_6 + acc_trade_price_7 + acc_trade_price_8 + acc_trade_price_9 + acc_trade_price_10 + acc_trade_price_11 + acc_trade_price_12 + acc_trade_price_13 + acc_trade_price_14 ) / acc_volume12_3
    acc_ma12_4 = ( acc_trade_price_4 + acc_trade_price_5 + acc_trade_price_6 + acc_trade_price_7 + acc_trade_price_8 + acc_trade_price_9 + acc_trade_price_10 + acc_trade_price_11 + acc_trade_price_12 + acc_trade_price_13 + acc_trade_price_14 + acc_trade_price_15 ) / acc_volume12_4
    acc_ma12_5 = ( acc_trade_price_5 + acc_trade_price_6 + acc_trade_price_7 + acc_trade_price_8 + acc_trade_price_9 + acc_trade_price_10 + acc_trade_price_11 + acc_trade_price_12 + acc_trade_price_13 + acc_trade_price_14 + acc_trade_price_15 + acc_trade_price_16 ) / acc_volume12_5
    acc_ma12_6 = ( acc_trade_price_6 + acc_trade_price_7 + acc_trade_price_8 + acc_trade_price_9 + acc_trade_price_10 + acc_trade_price_11 + acc_trade_price_12 + acc_trade_price_13 + acc_trade_price_14 + acc_trade_price_15 + acc_trade_price_16 + acc_trade_price_17 ) / acc_volume12_6
    acc_ma12_7 = ( acc_trade_price_7 + acc_trade_price_8 + acc_trade_price_9 + acc_trade_price_10 + acc_trade_price_11 + acc_trade_price_12 + acc_trade_price_13 + acc_trade_price_14 + acc_trade_price_15 + acc_trade_price_16 + acc_trade_price_17 + acc_trade_price_18 ) / acc_volume12_7
    acc_ma12_8 = ( acc_trade_price_8 + acc_trade_price_9 + acc_trade_price_10 + acc_trade_price_11 + acc_trade_price_12 + acc_trade_price_13 + acc_trade_price_14 + acc_trade_price_15 + acc_trade_price_16 + acc_trade_price_17 + acc_trade_price_18 + acc_trade_price_19 ) / acc_volume12_8
    acc_ma12_9 = ( acc_trade_price_9 + acc_trade_price_10 + acc_trade_price_11 + acc_trade_price_12 + acc_trade_price_13 + acc_trade_price_14 + acc_trade_price_15 + acc_trade_price_16 + acc_trade_price_17 + acc_trade_price_18 + acc_trade_price_19 + acc_trade_price_20 ) / acc_volume12_9
    # 여기까지


    # 장기 26일 거래량 합산
    acc_volume26_0 = volume_0 + volume_1 + volume_2 + volume_3 + volume_4 + volume_5 + volume_6 + volume_7 + volume_8 + volume_9 + volume_10 + volume_11 + volume_12 + volume_13 + volume_14 + volume_15 + volume_16 + volume_17 + volume_18 + volume_19 + volume_20 + volume_21 + volume_22 + volume_23 + volume_24 + volume_25
    # 여기부터
    acc_volume26_1 = volume_1 + volume_2 + volume_3 + volume_4 + volume_5 + volume_6 + volume_7 + volume_8 + volume_9 + volume_10 + volume_11 + volume_12 + volume_13 + volume_14 + volume_15 + volume_16 + volume_17 + volume_18 + volume_19 + volume_20 + volume_21 + volume_22 + volume_23 + volume_24 + volume_25 + volume_26
    acc_volume26_2 = volume_2 + volume_3 + volume_4 + volume_5 + volume_6 + volume_7 + volume_8 + volume_9 + volume_10 + volume_11 + volume_12 + volume_13 + volume_14 + volume_15 + volume_16 + volume_17 + volume_18 + volume_19 + volume_20 + volume_21 + volume_22 + volume_23 + volume_24 + volume_25 + volume_26 + volume_27
    acc_volume26_3 = volume_3 + volume_4 + volume_5 + volume_6 + volume_7 + volume_8 + volume_9 + volume_10 + volume_11 + volume_12 + volume_13 + volume_14 + volume_15 + volume_16 + volume_17 + volume_18 + volume_19 + volume_20 + volume_21 + volume_22 + volume_23 + volume_24 + volume_25 + volume_26 + volume_27 + volume_28
    acc_volume26_4 = volume_4 + volume_5 + volume_6 + volume_7 + volume_8 + volume_9 + volume_10 + volume_11 + volume_12 + volume_13 + volume_14 + volume_15 + volume_16 + volume_17 + volume_18 + volume_19 + volume_20 + volume_21 + volume_22 + volume_23 + volume_24 + volume_25 + volume_26 + volume_27 + volume_28 + volume_29
    acc_volume26_5 = volume_5 + volume_6 + volume_7 + volume_8 + volume_9 + volume_10 + volume_11 + volume_12 + volume_13 + volume_14 + volume_15 + volume_16 + volume_17 + volume_18 + volume_19 + volume_20 + volume_21 + volume_22 + volume_23 + volume_24 + volume_25 + volume_26 + volume_27 + volume_28 + volume_29 + volume_30
    acc_volume26_6 = volume_6 + volume_7 + volume_8 + volume_9 + volume_10 + volume_11 + volume_12 + volume_13 + volume_14 + volume_15 + volume_16 + volume_17 + volume_18 + volume_19 + volume_20 + volume_21 + volume_22 + volume_23 + volume_24 + volume_25 + volume_26 + volume_27 + volume_28 + volume_29 + volume_30 + volume_31
    acc_volume26_7 = volume_7 + volume_8 + volume_9 + volume_10 + volume_11 + volume_12 + volume_13 + volume_14 + volume_15 + volume_16 + volume_17 + volume_18 + volume_19 + volume_20 + volume_21 + volume_22 + volume_23 + volume_24 + volume_25 + volume_26 + volume_27 + volume_28 + volume_29 + volume_30 + volume_31 + volume_32
    acc_volume26_8 = volume_8 + volume_9 + volume_10 + volume_11 + volume_12 + volume_13 + volume_14 + volume_15 + volume_16 + volume_17 + volume_18 + volume_19 + volume_20 + volume_21 + volume_22 + volume_23 + volume_24 + volume_25 + volume_26 + volume_27 + volume_28 + volume_29 + volume_30 + volume_31 + volume_32 + volume_33
    acc_volume26_9 = volume_9 + volume_10 + volume_11 + volume_12 + volume_13 + volume_14 + volume_15 + volume_16 + volume_17 + volume_18 + volume_19 + volume_20 + volume_21 + volume_22 + volume_23 + volume_24 + volume_25 + volume_26 + volume_27 + volume_28 + volume_29 + volume_30 + volume_31 + volume_32 + volume_33 + volume_34
    # 여기까지


    # 거래량 동반한 장기 26이평선
    acc_ma26_0 = ( acc_trade_price_0 + acc_trade_price_1 + acc_trade_price_2 + acc_trade_price_3 + acc_trade_price_4 + acc_trade_price_5 + acc_trade_price_6 + acc_trade_price_7 + acc_trade_price_8 + acc_trade_price_9 + acc_trade_price_10 + acc_trade_price_11 + acc_trade_price_12 + acc_trade_price_13 + acc_trade_price_14 + acc_trade_price_15 + acc_trade_price_16 + acc_trade_price_17 + acc_trade_price_18 + acc_trade_price_19 + acc_trade_price_20 + acc_trade_price_21 + acc_trade_price_22 + acc_trade_price_23 + acc_trade_price_24 + acc_trade_price_25 ) / acc_volume26_0
    # 여기부터
    acc_ma26_1 = ( acc_trade_price_1 + acc_trade_price_2 + acc_trade_price_3 + acc_trade_price_4 + acc_trade_price_5 + acc_trade_price_6 + acc_trade_price_7 + acc_trade_price_8 + acc_trade_price_9 + acc_trade_price_10 + acc_trade_price_11 + acc_trade_price_12 + acc_trade_price_13 + acc_trade_price_14 + acc_trade_price_15 + acc_trade_price_16 + acc_trade_price_17 + acc_trade_price_18 + acc_trade_price_19 + acc_trade_price_20 + acc_trade_price_21 + acc_trade_price_22 + acc_trade_price_23 + acc_trade_price_24 + acc_trade_price_25 + acc_trade_price_26 ) / acc_volume26_1
    acc_ma26_2 = ( acc_trade_price_2 + acc_trade_price_3 + acc_trade_price_4 + acc_trade_price_5 + acc_trade_price_6 + acc_trade_price_7 + acc_trade_price_8 + acc_trade_price_9 + acc_trade_price_10 + acc_trade_price_11 + acc_trade_price_12 + acc_trade_price_13 + acc_trade_price_14 + acc_trade_price_15 + acc_trade_price_16 + acc_trade_price_17 + acc_trade_price_18 + acc_trade_price_19 + acc_trade_price_20 + acc_trade_price_21 + acc_trade_price_22 + acc_trade_price_23 + acc_trade_price_24 + acc_trade_price_25 + acc_trade_price_26 + acc_trade_price_27 ) / acc_volume26_2
    acc_ma26_3 = ( acc_trade_price_3 + acc_trade_price_4 + acc_trade_price_5 + acc_trade_price_6 + acc_trade_price_7 + acc_trade_price_8 + acc_trade_price_9 + acc_trade_price_10 + acc_trade_price_11 + acc_trade_price_12 + acc_trade_price_13 + acc_trade_price_14 + acc_trade_price_15 + acc_trade_price_16 + acc_trade_price_17 + acc_trade_price_18 + acc_trade_price_19 + acc_trade_price_20 + acc_trade_price_21 + acc_trade_price_22 + acc_trade_price_23 + acc_trade_price_24 + acc_trade_price_25 + acc_trade_price_26 + acc_trade_price_27 + acc_trade_price_28 ) / acc_volume26_3
    acc_ma26_4 = ( acc_trade_price_4 + acc_trade_price_5 + acc_trade_price_6 + acc_trade_price_7 + acc_trade_price_8 + acc_trade_price_9 + acc_trade_price_10 + acc_trade_price_11 + acc_trade_price_12 + acc_trade_price_13 + acc_trade_price_14 + acc_trade_price_15 + acc_trade_price_16 + acc_trade_price_17 + acc_trade_price_18 + acc_trade_price_19 + acc_trade_price_20 + acc_trade_price_21 + acc_trade_price_22 + acc_trade_price_23 + acc_trade_price_24 + acc_trade_price_25 + acc_trade_price_26 + acc_trade_price_27 + acc_trade_price_28 + acc_trade_price_29 ) / acc_volume26_4
    acc_ma26_5 = ( acc_trade_price_5 + acc_trade_price_6 + acc_trade_price_7 + acc_trade_price_8 + acc_trade_price_9 + acc_trade_price_10 + acc_trade_price_11 + acc_trade_price_12 + acc_trade_price_13 + acc_trade_price_14 + acc_trade_price_15 + acc_trade_price_16 + acc_trade_price_17 + acc_trade_price_18 + acc_trade_price_19 + acc_trade_price_20 + acc_trade_price_21 + acc_trade_price_22 + acc_trade_price_23 + acc_trade_price_24 + acc_trade_price_25 + acc_trade_price_26 + acc_trade_price_27 + acc_trade_price_28 + acc_trade_price_29 + acc_trade_price_30 ) / acc_volume26_5
    acc_ma26_6 = ( acc_trade_price_6 + acc_trade_price_7 + acc_trade_price_8 + acc_trade_price_9 + acc_trade_price_10 + acc_trade_price_11 + acc_trade_price_12 + acc_trade_price_13 + acc_trade_price_14 + acc_trade_price_15 + acc_trade_price_16 + acc_trade_price_17 + acc_trade_price_18 + acc_trade_price_19 + acc_trade_price_20 + acc_trade_price_21 + acc_trade_price_22 + acc_trade_price_23 + acc_trade_price_24 + acc_trade_price_25 + acc_trade_price_26 + acc_trade_price_27 + acc_trade_price_28 + acc_trade_price_29 + acc_trade_price_30 + acc_trade_price_31 ) / acc_volume26_6
    acc_ma26_7 = ( acc_trade_price_7 + acc_trade_price_8 + acc_trade_price_9 + acc_trade_price_10 + acc_trade_price_11 + acc_trade_price_12 + acc_trade_price_13 + acc_trade_price_14 + acc_trade_price_15 + acc_trade_price_16 + acc_trade_price_17 + acc_trade_price_18 + acc_trade_price_19 + acc_trade_price_20 + acc_trade_price_21 + acc_trade_price_22 + acc_trade_price_23 + acc_trade_price_24 + acc_trade_price_25 + acc_trade_price_26 + acc_trade_price_27 + acc_trade_price_28 + acc_trade_price_29 + acc_trade_price_30 + acc_trade_price_31 + acc_trade_price_32 ) / acc_volume26_7
    acc_ma26_8 = ( acc_trade_price_8 + acc_trade_price_9 + acc_trade_price_10 + acc_trade_price_11 + acc_trade_price_12 + acc_trade_price_13 + acc_trade_price_14 + acc_trade_price_15 + acc_trade_price_16 + acc_trade_price_17 + acc_trade_price_18 + acc_trade_price_19 + acc_trade_price_20 + acc_trade_price_21 + acc_trade_price_22 + acc_trade_price_23 + acc_trade_price_24 + acc_trade_price_25 + acc_trade_price_26 + acc_trade_price_27 + acc_trade_price_28 + acc_trade_price_29 + acc_trade_price_30 + acc_trade_price_31 + acc_trade_price_32 + acc_trade_price_33 ) / acc_volume26_8
    acc_ma26_9 = ( acc_trade_price_9 + acc_trade_price_10 + acc_trade_price_11 + acc_trade_price_12 + acc_trade_price_13 + acc_trade_price_14 + acc_trade_price_15 + acc_trade_price_16 + acc_trade_price_17 + acc_trade_price_18 + acc_trade_price_19 + acc_trade_price_20 + acc_trade_price_21 + acc_trade_price_22 + acc_trade_price_23 + acc_trade_price_24 + acc_trade_price_25 + acc_trade_price_26 + acc_trade_price_27 + acc_trade_price_28 + acc_trade_price_29 + acc_trade_price_30 + acc_trade_price_31 + acc_trade_price_32 + acc_trade_price_33 + acc_trade_price_34 ) / acc_volume26_9
    # 여기까지


    # 거래량 동반한 macd
    acc_macd_0 = acc_ma12_0 - acc_ma26_0
    # 여기부터
    acc_macd_1 = acc_ma12_1 - acc_ma26_1
    acc_macd_2 = acc_ma12_2 - acc_ma26_2
    acc_macd_3 = acc_ma12_3 - acc_ma26_3
    acc_macd_4 = acc_ma12_4 - acc_ma26_4
    acc_macd_5 = acc_ma12_5 - acc_ma26_5
    acc_macd_6 = acc_ma12_6 - acc_ma26_6
    acc_macd_7 = acc_ma12_7 - acc_ma26_7
    acc_macd_8 = acc_ma12_8 - acc_ma26_8
    acc_macd_9 = acc_ma12_9 - acc_ma26_9


    # signal = macd 9일선
    acc_signal_0 = ( acc_macd_0 + acc_macd_1 + acc_macd_2 + acc_macd_3 + acc_macd_4 + acc_macd_5 + acc_macd_6 + acc_macd_7 + acc_macd_8 ) / 9
    # 여기부터
    acc_signal_1 = ( acc_macd_1 + acc_macd_2 + acc_macd_3 + acc_macd_4 + acc_macd_5 + acc_macd_6 + acc_macd_7 + acc_macd_8 + acc_macd_9 ) / 9


    # 최종값
    acc_macd0 = acc_macd_0 - acc_signal_0
    # 여기부터
    acc_macd1 = acc_macd_1 - acc_signal_1


    ##### 거래량 동반한 macd 산출. 끝 #####
    #####################################

    return acc_macd1



# 흥효꺼
# 엑세스키, 시크릿키 가져오기
access = "s9mx5YF3TtInoUqUM3D8x464PUamTpUxZxRg35zj"
secret = "DfBQ4UXJMyaD172GD4rpwGIQ1zxBuxIMgpRvW4ZI"

# 동생꺼
# 엑세스키, 시크릿키 가져오기
#access = "aFU3balSDNODIEENihFta23gfpF1aqgeduofjFnA"
#secret = "LGQiWDaQWx9UDI4AqgS6rk41h55LrnoqCq9of3nL"


# 매수금액 가져오기
#buy_krw = int(lines[5].strip())

# 코인매매갯수 가져오기
#trade_coinX = int(lines[7].strip())


# 코인명 가져오기
coin1 = "BTC" # 비트코인
coin2 = "ETH" # 이더리움
coin3 = "ADA" # 에이다
coin4 = "XRP" # 리플
coin5 = "DOGE" # 도지코인

coin6 = "DOT" # 폴카닷
coin7 = "BCH" # 비트코인캐시
coin8 = "LINK" # 체인링크
coin9 = "LTC" # 라이트코인
coin10 = "ETC" # 이더리움클래식

coin11 = "XLM" # 스텔라루멘
coin12 = "VET" # 비체인
coin13 = "THETA" # 쎄타토큰
coin14 = "TRX" # 트론
coin15 = "EOS" # 이오스

coin16 = "AXS" # 엑시인피니티
coin17 = "ATOM" # 코스모스
coin18 = "NEO" # 네오
coin19 = "CRO" # 크립토닷컴체인
coin20 = "BSV" # 비트코인에스브이

coin21 = "XTZ" # 테조스
coin22 = "IOTA" # 아이오타
coin23 = "BTT" # 비트토렌트
coin24 = "WAVES" # 웨이브
coin25 = "HBAR" # 헤데라해시그래프

coin26 = "CHZ" # 칠리즈
coin27 = "XEM" # 넴
coin28 = "STX" # 스택스
coin29 = "TFUEL" # 쎄타퓨엘
coin30 = "BCHA" # 비트코인캐시에이비씨

coin31 = "MANA" # 디센트럴랜드
coin32 = "ENJ" # 엔진코인
coin33 = "FLOW" # 플로우
coin34 = "QTUM" # 퀀텀
coin35 = "BTG" # 비트코인골드

coin36 = "ZIL" # 질리카
coin37 = "BAT" # 베이직어텐션토크
coin38 = "ONT" # 온톨로지
coin39 = "SC" # 시아코인
coin40 = "ICX" # 아이콘

coin41 = "ZRX" # 제로엑스
coin42 = "OMG" # 오미세고
coin43 = "ANKR" # 앵커
coin44 = "SXP" # 스와이프
coin45 = "LSK" # 리스크

coin46 = "KAVA" # 카바
coin47 = "SAND" # 샌드박스
coin48 = "IOST" # 아이오에스티
coin49 = "PUNDIX" # 펀디엑스
# 개인 - 플레이댑
coin50 = "PLA" # 플레이댑


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

krw_coin41 = "KRW-" + coin41
krw_coin42 = "KRW-" + coin42
krw_coin43 = "KRW-" + coin43
krw_coin44 = "KRW-" + coin44
krw_coin45 = "KRW-" + coin45
krw_coin46 = "KRW-" + coin46
krw_coin47 = "KRW-" + coin47
krw_coin48 = "KRW-" + coin48
krw_coin49 = "KRW-" + coin49
krw_coin50 = "KRW-" + coin50



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


##### 41. 코인
# 보유수량 불러오기
krw_balance41 = upbit.get_balance(krw_coin41)
# 코인 현재가 불러오기
price41 = pyupbit.get_current_price(krw_coin41)
# 보유코인 원화금액으로 계산하기
bp41 = price41 * krw_balance41
# 코인 현황 출력.
print(f"41. 코인명 : {coin41}  |  현재가 = ￦{price41}  |  보유수량 = {krw_balance41}  |  평가금액 = ￦{bp41}")
# 코인 보유 유무
if bp41 > 10100:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode41 = False

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 보유중  |  매수가능 - {op_mode41} - 매수불가")
    print("")
else:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode41 = True

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 없음  |  매수가능 - {op_mode41} - 매수가능")
    print("")
time.sleep(1)


##### 42. 코인
# 보유수량 불러오기
krw_balance42 = upbit.get_balance(krw_coin42)
# 코인 현재가 불러오기
price42 = pyupbit.get_current_price(krw_coin42)
# 보유코인 원화금액으로 계산하기
bp42 = price42 * krw_balance42
# 코인 현황 출력.
print(f"42. 코인명 : {coin42}  |  현재가 = ￦{price42}  |  보유수량 = {krw_balance42}  |  평가금액 = ￦{bp42}")
# 코인 보유 유무
if bp42 > 10100:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode42 = False

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 보유중  |  매수가능 - {op_mode42} - 매수불가")
    print("")
else:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode42 = True

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 없음  |  매수가능 - {op_mode42} - 매수가능")
    print("")
time.sleep(1)


##### 43. 코인
# 보유수량 불러오기
krw_balance43 = upbit.get_balance(krw_coin43)
# 코인 현재가 불러오기
price43 = pyupbit.get_current_price(krw_coin43)
# 보유코인 원화금액으로 계산하기
bp43 = price43 * krw_balance43
# 코인 현황 출력.
print(f"43. 코인명 : {coin43}  |  현재가 = ￦{price43}  |  보유수량 = {krw_balance43}  |  평가금액 = ￦{bp43}")
# 코인 보유 유무
if bp43 > 10100:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode43 = False

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 보유중  |  매수가능 - {op_mode43} - 매수불가")
    print("")
else:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode43 = True

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 없음  |  매수가능 - {op_mode43} - 매수가능")
    print("")
time.sleep(1)


##### 44. 코인
# 보유수량 불러오기
krw_balance44 = upbit.get_balance(krw_coin44)
# 코인 현재가 불러오기
price44 = pyupbit.get_current_price(krw_coin44)
# 보유코인 원화금액으로 계산하기
bp44 = price44 * krw_balance44
# 코인 현황 출력.
print(f"44. 코인명 : {coin44}  |  현재가 = ￦{price44}  |  보유수량 = {krw_balance44}  |  평가금액 = ￦{bp44}")
# 코인 보유 유무
if bp44 > 10100:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode44 = False
    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 보유중  |  매수가능 - {op_mode44} - 매수불가")
    print("")
else:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode44 = True

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 없음  |  매수가능 - {op_mode44} - 매수가능")
    print("")
time.sleep(1)


##### 45. 코인
# 보유수량 불러오기
krw_balance45 = upbit.get_balance(krw_coin45)
# 코인 현재가 불러오기
price45 = pyupbit.get_current_price(krw_coin45)
# 보유코인 원화금액으로 계산하기
bp45 = price45 * krw_balance45
# 코인 현황 출력.
print(f"45. 코인명 : {coin45}  |  현재가 = ￦{price45}  |  보유수량 = {krw_balance45}  |  평가금액 = ￦{bp45}")
# 코인 보유 유무
if bp45 > 10100:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode45 = False

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 보유중  |  매수가능 - {op_mode45} - 매수불가")
    print("")
else:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode45 = True

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 없음  |  매수가능 - {op_mode45} - 매수가능")
    print("")
time.sleep(1)


##### 46. 코인
# 보유수량 불러오기
krw_balance46 = upbit.get_balance(krw_coin46)
# 코인 현재가 불러오기
price46 = pyupbit.get_current_price(krw_coin46)
# 보유코인 원화금액으로 계산하기
bp46 = price46 * krw_balance46
# 코인 현황 출력.
print(f"46. 코인명 : {coin46}  |  현재가 = ￦{price46}  |  보유수량 = {krw_balance46}  |  평가금액 = ￦{bp46}")
# 코인 보유 유무
if bp46 > 10100:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode46 = False

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 보유중  |  매수가능 - {op_mode46} - 매수불가")
    print("")
else:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode46 = True

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 없음  |  매수가능 - {op_mode46} - 매수가능")
    print("")
time.sleep(1)


##### 47. 코인
# 보유수량 불러오기
krw_balance47 = upbit.get_balance(krw_coin47)
# 코인 현재가 불러오기
price47 = pyupbit.get_current_price(krw_coin47)
# 보유코인 원화금액으로 계산하기
bp47 = price47 * krw_balance47
# 코인 현황 출력.
print(f"47. 코인명 : {coin47}  |  현재가 = ￦{price47}  |  보유수량 = {krw_balance47}  |  평가금액 = ￦{bp47}")
# 코인 보유 유무
if bp47 > 10100:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode47 = False

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 보유중  |  매수가능 - {op_mode47} - 매수불가")
    print("")
else:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode47 = True

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 없음  |  매수가능 - {op_mode47} - 매수가능")
    print("")
time.sleep(1)


##### 48. 코인
# 보유수량 불러오기
krw_balance48 = upbit.get_balance(krw_coin48)
# 코인 현재가 불러오기
price48 = pyupbit.get_current_price(krw_coin48)
# 보유코인 원화금액으로 계산하기
bp48 = price48 * krw_balance48
# 코인 현황 출력.
print(f"48. 코인명 : {coin48}  |  현재가 = ￦{price48}  |  보유수량 = {krw_balance48}  |  평가금액 = ￦{bp48}")
# 코인 보유 유무
if bp48 > 10100:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode48 = False

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 보유중  |  매수가능 - {op_mode48} - 매수불가")
    print("")
else:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode48 = True

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 없음  |  매수가능 - {op_mode48} - 매수가능")
    print("")
time.sleep(1)


##### 49. 코인
# 보유수량 불러오기
krw_balance49 = upbit.get_balance(krw_coin49)
# 코인 현재가 불러오기
price49 = pyupbit.get_current_price(krw_coin49)
# 보유코인 원화금액으로 계산하기
bp49 = price49 * krw_balance49
# 코인 현황 출력.
print(f"49. 코인명 : {coin49}  |  현재가 = ￦{price49}  |  보유수량 = {krw_balance49}  |  평가금액 = ￦{bp49}")
# 코인 보유 유무
if bp49 > 10100:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode49 = False

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 보유중  |  매수가능 - {op_mode49} - 매수불가")
    print("")
else:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode49 = True

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 없음  |  매수가능 - {op_mode49} - 매수가능")
    print("")
time.sleep(1)


##### 50. 코인
# 보유수량 불러오기
krw_balance50 = upbit.get_balance(krw_coin50)
# 코인 현재가 불러오기
price50 = pyupbit.get_current_price(krw_coin50)
# 보유코인 원화금액으로 계산하기
bp50 = price50 * krw_balance50
# 코인 현황 출력.
print(f"50. 코인명 : {coin50}  |  현재가 = ￦{price50}  |  보유수량 = {krw_balance50}  |  평가금액 = ￦{bp50}")
# 코인 보유 유무
if bp50 > 10100:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode50 = False

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 보유중  |  매수가능 - {op_mode50} - 매수불가")
    print("")
else:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode50 = True

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 없음  |  매수가능 - {op_mode50} - 매수가능")
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

    if now.hour == 1 or now.hour == 5 or now.hour == 9 or now.hour == 13 or now.hour == 17 or now.hour == 21:
        if now.minute == 0:
            # 총 평가금액 계산
            # 매수가능금액 불러오기
            krw = upbit.get_balance("KRW")
            ##### 매수가능금액을 평균구하기
            # 보유코인 합.
            total_bp1 = krw + bp1 + bp2 + bp3 + bp4 + bp5 + bp6 + bp7 + bp8 + bp9 + bp10
            total_bp2 = bp11 + bp12 + bp13 + bp14 + bp15 + bp16 + bp17 + bp18 + bp19 + bp20
            total_bp3 = bp21 + bp22 + bp23 + bp24 + bp25 + bp26 + bp27 + bp28 + bp29 + bp30
            total_bp4 = bp31 + bp32 + bp33 + bp34 + bp35 + bp36 + bp37 + bp38 + bp39 + bp40
            total_bp5 = bp41 + bp42 + bp43 + bp44 + bp45 + bp46 + bp47 + bp48 + bp49 + bp50
            # 보유코인 나누기
            total_sum1 = total_bp1 #/ 10
            total_sum2 = total_bp2 #/ 10
            total_sum3 = total_bp3 #/ 10
            total_sum4 = total_bp4 #/ 10
            total_sum5 = total_bp5 #/ 10
            # 매수가능 평균가.
            buy_krw = (total_sum1 + total_sum2 + total_sum3 + total_sum4 + total_sum5) / 50


            ###############################
            ##### 매매 : 1번코인 시작. #####

            ##### 코인보유현황
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
            #time.sleep(1)


            # 코인 현재가 불러오기
            price1 = pyupbit.get_current_price(krw_coin1)

            # MACD 조회.
            #macd1 = get_macd(krw_coin1)
            # 거래량 동반한 MACD 조회.
            macd1 = get_acc_macd(krw_coin1)
            # 20일 이평선 조회.
            #macd1 = get_ma20(krw_coin1)

            # 매수가능금액 불러오기
            krw1 = upbit.get_balance("KRW")

            # MACD 조건문
            #if macd1 >= 0 and ma1 > 0:     # macd가 0보다 높을때, ma가 0보다 높을때 매수
            if macd1 >= 0:     # macd가 0보다 높을때는 매수
                if op_mode1 == True:    # 매수 가능(True)일 경우 - 매수시도
                    if krw1 > buy_krw:      # 매수가능금액 krw1 가 매수평균가 buy_krw 보다 클때
                        if krw1 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                            if buy_krw > 10100:     # 매수평균가 buy_krw 가 10,100원 초과일 경우 : 매수
                                # 매수금액은 매수평균가 buy_krw 로
                                upbit.buy_market_order(krw_coin1, buy_krw * 0.99)   # 매수가능금액에서 1%를 빼고

                                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                                op_mode1 = False

                                # 1초 딜레이
                                #time.sleep(1)
                                # 보유수량 불러오기
                                krw_balance1 = upbit.get_balance(krw_coin1)
                                # 코인 현재가 불러오기
                                price1 = pyupbit.get_current_price(krw_coin1)
                                # 보유코인 원화금액으로 계산하기
                                bp1 = price1 * krw_balance1

                                # 보유 및 매수 가능 출력.
                                print(f"[ 1. {krw_coin1} 매수완료. ]")
                                print(f"매수시간 : {now}  |  코인명 : {coin1}  |  현재가 = ￦{price1}  |  MACD = ￦{macd1}  |  보유수량 = {krw_balance1}  |  평가금액 = ￦{bp1}")
                                print(f"매수가능 : {op_mode1} - 불가")
                                print("")

                            else:
                                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                                op_mode1 = False

                                print(f"[ 1. {krw_coin1} 잔고부족으로 매수불가. ]")
                                print(f"현재시간 : {now}  |  코인명 : {coin1}")
                                print(f"매수가능 : {op_mode1} - 불가")
                                print("")

                        else:
                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode1 = False

                            print(f"[ 1. {krw_coin1} 잔고부족으로 매수불가. ]")
                            print(f"현재시간 : {now}  |  코인명 : {coin1}")
                            print(f"매수가능 : {op_mode1} - 불가")
                            print("")

                    elif krw1 <= buy_krw:   # 매수가능금액 krw1 가 매수평균가 buy_krw 보다 같거나 작을때
                        if krw1 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                            # 매수금액은 매수가능금액인 krw1 로
                            upbit.buy_market_order(krw_coin1, krw1 * 0.99)   # 매수가능금액에서 1%를 빼고

                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode1 = False

                            # 1초 딜레이
                            #time.sleep(1)
                            # 보유수량 불러오기
                            krw_balance1 = upbit.get_balance(krw_coin1)
                            # 코인 현재가 불러오기
                            price1 = pyupbit.get_current_price(krw_coin1)
                            # 보유코인 원화금액으로 계산하기
                            bp1 = price1 * krw_balance1

                            # 보유 및 매수 가능 출력.
                            print(f"[ 1. {krw_coin1} 매수완료. ]")
                            print(f"매수시간 : {now}  |  코인명 : {coin1}  |  현재가 = ￦{price1}  |  MACD = ￦{macd1}  |  보유수량 = {krw_balance1}  |  평가금액 = ￦{bp1}")
                            print(f"매수가능 : {op_mode1} - 불가")
                            print("")

                        else:
                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode1 = False

                            print(f"[ 1. {krw_coin1} 잔고부족으로 매수불가. ]")
                            print(f"현재시간 : {now}  |  코인명 : {coin1}")
                            print(f"매수가능 : {op_mode1} - 불가")
                            print("")

            elif macd1 < 0:       # macd가 0보다 낮을때는 매도
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
                        print(f"매도시간 : {now}  |  코인명 : {coin1}  |  현재가 = ￦{price1}  |  MACD = ￦{macd1}  |  보유수량 = {krw_balance1}  |  평가금액 = ￦{bp1}")
                        print(f"매수가능 : {op_mode1} - 가능")
                        print("")

                    else:   # 보유코인 평가 금액이 10,100원 이하일때
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode1 = True

                        print(f"[ 1. {krw_coin1} 보유코인이 없으므로 매도불가. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin1}")
                        print(f"매수가능 : {op_mode1} - 가능")
                        print("")

            # 1초 딜레이.
            time.sleep(1)
            ##### 1번 코인 매매 종료 #####
            #############################


            ###############################
            ##### 매매 : 2번코인 시작. #####

            ##### 코인보유현황
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
            #time.sleep(1)


            # 코인 현재가 불러오기
            price2 = pyupbit.get_current_price(krw_coin2)

            # MACD 조회.
            #macd2 = get_macd(krw_coin2)
            # 거래량 동반한 MACD 조회.
            macd2 = get_acc_macd(krw_coin2)
            # 20일 이평선 조회.
            #macd2 = get_ma20(krw_coin2)

            # 매수가능금액 불러오기
            krw2 = upbit.get_balance("KRW")

            # MACD 조건문
            if macd2 >= 0:     # macd가 0보다 높을때는 매수
                if op_mode2 == True:    # 매수 가능(True)일 경우 - 매수시도
                    if krw2 > buy_krw:      # 매수가능금액 krw2 가 매수평균가 buy_krw 보다 클때
                        if krw2 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                            if buy_krw > 10100:     # 매수평균가 buy_krw 가 10,100원 초과일 경우 : 매수
                                # 매수금액은 매수평균가 buy_krw 로
                                upbit.buy_market_order(krw_coin2, buy_krw * 0.99)   # 매수가능금액에서 1%를 빼고

                                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                                op_mode2 = False

                                # 1초 딜레이
                                #time.sleep(1)
                                # 보유수량 불러오기
                                krw_balance2 = upbit.get_balance(krw_coin2)
                                # 코인 현재가 불러오기
                                price2 = pyupbit.get_current_price(krw_coin2)
                                # 보유코인 원화금액으로 계산하기
                                bp2 = price2 * krw_balance2

                                # 보유 및 매수 가능 출력.
                                print(f"[ 2. {krw_coin2} 매수완료. ]")
                                print(f"매수시간 : {now}  |  코인명 : {coin2}  |  현재가 = ￦{price2}  |  MACD = ￦{macd2}  |  보유수량 = {krw_balance2}  |  평가금액 = ￦{bp2}")
                                print(f"매수가능 : {op_mode2} - 불가")
                                print("")

                            else:
                                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                                op_mode2 = False

                                print(f"[ 2. {krw_coin2} 잔고부족으로 매수불가. ]")
                                print(f"현재시간 : {now}  |  코인명 : {coin2}")
                                print(f"매수가능 : {op_mode2} - 불가")
                                print("")

                        else:
                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode2 = False

                            print(f"[ 2. {krw_coin2} 잔고부족으로 매수불가. ]")
                            print(f"현재시간 : {now}  |  코인명 : {coin2}")
                            print(f"매수가능 : {op_mode2} - 불가")
                            print("")

                    elif krw2 <= buy_krw:   # 매수가능금액 krw2 가 매수평균가 buy_krw 보다 같거나 작을때
                        if krw2 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                            # 매수금액은 매수가능금액인 krw2 로
                            upbit.buy_market_order(krw_coin2, krw2 * 0.99)   # 매수가능금액에서 1%를 빼고

                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode2 = False

                            # 1초 딜레이
                            #time.sleep(1)
                            # 보유수량 불러오기
                            krw_balance2 = upbit.get_balance(krw_coin2)
                            # 코인 현재가 불러오기
                            price2 = pyupbit.get_current_price(krw_coin2)
                            # 보유코인 원화금액으로 계산하기
                            bp2 = price2 * krw_balance2

                            # 보유 및 매수 가능 출력.
                            print(f"[ 2. {krw_coin2} 매수완료. ]")
                            print(f"매수시간 : {now}  |  코인명 : {coin2}  |  현재가 = ￦{price2}  |  MACD = ￦{macd2}  |  보유수량 = {krw_balance2}  |  평가금액 = ￦{bp2}")
                            print(f"매수가능 : {op_mode2} - 불가")
                            print("")

                        else:
                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode2 = False

                            print(f"[ 2. {krw_coin2} 잔고부족으로 매수불가. ]")
                            print(f"현재시간 : {now}  |  코인명 : {coin2}")
                            print(f"매수가능 : {op_mode2} - 불가")
                            print("")

            elif macd2 < 0:       # macd가 0보다 낮을때는 매도
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
                        print(f"매도시간 : {now}  |  코인명 : {coin2}  |  현재가 = ￦{price2}  |  MACD = ￦{macd2}  |  보유수량 = {krw_balance2}  |  평가금액 = ￦{bp2}")
                        print(f"매수가능 : {op_mode2} - 가능")
                        print("")

                    else:   # 보유코인 평가 금액이 10,100원 이하일때
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode2 = True

                        print(f"[ 2. {krw_coin2} 보유코인이 없으므로 매도불가. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin2}")
                        print(f"매수가능 : {op_mode2} - 가능")
                        print("")

            # 1초 딜레이.
            time.sleep(1)
            ##### 2번 코인 매매 종료 #####
            #############################


            ###############################
            ##### 매매 : 3번코인 시작. #####

            ##### 코인보유현황
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
            #time.sleep(1)


            # 코인 현재가 불러오기
            price3 = pyupbit.get_current_price(krw_coin3)

            # MACD 조회.
            #macd3 = get_macd(krw_coin3)
            # 거래량 동반한 MACD 조회.
            macd3 = get_acc_macd(krw_coin3)
            # 20일 이평선 조회.
            #macd3 = get_ma20(krw_coin3)

            # 매수가능금액 불러오기
            krw3 = upbit.get_balance("KRW")

            # MACD 조건문
            if macd3 >= 0:     # macd가 0보다 높을때는 매수
                if op_mode3 == True:    # 매수 가능(True)일 경우 - 매수시도
                    if krw3 > buy_krw:      # 매수가능금액 krw3 가 매수평균가 buy_krw 보다 클때
                        if krw3 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                            if buy_krw > 10100:     # 매수평균가 buy_krw 가 10,100원 초과일 경우 : 매수
                                # 매수금액은 매수평균가 buy_krw 로
                                upbit.buy_market_order(krw_coin3, buy_krw * 0.99)   # 매수가능금액에서 1%를 빼고

                                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                                op_mode3 = False

                                # 1초 딜레이
                                #time.sleep(1)
                                # 보유수량 불러오기
                                krw_balance3 = upbit.get_balance(krw_coin3)
                                # 코인 현재가 불러오기
                                price3 = pyupbit.get_current_price(krw_coin3)
                                # 보유코인 원화금액으로 계산하기
                                bp3 = price3 * krw_balance3

                                # 보유 및 매수 가능 출력.
                                print(f"[ 3. {krw_coin3} 매수완료. ]")
                                print(f"매수시간 : {now}  |  코인명 : {coin3}  |  현재가 = ￦{price3}  |  MACD = ￦{macd3}  |  보유수량 = {krw_balance3}  |  평가금액 = ￦{bp3}")
                                print(f"매수가능 : {op_mode3} - 불가")
                                print("")

                            else:
                                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                                op_mode3 = False

                                print(f"[ 3. {krw_coin3} 잔고부족으로 매수불가. ]")
                                print(f"현재시간 : {now}  |  코인명 : {coin3}")
                                print(f"매수가능 : {op_mode3} - 불가")
                                print("")

                        else:
                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode3 = False

                            print(f"[ 3. {krw_coin3} 잔고부족으로 매수불가. ]")
                            print(f"현재시간 : {now}  |  코인명 : {coin3}")
                            print(f"매수가능 : {op_mode3} - 불가")
                            print("")

                    elif krw3 <= buy_krw:   # 매수가능금액 krw3 가 매수평균가 buy_krw 보다 같거나 작을때
                        if krw3 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                            # 매수금액은 매수가능금액인 krw3 로
                            upbit.buy_market_order(krw_coin3, krw3 * 0.99)   # 매수가능금액에서 1%를 빼고

                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode3 = False

                            # 1초 딜레이
                            #time.sleep(1)
                            # 보유수량 불러오기
                            krw_balance3 = upbit.get_balance(krw_coin3)
                            # 코인 현재가 불러오기
                            price3 = pyupbit.get_current_price(krw_coin3)
                            # 보유코인 원화금액으로 계산하기
                            bp3 = price3 * krw_balance3

                            # 보유 및 매수 가능 출력.
                            print(f"[ 3. {krw_coin3} 매수완료. ]")
                            print(f"매수시간 : {now}  |  코인명 : {coin3}  |  현재가 = ￦{price3}  |  MACD = ￦{macd3}  |  보유수량 = {krw_balance3}  |  평가금액 = ￦{bp3}")
                            print(f"매수가능 : {op_mode3} - 불가")
                            print("")

                        else:
                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode3 = False

                            print(f"[ 3. {krw_coin3} 잔고부족으로 매수불가. ]")
                            print(f"현재시간 : {now}  |  코인명 : {coin3}")
                            print(f"매수가능 : {op_mode3} - 불가")
                            print("")

            elif macd3 < 0:       # macd가 0보다 낮을때는 매도
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
                        print(f"매도시간 : {now}  |  코인명 : {coin3}  |  현재가 = ￦{price3}  |  MACD = ￦{macd3}  |  보유수량 = {krw_balance3}  |  평가금액 = ￦{bp3}")
                        print(f"매수가능 : {op_mode3} - 가능")
                        print("")

                    else:   # 보유코인 평가 금액이 10,100원 이하일때
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode3 = True

                        print(f"[ 3. {krw_coin3} 보유코인이 없으므로 매도불가. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin3}")
                        print(f"매수가능 : {op_mode3} - 가능")
                        print("")

            # 1초 딜레이.
            time.sleep(1)
            ##### 3번 코인 매매 종료 #####
            #############################


            ###############################
            ##### 매매 : 4번코인 시작. #####

            ##### 코인보유현황
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
            #time.sleep(1)


            # 코인 현재가 불러오기
            price4 = pyupbit.get_current_price(krw_coin4)

            # MACD 조회.
            #macd4 = get_macd(krw_coin4)
            # 거래량 동반한 MACD 조회.
            macd4 = get_acc_macd(krw_coin4)
            # 20일 이평선 조회.
            #macd4 = get_ma20(krw_coin4)

            # 매수가능금액 불러오기
            krw4 = upbit.get_balance("KRW")

            # MACD 조건문
            if macd4 >= 0:     # macd가 0보다 높을때는 매수
                if op_mode4 == True:    # 매수 가능(True)일 경우 - 매수시도
                    if krw4 > buy_krw:      # 매수가능금액 krw4 가 매수평균가 buy_krw 보다 클때
                        if krw4 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                            if buy_krw > 10100:     # 매수평균가 buy_krw 가 10,100원 초과일 경우 : 매수
                                # 매수금액은 매수평균가 buy_krw 로
                                upbit.buy_market_order(krw_coin4, buy_krw * 0.99)   # 매수가능금액에서 1%를 빼고

                                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                                op_mode4 = False

                                # 1초 딜레이
                                #time.sleep(1)
                                # 보유수량 불러오기
                                krw_balance4 = upbit.get_balance(krw_coin4)
                                # 코인 현재가 불러오기
                                price4 = pyupbit.get_current_price(krw_coin4)
                                # 보유코인 원화금액으로 계산하기
                                bp4 = price4 * krw_balance4

                                # 보유 및 매수 가능 출력.
                                print(f"[ 4. {krw_coin4} 매수완료. ]")
                                print(f"매수시간 : {now}  |  코인명 : {coin4}  |  현재가 = ￦{price4}  |  MACD = ￦{macd4}  |  보유수량 = {krw_balance4}  |  평가금액 = ￦{bp4}")
                                print(f"매수가능 : {op_mode4} - 불가")
                                print("")

                            else:
                                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                                op_mode4 = False

                                print(f"[ 4. {krw_coin4} 잔고부족으로 매수불가. ]")
                                print(f"현재시간 : {now}  |  코인명 : {coin4}")
                                print(f"매수가능 : {op_mode4} - 불가")
                                print("")

                        else:
                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode4 = False

                            print(f"[ 4. {krw_coin4} 잔고부족으로 매수불가. ]")
                            print(f"현재시간 : {now}  |  코인명 : {coin4}")
                            print(f"매수가능 : {op_mode4} - 불가")
                            print("")

                    elif krw4 <= buy_krw:   # 매수가능금액 krw4 가 매수평균가 buy_krw 보다 같거나 작을때
                        if krw4 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                            # 매수금액은 매수가능금액인 krw4 로
                            upbit.buy_market_order(krw_coin4, krw4 * 0.99)   # 매수가능금액에서 1%를 빼고

                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode4 = False

                            # 1초 딜레이
                            #time.sleep(1)
                            # 보유수량 불러오기
                            krw_balance4 = upbit.get_balance(krw_coin4)
                            # 코인 현재가 불러오기
                            price4 = pyupbit.get_current_price(krw_coin4)
                            # 보유코인 원화금액으로 계산하기
                            bp4 = price4 * krw_balance4

                            # 보유 및 매수 가능 출력.
                            print(f"[ 4. {krw_coin4} 매수완료. ]")
                            print(f"매수시간 : {now}  |  코인명 : {coin4}  |  현재가 = ￦{price4}  |  MACD = ￦{macd4}  |  보유수량 = {krw_balance4}  |  평가금액 = ￦{bp4}")
                            print(f"매수가능 : {op_mode4} - 불가")
                            print("")

                        else:
                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode4 = False

                            print(f"[ 4. {krw_coin4} 잔고부족으로 매수불가. ]")
                            print(f"현재시간 : {now}  |  코인명 : {coin4}")
                            print(f"매수가능 : {op_mode4} - 불가")
                            print("")

            elif macd4 < 0:       # macd가 0보다 낮을때는 매도
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
                        print(f"매도시간 : {now}  |  코인명 : {coin4}  |  현재가 = ￦{price4}  |  MACD = ￦{macd4}  |  보유수량 = {krw_balance4}  |  평가금액 = ￦{bp4}")
                        print(f"매수가능 : {op_mode4} - 가능")
                        print("")

                    else:   # 보유코인 평가 금액이 10,100원 이하일때
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode4 = True

                        print(f"[ 4. {krw_coin4} 보유코인이 없으므로 매도불가. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin4}")
                        print(f"매수가능 : {op_mode4} - 가능")
                        print("")

            # 1초 딜레이.
            time.sleep(1)
            ##### 4번 코인 매매 종료 #####
            #############################


            ###############################
            ##### 매매 : 5번코인 시작. #####

            ##### 코인보유현황
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
            #time.sleep(1)


            # 코인 현재가 불러오기
            price5 = pyupbit.get_current_price(krw_coin5)

            # MACD 조회.
            #macd5 = get_macd(krw_coin5)
            # 거래량 동반한 MACD 조회.
            macd5 = get_acc_macd(krw_coin5)
            # 20일 이평선 조회.
            #macd5 = get_ma20(krw_coin5)

            # 매수가능금액 불러오기
            krw5 = upbit.get_balance("KRW")

            # MACD 조건문
            if macd5 >= 0:     # macd가 0보다 높을때는 매수
                if op_mode5 == True:    # 매수 가능(True)일 경우 - 매수시도
                    if krw5 > buy_krw:      # 매수가능금액 krw5 가 매수평균가 buy_krw 보다 클때
                        if krw5 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                            if buy_krw > 10100:     # 매수평균가 buy_krw 가 10,100원 초과일 경우 : 매수
                                # 매수금액은 매수평균가 buy_krw 로
                                upbit.buy_market_order(krw_coin5, buy_krw * 0.99)   # 매수가능금액에서 1%를 빼고

                                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                                op_mode5 = False

                                # 1초 딜레이
                                #time.sleep(1)
                                # 보유수량 불러오기
                                krw_balance5 = upbit.get_balance(krw_coin5)
                                # 코인 현재가 불러오기
                                price5 = pyupbit.get_current_price(krw_coin5)
                                # 보유코인 원화금액으로 계산하기
                                bp5 = price5 * krw_balance5

                                # 보유 및 매수 가능 출력.
                                print(f"[ 5. {krw_coin5} 매수완료. ]")
                                print(f"매수시간 : {now}  |  코인명 : {coin5}  |  현재가 = ￦{price5}  |  MACD = ￦{macd5}  |  보유수량 = {krw_balance5}  |  평가금액 = ￦{bp5}")
                                print(f"매수가능 : {op_mode5} - 불가")
                                print("")

                            else:
                                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                                op_mode5 = False

                                print(f"[ 5. {krw_coin5} 잔고부족으로 매수불가. ]")
                                print(f"현재시간 : {now}  |  코인명 : {coin5}")
                                print(f"매수가능 : {op_mode5} - 불가")
                                print("")

                        else:
                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode5 = False

                            print(f"[ 5. {krw_coin5} 잔고부족으로 매수불가. ]")
                            print(f"현재시간 : {now}  |  코인명 : {coin5}")
                            print(f"매수가능 : {op_mode5} - 불가")
                            print("")

                    elif krw5 <= buy_krw:   # 매수가능금액 krw5 가 매수평균가 buy_krw 보다 같거나 작을때
                        if krw5 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                            # 매수금액은 매수가능금액인 krw5 로
                            upbit.buy_market_order(krw_coin5, krw5 * 0.99)   # 매수가능금액에서 1%를 빼고

                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode5 = False

                            # 1초 딜레이
                            #time.sleep(1)
                            # 보유수량 불러오기
                            krw_balance5 = upbit.get_balance(krw_coin5)
                            # 코인 현재가 불러오기
                            price5 = pyupbit.get_current_price(krw_coin5)
                            # 보유코인 원화금액으로 계산하기
                            bp5 = price5 * krw_balance5

                            # 보유 및 매수 가능 출력.
                            print(f"[ 5. {krw_coin5} 매수완료. ]")
                            print(f"매수시간 : {now}  |  코인명 : {coin5}  |  현재가 = ￦{price5}  |  MACD = ￦{macd5}  |  보유수량 = {krw_balance5}  |  평가금액 = ￦{bp5}")
                            print(f"매수가능 : {op_mode5} - 불가")
                            print("")

                        else:
                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode5 = False

                            print(f"[ 5. {krw_coin5} 잔고부족으로 매수불가. ]")
                            print(f"현재시간 : {now}  |  코인명 : {coin5}")
                            print(f"매수가능 : {op_mode5} - 불가")
                            print("")

            elif macd5 < 0:       # macd가 0보다 낮을때는 매도
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
                        print(f"매도시간 : {now}  |  코인명 : {coin5}  |  현재가 = ￦{price5}  |  MACD = ￦{macd5}  |  보유수량 = {krw_balance5}  |  평가금액 = ￦{bp5}")
                        print(f"매수가능 : {op_mode5} - 가능")
                        print("")

                    else:   # 보유코인 평가 금액이 10,100원 이하일때
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode5 = True

                        print(f"[ 5. {krw_coin5} 보유코인이 없으므로 매도불가. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin5}")
                        print(f"매수가능 : {op_mode5} - 가능")
                        print("")

            # 1초 딜레이.
            time.sleep(1)
            ##### 5번 코인 매매 종료 #####
            #############################


            ###############################
            ##### 매매 : 6번코인 시작. #####

            ##### 코인보유현황
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
            #time.sleep(1)


            # 코인 현재가 불러오기
            price6 = pyupbit.get_current_price(krw_coin6)

            # MACD 조회.
            #macd6 = get_macd(krw_coin6)
            # 거래량 동반한 MACD 조회.
            macd6 = get_acc_macd(krw_coin6)
            # 20일 이평선 조회.
            #macd6 = get_ma20(krw_coin6)

            # 매수가능금액 불러오기
            krw6 = upbit.get_balance("KRW")

            # MACD 조건문
            if macd6 >= 0:     # macd가 0보다 높을때는 매수
                if op_mode6 == True:    # 매수 가능(True)일 경우 - 매수시도
                    if krw6 > buy_krw:      # 매수가능금액 krw6 가 매수평균가 buy_krw 보다 클때
                        if krw6 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                            if buy_krw > 10100:     # 매수평균가 buy_krw 가 10,100원 초과일 경우 : 매수
                                # 매수금액은 매수평균가 buy_krw 로
                                upbit.buy_market_order(krw_coin6, buy_krw * 0.99)   # 매수가능금액에서 1%를 빼고

                                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                                op_mode6 = False

                                # 1초 딜레이
                                #time.sleep(1)
                                # 보유수량 불러오기
                                krw_balance6 = upbit.get_balance(krw_coin6)
                                # 코인 현재가 불러오기
                                price6 = pyupbit.get_current_price(krw_coin6)
                                # 보유코인 원화금액으로 계산하기
                                bp6 = price6 * krw_balance6

                                # 보유 및 매수 가능 출력.
                                print(f"[ 6. {krw_coin6} 매수완료. ]")
                                print(f"매수시간 : {now}  |  코인명 : {coin6}  |  현재가 = ￦{price6}  |  MACD = ￦{macd6}  |  보유수량 = {krw_balance6}  |  평가금액 = ￦{bp6}")
                                print(f"매수가능 : {op_mode6} - 불가")
                                print("")

                            else:
                                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                                op_mode6 = False

                                print(f"[ 6. {krw_coin6} 잔고부족으로 매수불가. ]")
                                print(f"현재시간 : {now}  |  코인명 : {coin6}")
                                print(f"매수가능 : {op_mode6} - 불가")
                                print("")

                        else:
                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode6 = False

                            print(f"[ 6. {krw_coin6} 잔고부족으로 매수불가. ]")
                            print(f"현재시간 : {now}  |  코인명 : {coin6}")
                            print(f"매수가능 : {op_mode6} - 불가")
                            print("")

                    elif krw6 <= buy_krw:   # 매수가능금액 krw6 가 매수평균가 buy_krw 보다 같거나 작을때
                        if krw6 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                            # 매수금액은 매수가능금액인 krw6 로
                            upbit.buy_market_order(krw_coin6, krw6 * 0.99)   # 매수가능금액에서 1%를 빼고

                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode6 = False

                            # 1초 딜레이
                            #time.sleep(1)
                            # 보유수량 불러오기
                            krw_balance6 = upbit.get_balance(krw_coin6)
                            # 코인 현재가 불러오기
                            price6 = pyupbit.get_current_price(krw_coin6)
                            # 보유코인 원화금액으로 계산하기
                            bp6 = price6 * krw_balance6

                            # 보유 및 매수 가능 출력.
                            print(f"[ 6. {krw_coin6} 매수완료. ]")
                            print(f"매수시간 : {now}  |  코인명 : {coin6}  |  현재가 = ￦{price6}  |  MACD = ￦{macd6}  |  보유수량 = {krw_balance6}  |  평가금액 = ￦{bp6}")
                            print(f"매수가능 : {op_mode6} - 불가")
                            print("")

                        else:
                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode6 = False

                            print(f"[ 6. {krw_coin6} 잔고부족으로 매수불가. ]")
                            print(f"현재시간 : {now}  |  코인명 : {coin6}")
                            print(f"매수가능 : {op_mode6} - 불가")
                            print("")

            elif macd6 < 0:       # macd가 0보다 낮을때는 매도
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
                        print(f"매도시간 : {now}  |  코인명 : {coin6}  |  현재가 = ￦{price6}  |  MACD = ￦{macd6}  |  보유수량 = {krw_balance6}  |  평가금액 = ￦{bp6}")
                        print(f"매수가능 : {op_mode6} - 가능")
                        print("")

                    else:   # 보유코인 평가 금액이 10,100원 이하일때
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode6 = True

                        print(f"[ 6. {krw_coin6} 보유코인이 없으므로 매도불가. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin6}")
                        print(f"매수가능 : {op_mode6} - 가능")
                        print("")

            # 1초 딜레이.
            time.sleep(1)
            ##### 6번 코인 매매 종료 #####
            #############################


            ###############################
            ##### 매매 : 7번코인 시작. #####

            ##### 코인보유현황
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
            #time.sleep(1)


            # 코인 현재가 불러오기
            price7 = pyupbit.get_current_price(krw_coin7)

            # MACD 조회.
            #macd7 = get_macd(krw_coin7)
            # 거래량 동반한 MACD 조회.
            macd7 = get_acc_macd(krw_coin7)
            # 20일 이평선 조회.
            #macd7 = get_ma20(krw_coin7)

            # 매수가능금액 불러오기
            krw7 = upbit.get_balance("KRW")

            # MACD 조건문
            if macd7 >= 0:     # macd가 0보다 높을때는 매수
                if op_mode7 == True:    # 매수 가능(True)일 경우 - 매수시도
                    if krw7 > buy_krw:      # 매수가능금액 krw7 가 매수평균가 buy_krw 보다 클때
                        if krw7 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                            if buy_krw > 10100:     # 매수평균가 buy_krw 가 10,100원 초과일 경우 : 매수
                                # 매수금액은 매수평균가 buy_krw 로
                                upbit.buy_market_order(krw_coin7, buy_krw * 0.99)   # 매수가능금액에서 1%를 빼고

                                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                                op_mode7 = False

                                # 1초 딜레이
                                #time.sleep(1)
                                # 보유수량 불러오기
                                krw_balance7 = upbit.get_balance(krw_coin7)
                                # 코인 현재가 불러오기
                                price7 = pyupbit.get_current_price(krw_coin7)
                                # 보유코인 원화금액으로 계산하기
                                bp7 = price7 * krw_balance7

                                # 보유 및 매수 가능 출력.
                                print(f"[ 7. {krw_coin7} 매수완료. ]")
                                print(f"매수시간 : {now}  |  코인명 : {coin7}  |  현재가 = ￦{price7}  |  MACD = ￦{macd7}  |  보유수량 = {krw_balance7}  |  평가금액 = ￦{bp7}")
                                print(f"매수가능 : {op_mode7} - 불가")
                                print("")

                            else:
                                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                                op_mode7 = False

                                print(f"[ 7. {krw_coin7} 잔고부족으로 매수불가. ]")
                                print(f"현재시간 : {now}  |  코인명 : {coin7}")
                                print(f"매수가능 : {op_mode7} - 불가")
                                print("")

                        else:
                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode7 = False

                            print(f"[ 7. {krw_coin7} 잔고부족으로 매수불가. ]")
                            print(f"현재시간 : {now}  |  코인명 : {coin7}")
                            print(f"매수가능 : {op_mode7} - 불가")
                            print("")

                    elif krw7 <= buy_krw:   # 매수가능금액 krw7 가 매수평균가 buy_krw 보다 같거나 작을때
                        if krw7 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                            # 매수금액은 매수가능금액인 krw7 로
                            upbit.buy_market_order(krw_coin7, krw7 * 0.99)   # 매수가능금액에서 1%를 빼고

                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode7 = False

                            # 1초 딜레이
                            #time.sleep(1)
                            # 보유수량 불러오기
                            krw_balance7 = upbit.get_balance(krw_coin7)
                            # 코인 현재가 불러오기
                            price7 = pyupbit.get_current_price(krw_coin7)
                            # 보유코인 원화금액으로 계산하기
                            bp7 = price7 * krw_balance7

                            # 보유 및 매수 가능 출력.
                            print(f"[ 7. {krw_coin7} 매수완료. ]")
                            print(f"매수시간 : {now}  |  코인명 : {coin7}  |  현재가 = ￦{price7}  |  MACD = ￦{macd7}  |  보유수량 = {krw_balance7}  |  평가금액 = ￦{bp7}")
                            print(f"매수가능 : {op_mode7} - 불가")
                            print("")

                        else:
                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode7 = False

                            print(f"[ 7. {krw_coin7} 잔고부족으로 매수불가. ]")
                            print(f"현재시간 : {now}  |  코인명 : {coin7}")
                            print(f"매수가능 : {op_mode7} - 불가")
                            print("")

            elif macd7 < 0:       # macd가 0보다 낮을때는 매도
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
                        print(f"매도시간 : {now}  |  코인명 : {coin7}  |  현재가 = ￦{price7}  |  MACD = ￦{macd7}  |  보유수량 = {krw_balance7}  |  평가금액 = ￦{bp7}")
                        print(f"매수가능 : {op_mode7} - 가능")
                        print("")

                    else:   # 보유코인 평가 금액이 10,100원 이하일때
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode7 = True

                        print(f"[ 7. {krw_coin7} 보유코인이 없으므로 매도불가. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin7}")
                        print(f"매수가능 : {op_mode7} - 가능")
                        print("")

            # 1초 딜레이.
            time.sleep(1)
            ##### 7번 코인 매매 종료 #####
            #############################


            ###############################
            ##### 매매 : 8번코인 시작. #####

            ##### 코인보유현황
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
            #time.sleep(1)


            # 코인 현재가 불러오기
            price8 = pyupbit.get_current_price(krw_coin8)

            # MACD 조회.
            #macd8 = get_macd(krw_coin8)
            # 거래량 동반한 MACD 조회.
            macd8 = get_acc_macd(krw_coin8)
            # 20일 이평선 조회.
            #macd8 = get_ma20(krw_coin8)

            # 매수가능금액 불러오기
            krw8 = upbit.get_balance("KRW")

            # MACD 조건문
            if macd8 >= 0:     # macd가 0보다 높을때는 매수
                if op_mode8 == True:    # 매수 가능(True)일 경우 - 매수시도
                    if krw8 > buy_krw:      # 매수가능금액 krw8 가 매수평균가 buy_krw 보다 클때
                        if krw8 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                            if buy_krw > 10100:     # 매수평균가 buy_krw 가 10,100원 초과일 경우 : 매수
                                # 매수금액은 매수평균가 buy_krw 로
                                upbit.buy_market_order(krw_coin8, buy_krw * 0.99)   # 매수가능금액에서 1%를 빼고

                                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                                op_mode8 = False

                                # 1초 딜레이
                                #time.sleep(1)
                                # 보유수량 불러오기
                                krw_balance8 = upbit.get_balance(krw_coin8)
                                # 코인 현재가 불러오기
                                price8 = pyupbit.get_current_price(krw_coin8)
                                # 보유코인 원화금액으로 계산하기
                                bp8 = price8 * krw_balance8

                                # 보유 및 매수 가능 출력.
                                print(f"[ 8. {krw_coin8} 매수완료. ]")
                                print(f"매수시간 : {now}  |  코인명 : {coin8}  |  현재가 = ￦{price8}  |  MACD = ￦{macd8}  |  보유수량 = {krw_balance8}  |  평가금액 = ￦{bp8}")
                                print(f"매수가능 : {op_mode8} - 불가")
                                print("")

                            else:
                                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                                op_mode8 = False

                                print(f"[ 8. {krw_coin8} 잔고부족으로 매수불가. ]")
                                print(f"현재시간 : {now}  |  코인명 : {coin8}")
                                print(f"매수가능 : {op_mode8} - 불가")
                                print("")

                        else:
                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode8 = False

                            print(f"[ 8. {krw_coin8} 잔고부족으로 매수불가. ]")
                            print(f"현재시간 : {now}  |  코인명 : {coin8}")
                            print(f"매수가능 : {op_mode8} - 불가")
                            print("")

                    elif krw8 <= buy_krw:   # 매수가능금액 krw8 가 매수평균가 buy_krw 보다 같거나 작을때
                        if krw8 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                            # 매수금액은 매수가능금액인 krw8 로
                            upbit.buy_market_order(krw_coin8, krw8 * 0.99)   # 매수가능금액에서 1%를 빼고

                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode8 = False

                            # 1초 딜레이
                            #time.sleep(1)
                            # 보유수량 불러오기
                            krw_balance8 = upbit.get_balance(krw_coin8)
                            # 코인 현재가 불러오기
                            price8 = pyupbit.get_current_price(krw_coin8)
                            # 보유코인 원화금액으로 계산하기
                            bp8 = price8 * krw_balance8

                            # 보유 및 매수 가능 출력.
                            print(f"[ 8. {krw_coin8} 매수완료. ]")
                            print(f"매수시간 : {now}  |  코인명 : {coin8}  |  현재가 = ￦{price8}  |  MACD = ￦{macd8}  |  보유수량 = {krw_balance8}  |  평가금액 = ￦{bp8}")
                            print(f"매수가능 : {op_mode8} - 불가")
                            print("")

                        else:
                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode8 = False

                            print(f"[ 8. {krw_coin8} 잔고부족으로 매수불가. ]")
                            print(f"현재시간 : {now}  |  코인명 : {coin8}")
                            print(f"매수가능 : {op_mode8} - 불가")
                            print("")

            elif macd8 < 0:       # macd가 0보다 낮을때는 매도
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
                        print(f"매도시간 : {now}  |  코인명 : {coin8}  |  현재가 = ￦{price8}  |  MACD = ￦{macd8}  |  보유수량 = {krw_balance8}  |  평가금액 = ￦{bp8}")
                        print(f"매수가능 : {op_mode8} - 가능")
                        print("")

                    else:   # 보유코인 평가 금액이 10,100원 이하일때
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode8 = True

                        print(f"[ 8. {krw_coin8} 보유코인이 없으므로 매도불가. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin8}")
                        print(f"매수가능 : {op_mode8} - 가능")
                        print("")

            # 1초 딜레이.
            time.sleep(1)
            ##### 8번 코인 매매 종료 #####
            #############################


            ###############################
            ##### 매매 : 9번코인 시작. #####

            ##### 코인보유현황
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
            #time.sleep(1)


            # 코인 현재가 불러오기
            price9 = pyupbit.get_current_price(krw_coin9)

            # MACD 조회.
            #macd9 = get_macd(krw_coin9)
            # 거래량 동반한 MACD 조회.
            macd9 = get_acc_macd(krw_coin9)
            # 20일 이평선 조회.
            #macd9 = get_ma20(krw_coin9)

            # 매수가능금액 불러오기
            krw9 = upbit.get_balance("KRW")

            # MACD 조건문
            if macd9 >= 0:     # macd가 0보다 높을때는 매수
                if op_mode9 == True:    # 매수 가능(True)일 경우 - 매수시도
                    if krw9 > buy_krw:      # 매수가능금액 krw9 가 매수평균가 buy_krw 보다 클때
                        if krw9 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                            if buy_krw > 10100:     # 매수평균가 buy_krw 가 10,100원 초과일 경우 : 매수
                                # 매수금액은 매수평균가 buy_krw 로
                                upbit.buy_market_order(krw_coin9, buy_krw * 0.99)   # 매수가능금액에서 1%를 빼고

                                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                                op_mode9 = False

                                # 1초 딜레이
                                #time.sleep(1)
                                # 보유수량 불러오기
                                krw_balance9 = upbit.get_balance(krw_coin9)
                                # 코인 현재가 불러오기
                                price9 = pyupbit.get_current_price(krw_coin9)
                                # 보유코인 원화금액으로 계산하기
                                bp9 = price9 * krw_balance9

                                # 보유 및 매수 가능 출력.
                                print(f"[ 9. {krw_coin9} 매수완료. ]")
                                print(f"매수시간 : {now}  |  코인명 : {coin9}  |  현재가 = ￦{price9}  |  MACD = ￦{macd9}  |  보유수량 = {krw_balance9}  |  평가금액 = ￦{bp9}")
                                print(f"매수가능 : {op_mode9} - 불가")
                                print("")

                            else:
                                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                                op_mode9 = False

                                print(f"[ 9. {krw_coin9} 잔고부족으로 매수불가. ]")
                                print(f"현재시간 : {now}  |  코인명 : {coin9}")
                                print(f"매수가능 : {op_mode9} - 불가")
                                print("")

                        else:
                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode9 = False

                            print(f"[ 9. {krw_coin9} 잔고부족으로 매수불가. ]")
                            print(f"현재시간 : {now}  |  코인명 : {coin9}")
                            print(f"매수가능 : {op_mode9} - 불가")
                            print("")

                    elif krw9 <= buy_krw:   # 매수가능금액 krw9 가 매수평균가 buy_krw 보다 같거나 작을때
                        if krw9 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                            # 매수금액은 매수가능금액인 krw9 로
                            upbit.buy_market_order(krw_coin9, krw9 * 0.99)   # 매수가능금액에서 1%를 빼고

                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode9 = False

                            # 1초 딜레이
                            #time.sleep(1)
                            # 보유수량 불러오기
                            krw_balance9 = upbit.get_balance(krw_coin9)
                            # 코인 현재가 불러오기
                            price9 = pyupbit.get_current_price(krw_coin9)
                            # 보유코인 원화금액으로 계산하기
                            bp9 = price9 * krw_balance9

                            # 보유 및 매수 가능 출력.
                            print(f"[ 9. {krw_coin9} 매수완료. ]")
                            print(f"매수시간 : {now}  |  코인명 : {coin9}  |  현재가 = ￦{price9}  |  MACD = ￦{macd9}  |  보유수량 = {krw_balance9}  |  평가금액 = ￦{bp9}")
                            print(f"매수가능 : {op_mode9} - 불가")
                            print("")

                        else:
                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode9 = False

                            print(f"[ 9. {krw_coin9} 잔고부족으로 매수불가. ]")
                            print(f"현재시간 : {now}  |  코인명 : {coin9}")
                            print(f"매수가능 : {op_mode9} - 불가")
                            print("")

            elif macd9 < 0:       # macd가 0보다 낮을때는 매도
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
                        print(f"매도시간 : {now}  |  코인명 : {coin9}  |  현재가 = ￦{price9}  |  MACD = ￦{macd9}  |  보유수량 = {krw_balance9}  |  평가금액 = ￦{bp9}")
                        print(f"매수가능 : {op_mode9} - 가능")
                        print("")

                    else:   # 보유코인 평가 금액이 10,100원 이하일때
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode9 = True

                        print(f"[ 9. {krw_coin9} 보유코인이 없으므로 매도불가. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin9}")
                        print(f"매수가능 : {op_mode9} - 가능")
                        print("")

            # 1초 딜레이.
            time.sleep(1)
            ##### 9번 코인 매매 종료 #####
            #############################


            ###############################
            ##### 매매 : 10번코인 시작. #####

            ##### 코인보유현황
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
            #time.sleep(1)


            # 코인 현재가 불러오기
            price10 = pyupbit.get_current_price(krw_coin10)

            # MACD 조회.
            #macd10 = get_macd(krw_coin10)
            # 거래량 동반한 MACD 조회.
            macd10 = get_acc_macd(krw_coin10)
            # 20일 이평선 조회.
            #macd10 = get_ma20(krw_coin10)

            # 매수가능금액 불러오기
            krw10 = upbit.get_balance("KRW")

            # MACD 조건문
            if macd10 >= 0:     # macd가 0보다 높을때는 매수
                if op_mode10 == True:    # 매수 가능(True)일 경우 - 매수시도
                    if krw10 > buy_krw:      # 매수가능금액 krw10 가 매수평균가 buy_krw 보다 클때
                        if krw10 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                            if buy_krw > 10100:     # 매수평균가 buy_krw 가 10,100원 초과일 경우 : 매수
                                # 매수금액은 매수평균가 buy_krw 로
                                upbit.buy_market_order(krw_coin10, buy_krw * 0.99)   # 매수가능금액에서 1%를 빼고

                                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                                op_mode10 = False

                                # 1초 딜레이
                                #time.sleep(1)
                                # 보유수량 불러오기
                                krw_balance10 = upbit.get_balance(krw_coin10)
                                # 코인 현재가 불러오기
                                price10 = pyupbit.get_current_price(krw_coin10)
                                # 보유코인 원화금액으로 계산하기
                                bp10 = price10 * krw_balance10

                                # 보유 및 매수 가능 출력.
                                print(f"[ 10. {krw_coin10} 매수완료. ]")
                                print(f"매수시간 : {now}  |  코인명 : {coin10}  |  현재가 = ￦{price10}  |  MACD = ￦{macd10}  |  보유수량 = {krw_balance10}  |  평가금액 = ￦{bp10}")
                                print(f"매수가능 : {op_mode10} - 불가")
                                print("")

                            else:
                                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                                op_mode10 = False

                                print(f"[ 10. {krw_coin10} 잔고부족으로 매수불가. ]")
                                print(f"현재시간 : {now}  |  코인명 : {coin10}")
                                print(f"매수가능 : {op_mode10} - 불가")
                                print("")

                        else:
                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode10 = False

                            print(f"[ 10. {krw_coin10} 잔고부족으로 매수불가. ]")
                            print(f"현재시간 : {now}  |  코인명 : {coin10}")
                            print(f"매수가능 : {op_mode10} - 불가")
                            print("")

                    elif krw10 <= buy_krw:   # 매수가능금액 krw10 가 매수평균가 buy_krw 보다 같거나 작을때
                        if krw10 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                            # 매수금액은 매수가능금액인 krw10 로
                            upbit.buy_market_order(krw_coin10, krw10 * 0.99)   # 매수가능금액에서 1%를 빼고

                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode10 = False

                            # 1초 딜레이
                            #time.sleep(1)
                            # 보유수량 불러오기
                            krw_balance10 = upbit.get_balance(krw_coin10)
                            # 코인 현재가 불러오기
                            price10 = pyupbit.get_current_price(krw_coin10)
                            # 보유코인 원화금액으로 계산하기
                            bp10 = price10 * krw_balance10

                            # 보유 및 매수 가능 출력.
                            print(f"[ 10. {krw_coin10} 매수완료. ]")
                            print(f"매수시간 : {now}  |  코인명 : {coin10}  |  현재가 = ￦{price10}  |  MACD = ￦{macd10}  |  보유수량 = {krw_balance10}  |  평가금액 = ￦{bp10}")
                            print(f"매수가능 : {op_mode10} - 불가")
                            print("")

                        else:
                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode10 = False

                            print(f"[ 10. {krw_coin10} 잔고부족으로 매수불가. ]")
                            print(f"현재시간 : {now}  |  코인명 : {coin10}")
                            print(f"매수가능 : {op_mode10} - 불가")
                            print("")

            elif macd10 < 0:       # macd가 0보다 낮을때는 매도
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
                        print(f"매도시간 : {now}  |  코인명 : {coin10}  |  현재가 = ￦{price10}  |  MACD = ￦{macd10}  |  보유수량 = {krw_balance10}  |  평가금액 = ￦{bp10}")
                        print(f"매수가능 : {op_mode10} - 가능")
                        print("")

                    else:   # 보유코인 평가 금액이 10,100원 이하일때
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode10 = True

                        print(f"[ 10. {krw_coin10} 보유코인이 없으므로 매도불가. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin10}")
                        print(f"매수가능 : {op_mode10} - 가능")
                        print("")

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

            ##### 코인보유현황
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
            #time.sleep(1)


            # 코인 현재가 불러오기
            price11 = pyupbit.get_current_price(krw_coin11)

            # MACD 조회.
            #macd11 = get_macd(krw_coin11)
            # 거래량 동반한 MACD 조회.
            macd11 = get_acc_macd(krw_coin11)
            # 20일 이평선 조회.
            #macd11 = get_ma20(krw_coin11)

            # 매수가능금액 불러오기
            krw11 = upbit.get_balance("KRW")

            # MACD 조건문
            if macd11 >= 0:     # macd가 0보다 높을때는 매수
                if op_mode11 == True:    # 매수 가능(True)일 경우 - 매수시도
                    if krw11 > buy_krw:      # 매수가능금액 krw11 가 매수평균가 buy_krw 보다 클때
                        if krw11 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                            if buy_krw > 10100:     # 매수평균가 buy_krw 가 10,100원 초과일 경우 : 매수
                                # 매수금액은 매수평균가 buy_krw 로
                                upbit.buy_market_order(krw_coin11, buy_krw * 0.99)   # 매수가능금액에서 1%를 빼고

                                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                                op_mode11 = False

                                # 1초 딜레이
                                #time.sleep(1)
                                # 보유수량 불러오기
                                krw_balance11 = upbit.get_balance(krw_coin11)
                                # 코인 현재가 불러오기
                                price11 = pyupbit.get_current_price(krw_coin11)
                                # 보유코인 원화금액으로 계산하기
                                bp11 = price11 * krw_balance11

                                # 보유 및 매수 가능 출력.
                                print(f"[ 11. {krw_coin11} 매수완료. ]")
                                print(f"매수시간 : {now}  |  코인명 : {coin11}  |  현재가 = ￦{price11}  |  MACD = ￦{macd11}  |  보유수량 = {krw_balance11}  |  평가금액 = ￦{bp11}")
                                print(f"매수가능 : {op_mode11} - 불가")
                                print("")

                            else:
                                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                                op_mode11 = False

                                print(f"[ 11. {krw_coin11} 잔고부족으로 매수불가. ]")
                                print(f"현재시간 : {now}  |  코인명 : {coin11}")
                                print(f"매수가능 : {op_mode11} - 불가")
                                print("")

                        else:
                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode11 = False

                            print(f"[ 11. {krw_coin11} 잔고부족으로 매수불가. ]")
                            print(f"현재시간 : {now}  |  코인명 : {coin11}")
                            print(f"매수가능 : {op_mode11} - 불가")
                            print("")

                    elif krw11 <= buy_krw:   # 매수가능금액 krw11 가 매수평균가 buy_krw 보다 같거나 작을때
                        if krw11 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                            # 매수금액은 매수가능금액인 krw11 로
                            upbit.buy_market_order(krw_coin11, krw11 * 0.99)   # 매수가능금액에서 1%를 빼고

                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode11 = False

                            # 1초 딜레이
                            #time.sleep(1)
                            # 보유수량 불러오기
                            krw_balance11 = upbit.get_balance(krw_coin11)
                            # 코인 현재가 불러오기
                            price11 = pyupbit.get_current_price(krw_coin11)
                            # 보유코인 원화금액으로 계산하기
                            bp11 = price11 * krw_balance11

                            # 보유 및 매수 가능 출력.
                            print(f"[ 11. {krw_coin11} 매수완료. ]")
                            print(f"매수시간 : {now}  |  코인명 : {coin11}  |  현재가 = ￦{price11}  |  MACD = ￦{macd11}  |  보유수량 = {krw_balance11}  |  평가금액 = ￦{bp11}")
                            print(f"매수가능 : {op_mode11} - 불가")
                            print("")

                        else:
                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode11 = False

                            print(f"[ 11. {krw_coin11} 잔고부족으로 매수불가. ]")
                            print(f"현재시간 : {now}  |  코인명 : {coin11}")
                            print(f"매수가능 : {op_mode11} - 불가")
                            print("")

            elif macd11 < 0:       # macd가 0보다 낮을때는 매도
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
                        print(f"매도시간 : {now}  |  코인명 : {coin11}  |  현재가 = ￦{price11}  |  MACD = ￦{macd11}  |  보유수량 = {krw_balance11}  |  평가금액 = ￦{bp11}")
                        print(f"매수가능 : {op_mode11} - 가능")
                        print("")

                    else:   # 보유코인 평가 금액이 10,100원 이하일때
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode11 = True

                        print(f"[ 11. {krw_coin11} 보유코인이 없으므로 매도불가. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin11}")
                        print(f"매수가능 : {op_mode11} - 가능")
                        print("")

            # 1초 딜레이.
            time.sleep(1)
            ##### 11번 코인 매매 종료 #####
            #############################


            ###############################
            ##### 매매 : 12번코인 시작. #####

            ##### 코인보유현황
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
            #time.sleep(1)


            # 코인 현재가 불러오기
            price12 = pyupbit.get_current_price(krw_coin12)

            # MACD 조회.
            #macd12 = get_macd(krw_coin12)
            # 거래량 동반한 MACD 조회.
            macd12 = get_acc_macd(krw_coin12)
            # 20일 이평선 조회.
            #macd12 = get_ma20(krw_coin12)

            # 매수가능금액 불러오기
            krw12 = upbit.get_balance("KRW")

            # MACD 조건문
            if macd12 >= 0:     # macd가 0보다 높을때는 매수
                if op_mode12 == True:    # 매수 가능(True)일 경우 - 매수시도
                    if krw12 > buy_krw:      # 매수가능금액 krw12 가 매수평균가 buy_krw 보다 클때
                        if krw12 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                            if buy_krw > 10100:     # 매수평균가 buy_krw 가 10,100원 초과일 경우 : 매수
                                # 매수금액은 매수평균가 buy_krw 로
                                upbit.buy_market_order(krw_coin12, buy_krw * 0.99)   # 매수가능금액에서 1%를 빼고

                                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                                op_mode12 = False

                                # 1초 딜레이
                                #time.sleep(1)
                                # 보유수량 불러오기
                                krw_balance12 = upbit.get_balance(krw_coin12)
                                # 코인 현재가 불러오기
                                price12 = pyupbit.get_current_price(krw_coin12)
                                # 보유코인 원화금액으로 계산하기
                                bp12 = price12 * krw_balance12

                                # 보유 및 매수 가능 출력.
                                print(f"[ 12. {krw_coin12} 매수완료. ]")
                                print(f"매수시간 : {now}  |  코인명 : {coin12}  |  현재가 = ￦{price12}  |  MACD = ￦{macd12}  |  보유수량 = {krw_balance12}  |  평가금액 = ￦{bp12}")
                                print(f"매수가능 : {op_mode12} - 불가")
                                print("")

                            else:
                                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                                op_mode12 = False

                                print(f"[ 12. {krw_coin12} 잔고부족으로 매수불가. ]")
                                print(f"현재시간 : {now}  |  코인명 : {coin12}")
                                print(f"매수가능 : {op_mode12} - 불가")
                                print("")

                        else:
                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode12 = False

                            print(f"[ 12. {krw_coin12} 잔고부족으로 매수불가. ]")
                            print(f"현재시간 : {now}  |  코인명 : {coin12}")
                            print(f"매수가능 : {op_mode12} - 불가")
                            print("")

                    elif krw12 <= buy_krw:   # 매수가능금액 krw12 가 매수평균가 buy_krw 보다 같거나 작을때
                        if krw12 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                            # 매수금액은 매수가능금액인 krw12 로
                            upbit.buy_market_order(krw_coin12, krw12 * 0.99)   # 매수가능금액에서 1%를 빼고

                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode12 = False

                            # 1초 딜레이
                            #time.sleep(1)
                            # 보유수량 불러오기
                            krw_balance12 = upbit.get_balance(krw_coin12)
                            # 코인 현재가 불러오기
                            price12 = pyupbit.get_current_price(krw_coin12)
                            # 보유코인 원화금액으로 계산하기
                            bp12 = price12 * krw_balance12

                            # 보유 및 매수 가능 출력.
                            print(f"[ 12. {krw_coin12} 매수완료. ]")
                            print(f"매수시간 : {now}  |  코인명 : {coin12}  |  현재가 = ￦{price12}  |  MACD = ￦{macd12}  |  보유수량 = {krw_balance12}  |  평가금액 = ￦{bp12}")
                            print(f"매수가능 : {op_mode12} - 불가")
                            print("")

                        else:
                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode12 = False

                            print(f"[ 12. {krw_coin12} 잔고부족으로 매수불가. ]")
                            print(f"현재시간 : {now}  |  코인명 : {coin12}")
                            print(f"매수가능 : {op_mode12} - 불가")
                            print("")

            elif macd12 < 0:       # macd가 0보다 낮을때는 매도
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
                        print(f"매도시간 : {now}  |  코인명 : {coin12}  |  현재가 = ￦{price12}  |  MACD = ￦{macd12}  |  보유수량 = {krw_balance12}  |  평가금액 = ￦{bp12}")
                        print(f"매수가능 : {op_mode12} - 가능")
                        print("")

                    else:   # 보유코인 평가 금액이 10,100원 이하일때
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode12 = True

                        print(f"[ 12. {krw_coin12} 보유코인이 없으므로 매도불가. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin12}")
                        print(f"매수가능 : {op_mode12} - 가능")
                        print("")

            # 1초 딜레이.
            time.sleep(1)
            ##### 12번 코인 매매 종료 #####
            #############################


            ###############################
            ##### 매매 : 13번코인 시작. #####

            ##### 코인보유현황
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
            #time.sleep(1)


            # 코인 현재가 불러오기
            price13 = pyupbit.get_current_price(krw_coin13)

            # MACD 조회.
            #macd13 = get_macd(krw_coin13)
            # 거래량 동반한 MACD 조회.
            macd13 = get_acc_macd(krw_coin13)
            # 20일 이평선 조회.
            #macd13 = get_ma20(krw_coin13)

            # 매수가능금액 불러오기
            krw13 = upbit.get_balance("KRW")

            # MACD 조건문
            if macd13 >= 0:     # macd가 0보다 높을때는 매수
                if op_mode13 == True:    # 매수 가능(True)일 경우 - 매수시도
                    if krw13 > buy_krw:      # 매수가능금액 krw13 가 매수평균가 buy_krw 보다 클때
                        if krw13 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                            if buy_krw > 10100:     # 매수평균가 buy_krw 가 10,100원 초과일 경우 : 매수
                                # 매수금액은 매수평균가 buy_krw 로
                                upbit.buy_market_order(krw_coin13, buy_krw * 0.99)   # 매수가능금액에서 1%를 빼고

                                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                                op_mode13 = False

                                # 1초 딜레이
                                #time.sleep(1)
                                # 보유수량 불러오기
                                krw_balance13 = upbit.get_balance(krw_coin13)
                                # 코인 현재가 불러오기
                                price13 = pyupbit.get_current_price(krw_coin13)
                                # 보유코인 원화금액으로 계산하기
                                bp13 = price13 * krw_balance13

                                # 보유 및 매수 가능 출력.
                                print(f"[ 13. {krw_coin13} 매수완료. ]")
                                print(f"매수시간 : {now}  |  코인명 : {coin13}  |  현재가 = ￦{price13}  |  MACD = ￦{macd13}  |  보유수량 = {krw_balance13}  |  평가금액 = ￦{bp13}")
                                print(f"매수가능 : {op_mode13} - 불가")
                                print("")

                            else:
                                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                                op_mode13 = False

                                print(f"[ 13. {krw_coin13} 잔고부족으로 매수불가. ]")
                                print(f"현재시간 : {now}  |  코인명 : {coin13}")
                                print(f"매수가능 : {op_mode13} - 불가")
                                print("")

                        else:
                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode13 = False

                            print(f"[ 13. {krw_coin13} 잔고부족으로 매수불가. ]")
                            print(f"현재시간 : {now}  |  코인명 : {coin13}")
                            print(f"매수가능 : {op_mode13} - 불가")
                            print("")

                    elif krw13 <= buy_krw:   # 매수가능금액 krw13 가 매수평균가 buy_krw 보다 같거나 작을때
                        if krw13 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                            # 매수금액은 매수가능금액인 krw13 로
                            upbit.buy_market_order(krw_coin13, krw13 * 0.99)   # 매수가능금액에서 1%를 빼고

                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode13 = False

                            # 1초 딜레이
                            #time.sleep(1)
                            # 보유수량 불러오기
                            krw_balance13 = upbit.get_balance(krw_coin13)
                            # 코인 현재가 불러오기
                            price13 = pyupbit.get_current_price(krw_coin13)
                            # 보유코인 원화금액으로 계산하기
                            bp13 = price13 * krw_balance13

                            # 보유 및 매수 가능 출력.
                            print(f"[ 13. {krw_coin13} 매수완료. ]")
                            print(f"매수시간 : {now}  |  코인명 : {coin13}  |  현재가 = ￦{price13}  |  MACD = ￦{macd13}  |  보유수량 = {krw_balance13}  |  평가금액 = ￦{bp13}")
                            print(f"매수가능 : {op_mode13} - 불가")
                            print("")

                        else:
                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode13 = False

                            print(f"[ 13. {krw_coin13} 잔고부족으로 매수불가. ]")
                            print(f"현재시간 : {now}  |  코인명 : {coin13}")
                            print(f"매수가능 : {op_mode13} - 불가")
                            print("")

            elif macd13 < 0:       # macd가 0보다 낮을때는 매도
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
                        print(f"매도시간 : {now}  |  코인명 : {coin13}  |  현재가 = ￦{price13}  |  MACD = ￦{macd13}  |  보유수량 = {krw_balance13}  |  평가금액 = ￦{bp13}")
                        print(f"매수가능 : {op_mode13} - 가능")
                        print("")

                    else:   # 보유코인 평가 금액이 10,100원 이하일때
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode13 = True

                        print(f"[ 13. {krw_coin13} 보유코인이 없으므로 매도불가. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin13}")
                        print(f"매수가능 : {op_mode13} - 가능")
                        print("")

            # 1초 딜레이.
            time.sleep(1)
            ##### 13번 코인 매매 종료 #####
            #############################


            ###############################
            ##### 매매 : 14번코인 시작. #####

            ##### 코인보유현황
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
            #time.sleep(1)


            # 코인 현재가 불러오기
            price14 = pyupbit.get_current_price(krw_coin14)

            # MACD 조회.
            #macd14 = get_macd(krw_coin14)
            # 거래량 동반한 MACD 조회.
            macd14 = get_acc_macd(krw_coin14)
            # 20일 이평선 조회.
            #macd14 = get_ma20(krw_coin14)

            # 매수가능금액 불러오기
            krw14 = upbit.get_balance("KRW")

            # MACD 조건문
            if macd14 >= 0:     # macd가 0보다 높을때는 매수
                if op_mode14 == True:    # 매수 가능(True)일 경우 - 매수시도
                    if krw14 > buy_krw:      # 매수가능금액 krw14 가 매수평균가 buy_krw 보다 클때
                        if krw14 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                            if buy_krw > 10100:     # 매수평균가 buy_krw 가 10,100원 초과일 경우 : 매수
                                # 매수금액은 매수평균가 buy_krw 로
                                upbit.buy_market_order(krw_coin14, buy_krw * 0.99)   # 매수가능금액에서 1%를 빼고

                                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                                op_mode14 = False

                                # 1초 딜레이
                                #time.sleep(1)
                                # 보유수량 불러오기
                                krw_balance14 = upbit.get_balance(krw_coin14)
                                # 코인 현재가 불러오기
                                price14 = pyupbit.get_current_price(krw_coin14)
                                # 보유코인 원화금액으로 계산하기
                                bp14 = price14 * krw_balance14

                                # 보유 및 매수 가능 출력.
                                print(f"[ 14. {krw_coin14} 매수완료. ]")
                                print(f"매수시간 : {now}  |  코인명 : {coin14}  |  현재가 = ￦{price14}  |  MACD = ￦{macd14}  |  보유수량 = {krw_balance14}  |  평가금액 = ￦{bp14}")
                                print(f"매수가능 : {op_mode14} - 불가")
                                print("")

                            else:
                                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                                op_mode14 = False

                                print(f"[ 14. {krw_coin14} 잔고부족으로 매수불가. ]")
                                print(f"현재시간 : {now}  |  코인명 : {coin14}")
                                print(f"매수가능 : {op_mode14} - 불가")
                                print("")

                        else:
                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode14 = False

                            print(f"[ 14. {krw_coin14} 잔고부족으로 매수불가. ]")
                            print(f"현재시간 : {now}  |  코인명 : {coin14}")
                            print(f"매수가능 : {op_mode14} - 불가")
                            print("")

                    elif krw14 <= buy_krw:   # 매수가능금액 krw14 가 매수평균가 buy_krw 보다 같거나 작을때
                        if krw14 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                            # 매수금액은 매수가능금액인 krw14 로
                            upbit.buy_market_order(krw_coin14, krw14 * 0.99)   # 매수가능금액에서 1%를 빼고

                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode14 = False

                            # 1초 딜레이
                            #time.sleep(1)
                            # 보유수량 불러오기
                            krw_balance14 = upbit.get_balance(krw_coin14)
                            # 코인 현재가 불러오기
                            price14 = pyupbit.get_current_price(krw_coin14)
                            # 보유코인 원화금액으로 계산하기
                            bp14 = price14 * krw_balance14

                            # 보유 및 매수 가능 출력.
                            print(f"[ 14. {krw_coin14} 매수완료. ]")
                            print(f"매수시간 : {now}  |  코인명 : {coin14}  |  현재가 = ￦{price14}  |  MACD = ￦{macd14}  |  보유수량 = {krw_balance14}  |  평가금액 = ￦{bp14}")
                            print(f"매수가능 : {op_mode14} - 불가")
                            print("")

                        else:
                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode14 = False

                            print(f"[ 14. {krw_coin14} 잔고부족으로 매수불가. ]")
                            print(f"현재시간 : {now}  |  코인명 : {coin14}")
                            print(f"매수가능 : {op_mode14} - 불가")
                            print("")

            elif macd14 < 0:       # macd가 0보다 낮을때는 매도
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
                        print(f"매도시간 : {now}  |  코인명 : {coin14}  |  현재가 = ￦{price14}  |  MACD = ￦{macd14}  |  보유수량 = {krw_balance14}  |  평가금액 = ￦{bp14}")
                        print(f"매수가능 : {op_mode14} - 가능")
                        print("")

                    else:   # 보유코인 평가 금액이 10,100원 이하일때
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode14 = True

                        print(f"[ 14. {krw_coin14} 보유코인이 없으므로 매도불가. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin14}")
                        print(f"매수가능 : {op_mode14} - 가능")
                        print("")

            # 1초 딜레이.
            time.sleep(1)
            ##### 14번 코인 매매 종료 #####
            #############################


            ###############################
            ##### 매매 : 15번코인 시작. #####

            ##### 코인보유현황
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
            #time.sleep(1)


            # 코인 현재가 불러오기
            price15 = pyupbit.get_current_price(krw_coin15)
            
            # MACD 조회.
            #macd15 = get_macd(krw_coin15)
            # 거래량 동반한 MACD 조회.
            macd15 = get_acc_macd(krw_coin15)
            # 20일 이평선 조회.
            #macd15 = get_ma20(krw_coin15)

            # 매수가능금액 불러오기
            krw15 = upbit.get_balance("KRW")

            # MACD 조건문
            if macd15 >= 0:     # macd가 0보다 높을때는 매수
                if op_mode15 == True:    # 매수 가능(True)일 경우 - 매수시도
                    if krw15 > buy_krw:      # 매수가능금액 krw15 가 매수평균가 buy_krw 보다 클때
                        if krw15 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                            if buy_krw > 10100:     # 매수평균가 buy_krw 가 10,100원 초과일 경우 : 매수
                                # 매수금액은 매수평균가 buy_krw 로
                                upbit.buy_market_order(krw_coin15, buy_krw * 0.99)   # 매수가능금액에서 1%를 빼고

                                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                                op_mode15 = False

                                # 1초 딜레이
                                #time.sleep(1)
                                # 보유수량 불러오기
                                krw_balance15 = upbit.get_balance(krw_coin15)
                                # 코인 현재가 불러오기
                                price15 = pyupbit.get_current_price(krw_coin15)
                                # 보유코인 원화금액으로 계산하기
                                bp15 = price15 * krw_balance15

                                # 보유 및 매수 가능 출력.
                                print(f"[ 15. {krw_coin15} 매수완료. ]")
                                print(f"매수시간 : {now}  |  코인명 : {coin15}  |  현재가 = ￦{price15}  |  MACD = ￦{macd15}  |  보유수량 = {krw_balance15}  |  평가금액 = ￦{bp15}")
                                print(f"매수가능 : {op_mode15} - 불가")
                                print("")

                            else:
                                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                                op_mode15 = False

                                print(f"[ 15. {krw_coin15} 잔고부족으로 매수불가. ]")
                                print(f"현재시간 : {now}  |  코인명 : {coin15}")
                                print(f"매수가능 : {op_mode15} - 불가")
                                print("")

                        else:
                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode15 = False

                            print(f"[ 15. {krw_coin15} 잔고부족으로 매수불가. ]")
                            print(f"현재시간 : {now}  |  코인명 : {coin15}")
                            print(f"매수가능 : {op_mode15} - 불가")
                            print("")

                    elif krw15 <= buy_krw:   # 매수가능금액 krw15 가 매수평균가 buy_krw 보다 같거나 작을때
                        if krw15 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                            # 매수금액은 매수가능금액인 krw15 로
                            upbit.buy_market_order(krw_coin15, krw15 * 0.99)   # 매수가능금액에서 1%를 빼고

                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode15 = False

                            # 1초 딜레이
                            #time.sleep(1)
                            # 보유수량 불러오기
                            krw_balance15 = upbit.get_balance(krw_coin15)
                            # 코인 현재가 불러오기
                            price15 = pyupbit.get_current_price(krw_coin15)
                            # 보유코인 원화금액으로 계산하기
                            bp15 = price15 * krw_balance15

                            # 보유 및 매수 가능 출력.
                            print(f"[ 15. {krw_coin15} 매수완료. ]")
                            print(f"매수시간 : {now}  |  코인명 : {coin15}  |  현재가 = ￦{price15}  |  MACD = ￦{macd15}  |  보유수량 = {krw_balance15}  |  평가금액 = ￦{bp15}")
                            print(f"매수가능 : {op_mode15} - 불가")
                            print("")

                        else:
                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode15 = False

                            print(f"[ 15. {krw_coin15} 잔고부족으로 매수불가. ]")
                            print(f"현재시간 : {now}  |  코인명 : {coin15}")
                            print(f"매수가능 : {op_mode15} - 불가")
                            print("")

            elif macd15 < 0:       # macd가 0보다 낮을때는 매도
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
                        print(f"매도시간 : {now}  |  코인명 : {coin15}  |  현재가 = ￦{price15}  |  MACD = ￦{macd15}  |  보유수량 = {krw_balance15}  |  평가금액 = ￦{bp15}")
                        print(f"매수가능 : {op_mode15} - 가능")
                        print("")

                    else:   # 보유코인 평가 금액이 10,100원 이하일때
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode15 = True

                        print(f"[ 15. {krw_coin15} 보유코인이 없으므로 매도불가. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin15}")
                        print(f"매수가능 : {op_mode15} - 가능")
                        print("")

            # 1초 딜레이.
            time.sleep(1)
            ##### 15번 코인 매매 종료 #####
            #############################


            ###############################
            ##### 매매 : 16번코인 시작. #####

            ##### 코인보유현황
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
            #time.sleep(1)


            # 코인 현재가 불러오기
            price16 = pyupbit.get_current_price(krw_coin16)

            # MACD 조회.
            #macd16 = get_macd(krw_coin16)
            # 거래량 동반한 MACD 조회.
            macd16 = get_acc_macd(krw_coin16)
            # 20일 이평선 조회.
            #macd16 = get_ma20(krw_coin16)

            # 매수가능금액 불러오기
            krw16 = upbit.get_balance("KRW")

            # MACD 조건문
            if macd16 >= 0:     # macd가 0보다 높을때는 매수
                if op_mode16 == True:    # 매수 가능(True)일 경우 - 매수시도
                    if krw16 > buy_krw:      # 매수가능금액 krw16 가 매수평균가 buy_krw 보다 클때
                        if krw16 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                            if buy_krw > 10100:     # 매수평균가 buy_krw 가 10,100원 초과일 경우 : 매수
                                # 매수금액은 매수평균가 buy_krw 로
                                upbit.buy_market_order(krw_coin16, buy_krw * 0.99)   # 매수가능금액에서 1%를 빼고

                                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                                op_mode16 = False

                                # 1초 딜레이
                                #time.sleep(1)
                                # 보유수량 불러오기
                                krw_balance16 = upbit.get_balance(krw_coin16)
                                # 코인 현재가 불러오기
                                price16 = pyupbit.get_current_price(krw_coin16)
                                # 보유코인 원화금액으로 계산하기
                                bp16 = price16 * krw_balance16

                                # 보유 및 매수 가능 출력.
                                print(f"[ 16. {krw_coin16} 매수완료. ]")
                                print(f"매수시간 : {now}  |  코인명 : {coin16}  |  현재가 = ￦{price16}  |  MACD = ￦{macd16}  |  보유수량 = {krw_balance16}  |  평가금액 = ￦{bp16}")
                                print(f"매수가능 : {op_mode16} - 불가")
                                print("")

                            else:
                                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                                op_mode16 = False

                                print(f"[ 16. {krw_coin16} 잔고부족으로 매수불가. ]")
                                print(f"현재시간 : {now}  |  코인명 : {coin16}")
                                print(f"매수가능 : {op_mode16} - 불가")
                                print("")

                        else:
                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode16 = False

                            print(f"[ 16. {krw_coin16} 잔고부족으로 매수불가. ]")
                            print(f"현재시간 : {now}  |  코인명 : {coin16}")
                            print(f"매수가능 : {op_mode16} - 불가")
                            print("")

                    elif krw16 <= buy_krw:   # 매수가능금액 krw16 가 매수평균가 buy_krw 보다 같거나 작을때
                        if krw16 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                            # 매수금액은 매수가능금액인 krw16 로
                            upbit.buy_market_order(krw_coin16, krw16 * 0.99)   # 매수가능금액에서 1%를 빼고

                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode16 = False

                            # 1초 딜레이
                            #time.sleep(1)
                            # 보유수량 불러오기
                            krw_balance16 = upbit.get_balance(krw_coin16)
                            # 코인 현재가 불러오기
                            price16 = pyupbit.get_current_price(krw_coin16)
                            # 보유코인 원화금액으로 계산하기
                            bp16 = price16 * krw_balance16

                            # 보유 및 매수 가능 출력.
                            print(f"[ 16. {krw_coin16} 매수완료. ]")
                            print(f"매수시간 : {now}  |  코인명 : {coin16}  |  현재가 = ￦{price16}  |  MACD = ￦{macd16}  |  보유수량 = {krw_balance16}  |  평가금액 = ￦{bp16}")
                            print(f"매수가능 : {op_mode16} - 불가")
                            print("")

                        else:
                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode16 = False

                            print(f"[ 16. {krw_coin16} 잔고부족으로 매수불가. ]")
                            print(f"현재시간 : {now}  |  코인명 : {coin16}")
                            print(f"매수가능 : {op_mode16} - 불가")
                            print("")

            elif macd16 < 0:       # macd가 0보다 낮을때는 매도
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
                        print(f"매도시간 : {now}  |  코인명 : {coin16}  |  현재가 = ￦{price16}  |  MACD = ￦{macd16}  |  보유수량 = {krw_balance16}  |  평가금액 = ￦{bp16}")
                        print(f"매수가능 : {op_mode16} - 가능")
                        print("")

                    else:   # 보유코인 평가 금액이 10,100원 이하일때
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode16 = True

                        print(f"[ 16. {krw_coin16} 보유코인이 없으므로 매도불가. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin16}")
                        print(f"매수가능 : {op_mode16} - 가능")
                        print("")

            # 1초 딜레이.
            time.sleep(1)
            ##### 16번 코인 매매 종료 #####
            #############################


            ###############################
            ##### 매매 : 17번코인 시작. #####

            ##### 코인보유현황
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
            #time.sleep(1)


            # 코인 현재가 불러오기
            price17 = pyupbit.get_current_price(krw_coin17)

            # MACD 조회.
            #macd17 = get_macd(krw_coin17)
            # 거래량 동반한 MACD 조회.
            macd17 = get_acc_macd(krw_coin17)
            # 20일 이평선 조회.
            #macd17 = get_ma20(krw_coin17)

            # 매수가능금액 불러오기
            krw17 = upbit.get_balance("KRW")

            # MACD 조건문
            if macd17 >= 0:     # macd가 0보다 높을때는 매수
                if op_mode17 == True:    # 매수 가능(True)일 경우 - 매수시도
                    if krw17 > buy_krw:      # 매수가능금액 krw17 가 매수평균가 buy_krw 보다 클때
                        if krw17 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                            if buy_krw > 10100:     # 매수평균가 buy_krw 가 10,100원 초과일 경우 : 매수
                                # 매수금액은 매수평균가 buy_krw 로
                                upbit.buy_market_order(krw_coin17, buy_krw * 0.99)   # 매수가능금액에서 1%를 빼고

                                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                                op_mode17 = False

                                # 1초 딜레이
                                #time.sleep(1)
                                # 보유수량 불러오기
                                krw_balance17 = upbit.get_balance(krw_coin17)
                                # 코인 현재가 불러오기
                                price17 = pyupbit.get_current_price(krw_coin17)
                                # 보유코인 원화금액으로 계산하기
                                bp17 = price17 * krw_balance17

                                # 보유 및 매수 가능 출력.
                                print(f"[ 17. {krw_coin17} 매수완료. ]")
                                print(f"매수시간 : {now}  |  코인명 : {coin17}  |  현재가 = ￦{price17}  |  MACD = ￦{macd17}  |  보유수량 = {krw_balance17}  |  평가금액 = ￦{bp17}")
                                print(f"매수가능 : {op_mode17} - 불가")
                                print("")

                            else:
                                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                                op_mode17 = False

                                print(f"[ 17. {krw_coin17} 잔고부족으로 매수불가. ]")
                                print(f"현재시간 : {now}  |  코인명 : {coin17}")
                                print(f"매수가능 : {op_mode17} - 불가")
                                print("")

                        else:
                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode17 = False

                            print(f"[ 17. {krw_coin17} 잔고부족으로 매수불가. ]")
                            print(f"현재시간 : {now}  |  코인명 : {coin17}")
                            print(f"매수가능 : {op_mode17} - 불가")
                            print("")

                    elif krw17 <= buy_krw:   # 매수가능금액 krw17 가 매수평균가 buy_krw 보다 같거나 작을때
                        if krw17 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                            # 매수금액은 매수가능금액인 krw17 로
                            upbit.buy_market_order(krw_coin17, krw17 * 0.99)   # 매수가능금액에서 1%를 빼고

                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode17 = False

                            # 1초 딜레이
                            #time.sleep(1)
                            # 보유수량 불러오기
                            krw_balance17 = upbit.get_balance(krw_coin17)
                            # 코인 현재가 불러오기
                            price17 = pyupbit.get_current_price(krw_coin17)
                            # 보유코인 원화금액으로 계산하기
                            bp17 = price17 * krw_balance17

                            # 보유 및 매수 가능 출력.
                            print(f"[ 17. {krw_coin17} 매수완료. ]")
                            print(f"매수시간 : {now}  |  코인명 : {coin17}  |  현재가 = ￦{price17}  |  MACD = ￦{macd17}  |  보유수량 = {krw_balance17}  |  평가금액 = ￦{bp17}")
                            print(f"매수가능 : {op_mode17} - 불가")
                            print("")

                        else:
                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode17 = False

                            print(f"[ 17. {krw_coin17} 잔고부족으로 매수불가. ]")
                            print(f"현재시간 : {now}  |  코인명 : {coin17}")
                            print(f"매수가능 : {op_mode17} - 불가")
                            print("")

            elif macd17 < 0:       # macd가 0보다 낮을때는 매도
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
                        print(f"매도시간 : {now}  |  코인명 : {coin17}  |  현재가 = ￦{price17}  |  MACD = ￦{macd17}  |  보유수량 = {krw_balance17}  |  평가금액 = ￦{bp17}")
                        print(f"매수가능 : {op_mode17} - 가능")
                        print("")

                    else:   # 보유코인 평가 금액이 10,100원 이하일때
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode17 = True

                        print(f"[ 17. {krw_coin17} 보유코인이 없으므로 매도불가. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin17}")
                        print(f"매수가능 : {op_mode17} - 가능")
                        print("")

            # 1초 딜레이.
            time.sleep(1)
            ##### 17번 코인 매매 종료 #####
            #############################


            ###############################
            ##### 매매 : 18번코인 시작. #####

            ##### 코인보유현황
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
            #time.sleep(1)


            # 코인 현재가 불러오기
            price18 = pyupbit.get_current_price(krw_coin18)

            # MACD 조회.
            #macd18 = get_macd(krw_coin18)
            # 거래량 동반한 MACD 조회.
            macd18 = get_acc_macd(krw_coin18)
            # 20일 이평선 조회.
            #macd18 = get_ma20(krw_coin18)

            # 매수가능금액 불러오기
            krw18 = upbit.get_balance("KRW")

            # MACD 조건문
            if macd18 >= 0:     # macd가 0보다 높을때는 매수
                if op_mode18 == True:    # 매수 가능(True)일 경우 - 매수시도
                    if krw18 > buy_krw:      # 매수가능금액 krw18 가 매수평균가 buy_krw 보다 클때
                        if krw18 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                            if buy_krw > 10100:     # 매수평균가 buy_krw 가 10,100원 초과일 경우 : 매수
                                # 매수금액은 매수평균가 buy_krw 로
                                upbit.buy_market_order(krw_coin18, buy_krw * 0.99)   # 매수가능금액에서 1%를 빼고

                                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                                op_mode18 = False

                                # 1초 딜레이
                                #time.sleep(1)
                                # 보유수량 불러오기
                                krw_balance18 = upbit.get_balance(krw_coin18)
                                # 코인 현재가 불러오기
                                price18 = pyupbit.get_current_price(krw_coin18)
                                # 보유코인 원화금액으로 계산하기
                                bp18 = price18 * krw_balance18

                                # 보유 및 매수 가능 출력.
                                print(f"[ 18. {krw_coin18} 매수완료. ]")
                                print(f"매수시간 : {now}  |  코인명 : {coin18}  |  현재가 = ￦{price18}  |  MACD = ￦{macd18}  |  보유수량 = {krw_balance18}  |  평가금액 = ￦{bp18}")
                                print(f"매수가능 : {op_mode18} - 불가")
                                print("")

                            else:
                                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                                op_mode18 = False

                                print(f"[ 18. {krw_coin18} 잔고부족으로 매수불가. ]")
                                print(f"현재시간 : {now}  |  코인명 : {coin18}")
                                print(f"매수가능 : {op_mode18} - 불가")
                                print("")

                        else:
                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode18 = False

                            print(f"[ 18. {krw_coin18} 잔고부족으로 매수불가. ]")
                            print(f"현재시간 : {now}  |  코인명 : {coin18}")
                            print(f"매수가능 : {op_mode18} - 불가")
                            print("")

                    elif krw18 <= buy_krw:   # 매수가능금액 krw18 가 매수평균가 buy_krw 보다 같거나 작을때
                        if krw18 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                            # 매수금액은 매수가능금액인 krw18 로
                            upbit.buy_market_order(krw_coin18, krw18 * 0.99)   # 매수가능금액에서 1%를 빼고

                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode18 = False

                            # 1초 딜레이
                            #time.sleep(1)
                            # 보유수량 불러오기
                            krw_balance18 = upbit.get_balance(krw_coin18)
                            # 코인 현재가 불러오기
                            price18 = pyupbit.get_current_price(krw_coin18)
                            # 보유코인 원화금액으로 계산하기
                            bp18 = price18 * krw_balance18

                            # 보유 및 매수 가능 출력.
                            print(f"[ 18. {krw_coin18} 매수완료. ]")
                            print(f"매수시간 : {now}  |  코인명 : {coin18}  |  현재가 = ￦{price18}  |  MACD = ￦{macd18}  |  보유수량 = {krw_balance18}  |  평가금액 = ￦{bp18}")
                            print(f"매수가능 : {op_mode18} - 불가")
                            print("")

                        else:
                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode18 = False

                            print(f"[ 18. {krw_coin18} 잔고부족으로 매수불가. ]")
                            print(f"현재시간 : {now}  |  코인명 : {coin18}")
                            print(f"매수가능 : {op_mode18} - 불가")
                            print("")

            elif macd18 < 0:       # macd가 0보다 낮을때는 매도
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
                        print(f"매도시간 : {now}  |  코인명 : {coin18}  |  현재가 = ￦{price18}  |  MACD = ￦{macd18}  |  보유수량 = {krw_balance18}  |  평가금액 = ￦{bp18}")
                        print(f"매수가능 : {op_mode18} - 가능")
                        print("")

                    else:   # 보유코인 평가 금액이 10,100원 이하일때
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode18 = True

                        print(f"[ 18. {krw_coin18} 보유코인이 없으므로 매도불가. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin18}")
                        print(f"매수가능 : {op_mode18} - 가능")
                        print("")

            # 1초 딜레이.
            time.sleep(1)
            ##### 18번 코인 매매 종료 #####
            #############################


            ###############################
            ##### 매매 : 19번코인 시작. #####

            ##### 코인보유현황
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
            #time.sleep(1)


            # 코인 현재가 불러오기
            price19 = pyupbit.get_current_price(krw_coin19)

            # MACD 조회.
            #macd19 = get_macd(krw_coin19)
            # 거래량 동반한 MACD 조회.
            macd19 = get_acc_macd(krw_coin19)
            # 20일 이평선 조회.
            #macd19 = get_ma20(krw_coin19)

            # 매수가능금액 불러오기
            krw19 = upbit.get_balance("KRW")

            # MACD 조건문
            if macd19 >= 0:     # macd가 0보다 높을때는 매수
                if op_mode19 == True:    # 매수 가능(True)일 경우 - 매수시도
                    if krw19 > buy_krw:      # 매수가능금액 krw19 가 매수평균가 buy_krw 보다 클때
                        if krw19 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                            if buy_krw > 10100:     # 매수평균가 buy_krw 가 10,100원 초과일 경우 : 매수
                                # 매수금액은 매수평균가 buy_krw 로
                                upbit.buy_market_order(krw_coin19, buy_krw * 0.99)   # 매수가능금액에서 1%를 빼고

                                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                                op_mode19 = False

                                # 1초 딜레이
                                #time.sleep(1)
                                # 보유수량 불러오기
                                krw_balance19 = upbit.get_balance(krw_coin19)
                                # 코인 현재가 불러오기
                                price19 = pyupbit.get_current_price(krw_coin19)
                                # 보유코인 원화금액으로 계산하기
                                bp19 = price19 * krw_balance19

                                # 보유 및 매수 가능 출력.
                                print(f"[ 19. {krw_coin19} 매수완료. ]")
                                print(f"매수시간 : {now}  |  코인명 : {coin19}  |  현재가 = ￦{price19}  |  MACD = ￦{macd19}  |  보유수량 = {krw_balance19}  |  평가금액 = ￦{bp19}")
                                print(f"매수가능 : {op_mode19} - 불가")
                                print("")

                            else:
                                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                                op_mode19 = False

                                print(f"[ 19. {krw_coin19} 잔고부족으로 매수불가. ]")
                                print(f"현재시간 : {now}  |  코인명 : {coin19}")
                                print(f"매수가능 : {op_mode19} - 불가")
                                print("")

                        else:
                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode19 = False

                            print(f"[ 19. {krw_coin19} 잔고부족으로 매수불가. ]")
                            print(f"현재시간 : {now}  |  코인명 : {coin19}")
                            print(f"매수가능 : {op_mode19} - 불가")
                            print("")

                    elif krw19 <= buy_krw:   # 매수가능금액 krw19 가 매수평균가 buy_krw 보다 같거나 작을때
                        if krw19 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                            # 매수금액은 매수가능금액인 krw19 로
                            upbit.buy_market_order(krw_coin19, krw19 * 0.99)   # 매수가능금액에서 1%를 빼고

                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode19 = False

                            # 1초 딜레이
                            #time.sleep(1)
                            # 보유수량 불러오기
                            krw_balance19 = upbit.get_balance(krw_coin19)
                            # 코인 현재가 불러오기
                            price19 = pyupbit.get_current_price(krw_coin19)
                            # 보유코인 원화금액으로 계산하기
                            bp19 = price19 * krw_balance19

                            # 보유 및 매수 가능 출력.
                            print(f"[ 19. {krw_coin19} 매수완료. ]")
                            print(f"매수시간 : {now}  |  코인명 : {coin19}  |  현재가 = ￦{price19}  |  MACD = ￦{macd19}  |  보유수량 = {krw_balance19}  |  평가금액 = ￦{bp19}")
                            print(f"매수가능 : {op_mode19} - 불가")
                            print("")

                        else:
                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode19 = False

                            print(f"[ 19. {krw_coin19} 잔고부족으로 매수불가. ]")
                            print(f"현재시간 : {now}  |  코인명 : {coin19}")
                            print(f"매수가능 : {op_mode19} - 불가")
                            print("")

            elif macd19 < 0:       # macd가 0보다 낮을때는 매도
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
                        print(f"매도시간 : {now}  |  코인명 : {coin19}  |  현재가 = ￦{price19}  |  MACD = ￦{macd19}  |  보유수량 = {krw_balance19}  |  평가금액 = ￦{bp19}")
                        print(f"매수가능 : {op_mode19} - 가능")
                        print("")

                    else:   # 보유코인 평가 금액이 10,100원 이하일때
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode19 = True

                        print(f"[ 19. {krw_coin19} 보유코인이 없으므로 매도불가. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin19}")
                        print(f"매수가능 : {op_mode19} - 가능")
                        print("")

            # 1초 딜레이.
            time.sleep(1)
            ##### 19번 코인 매매 종료 #####
            #############################


            ###############################
            ##### 매매 : 20번코인 시작. #####

            ##### 코인보유현황
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
            #time.sleep(1)


            # 코인 현재가 불러오기
            price20 = pyupbit.get_current_price(krw_coin20)

            # MACD 조회.
            #macd20 = get_macd(krw_coin20)
            # 거래량 동반한 MACD 조회.
            macd20 = get_acc_macd(krw_coin20)
            # 20일 이평선 조회.
            #macd20 = get_ma20(krw_coin20)

            # 매수가능금액 불러오기
            krw20 = upbit.get_balance("KRW")

            # MACD 조건문
            if macd20 >= 0:     # macd가 0보다 높을때는 매수
                if op_mode20 == True:    # 매수 가능(True)일 경우 - 매수시도
                    if krw20 > buy_krw:      # 매수가능금액 krw20 가 매수평균가 buy_krw 보다 클때
                        if krw20 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                            if buy_krw > 10100:     # 매수평균가 buy_krw 가 10,100원 초과일 경우 : 매수
                                # 매수금액은 매수평균가 buy_krw 로
                                upbit.buy_market_order(krw_coin20, buy_krw * 0.99)   # 매수가능금액에서 1%를 빼고

                                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                                op_mode20 = False

                                # 1초 딜레이
                                #time.sleep(1)
                                # 보유수량 불러오기
                                krw_balance20 = upbit.get_balance(krw_coin20)
                                # 코인 현재가 불러오기
                                price20 = pyupbit.get_current_price(krw_coin20)
                                # 보유코인 원화금액으로 계산하기
                                bp20 = price20 * krw_balance20

                                # 보유 및 매수 가능 출력.
                                print(f"[ 20. {krw_coin20} 매수완료. ]")
                                print(f"매수시간 : {now}  |  코인명 : {coin20}  |  현재가 = ￦{price20}  |  MACD = ￦{macd20}  |  보유수량 = {krw_balance20}  |  평가금액 = ￦{bp20}")
                                print(f"매수가능 : {op_mode20} - 불가")
                                print("")

                            else:
                                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                                op_mode20 = False

                                print(f"[ 20. {krw_coin20} 잔고부족으로 매수불가. ]")
                                print(f"현재시간 : {now}  |  코인명 : {coin20}")
                                print(f"매수가능 : {op_mode20} - 불가")
                                print("")

                        else:
                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode20 = False

                            print(f"[ 20. {krw_coin20} 잔고부족으로 매수불가. ]")
                            print(f"현재시간 : {now}  |  코인명 : {coin20}")
                            print(f"매수가능 : {op_mode20} - 불가")
                            print("")

                    elif krw20 <= buy_krw:   # 매수가능금액 krw20 가 매수평균가 buy_krw 보다 같거나 작을때
                        if krw20 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                            # 매수금액은 매수가능금액인 krw20 로
                            upbit.buy_market_order(krw_coin20, krw20 * 0.99)   # 매수가능금액에서 1%를 빼고

                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode20 = False

                            # 1초 딜레이
                            #time.sleep(1)
                            # 보유수량 불러오기
                            krw_balance20 = upbit.get_balance(krw_coin20)
                            # 코인 현재가 불러오기
                            price20 = pyupbit.get_current_price(krw_coin20)
                            # 보유코인 원화금액으로 계산하기
                            bp20 = price20 * krw_balance20

                            # 보유 및 매수 가능 출력.
                            print(f"[ 20. {krw_coin20} 매수완료. ]")
                            print(f"매수시간 : {now}  |  코인명 : {coin20}  |  현재가 = ￦{price20}  |  MACD = ￦{macd20}  |  보유수량 = {krw_balance20}  |  평가금액 = ￦{bp20}")
                            print(f"매수가능 : {op_mode20} - 불가")
                            print("")

                        else:
                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode20 = False

                            print(f"[ 20. {krw_coin20} 잔고부족으로 매수불가. ]")
                            print(f"현재시간 : {now}  |  코인명 : {coin20}")
                            print(f"매수가능 : {op_mode20} - 불가")
                            print("")

            elif macd20 < 0:       # macd가 0보다 낮을때는 매도
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
                        print(f"매도시간 : {now}  |  코인명 : {coin20}  |  현재가 = ￦{price20}  |  MACD = ￦{macd20}  |  보유수량 = {krw_balance20}  |  평가금액 = ￦{bp20}")
                        print(f"매수가능 : {op_mode20} - 가능")
                        print("")

                    else:   # 보유코인 평가 금액이 10,100원 이하일때
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode20 = True

                        print(f"[ 20. {krw_coin20} 보유코인이 없으므로 매도불가. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin20}")
                        print(f"매수가능 : {op_mode20} - 가능")
                        print("")

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

            ##### 코인보유현황
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
            #time.sleep(1)


            # 코인 현재가 불러오기
            price21 = pyupbit.get_current_price(krw_coin21)

            # MACD 조회.
            #macd21 = get_macd(krw_coin21)
            # 거래량 동반한 MACD 조회.
            macd21 = get_acc_macd(krw_coin21)
            # 20일 이평선 조회.
            #macd21 = get_ma20(krw_coin21)

            # 매수가능금액 불러오기
            krw21 = upbit.get_balance("KRW")

            # MACD 조건문
            if macd21 >= 0:     # macd가 0보다 높을때는 매수
                if op_mode21 == True:    # 매수 가능(True)일 경우 - 매수시도
                    if krw21 > buy_krw:      # 매수가능금액 krw21 가 매수평균가 buy_krw 보다 클때
                        if krw21 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                            if buy_krw > 10100:     # 매수평균가 buy_krw 가 10,100원 초과일 경우 : 매수
                                # 매수금액은 매수평균가 buy_krw 로
                                upbit.buy_market_order(krw_coin21, buy_krw * 0.99)   # 매수가능금액에서 1%를 빼고

                                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                                op_mode21 = False

                                # 1초 딜레이
                                #time.sleep(1)
                                # 보유수량 불러오기
                                krw_balance21 = upbit.get_balance(krw_coin21)
                                # 코인 현재가 불러오기
                                price21 = pyupbit.get_current_price(krw_coin21)
                                # 보유코인 원화금액으로 계산하기
                                bp21 = price21 * krw_balance21

                                # 보유 및 매수 가능 출력.
                                print(f"[ 21. {krw_coin21} 매수완료. ]")
                                print(f"매수시간 : {now}  |  코인명 : {coin21}  |  현재가 = ￦{price21}  |  MACD = ￦{macd21}  |  보유수량 = {krw_balance21}  |  평가금액 = ￦{bp21}")
                                print(f"매수가능 : {op_mode21} - 불가")
                                print("")

                            else:
                                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                                op_mode21 = False

                                print(f"[ 21. {krw_coin21} 잔고부족으로 매수불가. ]")
                                print(f"현재시간 : {now}  |  코인명 : {coin21}")
                                print(f"매수가능 : {op_mode21} - 불가")
                                print("")

                        else:
                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode21 = False

                            print(f"[ 21. {krw_coin21} 잔고부족으로 매수불가. ]")
                            print(f"현재시간 : {now}  |  코인명 : {coin21}")
                            print(f"매수가능 : {op_mode21} - 불가")
                            print("")

                    elif krw21 <= buy_krw:   # 매수가능금액 krw21 가 매수평균가 buy_krw 보다 같거나 작을때
                        if krw21 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                            # 매수금액은 매수가능금액인 krw21 로
                            upbit.buy_market_order(krw_coin21, krw21 * 0.99)   # 매수가능금액에서 1%를 빼고

                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode21 = False

                            # 1초 딜레이
                            #time.sleep(1)
                            # 보유수량 불러오기
                            krw_balance21 = upbit.get_balance(krw_coin21)
                            # 코인 현재가 불러오기
                            price21 = pyupbit.get_current_price(krw_coin21)
                            # 보유코인 원화금액으로 계산하기
                            bp21 = price21 * krw_balance21

                            # 보유 및 매수 가능 출력.
                            print(f"[ 21. {krw_coin21} 매수완료. ]")
                            print(f"매수시간 : {now}  |  코인명 : {coin21}  |  현재가 = ￦{price21}  |  MACD = ￦{macd21}  |  보유수량 = {krw_balance21}  |  평가금액 = ￦{bp21}")
                            print(f"매수가능 : {op_mode21} - 불가")
                            print("")

                        else:
                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode21 = False

                            print(f"[ 21. {krw_coin21} 잔고부족으로 매수불가. ]")
                            print(f"현재시간 : {now}  |  코인명 : {coin21}")
                            print(f"매수가능 : {op_mode21} - 불가")
                            print("")

            elif macd21 < 0:       # macd가 0보다 낮을때는 매도
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
                        print(f"매도시간 : {now}  |  코인명 : {coin21}  |  현재가 = ￦{price21}  |  MACD = ￦{macd21}  |  보유수량 = {krw_balance21}  |  평가금액 = ￦{bp21}")
                        print(f"매수가능 : {op_mode21} - 가능")
                        print("")

                    else:   # 보유코인 평가 금액이 10,100원 이하일때
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode21 = True

                        print(f"[ 21. {krw_coin21} 보유코인이 없으므로 매도불가. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin21}")
                        print(f"매수가능 : {op_mode21} - 가능")
                        print("")

            # 1초 딜레이.
            time.sleep(1)
            ##### 21번 코인 매매 종료 #####
            #############################


            ###############################
            ##### 매매 : 22번코인 시작. #####

            ##### 코인보유현황
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
            #time.sleep(1)


            # 코인 현재가 불러오기
            price22 = pyupbit.get_current_price(krw_coin22)

            # MACD 조회.
            #macd22 = get_macd(krw_coin22)
            # 거래량 동반한 MACD 조회.
            macd22 = get_acc_macd(krw_coin22)
            # 20일 이평선 조회.
            #macd22 = get_ma20(krw_coin22)

            # 매수가능금액 불러오기
            krw22 = upbit.get_balance("KRW")

            # MACD 조건문
            if macd22 >= 0:     # macd가 0보다 높을때는 매수
                if op_mode22 == True:    # 매수 가능(True)일 경우 - 매수시도
                    if krw22 > buy_krw:      # 매수가능금액 krw22 가 매수평균가 buy_krw 보다 클때
                        if krw22 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                            if buy_krw > 10100:     # 매수평균가 buy_krw 가 10,100원 초과일 경우 : 매수
                                # 매수금액은 매수평균가 buy_krw 로
                                upbit.buy_market_order(krw_coin22, buy_krw * 0.99)   # 매수가능금액에서 1%를 빼고

                                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                                op_mode22 = False

                                # 1초 딜레이
                                #time.sleep(1)
                                # 보유수량 불러오기
                                krw_balance22 = upbit.get_balance(krw_coin22)
                                # 코인 현재가 불러오기
                                price22 = pyupbit.get_current_price(krw_coin22)
                                # 보유코인 원화금액으로 계산하기
                                bp22 = price22 * krw_balance22

                                # 보유 및 매수 가능 출력.
                                print(f"[ 22. {krw_coin22} 매수완료. ]")
                                print(f"매수시간 : {now}  |  코인명 : {coin22}  |  현재가 = ￦{price22}  |  MACD = ￦{macd22}  |  보유수량 = {krw_balance22}  |  평가금액 = ￦{bp22}")
                                print(f"매수가능 : {op_mode22} - 불가")
                                print("")

                            else:
                                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                                op_mode22 = False

                                print(f"[ 22. {krw_coin22} 잔고부족으로 매수불가. ]")
                                print(f"현재시간 : {now}  |  코인명 : {coin22}")
                                print(f"매수가능 : {op_mode22} - 불가")
                                print("")

                        else:
                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode22 = False

                            print(f"[ 22. {krw_coin22} 잔고부족으로 매수불가. ]")
                            print(f"현재시간 : {now}  |  코인명 : {coin22}")
                            print(f"매수가능 : {op_mode22} - 불가")
                            print("")

                    elif krw22 <= buy_krw:   # 매수가능금액 krw22 가 매수평균가 buy_krw 보다 같거나 작을때
                        if krw22 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                            # 매수금액은 매수가능금액인 krw22 로
                            upbit.buy_market_order(krw_coin22, krw22 * 0.99)   # 매수가능금액에서 1%를 빼고

                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode22 = False

                            # 1초 딜레이
                            #time.sleep(1)
                            # 보유수량 불러오기
                            krw_balance22 = upbit.get_balance(krw_coin22)
                            # 코인 현재가 불러오기
                            price22 = pyupbit.get_current_price(krw_coin22)
                            # 보유코인 원화금액으로 계산하기
                            bp22 = price22 * krw_balance22

                            # 보유 및 매수 가능 출력.
                            print(f"[ 22. {krw_coin22} 매수완료. ]")
                            print(f"매수시간 : {now}  |  코인명 : {coin22}  |  현재가 = ￦{price22}  |  MACD = ￦{macd22}  |  보유수량 = {krw_balance22}  |  평가금액 = ￦{bp22}")
                            print(f"매수가능 : {op_mode22} - 불가")
                            print("")

                        else:
                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode22 = False

                            print(f"[ 22. {krw_coin22} 잔고부족으로 매수불가. ]")
                            print(f"현재시간 : {now}  |  코인명 : {coin22}")
                            print(f"매수가능 : {op_mode22} - 불가")
                            print("")

            elif macd22 < 0:       # macd가 0보다 낮을때는 매도
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
                        print(f"매도시간 : {now}  |  코인명 : {coin22}  |  현재가 = ￦{price22}  |  MACD = ￦{macd22}  |  보유수량 = {krw_balance22}  |  평가금액 = ￦{bp22}")
                        print(f"매수가능 : {op_mode22} - 가능")
                        print("")

                    else:   # 보유코인 평가 금액이 10,100원 이하일때
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode22 = True

                        print(f"[ 22. {krw_coin22} 보유코인이 없으므로 매도불가. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin22}")
                        print(f"매수가능 : {op_mode22} - 가능")
                        print("")

            # 1초 딜레이.
            time.sleep(1)
            ##### 22번 코인 매매 종료 #####
            #############################


            ###############################
            ##### 매매 : 23번코인 시작. #####

            ##### 코인보유현황
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
            #time.sleep(1)


            # 코인 현재가 불러오기
            price23 = pyupbit.get_current_price(krw_coin23)

            # MACD 조회.
            #macd23 = get_macd(krw_coin23)
            # 거래량 동반한 MACD 조회.
            macd23 = get_acc_macd(krw_coin23)
            # 20일 이평선 조회.
            #macd23 = get_ma20(krw_coin23)

            # 매수가능금액 불러오기
            krw23 = upbit.get_balance("KRW")

            # MACD 조건문
            if macd23 >= 0:     # macd가 0보다 높을때는 매수
                if op_mode23 == True:    # 매수 가능(True)일 경우 - 매수시도
                    if krw23 > buy_krw:      # 매수가능금액 krw23 가 매수평균가 buy_krw 보다 클때
                        if krw23 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                            if buy_krw > 10100:     # 매수평균가 buy_krw 가 10,100원 초과일 경우 : 매수
                                # 매수금액은 매수평균가 buy_krw 로
                                upbit.buy_market_order(krw_coin23, buy_krw * 0.99)   # 매수가능금액에서 1%를 빼고

                                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                                op_mode23 = False

                                # 1초 딜레이
                                #time.sleep(1)
                                # 보유수량 불러오기
                                krw_balance23 = upbit.get_balance(krw_coin23)
                                # 코인 현재가 불러오기
                                price23 = pyupbit.get_current_price(krw_coin23)
                                # 보유코인 원화금액으로 계산하기
                                bp23 = price23 * krw_balance23

                                # 보유 및 매수 가능 출력.
                                print(f"[ 23. {krw_coin23} 매수완료. ]")
                                print(f"매수시간 : {now}  |  코인명 : {coin23}  |  현재가 = ￦{price23}  |  MACD = ￦{macd23}  |  보유수량 = {krw_balance23}  |  평가금액 = ￦{bp23}")
                                print(f"매수가능 : {op_mode23} - 불가")
                                print("")

                            else:
                                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                                op_mode23 = False

                                print(f"[ 23. {krw_coin23} 잔고부족으로 매수불가. ]")
                                print(f"현재시간 : {now}  |  코인명 : {coin23}")
                                print(f"매수가능 : {op_mode23} - 불가")
                                print("")

                        else:
                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode23 = False

                            print(f"[ 23. {krw_coin23} 잔고부족으로 매수불가. ]")
                            print(f"현재시간 : {now}  |  코인명 : {coin23}")
                            print(f"매수가능 : {op_mode23} - 불가")
                            print("")

                    elif krw23 <= buy_krw:   # 매수가능금액 krw23 가 매수평균가 buy_krw 보다 같거나 작을때
                        if krw23 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                            # 매수금액은 매수가능금액인 krw23 로
                            upbit.buy_market_order(krw_coin23, krw23 * 0.99)   # 매수가능금액에서 1%를 빼고

                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode23 = False

                            # 1초 딜레이
                            #time.sleep(1)
                            # 보유수량 불러오기
                            krw_balance23 = upbit.get_balance(krw_coin23)
                            # 코인 현재가 불러오기
                            price23 = pyupbit.get_current_price(krw_coin23)
                            # 보유코인 원화금액으로 계산하기
                            bp23 = price23 * krw_balance23

                            # 보유 및 매수 가능 출력.
                            print(f"[ 23. {krw_coin23} 매수완료. ]")
                            print(f"매수시간 : {now}  |  코인명 : {coin23}  |  현재가 = ￦{price23}  |  MACD = ￦{macd23}  |  보유수량 = {krw_balance23}  |  평가금액 = ￦{bp23}")
                            print(f"매수가능 : {op_mode23} - 불가")
                            print("")

                        else:
                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode23 = False

                            print(f"[ 23. {krw_coin23} 잔고부족으로 매수불가. ]")
                            print(f"현재시간 : {now}  |  코인명 : {coin23}")
                            print(f"매수가능 : {op_mode23} - 불가")
                            print("")

            elif macd23 < 0:       # macd가 0보다 낮을때는 매도
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
                        print(f"매도시간 : {now}  |  코인명 : {coin23}  |  현재가 = ￦{price23}  |  MACD = ￦{macd23}  |  보유수량 = {krw_balance23}  |  평가금액 = ￦{bp23}")
                        print(f"매수가능 : {op_mode23} - 가능")
                        print("")

                    else:   # 보유코인 평가 금액이 10,100원 이하일때
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode23 = True

                        print(f"[ 23. {krw_coin23} 보유코인이 없으므로 매도불가. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin23}")
                        print(f"매수가능 : {op_mode23} - 가능")
                        print("")

            # 1초 딜레이.
            time.sleep(1)
            ##### 23번 코인 매매 종료 #####
            #############################


            ###############################
            ##### 매매 : 24번코인 시작. #####

            ##### 코인보유현황
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
            #time.sleep(1)


            # 코인 현재가 불러오기
            price24 = pyupbit.get_current_price(krw_coin24)

            # MACD 조회.
            #macd24 = get_macd(krw_coin24)
            # 거래량 동반한 MACD 조회.
            macd24 = get_acc_macd(krw_coin24)
            # 20일 이평선 조회.
            #macd24 = get_ma20(krw_coin24)

            # 매수가능금액 불러오기
            krw24 = upbit.get_balance("KRW")

            # MACD 조건문
            if macd24 >= 0:     # macd가 0보다 높을때는 매수
                if op_mode24 == True:    # 매수 가능(True)일 경우 - 매수시도
                    if krw24 > buy_krw:      # 매수가능금액 krw24 가 매수평균가 buy_krw 보다 클때
                        if krw24 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                            if buy_krw > 10100:     # 매수평균가 buy_krw 가 10,100원 초과일 경우 : 매수
                                # 매수금액은 매수평균가 buy_krw 로
                                upbit.buy_market_order(krw_coin24, buy_krw * 0.99)   # 매수가능금액에서 1%를 빼고

                                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                                op_mode24 = False

                                # 1초 딜레이
                                #time.sleep(1)
                                # 보유수량 불러오기
                                krw_balance24 = upbit.get_balance(krw_coin24)
                                # 코인 현재가 불러오기
                                price24 = pyupbit.get_current_price(krw_coin24)
                                # 보유코인 원화금액으로 계산하기
                                bp24 = price24 * krw_balance24

                                # 보유 및 매수 가능 출력.
                                print(f"[ 24. {krw_coin24} 매수완료. ]")
                                print(f"매수시간 : {now}  |  코인명 : {coin24}  |  현재가 = ￦{price24}  |  MACD = ￦{macd24}  |  보유수량 = {krw_balance24}  |  평가금액 = ￦{bp24}")
                                print(f"매수가능 : {op_mode24} - 불가")
                                print("")

                            else:
                                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                                op_mode24 = False

                                print(f"[ 24. {krw_coin24} 잔고부족으로 매수불가. ]")
                                print(f"현재시간 : {now}  |  코인명 : {coin24}")
                                print(f"매수가능 : {op_mode24} - 불가")
                                print("")

                        else:
                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode24 = False

                            print(f"[ 24. {krw_coin24} 잔고부족으로 매수불가. ]")
                            print(f"현재시간 : {now}  |  코인명 : {coin24}")
                            print(f"매수가능 : {op_mode24} - 불가")
                            print("")

                    elif krw24 <= buy_krw:   # 매수가능금액 krw24 가 매수평균가 buy_krw 보다 같거나 작을때
                        if krw24 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                            # 매수금액은 매수가능금액인 krw24 로
                            upbit.buy_market_order(krw_coin24, krw24 * 0.99)   # 매수가능금액에서 1%를 빼고

                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode24 = False

                            # 1초 딜레이
                            #time.sleep(1)
                            # 보유수량 불러오기
                            krw_balance24 = upbit.get_balance(krw_coin24)
                            # 코인 현재가 불러오기
                            price24 = pyupbit.get_current_price(krw_coin24)
                            # 보유코인 원화금액으로 계산하기
                            bp24 = price24 * krw_balance24

                            # 보유 및 매수 가능 출력.
                            print(f"[ 24. {krw_coin24} 매수완료. ]")
                            print(f"매수시간 : {now}  |  코인명 : {coin24}  |  현재가 = ￦{price24}  |  MACD = ￦{macd24}  |  보유수량 = {krw_balance24}  |  평가금액 = ￦{bp24}")
                            print(f"매수가능 : {op_mode24} - 불가")
                            print("")

                        else:
                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode24 = False

                            print(f"[ 24. {krw_coin24} 잔고부족으로 매수불가. ]")
                            print(f"현재시간 : {now}  |  코인명 : {coin24}")
                            print(f"매수가능 : {op_mode24} - 불가")
                            print("")

            elif macd24 < 0:       # macd가 0보다 낮을때는 매도
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
                        print(f"매도시간 : {now}  |  코인명 : {coin24}  |  현재가 = ￦{price24}  |  MACD = ￦{macd24}  |  보유수량 = {krw_balance24}  |  평가금액 = ￦{bp24}")
                        print(f"매수가능 : {op_mode24} - 가능")
                        print("")

                    else:   # 보유코인 평가 금액이 10,100원 이하일때
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode24 = True

                        print(f"[ 24. {krw_coin24} 보유코인이 없으므로 매도불가. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin24}")
                        print(f"매수가능 : {op_mode24} - 가능")
                        print("")

            # 1초 딜레이.
            time.sleep(1)
            ##### 24번 코인 매매 종료 #####
            #############################


            ###############################
            ##### 매매 : 25번코인 시작. #####

            ##### 코인보유현황
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
            #time.sleep(1)


            # 코인 현재가 불러오기
            price25 = pyupbit.get_current_price(krw_coin25)

            # MACD 조회.
            #macd25 = get_macd(krw_coin25)
            # 거래량 동반한 MACD 조회.
            macd25 = get_acc_macd(krw_coin25)
            # 20일 이평선 조회.
            #macd25 = get_ma20(krw_coin25)

            # 매수가능금액 불러오기
            krw25 = upbit.get_balance("KRW")

            # MACD 조건문
            if macd25 >= 0:     # macd가 0보다 높을때는 매수
                if op_mode25 == True:    # 매수 가능(True)일 경우 - 매수시도
                    if krw25 > buy_krw:      # 매수가능금액 krw25 가 매수평균가 buy_krw 보다 클때
                        if krw25 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                            if buy_krw > 10100:     # 매수평균가 buy_krw 가 10,100원 초과일 경우 : 매수
                                # 매수금액은 매수평균가 buy_krw 로
                                upbit.buy_market_order(krw_coin25, buy_krw * 0.99)   # 매수가능금액에서 1%를 빼고

                                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                                op_mode25 = False

                                # 1초 딜레이
                                #time.sleep(1)
                                # 보유수량 불러오기
                                krw_balance25 = upbit.get_balance(krw_coin25)
                                # 코인 현재가 불러오기
                                price25 = pyupbit.get_current_price(krw_coin25)
                                # 보유코인 원화금액으로 계산하기
                                bp25 = price25 * krw_balance25

                                # 보유 및 매수 가능 출력.
                                print(f"[ 25. {krw_coin25} 매수완료. ]")
                                print(f"매수시간 : {now}  |  코인명 : {coin25}  |  현재가 = ￦{price25}  |  MACD = ￦{macd25}  |  보유수량 = {krw_balance25}  |  평가금액 = ￦{bp25}")
                                print(f"매수가능 : {op_mode25} - 불가")
                                print("")

                            else:
                                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                                op_mode25 = False

                                print(f"[ 25. {krw_coin25} 잔고부족으로 매수불가. ]")
                                print(f"현재시간 : {now}  |  코인명 : {coin25}")
                                print(f"매수가능 : {op_mode25} - 불가")
                                print("")

                        else:
                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode25 = False

                            print(f"[ 25. {krw_coin25} 잔고부족으로 매수불가. ]")
                            print(f"현재시간 : {now}  |  코인명 : {coin25}")
                            print(f"매수가능 : {op_mode25} - 불가")
                            print("")

                    elif krw25 <= buy_krw:   # 매수가능금액 krw25 가 매수평균가 buy_krw 보다 같거나 작을때
                        if krw25 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                            # 매수금액은 매수가능금액인 krw25 로
                            upbit.buy_market_order(krw_coin25, krw25 * 0.99)   # 매수가능금액에서 1%를 빼고

                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode25 = False

                            # 1초 딜레이
                            #time.sleep(1)
                            # 보유수량 불러오기
                            krw_balance25 = upbit.get_balance(krw_coin25)
                            # 코인 현재가 불러오기
                            price25 = pyupbit.get_current_price(krw_coin25)
                            # 보유코인 원화금액으로 계산하기
                            bp25 = price25 * krw_balance25

                            # 보유 및 매수 가능 출력.
                            print(f"[ 25. {krw_coin25} 매수완료. ]")
                            print(f"매수시간 : {now}  |  코인명 : {coin25}  |  현재가 = ￦{price25}  |  MACD = ￦{macd25}  |  보유수량 = {krw_balance25}  |  평가금액 = ￦{bp25}")
                            print(f"매수가능 : {op_mode25} - 불가")
                            print("")

                        else:
                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode25 = False

                            print(f"[ 25. {krw_coin25} 잔고부족으로 매수불가. ]")
                            print(f"현재시간 : {now}  |  코인명 : {coin25}")
                            print(f"매수가능 : {op_mode25} - 불가")
                            print("")

            elif macd25 < 0:       # macd가 0보다 낮을때는 매도
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
                        print(f"매도시간 : {now}  |  코인명 : {coin25}  |  현재가 = ￦{price25}  |  MACD = ￦{macd25}  |  보유수량 = {krw_balance25}  |  평가금액 = ￦{bp25}")
                        print(f"매수가능 : {op_mode25} - 가능")
                        print("")

                    else:   # 보유코인 평가 금액이 10,100원 이하일때
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode25 = True

                        print(f"[ 25. {krw_coin25} 보유코인이 없으므로 매도불가. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin25}")
                        print(f"매수가능 : {op_mode25} - 가능")
                        print("")

            # 1초 딜레이.
            time.sleep(1)
            ##### 25번 코인 매매 종료 #####
            #############################


            ###############################
            ##### 매매 : 26번코인 시작. #####

            ##### 코인보유현황
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
            #time.sleep(1)


            # 코인 현재가 불러오기
            price26 = pyupbit.get_current_price(krw_coin26)

            # MACD 조회.
            #macd26 = get_macd(krw_coin26)
            # 거래량 동반한 MACD 조회.
            macd26 = get_acc_macd(krw_coin26)
            # 20일 이평선 조회.
            #macd26 = get_ma20(krw_coin26)

            # 매수가능금액 불러오기
            krw26 = upbit.get_balance("KRW")

            # MACD 조건문
            if macd26 >= 0:     # macd가 0보다 높을때는 매수
                if op_mode26 == True:    # 매수 가능(True)일 경우 - 매수시도
                    if krw26 > buy_krw:      # 매수가능금액 krw26 가 매수평균가 buy_krw 보다 클때
                        if krw26 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                            if buy_krw > 10100:     # 매수평균가 buy_krw 가 10,100원 초과일 경우 : 매수
                                # 매수금액은 매수평균가 buy_krw 로
                                upbit.buy_market_order(krw_coin26, buy_krw * 0.99)   # 매수가능금액에서 1%를 빼고

                                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                                op_mode26 = False

                                # 1초 딜레이
                                #time.sleep(1)
                                # 보유수량 불러오기
                                krw_balance26 = upbit.get_balance(krw_coin26)
                                # 코인 현재가 불러오기
                                price26 = pyupbit.get_current_price(krw_coin26)
                                # 보유코인 원화금액으로 계산하기
                                bp26 = price26 * krw_balance26

                                # 보유 및 매수 가능 출력.
                                print(f"[ 26. {krw_coin26} 매수완료. ]")
                                print(f"매수시간 : {now}  |  코인명 : {coin26}  |  현재가 = ￦{price26}  |  MACD = ￦{macd26}  |  보유수량 = {krw_balance26}  |  평가금액 = ￦{bp26}")
                                print(f"매수가능 : {op_mode26} - 불가")
                                print("")

                            else:
                                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                                op_mode26 = False

                                print(f"[ 26. {krw_coin26} 잔고부족으로 매수불가. ]")
                                print(f"현재시간 : {now}  |  코인명 : {coin26}")
                                print(f"매수가능 : {op_mode26} - 불가")
                                print("")

                        else:
                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode26 = False

                            print(f"[ 26. {krw_coin26} 잔고부족으로 매수불가. ]")
                            print(f"현재시간 : {now}  |  코인명 : {coin26}")
                            print(f"매수가능 : {op_mode26} - 불가")
                            print("")

                    elif krw26 <= buy_krw:   # 매수가능금액 krw26 가 매수평균가 buy_krw 보다 같거나 작을때
                        if krw26 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                            # 매수금액은 매수가능금액인 krw26 로
                            upbit.buy_market_order(krw_coin26, krw26 * 0.99)   # 매수가능금액에서 1%를 빼고

                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode26 = False

                            # 1초 딜레이
                            #time.sleep(1)
                            # 보유수량 불러오기
                            krw_balance26 = upbit.get_balance(krw_coin26)
                            # 코인 현재가 불러오기
                            price26 = pyupbit.get_current_price(krw_coin26)
                            # 보유코인 원화금액으로 계산하기
                            bp26 = price26 * krw_balance26

                            # 보유 및 매수 가능 출력.
                            print(f"[ 26. {krw_coin26} 매수완료. ]")
                            print(f"매수시간 : {now}  |  코인명 : {coin26}  |  현재가 = ￦{price26}  |  MACD = ￦{macd26}  |  보유수량 = {krw_balance26}  |  평가금액 = ￦{bp26}")
                            print(f"매수가능 : {op_mode26} - 불가")
                            print("")

                        else:
                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode26 = False

                            print(f"[ 26. {krw_coin26} 잔고부족으로 매수불가. ]")
                            print(f"현재시간 : {now}  |  코인명 : {coin26}")
                            print(f"매수가능 : {op_mode26} - 불가")
                            print("")

            elif macd26 < 0:       # macd가 0보다 낮을때는 매도
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
                        print(f"매도시간 : {now}  |  코인명 : {coin26}  |  현재가 = ￦{price26}  |  MACD = ￦{macd26}  |  보유수량 = {krw_balance26}  |  평가금액 = ￦{bp26}")
                        print(f"매수가능 : {op_mode26} - 가능")
                        print("")

                    else:   # 보유코인 평가 금액이 10,100원 이하일때
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode26 = True

                        print(f"[ 26. {krw_coin26} 보유코인이 없으므로 매도불가. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin26}")
                        print(f"매수가능 : {op_mode26} - 가능")
                        print("")

            # 1초 딜레이.
            time.sleep(1)
            ##### 26번 코인 매매 종료 #####
            #############################


            ###############################
            ##### 매매 : 27번코인 시작. #####

            ##### 코인보유현황
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
            #time.sleep(1)


            # 코인 현재가 불러오기
            price27 = pyupbit.get_current_price(krw_coin27)

            # MACD 조회.
            #macd27 = get_macd(krw_coin27)
            # 거래량 동반한 MACD 조회.
            macd27 = get_acc_macd(krw_coin27)
            # 20일 이평선 조회.
            #macd27 = get_ma20(krw_coin27)

            # 매수가능금액 불러오기
            krw27 = upbit.get_balance("KRW")

            # MACD 조건문
            if macd27 >= 0:     # macd가 0보다 높을때는 매수
                if op_mode27 == True:    # 매수 가능(True)일 경우 - 매수시도
                    if krw27 > buy_krw:      # 매수가능금액 krw27 가 매수평균가 buy_krw 보다 클때
                        if krw27 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                            if buy_krw > 10100:     # 매수평균가 buy_krw 가 10,100원 초과일 경우 : 매수
                                # 매수금액은 매수평균가 buy_krw 로
                                upbit.buy_market_order(krw_coin27, buy_krw * 0.99)   # 매수가능금액에서 1%를 빼고

                                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                                op_mode27 = False

                                # 1초 딜레이
                                #time.sleep(1)
                                # 보유수량 불러오기
                                krw_balance27 = upbit.get_balance(krw_coin27)
                                # 코인 현재가 불러오기
                                price27 = pyupbit.get_current_price(krw_coin27)
                                # 보유코인 원화금액으로 계산하기
                                bp27 = price27 * krw_balance27

                                # 보유 및 매수 가능 출력.
                                print(f"[ 27. {krw_coin27} 매수완료. ]")
                                print(f"매수시간 : {now}  |  코인명 : {coin27}  |  현재가 = ￦{price27}  |  MACD = ￦{macd27}  |  보유수량 = {krw_balance27}  |  평가금액 = ￦{bp27}")
                                print(f"매수가능 : {op_mode27} - 불가")
                                print("")

                            else:
                                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                                op_mode27 = False

                                print(f"[ 27. {krw_coin27} 잔고부족으로 매수불가. ]")
                                print(f"현재시간 : {now}  |  코인명 : {coin27}")
                                print(f"매수가능 : {op_mode27} - 불가")
                                print("")

                        else:
                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode27 = False

                            print(f"[ 27. {krw_coin27} 잔고부족으로 매수불가. ]")
                            print(f"현재시간 : {now}  |  코인명 : {coin27}")
                            print(f"매수가능 : {op_mode27} - 불가")
                            print("")

                    elif krw27 <= buy_krw:   # 매수가능금액 krw27 가 매수평균가 buy_krw 보다 같거나 작을때
                        if krw27 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                            # 매수금액은 매수가능금액인 krw27 로
                            upbit.buy_market_order(krw_coin27, krw27 * 0.99)   # 매수가능금액에서 1%를 빼고

                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode27 = False

                            # 1초 딜레이
                            #time.sleep(1)
                            # 보유수량 불러오기
                            krw_balance27 = upbit.get_balance(krw_coin27)
                            # 코인 현재가 불러오기
                            price27 = pyupbit.get_current_price(krw_coin27)
                            # 보유코인 원화금액으로 계산하기
                            bp27 = price27 * krw_balance27

                            # 보유 및 매수 가능 출력.
                            print(f"[ 27. {krw_coin27} 매수완료. ]")
                            print(f"매수시간 : {now}  |  코인명 : {coin27}  |  현재가 = ￦{price27}  |  MACD = ￦{macd27}  |  보유수량 = {krw_balance27}  |  평가금액 = ￦{bp27}")
                            print(f"매수가능 : {op_mode27} - 불가")
                            print("")

                        else:
                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode27 = False

                            print(f"[ 27. {krw_coin27} 잔고부족으로 매수불가. ]")
                            print(f"현재시간 : {now}  |  코인명 : {coin27}")
                            print(f"매수가능 : {op_mode27} - 불가")
                            print("")

            elif macd27 < 0:       # macd가 0보다 낮을때는 매도
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
                        print(f"매도시간 : {now}  |  코인명 : {coin27}  |  현재가 = ￦{price27}  |  MACD = ￦{macd27}  |  보유수량 = {krw_balance27}  |  평가금액 = ￦{bp27}")
                        print(f"매수가능 : {op_mode27} - 가능")
                        print("")

                    else:   # 보유코인 평가 금액이 10,100원 이하일때
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode27 = True

                        print(f"[ 27. {krw_coin27} 보유코인이 없으므로 매도불가. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin27}")
                        print(f"매수가능 : {op_mode27} - 가능")
                        print("")

            # 1초 딜레이.
            time.sleep(1)
            ##### 27번 코인 매매 종료 #####
            #############################


            ###############################
            ##### 매매 : 28번코인 시작. #####

            ##### 코인보유현황
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
            #time.sleep(1)


            # 코인 현재가 불러오기
            price28 = pyupbit.get_current_price(krw_coin28)

            # MACD 조회.
            #macd28 = get_macd(krw_coin28)
            # 거래량 동반한 MACD 조회.
            macd28 = get_acc_macd(krw_coin28)
            # 20일 이평선 조회.
            #macd28 = get_ma20(krw_coin28)

            # 매수가능금액 불러오기
            krw28 = upbit.get_balance("KRW")

            # MACD 조건문
            if macd28 >= 0:     # macd가 0보다 높을때는 매수
                if op_mode28 == True:    # 매수 가능(True)일 경우 - 매수시도
                    if krw28 > buy_krw:      # 매수가능금액 krw28 가 매수평균가 buy_krw 보다 클때
                        if krw28 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                            if buy_krw > 10100:     # 매수평균가 buy_krw 가 10,100원 초과일 경우 : 매수
                                # 매수금액은 매수평균가 buy_krw 로
                                upbit.buy_market_order(krw_coin28, buy_krw * 0.99)   # 매수가능금액에서 1%를 빼고

                                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                                op_mode28 = False

                                # 1초 딜레이
                                #time.sleep(1)
                                # 보유수량 불러오기
                                krw_balance28 = upbit.get_balance(krw_coin28)
                                # 코인 현재가 불러오기
                                price28 = pyupbit.get_current_price(krw_coin28)
                                # 보유코인 원화금액으로 계산하기
                                bp28 = price28 * krw_balance28

                                # 보유 및 매수 가능 출력.
                                print(f"[ 28. {krw_coin28} 매수완료. ]")
                                print(f"매수시간 : {now}  |  코인명 : {coin28}  |  현재가 = ￦{price28}  |  MACD = ￦{macd28}  |  보유수량 = {krw_balance28}  |  평가금액 = ￦{bp28}")
                                print(f"매수가능 : {op_mode28} - 불가")
                                print("")

                            else:
                                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                                op_mode28 = False

                                print(f"[ 28. {krw_coin28} 잔고부족으로 매수불가. ]")
                                print(f"현재시간 : {now}  |  코인명 : {coin28}")
                                print(f"매수가능 : {op_mode28} - 불가")
                                print("")

                        else:
                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode28 = False

                            print(f"[ 28. {krw_coin28} 잔고부족으로 매수불가. ]")
                            print(f"현재시간 : {now}  |  코인명 : {coin28}")
                            print(f"매수가능 : {op_mode28} - 불가")
                            print("")

                    elif krw28 <= buy_krw:   # 매수가능금액 krw28 가 매수평균가 buy_krw 보다 같거나 작을때
                        if krw28 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                            # 매수금액은 매수가능금액인 krw28 로
                            upbit.buy_market_order(krw_coin28, krw28 * 0.99)   # 매수가능금액에서 1%를 빼고

                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode28 = False

                            # 1초 딜레이
                            #time.sleep(1)
                            # 보유수량 불러오기
                            krw_balance28 = upbit.get_balance(krw_coin28)
                            # 코인 현재가 불러오기
                            price28 = pyupbit.get_current_price(krw_coin28)
                            # 보유코인 원화금액으로 계산하기
                            bp28 = price28 * krw_balance28

                            # 보유 및 매수 가능 출력.
                            print(f"[ 28. {krw_coin28} 매수완료. ]")
                            print(f"매수시간 : {now}  |  코인명 : {coin28}  |  현재가 = ￦{price28}  |  MACD = ￦{macd28}  |  보유수량 = {krw_balance28}  |  평가금액 = ￦{bp28}")
                            print(f"매수가능 : {op_mode28} - 불가")
                            print("")

                        else:
                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode28 = False

                            print(f"[ 28. {krw_coin28} 잔고부족으로 매수불가. ]")
                            print(f"현재시간 : {now}  |  코인명 : {coin28}")
                            print(f"매수가능 : {op_mode28} - 불가")
                            print("")

            elif macd28 < 0:       # macd가 0보다 낮을때는 매도
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
                        print(f"매도시간 : {now}  |  코인명 : {coin28}  |  현재가 = ￦{price28}  |  MACD = ￦{macd28}  |  보유수량 = {krw_balance28}  |  평가금액 = ￦{bp28}")
                        print(f"매수가능 : {op_mode28} - 가능")
                        print("")

                    else:   # 보유코인 평가 금액이 10,100원 이하일때
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode28 = True

                        print(f"[ 28. {krw_coin28} 보유코인이 없으므로 매도불가. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin28}")
                        print(f"매수가능 : {op_mode28} - 가능")
                        print("")

            # 1초 딜레이.
            time.sleep(1)
            ##### 28번 코인 매매 종료 #####
            #############################


            ###############################
            ##### 매매 : 29번코인 시작. #####

            ##### 코인보유현황
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
            #time.sleep(1)


            # 코인 현재가 불러오기
            price29 = pyupbit.get_current_price(krw_coin29)

            # MACD 조회.
            #macd29 = get_macd(krw_coin29)
            # 거래량 동반한 MACD 조회.
            macd29 = get_acc_macd(krw_coin29)
            # 20일 이평선 조회.
            #macd29 = get_ma20(krw_coin29)

            # 매수가능금액 불러오기
            krw29 = upbit.get_balance("KRW")

            # MACD 조건문
            if macd29 >= 0:     # macd가 0보다 높을때는 매수
                if op_mode29 == True:    # 매수 가능(True)일 경우 - 매수시도
                    if krw29 > buy_krw:      # 매수가능금액 krw29 가 매수평균가 buy_krw 보다 클때
                        if krw29 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                            if buy_krw > 10100:     # 매수평균가 buy_krw 가 10,100원 초과일 경우 : 매수
                                # 매수금액은 매수평균가 buy_krw 로
                                upbit.buy_market_order(krw_coin29, buy_krw * 0.99)   # 매수가능금액에서 1%를 빼고

                                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                                op_mode29 = False

                                # 1초 딜레이
                                #time.sleep(1)
                                # 보유수량 불러오기
                                krw_balance29 = upbit.get_balance(krw_coin29)
                                # 코인 현재가 불러오기
                                price29 = pyupbit.get_current_price(krw_coin29)
                                # 보유코인 원화금액으로 계산하기
                                bp29 = price29 * krw_balance29

                                # 보유 및 매수 가능 출력.
                                print(f"[ 29. {krw_coin29} 매수완료. ]")
                                print(f"매수시간 : {now}  |  코인명 : {coin29}  |  현재가 = ￦{price29}  |  MACD = ￦{macd29}  |  보유수량 = {krw_balance29}  |  평가금액 = ￦{bp29}")
                                print(f"매수가능 : {op_mode29} - 불가")
                                print("")

                            else:
                                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                                op_mode29 = False

                                print(f"[ 29. {krw_coin29} 잔고부족으로 매수불가. ]")
                                print(f"현재시간 : {now}  |  코인명 : {coin29}")
                                print(f"매수가능 : {op_mode29} - 불가")
                                print("")

                        else:
                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode29 = False

                            print(f"[ 29. {krw_coin29} 잔고부족으로 매수불가. ]")
                            print(f"현재시간 : {now}  |  코인명 : {coin29}")
                            print(f"매수가능 : {op_mode29} - 불가")
                            print("")

                    elif krw29 <= buy_krw:   # 매수가능금액 krw29 가 매수평균가 buy_krw 보다 같거나 작을때
                        if krw29 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                            # 매수금액은 매수가능금액인 krw29 로
                            upbit.buy_market_order(krw_coin29, krw29 * 0.99)   # 매수가능금액에서 1%를 빼고

                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode29 = False

                            # 1초 딜레이
                            #time.sleep(1)
                            # 보유수량 불러오기
                            krw_balance29 = upbit.get_balance(krw_coin29)
                            # 코인 현재가 불러오기
                            price29 = pyupbit.get_current_price(krw_coin29)
                            # 보유코인 원화금액으로 계산하기
                            bp29 = price29 * krw_balance29

                            # 보유 및 매수 가능 출력.
                            print(f"[ 29. {krw_coin29} 매수완료. ]")
                            print(f"매수시간 : {now}  |  코인명 : {coin29}  |  현재가 = ￦{price29}  |  MACD = ￦{macd29}  |  보유수량 = {krw_balance29}  |  평가금액 = ￦{bp29}")
                            print(f"매수가능 : {op_mode29} - 불가")
                            print("")

                        else:
                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode29 = False

                            print(f"[ 29. {krw_coin29} 잔고부족으로 매수불가. ]")
                            print(f"현재시간 : {now}  |  코인명 : {coin29}")
                            print(f"매수가능 : {op_mode29} - 불가")
                            print("")

            elif macd29 < 0:       # macd가 0보다 낮을때는 매도
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
                        print(f"매도시간 : {now}  |  코인명 : {coin29}  |  현재가 = ￦{price29}  |  MACD = ￦{macd29}  |  보유수량 = {krw_balance29}  |  평가금액 = ￦{bp29}")
                        print(f"매수가능 : {op_mode29} - 가능")
                        print("")

                    else:   # 보유코인 평가 금액이 10,100원 이하일때
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode29 = True

                        print(f"[ 29. {krw_coin29} 보유코인이 없으므로 매도불가. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin29}")
                        print(f"매수가능 : {op_mode29} - 가능")
                        print("")

            # 1초 딜레이.
            time.sleep(1)
            ##### 29번 코인 매매 종료 #####
            #############################


            ###############################
            ##### 매매 : 30번코인 시작. #####

            ##### 코인보유현황
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
            #time.sleep(1)


            # 코인 현재가 불러오기
            price30 = pyupbit.get_current_price(krw_coin30)

            # MACD 조회.
            #macd30 = get_macd(krw_coin30)
            # 거래량 동반한 MACD 조회.
            macd30 = get_acc_macd(krw_coin30)
            # 20일 이평선 조회.
            #macd30 = get_ma20(krw_coin30)

            # 매수가능금액 불러오기
            krw30 = upbit.get_balance("KRW")

            # MACD 조건문
            if macd30 >= 0:     # macd가 0보다 높을때는 매수
                if op_mode30 == True:    # 매수 가능(True)일 경우 - 매수시도
                    if krw30 > buy_krw:      # 매수가능금액 krw30 가 매수평균가 buy_krw 보다 클때
                        if krw30 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                            if buy_krw > 10100:     # 매수평균가 buy_krw 가 10,100원 초과일 경우 : 매수
                                # 매수금액은 매수평균가 buy_krw 로
                                upbit.buy_market_order(krw_coin30, buy_krw * 0.99)   # 매수가능금액에서 1%를 빼고

                                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                                op_mode30 = False

                                # 1초 딜레이
                                #time.sleep(1)
                                # 보유수량 불러오기
                                krw_balance30 = upbit.get_balance(krw_coin30)
                                # 코인 현재가 불러오기
                                price30 = pyupbit.get_current_price(krw_coin30)
                                # 보유코인 원화금액으로 계산하기
                                bp30 = price30 * krw_balance30

                                # 보유 및 매수 가능 출력.
                                print(f"[ 30. {krw_coin30} 매수완료. ]")
                                print(f"매수시간 : {now}  |  코인명 : {coin30}  |  현재가 = ￦{price30}  |  MACD = ￦{macd30}  |  보유수량 = {krw_balance30}  |  평가금액 = ￦{bp30}")
                                print(f"매수가능 : {op_mode30} - 불가")
                                print("")

                            else:
                                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                                op_mode30 = False

                                print(f"[ 30. {krw_coin30} 잔고부족으로 매수불가. ]")
                                print(f"현재시간 : {now}  |  코인명 : {coin30}")
                                print(f"매수가능 : {op_mode30} - 불가")
                                print("")

                        else:
                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode30 = False

                            print(f"[ 30. {krw_coin30} 잔고부족으로 매수불가. ]")
                            print(f"현재시간 : {now}  |  코인명 : {coin30}")
                            print(f"매수가능 : {op_mode30} - 불가")
                            print("")

                    elif krw30 <= buy_krw:   # 매수가능금액 krw30 가 매수평균가 buy_krw 보다 같거나 작을때
                        if krw30 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                            # 매수금액은 매수가능금액인 krw30 로
                            upbit.buy_market_order(krw_coin30, krw30 * 0.99)   # 매수가능금액에서 1%를 빼고

                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode30 = False

                            # 1초 딜레이
                            #time.sleep(1)
                            # 보유수량 불러오기
                            krw_balance30 = upbit.get_balance(krw_coin30)
                            # 코인 현재가 불러오기
                            price30 = pyupbit.get_current_price(krw_coin30)
                            # 보유코인 원화금액으로 계산하기
                            bp30 = price30 * krw_balance30

                            # 보유 및 매수 가능 출력.
                            print(f"[ 30. {krw_coin30} 매수완료. ]")
                            print(f"매수시간 : {now}  |  코인명 : {coin30}  |  현재가 = ￦{price30}  |  MACD = ￦{macd30}  |  보유수량 = {krw_balance30}  |  평가금액 = ￦{bp30}")
                            print(f"매수가능 : {op_mode30} - 불가")
                            print("")

                        else:
                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode30 = False

                            print(f"[ 30. {krw_coin30} 잔고부족으로 매수불가. ]")
                            print(f"현재시간 : {now}  |  코인명 : {coin30}")
                            print(f"매수가능 : {op_mode30} - 불가")
                            print("")

            elif macd30 < 0:       # macd가 0보다 낮을때는 매도
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
                        print(f"매도시간 : {now}  |  코인명 : {coin30}  |  현재가 = ￦{price30}  |  MACD = ￦{macd30}  |  보유수량 = {krw_balance30}  |  평가금액 = ￦{bp30}")
                        print(f"매수가능 : {op_mode30} - 가능")
                        print("")

                    else:   # 보유코인 평가 금액이 10,100원 이하일때
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode30 = True

                        print(f"[ 30. {krw_coin30} 보유코인이 없으므로 매도불가. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin30}")
                        print(f"매수가능 : {op_mode30} - 가능")
                        print("")

            # 1초 딜레이.
            time.sleep(1)
            ##### 30번 코인 매매 종료 #####
            #############################


            ######################################################################################################################################################
            ######################################################################################################################################################
            ######################################################################################################################################################
            ######################################################################################################################################################
            ######################################################################################################################################################


            

            ###############################
            ##### 매매 : 31번코인 시작. #####

            ##### 코인보유현황
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
            #time.sleep(1)


            # 코인 현재가 불러오기
            price31 = pyupbit.get_current_price(krw_coin31)

            # MACD 조회.
            #macd31 = get_macd(krw_coin31)
            # 거래량 동반한 MACD 조회.
            macd31 = get_acc_macd(krw_coin31)
            # 20일 이평선 조회.
            #macd31 = get_ma20(krw_coin31)

            # 매수가능금액 불러오기
            krw31 = upbit.get_balance("KRW")

            # MACD 조건문
            if macd31 >= 0:     # macd가 0보다 높을때는 매수
                if op_mode31 == True:    # 매수 가능(True)일 경우 - 매수시도
                    if krw31 > buy_krw:      # 매수가능금액 krw31 가 매수평균가 buy_krw 보다 클때
                        if krw31 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                            if buy_krw > 10100:     # 매수평균가 buy_krw 가 10,100원 초과일 경우 : 매수
                                # 매수금액은 매수평균가 buy_krw 로
                                upbit.buy_market_order(krw_coin31, buy_krw * 0.99)   # 매수가능금액에서 1%를 빼고

                                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                                op_mode31 = False

                                # 1초 딜레이
                                #time.sleep(1)
                                # 보유수량 불러오기
                                krw_balance31 = upbit.get_balance(krw_coin31)
                                # 코인 현재가 불러오기
                                price31 = pyupbit.get_current_price(krw_coin31)
                                # 보유코인 원화금액으로 계산하기
                                bp31 = price31 * krw_balance31

                                # 보유 및 매수 가능 출력.
                                print(f"[ 31. {krw_coin31} 매수완료. ]")
                                print(f"매수시간 : {now}  |  코인명 : {coin31}  |  현재가 = ￦{price31}  |  MACD = ￦{macd31}  |  보유수량 = {krw_balance31}  |  평가금액 = ￦{bp31}")
                                print(f"매수가능 : {op_mode31} - 불가")
                                print("")

                            else:
                                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                                op_mode31 = False

                                print(f"[ 31. {krw_coin31} 잔고부족으로 매수불가. ]")
                                print(f"현재시간 : {now}  |  코인명 : {coin31}")
                                print(f"매수가능 : {op_mode31} - 불가")
                                print("")

                        else:
                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode31 = False

                            print(f"[ 31. {krw_coin31} 잔고부족으로 매수불가. ]")
                            print(f"현재시간 : {now}  |  코인명 : {coin31}")
                            print(f"매수가능 : {op_mode31} - 불가")
                            print("")

                    elif krw31 <= buy_krw:   # 매수가능금액 krw31 가 매수평균가 buy_krw 보다 같거나 작을때
                        if krw31 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                            # 매수금액은 매수가능금액인 krw31 로
                            upbit.buy_market_order(krw_coin31, krw31 * 0.99)   # 매수가능금액에서 1%를 빼고

                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode31 = False

                            # 1초 딜레이
                            #time.sleep(1)
                            # 보유수량 불러오기
                            krw_balance31 = upbit.get_balance(krw_coin31)
                            # 코인 현재가 불러오기
                            price31 = pyupbit.get_current_price(krw_coin31)
                            # 보유코인 원화금액으로 계산하기
                            bp31 = price31 * krw_balance31

                            # 보유 및 매수 가능 출력.
                            print(f"[ 31. {krw_coin31} 매수완료. ]")
                            print(f"매수시간 : {now}  |  코인명 : {coin31}  |  현재가 = ￦{price31}  |  MACD = ￦{macd31}  |  보유수량 = {krw_balance31}  |  평가금액 = ￦{bp31}")
                            print(f"매수가능 : {op_mode31} - 불가")
                            print("")

                        else:
                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode31 = False

                            print(f"[ 31. {krw_coin31} 잔고부족으로 매수불가. ]")
                            print(f"현재시간 : {now}  |  코인명 : {coin31}")
                            print(f"매수가능 : {op_mode31} - 불가")
                            print("")

            elif macd31 < 0:       # macd가 0보다 낮을때는 매도
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
                        print(f"매도시간 : {now}  |  코인명 : {coin31}  |  현재가 = ￦{price31}  |  MACD = ￦{macd31}  |  보유수량 = {krw_balance31}  |  평가금액 = ￦{bp31}")
                        print(f"매수가능 : {op_mode31} - 가능")
                        print("")

                    else:   # 보유코인 평가 금액이 10,100원 이하일때
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode31 = True

                        print(f"[ 31. {krw_coin31} 보유코인이 없으므로 매도불가. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin31}")
                        print(f"매수가능 : {op_mode31} - 가능")
                        print("")

            # 1초 딜레이.
            time.sleep(1)
            ##### 31번 코인 매매 종료 #####
            #############################


            ###############################
            ##### 매매 : 32번코인 시작. #####

            ##### 코인보유현황
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
            #time.sleep(1)


            # 코인 현재가 불러오기
            price32 = pyupbit.get_current_price(krw_coin32)

            # MACD 조회.
            #macd32 = get_macd(krw_coin32)
            # 거래량 동반한 MACD 조회.
            macd32 = get_acc_macd(krw_coin32)
            # 20일 이평선 조회.
            #macd32 = get_ma20(krw_coin32)

            # 매수가능금액 불러오기
            krw32 = upbit.get_balance("KRW")

            # MACD 조건문
            if macd32 >= 0:     # macd가 0보다 높을때는 매수
                if op_mode32 == True:    # 매수 가능(True)일 경우 - 매수시도
                    if krw32 > buy_krw:      # 매수가능금액 krw32 가 매수평균가 buy_krw 보다 클때
                        if krw32 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                            if buy_krw > 10100:     # 매수평균가 buy_krw 가 10,100원 초과일 경우 : 매수
                                # 매수금액은 매수평균가 buy_krw 로
                                upbit.buy_market_order(krw_coin32, buy_krw * 0.99)   # 매수가능금액에서 1%를 빼고

                                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                                op_mode32 = False

                                # 1초 딜레이
                                #time.sleep(1)
                                # 보유수량 불러오기
                                krw_balance32 = upbit.get_balance(krw_coin32)
                                # 코인 현재가 불러오기
                                price32 = pyupbit.get_current_price(krw_coin32)
                                # 보유코인 원화금액으로 계산하기
                                bp32 = price32 * krw_balance32

                                # 보유 및 매수 가능 출력.
                                print(f"[ 32. {krw_coin32} 매수완료. ]")
                                print(f"매수시간 : {now}  |  코인명 : {coin32}  |  현재가 = ￦{price32}  |  MACD = ￦{macd32}  |  보유수량 = {krw_balance32}  |  평가금액 = ￦{bp32}")
                                print(f"매수가능 : {op_mode32} - 불가")
                                print("")

                            else:
                                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                                op_mode32 = False

                                print(f"[ 32. {krw_coin32} 잔고부족으로 매수불가. ]")
                                print(f"현재시간 : {now}  |  코인명 : {coin32}")
                                print(f"매수가능 : {op_mode32} - 불가")
                                print("")

                        else:
                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode32 = False

                            print(f"[ 32. {krw_coin32} 잔고부족으로 매수불가. ]")
                            print(f"현재시간 : {now}  |  코인명 : {coin32}")
                            print(f"매수가능 : {op_mode32} - 불가")
                            print("")

                    elif krw32 <= buy_krw:   # 매수가능금액 krw32 가 매수평균가 buy_krw 보다 같거나 작을때
                        if krw32 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                            # 매수금액은 매수가능금액인 krw32 로
                            upbit.buy_market_order(krw_coin32, krw32 * 0.99)   # 매수가능금액에서 1%를 빼고

                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode32 = False

                            # 1초 딜레이
                            #time.sleep(1)
                            # 보유수량 불러오기
                            krw_balance32 = upbit.get_balance(krw_coin32)
                            # 코인 현재가 불러오기
                            price32 = pyupbit.get_current_price(krw_coin32)
                            # 보유코인 원화금액으로 계산하기
                            bp32 = price32 * krw_balance32

                            # 보유 및 매수 가능 출력.
                            print(f"[ 32. {krw_coin32} 매수완료. ]")
                            print(f"매수시간 : {now}  |  코인명 : {coin32}  |  현재가 = ￦{price32}  |  MACD = ￦{macd32}  |  보유수량 = {krw_balance32}  |  평가금액 = ￦{bp32}")
                            print(f"매수가능 : {op_mode32} - 불가")
                            print("")

                        else:
                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode32 = False

                            print(f"[ 32. {krw_coin32} 잔고부족으로 매수불가. ]")
                            print(f"현재시간 : {now}  |  코인명 : {coin32}")
                            print(f"매수가능 : {op_mode32} - 불가")
                            print("")

            elif macd32 < 0:       # macd가 0보다 낮을때는 매도
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
                        print(f"매도시간 : {now}  |  코인명 : {coin32}  |  현재가 = ￦{price32}  |  MACD = ￦{macd32}  |  보유수량 = {krw_balance32}  |  평가금액 = ￦{bp32}")
                        print(f"매수가능 : {op_mode32} - 가능")
                        print("")

                    else:   # 보유코인 평가 금액이 10,100원 이하일때
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode32 = True

                        print(f"[ 32. {krw_coin32} 보유코인이 없으므로 매도불가. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin32}")
                        print(f"매수가능 : {op_mode32} - 가능")
                        print("")

            # 1초 딜레이.
            time.sleep(1)
            ##### 32번 코인 매매 종료 #####
            #############################


            ###############################
            ##### 매매 : 33번코인 시작. #####

            ##### 코인보유현황
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
            #time.sleep(1)


            # 코인 현재가 불러오기
            price33 = pyupbit.get_current_price(krw_coin33)

            # MACD 조회.
            #macd33 = get_macd(krw_coin33)
            # 거래량 동반한 MACD 조회.
            macd33 = get_acc_macd(krw_coin33)
            # 20일 이평선 조회.
            #macd33 = get_ma20(krw_coin33)

            # 매수가능금액 불러오기
            krw33 = upbit.get_balance("KRW")

            # MACD 조건문
            if macd33 >= 0:     # macd가 0보다 높을때는 매수
                if op_mode33 == True:    # 매수 가능(True)일 경우 - 매수시도
                    if krw33 > buy_krw:      # 매수가능금액 krw33 가 매수평균가 buy_krw 보다 클때
                        if krw33 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                            if buy_krw > 10100:     # 매수평균가 buy_krw 가 10,100원 초과일 경우 : 매수
                                # 매수금액은 매수평균가 buy_krw 로
                                upbit.buy_market_order(krw_coin33, buy_krw * 0.99)   # 매수가능금액에서 1%를 빼고

                                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                                op_mode33 = False

                                # 1초 딜레이
                                #time.sleep(1)
                                # 보유수량 불러오기
                                krw_balance33 = upbit.get_balance(krw_coin33)
                                # 코인 현재가 불러오기
                                price33 = pyupbit.get_current_price(krw_coin33)
                                # 보유코인 원화금액으로 계산하기
                                bp33 = price33 * krw_balance33

                                # 보유 및 매수 가능 출력.
                                print(f"[ 33. {krw_coin33} 매수완료. ]")
                                print(f"매수시간 : {now}  |  코인명 : {coin33}  |  현재가 = ￦{price33}  |  MACD = ￦{macd33}  |  보유수량 = {krw_balance33}  |  평가금액 = ￦{bp33}")
                                print(f"매수가능 : {op_mode33} - 불가")
                                print("")

                            else:
                                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                                op_mode33 = False

                                print(f"[ 33. {krw_coin33} 잔고부족으로 매수불가. ]")
                                print(f"현재시간 : {now}  |  코인명 : {coin33}")
                                print(f"매수가능 : {op_mode33} - 불가")
                                print("")

                        else:
                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode33 = False

                            print(f"[ 33. {krw_coin33} 잔고부족으로 매수불가. ]")
                            print(f"현재시간 : {now}  |  코인명 : {coin33}")
                            print(f"매수가능 : {op_mode33} - 불가")
                            print("")

                    elif krw33 <= buy_krw:   # 매수가능금액 krw33 가 매수평균가 buy_krw 보다 같거나 작을때
                        if krw33 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                            # 매수금액은 매수가능금액인 krw33 로
                            upbit.buy_market_order(krw_coin33, krw33 * 0.99)   # 매수가능금액에서 1%를 빼고

                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode33 = False

                            # 1초 딜레이
                            #time.sleep(1)
                            # 보유수량 불러오기
                            krw_balance33 = upbit.get_balance(krw_coin33)
                            # 코인 현재가 불러오기
                            price33 = pyupbit.get_current_price(krw_coin33)
                            # 보유코인 원화금액으로 계산하기
                            bp33 = price33 * krw_balance33

                            # 보유 및 매수 가능 출력.
                            print(f"[ 33. {krw_coin33} 매수완료. ]")
                            print(f"매수시간 : {now}  |  코인명 : {coin33}  |  현재가 = ￦{price33}  |  MACD = ￦{macd33}  |  보유수량 = {krw_balance33}  |  평가금액 = ￦{bp33}")
                            print(f"매수가능 : {op_mode33} - 불가")
                            print("")

                        else:
                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode33 = False

                            print(f"[ 33. {krw_coin33} 잔고부족으로 매수불가. ]")
                            print(f"현재시간 : {now}  |  코인명 : {coin33}")
                            print(f"매수가능 : {op_mode33} - 불가")
                            print("")

            elif macd33 < 0:       # macd가 0보다 낮을때는 매도
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
                        print(f"매도시간 : {now}  |  코인명 : {coin33}  |  현재가 = ￦{price33}  |  MACD = ￦{macd33}  |  보유수량 = {krw_balance33}  |  평가금액 = ￦{bp33}")
                        print(f"매수가능 : {op_mode33} - 가능")
                        print("")

                    else:   # 보유코인 평가 금액이 10,100원 이하일때
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode33 = True

                        print(f"[ 33. {krw_coin33} 보유코인이 없으므로 매도불가. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin33}")
                        print(f"매수가능 : {op_mode33} - 가능")
                        print("")

            # 1초 딜레이.
            time.sleep(1)
            ##### 33번 코인 매매 종료 #####
            #############################


            ###############################
            ##### 매매 : 34번코인 시작. #####

            ##### 코인보유현황
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
            #time.sleep(1)


            # 코인 현재가 불러오기
            price34 = pyupbit.get_current_price(krw_coin34)

            # MACD 조회.
            #macd34 = get_macd(krw_coin34)
            # 거래량 동반한 MACD 조회.
            macd34 = get_acc_macd(krw_coin34)
            # 20일 이평선 조회.
            #macd34 = get_ma20(krw_coin34)

            # 매수가능금액 불러오기
            krw34 = upbit.get_balance("KRW")

            # MACD 조건문
            if macd34 >= 0:     # macd가 0보다 높을때는 매수
                if op_mode34 == True:    # 매수 가능(True)일 경우 - 매수시도
                    if krw34 > buy_krw:      # 매수가능금액 krw34 가 매수평균가 buy_krw 보다 클때
                        if krw34 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                            if buy_krw > 10100:     # 매수평균가 buy_krw 가 10,100원 초과일 경우 : 매수
                                # 매수금액은 매수평균가 buy_krw 로
                                upbit.buy_market_order(krw_coin34, buy_krw * 0.99)   # 매수가능금액에서 1%를 빼고

                                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                                op_mode34 = False

                                # 1초 딜레이
                                #time.sleep(1)
                                # 보유수량 불러오기
                                krw_balance34 = upbit.get_balance(krw_coin34)
                                # 코인 현재가 불러오기
                                price34 = pyupbit.get_current_price(krw_coin34)
                                # 보유코인 원화금액으로 계산하기
                                bp34 = price34 * krw_balance34

                                # 보유 및 매수 가능 출력.
                                print(f"[ 34. {krw_coin34} 매수완료. ]")
                                print(f"매수시간 : {now}  |  코인명 : {coin34}  |  현재가 = ￦{price34}  |  MACD = ￦{macd34}  |  보유수량 = {krw_balance34}  |  평가금액 = ￦{bp34}")
                                print(f"매수가능 : {op_mode34} - 불가")
                                print("")

                            else:
                                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                                op_mode34 = False

                                print(f"[ 34. {krw_coin34} 잔고부족으로 매수불가. ]")
                                print(f"현재시간 : {now}  |  코인명 : {coin34}")
                                print(f"매수가능 : {op_mode34} - 불가")
                                print("")

                        else:
                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode34 = False

                            print(f"[ 34. {krw_coin34} 잔고부족으로 매수불가. ]")
                            print(f"현재시간 : {now}  |  코인명 : {coin34}")
                            print(f"매수가능 : {op_mode34} - 불가")
                            print("")

                    elif krw34 <= buy_krw:   # 매수가능금액 krw34 가 매수평균가 buy_krw 보다 같거나 작을때
                        if krw34 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                            # 매수금액은 매수가능금액인 krw34 로
                            upbit.buy_market_order(krw_coin34, krw34 * 0.99)   # 매수가능금액에서 1%를 빼고

                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode34 = False

                            # 1초 딜레이
                            #time.sleep(1)
                            # 보유수량 불러오기
                            krw_balance34 = upbit.get_balance(krw_coin34)
                            # 코인 현재가 불러오기
                            price34 = pyupbit.get_current_price(krw_coin34)
                            # 보유코인 원화금액으로 계산하기
                            bp34 = price34 * krw_balance34

                            # 보유 및 매수 가능 출력.
                            print(f"[ 34. {krw_coin34} 매수완료. ]")
                            print(f"매수시간 : {now}  |  코인명 : {coin34}  |  현재가 = ￦{price34}  |  MACD = ￦{macd34}  |  보유수량 = {krw_balance34}  |  평가금액 = ￦{bp34}")
                            print(f"매수가능 : {op_mode34} - 불가")
                            print("")

                        else:
                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode34 = False

                            print(f"[ 34. {krw_coin34} 잔고부족으로 매수불가. ]")
                            print(f"현재시간 : {now}  |  코인명 : {coin34}")
                            print(f"매수가능 : {op_mode34} - 불가")
                            print("")

            elif macd34 < 0:       # macd가 0보다 낮을때는 매도
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
                        print(f"매도시간 : {now}  |  코인명 : {coin34}  |  현재가 = ￦{price34}  |  MACD = ￦{macd34}  |  보유수량 = {krw_balance34}  |  평가금액 = ￦{bp34}")
                        print(f"매수가능 : {op_mode34} - 가능")
                        print("")

                    else:   # 보유코인 평가 금액이 10,100원 이하일때
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode34 = True

                        print(f"[ 34. {krw_coin34} 보유코인이 없으므로 매도불가. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin34}")
                        print(f"매수가능 : {op_mode34} - 가능")
                        print("")

            # 1초 딜레이.
            time.sleep(1)
            ##### 34번 코인 매매 종료 #####
            #############################


            ###############################
            ##### 매매 : 35번코인 시작. #####

            ##### 코인보유현황
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
            #time.sleep(1)


            # 코인 현재가 불러오기
            price35 = pyupbit.get_current_price(krw_coin35)

            # MACD 조회.
            #macd35 = get_macd(krw_coin35)
            # 거래량 동반한 MACD 조회.
            macd35 = get_acc_macd(krw_coin35)
            # 20일 이평선 조회.
            #macd35 = get_ma20(krw_coin35)

            # 매수가능금액 불러오기
            krw35 = upbit.get_balance("KRW")

            # MACD 조건문
            if macd35 >= 0:     # macd가 0보다 높을때는 매수
                if op_mode35 == True:    # 매수 가능(True)일 경우 - 매수시도
                    if krw35 > buy_krw:      # 매수가능금액 krw35 가 매수평균가 buy_krw 보다 클때
                        if krw35 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                            if buy_krw > 10100:     # 매수평균가 buy_krw 가 10,100원 초과일 경우 : 매수
                                # 매수금액은 매수평균가 buy_krw 로
                                upbit.buy_market_order(krw_coin35, buy_krw * 0.99)   # 매수가능금액에서 1%를 빼고

                                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                                op_mode35 = False

                                # 1초 딜레이
                                #time.sleep(1)
                                # 보유수량 불러오기
                                krw_balance35 = upbit.get_balance(krw_coin35)
                                # 코인 현재가 불러오기
                                price35 = pyupbit.get_current_price(krw_coin35)
                                # 보유코인 원화금액으로 계산하기
                                bp35 = price35 * krw_balance35

                                # 보유 및 매수 가능 출력.
                                print(f"[ 35. {krw_coin35} 매수완료. ]")
                                print(f"매수시간 : {now}  |  코인명 : {coin35}  |  현재가 = ￦{price35}  |  MACD = ￦{macd35}  |  보유수량 = {krw_balance35}  |  평가금액 = ￦{bp35}")
                                print(f"매수가능 : {op_mode35} - 불가")
                                print("")

                            else:
                                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                                op_mode35 = False

                                print(f"[ 35. {krw_coin35} 잔고부족으로 매수불가. ]")
                                print(f"현재시간 : {now}  |  코인명 : {coin35}")
                                print(f"매수가능 : {op_mode35} - 불가")
                                print("")

                        else:
                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode35 = False

                            print(f"[ 35. {krw_coin35} 잔고부족으로 매수불가. ]")
                            print(f"현재시간 : {now}  |  코인명 : {coin35}")
                            print(f"매수가능 : {op_mode35} - 불가")
                            print("")

                    elif krw35 <= buy_krw:   # 매수가능금액 krw35 가 매수평균가 buy_krw 보다 같거나 작을때
                        if krw35 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                            # 매수금액은 매수가능금액인 krw35 로
                            upbit.buy_market_order(krw_coin35, krw35 * 0.99)   # 매수가능금액에서 1%를 빼고

                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode35 = False

                            # 1초 딜레이
                            #time.sleep(1)
                            # 보유수량 불러오기
                            krw_balance35 = upbit.get_balance(krw_coin35)
                            # 코인 현재가 불러오기
                            price35 = pyupbit.get_current_price(krw_coin35)
                            # 보유코인 원화금액으로 계산하기
                            bp35 = price35 * krw_balance35

                            # 보유 및 매수 가능 출력.
                            print(f"[ 35. {krw_coin35} 매수완료. ]")
                            print(f"매수시간 : {now}  |  코인명 : {coin35}  |  현재가 = ￦{price35}  |  MACD = ￦{macd35}  |  보유수량 = {krw_balance35}  |  평가금액 = ￦{bp35}")
                            print(f"매수가능 : {op_mode35} - 불가")
                            print("")

                        else:
                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode35 = False

                            print(f"[ 35. {krw_coin35} 잔고부족으로 매수불가. ]")
                            print(f"현재시간 : {now}  |  코인명 : {coin35}")
                            print(f"매수가능 : {op_mode35} - 불가")
                            print("")

            elif macd35 < 0:       # macd가 0보다 낮을때는 매도
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
                        print(f"매도시간 : {now}  |  코인명 : {coin35}  |  현재가 = ￦{price35}  |  MACD = ￦{macd35}  |  보유수량 = {krw_balance35}  |  평가금액 = ￦{bp35}")
                        print(f"매수가능 : {op_mode35} - 가능")
                        print("")

                    else:   # 보유코인 평가 금액이 10,100원 이하일때
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode35 = True

                        print(f"[ 35. {krw_coin35} 보유코인이 없으므로 매도불가. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin35}")
                        print(f"매수가능 : {op_mode35} - 가능")
                        print("")

            # 1초 딜레이.
            time.sleep(1)
            ##### 35번 코인 매매 종료 #####
            #############################


            ###############################
            ##### 매매 : 36번코인 시작. #####

            ##### 코인보유현황
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
            #time.sleep(1)


            # 코인 현재가 불러오기
            price36 = pyupbit.get_current_price(krw_coin36)

            # MACD 조회.
            #macd36 = get_macd(krw_coin36)
            # 거래량 동반한 MACD 조회.
            macd36 = get_acc_macd(krw_coin36)
            # 20일 이평선 조회.
            #macd36 = get_ma20(krw_coin36)

            # 매수가능금액 불러오기
            krw36 = upbit.get_balance("KRW")

            # MACD 조건문
            if macd36 >= 0:     # macd가 0보다 높을때는 매수
                if op_mode36 == True:    # 매수 가능(True)일 경우 - 매수시도
                    if krw36 > buy_krw:      # 매수가능금액 krw36 가 매수평균가 buy_krw 보다 클때
                        if krw36 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                            if buy_krw > 10100:     # 매수평균가 buy_krw 가 10,100원 초과일 경우 : 매수
                                # 매수금액은 매수평균가 buy_krw 로
                                upbit.buy_market_order(krw_coin36, buy_krw * 0.99)   # 매수가능금액에서 1%를 빼고

                                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                                op_mode36 = False

                                # 1초 딜레이
                                #time.sleep(1)
                                # 보유수량 불러오기
                                krw_balance36 = upbit.get_balance(krw_coin36)
                                # 코인 현재가 불러오기
                                price36 = pyupbit.get_current_price(krw_coin36)
                                # 보유코인 원화금액으로 계산하기
                                bp36 = price36 * krw_balance36

                                # 보유 및 매수 가능 출력.
                                print(f"[ 36. {krw_coin36} 매수완료. ]")
                                print(f"매수시간 : {now}  |  코인명 : {coin36}  |  현재가 = ￦{price36}  |  MACD = ￦{macd36}  |  보유수량 = {krw_balance36}  |  평가금액 = ￦{bp36}")
                                print(f"매수가능 : {op_mode36} - 불가")
                                print("")

                            else:
                                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                                op_mode36 = False

                                print(f"[ 36. {krw_coin36} 잔고부족으로 매수불가. ]")
                                print(f"현재시간 : {now}  |  코인명 : {coin36}")
                                print(f"매수가능 : {op_mode36} - 불가")
                                print("")

                        else:
                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode36 = False

                            print(f"[ 36. {krw_coin36} 잔고부족으로 매수불가. ]")
                            print(f"현재시간 : {now}  |  코인명 : {coin36}")
                            print(f"매수가능 : {op_mode36} - 불가")
                            print("")

                    elif krw36 <= buy_krw:   # 매수가능금액 krw36 가 매수평균가 buy_krw 보다 같거나 작을때
                        if krw36 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                            # 매수금액은 매수가능금액인 krw36 로
                            upbit.buy_market_order(krw_coin36, krw36 * 0.99)   # 매수가능금액에서 1%를 빼고

                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode36 = False

                            # 1초 딜레이
                            #time.sleep(1)
                            # 보유수량 불러오기
                            krw_balance36 = upbit.get_balance(krw_coin36)
                            # 코인 현재가 불러오기
                            price36 = pyupbit.get_current_price(krw_coin36)
                            # 보유코인 원화금액으로 계산하기
                            bp36 = price36 * krw_balance36

                            # 보유 및 매수 가능 출력.
                            print(f"[ 36. {krw_coin36} 매수완료. ]")
                            print(f"매수시간 : {now}  |  코인명 : {coin36}  |  현재가 = ￦{price36}  |  MACD = ￦{macd36}  |  보유수량 = {krw_balance36}  |  평가금액 = ￦{bp36}")
                            print(f"매수가능 : {op_mode36} - 불가")
                            print("")

                        else:
                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode36 = False

                            print(f"[ 36. {krw_coin36} 잔고부족으로 매수불가. ]")
                            print(f"현재시간 : {now}  |  코인명 : {coin36}")
                            print(f"매수가능 : {op_mode36} - 불가")
                            print("")

            elif macd36 < 0:       # macd가 0보다 낮을때는 매도
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
                        print(f"매도시간 : {now}  |  코인명 : {coin36}  |  현재가 = ￦{price36}  |  MACD = ￦{macd36}  |  보유수량 = {krw_balance36}  |  평가금액 = ￦{bp36}")
                        print(f"매수가능 : {op_mode36} - 가능")
                        print("")

                    else:   # 보유코인 평가 금액이 10,100원 이하일때
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode36 = True

                        print(f"[ 36. {krw_coin36} 보유코인이 없으므로 매도불가. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin36}")
                        print(f"매수가능 : {op_mode36} - 가능")
                        print("")

            # 1초 딜레이.
            time.sleep(1)
            ##### 36번 코인 매매 종료 #####
            #############################


            ###############################
            ##### 매매 : 37번코인 시작. #####

            ##### 코인보유현황
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
            #time.sleep(1)


            # 코인 현재가 불러오기
            price37 = pyupbit.get_current_price(krw_coin37)

            # MACD 조회.
            #macd37 = get_macd(krw_coin37)
            # 거래량 동반한 MACD 조회.
            macd37 = get_acc_macd(krw_coin37)
            # 20일 이평선 조회.
            #macd37 = get_ma20(krw_coin37)

            # 매수가능금액 불러오기
            krw37 = upbit.get_balance("KRW")

            # MACD 조건문
            if macd37 >= 0:     # macd가 0보다 높을때는 매수
                if op_mode37 == True:    # 매수 가능(True)일 경우 - 매수시도
                    if krw37 > buy_krw:      # 매수가능금액 krw37 가 매수평균가 buy_krw 보다 클때
                        if krw37 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                            if buy_krw > 10100:     # 매수평균가 buy_krw 가 10,100원 초과일 경우 : 매수
                                # 매수금액은 매수평균가 buy_krw 로
                                upbit.buy_market_order(krw_coin37, buy_krw * 0.99)   # 매수가능금액에서 1%를 빼고

                                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                                op_mode37 = False

                                # 1초 딜레이
                                #time.sleep(1)
                                # 보유수량 불러오기
                                krw_balance37 = upbit.get_balance(krw_coin37)
                                # 코인 현재가 불러오기
                                price37 = pyupbit.get_current_price(krw_coin37)
                                # 보유코인 원화금액으로 계산하기
                                bp37 = price37 * krw_balance37

                                # 보유 및 매수 가능 출력.
                                print(f"[ 37. {krw_coin37} 매수완료. ]")
                                print(f"매수시간 : {now}  |  코인명 : {coin37}  |  현재가 = ￦{price37}  |  MACD = ￦{macd37}  |  보유수량 = {krw_balance37}  |  평가금액 = ￦{bp37}")
                                print(f"매수가능 : {op_mode37} - 불가")
                                print("")

                            else:
                                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                                op_mode37 = False

                                print(f"[ 37. {krw_coin37} 잔고부족으로 매수불가. ]")
                                print(f"현재시간 : {now}  |  코인명 : {coin37}")
                                print(f"매수가능 : {op_mode37} - 불가")
                                print("")

                        else:
                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode37 = False

                            print(f"[ 37. {krw_coin37} 잔고부족으로 매수불가. ]")
                            print(f"현재시간 : {now}  |  코인명 : {coin37}")
                            print(f"매수가능 : {op_mode37} - 불가")
                            print("")

                    elif krw37 <= buy_krw:   # 매수가능금액 krw37 가 매수평균가 buy_krw 보다 같거나 작을때
                        if krw37 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                            # 매수금액은 매수가능금액인 krw37 로
                            upbit.buy_market_order(krw_coin37, krw37 * 0.99)   # 매수가능금액에서 1%를 빼고

                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode37 = False

                            # 1초 딜레이
                            #time.sleep(1)
                            # 보유수량 불러오기
                            krw_balance37 = upbit.get_balance(krw_coin37)
                            # 코인 현재가 불러오기
                            price37 = pyupbit.get_current_price(krw_coin37)
                            # 보유코인 원화금액으로 계산하기
                            bp37 = price37 * krw_balance37

                            # 보유 및 매수 가능 출력.
                            print(f"[ 37. {krw_coin37} 매수완료. ]")
                            print(f"매수시간 : {now}  |  코인명 : {coin37}  |  현재가 = ￦{price37}  |  MACD = ￦{macd37}  |  보유수량 = {krw_balance37}  |  평가금액 = ￦{bp37}")
                            print(f"매수가능 : {op_mode37} - 불가")
                            print("")

                        else:
                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode37 = False

                            print(f"[ 37. {krw_coin37} 잔고부족으로 매수불가. ]")
                            print(f"현재시간 : {now}  |  코인명 : {coin37}")
                            print(f"매수가능 : {op_mode37} - 불가")
                            print("")

            elif macd37 < 0:       # macd가 0보다 낮을때는 매도
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
                        print(f"매도시간 : {now}  |  코인명 : {coin37}  |  현재가 = ￦{price37}  |  MACD = ￦{macd37}  |  보유수량 = {krw_balance37}  |  평가금액 = ￦{bp37}")
                        print(f"매수가능 : {op_mode37} - 가능")
                        print("")

                    else:   # 보유코인 평가 금액이 10,100원 이하일때
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode37 = True

                        print(f"[ 37. {krw_coin37} 보유코인이 없으므로 매도불가. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin37}")
                        print(f"매수가능 : {op_mode37} - 가능")
                        print("")

            # 1초 딜레이.
            time.sleep(1)
            ##### 37번 코인 매매 종료 #####
            #############################


            ###############################
            ##### 매매 : 38번코인 시작. #####

            ##### 코인보유현황
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
            #time.sleep(1)


            # 코인 현재가 불러오기
            price38 = pyupbit.get_current_price(krw_coin38)

            # MACD 조회.
            #macd38 = get_macd(krw_coin38)
            # 거래량 동반한 MACD 조회.
            macd38 = get_acc_macd(krw_coin38)
            # 20일 이평선 조회.
            #macd38 = get_ma20(krw_coin38)

            # 매수가능금액 불러오기
            krw38 = upbit.get_balance("KRW")

            # MACD 조건문
            if macd38 >= 0:     # macd가 0보다 높을때는 매수
                if op_mode38 == True:    # 매수 가능(True)일 경우 - 매수시도
                    if krw38 > buy_krw:      # 매수가능금액 krw38 가 매수평균가 buy_krw 보다 클때
                        if krw38 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                            if buy_krw > 10100:     # 매수평균가 buy_krw 가 10,100원 초과일 경우 : 매수
                                # 매수금액은 매수평균가 buy_krw 로
                                upbit.buy_market_order(krw_coin38, buy_krw * 0.99)   # 매수가능금액에서 1%를 빼고

                                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                                op_mode38 = False

                                # 1초 딜레이
                                #time.sleep(1)
                                # 보유수량 불러오기
                                krw_balance38 = upbit.get_balance(krw_coin38)
                                # 코인 현재가 불러오기
                                price38 = pyupbit.get_current_price(krw_coin38)
                                # 보유코인 원화금액으로 계산하기
                                bp38 = price38 * krw_balance38

                                # 보유 및 매수 가능 출력.
                                print(f"[ 38. {krw_coin38} 매수완료. ]")
                                print(f"매수시간 : {now}  |  코인명 : {coin38}  |  현재가 = ￦{price38}  |  MACD = ￦{macd38}  |  보유수량 = {krw_balance38}  |  평가금액 = ￦{bp38}")
                                print(f"매수가능 : {op_mode38} - 불가")
                                print("")

                            else:
                                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                                op_mode38 = False

                                print(f"[ 38. {krw_coin38} 잔고부족으로 매수불가. ]")
                                print(f"현재시간 : {now}  |  코인명 : {coin38}")
                                print(f"매수가능 : {op_mode38} - 불가")
                                print("")

                        else:
                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode38 = False

                            print(f"[ 38. {krw_coin38} 잔고부족으로 매수불가. ]")
                            print(f"현재시간 : {now}  |  코인명 : {coin38}")
                            print(f"매수가능 : {op_mode38} - 불가")
                            print("")

                    elif krw38 <= buy_krw:   # 매수가능금액 krw38 가 매수평균가 buy_krw 보다 같거나 작을때
                        if krw38 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                            # 매수금액은 매수가능금액인 krw38 로
                            upbit.buy_market_order(krw_coin38, krw38 * 0.99)   # 매수가능금액에서 1%를 빼고

                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode38 = False

                            # 1초 딜레이
                            #time.sleep(1)
                            # 보유수량 불러오기
                            krw_balance38 = upbit.get_balance(krw_coin38)
                            # 코인 현재가 불러오기
                            price38 = pyupbit.get_current_price(krw_coin38)
                            # 보유코인 원화금액으로 계산하기
                            bp38 = price38 * krw_balance38

                            # 보유 및 매수 가능 출력.
                            print(f"[ 28. {krw_coin38} 매수완료. ]")
                            print(f"매수시간 : {now}  |  코인명 : {coin38}  |  현재가 = ￦{price38}  |  MACD = ￦{macd38}  |  보유수량 = {krw_balance38}  |  평가금액 = ￦{bp38}")
                            print(f"매수가능 : {op_mode38} - 불가")
                            print("")

                        else:
                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode38 = False

                            print(f"[ 38. {krw_coin38} 잔고부족으로 매수불가. ]")
                            print(f"현재시간 : {now}  |  코인명 : {coin38}")
                            print(f"매수가능 : {op_mode38} - 불가")
                            print("")

            elif macd38 < 0:       # macd가 0보다 낮을때는 매도
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
                        print(f"매도시간 : {now}  |  코인명 : {coin38}  |  현재가 = ￦{price38}  |  MACD = ￦{macd38}  |  보유수량 = {krw_balance38}  |  평가금액 = ￦{bp38}")
                        print(f"매수가능 : {op_mode38} - 가능")
                        print("")

                    else:   # 보유코인 평가 금액이 10,100원 이하일때
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode38 = True

                        print(f"[ 38. {krw_coin38} 보유코인이 없으므로 매도불가. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin38}")
                        print(f"매수가능 : {op_mode38} - 가능")
                        print("")

            # 1초 딜레이.
            time.sleep(1)
            ##### 38번 코인 매매 종료 #####
            #############################


            ###############################
            ##### 매매 : 39번코인 시작. #####

            ##### 코인보유현황
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
            #time.sleep(1)


            # 코인 현재가 불러오기
            price39 = pyupbit.get_current_price(krw_coin39)

            # MACD 조회.
            #macd39 = get_macd(krw_coin39)
            # 거래량 동반한 MACD 조회.
            macd39 = get_acc_macd(krw_coin39)
            # 20일 이평선 조회.
            #macd39 = get_ma20(krw_coin39)

            # 매수가능금액 불러오기
            krw39 = upbit.get_balance("KRW")

            # MACD 조건문
            if macd39 >= 0:     # macd가 0보다 높을때는 매수
                if op_mode39 == True:    # 매수 가능(True)일 경우 - 매수시도
                    if krw39 > buy_krw:      # 매수가능금액 krw39 가 매수평균가 buy_krw 보다 클때
                        if krw39 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                            if buy_krw > 10100:     # 매수평균가 buy_krw 가 10,100원 초과일 경우 : 매수
                                # 매수금액은 매수평균가 buy_krw 로
                                upbit.buy_market_order(krw_coin39, buy_krw * 0.99)   # 매수가능금액에서 1%를 빼고

                                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                                op_mode39 = False

                                # 1초 딜레이
                                #time.sleep(1)
                                # 보유수량 불러오기
                                krw_balance39 = upbit.get_balance(krw_coin39)
                                # 코인 현재가 불러오기
                                price39 = pyupbit.get_current_price(krw_coin39)
                                # 보유코인 원화금액으로 계산하기
                                bp39 = price39 * krw_balance39

                                # 보유 및 매수 가능 출력.
                                print(f"[ 39. {krw_coin39} 매수완료. ]")
                                print(f"매수시간 : {now}  |  코인명 : {coin39}  |  현재가 = ￦{price39}  |  MACD = ￦{macd39}  |  보유수량 = {krw_balance39}  |  평가금액 = ￦{bp39}")
                                print(f"매수가능 : {op_mode39} - 불가")
                                print("")

                            else:
                                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                                op_mode39 = False

                                print(f"[ 39. {krw_coin39} 잔고부족으로 매수불가. ]")
                                print(f"현재시간 : {now}  |  코인명 : {coin39}")
                                print(f"매수가능 : {op_mode39} - 불가")
                                print("")

                        else:
                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode39 = False

                            print(f"[ 39. {krw_coin39} 잔고부족으로 매수불가. ]")
                            print(f"현재시간 : {now}  |  코인명 : {coin39}")
                            print(f"매수가능 : {op_mode39} - 불가")
                            print("")

                    elif krw39 <= buy_krw:   # 매수가능금액 krw39 가 매수평균가 buy_krw 보다 같거나 작을때
                        if krw39 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                            # 매수금액은 매수가능금액인 krw39 로
                            upbit.buy_market_order(krw_coin39, krw39 * 0.99)   # 매수가능금액에서 1%를 빼고

                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode39 = False

                            # 1초 딜레이
                            #time.sleep(1)
                            # 보유수량 불러오기
                            krw_balance39 = upbit.get_balance(krw_coin39)
                            # 코인 현재가 불러오기
                            price39 = pyupbit.get_current_price(krw_coin39)
                            # 보유코인 원화금액으로 계산하기
                            bp39 = price39 * krw_balance39

                            # 보유 및 매수 가능 출력.
                            print(f"[ 39. {krw_coin39} 매수완료. ]")
                            print(f"매수시간 : {now}  |  코인명 : {coin39}  |  현재가 = ￦{price39}  |  MACD = ￦{macd39}  |  보유수량 = {krw_balance39}  |  평가금액 = ￦{bp39}")
                            print(f"매수가능 : {op_mode39} - 불가")
                            print("")

                        else:
                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode39 = False

                            print(f"[ 39. {krw_coin39} 잔고부족으로 매수불가. ]")
                            print(f"현재시간 : {now}  |  코인명 : {coin39}")
                            print(f"매수가능 : {op_mode39} - 불가")
                            print("")

            elif macd39 < 0:       # macd가 0보다 낮을때는 매도
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
                        print(f"매도시간 : {now}  |  코인명 : {coin39}  |  현재가 = ￦{price39}  |  MACD = ￦{macd39}  |  보유수량 = {krw_balance39}  |  평가금액 = ￦{bp39}")
                        print(f"매수가능 : {op_mode39} - 가능")
                        print("")

                    else:   # 보유코인 평가 금액이 10,100원 이하일때
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode39 = True

                        print(f"[ 39. {krw_coin39} 보유코인이 없으므로 매도불가. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin39}")
                        print(f"매수가능 : {op_mode39} - 가능")
                        print("")

            # 1초 딜레이.
            time.sleep(1)
            ##### 39번 코인 매매 종료 #####
            #############################


            ###############################
            ##### 매매 : 40번코인 시작. #####

            ##### 코인보유현황
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
            #time.sleep(1)


            # 코인 현재가 불러오기
            price40 = pyupbit.get_current_price(krw_coin40)

            # MACD 조회.
            #macd40 = get_macd(krw_coin40)
            # 거래량 동반한 MACD 조회.
            macd40 = get_acc_macd(krw_coin40)
            # 20일 이평선 조회.
            #macd40 = get_ma20(krw_coin40)

            # 매수가능금액 불러오기
            krw40 = upbit.get_balance("KRW")

            # MACD 조건문
            if macd40 >= 0:     # macd가 0보다 높을때는 매수
                if op_mode40 == True:    # 매수 가능(True)일 경우 - 매수시도
                    if krw40 > buy_krw:      # 매수가능금액 krw40 가 매수평균가 buy_krw 보다 클때
                        if krw40 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                            if buy_krw > 10100:     # 매수평균가 buy_krw 가 10,100원 초과일 경우 : 매수
                                # 매수금액은 매수평균가 buy_krw 로
                                upbit.buy_market_order(krw_coin40, buy_krw * 0.99)   # 매수가능금액에서 1%를 빼고

                                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                                op_mode40 = False

                                # 1초 딜레이
                                #time.sleep(1)
                                # 보유수량 불러오기
                                krw_balance40 = upbit.get_balance(krw_coin40)
                                # 코인 현재가 불러오기
                                price40 = pyupbit.get_current_price(krw_coin40)
                                # 보유코인 원화금액으로 계산하기
                                bp40 = price40 * krw_balance40

                                # 보유 및 매수 가능 출력.
                                print(f"[ 40. {krw_coin40} 매수완료. ]")
                                print(f"매수시간 : {now}  |  코인명 : {coin40}  |  현재가 = ￦{price40}  |  MACD = ￦{macd40}  |  보유수량 = {krw_balance40}  |  평가금액 = ￦{bp40}")
                                print(f"매수가능 : {op_mode40} - 불가")
                                print("")

                            else:
                                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                                op_mode40 = False

                                print(f"[ 40. {krw_coin40} 잔고부족으로 매수불가. ]")
                                print(f"현재시간 : {now}  |  코인명 : {coin40}")
                                print(f"매수가능 : {op_mode40} - 불가")
                                print("")

                        else:
                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode40 = False

                            print(f"[ 40. {krw_coin40} 잔고부족으로 매수불가. ]")
                            print(f"현재시간 : {now}  |  코인명 : {coin40}")
                            print(f"매수가능 : {op_mode40} - 불가")
                            print("")

                    elif krw40 <= buy_krw:   # 매수가능금액 krw40 가 매수평균가 buy_krw 보다 같거나 작을때
                        if krw40 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                            # 매수금액은 매수가능금액인 krw40 로
                            upbit.buy_market_order(krw_coin40, krw40 * 0.99)   # 매수가능금액에서 1%를 빼고

                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode40 = False

                            # 1초 딜레이
                            #time.sleep(1)
                            # 보유수량 불러오기
                            krw_balance40 = upbit.get_balance(krw_coin40)
                            # 코인 현재가 불러오기
                            price40 = pyupbit.get_current_price(krw_coin40)
                            # 보유코인 원화금액으로 계산하기
                            bp40 = price40 * krw_balance40

                            # 보유 및 매수 가능 출력.
                            print(f"[ 40. {krw_coin40} 매수완료. ]")
                            print(f"매수시간 : {now}  |  코인명 : {coin40}  |  현재가 = ￦{price40}  |  MACD = ￦{macd40}  |  보유수량 = {krw_balance40}  |  평가금액 = ￦{bp40}")
                            print(f"매수가능 : {op_mode40} - 불가")
                            print("")

                        else:
                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode40 = False

                            print(f"[ 40. {krw_coin40} 잔고부족으로 매수불가. ]")
                            print(f"현재시간 : {now}  |  코인명 : {coin40}")
                            print(f"매수가능 : {op_mode40} - 불가")
                            print("")

            elif macd40 < 0:       # macd가 0보다 낮을때는 매도
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
                        print(f"매도시간 : {now}  |  코인명 : {coin40}  |  현재가 = ￦{price40}  |  MACD = ￦{macd40}  |  보유수량 = {krw_balance40}  |  평가금액 = ￦{bp40}")
                        print(f"매수가능 : {op_mode40} - 가능")
                        print("")

                    else:   # 보유코인 평가 금액이 10,100원 이하일때
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode40 = True

                        print(f"[ 40. {krw_coin40} 보유코인이 없으므로 매도불가. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin40}")
                        print(f"매수가능 : {op_mode40} - 가능")
                        print("")

            # 1초 딜레이.
            time.sleep(1)
            ##### 40번 코인 매매 종료 #####
            #############################


            ######################################################################################################################################################
            ######################################################################################################################################################
            ######################################################################################################################################################
            ######################################################################################################################################################
            ######################################################################################################################################################


            ###############################
            ##### 매매 : 41번코인 시작. #####

            ##### 코인보유현황
            # 보유수량 불러오기
            krw_balance41 = upbit.get_balance(krw_coin41)
            # 코인 현재가 불러오기
            price41 = pyupbit.get_current_price(krw_coin41)
            # 보유코인 원화금액으로 계산하기
            bp41 = price41 * krw_balance41
            # 코인 현황 출력.
            print(f"41. 코인명 : {coin41}  |  현재가 = ￦{price41}  |  보유수량 = {krw_balance41}  |  평가금액 = ￦{bp41}")
            # 코인 보유 유무
            if bp41 > 10100:
                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                op_mode41 = False

                # 보유 및 매수 가능 출력.
                print(f" 코인 보유 : 보유중  |  매수가능 - {op_mode41} - 매수불가")
                print("")
            else:
                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                op_mode41 = True

                # 보유 및 매수 가능 출력.
                print(f" 코인 보유 : 없음  |  매수가능 - {op_mode41} - 매수가능")
                print("")
            #time.sleep(1)


            # 코인 현재가 불러오기
            price41 = pyupbit.get_current_price(krw_coin41)

            # MACD 조회.
            #macd41 = get_macd(krw_coin41)
            # 거래량 동반한 MACD 조회.
            macd41 = get_acc_macd(krw_coin41)
            # 20일 이평선 조회.
            #macd41 = get_ma20(krw_coin41)

            # 매수가능금액 불러오기
            krw41 = upbit.get_balance("KRW")

            # MACD 조건문
            if macd41 >= 0:     # macd가 0보다 높을때는 매수
                if op_mode41 == True:    # 매수 가능(True)일 경우 - 매수시도
                    if krw41 > buy_krw:      # 매수가능금액 krw41 가 매수평균가 buy_krw 보다 클때
                        if krw41 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                            if buy_krw > 10100:     # 매수평균가 buy_krw 가 10,100원 초과일 경우 : 매수
                                # 매수금액은 매수평균가 buy_krw 로
                                upbit.buy_market_order(krw_coin41, buy_krw * 0.99)   # 매수가능금액에서 1%를 빼고

                                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                                op_mode41 = False

                                # 1초 딜레이
                                #time.sleep(1)
                                # 보유수량 불러오기
                                krw_balance41 = upbit.get_balance(krw_coin41)
                                # 코인 현재가 불러오기
                                price41 = pyupbit.get_current_price(krw_coin41)
                                # 보유코인 원화금액으로 계산하기
                                bp41 = price41 * krw_balance41

                                # 보유 및 매수 가능 출력.
                                print(f"[ 41. {krw_coin41} 매수완료. ]")
                                print(f"매수시간 : {now}  |  코인명 : {coin41}  |  현재가 = ￦{price41}  |  MACD = ￦{macd41}  |  보유수량 = {krw_balance41}  |  평가금액 = ￦{bp41}")
                                print(f"매수가능 : {op_mode41} - 불가")
                                print("")

                            else:
                                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                                op_mode41 = False

                                print(f"[ 41. {krw_coin41} 잔고부족으로 매수불가. ]")
                                print(f"현재시간 : {now}  |  코인명 : {coin41}")
                                print(f"매수가능 : {op_mode41} - 불가")
                                print("")

                        else:
                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode41 = False

                            print(f"[ 41. {krw_coin41} 잔고부족으로 매수불가. ]")
                            print(f"현재시간 : {now}  |  코인명 : {coin41}")
                            print(f"매수가능 : {op_mode41} - 불가")
                            print("")

                    elif krw41 <= buy_krw:   # 매수가능금액 krw41 가 매수평균가 buy_krw 보다 같거나 작을때
                        if krw41 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                            # 매수금액은 매수가능금액인 krw41 로
                            upbit.buy_market_order(krw_coin41, krw41 * 0.99)   # 매수가능금액에서 1%를 빼고

                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode41 = False

                            # 1초 딜레이
                            #time.sleep(1)
                            # 보유수량 불러오기
                            krw_balance41 = upbit.get_balance(krw_coin41)
                            # 코인 현재가 불러오기
                            price41 = pyupbit.get_current_price(krw_coin41)
                            # 보유코인 원화금액으로 계산하기
                            bp41 = price41 * krw_balance41

                            # 보유 및 매수 가능 출력.
                            print(f"[ 41. {krw_coin41} 매수완료. ]")
                            print(f"매수시간 : {now}  |  코인명 : {coin41}  |  현재가 = ￦{price41}  |  MACD = ￦{macd41}  |  보유수량 = {krw_balance41}  |  평가금액 = ￦{bp41}")
                            print(f"매수가능 : {op_mode41} - 불가")
                            print("")

                        else:
                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode41 = False

                            print(f"[ 41. {krw_coin41} 잔고부족으로 매수불가. ]")
                            print(f"현재시간 : {now}  |  코인명 : {coin41}")
                            print(f"매수가능 : {op_mode41} - 불가")
                            print("")

            elif macd41 < 0:       # macd가 0보다 낮을때는 매도
                if op_mode41 == False:   # 매수 불가(False)일 경우 - 매도시도
                    # 보유수량 불러오기
                    krw_balance41 = upbit.get_balance(krw_coin41)
                    # 현재가 불러오기
                    price41 = pyupbit.get_current_price(krw_coin41)
                    # 보유코인 원화금액으로 계산하기
                    bp41 = price41 * krw_balance41

                    # 보유코인 원화금액 매도시도
                    if  bp41 > 10100:   # 보유코인 평가 금액이 10,100원 초과일때 - 매도시도
                        # 매도할 코인명 - krw_coin41, 매도할 코인수량 - krw_balance41
                        upbit.sell_market_order(krw_coin41, krw_balance41)

                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode41 = True

                        # 1초 딜레이
                        #time.sleep(1)
                        # 보유수량 불러오기
                        krw_balance41 = upbit.get_balance(krw_coin41)
                        # 코인 현재가 불러오기
                        price41 = pyupbit.get_current_price(krw_coin41)
                        # 보유코인 원화금액으로 계산하기
                        bp41 = price41 * krw_balance41

                        # 보유 및 매수 가능 출력.
                        print(f"[ 41. {krw_coin41} 매도완료. ]")
                        print(f"매도시간 : {now}  |  코인명 : {coin41}  |  현재가 = ￦{price41}  |  MACD = ￦{macd41}  |  보유수량 = {krw_balance41}  |  평가금액 = ￦{bp41}")
                        print(f"매수가능 : {op_mode41} - 가능")
                        print("")

                    else:   # 보유코인 평가 금액이 10,100원 이하일때
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode41 = True

                        print(f"[ 41. {krw_coin41} 보유코인이 없으므로 매도불가. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin41}")
                        print(f"매수가능 : {op_mode41} - 가능")
                        print("")

            # 1초 딜레이.
            time.sleep(1)
            ##### 41번 코인 매매 종료 #####
            #############################


            ###############################
            ##### 매매 : 42번코인 시작. #####

            ##### 코인보유현황
            # 보유수량 불러오기
            krw_balance42 = upbit.get_balance(krw_coin42)
            # 코인 현재가 불러오기
            price42 = pyupbit.get_current_price(krw_coin42)
            # 보유코인 원화금액으로 계산하기
            bp42 = price42 * krw_balance42
            # 코인 현황 출력.
            print(f"42. 코인명 : {coin42}  |  현재가 = ￦{price42}  |  보유수량 = {krw_balance42}  |  평가금액 = ￦{bp42}")
            # 코인 보유 유무
            if bp42 > 10100:
                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                op_mode42 = False

                # 보유 및 매수 가능 출력.
                print(f" 코인 보유 : 보유중  |  매수가능 - {op_mode42} - 매수불가")
                print("")
            else:
                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                op_mode42 = True

                # 보유 및 매수 가능 출력.
                print(f" 코인 보유 : 없음  |  매수가능 - {op_mode42} - 매수가능")
                print("")
            #time.sleep(1)


            # 코인 현재가 불러오기
            price42 = pyupbit.get_current_price(krw_coin42)

            # MACD 조회.
            #macd42 = get_macd(krw_coin42)
            # 거래량 동반한 MACD 조회.
            macd42 = get_acc_macd(krw_coin42)
            # 20일 이평선 조회.
            #macd42 = get_ma20(krw_coin42)

            # 매수가능금액 불러오기
            krw42 = upbit.get_balance("KRW")

            # MACD 조건문
            if macd42 >= 0:     # macd가 0보다 높을때는 매수
                if op_mode42 == True:    # 매수 가능(True)일 경우 - 매수시도
                    if krw42 > buy_krw:      # 매수가능금액 krw42 가 매수평균가 buy_krw 보다 클때
                        if krw42 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                            if buy_krw > 10100:     # 매수평균가 buy_krw 가 10,100원 초과일 경우 : 매수
                                # 매수금액은 매수평균가 buy_krw 로
                                upbit.buy_market_order(krw_coin42, buy_krw * 0.99)   # 매수가능금액에서 1%를 빼고

                                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                                op_mode42 = False

                                # 1초 딜레이
                                #time.sleep(1)
                                # 보유수량 불러오기
                                krw_balance42 = upbit.get_balance(krw_coin42)
                                # 코인 현재가 불러오기
                                price42 = pyupbit.get_current_price(krw_coin42)
                                # 보유코인 원화금액으로 계산하기
                                bp42 = price42 * krw_balance42

                                # 보유 및 매수 가능 출력.
                                print(f"[ 42. {krw_coin42} 매수완료. ]")
                                print(f"매수시간 : {now}  |  코인명 : {coin42}  |  현재가 = ￦{price42}  |  MACD = ￦{macd42}  |  보유수량 = {krw_balance42}  |  평가금액 = ￦{bp42}")
                                print(f"매수가능 : {op_mode42} - 불가")
                                print("")

                            else:
                                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                                op_mode42 = False

                                print(f"[ 42. {krw_coin42} 잔고부족으로 매수불가. ]")
                                print(f"현재시간 : {now}  |  코인명 : {coin42}")
                                print(f"매수가능 : {op_mode42} - 불가")
                                print("")

                        else:
                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode42 = False

                            print(f"[ 42. {krw_coin42} 잔고부족으로 매수불가. ]")
                            print(f"현재시간 : {now}  |  코인명 : {coin42}")
                            print(f"매수가능 : {op_mode42} - 불가")
                            print("")

                    elif krw42 <= buy_krw:   # 매수가능금액 krw42 가 매수평균가 buy_krw 보다 같거나 작을때
                        if krw42 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                            # 매수금액은 매수가능금액인 krw42 로
                            upbit.buy_market_order(krw_coin42, krw42 * 0.99)   # 매수가능금액에서 1%를 빼고

                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode42 = False

                            # 1초 딜레이
                            #time.sleep(1)
                            # 보유수량 불러오기
                            krw_balance42 = upbit.get_balance(krw_coin42)
                            # 코인 현재가 불러오기
                            price42 = pyupbit.get_current_price(krw_coin42)
                            # 보유코인 원화금액으로 계산하기
                            bp42 = price42 * krw_balance42

                            # 보유 및 매수 가능 출력.
                            print(f"[ 42. {krw_coin42} 매수완료. ]")
                            print(f"매수시간 : {now}  |  코인명 : {coin42}  |  현재가 = ￦{price42}  |  MACD = ￦{macd42}  |  보유수량 = {krw_balance42}  |  평가금액 = ￦{bp42}")
                            print(f"매수가능 : {op_mode42} - 불가")
                            print("")

                        else:
                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode42 = False

                            print(f"[ 42. {krw_coin42} 잔고부족으로 매수불가. ]")
                            print(f"현재시간 : {now}  |  코인명 : {coin42}")
                            print(f"매수가능 : {op_mode42} - 불가")
                            print("")

            elif macd42 < 0:       # macd가 0보다 낮을때는 매도
                if op_mode42 == False:   # 매수 불가(False)일 경우 - 매도시도
                    # 보유수량 불러오기
                    krw_balance42 = upbit.get_balance(krw_coin42)
                    # 현재가 불러오기
                    price42 = pyupbit.get_current_price(krw_coin42)
                    # 보유코인 원화금액으로 계산하기
                    bp42 = price42 * krw_balance42

                    # 보유코인 원화금액 매도시도
                    if  bp42 > 10100:   # 보유코인 평가 금액이 10,100원 초과일때 - 매도시도
                        # 매도할 코인명 - krw_coin42, 매도할 코인수량 - krw_balance42
                        upbit.sell_market_order(krw_coin42, krw_balance42)

                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode42 = True

                        # 1초 딜레이
                        #time.sleep(1)
                        # 보유수량 불러오기
                        krw_balance42 = upbit.get_balance(krw_coin42)
                        # 코인 현재가 불러오기
                        price42 = pyupbit.get_current_price(krw_coin42)
                        # 보유코인 원화금액으로 계산하기
                        bp42 = price42 * krw_balance42

                        # 보유 및 매수 가능 출력.
                        print(f"[ 42. {krw_coin42} 매도완료. ]")
                        print(f"매도시간 : {now}  |  코인명 : {coin42}  |  현재가 = ￦{price42}  |  MACD = ￦{macd42}  |  보유수량 = {krw_balance42}  |  평가금액 = ￦{bp42}")
                        print(f"매수가능 : {op_mode42} - 가능")
                        print("")

                    else:   # 보유코인 평가 금액이 10,100원 이하일때
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode42 = True

                        print(f"[ 42. {krw_coin42} 보유코인이 없으므로 매도불가. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin42}")
                        print(f"매수가능 : {op_mode42} - 가능")
                        print("")

            # 1초 딜레이.
            time.sleep(1)
            ##### 42번 코인 매매 종료 #####
            #############################


            ###############################
            ##### 매매 : 43번코인 시작. #####

            ##### 코인보유현황
            # 보유수량 불러오기
            krw_balance43 = upbit.get_balance(krw_coin43)
            # 코인 현재가 불러오기
            price43 = pyupbit.get_current_price(krw_coin43)
            # 보유코인 원화금액으로 계산하기
            bp43 = price43 * krw_balance43
            # 코인 현황 출력.
            print(f"43. 코인명 : {coin43}  |  현재가 = ￦{price43}  |  보유수량 = {krw_balance43}  |  평가금액 = ￦{bp43}")
            # 코인 보유 유무
            if bp43 > 10100:
                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                op_mode43 = False

                # 보유 및 매수 가능 출력.
                print(f" 코인 보유 : 보유중  |  매수가능 - {op_mode43} - 매수불가")
                print("")
            else:
                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                op_mode43 = True

                # 보유 및 매수 가능 출력.
                print(f" 코인 보유 : 없음  |  매수가능 - {op_mode43} - 매수가능")
                print("")
            #time.sleep(1)


            # 코인 현재가 불러오기
            price43 = pyupbit.get_current_price(krw_coin43)

            # MACD 조회.
            #macd43 = get_macd(krw_coin43)
            # 거래량 동반한 MACD 조회.
            macd43 = get_acc_macd(krw_coin43)
            # 20일 이평선 조회.
            #macd43 = get_ma20(krw_coin43)

            # 매수가능금액 불러오기
            krw43 = upbit.get_balance("KRW")

            # MACD 조건문
            if macd43 >= 0:     # macd가 0보다 높을때는 매수
                if op_mode43 == True:    # 매수 가능(True)일 경우 - 매수시도
                    if krw43 > buy_krw:      # 매수가능금액 krw43 가 매수평균가 buy_krw 보다 클때
                        if krw43 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                            if buy_krw > 10100:     # 매수평균가 buy_krw 가 10,100원 초과일 경우 : 매수
                                # 매수금액은 매수평균가 buy_krw 로
                                upbit.buy_market_order(krw_coin43, buy_krw * 0.99)   # 매수가능금액에서 1%를 빼고

                                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                                op_mode43 = False

                                # 1초 딜레이
                                #time.sleep(1)
                                # 보유수량 불러오기
                                krw_balance43 = upbit.get_balance(krw_coin43)
                                # 코인 현재가 불러오기
                                price43 = pyupbit.get_current_price(krw_coin43)
                                # 보유코인 원화금액으로 계산하기
                                bp43 = price43 * krw_balance43

                                # 보유 및 매수 가능 출력.
                                print(f"[ 43. {krw_coin43} 매수완료. ]")
                                print(f"매수시간 : {now}  |  코인명 : {coin43}  |  현재가 = ￦{price43}  |  MACD = ￦{macd43}  |  보유수량 = {krw_balance43}  |  평가금액 = ￦{bp43}")
                                print(f"매수가능 : {op_mode43} - 불가")
                                print("")

                            else:
                                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                                op_mode43 = False

                                print(f"[ 43. {krw_coin43} 잔고부족으로 매수불가. ]")
                                print(f"현재시간 : {now}  |  코인명 : {coin43}")
                                print(f"매수가능 : {op_mode43} - 불가")
                                print("")

                        else:
                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode43 = False

                            print(f"[ 43. {krw_coin43} 잔고부족으로 매수불가. ]")
                            print(f"현재시간 : {now}  |  코인명 : {coin43}")
                            print(f"매수가능 : {op_mode43} - 불가")
                            print("")

                    elif krw43 <= buy_krw:   # 매수가능금액 krw43 가 매수평균가 buy_krw 보다 같거나 작을때
                        if krw43 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                            # 매수금액은 매수가능금액인 krw43 로
                            upbit.buy_market_order(krw_coin43, krw43 * 0.99)   # 매수가능금액에서 1%를 빼고

                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode43 = False

                            # 1초 딜레이
                            #time.sleep(1)
                            # 보유수량 불러오기
                            krw_balance43 = upbit.get_balance(krw_coin43)
                            # 코인 현재가 불러오기
                            price43 = pyupbit.get_current_price(krw_coin43)
                            # 보유코인 원화금액으로 계산하기
                            bp43 = price43 * krw_balance43

                            # 보유 및 매수 가능 출력.
                            print(f"[ 43. {krw_coin43} 매수완료. ]")
                            print(f"매수시간 : {now}  |  코인명 : {coin43}  |  현재가 = ￦{price43}  |  MACD = ￦{macd43}  |  보유수량 = {krw_balance43}  |  평가금액 = ￦{bp43}")
                            print(f"매수가능 : {op_mode43} - 불가")
                            print("")

                        else:
                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode43 = False

                            print(f"[ 43. {krw_coin43} 잔고부족으로 매수불가. ]")
                            print(f"현재시간 : {now}  |  코인명 : {coin43}")
                            print(f"매수가능 : {op_mode43} - 불가")
                            print("")

            elif macd43 < 0:       # macd가 0보다 낮을때는 매도
                if op_mode43 == False:   # 매수 불가(False)일 경우 - 매도시도
                    # 보유수량 불러오기
                    krw_balance43 = upbit.get_balance(krw_coin43)
                    # 현재가 불러오기
                    price43 = pyupbit.get_current_price(krw_coin43)
                    # 보유코인 원화금액으로 계산하기
                    bp43 = price43 * krw_balance43

                    # 보유코인 원화금액 매도시도
                    if  bp43 > 10100:   # 보유코인 평가 금액이 10,100원 초과일때 - 매도시도
                        # 매도할 코인명 - krw_coin43, 매도할 코인수량 - krw_balance43
                        upbit.sell_market_order(krw_coin43, krw_balance43)

                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode43 = True

                        # 1초 딜레이
                        #time.sleep(1)
                        # 보유수량 불러오기
                        krw_balance43 = upbit.get_balance(krw_coin43)
                        # 코인 현재가 불러오기
                        price43 = pyupbit.get_current_price(krw_coin43)
                        # 보유코인 원화금액으로 계산하기
                        bp43 = price43 * krw_balance43

                        # 보유 및 매수 가능 출력.
                        print(f"[ 43. {krw_coin43} 매도완료. ]")
                        print(f"매도시간 : {now}  |  코인명 : {coin43}  |  현재가 = ￦{price43}  |  MACD = ￦{macd43}  |  보유수량 = {krw_balance43}  |  평가금액 = ￦{bp43}")
                        print(f"매수가능 : {op_mode43} - 가능")
                        print("")

                    else:   # 보유코인 평가 금액이 10,100원 이하일때
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode43 = True

                        print(f"[ 43. {krw_coin43} 보유코인이 없으므로 매도불가. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin43}")
                        print(f"매수가능 : {op_mode43} - 가능")
                        print("")

            # 1초 딜레이.
            time.sleep(1)
            ##### 43번 코인 매매 종료 #####
            #############################

            
            ###############################
            ##### 매매 : 44번코인 시작. #####

            ##### 코인보유현황
            # 보유수량 불러오기
            krw_balance44 = upbit.get_balance(krw_coin44)
            # 코인 현재가 불러오기
            price44 = pyupbit.get_current_price(krw_coin44)
            # 보유코인 원화금액으로 계산하기
            bp44 = price44 * krw_balance44
            # 코인 현황 출력.
            print(f"44. 코인명 : {coin44}  |  현재가 = ￦{price44}  |  보유수량 = {krw_balance44}  |  평가금액 = ￦{bp44}")
            # 코인 보유 유무
            if bp44 > 10100:
                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                op_mode44 = False
                # 보유 및 매수 가능 출력.
                print(f" 코인 보유 : 보유중  |  매수가능 - {op_mode44} - 매수불가")
                print("")
            else:
                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                op_mode44 = True

                # 보유 및 매수 가능 출력.
                print(f" 코인 보유 : 없음  |  매수가능 - {op_mode44} - 매수가능")
                print("")
            #time.sleep(1)


            # 코인 현재가 불러오기
            price44 = pyupbit.get_current_price(krw_coin44)

            # MACD 조회.
            #macd44 = get_macd(krw_coin44)
            # 거래량 동반한 MACD 조회.
            macd44 = get_acc_macd(krw_coin44)
            # 20일 이평선 조회.
            #macd44 = get_ma20(krw_coin44)

            # 매수가능금액 불러오기
            krw44 = upbit.get_balance("KRW")

            # MACD 조건문
            if macd44 >= 0:     # macd가 0보다 높을때는 매수
                if op_mode44 == True:    # 매수 가능(True)일 경우 - 매수시도
                    if krw44 > buy_krw:      # 매수가능금액 krw44 가 매수평균가 buy_krw 보다 클때
                        if krw44 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                            if buy_krw > 10100:     # 매수평균가 buy_krw 가 10,100원 초과일 경우 : 매수
                                # 매수금액은 매수평균가 buy_krw 로
                                upbit.buy_market_order(krw_coin44, buy_krw * 0.99)   # 매수가능금액에서 1%를 빼고

                                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                                op_mode44 = False

                                # 1초 딜레이
                                #time.sleep(1)
                                # 보유수량 불러오기
                                krw_balance44 = upbit.get_balance(krw_coin44)
                                # 코인 현재가 불러오기
                                price44 = pyupbit.get_current_price(krw_coin44)
                                # 보유코인 원화금액으로 계산하기
                                bp44 = price44 * krw_balance44

                                # 보유 및 매수 가능 출력.
                                print(f"[ 44. {krw_coin44} 매수완료. ]")
                                print(f"매수시간 : {now}  |  코인명 : {coin44}  |  현재가 = ￦{price44}  |  MACD = ￦{macd44}  |  보유수량 = {krw_balance44}  |  평가금액 = ￦{bp44}")
                                print(f"매수가능 : {op_mode44} - 불가")
                                print("")

                            else:
                                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                                op_mode44 = False

                                print(f"[ 44. {krw_coin44} 잔고부족으로 매수불가. ]")
                                print(f"현재시간 : {now}  |  코인명 : {coin44}")
                                print(f"매수가능 : {op_mode44} - 불가")
                                print("")

                        else:
                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode44 = False

                            print(f"[ 44. {krw_coin44} 잔고부족으로 매수불가. ]")
                            print(f"현재시간 : {now}  |  코인명 : {coin44}")
                            print(f"매수가능 : {op_mode44} - 불가")
                            print("")

                    elif krw44 <= buy_krw:   # 매수가능금액 krw44 가 매수평균가 buy_krw 보다 같거나 작을때
                        if krw44 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                            # 매수금액은 매수가능금액인 krw44 로
                            upbit.buy_market_order(krw_coin44, krw44 * 0.99)   # 매수가능금액에서 1%를 빼고

                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode44 = False

                            # 1초 딜레이
                            #time.sleep(1)
                            # 보유수량 불러오기
                            krw_balance44 = upbit.get_balance(krw_coin44)
                            # 코인 현재가 불러오기
                            price44 = pyupbit.get_current_price(krw_coin44)
                            # 보유코인 원화금액으로 계산하기
                            bp44 = price44 * krw_balance44

                            # 보유 및 매수 가능 출력.
                            print(f"[ 44. {krw_coin44} 매수완료. ]")
                            print(f"매수시간 : {now}  |  코인명 : {coin44}  |  현재가 = ￦{price44}  |  MACD = ￦{macd44}  |  보유수량 = {krw_balance44}  |  평가금액 = ￦{bp44}")
                            print(f"매수가능 : {op_mode44} - 불가")
                            print("")

                        else:
                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode44 = False

                            print(f"[ 44. {krw_coin44} 잔고부족으로 매수불가. ]")
                            print(f"현재시간 : {now}  |  코인명 : {coin44}")
                            print(f"매수가능 : {op_mode44} - 불가")
                            print("")

            elif macd44 < 0:       # macd가 0보다 낮을때는 매도
                if op_mode44 == False:   # 매수 불가(False)일 경우 - 매도시도
                    # 보유수량 불러오기
                    krw_balance44 = upbit.get_balance(krw_coin44)
                    # 현재가 불러오기
                    price44 = pyupbit.get_current_price(krw_coin44)
                    # 보유코인 원화금액으로 계산하기
                    bp44 = price44 * krw_balance44

                    # 보유코인 원화금액 매도시도
                    if  bp44 > 10100:   # 보유코인 평가 금액이 10,100원 초과일때 - 매도시도
                        # 매도할 코인명 - krw_coin44, 매도할 코인수량 - krw_balance44
                        upbit.sell_market_order(krw_coin44, krw_balance44)

                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode44 = True

                        # 1초 딜레이
                        #time.sleep(1)
                        # 보유수량 불러오기
                        krw_balance44 = upbit.get_balance(krw_coin44)
                        # 코인 현재가 불러오기
                        price44 = pyupbit.get_current_price(krw_coin44)
                        # 보유코인 원화금액으로 계산하기
                        bp44 = price44 * krw_balance44

                        # 보유 및 매수 가능 출력.
                        print(f"[ 44. {krw_coin44} 매도완료. ]")
                        print(f"매도시간 : {now}  |  코인명 : {coin44}  |  현재가 = ￦{price44}  |  MACD = ￦{macd44}  |  보유수량 = {krw_balance44}  |  평가금액 = ￦{bp44}")
                        print(f"매수가능 : {op_mode44} - 가능")
                        print("")

                    else:   # 보유코인 평가 금액이 10,100원 이하일때
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode44 = True

                        print(f"[ 44. {krw_coin44} 보유코인이 없으므로 매도불가. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin44}")
                        print(f"매수가능 : {op_mode44} - 가능")
                        print("")

            # 1초 딜레이.
            time.sleep(1)
            ##### 44번 코인 매매 종료 #####
            #############################


            ###############################
            ##### 매매 : 45번코인 시작. #####

            ##### 코인보유현황
            # 보유수량 불러오기
            krw_balance45 = upbit.get_balance(krw_coin45)
            # 코인 현재가 불러오기
            price45 = pyupbit.get_current_price(krw_coin45)
            # 보유코인 원화금액으로 계산하기
            bp45 = price45 * krw_balance45
            # 코인 현황 출력.
            print(f"45. 코인명 : {coin45}  |  현재가 = ￦{price45}  |  보유수량 = {krw_balance45}  |  평가금액 = ￦{bp45}")
            # 코인 보유 유무
            if bp45 > 10100:
                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                op_mode45 = False

                # 보유 및 매수 가능 출력.
                print(f" 코인 보유 : 보유중  |  매수가능 - {op_mode45} - 매수불가")
                print("")
            else:
                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                op_mode45 = True

                # 보유 및 매수 가능 출력.
                print(f" 코인 보유 : 없음  |  매수가능 - {op_mode45} - 매수가능")
                print("")
            #time.sleep(1)


            # 코인 현재가 불러오기
            price45 = pyupbit.get_current_price(krw_coin45)

            # MACD 조회.
            #macd45 = get_macd(krw_coin45)
            # 거래량 동반한 MACD 조회.
            macd45 = get_acc_macd(krw_coin45)
            # 20일 이평선 조회.
            #macd45 = get_ma20(krw_coin45)

            # 매수가능금액 불러오기
            krw45 = upbit.get_balance("KRW")

            # MACD 조건문
            if macd45 >= 0:     # macd가 0보다 높을때는 매수
                if op_mode45 == True:    # 매수 가능(True)일 경우 - 매수시도
                    if krw45 > buy_krw:      # 매수가능금액 krw45 가 매수평균가 buy_krw 보다 클때
                        if krw45 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                            if buy_krw > 10100:     # 매수평균가 buy_krw 가 10,100원 초과일 경우 : 매수
                                # 매수금액은 매수평균가 buy_krw 로
                                upbit.buy_market_order(krw_coin45, buy_krw * 0.99)   # 매수가능금액에서 1%를 빼고

                                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                                op_mode45 = False

                                # 1초 딜레이
                                #time.sleep(1)
                                # 보유수량 불러오기
                                krw_balance45 = upbit.get_balance(krw_coin45)
                                # 코인 현재가 불러오기
                                price45 = pyupbit.get_current_price(krw_coin45)
                                # 보유코인 원화금액으로 계산하기
                                bp45 = price45 * krw_balance45

                                # 보유 및 매수 가능 출력.
                                print(f"[ 45. {krw_coin45} 매수완료. ]")
                                print(f"매수시간 : {now}  |  코인명 : {coin45}  |  현재가 = ￦{price45}  |  MACD = ￦{macd45}  |  보유수량 = {krw_balance45}  |  평가금액 = ￦{bp45}")
                                print(f"매수가능 : {op_mode45} - 불가")
                                print("")

                            else:
                                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                                op_mode45 = False

                                print(f"[ 45. {krw_coin45} 잔고부족으로 매수불가. ]")
                                print(f"현재시간 : {now}  |  코인명 : {coin45}")
                                print(f"매수가능 : {op_mode45} - 불가")
                                print("")

                        else:
                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode45 = False

                            print(f"[ 45. {krw_coin45} 잔고부족으로 매수불가. ]")
                            print(f"현재시간 : {now}  |  코인명 : {coin45}")
                            print(f"매수가능 : {op_mode45} - 불가")
                            print("")

                    elif krw45 <= buy_krw:   # 매수가능금액 krw45 가 매수평균가 buy_krw 보다 같거나 작을때
                        if krw45 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                            # 매수금액은 매수가능금액인 krw45 로
                            upbit.buy_market_order(krw_coin45, krw45 * 0.99)   # 매수가능금액에서 1%를 빼고

                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode45 = False

                            # 1초 딜레이
                            #time.sleep(1)
                            # 보유수량 불러오기
                            krw_balance45 = upbit.get_balance(krw_coin45)
                            # 코인 현재가 불러오기
                            price45 = pyupbit.get_current_price(krw_coin45)
                            # 보유코인 원화금액으로 계산하기
                            bp45 = price45 * krw_balance45

                            # 보유 및 매수 가능 출력.
                            print(f"[ 45. {krw_coin45} 매수완료. ]")
                            print(f"매수시간 : {now}  |  코인명 : {coin45}  |  현재가 = ￦{price45}  |  MACD = ￦{macd45}  |  보유수량 = {krw_balance45}  |  평가금액 = ￦{bp45}")
                            print(f"매수가능 : {op_mode45} - 불가")
                            print("")

                        else:
                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode45 = False

                            print(f"[ 45. {krw_coin45} 잔고부족으로 매수불가. ]")
                            print(f"현재시간 : {now}  |  코인명 : {coin45}")
                            print(f"매수가능 : {op_mode45} - 불가")
                            print("")

            elif macd45 < 0:       # macd가 0보다 낮을때는 매도
                if op_mode45 == False:   # 매수 불가(False)일 경우 - 매도시도
                    # 보유수량 불러오기
                    krw_balance45 = upbit.get_balance(krw_coin45)
                    # 현재가 불러오기
                    price45 = pyupbit.get_current_price(krw_coin45)
                    # 보유코인 원화금액으로 계산하기
                    bp45 = price45 * krw_balance45

                    # 보유코인 원화금액 매도시도
                    if  bp45 > 10100:   # 보유코인 평가 금액이 10,100원 초과일때 - 매도시도
                        # 매도할 코인명 - krw_coin45, 매도할 코인수량 - krw_balance45
                        upbit.sell_market_order(krw_coin45, krw_balance45)

                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode45 = True

                        # 1초 딜레이
                        #time.sleep(1)
                        # 보유수량 불러오기
                        krw_balance45 = upbit.get_balance(krw_coin45)
                        # 코인 현재가 불러오기
                        price45 = pyupbit.get_current_price(krw_coin45)
                        # 보유코인 원화금액으로 계산하기
                        bp45 = price45 * krw_balance45

                        # 보유 및 매수 가능 출력.
                        print(f"[ 45. {krw_coin45} 매도완료. ]")
                        print(f"매도시간 : {now}  |  코인명 : {coin45}  |  현재가 = ￦{price45}  |  MACD = ￦{macd45}  |  보유수량 = {krw_balance45}  |  평가금액 = ￦{bp45}")
                        print(f"매수가능 : {op_mode45} - 가능")
                        print("")

                    else:   # 보유코인 평가 금액이 10,100원 이하일때
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode45 = True

                        print(f"[ 45. {krw_coin45} 보유코인이 없으므로 매도불가. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin45}")
                        print(f"매수가능 : {op_mode45} - 가능")
                        print("")

            # 1초 딜레이.
            time.sleep(1)
            ##### 45번 코인 매매 종료 #####
            #############################


            ###############################
            ##### 매매 : 46번코인 시작. #####

            ##### 코인보유현황
            # 보유수량 불러오기
            krw_balance46 = upbit.get_balance(krw_coin46)
            # 코인 현재가 불러오기
            price46 = pyupbit.get_current_price(krw_coin46)
            # 보유코인 원화금액으로 계산하기
            bp46 = price46 * krw_balance46
            # 코인 현황 출력.
            print(f"46. 코인명 : {coin46}  |  현재가 = ￦{price46}  |  보유수량 = {krw_balance46}  |  평가금액 = ￦{bp46}")
            # 코인 보유 유무
            if bp46 > 10100:
                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                op_mode46 = False

                # 보유 및 매수 가능 출력.
                print(f" 코인 보유 : 보유중  |  매수가능 - {op_mode46} - 매수불가")
                print("")
            else:
                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                op_mode46 = True

                # 보유 및 매수 가능 출력.
                print(f" 코인 보유 : 없음  |  매수가능 - {op_mode46} - 매수가능")
                print("")
            #time.sleep(1)


            # 코인 현재가 불러오기
            price46 = pyupbit.get_current_price(krw_coin46)

            # MACD 조회.
            #macd46 = get_macd(krw_coin46)
            # 거래량 동반한 MACD 조회.
            macd46 = get_acc_macd(krw_coin46)
            # 20일 이평선 조회.
            #macd46 = get_ma20(krw_coin46)

            # 매수가능금액 불러오기
            krw46 = upbit.get_balance("KRW")

            # MACD 조건문
            if macd46 >= 0:     # macd가 0보다 높을때는 매수
                if op_mode46 == True:    # 매수 가능(True)일 경우 - 매수시도
                    if krw46 > buy_krw:      # 매수가능금액 krw46 가 매수평균가 buy_krw 보다 클때
                        if krw46 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                            if buy_krw > 10100:     # 매수평균가 buy_krw 가 10,100원 초과일 경우 : 매수
                                # 매수금액은 매수평균가 buy_krw 로
                                upbit.buy_market_order(krw_coin46, buy_krw * 0.99)   # 매수가능금액에서 1%를 빼고

                                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                                op_mode46 = False

                                # 1초 딜레이
                                #time.sleep(1)
                                # 보유수량 불러오기
                                krw_balance46 = upbit.get_balance(krw_coin46)
                                # 코인 현재가 불러오기
                                price46 = pyupbit.get_current_price(krw_coin46)
                                # 보유코인 원화금액으로 계산하기
                                bp46 = price46 * krw_balance46

                                # 보유 및 매수 가능 출력.
                                print(f"[ 46. {krw_coin46} 매수완료. ]")
                                print(f"매수시간 : {now}  |  코인명 : {coin46}  |  현재가 = ￦{price46}  |  MACD = ￦{macd46}  |  보유수량 = {krw_balance46}  |  평가금액 = ￦{bp46}")
                                print(f"매수가능 : {op_mode46} - 불가")
                                print("")

                            else:
                                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                                op_mode46 = False

                                print(f"[ 46. {krw_coin46} 잔고부족으로 매수불가. ]")
                                print(f"현재시간 : {now}  |  코인명 : {coin46}")
                                print(f"매수가능 : {op_mode46} - 불가")
                                print("")

                        else:
                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode46 = False

                            print(f"[ 46. {krw_coin46} 잔고부족으로 매수불가. ]")
                            print(f"현재시간 : {now}  |  코인명 : {coin46}")
                            print(f"매수가능 : {op_mode46} - 불가")
                            print("")

                    elif krw46 <= buy_krw:   # 매수가능금액 krw46 가 매수평균가 buy_krw 보다 같거나 작을때
                        if krw46 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                            # 매수금액은 매수가능금액인 krw46 로
                            upbit.buy_market_order(krw_coin46, krw46 * 0.99)   # 매수가능금액에서 1%를 빼고

                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode46 = False

                            # 1초 딜레이
                            #time.sleep(1)
                            # 보유수량 불러오기
                            krw_balance46 = upbit.get_balance(krw_coin46)
                            # 코인 현재가 불러오기
                            price46 = pyupbit.get_current_price(krw_coin46)
                            # 보유코인 원화금액으로 계산하기
                            bp46 = price46 * krw_balance46

                            # 보유 및 매수 가능 출력.
                            print(f"[ 46. {krw_coin46} 매수완료. ]")
                            print(f"매수시간 : {now}  |  코인명 : {coin46}  |  현재가 = ￦{price46}  |  MACD = ￦{macd46}  |  보유수량 = {krw_balance46}  |  평가금액 = ￦{bp46}")
                            print(f"매수가능 : {op_mode46} - 불가")
                            print("")

                        else:
                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode46 = False

                            print(f"[ 46. {krw_coin46} 잔고부족으로 매수불가. ]")
                            print(f"현재시간 : {now}  |  코인명 : {coin46}")
                            print(f"매수가능 : {op_mode46} - 불가")
                            print("")

            elif macd46 < 0:       # macd가 0보다 낮을때는 매도
                if op_mode46 == False:   # 매수 불가(False)일 경우 - 매도시도
                    # 보유수량 불러오기
                    krw_balance46 = upbit.get_balance(krw_coin46)
                    # 현재가 불러오기
                    price46 = pyupbit.get_current_price(krw_coin46)
                    # 보유코인 원화금액으로 계산하기
                    bp46 = price46 * krw_balance46

                    # 보유코인 원화금액 매도시도
                    if  bp46 > 10100:   # 보유코인 평가 금액이 10,100원 초과일때 - 매도시도
                        # 매도할 코인명 - krw_coin46, 매도할 코인수량 - krw_balance46
                        upbit.sell_market_order(krw_coin46, krw_balance46)

                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode46 = True

                        # 1초 딜레이
                        #time.sleep(1)
                        # 보유수량 불러오기
                        krw_balance46 = upbit.get_balance(krw_coin46)
                        # 코인 현재가 불러오기
                        price46 = pyupbit.get_current_price(krw_coin46)
                        # 보유코인 원화금액으로 계산하기
                        bp46 = price46 * krw_balance46

                        # 보유 및 매수 가능 출력.
                        print(f"[ 46. {krw_coin46} 매도완료. ]")
                        print(f"매도시간 : {now}  |  코인명 : {coin46}  |  현재가 = ￦{price46}  |  MACD = ￦{macd46}  |  보유수량 = {krw_balance46}  |  평가금액 = ￦{bp46}")
                        print(f"매수가능 : {op_mode46} - 가능")
                        print("")

                    else:   # 보유코인 평가 금액이 10,100원 이하일때
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode46 = True

                        print(f"[ 46. {krw_coin46} 보유코인이 없으므로 매도불가. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin46}")
                        print(f"매수가능 : {op_mode46} - 가능")
                        print("")

            # 1초 딜레이.
            time.sleep(1)
            ##### 46번 코인 매매 종료 #####
            #############################


            ###############################
            ##### 매매 : 47번코인 시작. #####

            ##### 코인보유현황
            # 보유수량 불러오기
            krw_balance47 = upbit.get_balance(krw_coin47)
            # 코인 현재가 불러오기
            price47 = pyupbit.get_current_price(krw_coin47)
            # 보유코인 원화금액으로 계산하기
            bp47 = price47 * krw_balance47
            # 코인 현황 출력.
            print(f"47. 코인명 : {coin47}  |  현재가 = ￦{price47}  |  보유수량 = {krw_balance47}  |  평가금액 = ￦{bp47}")
            # 코인 보유 유무
            if bp47 > 10100:
                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                op_mode47 = False

                # 보유 및 매수 가능 출력.
                print(f" 코인 보유 : 보유중  |  매수가능 - {op_mode47} - 매수불가")
                print("")
            else:
                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                op_mode47 = True

                # 보유 및 매수 가능 출력.
                print(f" 코인 보유 : 없음  |  매수가능 - {op_mode47} - 매수가능")
                print("")
            #time.sleep(1)


            # 코인 현재가 불러오기
            price47 = pyupbit.get_current_price(krw_coin47)

            # MACD 조회.
            #macd47 = get_macd(krw_coin47)
            # 거래량 동반한 MACD 조회.
            macd47 = get_acc_macd(krw_coin47)
            # 20일 이평선 조회.
            #macd47 = get_ma20(krw_coin47)

            # 매수가능금액 불러오기
            krw47 = upbit.get_balance("KRW")

            # MACD 조건문
            if macd47 >= 0:     # macd가 0보다 높을때는 매수
                if op_mode47 == True:    # 매수 가능(True)일 경우 - 매수시도
                    if krw47 > buy_krw:      # 매수가능금액 krw47 가 매수평균가 buy_krw 보다 클때
                        if krw47 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                            if buy_krw > 10100:     # 매수평균가 buy_krw 가 10,100원 초과일 경우 : 매수
                                # 매수금액은 매수평균가 buy_krw 로
                                upbit.buy_market_order(krw_coin47, buy_krw * 0.99)   # 매수가능금액에서 1%를 빼고

                                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                                op_mode47 = False

                                # 1초 딜레이
                                #time.sleep(1)
                                # 보유수량 불러오기
                                krw_balance47 = upbit.get_balance(krw_coin47)
                                # 코인 현재가 불러오기
                                price47 = pyupbit.get_current_price(krw_coin47)
                                # 보유코인 원화금액으로 계산하기
                                bp47 = price47 * krw_balance47

                                # 보유 및 매수 가능 출력.
                                print(f"[ 47. {krw_coin47} 매수완료. ]")
                                print(f"매수시간 : {now}  |  코인명 : {coin47}  |  현재가 = ￦{price47}  |  MACD = ￦{macd47}  |  보유수량 = {krw_balance47}  |  평가금액 = ￦{bp47}")
                                print(f"매수가능 : {op_mode47} - 불가")
                                print("")

                            else:
                                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                                op_mode47 = False

                                print(f"[ 47. {krw_coin47} 잔고부족으로 매수불가. ]")
                                print(f"현재시간 : {now}  |  코인명 : {coin47}")
                                print(f"매수가능 : {op_mode47} - 불가")
                                print("")

                        else:
                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode47 = False

                            print(f"[ 47. {krw_coin47} 잔고부족으로 매수불가. ]")
                            print(f"현재시간 : {now}  |  코인명 : {coin47}")
                            print(f"매수가능 : {op_mode47} - 불가")
                            print("")

                    elif krw47 <= buy_krw:   # 매수가능금액 krw47 가 매수평균가 buy_krw 보다 같거나 작을때
                        if krw47 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                            # 매수금액은 매수가능금액인 krw47 로
                            upbit.buy_market_order(krw_coin47, krw47 * 0.99)   # 매수가능금액에서 1%를 빼고

                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode47 = False

                            # 1초 딜레이
                            #time.sleep(1)
                            # 보유수량 불러오기
                            krw_balance47 = upbit.get_balance(krw_coin47)
                            # 코인 현재가 불러오기
                            price47 = pyupbit.get_current_price(krw_coin47)
                            # 보유코인 원화금액으로 계산하기
                            bp47 = price47 * krw_balance47

                            # 보유 및 매수 가능 출력.
                            print(f"[ 47. {krw_coin47} 매수완료. ]")
                            print(f"매수시간 : {now}  |  코인명 : {coin47}  |  현재가 = ￦{price47}  |  MACD = ￦{macd47}  |  보유수량 = {krw_balance47}  |  평가금액 = ￦{bp47}")
                            print(f"매수가능 : {op_mode47} - 불가")
                            print("")

                        else:
                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode47 = False

                            print(f"[ 47. {krw_coin47} 잔고부족으로 매수불가. ]")
                            print(f"현재시간 : {now}  |  코인명 : {coin47}")
                            print(f"매수가능 : {op_mode47} - 불가")
                            print("")

            elif macd47 < 0:       # macd가 0보다 낮을때는 매도
                if op_mode47 == False:   # 매수 불가(False)일 경우 - 매도시도
                    # 보유수량 불러오기
                    krw_balance47 = upbit.get_balance(krw_coin47)
                    # 현재가 불러오기
                    price47 = pyupbit.get_current_price(krw_coin47)
                    # 보유코인 원화금액으로 계산하기
                    bp47 = price47 * krw_balance47

                    # 보유코인 원화금액 매도시도
                    if  bp47 > 10100:   # 보유코인 평가 금액이 10,100원 초과일때 - 매도시도
                        # 매도할 코인명 - krw_coin47, 매도할 코인수량 - krw_balance47
                        upbit.sell_market_order(krw_coin47, krw_balance47)

                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode47 = True

                        # 1초 딜레이
                        #time.sleep(1)
                        # 보유수량 불러오기
                        krw_balance47 = upbit.get_balance(krw_coin47)
                        # 코인 현재가 불러오기
                        price47 = pyupbit.get_current_price(krw_coin47)
                        # 보유코인 원화금액으로 계산하기
                        bp47 = price47 * krw_balance47

                        # 보유 및 매수 가능 출력.
                        print(f"[ 47. {krw_coin47} 매도완료. ]")
                        print(f"매도시간 : {now}  |  코인명 : {coin47}  |  현재가 = ￦{price47}  |  MACD = ￦{macd47}  |  보유수량 = {krw_balance47}  |  평가금액 = ￦{bp47}")
                        print(f"매수가능 : {op_mode47} - 가능")
                        print("")

                    else:   # 보유코인 평가 금액이 10,100원 이하일때
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode47 = True

                        print(f"[ 47. {krw_coin47} 보유코인이 없으므로 매도불가. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin47}")
                        print(f"매수가능 : {op_mode47} - 가능")
                        print("")

            # 1초 딜레이.
            time.sleep(1)
            ##### 47번 코인 매매 종료 #####
            #############################


            ###############################
            ##### 매매 : 48번코인 시작. #####

            ##### 코인보유현황
            # 보유수량 불러오기
            krw_balance48 = upbit.get_balance(krw_coin48)
            # 코인 현재가 불러오기
            price48 = pyupbit.get_current_price(krw_coin48)
            # 보유코인 원화금액으로 계산하기
            bp48 = price48 * krw_balance48
            # 코인 현황 출력.
            print(f"48. 코인명 : {coin48}  |  현재가 = ￦{price48}  |  보유수량 = {krw_balance48}  |  평가금액 = ￦{bp48}")
            # 코인 보유 유무
            if bp48 > 10100:
                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                op_mode48 = False

                # 보유 및 매수 가능 출력.
                print(f" 코인 보유 : 보유중  |  매수가능 - {op_mode48} - 매수불가")
                print("")
            else:
                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                op_mode48 = True

                # 보유 및 매수 가능 출력.
                print(f" 코인 보유 : 없음  |  매수가능 - {op_mode48} - 매수가능")
                print("")
            #time.sleep(1)


            # 코인 현재가 불러오기
            price48 = pyupbit.get_current_price(krw_coin48)

            # MACD 조회.
            #macd48 = get_macd(krw_coin48)
            # 거래량 동반한 MACD 조회.
            macd48 = get_acc_macd(krw_coin48)
            # 20일 이평선 조회.
            #macd48 = get_ma20(krw_coin48)

            # 매수가능금액 불러오기
            krw48 = upbit.get_balance("KRW")

            # MACD 조건문
            if macd48 >= 0:     # macd가 0보다 높을때는 매수
                if op_mode48 == True:    # 매수 가능(True)일 경우 - 매수시도
                    if krw48 > buy_krw:      # 매수가능금액 krw48 가 매수평균가 buy_krw 보다 클때
                        if krw48 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                            if buy_krw > 10100:     # 매수평균가 buy_krw 가 10,100원 초과일 경우 : 매수
                                # 매수금액은 매수평균가 buy_krw 로
                                upbit.buy_market_order(krw_coin48, buy_krw * 0.99)   # 매수가능금액에서 1%를 빼고

                                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                                op_mode48 = False

                                # 1초 딜레이
                                #time.sleep(1)
                                # 보유수량 불러오기
                                krw_balance48 = upbit.get_balance(krw_coin48)
                                # 코인 현재가 불러오기
                                price48 = pyupbit.get_current_price(krw_coin48)
                                # 보유코인 원화금액으로 계산하기
                                bp48 = price48 * krw_balance48

                                # 보유 및 매수 가능 출력.
                                print(f"[ 48. {krw_coin48} 매수완료. ]")
                                print(f"매수시간 : {now}  |  코인명 : {coin48}  |  현재가 = ￦{price48}  |  MACD = ￦{macd48}  |  보유수량 = {krw_balance48}  |  평가금액 = ￦{bp48}")
                                print(f"매수가능 : {op_mode48} - 불가")
                                print("")

                            else:
                                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                                op_mode48 = False

                                print(f"[ 48. {krw_coin48} 잔고부족으로 매수불가. ]")
                                print(f"현재시간 : {now}  |  코인명 : {coin48}")
                                print(f"매수가능 : {op_mode48} - 불가")
                                print("")

                        else:
                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode48 = False

                            print(f"[ 48. {krw_coin48} 잔고부족으로 매수불가. ]")
                            print(f"현재시간 : {now}  |  코인명 : {coin48}")
                            print(f"매수가능 : {op_mode48} - 불가")
                            print("")

                    elif krw48 <= buy_krw:   # 매수가능금액 krw48 가 매수평균가 buy_krw 보다 같거나 작을때
                        if krw48 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                            # 매수금액은 매수가능금액인 krw48 로
                            upbit.buy_market_order(krw_coin48, krw48 * 0.99)   # 매수가능금액에서 1%를 빼고

                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode48 = False

                            # 1초 딜레이
                            #time.sleep(1)
                            # 보유수량 불러오기
                            krw_balance48 = upbit.get_balance(krw_coin48)
                            # 코인 현재가 불러오기
                            price48 = pyupbit.get_current_price(krw_coin48)
                            # 보유코인 원화금액으로 계산하기
                            bp48 = price48 * krw_balance48

                            # 보유 및 매수 가능 출력.
                            print(f"[ 48. {krw_coin48} 매수완료. ]")
                            print(f"매수시간 : {now}  |  코인명 : {coin48}  |  현재가 = ￦{price48}  |  MACD = ￦{macd48}  |  보유수량 = {krw_balance48}  |  평가금액 = ￦{bp48}")
                            print(f"매수가능 : {op_mode48} - 불가")
                            print("")

                        else:
                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode48 = False

                            print(f"[ 48. {krw_coin48} 잔고부족으로 매수불가. ]")
                            print(f"현재시간 : {now}  |  코인명 : {coin48}")
                            print(f"매수가능 : {op_mode48} - 불가")
                            print("")

            elif macd48 < 0:       # macd가 0보다 낮을때는 매도
                if op_mode48 == False:   # 매수 불가(False)일 경우 - 매도시도
                    # 보유수량 불러오기
                    krw_balance48 = upbit.get_balance(krw_coin48)
                    # 현재가 불러오기
                    price48 = pyupbit.get_current_price(krw_coin48)
                    # 보유코인 원화금액으로 계산하기
                    bp48 = price48 * krw_balance48

                    # 보유코인 원화금액 매도시도
                    if  bp48 > 10100:   # 보유코인 평가 금액이 10,100원 초과일때 - 매도시도
                        # 매도할 코인명 - krw_coin48, 매도할 코인수량 - krw_balance48
                        upbit.sell_market_order(krw_coin48, krw_balance48)

                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode48 = True

                        # 1초 딜레이
                        #time.sleep(1)
                        # 보유수량 불러오기
                        krw_balance48 = upbit.get_balance(krw_coin48)
                        # 코인 현재가 불러오기
                        price48 = pyupbit.get_current_price(krw_coin48)
                        # 보유코인 원화금액으로 계산하기
                        bp48 = price48 * krw_balance48

                        # 보유 및 매수 가능 출력.
                        print(f"[ 48. {krw_coin48} 매도완료. ]")
                        print(f"매도시간 : {now}  |  코인명 : {coin48}  |  현재가 = ￦{price48}  |  MACD = ￦{macd48}  |  보유수량 = {krw_balance48}  |  평가금액 = ￦{bp48}")
                        print(f"매수가능 : {op_mode48} - 가능")
                        print("")

                    else:   # 보유코인 평가 금액이 10,100원 이하일때
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode48 = True

                        print(f"[ 48. {krw_coin48} 보유코인이 없으므로 매도불가. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin48}")
                        print(f"매수가능 : {op_mode48} - 가능")
                        print("")

            # 1초 딜레이.
            time.sleep(1)
            ##### 48번 코인 매매 종료 #####
            #############################


            ###############################
            ##### 매매 : 49번코인 시작. #####

            ##### 코인보유현황
            # 보유수량 불러오기
            krw_balance49 = upbit.get_balance(krw_coin49)
            # 코인 현재가 불러오기
            price49 = pyupbit.get_current_price(krw_coin49)
            # 보유코인 원화금액으로 계산하기
            bp49 = price49 * krw_balance49
            # 코인 현황 출력.
            print(f"49. 코인명 : {coin49}  |  현재가 = ￦{price49}  |  보유수량 = {krw_balance49}  |  평가금액 = ￦{bp49}")
            # 코인 보유 유무
            if bp49 > 10100:
                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                op_mode49 = False

                # 보유 및 매수 가능 출력.
                print(f" 코인 보유 : 보유중  |  매수가능 - {op_mode49} - 매수불가")
                print("")
            else:
                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                op_mode49 = True

                # 보유 및 매수 가능 출력.
                print(f" 코인 보유 : 없음  |  매수가능 - {op_mode49} - 매수가능")
                print("")
            #time.sleep(1)


            # 코인 현재가 불러오기
            price49 = pyupbit.get_current_price(krw_coin49)

            # MACD 조회.
            #macd49 = get_macd(krw_coin49)
            # 거래량 동반한 MACD 조회.
            macd49 = get_acc_macd(krw_coin49)
            # 20일 이평선 조회.
            #macd49 = get_ma20(krw_coin49)

            # 매수가능금액 불러오기
            krw49 = upbit.get_balance("KRW")

            # MACD 조건문
            if macd49 >= 0:     # macd가 0보다 높을때는 매수
                if op_mode49 == True:    # 매수 가능(True)일 경우 - 매수시도
                    if krw49 > buy_krw:      # 매수가능금액 krw49 가 매수평균가 buy_krw 보다 클때
                        if krw49 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                            if buy_krw > 10100:     # 매수평균가 buy_krw 가 10,100원 초과일 경우 : 매수
                                # 매수금액은 매수평균가 buy_krw 로
                                upbit.buy_market_order(krw_coin49, buy_krw * 0.99)   # 매수가능금액에서 1%를 빼고

                                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                                op_mode49 = False

                                # 1초 딜레이
                                #time.sleep(1)
                                # 보유수량 불러오기
                                krw_balance49 = upbit.get_balance(krw_coin49)
                                # 코인 현재가 불러오기
                                price49 = pyupbit.get_current_price(krw_coin49)
                                # 보유코인 원화금액으로 계산하기
                                bp49 = price49 * krw_balance49

                                # 보유 및 매수 가능 출력.
                                print(f"[ 49. {krw_coin49} 매수완료. ]")
                                print(f"매수시간 : {now}  |  코인명 : {coin49}  |  현재가 = ￦{price49}  |  MACD = ￦{macd49}  |  보유수량 = {krw_balance49}  |  평가금액 = ￦{bp49}")
                                print(f"매수가능 : {op_mode49} - 불가")
                                print("")

                            else:
                                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                                op_mode49 = False

                                print(f"[ 49. {krw_coin49} 잔고부족으로 매수불가. ]")
                                print(f"현재시간 : {now}  |  코인명 : {coin49}")
                                print(f"매수가능 : {op_mode49} - 불가")
                                print("")

                        else:
                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode49 = False

                            print(f"[ 49. {krw_coin49} 잔고부족으로 매수불가. ]")
                            print(f"현재시간 : {now}  |  코인명 : {coin49}")
                            print(f"매수가능 : {op_mode49} - 불가")
                            print("")

                    elif krw49 <= buy_krw:   # 매수가능금액 krw49 가 매수평균가 buy_krw 보다 같거나 작을때
                        if krw49 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                            # 매수금액은 매수가능금액인 krw49 로
                            upbit.buy_market_order(krw_coin49, krw49 * 0.99)   # 매수가능금액에서 1%를 빼고

                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode49 = False

                            # 1초 딜레이
                            #time.sleep(1)
                            # 보유수량 불러오기
                            krw_balance49 = upbit.get_balance(krw_coin49)
                            # 코인 현재가 불러오기
                            price49 = pyupbit.get_current_price(krw_coin49)
                            # 보유코인 원화금액으로 계산하기
                            bp49 = price49 * krw_balance49

                            # 보유 및 매수 가능 출력.
                            print(f"[ 49. {krw_coin49} 매수완료. ]")
                            print(f"매수시간 : {now}  |  코인명 : {coin49}  |  현재가 = ￦{price49}  |  MACD = ￦{macd49}  |  보유수량 = {krw_balance49}  |  평가금액 = ￦{bp49}")
                            print(f"매수가능 : {op_mode49} - 불가")
                            print("")

                        else:
                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode49 = False

                            print(f"[ 49. {krw_coin49} 잔고부족으로 매수불가. ]")
                            print(f"현재시간 : {now}  |  코인명 : {coin49}")
                            print(f"매수가능 : {op_mode49} - 불가")
                            print("")

            elif macd49 < 0:       # macd가 0보다 낮을때는 매도
                if op_mode49 == False:   # 매수 불가(False)일 경우 - 매도시도
                    # 보유수량 불러오기
                    krw_balance49 = upbit.get_balance(krw_coin49)
                    # 현재가 불러오기
                    price49 = pyupbit.get_current_price(krw_coin49)
                    # 보유코인 원화금액으로 계산하기
                    bp49 = price49 * krw_balance49

                    # 보유코인 원화금액 매도시도
                    if  bp49 > 10100:   # 보유코인 평가 금액이 10,100원 초과일때 - 매도시도
                        # 매도할 코인명 - krw_coin49, 매도할 코인수량 - krw_balance49
                        upbit.sell_market_order(krw_coin49, krw_balance49)

                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode49 = True

                        # 1초 딜레이
                        #time.sleep(1)
                        # 보유수량 불러오기
                        krw_balance49 = upbit.get_balance(krw_coin49)
                        # 코인 현재가 불러오기
                        price49 = pyupbit.get_current_price(krw_coin49)
                        # 보유코인 원화금액으로 계산하기
                        bp49 = price49 * krw_balance49

                        # 보유 및 매수 가능 출력.
                        print(f"[ 49. {krw_coin49} 매도완료. ]")
                        print(f"매도시간 : {now}  |  코인명 : {coin49}  |  현재가 = ￦{price49}  |  MACD = ￦{macd49}  |  보유수량 = {krw_balance49}  |  평가금액 = ￦{bp49}")
                        print(f"매수가능 : {op_mode49} - 가능")
                        print("")

                    else:   # 보유코인 평가 금액이 10,100원 이하일때
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode49 = True

                        print(f"[ 49. {krw_coin49} 보유코인이 없으므로 매도불가. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin49}")
                        print(f"매수가능 : {op_mode49} - 가능")
                        print("")

            # 1초 딜레이.
            time.sleep(1)
            ##### 49번 코인 매매 종료 #####
            #############################


            ###############################
            ##### 매매 : 50번코인 시작. #####

            ##### 코인보유현황
            # 보유수량 불러오기
            krw_balance50 = upbit.get_balance(krw_coin50)
            # 코인 현재가 불러오기
            price50 = pyupbit.get_current_price(krw_coin50)
            # 보유코인 원화금액으로 계산하기
            bp50 = price50 * krw_balance50
            # 코인 현황 출력.
            print(f"50. 코인명 : {coin50}  |  현재가 = ￦{price50}  |  보유수량 = {krw_balance50}  |  평가금액 = ￦{bp50}")
            # 코인 보유 유무
            if bp50 > 10100:
                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                op_mode50 = False

                # 보유 및 매수 가능 출력.
                print(f" 코인 보유 : 보유중  |  매수가능 - {op_mode50} - 매수불가")
                print("")
            else:
                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                op_mode50 = True


                # 보유 및 매수 가능 출력.
                print(f" 코인 보유 : 없음  |  매수가능 - {op_mode50} - 매수가능")
                print("")
            #time.sleep(1)


            # 코인 현재가 불러오기
            price50 = pyupbit.get_current_price(krw_coin50)

            # MACD 조회.
            #macd50 = get_macd(krw_coin50)
            # 거래량 동반한 MACD 조회.
            macd50 = get_acc_macd(krw_coin50)
            # 20일 이평선 조회.
            #macd50 = get_ma20(krw_coin50)

            # 매수가능금액 불러오기
            krw50 = upbit.get_balance("KRW")

            # MACD 조건문
            if macd50 >= 0:     # macd가 0보다 높을때는 매수
                if op_mode50 == True:    # 매수 가능(True)일 경우 - 매수시도
                    if krw50 > buy_krw:      # 매수가능금액 krw50 가 매수평균가 buy_krw 보다 클때
                        if krw50 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                            if buy_krw > 10100:     # 매수평균가 buy_krw 가 10,100원 초과일 경우 : 매수
                                # 매수금액은 매수평균가 buy_krw 로
                                upbit.buy_market_order(krw_coin50, buy_krw * 0.99)   # 매수가능금액에서 1%를 빼고

                                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                                op_mode50 = False

                                # 1초 딜레이
                                #time.sleep(1)
                                # 보유수량 불러오기
                                krw_balance50 = upbit.get_balance(krw_coin50)
                                # 코인 현재가 불러오기
                                price50 = pyupbit.get_current_price(krw_coin50)
                                # 보유코인 원화금액으로 계산하기
                                bp50 = price50 * krw_balance50

                                # 보유 및 매수 가능 출력.
                                print(f"[ 50. {krw_coin50} 매수완료. ]")
                                print(f"매수시간 : {now}  |  코인명 : {coin50}  |  현재가 = ￦{price50}  |  MACD = ￦{macd50}  |  보유수량 = {krw_balance50}  |  평가금액 = ￦{bp50}")
                                print(f"매수가능 : {op_mode50} - 불가")
                                print("")

                            else:
                                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                                op_mode50 = False

                                print(f"[ 50. {krw_coin50} 잔고부족으로 매수불가. ]")
                                print(f"현재시간 : {now}  |  코인명 : {coin50}")
                                print(f"매수가능 : {op_mode50} - 불가")
                                print("")

                        else:
                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode50 = False

                            print(f"[ 50. {krw_coin50} 잔고부족으로 매수불가. ]")
                            print(f"현재시간 : {now}  |  코인명 : {coin50}")
                            print(f"매수가능 : {op_mode50} - 불가")
                            print("")

                    elif krw50 <= buy_krw:   # 매수가능금액 krw50 가 매수평균가 buy_krw 보다 같거나 작을때
                        if krw50 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
                            # 매수금액은 매수가능금액인 krw50 로
                            upbit.buy_market_order(krw_coin50, krw50 * 0.99)   # 매수가능금액에서 1%를 빼고

                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode50 = False

                            # 1초 딜레이
                            #time.sleep(1)
                            # 보유수량 불러오기
                            krw_balance50 = upbit.get_balance(krw_coin50)
                            # 코인 현재가 불러오기
                            price50 = pyupbit.get_current_price(krw_coin50)
                            # 보유코인 원화금액으로 계산하기
                            bp50 = price50 * krw_balance50

                            # 보유 및 매수 가능 출력.
                            print(f"[ 50. {krw_coin50} 매수완료. ]")
                            print(f"매수시간 : {now}  |  코인명 : {coin50}  |  현재가 = ￦{price50}  |  MACD = ￦{macd50}  |  보유수량 = {krw_balance50}  |  평가금액 = ￦{bp50}")
                            print(f"매수가능 : {op_mode50} - 불가")
                            print("")

                        else:
                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                            op_mode50 = False

                            print(f"[ 50. {krw_coin50} 잔고부족으로 매수불가. ]")
                            print(f"현재시간 : {now}  |  코인명 : {coin50}")
                            print(f"매수가능 : {op_mode50} - 불가")
                            print("")

            elif macd50 < 0:       # macd가 0보다 낮을때는 매도
                if op_mode50 == False:   # 매수 불가(False)일 경우 - 매도시도
                    # 보유수량 불러오기
                    krw_balance50 = upbit.get_balance(krw_coin50)
                    # 현재가 불러오기
                    price50 = pyupbit.get_current_price(krw_coin50)
                    # 보유코인 원화금액으로 계산하기
                    bp50 = price50 * krw_balance50

                    # 보유코인 원화금액 매도시도
                    if  bp50 > 10100:   # 보유코인 평가 금액이 10,100원 초과일때 - 매도시도
                        # 매도할 코인명 - krw_coin50, 매도할 코인수량 - krw_balance50
                        upbit.sell_market_order(krw_coin50, krw_balance50)

                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode50 = True

                        # 1초 딜레이
                        #time.sleep(1)
                        # 보유수량 불러오기
                        krw_balance50 = upbit.get_balance(krw_coin50)
                        # 코인 현재가 불러오기
                        price50 = pyupbit.get_current_price(krw_coin50)
                        # 보유코인 원화금액으로 계산하기
                        bp50 = price50 * krw_balance50

                        # 보유 및 매수 가능 출력.
                        print(f"[ 50. {krw_coin50} 매도완료. ]")
                        print(f"매도시간 : {now}  |  코인명 : {coin50}  |  현재가 = ￦{price50}  |  MACD = ￦{macd50}  |  보유수량 = {krw_balance50}  |  평가금액 = ￦{bp50}")
                        print(f"매수가능 : {op_mode50} - 가능")
                        print("")

                    else:   # 보유코인 평가 금액이 10,100원 이하일때
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode50 = True

                        print(f"[ 50. {krw_coin50} 보유코인이 없으므로 매도불가. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin50}")
                        print(f"매수가능 : {op_mode50} - 가능")
                        print("")

            # 1초 딜레이.
            time.sleep(1)
            ##### 50번 코인 매매 종료 #####
            #############################


            ######################################################################################################################################################
            ######################################################################################################################################################
            ######################################################################################################################################################
            ######################################################################################################################################################
            ######################################################################################################################################################

            # 60초 딜레이.
            time.sleep(60)