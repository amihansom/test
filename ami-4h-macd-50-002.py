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
coin1 = "BTC" # 비트코인 - 그레이스케일
coin2 = "ETH" # 이더리움 - 그레이스케일
coin3 = "ADA" # 에이다
coin4 = "XRP" # 리플
coin5 = "DOT" # 폴카닷

coin6 = "DOGE" # 도지코인
coin7 = "LINK" # 체인링크 - 그레이스케일
coin8 = "LTC" # 라이트코인 - 그레이스케일
coin9 = "BCH" # 비트코인캐시 - 그레이스케일
coin10 = "ATOM" # 코스모스

coin11 = "XLM" # 스텔라루멘 - 그레이스케일
coin12 = "TRX" # 트론
coin13 = "ETC" # 이더리움클래식 - 그레이스케일
coin14 = "XTZ" # 테조스
coin15 = "VET" # 비체인

coin16 = "THETA" # 쎄타토큰
coin17 = "BCHA" # 비트코인캐시에이비씨
coin18 = "CRO" # 크립토닷컴체인
coin19 = "AXS" # 엑시인피니티
coin20 = "EOS" # 이오스

coin21 = "HBAR" # 헤데라해시그래프
coin22 = "IOTA" # 아이오타
coin23 = "NEO" # 네오
coin24 = "WAVES" # 웨이브
coin25 = "BSV" # 비트코인에스브이

coin26 = "BTT" # 비트토렌트
coin27 = "CHZ" # 칠리즈
coin28 = "STX" # 스택스
coin29 = "TFUEL" # 쎄타퓨엘
coin30 = "MANA" # 디센트럴랜드 - 그레이스케일

coin31 = "XEM" # 넴
coin32 = "OMG" # 오미세고
coin33 = "ENJ" # 엔진코인
coin34 = "IOST" # 아이오에스티
coin35 = "FLOW" # 플로우

coin36 = "ICX" # 아이콘
coin37 = "SRM" # 세럼
coin38 = "ZIL" # 질리카
coin39 = "BAT" # 베이직어텐션토큰 - 그레이스케일
coin40 = "QTUM" # 퀀텀

coin41 = "BTG" # 비트코인골드
coin42 = "ZRX" # 제로엑스
coin43 = "SC" # 시아코인
coin44 = "ONT" # 온톨로지
coin45 = "ANKR" # 앵커

coin46 = "SAND" # 샌드박스
coin47 = "KAVA" # 카바
coin48 = "GLM" # 골렘
coin49 = "SXP" # 스와이프
coin50 = "ORBS" # 오브스 - 오뽀가디언

##### 여기까지 매매 #####
##### 여기부터는 매도용 #####

coin51 = "LSK" # 리스크
coin52 = "WAXP" # 왁스
coin53 = "ELF" # 엘프
coin54 = "STORJ" # 스토리지
coin55 = "POLY" # 폴리매쓰

coin56 = "PUNDIX" # 펀디엑스
coin57 = "MED" # 메디블록
coin58 = "ARDR" # 아더
coin59 = "CVC" # 시빅
coin60 = "STMX" # 스톰엑스

coin61 = "STRAX" # 스트라티스
coin62 = "SNT" # 스테이터스네트워크토큰
coin63 = "KNC" # 카이버네트워크
coin64 = "ONG" # 온톨로지가스
coin65 = "HIVE" # 하이브

coin66 = "REP" # 어거
coin67 = "ARK" # 아크
coin68 = "STEEM" # 스팀
coin69 = "MTL" # 메탈
coin70 = "DAWN" # 던프로토콜

coin71 = "PLA" # 플레이댑
coin72 = "MVL" # 엠블
coin73 = "JST" # 저스트
coin74 = "POWR" # 파워렛저
coin75 = "STRK" # 스트라이크

coin76 = "BORA" # 보라
coin77 = "DKA" # 디카르고
coin78 = "IQ" # 에브리피디아
coin79 = "SSX" # 썸씽
coin80 = "QKC" # 쿼크체인

coin81 = "META" # 메타디움
coin82 = "LOOM" # 룸네트워크
coin83 = "MFT" # 메인프레임
coin84 = "GAS" # 가스
coin85 = "TT" # 썬더토큰

coin86= "UPP" # 센티넬프로토콜
coin87 = "CRE" # 캐리프로토콜
coin88 = "AERGO" # 아르고
coin89 = "MLK" # 밀크
coin90 = "HUNT" # 헌트

coin91 = "GRS" # 그로스톨코인
coin92 = "HUM" # 휴먼스케이프
coin93 = "RFR" # 리퍼리움
coin94 = "STPT" # 에스티피
coin95 = "AQT" # 알파쿼크

coin96 = "SBD" # 스팀달러
coin97 = "FCT2" # 피르마체인
coin98 = "MOC" # 모스코인
coin99 = "AHT" # 아하토큰
coin100 = "MBL" # 무비토큰

coin101 = "TON" # 톤
coin102 = "CBK" # 코박토큰


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

krw_coin51 = "KRW-" + coin51
krw_coin52 = "KRW-" + coin52
krw_coin53 = "KRW-" + coin53
krw_coin54 = "KRW-" + coin54
krw_coin55 = "KRW-" + coin55
krw_coin56 = "KRW-" + coin56
krw_coin57 = "KRW-" + coin57
krw_coin58 = "KRW-" + coin58
krw_coin59 = "KRW-" + coin59
krw_coin60 = "KRW-" + coin60

krw_coin61 = "KRW-" + coin61
krw_coin62 = "KRW-" + coin62
krw_coin63 = "KRW-" + coin63
krw_coin64 = "KRW-" + coin64
krw_coin65 = "KRW-" + coin65
krw_coin66 = "KRW-" + coin66
krw_coin67 = "KRW-" + coin67
krw_coin68 = "KRW-" + coin68
krw_coin69 = "KRW-" + coin69
krw_coin70 = "KRW-" + coin70

krw_coin71 = "KRW-" + coin71
krw_coin72 = "KRW-" + coin72
krw_coin73 = "KRW-" + coin73
krw_coin74 = "KRW-" + coin74
krw_coin75 = "KRW-" + coin75
krw_coin76 = "KRW-" + coin76
krw_coin77 = "KRW-" + coin77
krw_coin78 = "KRW-" + coin78
krw_coin79 = "KRW-" + coin79
krw_coin80 = "KRW-" + coin80

krw_coin81 = "KRW-" + coin81
krw_coin82 = "KRW-" + coin82
krw_coin83 = "KRW-" + coin83
krw_coin84 = "KRW-" + coin84
krw_coin85 = "KRW-" + coin85
krw_coin86 = "KRW-" + coin86
krw_coin87 = "KRW-" + coin87
krw_coin88 = "KRW-" + coin88
krw_coin89 = "KRW-" + coin89
krw_coin90 = "KRW-" + coin90

krw_coin91 = "KRW-" + coin91
krw_coin92 = "KRW-" + coin92
krw_coin93 = "KRW-" + coin93
krw_coin94 = "KRW-" + coin94
krw_coin95 = "KRW-" + coin95
krw_coin96 = "KRW-" + coin96
krw_coin97 = "KRW-" + coin97
krw_coin98 = "KRW-" + coin98
krw_coin99 = "KRW-" + coin99
krw_coin100 = "KRW-" + coin100

krw_coin101 = "KRW-" + coin101
krw_coin102 = "KRW-" + coin102



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


##### 51. 코인
# 보유수량 불러오기
krw_balance51 = upbit.get_balance(krw_coin51)
# 코인 현재가 불러오기
price51 = pyupbit.get_current_price(krw_coin51)
# 보유코인 원화금액으로 계산하기
bp51 = price51 * krw_balance51
# 코인 현황 출력.
print(f"51. 코인명 : {coin51}  |  현재가 = ￦{price51}  |  보유수량 = {krw_balance51}  |  평가금액 = ￦{bp51}")
# 코인 보유 유무
if bp51 > 10100:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode51 = False

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 보유중  |  매수가능 - {op_mode51} - 매수불가")
    print("")
else:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode51 = True

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 없음  |  매수가능 - {op_mode51} - 매수가능")
    print("")
time.sleep(1)


##### 52. 코인
# 보유수량 불러오기
krw_balance52 = upbit.get_balance(krw_coin52)
# 코인 현재가 불러오기
price52 = pyupbit.get_current_price(krw_coin52)
# 보유코인 원화금액으로 계산하기
bp52 = price52 * krw_balance52
# 코인 현황 출력.
print(f"52. 코인명 : {coin52}  |  현재가 = ￦{price52}  |  보유수량 = {krw_balance52}  |  평가금액 = ￦{bp52}")
# 코인 보유 유무
if bp52 > 10100:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode52 = False

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 보유중  |  매수가능 - {op_mode52} - 매수불가")
    print("")
else:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode52 = True

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 없음  |  매수가능 - {op_mode52} - 매수가능")
    print("")
time.sleep(1)


##### 53. 코인
# 보유수량 불러오기
krw_balance53 = upbit.get_balance(krw_coin53)
# 코인 현재가 불러오기
price53 = pyupbit.get_current_price(krw_coin53)
# 보유코인 원화금액으로 계산하기
bp53 = price53 * krw_balance53
# 코인 현황 출력.
print(f"53. 코인명 : {coin53}  |  현재가 = ￦{price53}  |  보유수량 = {krw_balance53}  |  평가금액 = ￦{bp53}")
# 코인 보유 유무
if bp53 > 10100:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode53 = False

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 보유중  |  매수가능 - {op_mode53} - 매수불가")
    print("")
else:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode53 = True

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 없음  |  매수가능 - {op_mode53} - 매수가능")
    print("")
time.sleep(1)


##### 54. 코인
# 보유수량 불러오기
krw_balance54 = upbit.get_balance(krw_coin54)
# 코인 현재가 불러오기
price54 = pyupbit.get_current_price(krw_coin54)
# 보유코인 원화금액으로 계산하기
bp54 = price54 * krw_balance54
# 코인 현황 출력.
print(f"54. 코인명 : {coin54}  |  현재가 = ￦{price54}  |  보유수량 = {krw_balance54}  |  평가금액 = ￦{bp54}")
# 코인 보유 유무
if bp54 > 10100:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode54 = False

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 보유중  |  매수가능 - {op_mode54} - 매수불가")
    print("")
else:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode54 = True

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 없음  |  매수가능 - {op_mode54} - 매수가능")
    print("")
time.sleep(1)


##### 53. 코인
# 보유수량 불러오기
krw_balance53 = upbit.get_balance(krw_coin53)
# 코인 현재가 불러오기
price53 = pyupbit.get_current_price(krw_coin53)
# 보유코인 원화금액으로 계산하기
bp53 = price53 * krw_balance53
# 코인 현황 출력.
print(f"53. 코인명 : {coin53}  |  현재가 = ￦{price53}  |  보유수량 = {krw_balance53}  |  평가금액 = ￦{bp53}")
# 코인 보유 유무
if bp53 > 10100:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode53 = False

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 보유중  |  매수가능 - {op_mode53} - 매수불가")
    print("")
else:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode53 = True

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 없음  |  매수가능 - {op_mode53} - 매수가능")
    print("")
time.sleep(1)


##### 55. 코인
# 보유수량 불러오기
krw_balance55 = upbit.get_balance(krw_coin55)
# 코인 현재가 불러오기
price55 = pyupbit.get_current_price(krw_coin55)
# 보유코인 원화금액으로 계산하기
bp55 = price55 * krw_balance55
# 코인 현황 출력.
print(f"55. 코인명 : {coin55}  |  현재가 = ￦{price55}  |  보유수량 = {krw_balance55}  |  평가금액 = ￦{bp55}")
# 코인 보유 유무
if bp55 > 10100:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode55 = False

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 보유중  |  매수가능 - {op_mode55} - 매수불가")
    print("")
else:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode55 = True

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 없음  |  매수가능 - {op_mode55} - 매수가능")
    print("")
time.sleep(1)


##### 56. 코인
# 보유수량 불러오기
krw_balance56 = upbit.get_balance(krw_coin56)
# 코인 현재가 불러오기
price56 = pyupbit.get_current_price(krw_coin56)
# 보유코인 원화금액으로 계산하기
bp56 = price56 * krw_balance56
# 코인 현황 출력.
print(f"56. 코인명 : {coin56}  |  현재가 = ￦{price56}  |  보유수량 = {krw_balance56}  |  평가금액 = ￦{bp56}")
# 코인 보유 유무
if bp56 > 10100:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode56 = False

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 보유중  |  매수가능 - {op_mode56} - 매수불가")
    print("")
else:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode56 = True

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 없음  |  매수가능 - {op_mode56} - 매수가능")
    print("")
time.sleep(1)


##### 57. 코인
# 보유수량 불러오기
krw_balance57 = upbit.get_balance(krw_coin57)
# 코인 현재가 불러오기
price57 = pyupbit.get_current_price(krw_coin57)
# 보유코인 원화금액으로 계산하기
bp57 = price57 * krw_balance57
# 코인 현황 출력.
print(f"57. 코인명 : {coin57}  |  현재가 = ￦{price57}  |  보유수량 = {krw_balance57}  |  평가금액 = ￦{bp57}")
# 코인 보유 유무
if bp57 > 10100:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode57 = False

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 보유중  |  매수가능 - {op_mode57} - 매수불가")
    print("")
else:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode57 = True

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 없음  |  매수가능 - {op_mode57} - 매수가능")
    print("")
time.sleep(1)


##### 58. 코인
# 보유수량 불러오기
krw_balance58 = upbit.get_balance(krw_coin58)
# 코인 현재가 불러오기
price58 = pyupbit.get_current_price(krw_coin58)
# 보유코인 원화금액으로 계산하기
bp58 = price58 * krw_balance58
# 코인 현황 출력.
print(f"58. 코인명 : {coin58}  |  현재가 = ￦{price58}  |  보유수량 = {krw_balance58}  |  평가금액 = ￦{bp58}")
# 코인 보유 유무
if bp58 > 10100:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode58 = False

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 보유중  |  매수가능 - {op_mode58} - 매수불가")
    print("")
else:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode58 = True

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 없음  |  매수가능 - {op_mode58} - 매수가능")
    print("")
time.sleep(1)


##### 59. 코인
# 보유수량 불러오기
krw_balance59 = upbit.get_balance(krw_coin59)
# 코인 현재가 불러오기
price59 = pyupbit.get_current_price(krw_coin59)
# 보유코인 원화금액으로 계산하기
bp59 = price59 * krw_balance59
# 코인 현황 출력.
print(f"59. 코인명 : {coin59}  |  현재가 = ￦{price59}  |  보유수량 = {krw_balance59}  |  평가금액 = ￦{bp59}")
# 코인 보유 유무
if bp59 > 10100:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode59 = False

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 보유중  |  매수가능 - {op_mode59} - 매수불가")
    print("")
else:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode59 = True

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 없음  |  매수가능 - {op_mode59} - 매수가능")
    print("")
time.sleep(1)


##### 60. 코인
# 보유수량 불러오기
krw_balance60 = upbit.get_balance(krw_coin60)
# 코인 현재가 불러오기
price60 = pyupbit.get_current_price(krw_coin60)
# 보유코인 원화금액으로 계산하기
bp60 = price60 * krw_balance60
# 코인 현황 출력.
print(f"60. 코인명 : {coin60}  |  현재가 = ￦{price60}  |  보유수량 = {krw_balance60}  |  평가금액 = ￦{bp60}")
# 코인 보유 유무
if bp60 > 10100:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode60 = False

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 보유중  |  매수가능 - {op_mode60} - 매수불가")
    print("")
else:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode60 = True

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 없음  |  매수가능 - {op_mode60} - 매수가능")
    print("")
time.sleep(1)


######################################################################################################################################################
######################################################################################################################################################
######################################################################################################################################################


##### 61. 코인
# 보유수량 불러오기
krw_balance61 = upbit.get_balance(krw_coin61)
# 코인 현재가 불러오기
price61 = pyupbit.get_current_price(krw_coin61)
# 보유코인 원화금액으로 계산하기
bp61 = price61 * krw_balance61
# 코인 현황 출력.
print(f"61. 코인명 : {coin61}  |  현재가 = ￦{price61}  |  보유수량 = {krw_balance61}  |  평가금액 = ￦{bp61}")
# 코인 보유 유무
if bp61 > 10100:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode61 = False

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 보유중  |  매수가능 - {op_mode61} - 매수불가")
    print("")
else:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode61 = True

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 없음  |  매수가능 - {op_mode61} - 매수가능")
    print("")
time.sleep(1)


##### 62. 코인
# 보유수량 불러오기
krw_balance62 = upbit.get_balance(krw_coin62)
# 코인 현재가 불러오기
price62 = pyupbit.get_current_price(krw_coin62)
# 보유코인 원화금액으로 계산하기
bp62 = price62 * krw_balance62
# 코인 현황 출력.
print(f"62. 코인명 : {coin62}  |  현재가 = ￦{price62}  |  보유수량 = {krw_balance62}  |  평가금액 = ￦{bp62}")
# 코인 보유 유무
if bp62 > 10100:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode62 = False

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 보유중  |  매수가능 - {op_mode62} - 매수불가")
    print("")
else:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode62 = True

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 없음  |  매수가능 - {op_mode62} - 매수가능")
    print("")
time.sleep(1)


##### 63. 코인
# 보유수량 불러오기
krw_balance63 = upbit.get_balance(krw_coin63)
# 코인 현재가 불러오기
price63 = pyupbit.get_current_price(krw_coin63)
# 보유코인 원화금액으로 계산하기
bp63 = price63 * krw_balance63
# 코인 현황 출력.
print(f"63. 코인명 : {coin63}  |  현재가 = ￦{price63}  |  보유수량 = {krw_balance63}  |  평가금액 = ￦{bp63}")
# 코인 보유 유무
if bp63 > 10100:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode63 = False

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 보유중  |  매수가능 - {op_mode63} - 매수불가")
    print("")
else:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode63 = True

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 없음  |  매수가능 - {op_mode63} - 매수가능")
    print("")
time.sleep(1)


##### 64. 코인
# 보유수량 불러오기
krw_balance64 = upbit.get_balance(krw_coin64)
# 코인 현재가 불러오기
price64 = pyupbit.get_current_price(krw_coin64)
# 보유코인 원화금액으로 계산하기
bp64 = price64 * krw_balance64
# 코인 현황 출력.
print(f"64. 코인명 : {coin64}  |  현재가 = ￦{price64}  |  보유수량 = {krw_balance64}  |  평가금액 = ￦{bp64}")
# 코인 보유 유무
if bp64 > 10100:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode64 = False

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 보유중  |  매수가능 - {op_mode64} - 매수불가")
    print("")
else:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode64 = True

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 없음  |  매수가능 - {op_mode64} - 매수가능")
    print("")
time.sleep(1)


##### 65. 코인
# 보유수량 불러오기
krw_balance65 = upbit.get_balance(krw_coin65)
# 코인 현재가 불러오기
price65 = pyupbit.get_current_price(krw_coin65)
# 보유코인 원화금액으로 계산하기
bp65 = price65 * krw_balance65
# 코인 현황 출력.
print(f"65. 코인명 : {coin65}  |  현재가 = ￦{price65}  |  보유수량 = {krw_balance65}  |  평가금액 = ￦{bp65}")
# 코인 보유 유무
if bp65 > 10100:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode65 = False

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 보유중  |  매수가능 - {op_mode65} - 매수불가")
    print("")
else:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode65 = True

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 없음  |  매수가능 - {op_mode65} - 매수가능")
    print("")
time.sleep(1)


##### 66. 코인
# 보유수량 불러오기
krw_balance66 = upbit.get_balance(krw_coin66)
# 코인 현재가 불러오기
price66 = pyupbit.get_current_price(krw_coin66)
# 보유코인 원화금액으로 계산하기
bp66 = price66 * krw_balance66
# 코인 현황 출력.
print(f"66. 코인명 : {coin66}  |  현재가 = ￦{price66}  |  보유수량 = {krw_balance66}  |  평가금액 = ￦{bp66}")
# 코인 보유 유무
if bp66 > 10100:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode66 = False

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 보유중  |  매수가능 - {op_mode66} - 매수불가")
    print("")
else:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode66 = True

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 없음  |  매수가능 - {op_mode66} - 매수가능")
    print("")
time.sleep(1)


##### 67. 코인
# 보유수량 불러오기
krw_balance67 = upbit.get_balance(krw_coin67)
# 코인 현재가 불러오기
price67 = pyupbit.get_current_price(krw_coin67)
# 보유코인 원화금액으로 계산하기
bp67 = price67 * krw_balance67
# 코인 현황 출력.
print(f"67. 코인명 : {coin67}  |  현재가 = ￦{price67}  |  보유수량 = {krw_balance67}  |  평가금액 = ￦{bp67}")
# 코인 보유 유무
if bp67 > 10100:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode67 = False

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 보유중  |  매수가능 - {op_mode67} - 매수불가")
    print("")
else:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode67 = True

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 없음  |  매수가능 - {op_mode67} - 매수가능")
    print("")
time.sleep(1)


##### 68. 코인
# 보유수량 불러오기
krw_balance68 = upbit.get_balance(krw_coin68)
# 코인 현재가 불러오기
price68 = pyupbit.get_current_price(krw_coin68)
# 보유코인 원화금액으로 계산하기
bp68 = price68 * krw_balance68
# 코인 현황 출력.
print(f"68. 코인명 : {coin68}  |  현재가 = ￦{price68}  |  보유수량 = {krw_balance68}  |  평가금액 = ￦{bp68}")
# 코인 보유 유무
if bp68 > 10100:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode68 = False

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 보유중  |  매수가능 - {op_mode68} - 매수불가")
    print("")
else:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode68 = True

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 없음  |  매수가능 - {op_mode68} - 매수가능")
    print("")
time.sleep(1)


##### 69. 코인
# 보유수량 불러오기
krw_balance69 = upbit.get_balance(krw_coin69)
# 코인 현재가 불러오기
price69 = pyupbit.get_current_price(krw_coin69)
# 보유코인 원화금액으로 계산하기
bp69 = price69 * krw_balance69
# 코인 현황 출력.
print(f"69. 코인명 : {coin69}  |  현재가 = ￦{price69}  |  보유수량 = {krw_balance69}  |  평가금액 = ￦{bp69}")
# 코인 보유 유무
if bp69 > 10100:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode69 = False

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 보유중  |  매수가능 - {op_mode69} - 매수불가")
    print("")
else:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode69 = True

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 없음  |  매수가능 - {op_mode69} - 매수가능")
    print("")
time.sleep(1)


##### 70. 코인
# 보유수량 불러오기
krw_balance70 = upbit.get_balance(krw_coin70)
# 코인 현재가 불러오기
price70 = pyupbit.get_current_price(krw_coin70)
# 보유코인 원화금액으로 계산하기
bp70 = price70 * krw_balance70
# 코인 현황 출력.
print(f"70. 코인명 : {coin70}  |  현재가 = ￦{price70}  |  보유수량 = {krw_balance70}  |  평가금액 = ￦{bp70}")
# 코인 보유 유무
if bp70 > 10100:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode70 = False

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 보유중  |  매수가능 - {op_mode70} - 매수불가")
    print("")
else:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode70 = True

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 없음  |  매수가능 - {op_mode70} - 매수가능")
    print("")
time.sleep(1)


######################################################################################################################################################
######################################################################################################################################################
######################################################################################################################################################


##### 71. 코인
# 보유수량 불러오기
krw_balance71 = upbit.get_balance(krw_coin71)
# 코인 현재가 불러오기
price71 = pyupbit.get_current_price(krw_coin71)
# 보유코인 원화금액으로 계산하기
bp71 = price71 * krw_balance71
# 코인 현황 출력.
print(f"71. 코인명 : {coin71}  |  현재가 = ￦{price71}  |  보유수량 = {krw_balance71}  |  평가금액 = ￦{bp71}")
# 코인 보유 유무
if bp71 > 10100:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode71 = False

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 보유중  |  매수가능 - {op_mode71} - 매수불가")
    print("")
else:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode71 = True

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 없음  |  매수가능 - {op_mode71} - 매수가능")
    print("")
time.sleep(1)


##### 72. 코인
# 보유수량 불러오기
krw_balance72 = upbit.get_balance(krw_coin72)
# 코인 현재가 불러오기
price72 = pyupbit.get_current_price(krw_coin72)
# 보유코인 원화금액으로 계산하기
bp72 = price72 * krw_balance72
# 코인 현황 출력.
print(f"72. 코인명 : {coin72}  |  현재가 = ￦{price72}  |  보유수량 = {krw_balance72}  |  평가금액 = ￦{bp72}")
# 코인 보유 유무
if bp72 > 10100:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode72 = False

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 보유중  |  매수가능 - {op_mode72} - 매수불가")
    print("")
else:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode72 = True

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 없음  |  매수가능 - {op_mode72} - 매수가능")
    print("")
time.sleep(1)


##### 73. 코인
# 보유수량 불러오기
krw_balance73 = upbit.get_balance(krw_coin73)
# 코인 현재가 불러오기
price73 = pyupbit.get_current_price(krw_coin73)
# 보유코인 원화금액으로 계산하기
bp73 = price73 * krw_balance73
# 코인 현황 출력.
print(f"73. 코인명 : {coin73}  |  현재가 = ￦{price73}  |  보유수량 = {krw_balance73}  |  평가금액 = ￦{bp73}")
# 코인 보유 유무
if bp73 > 10100:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode73 = False

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 보유중  |  매수가능 - {op_mode73} - 매수불가")
    print("")
else:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode73 = True

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 없음  |  매수가능 - {op_mode73} - 매수가능")
    print("")
time.sleep(1)


##### 74. 코인
# 보유수량 불러오기
krw_balance74 = upbit.get_balance(krw_coin74)
# 코인 현재가 불러오기
price74 = pyupbit.get_current_price(krw_coin74)
# 보유코인 원화금액으로 계산하기
bp74 = price74 * krw_balance74
# 코인 현황 출력.
print(f"74. 코인명 : {coin74}  |  현재가 = ￦{price74}  |  보유수량 = {krw_balance74}  |  평가금액 = ￦{bp74}")
# 코인 보유 유무
if bp74 > 10100:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode74 = False

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 보유중  |  매수가능 - {op_mode74} - 매수불가")
    print("")
else:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode74 = True

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 없음  |  매수가능 - {op_mode74} - 매수가능")
    print("")
time.sleep(1)


##### 75. 코인
# 보유수량 불러오기
krw_balance75 = upbit.get_balance(krw_coin75)
# 코인 현재가 불러오기
price75 = pyupbit.get_current_price(krw_coin75)
# 보유코인 원화금액으로 계산하기
bp75 = price75 * krw_balance75
# 코인 현황 출력.
print(f"75. 코인명 : {coin75}  |  현재가 = ￦{price75}  |  보유수량 = {krw_balance75}  |  평가금액 = ￦{bp75}")
# 코인 보유 유무
if bp75 > 10100:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode75 = False

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 보유중  |  매수가능 - {op_mode75} - 매수불가")
    print("")
else:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode75 = True

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 없음  |  매수가능 - {op_mode75} - 매수가능")
    print("")
time.sleep(1)


##### 76. 코인
# 보유수량 불러오기
krw_balance76 = upbit.get_balance(krw_coin76)
# 코인 현재가 불러오기
price76 = pyupbit.get_current_price(krw_coin76)
# 보유코인 원화금액으로 계산하기
bp76 = price76 * krw_balance76
# 코인 현황 출력.
print(f"76. 코인명 : {coin76}  |  현재가 = ￦{price76}  |  보유수량 = {krw_balance76}  |  평가금액 = ￦{bp76}")
# 코인 보유 유무
if bp76 > 10100:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode76 = False

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 보유중  |  매수가능 - {op_mode76} - 매수불가")
    print("")
else:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode76 = True

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 없음  |  매수가능 - {op_mode76} - 매수가능")
    print("")
time.sleep(1)


##### 77. 코인
# 보유수량 불러오기
krw_balance77 = upbit.get_balance(krw_coin77)
# 코인 현재가 불러오기
price77 = pyupbit.get_current_price(krw_coin77)
# 보유코인 원화금액으로 계산하기
bp77 = price77 * krw_balance77
# 코인 현황 출력.
print(f"77. 코인명 : {coin77}  |  현재가 = ￦{price77}  |  보유수량 = {krw_balance77}  |  평가금액 = ￦{bp77}")
# 코인 보유 유무
if bp77 > 10100:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode77 = False

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 보유중  |  매수가능 - {op_mode77} - 매수불가")
    print("")
else:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode77 = True

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 없음  |  매수가능 - {op_mode77} - 매수가능")
    print("")
time.sleep(1)


##### 78. 코인
# 보유수량 불러오기
krw_balance78 = upbit.get_balance(krw_coin78)
# 코인 현재가 불러오기
price78 = pyupbit.get_current_price(krw_coin78)
# 보유코인 원화금액으로 계산하기
bp78 = price78 * krw_balance78
# 코인 현황 출력.
print(f"78. 코인명 : {coin78}  |  현재가 = ￦{price78}  |  보유수량 = {krw_balance78}  |  평가금액 = ￦{bp78}")
# 코인 보유 유무
if bp78 > 10100:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode78 = False

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 보유중  |  매수가능 - {op_mode78} - 매수불가")
    print("")
else:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode78 = True

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 없음  |  매수가능 - {op_mode78} - 매수가능")
    print("")
time.sleep(1)


##### 79. 코인
# 보유수량 불러오기
krw_balance79 = upbit.get_balance(krw_coin79)
# 코인 현재가 불러오기
price79 = pyupbit.get_current_price(krw_coin79)
# 보유코인 원화금액으로 계산하기
bp79 = price79 * krw_balance79
# 코인 현황 출력.
print(f"79. 코인명 : {coin79}  |  현재가 = ￦{price79}  |  보유수량 = {krw_balance79}  |  평가금액 = ￦{bp79}")
# 코인 보유 유무
if bp79 > 10100:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode79 = False

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 보유중  |  매수가능 - {op_mode79} - 매수불가")
    print("")
else:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode79 = True

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 없음  |  매수가능 - {op_mode79} - 매수가능")
    print("")
time.sleep(1)


##### 80. 코인
# 보유수량 불러오기
krw_balance80 = upbit.get_balance(krw_coin80)
# 코인 현재가 불러오기
price80 = pyupbit.get_current_price(krw_coin80)
# 보유코인 원화금액으로 계산하기
bp80 = price80 * krw_balance80
# 코인 현황 출력.
print(f"80. 코인명 : {coin80}  |  현재가 = ￦{price80}  |  보유수량 = {krw_balance80}  |  평가금액 = ￦{bp80}")
# 코인 보유 유무
if bp80 > 10100:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode80 = False

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 보유중  |  매수가능 - {op_mode80} - 매수불가")
    print("")
else:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode80 = True

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 없음  |  매수가능 - {op_mode80} - 매수가능")
    print("")
time.sleep(1)


######################################################################################################################################################
######################################################################################################################################################
######################################################################################################################################################


##### 81. 코인
# 보유수량 불러오기
krw_balance81 = upbit.get_balance(krw_coin81)
# 코인 현재가 불러오기
price81 = pyupbit.get_current_price(krw_coin81)
# 보유코인 원화금액으로 계산하기
bp81 = price81 * krw_balance81
# 코인 현황 출력.
print(f"81. 코인명 : {coin81}  |  현재가 = ￦{price81}  |  보유수량 = {krw_balance81}  |  평가금액 = ￦{bp81}")
# 코인 보유 유무
if bp81 > 10100:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode81 = False

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 보유중  |  매수가능 - {op_mode81} - 매수불가")
    print("")
else:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode81 = True

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 없음  |  매수가능 - {op_mode81} - 매수가능")
    print("")
time.sleep(1)


##### 82. 코인
# 보유수량 불러오기
krw_balance82 = upbit.get_balance(krw_coin82)
# 코인 현재가 불러오기
price82 = pyupbit.get_current_price(krw_coin82)
# 보유코인 원화금액으로 계산하기
bp82 = price82 * krw_balance82
# 코인 현황 출력.
print(f"82. 코인명 : {coin82}  |  현재가 = ￦{price82}  |  보유수량 = {krw_balance82}  |  평가금액 = ￦{bp82}")
# 코인 보유 유무
if bp82 > 10100:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode82 = False

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 보유중  |  매수가능 - {op_mode82} - 매수불가")
    print("")
else:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode82 = True

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 없음  |  매수가능 - {op_mode82} - 매수가능")
    print("")
time.sleep(1)


##### 83. 코인
# 보유수량 불러오기
krw_balance83 = upbit.get_balance(krw_coin83)
# 코인 현재가 불러오기
price83 = pyupbit.get_current_price(krw_coin83)
# 보유코인 원화금액으로 계산하기
bp83 = price83 * krw_balance83
# 코인 현황 출력.
print(f"83. 코인명 : {coin83}  |  현재가 = ￦{price83}  |  보유수량 = {krw_balance83}  |  평가금액 = ￦{bp83}")
# 코인 보유 유무
if bp83 > 10100:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode83 = False

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 보유중  |  매수가능 - {op_mode83} - 매수불가")
    print("")
else:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode83 = True

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 없음  |  매수가능 - {op_mode83} - 매수가능")
    print("")
time.sleep(1)


##### 84. 코인
# 보유수량 불러오기
krw_balance84 = upbit.get_balance(krw_coin84)
# 코인 현재가 불러오기
price84 = pyupbit.get_current_price(krw_coin84)
# 보유코인 원화금액으로 계산하기
bp84 = price84 * krw_balance84
# 코인 현황 출력.
print(f"84. 코인명 : {coin84}  |  현재가 = ￦{price84}  |  보유수량 = {krw_balance84}  |  평가금액 = ￦{bp84}")
# 코인 보유 유무
if bp84 > 10100:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode84 = False

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 보유중  |  매수가능 - {op_mode84} - 매수불가")
    print("")
else:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode84 = True

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 없음  |  매수가능 - {op_mode84} - 매수가능")
    print("")
time.sleep(1)


##### 85. 코인
# 보유수량 불러오기
krw_balance85 = upbit.get_balance(krw_coin85)
# 코인 현재가 불러오기
price85 = pyupbit.get_current_price(krw_coin85)
# 보유코인 원화금액으로 계산하기
bp85 = price85 * krw_balance85
# 코인 현황 출력.
print(f"85. 코인명 : {coin85}  |  현재가 = ￦{price85}  |  보유수량 = {krw_balance85}  |  평가금액 = ￦{bp85}")
# 코인 보유 유무
if bp85 > 10100:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode85 = False

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 보유중  |  매수가능 - {op_mode85} - 매수불가")
    print("")
else:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode85 = True

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 없음  |  매수가능 - {op_mode85} - 매수가능")
    print("")
time.sleep(1)


##### 86. 코인
# 보유수량 불러오기
krw_balance86 = upbit.get_balance(krw_coin86)
# 코인 현재가 불러오기
price86 = pyupbit.get_current_price(krw_coin86)
# 보유코인 원화금액으로 계산하기
bp86 = price86 * krw_balance86
# 코인 현황 출력.
print(f"86. 코인명 : {coin86}  |  현재가 = ￦{price86}  |  보유수량 = {krw_balance86}  |  평가금액 = ￦{bp86}")
# 코인 보유 유무
if bp86 > 10100:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode86 = False

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 보유중  |  매수가능 - {op_mode86} - 매수불가")
    print("")
else:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode86 = True

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 없음  |  매수가능 - {op_mode86} - 매수가능")
    print("")
time.sleep(1)


##### 87. 코인
# 보유수량 불러오기
krw_balance87 = upbit.get_balance(krw_coin87)
# 코인 현재가 불러오기
price87 = pyupbit.get_current_price(krw_coin87)
# 보유코인 원화금액으로 계산하기
bp87 = price87 * krw_balance87
# 코인 현황 출력.
print(f"87. 코인명 : {coin87}  |  현재가 = ￦{price87}  |  보유수량 = {krw_balance87}  |  평가금액 = ￦{bp87}")
# 코인 보유 유무
if bp87 > 10100:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode87 = False

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 보유중  |  매수가능 - {op_mode87} - 매수불가")
    print("")
else:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode87 = True

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 없음  |  매수가능 - {op_mode87} - 매수가능")
    print("")
time.sleep(1)


##### 88. 코인
# 보유수량 불러오기
krw_balance88 = upbit.get_balance(krw_coin88)
# 코인 현재가 불러오기
price88 = pyupbit.get_current_price(krw_coin88)
# 보유코인 원화금액으로 계산하기
bp88 = price88 * krw_balance88
# 코인 현황 출력.
print(f"88. 코인명 : {coin88}  |  현재가 = ￦{price88}  |  보유수량 = {krw_balance88}  |  평가금액 = ￦{bp88}")
# 코인 보유 유무
if bp88 > 10100:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode88 = False

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 보유중  |  매수가능 - {op_mode88} - 매수불가")
    print("")
else:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode88 = True

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 없음  |  매수가능 - {op_mode88} - 매수가능")
    print("")
time.sleep(1)


##### 89. 코인
# 보유수량 불러오기
krw_balance89 = upbit.get_balance(krw_coin89)
# 코인 현재가 불러오기
price89 = pyupbit.get_current_price(krw_coin89)
# 보유코인 원화금액으로 계산하기
bp89 = price89 * krw_balance89
# 코인 현황 출력.
print(f"89. 코인명 : {coin89}  |  현재가 = ￦{price89}  |  보유수량 = {krw_balance89}  |  평가금액 = ￦{bp89}")
# 코인 보유 유무
if bp89 > 10100:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode89 = False

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 보유중  |  매수가능 - {op_mode89} - 매수불가")
    print("")
else:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode89 = True

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 없음  |  매수가능 - {op_mode89} - 매수가능")
    print("")
time.sleep(1)


##### 90. 코인
# 보유수량 불러오기
krw_balance90 = upbit.get_balance(krw_coin90)
# 코인 현재가 불러오기
price90 = pyupbit.get_current_price(krw_coin90)
# 보유코인 원화금액으로 계산하기
bp90 = price90 * krw_balance90
# 코인 현황 출력.
print(f"90. 코인명 : {coin90}  |  현재가 = ￦{price90}  |  보유수량 = {krw_balance90}  |  평가금액 = ￦{bp90}")
# 코인 보유 유무
if bp90 > 10100:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode90 = False

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 보유중  |  매수가능 - {op_mode90} - 매수불가")
    print("")
else:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode90 = True

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 없음  |  매수가능 - {op_mode90} - 매수가능")
    print("")
time.sleep(1)


######################################################################################################################################################
######################################################################################################################################################
######################################################################################################################################################


##### 91. 코인
# 보유수량 불러오기
krw_balance91 = upbit.get_balance(krw_coin91)
# 코인 현재가 불러오기
price91 = pyupbit.get_current_price(krw_coin91)
# 보유코인 원화금액으로 계산하기
bp91 = price91 * krw_balance91
# 코인 현황 출력.
print(f"91. 코인명 : {coin91}  |  현재가 = ￦{price91}  |  보유수량 = {krw_balance91}  |  평가금액 = ￦{bp91}")
# 코인 보유 유무
if bp91 > 10100:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode91 = False

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 보유중  |  매수가능 - {op_mode91} - 매수불가")
    print("")
else:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode91 = True

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 없음  |  매수가능 - {op_mode91} - 매수가능")
    print("")
time.sleep(1)


##### 92. 코인
# 보유수량 불러오기
krw_balance92 = upbit.get_balance(krw_coin92)
# 코인 현재가 불러오기
price92 = pyupbit.get_current_price(krw_coin92)
# 보유코인 원화금액으로 계산하기
bp92 = price92 * krw_balance92
# 코인 현황 출력.
print(f"92. 코인명 : {coin92}  |  현재가 = ￦{price92}  |  보유수량 = {krw_balance92}  |  평가금액 = ￦{bp92}")
# 코인 보유 유무
if bp92 > 10100:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode92 = False

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 보유중  |  매수가능 - {op_mode92} - 매수불가")
    print("")
else:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode92 = True

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 없음  |  매수가능 - {op_mode92} - 매수가능")
    print("")
time.sleep(1)


##### 93. 코인
# 보유수량 불러오기
krw_balance93 = upbit.get_balance(krw_coin93)
# 코인 현재가 불러오기
price93 = pyupbit.get_current_price(krw_coin93)
# 보유코인 원화금액으로 계산하기
bp93 = price93 * krw_balance93
# 코인 현황 출력.
print(f"93. 코인명 : {coin93}  |  현재가 = ￦{price93}  |  보유수량 = {krw_balance93}  |  평가금액 = ￦{bp93}")
# 코인 보유 유무
if bp93 > 10100:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode93 = False

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 보유중  |  매수가능 - {op_mode93} - 매수불가")
    print("")
else:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode93 = True

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 없음  |  매수가능 - {op_mode93} - 매수가능")
    print("")
time.sleep(1)


##### 94. 코인
# 보유수량 불러오기
krw_balance94 = upbit.get_balance(krw_coin94)
# 코인 현재가 불러오기
price94 = pyupbit.get_current_price(krw_coin94)
# 보유코인 원화금액으로 계산하기
bp94 = price94 * krw_balance94
# 코인 현황 출력.
print(f"94. 코인명 : {coin94}  |  현재가 = ￦{price94}  |  보유수량 = {krw_balance94}  |  평가금액 = ￦{bp94}")
# 코인 보유 유무
if bp94 > 10100:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode94 = False

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 보유중  |  매수가능 - {op_mode94} - 매수불가")
    print("")
else:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode94 = True

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 없음  |  매수가능 - {op_mode94} - 매수가능")
    print("")
time.sleep(1)


##### 95. 코인
# 보유수량 불러오기
krw_balance95 = upbit.get_balance(krw_coin95)
# 코인 현재가 불러오기
price95 = pyupbit.get_current_price(krw_coin95)
# 보유코인 원화금액으로 계산하기
bp95 = price95 * krw_balance95
# 코인 현황 출력.
print(f"95. 코인명 : {coin95}  |  현재가 = ￦{price95}  |  보유수량 = {krw_balance95}  |  평가금액 = ￦{bp95}")
# 코인 보유 유무
if bp95 > 10100:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode95 = False

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 보유중  |  매수가능 - {op_mode95} - 매수불가")
    print("")
else:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode95 = True

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 없음  |  매수가능 - {op_mode95} - 매수가능")
    print("")
time.sleep(1)


##### 96. 코인
# 보유수량 불러오기
krw_balance96 = upbit.get_balance(krw_coin96)
# 코인 현재가 불러오기
price96 = pyupbit.get_current_price(krw_coin96)
# 보유코인 원화금액으로 계산하기
bp96 = price96 * krw_balance96
# 코인 현황 출력.
print(f"96. 코인명 : {coin96}  |  현재가 = ￦{price96}  |  보유수량 = {krw_balance96}  |  평가금액 = ￦{bp96}")
# 코인 보유 유무
if bp96 > 10100:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode96 = False

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 보유중  |  매수가능 - {op_mode96} - 매수불가")
    print("")
else:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode96 = True

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 없음  |  매수가능 - {op_mode96} - 매수가능")
    print("")
time.sleep(1)


##### 97. 코인
# 보유수량 불러오기
krw_balance97 = upbit.get_balance(krw_coin97)
# 코인 현재가 불러오기
price97 = pyupbit.get_current_price(krw_coin97)
# 보유코인 원화금액으로 계산하기
bp97 = price97 * krw_balance97
# 코인 현황 출력.
print(f"97. 코인명 : {coin97}  |  현재가 = ￦{price97}  |  보유수량 = {krw_balance97}  |  평가금액 = ￦{bp97}")
# 코인 보유 유무
if bp97 > 10100:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode97 = False

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 보유중  |  매수가능 - {op_mode97} - 매수불가")
    print("")
else:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode97 = True

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 없음  |  매수가능 - {op_mode97} - 매수가능")
    print("")
time.sleep(1)


##### 98. 코인
# 보유수량 불러오기
krw_balance98 = upbit.get_balance(krw_coin98)
# 코인 현재가 불러오기
price98 = pyupbit.get_current_price(krw_coin98)
# 보유코인 원화금액으로 계산하기
bp98 = price98 * krw_balance98
# 코인 현황 출력.
print(f"98. 코인명 : {coin98}  |  현재가 = ￦{price98}  |  보유수량 = {krw_balance98}  |  평가금액 = ￦{bp98}")
# 코인 보유 유무
if bp98 > 10100:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode98 = False

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 보유중  |  매수가능 - {op_mode98} - 매수불가")
    print("")
else:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode98 = True

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 없음  |  매수가능 - {op_mode98} - 매수가능")
    print("")
time.sleep(1)


##### 99. 코인
# 보유수량 불러오기
krw_balance99 = upbit.get_balance(krw_coin99)
# 코인 현재가 불러오기
price99 = pyupbit.get_current_price(krw_coin99)
# 보유코인 원화금액으로 계산하기
bp99 = price99 * krw_balance99
# 코인 현황 출력.
print(f"99. 코인명 : {coin99}  |  현재가 = ￦{price99}  |  보유수량 = {krw_balance99}  |  평가금액 = ￦{bp99}")
# 코인 보유 유무
if bp99 > 10100:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode99 = False

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 보유중  |  매수가능 - {op_mode99} - 매수불가")
    print("")
else:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode99 = True

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 없음  |  매수가능 - {op_mode99} - 매수가능")
    print("")
time.sleep(1)


##### 100. 코인
# 보유수량 불러오기
krw_balance100 = upbit.get_balance(krw_coin100)
# 코인 현재가 불러오기
price100 = pyupbit.get_current_price(krw_coin100)
# 보유코인 원화금액으로 계산하기
bp100 = price100 * krw_balance100
# 코인 현황 출력.
print(f"100. 코인명 : {coin100}  |  현재가 = ￦{price100}  |  보유수량 = {krw_balance100}  |  평가금액 = ￦{bp100}")
# 코인 보유 유무
if bp100 > 10100:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode100 = False

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 보유중  |  매수가능 - {op_mode100} - 매수불가")
    print("")
else:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode100 = True

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 없음  |  매수가능 - {op_mode100} - 매수가능")
    print("")
time.sleep(1)


######################################################################################################################################################
######################################################################################################################################################
######################################################################################################################################################


##### 101. 코인
# 보유수량 불러오기
krw_balance101 = upbit.get_balance(krw_coin101)
# 코인 현재가 불러오기
price101 = pyupbit.get_current_price(krw_coin101)
# 보유코인 원화금액으로 계산하기
bp101 = price101 * krw_balance101
# 코인 현황 출력.
print(f"101. 코인명 : {coin101}  |  현재가 = ￦{price101}  |  보유수량 = {krw_balance101}  |  평가금액 = ￦{bp101}")
# 코인 보유 유무
if bp101 > 10100:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode101 = False

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 보유중  |  매수가능 - {op_mode101} - 매수불가")
    print("")
else:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode101 = True

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 없음  |  매수가능 - {op_mode101} - 매수가능")
    print("")
time.sleep(1)


##### 102. 코인
# 보유수량 불러오기
krw_balance102 = upbit.get_balance(krw_coin102)
# 코인 현재가 불러오기
price102 = pyupbit.get_current_price(krw_coin102)
# 보유코인 원화금액으로 계산하기
bp102 = price102 * krw_balance102
# 코인 현황 출력.
print(f"102. 코인명 : {coin102}  |  현재가 = ￦{price102}  |  보유수량 = {krw_balance102}  |  평가금액 = ￦{bp102}")
# 코인 보유 유무
if bp102 > 10100:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode102 = False

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 보유중  |  매수가능 - {op_mode102} - 매수불가")
    print("")
else:
    # 금일 코인 매수 가능 - 가능 = True , 불가 = False
    op_mode102 = True

    # 보유 및 매수 가능 출력.
    print(f" 코인 보유 : 없음  |  매수가능 - {op_mode102} - 매수가능")
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
            print(f"* 현재시간 : {now}")
            print()
            
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


            ###############################
            ##### 매매 : 51번코인 시작. #####

            ##### 코인보유현황
            # 보유수량 불러오기
            krw_balance51 = upbit.get_balance(krw_coin51)
            # 코인 현재가 불러오기
            price51 = pyupbit.get_current_price(krw_coin51)
            # 보유코인 원화금액으로 계산하기
            bp51 = price51 * krw_balance51
            # 코인 현황 출력.
            print(f"51. 코인명 : {coin51}  |  현재가 = ￦{price51}  |  보유수량 = {krw_balance51}  |  평가금액 = ￦{bp51}")
            # 코인 보유 유무
            if bp51 > 10100:
                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                op_mode51 = False

                # 보유 및 매수 가능 출력.
                print(f" 코인 보유 : 보유중  |  매수가능 - {op_mode51} - 매수불가")
                print("")
            else:
                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                op_mode51 = True

                # 보유 및 매수 가능 출력.
                print(f" 코인 보유 : 없음  |  매수가능 - {op_mode51} - 매수가능")
                print("")
            #time.sleep(1)


            # 코인 현재가 불러오기
            price51 = pyupbit.get_current_price(krw_coin51)

            # MACD 조회.
            #macd51 = get_macd(krw_coin51)
            # 거래량 동반한 MACD 조회.
            macd51 = get_acc_macd(krw_coin51)
            # 20일 이평선 조회.
            #macd51 = get_ma20(krw_coin51)

            # 매수가능금액 불러오기
            krw51 = upbit.get_balance("KRW")

            # MACD 조건문
#            if macd51 >= 0:     # macd가 0보다 높을때는 매수
#                if op_mode51 == True:    # 매수 가능(True)일 경우 - 매수시도
#                    if krw51 > buy_krw:      # 매수가능금액 krw51 가 매수평균가 buy_krw 보다 클때
#                        if krw51 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
#                            if buy_krw > 10100:     # 매수평균가 buy_krw 가 10,100원 초과일 경우 : 매수
#                                # 매수금액은 매수평균가 buy_krw 로
#                                upbit.buy_market_order(krw_coin51, buy_krw * 0.99)   # 매수가능금액에서 1%를 빼고
#
#                                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
#                                op_mode51 = False
#
#                                # 1초 딜레이
#                                time.sleep(1)
#                                # 보유수량 불러오기
#                                krw_balance51 = upbit.get_balance(krw_coin51)
#                                # 코인 현재가 불러오기
#                                price51 = pyupbit.get_current_price(krw_coin51)
#                                # 보유코인 원화금액으로 계산하기
#                                bp51 = price51 * krw_balance51
#
#                                # 보유 및 매수 가능 출력.
#                                print(f"[ 51. {krw_coin51} 매수완료. ]")
#                                print(f"매수시간 : {now}  |  코인명 : {coin51}  |  현재가 = ￦{price51}  |  MACD = ￦{macd51}  |  보유수량 = {krw_balance51}  |  평가금액 = ￦{bp51}")
#                                print(f"매수가능 : {op_mode51} - 불가")
#                                print("")
#
#                            else:
#                                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
#                                op_mode51 = False
#
#                                print(f"[ 51. {krw_coin51} 잔고부족으로 매수불가. ]")
#                                print(f"현재시간 : {now}  |  코인명 : {coin51}")
#                                print(f"매수가능 : {op_mode51} - 불가")
#                                print("")
#
#                        else:
#                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
#                            op_mode51 = False
#
#                            print(f"[ 51. {krw_coin51} 잔고부족으로 매수불가. ]")
#                            print(f"현재시간 : {now}  |  코인명 : {coin51}")
#                            print(f"매수가능 : {op_mode51} - 불가")
#                            print("")
#
#                    elif krw51 <= buy_krw:   # 매수가능금액 krw51 가 매수평균가 buy_krw 보다 같거나 작을때
#                        if krw51 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
#                            # 매수금액은 매수가능금액인 krw51 로
#                            upbit.buy_market_order(krw_coin51, krw51 * 0.99)   # 매수가능금액에서 1%를 빼고
#
#                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
#                            op_mode51 = False
#
#                            # 1초 딜레이
#                            #time.sleep(1)
#                            # 보유수량 불러오기
#                            krw_balance51 = upbit.get_balance(krw_coin51)
#                            # 코인 현재가 불러오기
#                            price51 = pyupbit.get_current_price(krw_coin51)
#                            # 보유코인 원화금액으로 계산하기
#                            bp51 = price51 * krw_balance51
#
#                            # 보유 및 매수 가능 출력.
#                            print(f"[ 51. {krw_coin51} 매수완료. ]")
#                            print(f"매수시간 : {now}  |  코인명 : {coin51}  |  현재가 = ￦{price51}  |  MACD = ￦{macd51}  |  보유수량 = {krw_balance51}  |  평가금액 = ￦{bp51}")
#                            print(f"매수가능 : {op_mode51} - 불가")
#                            print("")
#
#                        else:
#                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
#                            op_mode51 = False
#
#                            print(f"[ 51. {krw_coin51} 잔고부족으로 매수불가. ]")
#                            print(f"현재시간 : {now}  |  코인명 : {coin51}")
#                            print(f"매수가능 : {op_mode51} - 불가")
#                            print("")
#
#            elif macd51 < 0:       # macd가 0보다 낮을때는 매도
            if macd51 < 0:       # macd가 0보다 낮을때는 매도
                if op_mode51 == False:   # 매수 불가(False)일 경우 - 매도시도
                    # 보유수량 불러오기
                    krw_balance51 = upbit.get_balance(krw_coin51)
                    # 현재가 불러오기
                    price51 = pyupbit.get_current_price(krw_coin51)
                    # 보유코인 원화금액으로 계산하기
                    bp51 = price51 * krw_balance51

                    # 보유코인 원화금액 매도시도
                    if  bp51 > 10100:   # 보유코인 평가 금액이 10,100원 초과일때 - 매도시도
                        # 매도할 코인명 - krw_coin51, 매도할 코인수량 - krw_balance51
                        upbit.sell_market_order(krw_coin51, krw_balance51)

                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode51 = True

                        # 1초 딜레이
                        #time.sleep(1)
                        # 보유수량 불러오기
                        krw_balance51 = upbit.get_balance(krw_coin51)
                        # 코인 현재가 불러오기
                        price51 = pyupbit.get_current_price(krw_coin51)
                        # 보유코인 원화금액으로 계산하기
                        bp51 = price51 * krw_balance51

                        # 보유 및 매수 가능 출력.
                        print(f"[ 51. {krw_coin51} 매도완료. ]")
                        print(f"매도시간 : {now}  |  코인명 : {coin51}  |  현재가 = ￦{price51}  |  MACD = ￦{macd51}  |  보유수량 = {krw_balance51}  |  평가금액 = ￦{bp51}")
                        print(f"매수가능 : {op_mode51} - 가능")
                        print("")

                    else:   # 보유코인 평가 금액이 10,100원 이하일때
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode51 = True

                        print(f"[ 51. {krw_coin51} 보유코인이 없으므로 매도불가. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin51}")
                        print(f"매수가능 : {op_mode51} - 가능")
                        print("")

            # 1초 딜레이.
            time.sleep(1)
            ##### 51번 코인 매매 종료 #####
            #############################


            ###############################
            ##### 매매 : 52번코인 시작. #####

            ##### 코인보유현황
            # 보유수량 불러오기
            krw_balance52 = upbit.get_balance(krw_coin52)
            # 코인 현재가 불러오기
            price52 = pyupbit.get_current_price(krw_coin52)
            # 보유코인 원화금액으로 계산하기
            bp52 = price52 * krw_balance52
            # 코인 현황 출력.
            print(f"52. 코인명 : {coin52}  |  현재가 = ￦{price52}  |  보유수량 = {krw_balance52}  |  평가금액 = ￦{bp52}")
            # 코인 보유 유무
            if bp52 > 10100:
                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                op_mode52 = False

                # 보유 및 매수 가능 출력.
                print(f" 코인 보유 : 보유중  |  매수가능 - {op_mode52} - 매수불가")
                print("")
            else:
                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                op_mode52 = True

                # 보유 및 매수 가능 출력.
                print(f" 코인 보유 : 없음  |  매수가능 - {op_mode52} - 매수가능")
                print("")
            #time.sleep(1)


            # 코인 현재가 불러오기
            price52 = pyupbit.get_current_price(krw_coin52)

            # MACD 조회.
            #macd52 = get_macd(krw_coin52)
            # 거래량 동반한 MACD 조회.
            macd52 = get_acc_macd(krw_coin52)
            # 20일 이평선 조회.
            #macd52 = get_ma20(krw_coin52)

            # 매수가능금액 불러오기
            krw52 = upbit.get_balance("KRW")

            # MACD 조건문
#            if macd52 >= 0:     # macd가 0보다 높을때는 매수
#                if op_mode52 == True:    # 매수 가능(True)일 경우 - 매수시도
#                    if krw52 > buy_krw:      # 매수가능금액 krw52 가 매수평균가 buy_krw 보다 클때
#                        if krw52 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
#                            if buy_krw > 10100:     # 매수평균가 buy_krw 가 10,100원 초과일 경우 : 매수
#                                # 매수금액은 매수평균가 buy_krw 로
#                                upbit.buy_market_order(krw_coin52, buy_krw * 0.99)   # 매수가능금액에서 1%를 빼고
#
#                                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
#                                op_mode52 = False
#
#                                # 1초 딜레이
#                                time.sleep(1)
#                                # 보유수량 불러오기
#                                krw_balance52 = upbit.get_balance(krw_coin52)
#                                # 코인 현재가 불러오기
#                                price52 = pyupbit.get_current_price(krw_coin52)
#                                # 보유코인 원화금액으로 계산하기
#                                bp52 = price52 * krw_balance52
#
#                                # 보유 및 매수 가능 출력.
#                                print(f"[ 52. {krw_coin52} 매수완료. ]")
#                                print(f"매수시간 : {now}  |  코인명 : {coin52}  |  현재가 = ￦{price52}  |  MACD = ￦{macd52}  |  보유수량 = {krw_balance52}  |  평가금액 = ￦{bp52}")
#                                print(f"매수가능 : {op_mode52} - 불가")
#                                print("")
#
#                            else:
#                                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
#                                op_mode52 = False
#
#                                print(f"[ 52. {krw_coin52} 잔고부족으로 매수불가. ]")
#                                print(f"현재시간 : {now}  |  코인명 : {coin52}")
#                                print(f"매수가능 : {op_mode52} - 불가")
#                                print("")
#
#                        else:
#                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
#                            op_mode52 = False
#
#                            print(f"[ 52. {krw_coin52} 잔고부족으로 매수불가. ]")
#                            print(f"현재시간 : {now}  |  코인명 : {coin52}")
#                            print(f"매수가능 : {op_mode52} - 불가")
#                            print("")
#
#                    elif krw52 <= buy_krw:   # 매수가능금액 krw52 가 매수평균가 buy_krw 보다 같거나 작을때
#                        if krw52 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
#                            # 매수금액은 매수가능금액인 krw52 로
#                            upbit.buy_market_order(krw_coin52, krw52 * 0.99)   # 매수가능금액에서 1%를 빼고
#
#                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
#                            op_mode52 = False
#
#                            # 1초 딜레이
#                            #time.sleep(1)
#                            # 보유수량 불러오기
#                            krw_balance52 = upbit.get_balance(krw_coin52)
#                            # 코인 현재가 불러오기
#                            price52 = pyupbit.get_current_price(krw_coin52)
#                            # 보유코인 원화금액으로 계산하기
#                            bp52 = price52 * krw_balance52
#
#                            # 보유 및 매수 가능 출력.
#                            print(f"[ 52. {krw_coin52} 매수완료. ]")
#                            print(f"매수시간 : {now}  |  코인명 : {coin52}  |  현재가 = ￦{price52}  |  MACD = ￦{macd52}  |  보유수량 = {krw_balance52}  |  평가금액 = ￦{bp52}")
#                            print(f"매수가능 : {op_mode52} - 불가")
#                            print("")
#
#                        else:
#                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
#                            op_mode52 = False
#
#                            print(f"[ 52. {krw_coin52} 잔고부족으로 매수불가. ]")
#                            print(f"현재시간 : {now}  |  코인명 : {coin52}")
#                            print(f"매수가능 : {op_mode52} - 불가")
#                            print("")
#
#            elif macd52 < 0:       # macd가 0보다 낮을때는 매도
            if macd52 < 0:       # macd가 0보다 낮을때는 매도
                if op_mode52 == False:   # 매수 불가(False)일 경우 - 매도시도
                    # 보유수량 불러오기
                    krw_balance52 = upbit.get_balance(krw_coin52)
                    # 현재가 불러오기
                    price52 = pyupbit.get_current_price(krw_coin52)
                    # 보유코인 원화금액으로 계산하기
                    bp52 = price52 * krw_balance52

                    # 보유코인 원화금액 매도시도
                    if  bp52 > 10100:   # 보유코인 평가 금액이 10,100원 초과일때 - 매도시도
                        # 매도할 코인명 - krw_coin52, 매도할 코인수량 - krw_balance52
                        upbit.sell_market_order(krw_coin52, krw_balance52)

                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode52 = True

                        # 1초 딜레이
                        #time.sleep(1)
                        # 보유수량 불러오기
                        krw_balance52 = upbit.get_balance(krw_coin52)
                        # 코인 현재가 불러오기
                        price52 = pyupbit.get_current_price(krw_coin52)
                        # 보유코인 원화금액으로 계산하기
                        bp52 = price52 * krw_balance52

                        # 보유 및 매수 가능 출력.
                        print(f"[ 52. {krw_coin52} 매도완료. ]")
                        print(f"매도시간 : {now}  |  코인명 : {coin52}  |  현재가 = ￦{price52}  |  MACD = ￦{macd52}  |  보유수량 = {krw_balance52}  |  평가금액 = ￦{bp52}")
                        print(f"매수가능 : {op_mode52} - 가능")
                        print("")

                    else:   # 보유코인 평가 금액이 10,100원 이하일때
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode52 = True

                        print(f"[ 52. {krw_coin52} 보유코인이 없으므로 매도불가. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin52}")
                        print(f"매수가능 : {op_mode52} - 가능")
                        print("")

            # 1초 딜레이.
            time.sleep(1)
            ##### 52번 코인 매매 종료 #####
            #############################


            ###############################
            ##### 매매 : 53번코인 시작. #####

            ##### 코인보유현황
            # 보유수량 불러오기
            krw_balance53 = upbit.get_balance(krw_coin53)
            # 코인 현재가 불러오기
            price53 = pyupbit.get_current_price(krw_coin53)
            # 보유코인 원화금액으로 계산하기
            bp53 = price53 * krw_balance53
            # 코인 현황 출력.
            print(f"53. 코인명 : {coin53}  |  현재가 = ￦{price53}  |  보유수량 = {krw_balance53}  |  평가금액 = ￦{bp53}")
            # 코인 보유 유무
            if bp53 > 10100:
                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                op_mode53 = False

                # 보유 및 매수 가능 출력.
                print(f" 코인 보유 : 보유중  |  매수가능 - {op_mode53} - 매수불가")
                print("")
            else:
                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                op_mode53 = True

                # 보유 및 매수 가능 출력.
                print(f" 코인 보유 : 없음  |  매수가능 - {op_mode53} - 매수가능")
                print("")
            #time.sleep(1)


            # 코인 현재가 불러오기
            price53 = pyupbit.get_current_price(krw_coin53)

            # MACD 조회.
            #macd53 = get_macd(krw_coin53)
            # 거래량 동반한 MACD 조회.
            macd53 = get_acc_macd(krw_coin53)
            # 20일 이평선 조회.
            #macd53 = get_ma20(krw_coin53)

            # 매수가능금액 불러오기
            krw53 = upbit.get_balance("KRW")

            # MACD 조건문
#            if macd53 >= 0:     # macd가 0보다 높을때는 매수
#                if op_mode53 == True:    # 매수 가능(True)일 경우 - 매수시도
#                    if krw53 > buy_krw:      # 매수가능금액 krw53 가 매수평균가 buy_krw 보다 클때
#                        if krw53 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
#                            if buy_krw > 10100:     # 매수평균가 buy_krw 가 10,100원 초과일 경우 : 매수
#                                # 매수금액은 매수평균가 buy_krw 로
#                                upbit.buy_market_order(krw_coin53, buy_krw * 0.99)   # 매수가능금액에서 1%를 빼고
#
#                                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
#                                op_mode53 = False
#
#                                # 1초 딜레이
#                                time.sleep(1)
#                                # 보유수량 불러오기
#                                krw_balance53 = upbit.get_balance(krw_coin53)
#                                # 코인 현재가 불러오기
#                                price53 = pyupbit.get_current_price(krw_coin53)
#                                # 보유코인 원화금액으로 계산하기
#                                bp53 = price53 * krw_balance53
#
#                                # 보유 및 매수 가능 출력.
#                                print(f"[ 53. {krw_coin53} 매수완료. ]")
#                                print(f"매수시간 : {now}  |  코인명 : {coin53}  |  현재가 = ￦{price53}  |  MACD = ￦{macd53}  |  보유수량 = {krw_balance53}  |  평가금액 = ￦{bp53}")
#                                print(f"매수가능 : {op_mode53} - 불가")
#                                print("")
#
#                            else:
#                                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
#                                op_mode53 = False
#
#                                print(f"[ 53. {krw_coin53} 잔고부족으로 매수불가. ]")
#                                print(f"현재시간 : {now}  |  코인명 : {coin53}")
#                                print(f"매수가능 : {op_mode53} - 불가")
#                                print("")
#
#                        else:
#                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
#                            op_mode53 = False
#
#                            print(f"[ 53. {krw_coin53} 잔고부족으로 매수불가. ]")
#                            print(f"현재시간 : {now}  |  코인명 : {coin53}")
#                            print(f"매수가능 : {op_mode53} - 불가")
#                            print("")
#
#                    elif krw53 <= buy_krw:   # 매수가능금액 krw53 가 매수평균가 buy_krw 보다 같거나 작을때
#                        if krw53 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
#                            # 매수금액은 매수가능금액인 krw53 로
#                            upbit.buy_market_order(krw_coin53, krw53 * 0.99)   # 매수가능금액에서 1%를 빼고
#
#                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
#                            op_mode53 = False
#
#                            # 1초 딜레이
#                            #time.sleep(1)
#                            # 보유수량 불러오기
#                            krw_balance53 = upbit.get_balance(krw_coin53)
#                            # 코인 현재가 불러오기
#                            price53 = pyupbit.get_current_price(krw_coin53)
#                            # 보유코인 원화금액으로 계산하기
#                            bp53 = price53 * krw_balance53
#
#                            # 보유 및 매수 가능 출력.
#                            print(f"[ 53. {krw_coin53} 매수완료. ]")
#                            print(f"매수시간 : {now}  |  코인명 : {coin53}  |  현재가 = ￦{price53}  |  MACD = ￦{macd53}  |  보유수량 = {krw_balance53}  |  평가금액 = ￦{bp53}")
#                            print(f"매수가능 : {op_mode53} - 불가")
#                            print("")
#
#                        else:
#                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
#                            op_mode53 = False
#
#                            print(f"[ 53. {krw_coin53} 잔고부족으로 매수불가. ]")
#                            print(f"현재시간 : {now}  |  코인명 : {coin53}")
#                            print(f"매수가능 : {op_mode53} - 불가")
#                            print("")
#
#            elif macd53 < 0:       # macd가 0보다 낮을때는 매도
            if macd53 < 0:       # macd가 0보다 낮을때는 매도
                if op_mode53 == False:   # 매수 불가(False)일 경우 - 매도시도
                    # 보유수량 불러오기
                    krw_balance53 = upbit.get_balance(krw_coin53)
                    # 현재가 불러오기
                    price53 = pyupbit.get_current_price(krw_coin53)
                    # 보유코인 원화금액으로 계산하기
                    bp53 = price53 * krw_balance53

                    # 보유코인 원화금액 매도시도
                    if  bp53 > 10100:   # 보유코인 평가 금액이 10,100원 초과일때 - 매도시도
                        # 매도할 코인명 - krw_coin53, 매도할 코인수량 - krw_balance53
                        upbit.sell_market_order(krw_coin53, krw_balance53)

                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode53 = True

                        # 1초 딜레이
                        #time.sleep(1)
                        # 보유수량 불러오기
                        krw_balance53 = upbit.get_balance(krw_coin53)
                        # 코인 현재가 불러오기
                        price53 = pyupbit.get_current_price(krw_coin53)
                        # 보유코인 원화금액으로 계산하기
                        bp53 = price53 * krw_balance53

                        # 보유 및 매수 가능 출력.
                        print(f"[ 53. {krw_coin53} 매도완료. ]")
                        print(f"매도시간 : {now}  |  코인명 : {coin53}  |  현재가 = ￦{price53}  |  MACD = ￦{macd53}  |  보유수량 = {krw_balance53}  |  평가금액 = ￦{bp53}")
                        print(f"매수가능 : {op_mode53} - 가능")
                        print("")

                    else:   # 보유코인 평가 금액이 10,100원 이하일때
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode53 = True

                        print(f"[ 53. {krw_coin53} 보유코인이 없으므로 매도불가. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin53}")
                        print(f"매수가능 : {op_mode53} - 가능")
                        print("")

            # 1초 딜레이.
            time.sleep(1)
            ##### 53번 코인 매매 종료 #####
            #############################


            ###############################
            ##### 매매 : 54번코인 시작. #####

            ##### 코인보유현황
            # 보유수량 불러오기
            krw_balance54 = upbit.get_balance(krw_coin54)
            # 코인 현재가 불러오기
            price54 = pyupbit.get_current_price(krw_coin54)
            # 보유코인 원화금액으로 계산하기
            bp54 = price54 * krw_balance54
            # 코인 현황 출력.
            print(f"54. 코인명 : {coin54}  |  현재가 = ￦{price54}  |  보유수량 = {krw_balance54}  |  평가금액 = ￦{bp54}")
            # 코인 보유 유무
            if bp54 > 10100:
                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                op_mode54 = False

                # 보유 및 매수 가능 출력.
                print(f" 코인 보유 : 보유중  |  매수가능 - {op_mode54} - 매수불가")
                print("")
            else:
                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                op_mode54 = True

                # 보유 및 매수 가능 출력.
                print(f" 코인 보유 : 없음  |  매수가능 - {op_mode54} - 매수가능")
                print("")
            #time.sleep(1)


            # 코인 현재가 불러오기
            price54 = pyupbit.get_current_price(krw_coin54)

            # MACD 조회.
            #macd54 = get_macd(krw_coin54)
            # 거래량 동반한 MACD 조회.
            macd54 = get_acc_macd(krw_coin54)
            # 20일 이평선 조회.
            #macd54 = get_ma20(krw_coin54)

            # 매수가능금액 불러오기
            krw54 = upbit.get_balance("KRW")

            # MACD 조건문
#            if macd54 >= 0:     # macd가 0보다 높을때는 매수
#                if op_mode54 == True:    # 매수 가능(True)일 경우 - 매수시도
#                    if krw54 > buy_krw:      # 매수가능금액 krw54 가 매수평균가 buy_krw 보다 클때
#                        if krw54 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
#                            if buy_krw > 10100:     # 매수평균가 buy_krw 가 10,100원 초과일 경우 : 매수
#                                # 매수금액은 매수평균가 buy_krw 로
#                                upbit.buy_market_order(krw_coin54, buy_krw * 0.99)   # 매수가능금액에서 1%를 빼고
#
#                                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
#                                op_mode54 = False
#
#                                # 1초 딜레이
#                                time.sleep(1)
#                                # 보유수량 불러오기
#                                krw_balance54 = upbit.get_balance(krw_coin54)
#                                # 코인 현재가 불러오기
#                                price54 = pyupbit.get_current_price(krw_coin54)
#                                # 보유코인 원화금액으로 계산하기
#                                bp54 = price54 * krw_balance54
#
#                                # 보유 및 매수 가능 출력.
#                                print(f"[ 54. {krw_coin54} 매수완료. ]")
#                                print(f"매수시간 : {now}  |  코인명 : {coin54}  |  현재가 = ￦{price54}  |  MACD = ￦{macd54}  |  보유수량 = {krw_balance54}  |  평가금액 = ￦{bp54}")
#                                print(f"매수가능 : {op_mode54} - 불가")
#                                print("")
#
#                            else:
#                                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
#                                op_mode54 = False
#
#                                print(f"[ 54. {krw_coin54} 잔고부족으로 매수불가. ]")
#                                print(f"현재시간 : {now}  |  코인명 : {coin54}")
#                                print(f"매수가능 : {op_mode54} - 불가")
#                                print("")
#
#                        else:
#                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
#                            op_mode54 = False
#
#                            print(f"[ 54. {krw_coin54} 잔고부족으로 매수불가. ]")
#                            print(f"현재시간 : {now}  |  코인명 : {coin54}")
#                            print(f"매수가능 : {op_mode54} - 불가")
#                            print("")
#
#                    elif krw54 <= buy_krw:   # 매수가능금액 krw54 가 매수평균가 buy_krw 보다 같거나 작을때
#                        if krw54 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
#                            # 매수금액은 매수가능금액인 krw54 로
#                            upbit.buy_market_order(krw_coin54, krw54 * 0.99)   # 매수가능금액에서 1%를 빼고
#
#                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
#                            op_mode54 = False
#
#                            # 1초 딜레이
#                            #time.sleep(1)
#                            # 보유수량 불러오기
#                            krw_balance54 = upbit.get_balance(krw_coin54)
#                            # 코인 현재가 불러오기
#                            price54 = pyupbit.get_current_price(krw_coin54)
#                            # 보유코인 원화금액으로 계산하기
#                            bp54 = price54 * krw_balance54
#
#                            # 보유 및 매수 가능 출력.
#                            print(f"[ 54. {krw_coin54} 매수완료. ]")
#                            print(f"매수시간 : {now}  |  코인명 : {coin54}  |  현재가 = ￦{price54}  |  MACD = ￦{macd54}  |  보유수량 = {krw_balance54}  |  평가금액 = ￦{bp54}")
#                            print(f"매수가능 : {op_mode54} - 불가")
#                            print("")
#
#                        else:
#                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
#                            op_mode54 = False
#
#                            print(f"[ 54. {krw_coin54} 잔고부족으로 매수불가. ]")
#                            print(f"현재시간 : {now}  |  코인명 : {coin54}")
#                            print(f"매수가능 : {op_mode54} - 불가")
#                            print("")
#
#            elif macd54 < 0:       # macd가 0보다 낮을때는 매도
            if macd54 < 0:       # macd가 0보다 낮을때는 매도
                if op_mode54 == False:   # 매수 불가(False)일 경우 - 매도시도
                    # 보유수량 불러오기
                    krw_balance54 = upbit.get_balance(krw_coin54)
                    # 현재가 불러오기
                    price54 = pyupbit.get_current_price(krw_coin54)
                    # 보유코인 원화금액으로 계산하기
                    bp54 = price54 * krw_balance54

                    # 보유코인 원화금액 매도시도
                    if  bp54 > 10100:   # 보유코인 평가 금액이 10,100원 초과일때 - 매도시도
                        # 매도할 코인명 - krw_coin54, 매도할 코인수량 - krw_balance54
                        upbit.sell_market_order(krw_coin54, krw_balance54)

                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode54 = True

                        # 1초 딜레이
                        #time.sleep(1)
                        # 보유수량 불러오기
                        krw_balance54 = upbit.get_balance(krw_coin54)
                        # 코인 현재가 불러오기
                        price54 = pyupbit.get_current_price(krw_coin54)
                        # 보유코인 원화금액으로 계산하기
                        bp54 = price54 * krw_balance54

                        # 보유 및 매수 가능 출력.
                        print(f"[ 54. {krw_coin54} 매도완료. ]")
                        print(f"매도시간 : {now}  |  코인명 : {coin54}  |  현재가 = ￦{price54}  |  MACD = ￦{macd54}  |  보유수량 = {krw_balance54}  |  평가금액 = ￦{bp54}")
                        print(f"매수가능 : {op_mode54} - 가능")
                        print("")

                    else:   # 보유코인 평가 금액이 10,100원 이하일때
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode54 = True

                        print(f"[ 54. {krw_coin54} 보유코인이 없으므로 매도불가. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin54}")
                        print(f"매수가능 : {op_mode54} - 가능")
                        print("")

            # 1초 딜레이.
            time.sleep(1)
            ##### 54번 코인 매매 종료 #####
            #############################


            ###############################
            ##### 매매 : 55번코인 시작. #####

            ##### 코인보유현황
            # 보유수량 불러오기
            krw_balance55 = upbit.get_balance(krw_coin55)
            # 코인 현재가 불러오기
            price55 = pyupbit.get_current_price(krw_coin55)
            # 보유코인 원화금액으로 계산하기
            bp55 = price55 * krw_balance55
            # 코인 현황 출력.
            print(f"55. 코인명 : {coin55}  |  현재가 = ￦{price55}  |  보유수량 = {krw_balance55}  |  평가금액 = ￦{bp55}")
            # 코인 보유 유무
            if bp55 > 10100:
                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                op_mode55 = False

                # 보유 및 매수 가능 출력.
                print(f" 코인 보유 : 보유중  |  매수가능 - {op_mode55} - 매수불가")
                print("")
            else:
                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                op_mode55 = True

                # 보유 및 매수 가능 출력.
                print(f" 코인 보유 : 없음  |  매수가능 - {op_mode55} - 매수가능")
                print("")
            #time.sleep(1)


            # 코인 현재가 불러오기
            price55 = pyupbit.get_current_price(krw_coin55)

            # MACD 조회.
            #macd55 = get_macd(krw_coin55)
            # 거래량 동반한 MACD 조회.
            macd55 = get_acc_macd(krw_coin55)
            # 20일 이평선 조회.
            #macd55 = get_ma20(krw_coin55)

            # 매수가능금액 불러오기
            krw55 = upbit.get_balance("KRW")

            # MACD 조건문
#            if macd55 >= 0:     # macd가 0보다 높을때는 매수
#                if op_mode55 == True:    # 매수 가능(True)일 경우 - 매수시도
#                    if krw55 > buy_krw:      # 매수가능금액 krw55 가 매수평균가 buy_krw 보다 클때
#                        if krw55 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
#                            if buy_krw > 10100:     # 매수평균가 buy_krw 가 10,100원 초과일 경우 : 매수
#                                # 매수금액은 매수평균가 buy_krw 로
#                                upbit.buy_market_order(krw_coin55, buy_krw * 0.99)   # 매수가능금액에서 1%를 빼고
#
#                                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
#                                op_mode55 = False
#
#                                # 1초 딜레이
#                                time.sleep(1)
#                                # 보유수량 불러오기
#                                krw_balance55 = upbit.get_balance(krw_coin55)
#                                # 코인 현재가 불러오기
#                                price55 = pyupbit.get_current_price(krw_coin55)
#                                # 보유코인 원화금액으로 계산하기
#                                bp55 = price55 * krw_balance55
#
#                                # 보유 및 매수 가능 출력.
#                                print(f"[ 55. {krw_coin55} 매수완료. ]")
#                                print(f"매수시간 : {now}  |  코인명 : {coin55}  |  현재가 = ￦{price55}  |  MACD = ￦{macd55}  |  보유수량 = {krw_balance55}  |  평가금액 = ￦{bp55}")
#                                print(f"매수가능 : {op_mode55} - 불가")
#                                print("")
#
#                            else:
#                                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
#                                op_mode55 = False
#
#                                print(f"[ 55. {krw_coin55} 잔고부족으로 매수불가. ]")
#                                print(f"현재시간 : {now}  |  코인명 : {coin55}")
#                                print(f"매수가능 : {op_mode55} - 불가")
#                                print("")
#
#                        else:
#                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
#                            op_mode55 = False
#
#                            print(f"[ 55. {krw_coin55} 잔고부족으로 매수불가. ]")
#                            print(f"현재시간 : {now}  |  코인명 : {coin55}")
#                            print(f"매수가능 : {op_mode55} - 불가")
#                            print("")
#
#                    elif krw55 <= buy_krw:   # 매수가능금액 krw55 가 매수평균가 buy_krw 보다 같거나 작을때
#                        if krw55 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
#                            # 매수금액은 매수가능금액인 krw55 로
#                            upbit.buy_market_order(krw_coin55, krw55 * 0.99)   # 매수가능금액에서 1%를 빼고
#
#                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
#                            op_mode55 = False
#
#                            # 1초 딜레이
#                            #time.sleep(1)
#                            # 보유수량 불러오기
#                            krw_balance55 = upbit.get_balance(krw_coin55)
#                            # 코인 현재가 불러오기
#                            price55 = pyupbit.get_current_price(krw_coin55)
#                            # 보유코인 원화금액으로 계산하기
#                            bp55 = price55 * krw_balance55
#
#                            # 보유 및 매수 가능 출력.
#                            print(f"[ 55. {krw_coin55} 매수완료. ]")
#                            print(f"매수시간 : {now}  |  코인명 : {coin55}  |  현재가 = ￦{price55}  |  MACD = ￦{macd55}  |  보유수량 = {krw_balance55}  |  평가금액 = ￦{bp55}")
#                            print(f"매수가능 : {op_mode55} - 불가")
#                            print("")
#
#                        else:
#                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
#                            op_mode55 = False
#
#                            print(f"[ 55. {krw_coin55} 잔고부족으로 매수불가. ]")
#                            print(f"현재시간 : {now}  |  코인명 : {coin55}")
#                            print(f"매수가능 : {op_mode55} - 불가")
#                            print("")
#
#            elif macd55 < 0:       # macd가 0보다 낮을때는 매도
            if macd55 < 0:       # macd가 0보다 낮을때는 매도
                if op_mode55 == False:   # 매수 불가(False)일 경우 - 매도시도
                    # 보유수량 불러오기
                    krw_balance55 = upbit.get_balance(krw_coin55)
                    # 현재가 불러오기
                    price55 = pyupbit.get_current_price(krw_coin55)
                    # 보유코인 원화금액으로 계산하기
                    bp55 = price55 * krw_balance55

                    # 보유코인 원화금액 매도시도
                    if  bp55 > 10100:   # 보유코인 평가 금액이 10,100원 초과일때 - 매도시도
                        # 매도할 코인명 - krw_coin55, 매도할 코인수량 - krw_balance55
                        upbit.sell_market_order(krw_coin55, krw_balance55)

                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode55 = True

                        # 1초 딜레이
                        #time.sleep(1)
                        # 보유수량 불러오기
                        krw_balance55 = upbit.get_balance(krw_coin55)
                        # 코인 현재가 불러오기
                        price55 = pyupbit.get_current_price(krw_coin55)
                        # 보유코인 원화금액으로 계산하기
                        bp55 = price55 * krw_balance55

                        # 보유 및 매수 가능 출력.
                        print(f"[ 55. {krw_coin55} 매도완료. ]")
                        print(f"매도시간 : {now}  |  코인명 : {coin55}  |  현재가 = ￦{price55}  |  MACD = ￦{macd55}  |  보유수량 = {krw_balance55}  |  평가금액 = ￦{bp55}")
                        print(f"매수가능 : {op_mode55} - 가능")
                        print("")

                    else:   # 보유코인 평가 금액이 10,100원 이하일때
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode55 = True

                        print(f"[ 55. {krw_coin55} 보유코인이 없으므로 매도불가. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin55}")
                        print(f"매수가능 : {op_mode55} - 가능")
                        print("")

            # 1초 딜레이.
            time.sleep(1)
            ##### 55번 코인 매매 종료 #####
            #############################


            ###############################
            ##### 매매 : 56번코인 시작. #####

            ##### 코인보유현황
            # 보유수량 불러오기
            krw_balance56 = upbit.get_balance(krw_coin56)
            # 코인 현재가 불러오기
            price56 = pyupbit.get_current_price(krw_coin56)
            # 보유코인 원화금액으로 계산하기
            bp56 = price56 * krw_balance56
            # 코인 현황 출력.
            print(f"56. 코인명 : {coin56}  |  현재가 = ￦{price56}  |  보유수량 = {krw_balance56}  |  평가금액 = ￦{bp56}")
            # 코인 보유 유무
            if bp56 > 10100:
                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                op_mode56 = False

                # 보유 및 매수 가능 출력.
                print(f" 코인 보유 : 보유중  |  매수가능 - {op_mode56} - 매수불가")
                print("")
            else:
                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                op_mode56 = True

                # 보유 및 매수 가능 출력.
                print(f" 코인 보유 : 없음  |  매수가능 - {op_mode56} - 매수가능")
                print("")
            #time.sleep(1)


            # 코인 현재가 불러오기
            price56 = pyupbit.get_current_price(krw_coin56)

            # MACD 조회.
            #macd56 = get_macd(krw_coin56)
            # 거래량 동반한 MACD 조회.
            macd56 = get_acc_macd(krw_coin56)
            # 20일 이평선 조회.
            #macd56 = get_ma20(krw_coin56)

            # 매수가능금액 불러오기
            krw56 = upbit.get_balance("KRW")

            # MACD 조건문
#            if macd56 >= 0:     # macd가 0보다 높을때는 매수
#                if op_mode56 == True:    # 매수 가능(True)일 경우 - 매수시도
#                    if krw56 > buy_krw:      # 매수가능금액 krw56 가 매수평균가 buy_krw 보다 클때
#                        if krw56 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
#                            if buy_krw > 10100:     # 매수평균가 buy_krw 가 10,100원 초과일 경우 : 매수
#                                # 매수금액은 매수평균가 buy_krw 로
#                                upbit.buy_market_order(krw_coin56, buy_krw * 0.99)   # 매수가능금액에서 1%를 빼고
#
#                                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
#                                op_mode56 = False
#
#                                # 1초 딜레이
#                                time.sleep(1)
#                                # 보유수량 불러오기
#                                krw_balance56 = upbit.get_balance(krw_coin56)
#                                # 코인 현재가 불러오기
#                                price56 = pyupbit.get_current_price(krw_coin56)
#                                # 보유코인 원화금액으로 계산하기
#                                bp56 = price56 * krw_balance56
#
#                                # 보유 및 매수 가능 출력.
#                                print(f"[ 56. {krw_coin56} 매수완료. ]")
#                                print(f"매수시간 : {now}  |  코인명 : {coin56}  |  현재가 = ￦{price56}  |  MACD = ￦{macd56}  |  보유수량 = {krw_balance56}  |  평가금액 = ￦{bp56}")
#                                print(f"매수가능 : {op_mode56} - 불가")
#                                print("")
#
#                            else:
#                                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
#                                op_mode56 = False
#
#                                print(f"[ 56. {krw_coin56} 잔고부족으로 매수불가. ]")
#                                print(f"현재시간 : {now}  |  코인명 : {coin56}")
#                                print(f"매수가능 : {op_mode56} - 불가")
#                                print("")
#
#                        else:
#                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
#                            op_mode56 = False
#
#                            print(f"[ 56. {krw_coin56} 잔고부족으로 매수불가. ]")
#                            print(f"현재시간 : {now}  |  코인명 : {coin56}")
#                            print(f"매수가능 : {op_mode56} - 불가")
#                            print("")
#
#                    elif krw56 <= buy_krw:   # 매수가능금액 krw56 가 매수평균가 buy_krw 보다 같거나 작을때
#                        if krw56 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
#                            # 매수금액은 매수가능금액인 krw56 로
#                            upbit.buy_market_order(krw_coin56, krw56 * 0.99)   # 매수가능금액에서 1%를 빼고
#
#                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
#                            op_mode56 = False
#
#                            # 1초 딜레이
#                            #time.sleep(1)
#                            # 보유수량 불러오기
#                            krw_balance56 = upbit.get_balance(krw_coin56)
#                            # 코인 현재가 불러오기
#                            price56 = pyupbit.get_current_price(krw_coin56)
#                            # 보유코인 원화금액으로 계산하기
#                            bp56 = price56 * krw_balance56
#
#                            # 보유 및 매수 가능 출력.
#                            print(f"[ 56. {krw_coin56} 매수완료. ]")
#                            print(f"매수시간 : {now}  |  코인명 : {coin56}  |  현재가 = ￦{price56}  |  MACD = ￦{macd56}  |  보유수량 = {krw_balance56}  |  평가금액 = ￦{bp56}")
#                            print(f"매수가능 : {op_mode56} - 불가")
#                            print("")
#
#                        else:
#                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
#                            op_mode56 = False
#
#                            print(f"[ 56. {krw_coin56} 잔고부족으로 매수불가. ]")
#                            print(f"현재시간 : {now}  |  코인명 : {coin56}")
#                            print(f"매수가능 : {op_mode56} - 불가")
#                            print("")
#
#            elif macd56 < 0:       # macd가 0보다 낮을때는 매도
            if macd56 < 0:       # macd가 0보다 낮을때는 매도
                if op_mode56 == False:   # 매수 불가(False)일 경우 - 매도시도
                    # 보유수량 불러오기
                    krw_balance56 = upbit.get_balance(krw_coin56)
                    # 현재가 불러오기
                    price56 = pyupbit.get_current_price(krw_coin56)
                    # 보유코인 원화금액으로 계산하기
                    bp56 = price56 * krw_balance56

                    # 보유코인 원화금액 매도시도
                    if  bp56 > 10100:   # 보유코인 평가 금액이 10,100원 초과일때 - 매도시도
                        # 매도할 코인명 - krw_coin56, 매도할 코인수량 - krw_balance56
                        upbit.sell_market_order(krw_coin56, krw_balance56)

                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode56 = True

                        # 1초 딜레이
                        #time.sleep(1)
                        # 보유수량 불러오기
                        krw_balance56 = upbit.get_balance(krw_coin56)
                        # 코인 현재가 불러오기
                        price56 = pyupbit.get_current_price(krw_coin56)
                        # 보유코인 원화금액으로 계산하기
                        bp56 = price56 * krw_balance56

                        # 보유 및 매수 가능 출력.
                        print(f"[ 56. {krw_coin56} 매도완료. ]")
                        print(f"매도시간 : {now}  |  코인명 : {coin56}  |  현재가 = ￦{price56}  |  MACD = ￦{macd56}  |  보유수량 = {krw_balance56}  |  평가금액 = ￦{bp56}")
                        print(f"매수가능 : {op_mode56} - 가능")
                        print("")

                    else:   # 보유코인 평가 금액이 10,100원 이하일때
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode56 = True

                        print(f"[ 56. {krw_coin56} 보유코인이 없으므로 매도불가. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin56}")
                        print(f"매수가능 : {op_mode56} - 가능")
                        print("")

            # 1초 딜레이.
            time.sleep(1)
            ##### 56번 코인 매매 종료 #####
            #############################


            ###############################
            ##### 매매 : 57번코인 시작. #####

            ##### 코인보유현황
            # 보유수량 불러오기
            krw_balance57 = upbit.get_balance(krw_coin57)
            # 코인 현재가 불러오기
            price57 = pyupbit.get_current_price(krw_coin57)
            # 보유코인 원화금액으로 계산하기
            bp57 = price57 * krw_balance57
            # 코인 현황 출력.
            print(f"57. 코인명 : {coin57}  |  현재가 = ￦{price57}  |  보유수량 = {krw_balance57}  |  평가금액 = ￦{bp57}")
            # 코인 보유 유무
            if bp57 > 10100:
                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                op_mode57 = False

                # 보유 및 매수 가능 출력.
                print(f" 코인 보유 : 보유중  |  매수가능 - {op_mode57} - 매수불가")
                print("")
            else:
                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                op_mode57 = True

                # 보유 및 매수 가능 출력.
                print(f" 코인 보유 : 없음  |  매수가능 - {op_mode57} - 매수가능")
                print("")
            #time.sleep(1)


            # 코인 현재가 불러오기
            price57 = pyupbit.get_current_price(krw_coin57)

            # MACD 조회.
            #macd57 = get_macd(krw_coin57)
            # 거래량 동반한 MACD 조회.
            macd57 = get_acc_macd(krw_coin57)
            # 20일 이평선 조회.
            #macd57 = get_ma20(krw_coin57)

            # 매수가능금액 불러오기
            krw57 = upbit.get_balance("KRW")

            # MACD 조건문
#            if macd57 >= 0:     # macd가 0보다 높을때는 매수
#                if op_mode57 == True:    # 매수 가능(True)일 경우 - 매수시도
#                    if krw57 > buy_krw:      # 매수가능금액 krw57 가 매수평균가 buy_krw 보다 클때
#                        if krw57 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
#                            if buy_krw > 10100:     # 매수평균가 buy_krw 가 10,100원 초과일 경우 : 매수
#                                # 매수금액은 매수평균가 buy_krw 로
#                                upbit.buy_market_order(krw_coin57, buy_krw * 0.99)   # 매수가능금액에서 1%를 빼고
#
#                                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
#                                op_mode57 = False
#
#                                # 1초 딜레이
#                                time.sleep(1)
#                                # 보유수량 불러오기
#                                krw_balance57 = upbit.get_balance(krw_coin57)
#                                # 코인 현재가 불러오기
#                                price57 = pyupbit.get_current_price(krw_coin57)
#                                # 보유코인 원화금액으로 계산하기
#                                bp57 = price57 * krw_balance57
#
#                                # 보유 및 매수 가능 출력.
#                                print(f"[ 57. {krw_coin57} 매수완료. ]")
#                                print(f"매수시간 : {now}  |  코인명 : {coin57}  |  현재가 = ￦{price57}  |  MACD = ￦{macd57}  |  보유수량 = {krw_balance57}  |  평가금액 = ￦{bp57}")
#                                print(f"매수가능 : {op_mode57} - 불가")
#                                print("")
#
#                            else:
#                                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
#                                op_mode57 = False
#
#                                print(f"[ 57. {krw_coin57} 잔고부족으로 매수불가. ]")
#                                print(f"현재시간 : {now}  |  코인명 : {coin57}")
#                                print(f"매수가능 : {op_mode57} - 불가")
#                                print("")
#
#                        else:
#                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
#                            op_mode57 = False
#
#                            print(f"[ 57. {krw_coin57} 잔고부족으로 매수불가. ]")
#                            print(f"현재시간 : {now}  |  코인명 : {coin57}")
#                            print(f"매수가능 : {op_mode57} - 불가")
#                            print("")
#
#                    elif krw57 <= buy_krw:   # 매수가능금액 krw57 가 매수평균가 buy_krw 보다 같거나 작을때
#                        if krw57 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
#                            # 매수금액은 매수가능금액인 krw57 로
#                            upbit.buy_market_order(krw_coin57, krw57 * 0.99)   # 매수가능금액에서 1%를 빼고
#
#                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
#                            op_mode57 = False
#
#                            # 1초 딜레이
#                            #time.sleep(1)
#                            # 보유수량 불러오기
#                            krw_balance57 = upbit.get_balance(krw_coin57)
#                            # 코인 현재가 불러오기
#                            price57 = pyupbit.get_current_price(krw_coin57)
#                            # 보유코인 원화금액으로 계산하기
#                            bp57 = price57 * krw_balance57
#
#                            # 보유 및 매수 가능 출력.
#                            print(f"[ 57. {krw_coin57} 매수완료. ]")
#                            print(f"매수시간 : {now}  |  코인명 : {coin57}  |  현재가 = ￦{price57}  |  MACD = ￦{macd57}  |  보유수량 = {krw_balance57}  |  평가금액 = ￦{bp57}")
#                            print(f"매수가능 : {op_mode57} - 불가")
#                            print("")
#
#                        else:
#                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
#                            op_mode57 = False
#
#                            print(f"[ 57. {krw_coin57} 잔고부족으로 매수불가. ]")
#                            print(f"현재시간 : {now}  |  코인명 : {coin57}")
#                            print(f"매수가능 : {op_mode57} - 불가")
#                            print("")
#
#            elif macd57 < 0:       # macd가 0보다 낮을때는 매도
            if macd57 < 0:       # macd가 0보다 낮을때는 매도
                if op_mode57 == False:   # 매수 불가(False)일 경우 - 매도시도
                    # 보유수량 불러오기
                    krw_balance57 = upbit.get_balance(krw_coin57)
                    # 현재가 불러오기
                    price57 = pyupbit.get_current_price(krw_coin57)
                    # 보유코인 원화금액으로 계산하기
                    bp57 = price57 * krw_balance57

                    # 보유코인 원화금액 매도시도
                    if  bp57 > 10100:   # 보유코인 평가 금액이 10,100원 초과일때 - 매도시도
                        # 매도할 코인명 - krw_coin57, 매도할 코인수량 - krw_balance57
                        upbit.sell_market_order(krw_coin57, krw_balance57)

                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode57 = True

                        # 1초 딜레이
                        #time.sleep(1)
                        # 보유수량 불러오기
                        krw_balance57 = upbit.get_balance(krw_coin57)
                        # 코인 현재가 불러오기
                        price57 = pyupbit.get_current_price(krw_coin57)
                        # 보유코인 원화금액으로 계산하기
                        bp57 = price57 * krw_balance57

                        # 보유 및 매수 가능 출력.
                        print(f"[ 57. {krw_coin57} 매도완료. ]")
                        print(f"매도시간 : {now}  |  코인명 : {coin57}  |  현재가 = ￦{price57}  |  MACD = ￦{macd57}  |  보유수량 = {krw_balance57}  |  평가금액 = ￦{bp57}")
                        print(f"매수가능 : {op_mode57} - 가능")
                        print("")

                    else:   # 보유코인 평가 금액이 10,100원 이하일때
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode57 = True

                        print(f"[ 57. {krw_coin57} 보유코인이 없으므로 매도불가. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin57}")
                        print(f"매수가능 : {op_mode57} - 가능")
                        print("")

            # 1초 딜레이.
            time.sleep(1)
            ##### 57번 코인 매매 종료 #####
            #############################


            ###############################
            ##### 매매 : 58번코인 시작. #####

            ##### 코인보유현황
            # 보유수량 불러오기
            krw_balance58 = upbit.get_balance(krw_coin58)
            # 코인 현재가 불러오기
            price58 = pyupbit.get_current_price(krw_coin58)
            # 보유코인 원화금액으로 계산하기
            bp58 = price58 * krw_balance58
            # 코인 현황 출력.
            print(f"58. 코인명 : {coin58}  |  현재가 = ￦{price58}  |  보유수량 = {krw_balance58}  |  평가금액 = ￦{bp58}")
            # 코인 보유 유무
            if bp58 > 10100:
                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                op_mode58 = False

                # 보유 및 매수 가능 출력.
                print(f" 코인 보유 : 보유중  |  매수가능 - {op_mode58} - 매수불가")
                print("")
            else:
                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                op_mode58 = True

                # 보유 및 매수 가능 출력.
                print(f" 코인 보유 : 없음  |  매수가능 - {op_mode58} - 매수가능")
                print("")
            #time.sleep(1)


            # 코인 현재가 불러오기
            price58 = pyupbit.get_current_price(krw_coin58)

            # MACD 조회.
            #macd58 = get_macd(krw_coin58)
            # 거래량 동반한 MACD 조회.
            macd58 = get_acc_macd(krw_coin58)
            # 20일 이평선 조회.
            #macd58 = get_ma20(krw_coin58)

            # 매수가능금액 불러오기
            krw58 = upbit.get_balance("KRW")

            # MACD 조건문
#            if macd58 >= 0:     # macd가 0보다 높을때는 매수
#                if op_mode58 == True:    # 매수 가능(True)일 경우 - 매수시도
#                    if krw58 > buy_krw:      # 매수가능금액 krw58 가 매수평균가 buy_krw 보다 클때
#                        if krw58 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
#                            if buy_krw > 10100:     # 매수평균가 buy_krw 가 10,100원 초과일 경우 : 매수
#                                # 매수금액은 매수평균가 buy_krw 로
#                                upbit.buy_market_order(krw_coin58, buy_krw * 0.99)   # 매수가능금액에서 1%를 빼고
#
#                                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
#                                op_mode58 = False
#
#                                # 1초 딜레이
#                                time.sleep(1)
#                                # 보유수량 불러오기
#                                krw_balance58 = upbit.get_balance(krw_coin58)
#                                # 코인 현재가 불러오기
#                                price58 = pyupbit.get_current_price(krw_coin58)
#                                # 보유코인 원화금액으로 계산하기
#                                bp58 = price58 * krw_balance58
#
#                                # 보유 및 매수 가능 출력.
#                                print(f"[ 58. {krw_coin58} 매수완료. ]")
#                                print(f"매수시간 : {now}  |  코인명 : {coin58}  |  현재가 = ￦{price58}  |  MACD = ￦{macd58}  |  보유수량 = {krw_balance58}  |  평가금액 = ￦{bp58}")
#                                print(f"매수가능 : {op_mode58} - 불가")
#                                print("")
#
#                            else:
#                                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
#                                op_mode58 = False
#
#                                print(f"[ 58. {krw_coin58} 잔고부족으로 매수불가. ]")
#                                print(f"현재시간 : {now}  |  코인명 : {coin58}")
#                                print(f"매수가능 : {op_mode58} - 불가")
#                                print("")
#
#                        else:
#                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
#                            op_mode58 = False
#
#                            print(f"[ 58. {krw_coin58} 잔고부족으로 매수불가. ]")
#                            print(f"현재시간 : {now}  |  코인명 : {coin58}")
#                            print(f"매수가능 : {op_mode58} - 불가")
#                            print("")
#
#                    elif krw58 <= buy_krw:   # 매수가능금액 krw58 가 매수평균가 buy_krw 보다 같거나 작을때
#                        if krw58 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
#                            # 매수금액은 매수가능금액인 krw58 로
#                            upbit.buy_market_order(krw_coin58, krw58 * 0.99)   # 매수가능금액에서 1%를 빼고
#
#                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
#                            op_mode58 = False
#
#                            # 1초 딜레이
#                            #time.sleep(1)
#                            # 보유수량 불러오기
#                            krw_balance58 = upbit.get_balance(krw_coin58)
#                            # 코인 현재가 불러오기
#                            price58 = pyupbit.get_current_price(krw_coin58)
#                            # 보유코인 원화금액으로 계산하기
#                            bp58 = price58 * krw_balance58
#
#                            # 보유 및 매수 가능 출력.
#                            print(f"[ 58. {krw_coin58} 매수완료. ]")
#                            print(f"매수시간 : {now}  |  코인명 : {coin58}  |  현재가 = ￦{price58}  |  MACD = ￦{macd58}  |  보유수량 = {krw_balance58}  |  평가금액 = ￦{bp58}")
#                            print(f"매수가능 : {op_mode58} - 불가")
#                            print("")
#
#                        else:
#                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
#                            op_mode58 = False
#
#                            print(f"[ 58. {krw_coin58} 잔고부족으로 매수불가. ]")
#                            print(f"현재시간 : {now}  |  코인명 : {coin58}")
#                            print(f"매수가능 : {op_mode58} - 불가")
#                            print("")
#
#            elif macd58 < 0:       # macd가 0보다 낮을때는 매도
            if macd58 < 0:       # macd가 0보다 낮을때는 매도
                if op_mode58 == False:   # 매수 불가(False)일 경우 - 매도시도
                    # 보유수량 불러오기
                    krw_balance58 = upbit.get_balance(krw_coin58)
                    # 현재가 불러오기
                    price58 = pyupbit.get_current_price(krw_coin58)
                    # 보유코인 원화금액으로 계산하기
                    bp58 = price58 * krw_balance58

                    # 보유코인 원화금액 매도시도
                    if  bp58 > 10100:   # 보유코인 평가 금액이 10,100원 초과일때 - 매도시도
                        # 매도할 코인명 - krw_coin58, 매도할 코인수량 - krw_balance58
                        upbit.sell_market_order(krw_coin58, krw_balance58)

                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode58 = True

                        # 1초 딜레이
                        #time.sleep(1)
                        # 보유수량 불러오기
                        krw_balance58 = upbit.get_balance(krw_coin58)
                        # 코인 현재가 불러오기
                        price58 = pyupbit.get_current_price(krw_coin58)
                        # 보유코인 원화금액으로 계산하기
                        bp58 = price58 * krw_balance58

                        # 보유 및 매수 가능 출력.
                        print(f"[ 58. {krw_coin58} 매도완료. ]")
                        print(f"매도시간 : {now}  |  코인명 : {coin58}  |  현재가 = ￦{price58}  |  MACD = ￦{macd58}  |  보유수량 = {krw_balance58}  |  평가금액 = ￦{bp58}")
                        print(f"매수가능 : {op_mode58} - 가능")
                        print("")

                    else:   # 보유코인 평가 금액이 10,100원 이하일때
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode58 = True

                        print(f"[ 58. {krw_coin58} 보유코인이 없으므로 매도불가. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin58}")
                        print(f"매수가능 : {op_mode58} - 가능")
                        print("")

            # 1초 딜레이.
            time.sleep(1)
            ##### 58번 코인 매매 종료 #####
            #############################


            ###############################
            ##### 매매 : 59번코인 시작. #####

            ##### 코인보유현황
            # 보유수량 불러오기
            krw_balance59 = upbit.get_balance(krw_coin59)
            # 코인 현재가 불러오기
            price59 = pyupbit.get_current_price(krw_coin59)
            # 보유코인 원화금액으로 계산하기
            bp59 = price59 * krw_balance59
            # 코인 현황 출력.
            print(f"59. 코인명 : {coin59}  |  현재가 = ￦{price59}  |  보유수량 = {krw_balance59}  |  평가금액 = ￦{bp59}")
            # 코인 보유 유무
            if bp59 > 10100:
                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                op_mode59 = False

                # 보유 및 매수 가능 출력.
                print(f" 코인 보유 : 보유중  |  매수가능 - {op_mode59} - 매수불가")
                print("")
            else:
                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                op_mode59 = True

                # 보유 및 매수 가능 출력.
                print(f" 코인 보유 : 없음  |  매수가능 - {op_mode59} - 매수가능")
                print("")
            #time.sleep(1)


            # 코인 현재가 불러오기
            price59 = pyupbit.get_current_price(krw_coin59)

            # MACD 조회.
            #macd59 = get_macd(krw_coin59)
            # 거래량 동반한 MACD 조회.
            macd59 = get_acc_macd(krw_coin59)
            # 20일 이평선 조회.
            #macd59 = get_ma20(krw_coin59)

            # 매수가능금액 불러오기
            krw59 = upbit.get_balance("KRW")

            # MACD 조건문
#            if macd59 >= 0:     # macd가 0보다 높을때는 매수
#                if op_mode59 == True:    # 매수 가능(True)일 경우 - 매수시도
#                    if krw59 > buy_krw:      # 매수가능금액 krw59 가 매수평균가 buy_krw 보다 클때
#                        if krw59 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
#                            if buy_krw > 10100:     # 매수평균가 buy_krw 가 10,100원 초과일 경우 : 매수
#                                # 매수금액은 매수평균가 buy_krw 로
#                                upbit.buy_market_order(krw_coin59, buy_krw * 0.99)   # 매수가능금액에서 1%를 빼고
#
#                                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
#                                op_mode59 = False
#
#                                # 1초 딜레이
#                                time.sleep(1)
#                                # 보유수량 불러오기
#                                krw_balance59 = upbit.get_balance(krw_coin59)
#                                # 코인 현재가 불러오기
#                                price59 = pyupbit.get_current_price(krw_coin59)
#                                # 보유코인 원화금액으로 계산하기
#                                bp59 = price59 * krw_balance59
#
#                                # 보유 및 매수 가능 출력.
#                                print(f"[ 59. {krw_coin59} 매수완료. ]")
#                                print(f"매수시간 : {now}  |  코인명 : {coin59}  |  현재가 = ￦{price59}  |  MACD = ￦{macd59}  |  보유수량 = {krw_balance59}  |  평가금액 = ￦{bp59}")
#                                print(f"매수가능 : {op_mode59} - 불가")
#                                print("")
#
#                            else:
#                                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
#                                op_mode59 = False
#
#                                print(f"[ 59. {krw_coin59} 잔고부족으로 매수불가. ]")
#                                print(f"현재시간 : {now}  |  코인명 : {coin59}")
#                                print(f"매수가능 : {op_mode59} - 불가")
#                                print("")
#
#                        else:
#                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
#                            op_mode59 = False
#
#                            print(f"[ 59. {krw_coin59} 잔고부족으로 매수불가. ]")
#                            print(f"현재시간 : {now}  |  코인명 : {coin59}")
#                            print(f"매수가능 : {op_mode59} - 불가")
#                            print("")
#
#                    elif krw59 <= buy_krw:   # 매수가능금액 krw59 가 매수평균가 buy_krw 보다 같거나 작을때
#                        if krw59 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
#                            # 매수금액은 매수가능금액인 krw59 로
#                            upbit.buy_market_order(krw_coin59, krw59 * 0.99)   # 매수가능금액에서 1%를 빼고
#
#                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
#                            op_mode59 = False
#
#                            # 1초 딜레이
#                            #time.sleep(1)
#                            # 보유수량 불러오기
#                            krw_balance59 = upbit.get_balance(krw_coin59)
#                            # 코인 현재가 불러오기
#                            price59 = pyupbit.get_current_price(krw_coin59)
#                            # 보유코인 원화금액으로 계산하기
#                            bp59 = price59 * krw_balance59
#
#                            # 보유 및 매수 가능 출력.
#                            print(f"[ 59. {krw_coin59} 매수완료. ]")
#                            print(f"매수시간 : {now}  |  코인명 : {coin59}  |  현재가 = ￦{price59}  |  MACD = ￦{macd59}  |  보유수량 = {krw_balance59}  |  평가금액 = ￦{bp59}")
#                            print(f"매수가능 : {op_mode59} - 불가")
#                            print("")
#
#                        else:
#                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
#                            op_mode59 = False
#
#                            print(f"[ 59. {krw_coin59} 잔고부족으로 매수불가. ]")
#                            print(f"현재시간 : {now}  |  코인명 : {coin59}")
#                            print(f"매수가능 : {op_mode59} - 불가")
#                            print("")
#
#            elif macd59 < 0:       # macd가 0보다 낮을때는 매도
            if macd59 < 0:       # macd가 0보다 낮을때는 매도
                if op_mode59 == False:   # 매수 불가(False)일 경우 - 매도시도
                    # 보유수량 불러오기
                    krw_balance59 = upbit.get_balance(krw_coin59)
                    # 현재가 불러오기
                    price59 = pyupbit.get_current_price(krw_coin59)
                    # 보유코인 원화금액으로 계산하기
                    bp59 = price59 * krw_balance59

                    # 보유코인 원화금액 매도시도
                    if  bp59 > 10100:   # 보유코인 평가 금액이 10,100원 초과일때 - 매도시도
                        # 매도할 코인명 - krw_coin59, 매도할 코인수량 - krw_balance59
                        upbit.sell_market_order(krw_coin59, krw_balance59)

                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode59 = True

                        # 1초 딜레이
                        #time.sleep(1)
                        # 보유수량 불러오기
                        krw_balance59 = upbit.get_balance(krw_coin59)
                        # 코인 현재가 불러오기
                        price59 = pyupbit.get_current_price(krw_coin59)
                        # 보유코인 원화금액으로 계산하기
                        bp59 = price59 * krw_balance59

                        # 보유 및 매수 가능 출력.
                        print(f"[ 59. {krw_coin59} 매도완료. ]")
                        print(f"매도시간 : {now}  |  코인명 : {coin59}  |  현재가 = ￦{price59}  |  MACD = ￦{macd59}  |  보유수량 = {krw_balance59}  |  평가금액 = ￦{bp59}")
                        print(f"매수가능 : {op_mode59} - 가능")
                        print("")

                    else:   # 보유코인 평가 금액이 10,100원 이하일때
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode59 = True

                        print(f"[ 59. {krw_coin59} 보유코인이 없으므로 매도불가. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin59}")
                        print(f"매수가능 : {op_mode59} - 가능")
                        print("")

            # 1초 딜레이.
            time.sleep(1)
            ##### 59번 코인 매매 종료 #####
            #############################


            ###############################
            ##### 매매 : 60번코인 시작. #####

            ##### 코인보유현황
            # 보유수량 불러오기
            krw_balance60 = upbit.get_balance(krw_coin60)
            # 코인 현재가 불러오기
            price60 = pyupbit.get_current_price(krw_coin60)
            # 보유코인 원화금액으로 계산하기
            bp60 = price60 * krw_balance60
            # 코인 현황 출력.
            print(f"60. 코인명 : {coin60}  |  현재가 = ￦{price60}  |  보유수량 = {krw_balance60}  |  평가금액 = ￦{bp60}")
            # 코인 보유 유무
            if bp60 > 10100:
                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                op_mode60 = False

                # 보유 및 매수 가능 출력.
                print(f" 코인 보유 : 보유중  |  매수가능 - {op_mode60} - 매수불가")
                print("")
            else:
                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                op_mode60 = True

                # 보유 및 매수 가능 출력.
                print(f" 코인 보유 : 없음  |  매수가능 - {op_mode60} - 매수가능")
                print("")
            #time.sleep(1)


            # 코인 현재가 불러오기
            price60 = pyupbit.get_current_price(krw_coin60)

            # MACD 조회.
            #macd60 = get_macd(krw_coin60)
            # 거래량 동반한 MACD 조회.
            macd60 = get_acc_macd(krw_coin60)
            # 20일 이평선 조회.
            #macd60 = get_ma20(krw_coin60)

            # 매수가능금액 불러오기
            krw60 = upbit.get_balance("KRW")

            # MACD 조건문
#            if macd60 >= 0:     # macd가 0보다 높을때는 매수
#                if op_mode60 == True:    # 매수 가능(True)일 경우 - 매수시도
#                    if krw60 > buy_krw:      # 매수가능금액 krw60 가 매수평균가 buy_krw 보다 클때
#                        if krw60 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
#                            if buy_krw > 10100:     # 매수평균가 buy_krw 가 10,100원 초과일 경우 : 매수
#                                # 매수금액은 매수평균가 buy_krw 로
#                                upbit.buy_market_order(krw_coin60, buy_krw * 0.99)   # 매수가능금액에서 1%를 빼고
#
#                                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
#                                op_mode60 = False
#
#                                # 1초 딜레이
#                                time.sleep(1)
#                                # 보유수량 불러오기
#                                krw_balance60 = upbit.get_balance(krw_coin60)
#                                # 코인 현재가 불러오기
#                                price60 = pyupbit.get_current_price(krw_coin60)
#                                # 보유코인 원화금액으로 계산하기
#                                bp60 = price60 * krw_balance60
#
#                                # 보유 및 매수 가능 출력.
#                                print(f"[ 60. {krw_coin60} 매수완료. ]")
#                                print(f"매수시간 : {now}  |  코인명 : {coin60}  |  현재가 = ￦{price60}  |  MACD = ￦{macd60}  |  보유수량 = {krw_balance60}  |  평가금액 = ￦{bp60}")
#                                print(f"매수가능 : {op_mode60} - 불가")
#                                print("")
#
#                            else:
#                                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
#                                op_mode60 = False
#
#                                print(f"[ 60. {krw_coin60} 잔고부족으로 매수불가. ]")
#                                print(f"현재시간 : {now}  |  코인명 : {coin60}")
#                                print(f"매수가능 : {op_mode60} - 불가")
#                                print("")
#
#                        else:
#                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
#                            op_mode60 = False
#
#                            print(f"[ 60. {krw_coin60} 잔고부족으로 매수불가. ]")
#                            print(f"현재시간 : {now}  |  코인명 : {coin60}")
#                            print(f"매수가능 : {op_mode60} - 불가")
#                            print("")
#
#                    elif krw60 <= buy_krw:   # 매수가능금액 krw60 가 매수평균가 buy_krw 보다 같거나 작을때
#                        if krw60 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
#                            # 매수금액은 매수가능금액인 krw60 로
#                            upbit.buy_market_order(krw_coin60, krw60 * 0.99)   # 매수가능금액에서 1%를 빼고
#
#                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
#                            op_mode60 = False
#
#                            # 1초 딜레이
#                            #time.sleep(1)
#                            # 보유수량 불러오기
#                            krw_balance60 = upbit.get_balance(krw_coin60)
#                            # 코인 현재가 불러오기
#                            price60 = pyupbit.get_current_price(krw_coin60)
#                            # 보유코인 원화금액으로 계산하기
#                            bp60 = price60 * krw_balance60
#
#                            # 보유 및 매수 가능 출력.
#                            print(f"[ 60. {krw_coin60} 매수완료. ]")
#                            print(f"매수시간 : {now}  |  코인명 : {coin60}  |  현재가 = ￦{price60}  |  MACD = ￦{macd60}  |  보유수량 = {krw_balance60}  |  평가금액 = ￦{bp60}")
#                            print(f"매수가능 : {op_mode60} - 불가")
#                            print("")
#
#                        else:
#                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
#                            op_mode60 = False
#
#                            print(f"[ 60. {krw_coin60} 잔고부족으로 매수불가. ]")
#                            print(f"현재시간 : {now}  |  코인명 : {coin60}")
#                            print(f"매수가능 : {op_mode60} - 불가")
#                            print("")
#
#            elif macd60 < 0:       # macd가 0보다 낮을때는 매도
            if macd60 < 0:       # macd가 0보다 낮을때는 매도
                if op_mode60 == False:   # 매수 불가(False)일 경우 - 매도시도
                    # 보유수량 불러오기
                    krw_balance60 = upbit.get_balance(krw_coin60)
                    # 현재가 불러오기
                    price60 = pyupbit.get_current_price(krw_coin60)
                    # 보유코인 원화금액으로 계산하기
                    bp60 = price60 * krw_balance60

                    # 보유코인 원화금액 매도시도
                    if  bp60 > 10100:   # 보유코인 평가 금액이 10,100원 초과일때 - 매도시도
                        # 매도할 코인명 - krw_coin60, 매도할 코인수량 - krw_balance60
                        upbit.sell_market_order(krw_coin60, krw_balance60)

                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode60 = True

                        # 1초 딜레이
                        #time.sleep(1)
                        # 보유수량 불러오기
                        krw_balance60 = upbit.get_balance(krw_coin60)
                        # 코인 현재가 불러오기
                        price60 = pyupbit.get_current_price(krw_coin60)
                        # 보유코인 원화금액으로 계산하기
                        bp60 = price60 * krw_balance60

                        # 보유 및 매수 가능 출력.
                        print(f"[ 60. {krw_coin60} 매도완료. ]")
                        print(f"매도시간 : {now}  |  코인명 : {coin60}  |  현재가 = ￦{price60}  |  MACD = ￦{macd60}  |  보유수량 = {krw_balance60}  |  평가금액 = ￦{bp60}")
                        print(f"매수가능 : {op_mode60} - 가능")
                        print("")

                    else:   # 보유코인 평가 금액이 10,100원 이하일때
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode60 = True

                        print(f"[ 60. {krw_coin60} 보유코인이 없으므로 매도불가. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin60}")
                        print(f"매수가능 : {op_mode60} - 가능")
                        print("")

            # 1초 딜레이.
            time.sleep(1)
            ##### 60번 코인 매매 종료 #####
            #############################


            ######################################################################################################################################################
            ######################################################################################################################################################
            ######################################################################################################################################################
            ######################################################################################################################################################
            ######################################################################################################################################################


            ###############################
            ##### 매매 : 61번코인 시작. #####

            ##### 코인보유현황
            # 보유수량 불러오기
            krw_balance61 = upbit.get_balance(krw_coin61)
            # 코인 현재가 불러오기
            price61 = pyupbit.get_current_price(krw_coin61)
            # 보유코인 원화금액으로 계산하기
            bp61 = price61 * krw_balance61
            # 코인 현황 출력.
            print(f"61. 코인명 : {coin61}  |  현재가 = ￦{price61}  |  보유수량 = {krw_balance61}  |  평가금액 = ￦{bp61}")
            # 코인 보유 유무
            if bp61 > 10100:
                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                op_mode61 = False

                # 보유 및 매수 가능 출력.
                print(f" 코인 보유 : 보유중  |  매수가능 - {op_mode61} - 매수불가")
                print("")
            else:
                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                op_mode61 = True

                # 보유 및 매수 가능 출력.
                print(f" 코인 보유 : 없음  |  매수가능 - {op_mode61} - 매수가능")
                print("")
            #time.sleep(1)


            # 코인 현재가 불러오기
            price61 = pyupbit.get_current_price(krw_coin61)

            # MACD 조회.
            #macd61 = get_macd(krw_coin61)
            # 거래량 동반한 MACD 조회.
            macd61 = get_acc_macd(krw_coin61)
            # 20일 이평선 조회.
            #macd61 = get_ma20(krw_coin61)

            # 매수가능금액 불러오기
            krw61 = upbit.get_balance("KRW")

            # MACD 조건문
#            if macd61 >= 0:     # macd가 0보다 높을때는 매수
#                if op_mode61 == True:    # 매수 가능(True)일 경우 - 매수시도
#                    if krw61 > buy_krw:      # 매수가능금액 krw61 가 매수평균가 buy_krw 보다 클때
#                        if krw61 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
#                            if buy_krw > 10100:     # 매수평균가 buy_krw 가 10,100원 초과일 경우 : 매수
#                                # 매수금액은 매수평균가 buy_krw 로
#                                upbit.buy_market_order(krw_coin61, buy_krw * 0.99)   # 매수가능금액에서 1%를 빼고
#
#                                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
#                                op_mode61 = False
#
#                                # 1초 딜레이
#                                time.sleep(1)
#                                # 보유수량 불러오기
#                                krw_balance61 = upbit.get_balance(krw_coin61)
#                                # 코인 현재가 불러오기
#                                price61 = pyupbit.get_current_price(krw_coin61)
#                                # 보유코인 원화금액으로 계산하기
#                                bp61 = price61 * krw_balance61
#
#                                # 보유 및 매수 가능 출력.
#                                print(f"[ 61. {krw_coin61} 매수완료. ]")
#                                print(f"매수시간 : {now}  |  코인명 : {coin61}  |  현재가 = ￦{price61}  |  MACD = ￦{macd61}  |  보유수량 = {krw_balance61}  |  평가금액 = ￦{bp61}")
#                                print(f"매수가능 : {op_mode61} - 불가")
#                                print("")
#
#                            else:
#                                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
#                                op_mode61 = False
#
#                                print(f"[ 61. {krw_coin61} 잔고부족으로 매수불가. ]")
#                                print(f"현재시간 : {now}  |  코인명 : {coin61}")
#                                print(f"매수가능 : {op_mode61} - 불가")
#                                print("")
#
#                        else:
#                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
#                            op_mode61 = False
#
#                            print(f"[ 61. {krw_coin61} 잔고부족으로 매수불가. ]")
#                            print(f"현재시간 : {now}  |  코인명 : {coin61}")
#                            print(f"매수가능 : {op_mode61} - 불가")
#                            print("")
#
#                    elif krw61 <= buy_krw:   # 매수가능금액 krw61 가 매수평균가 buy_krw 보다 같거나 작을때
#                        if krw61 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
#                            # 매수금액은 매수가능금액인 krw61 로
#                            upbit.buy_market_order(krw_coin61, krw61 * 0.99)   # 매수가능금액에서 1%를 빼고
#
#                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
#                            op_mode61 = False
#
#                            # 1초 딜레이
#                            #time.sleep(1)
#                            # 보유수량 불러오기
#                            krw_balance61 = upbit.get_balance(krw_coin61)
#                            # 코인 현재가 불러오기
#                            price61 = pyupbit.get_current_price(krw_coin61)
#                            # 보유코인 원화금액으로 계산하기
#                            bp61 = price61 * krw_balance61
#
#                            # 보유 및 매수 가능 출력.
#                            print(f"[ 61. {krw_coin61} 매수완료. ]")
#                            print(f"매수시간 : {now}  |  코인명 : {coin61}  |  현재가 = ￦{price61}  |  MACD = ￦{macd61}  |  보유수량 = {krw_balance61}  |  평가금액 = ￦{bp61}")
#                            print(f"매수가능 : {op_mode61} - 불가")
#                            print("")
#
#                        else:
#                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
#                            op_mode61 = False
#
#                            print(f"[ 61. {krw_coin61} 잔고부족으로 매수불가. ]")
#                            print(f"현재시간 : {now}  |  코인명 : {coin61}")
#                            print(f"매수가능 : {op_mode61} - 불가")
#                            print("")
#
#            elif macd61 < 0:       # macd가 0보다 낮을때는 매도
            if macd61 < 0:       # macd가 0보다 낮을때는 매도
                if op_mode61 == False:   # 매수 불가(False)일 경우 - 매도시도
                    # 보유수량 불러오기
                    krw_balance61 = upbit.get_balance(krw_coin61)
                    # 현재가 불러오기
                    price61 = pyupbit.get_current_price(krw_coin61)
                    # 보유코인 원화금액으로 계산하기
                    bp61 = price61 * krw_balance61

                    # 보유코인 원화금액 매도시도
                    if  bp61 > 10100:   # 보유코인 평가 금액이 10,100원 초과일때 - 매도시도
                        # 매도할 코인명 - krw_coin61, 매도할 코인수량 - krw_balance61
                        upbit.sell_market_order(krw_coin61, krw_balance61)

                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode61 = True

                        # 1초 딜레이
                        #time.sleep(1)
                        # 보유수량 불러오기
                        krw_balance61 = upbit.get_balance(krw_coin61)
                        # 코인 현재가 불러오기
                        price61 = pyupbit.get_current_price(krw_coin61)
                        # 보유코인 원화금액으로 계산하기
                        bp61 = price61 * krw_balance61

                        # 보유 및 매수 가능 출력.
                        print(f"[ 61. {krw_coin61} 매도완료. ]")
                        print(f"매도시간 : {now}  |  코인명 : {coin61}  |  현재가 = ￦{price61}  |  MACD = ￦{macd61}  |  보유수량 = {krw_balance61}  |  평가금액 = ￦{bp61}")
                        print(f"매수가능 : {op_mode61} - 가능")
                        print("")

                    else:   # 보유코인 평가 금액이 10,100원 이하일때
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode61 = True

                        print(f"[ 61. {krw_coin61} 보유코인이 없으므로 매도불가. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin61}")
                        print(f"매수가능 : {op_mode61} - 가능")
                        print("")

            # 1초 딜레이.
            time.sleep(1)
            ##### 61번 코인 매매 종료 #####
            #############################


            ###############################
            ##### 매매 : 62번코인 시작. #####

            ##### 코인보유현황
            # 보유수량 불러오기
            krw_balance62 = upbit.get_balance(krw_coin62)
            # 코인 현재가 불러오기
            price62 = pyupbit.get_current_price(krw_coin62)
            # 보유코인 원화금액으로 계산하기
            bp62 = price62 * krw_balance62
            # 코인 현황 출력.
            print(f"62. 코인명 : {coin62}  |  현재가 = ￦{price62}  |  보유수량 = {krw_balance62}  |  평가금액 = ￦{bp62}")
            # 코인 보유 유무
            if bp62 > 10100:
                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                op_mode62 = False

                # 보유 및 매수 가능 출력.
                print(f" 코인 보유 : 보유중  |  매수가능 - {op_mode62} - 매수불가")
                print("")
            else:
                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                op_mode62 = True

                # 보유 및 매수 가능 출력.
                print(f" 코인 보유 : 없음  |  매수가능 - {op_mode62} - 매수가능")
                print("")
            #time.sleep(1)


            # 코인 현재가 불러오기
            price62 = pyupbit.get_current_price(krw_coin62)

            # MACD 조회.
            #macd62 = get_macd(krw_coin62)
            # 거래량 동반한 MACD 조회.
            macd62 = get_acc_macd(krw_coin62)
            # 20일 이평선 조회.
            #macd62 = get_ma20(krw_coin62)

            # 매수가능금액 불러오기
            krw62 = upbit.get_balance("KRW")

            # MACD 조건문
#            if macd62 >= 0:     # macd가 0보다 높을때는 매수
#                if op_mode62 == True:    # 매수 가능(True)일 경우 - 매수시도
#                    if krw62 > buy_krw:      # 매수가능금액 krw62 가 매수평균가 buy_krw 보다 클때
#                        if krw62 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
#                            if buy_krw > 10100:     # 매수평균가 buy_krw 가 10,100원 초과일 경우 : 매수
#                                # 매수금액은 매수평균가 buy_krw 로
#                                upbit.buy_market_order(krw_coin62, buy_krw * 0.99)   # 매수가능금액에서 1%를 빼고
#
#                                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
#                                op_mode62 = False
#
#                                # 1초 딜레이
#                                time.sleep(1)
#                                # 보유수량 불러오기
#                                krw_balance62 = upbit.get_balance(krw_coin62)
#                                # 코인 현재가 불러오기
#                                price62 = pyupbit.get_current_price(krw_coin62)
#                                # 보유코인 원화금액으로 계산하기
#                                bp62 = price62 * krw_balance62
#
#                                # 보유 및 매수 가능 출력.
#                                print(f"[ 62. {krw_coin62} 매수완료. ]")
#                                print(f"매수시간 : {now}  |  코인명 : {coin62}  |  현재가 = ￦{price62}  |  MACD = ￦{macd62}  |  보유수량 = {krw_balance62}  |  평가금액 = ￦{bp62}")
#                                print(f"매수가능 : {op_mode62} - 불가")
#                                print("")
#
#                            else:
#                                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
#                                op_mode62 = False
#
#                                print(f"[ 62. {krw_coin62} 잔고부족으로 매수불가. ]")
#                                print(f"현재시간 : {now}  |  코인명 : {coin62}")
#                                print(f"매수가능 : {op_mode62} - 불가")
#                                print("")
#
#                        else:
#                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
#                            op_mode62 = False
#
#                            print(f"[ 62. {krw_coin62} 잔고부족으로 매수불가. ]")
#                            print(f"현재시간 : {now}  |  코인명 : {coin62}")
#                            print(f"매수가능 : {op_mode62} - 불가")
#                            print("")
#
#                    elif krw62 <= buy_krw:   # 매수가능금액 krw62 가 매수평균가 buy_krw 보다 같거나 작을때
#                        if krw62 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
#                            # 매수금액은 매수가능금액인 krw62 로
#                            upbit.buy_market_order(krw_coin62, krw62 * 0.99)   # 매수가능금액에서 1%를 빼고
#
#                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
#                            op_mode62 = False
#
#                            # 1초 딜레이
#                            #time.sleep(1)
#                            # 보유수량 불러오기
#                            krw_balance62 = upbit.get_balance(krw_coin62)
#                            # 코인 현재가 불러오기
#                            price62 = pyupbit.get_current_price(krw_coin62)
#                            # 보유코인 원화금액으로 계산하기
#                            bp62 = price62 * krw_balance62
#
#                            # 보유 및 매수 가능 출력.
#                            print(f"[ 62. {krw_coin62} 매수완료. ]")
#                            print(f"매수시간 : {now}  |  코인명 : {coin62}  |  현재가 = ￦{price62}  |  MACD = ￦{macd62}  |  보유수량 = {krw_balance62}  |  평가금액 = ￦{bp62}")
#                            print(f"매수가능 : {op_mode62} - 불가")
#                            print("")
#
#                        else:
#                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
#                            op_mode62 = False
#
#                            print(f"[ 62. {krw_coin62} 잔고부족으로 매수불가. ]")
#                            print(f"현재시간 : {now}  |  코인명 : {coin62}")
#                            print(f"매수가능 : {op_mode62} - 불가")
#                            print("")
#
#            elif macd62 < 0:       # macd가 0보다 낮을때는 매도
            if macd62 < 0:       # macd가 0보다 낮을때는 매도
                if op_mode62 == False:   # 매수 불가(False)일 경우 - 매도시도
                    # 보유수량 불러오기
                    krw_balance62 = upbit.get_balance(krw_coin62)
                    # 현재가 불러오기
                    price62 = pyupbit.get_current_price(krw_coin62)
                    # 보유코인 원화금액으로 계산하기
                    bp62 = price62 * krw_balance62

                    # 보유코인 원화금액 매도시도
                    if  bp62 > 10100:   # 보유코인 평가 금액이 10,100원 초과일때 - 매도시도
                        # 매도할 코인명 - krw_coin62, 매도할 코인수량 - krw_balance62
                        upbit.sell_market_order(krw_coin62, krw_balance62)

                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode62 = True

                        # 1초 딜레이
                        #time.sleep(1)
                        # 보유수량 불러오기
                        krw_balance62 = upbit.get_balance(krw_coin62)
                        # 코인 현재가 불러오기
                        price62 = pyupbit.get_current_price(krw_coin62)
                        # 보유코인 원화금액으로 계산하기
                        bp62 = price62 * krw_balance62

                        # 보유 및 매수 가능 출력.
                        print(f"[ 62. {krw_coin62} 매도완료. ]")
                        print(f"매도시간 : {now}  |  코인명 : {coin62}  |  현재가 = ￦{price62}  |  MACD = ￦{macd62}  |  보유수량 = {krw_balance62}  |  평가금액 = ￦{bp62}")
                        print(f"매수가능 : {op_mode62} - 가능")
                        print("")

                    else:   # 보유코인 평가 금액이 10,100원 이하일때
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode62 = True

                        print(f"[ 62. {krw_coin62} 보유코인이 없으므로 매도불가. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin62}")
                        print(f"매수가능 : {op_mode62} - 가능")
                        print("")

            # 1초 딜레이.
            time.sleep(1)
            ##### 62번 코인 매매 종료 #####
            #############################


            ###############################
            ##### 매매 : 63번코인 시작. #####

            ##### 코인보유현황
            # 보유수량 불러오기
            krw_balance63 = upbit.get_balance(krw_coin63)
            # 코인 현재가 불러오기
            price63 = pyupbit.get_current_price(krw_coin63)
            # 보유코인 원화금액으로 계산하기
            bp63 = price63 * krw_balance63
            # 코인 현황 출력.
            print(f"63. 코인명 : {coin63}  |  현재가 = ￦{price63}  |  보유수량 = {krw_balance63}  |  평가금액 = ￦{bp63}")
            # 코인 보유 유무
            if bp63 > 10100:
                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                op_mode63 = False

                # 보유 및 매수 가능 출력.
                print(f" 코인 보유 : 보유중  |  매수가능 - {op_mode63} - 매수불가")
                print("")
            else:
                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                op_mode63 = True

                # 보유 및 매수 가능 출력.
                print(f" 코인 보유 : 없음  |  매수가능 - {op_mode63} - 매수가능")
                print("")
            #time.sleep(1)


            # 코인 현재가 불러오기
            price63 = pyupbit.get_current_price(krw_coin63)

            # MACD 조회.
            #macd63 = get_macd(krw_coin63)
            # 거래량 동반한 MACD 조회.
            macd63 = get_acc_macd(krw_coin63)
            # 20일 이평선 조회.
            #macd63 = get_ma20(krw_coin63)

            # 매수가능금액 불러오기
            krw63 = upbit.get_balance("KRW")

            # MACD 조건문
#            if macd63 >= 0:     # macd가 0보다 높을때는 매수
#                if op_mode63 == True:    # 매수 가능(True)일 경우 - 매수시도
#                    if krw63 > buy_krw:      # 매수가능금액 krw63 가 매수평균가 buy_krw 보다 클때
#                        if krw63 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
#                            if buy_krw > 10100:     # 매수평균가 buy_krw 가 10,100원 초과일 경우 : 매수
#                                # 매수금액은 매수평균가 buy_krw 로
#                                upbit.buy_market_order(krw_coin63, buy_krw * 0.99)   # 매수가능금액에서 1%를 빼고
#
#                                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
#                                op_mode63 = False
#
#                                # 1초 딜레이
#                                time.sleep(1)
#                                # 보유수량 불러오기
#                                krw_balance63 = upbit.get_balance(krw_coin63)
#                                # 코인 현재가 불러오기
#                                price63 = pyupbit.get_current_price(krw_coin63)
#                                # 보유코인 원화금액으로 계산하기
#                                bp63 = price63 * krw_balance63
#
#                                # 보유 및 매수 가능 출력.
#                                print(f"[ 63. {krw_coin63} 매수완료. ]")
#                                print(f"매수시간 : {now}  |  코인명 : {coin63}  |  현재가 = ￦{price63}  |  MACD = ￦{macd63}  |  보유수량 = {krw_balance63}  |  평가금액 = ￦{bp63}")
#                                print(f"매수가능 : {op_mode63} - 불가")
#                                print("")
#
#                            else:
#                                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
#                                op_mode63 = False
#
#                                print(f"[ 63. {krw_coin63} 잔고부족으로 매수불가. ]")
#                                print(f"현재시간 : {now}  |  코인명 : {coin63}")
#                                print(f"매수가능 : {op_mode63} - 불가")
#                                print("")
#
#                        else:
#                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
#                            op_mode63 = False
#
#                            print(f"[ 63. {krw_coin63} 잔고부족으로 매수불가. ]")
#                            print(f"현재시간 : {now}  |  코인명 : {coin63}")
#                            print(f"매수가능 : {op_mode63} - 불가")
#                            print("")
#
#                    elif krw63 <= buy_krw:   # 매수가능금액 krw63 가 매수평균가 buy_krw 보다 같거나 작을때
#                        if krw63 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
#                            # 매수금액은 매수가능금액인 krw63 로
#                            upbit.buy_market_order(krw_coin63, krw63 * 0.99)   # 매수가능금액에서 1%를 빼고
#
#                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
#                            op_mode63 = False
#
#                            # 1초 딜레이
#                            #time.sleep(1)
#                            # 보유수량 불러오기
#                            krw_balance63 = upbit.get_balance(krw_coin63)
#                            # 코인 현재가 불러오기
#                            price63 = pyupbit.get_current_price(krw_coin63)
#                            # 보유코인 원화금액으로 계산하기
#                            bp63 = price63 * krw_balance63
#
#                            # 보유 및 매수 가능 출력.
#                            print(f"[ 63. {krw_coin63} 매수완료. ]")
#                            print(f"매수시간 : {now}  |  코인명 : {coin63}  |  현재가 = ￦{price63}  |  MACD = ￦{macd63}  |  보유수량 = {krw_balance63}  |  평가금액 = ￦{bp63}")
#                            print(f"매수가능 : {op_mode63} - 불가")
#                            print("")
#
#                        else:
#                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
#                            op_mode63 = False
#
#                            print(f"[ 63. {krw_coin63} 잔고부족으로 매수불가. ]")
#                            print(f"현재시간 : {now}  |  코인명 : {coin63}")
#                            print(f"매수가능 : {op_mode63} - 불가")
#                            print("")
#
#            elif macd63 < 0:       # macd가 0보다 낮을때는 매도
            if macd63 < 0:       # macd가 0보다 낮을때는 매도
                if op_mode63 == False:   # 매수 불가(False)일 경우 - 매도시도
                    # 보유수량 불러오기
                    krw_balance63 = upbit.get_balance(krw_coin63)
                    # 현재가 불러오기
                    price63 = pyupbit.get_current_price(krw_coin63)
                    # 보유코인 원화금액으로 계산하기
                    bp63 = price63 * krw_balance63

                    # 보유코인 원화금액 매도시도
                    if  bp63 > 10100:   # 보유코인 평가 금액이 10,100원 초과일때 - 매도시도
                        # 매도할 코인명 - krw_coin63, 매도할 코인수량 - krw_balance63
                        upbit.sell_market_order(krw_coin63, krw_balance63)

                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode63 = True

                        # 1초 딜레이
                        #time.sleep(1)
                        # 보유수량 불러오기
                        krw_balance63 = upbit.get_balance(krw_coin63)
                        # 코인 현재가 불러오기
                        price63 = pyupbit.get_current_price(krw_coin63)
                        # 보유코인 원화금액으로 계산하기
                        bp63 = price63 * krw_balance63

                        # 보유 및 매수 가능 출력.
                        print(f"[ 63. {krw_coin63} 매도완료. ]")
                        print(f"매도시간 : {now}  |  코인명 : {coin63}  |  현재가 = ￦{price63}  |  MACD = ￦{macd63}  |  보유수량 = {krw_balance63}  |  평가금액 = ￦{bp63}")
                        print(f"매수가능 : {op_mode63} - 가능")
                        print("")

                    else:   # 보유코인 평가 금액이 10,100원 이하일때
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode63 = True

                        print(f"[ 63. {krw_coin63} 보유코인이 없으므로 매도불가. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin63}")
                        print(f"매수가능 : {op_mode63} - 가능")
                        print("")

            # 1초 딜레이.
            time.sleep(1)
            ##### 63번 코인 매매 종료 #####
            #############################


            ###############################
            ##### 매매 : 64번코인 시작. #####

            ##### 코인보유현황
            # 보유수량 불러오기
            krw_balance64 = upbit.get_balance(krw_coin64)
            # 코인 현재가 불러오기
            price64 = pyupbit.get_current_price(krw_coin64)
            # 보유코인 원화금액으로 계산하기
            bp64 = price64 * krw_balance64
            # 코인 현황 출력.
            print(f"64. 코인명 : {coin64}  |  현재가 = ￦{price64}  |  보유수량 = {krw_balance64}  |  평가금액 = ￦{bp64}")
            # 코인 보유 유무
            if bp64 > 10100:
                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                op_mode64 = False

                # 보유 및 매수 가능 출력.
                print(f" 코인 보유 : 보유중  |  매수가능 - {op_mode64} - 매수불가")
                print("")
            else:
                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                op_mode64 = True

                # 보유 및 매수 가능 출력.
                print(f" 코인 보유 : 없음  |  매수가능 - {op_mode64} - 매수가능")
                print("")
            #time.sleep(1)


            # 코인 현재가 불러오기
            price64 = pyupbit.get_current_price(krw_coin64)

            # MACD 조회.
            #macd64 = get_macd(krw_coin64)
            # 거래량 동반한 MACD 조회.
            macd64 = get_acc_macd(krw_coin64)
            # 20일 이평선 조회.
            #macd64 = get_ma20(krw_coin64)

            # 매수가능금액 불러오기
            krw64 = upbit.get_balance("KRW")

            # MACD 조건문
#            if macd64 >= 0:     # macd가 0보다 높을때는 매수
#                if op_mode64 == True:    # 매수 가능(True)일 경우 - 매수시도
#                    if krw64 > buy_krw:      # 매수가능금액 krw64 가 매수평균가 buy_krw 보다 클때
#                        if krw64 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
#                            if buy_krw > 10100:     # 매수평균가 buy_krw 가 10,100원 초과일 경우 : 매수
#                                # 매수금액은 매수평균가 buy_krw 로
#                                upbit.buy_market_order(krw_coin64, buy_krw * 0.99)   # 매수가능금액에서 1%를 빼고
#
#                                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
#                                op_mode64 = False
#
#                                # 1초 딜레이
#                                time.sleep(1)
#                                # 보유수량 불러오기
#                                krw_balance64 = upbit.get_balance(krw_coin64)
#                                # 코인 현재가 불러오기
#                                price64 = pyupbit.get_current_price(krw_coin64)
#                                # 보유코인 원화금액으로 계산하기
#                                bp64 = price64 * krw_balance64
#
#                                # 보유 및 매수 가능 출력.
#                                print(f"[ 64. {krw_coin64} 매수완료. ]")
#                                print(f"매수시간 : {now}  |  코인명 : {coin64}  |  현재가 = ￦{price64}  |  MACD = ￦{macd64}  |  보유수량 = {krw_balance64}  |  평가금액 = ￦{bp64}")
#                                print(f"매수가능 : {op_mode64} - 불가")
#                                print("")
#
#                            else:
#                                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
#                                op_mode64 = False
#
#                                print(f"[ 64. {krw_coin64} 잔고부족으로 매수불가. ]")
#                                print(f"현재시간 : {now}  |  코인명 : {coin64}")
#                                print(f"매수가능 : {op_mode64} - 불가")
#                                print("")
#
#                        else:
#                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
#                            op_mode64 = False
#
#                            print(f"[ 64. {krw_coin64} 잔고부족으로 매수불가. ]")
#                            print(f"현재시간 : {now}  |  코인명 : {coin64}")
#                            print(f"매수가능 : {op_mode64} - 불가")
#                            print("")
#
#                    elif krw64 <= buy_krw:   # 매수가능금액 krw64 가 매수평균가 buy_krw 보다 같거나 작을때
#                        if krw64 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
#                            # 매수금액은 매수가능금액인 krw64 로
#                            upbit.buy_market_order(krw_coin64, krw64 * 0.99)   # 매수가능금액에서 1%를 빼고
#
#                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
#                            op_mode64 = False
#
#                            # 1초 딜레이
#                            #time.sleep(1)
#                            # 보유수량 불러오기
#                            krw_balance64 = upbit.get_balance(krw_coin64)
#                            # 코인 현재가 불러오기
#                            price64 = pyupbit.get_current_price(krw_coin64)
#                            # 보유코인 원화금액으로 계산하기
#                            bp64 = price64 * krw_balance64
#
#                            # 보유 및 매수 가능 출력.
#                            print(f"[ 64. {krw_coin64} 매수완료. ]")
#                            print(f"매수시간 : {now}  |  코인명 : {coin64}  |  현재가 = ￦{price64}  |  MACD = ￦{macd64}  |  보유수량 = {krw_balance64}  |  평가금액 = ￦{bp64}")
#                            print(f"매수가능 : {op_mode64} - 불가")
#                            print("")
#
#                        else:
#                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
#                            op_mode64 = False
#
#                            print(f"[ 64. {krw_coin64} 잔고부족으로 매수불가. ]")
#                            print(f"현재시간 : {now}  |  코인명 : {coin64}")
#                            print(f"매수가능 : {op_mode64} - 불가")
#                            print("")
#
#            elif macd64 < 0:       # macd가 0보다 낮을때는 매도
            if macd64 < 0:       # macd가 0보다 낮을때는 매도
                if op_mode64 == False:   # 매수 불가(False)일 경우 - 매도시도
                    # 보유수량 불러오기
                    krw_balance64 = upbit.get_balance(krw_coin64)
                    # 현재가 불러오기
                    price64 = pyupbit.get_current_price(krw_coin64)
                    # 보유코인 원화금액으로 계산하기
                    bp64 = price64 * krw_balance64

                    # 보유코인 원화금액 매도시도
                    if  bp64 > 10100:   # 보유코인 평가 금액이 10,100원 초과일때 - 매도시도
                        # 매도할 코인명 - krw_coin64, 매도할 코인수량 - krw_balance64
                        upbit.sell_market_order(krw_coin64, krw_balance64)

                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode64 = True

                        # 1초 딜레이
                        #time.sleep(1)
                        # 보유수량 불러오기
                        krw_balance64 = upbit.get_balance(krw_coin64)
                        # 코인 현재가 불러오기
                        price64 = pyupbit.get_current_price(krw_coin64)
                        # 보유코인 원화금액으로 계산하기
                        bp64 = price64 * krw_balance64

                        # 보유 및 매수 가능 출력.
                        print(f"[ 64. {krw_coin64} 매도완료. ]")
                        print(f"매도시간 : {now}  |  코인명 : {coin64}  |  현재가 = ￦{price64}  |  MACD = ￦{macd64}  |  보유수량 = {krw_balance64}  |  평가금액 = ￦{bp64}")
                        print(f"매수가능 : {op_mode64} - 가능")
                        print("")

                    else:   # 보유코인 평가 금액이 10,100원 이하일때
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode64 = True

                        print(f"[ 64. {krw_coin64} 보유코인이 없으므로 매도불가. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin64}")
                        print(f"매수가능 : {op_mode64} - 가능")
                        print("")

            # 1초 딜레이.
            time.sleep(1)
            ##### 64번 코인 매매 종료 #####
            #############################


            ###############################
            ##### 매매 : 65번코인 시작. #####

            ##### 코인보유현황
            # 보유수량 불러오기
            krw_balance65 = upbit.get_balance(krw_coin65)
            # 코인 현재가 불러오기
            price65 = pyupbit.get_current_price(krw_coin65)
            # 보유코인 원화금액으로 계산하기
            bp65 = price65 * krw_balance65
            # 코인 현황 출력.
            print(f"65. 코인명 : {coin65}  |  현재가 = ￦{price65}  |  보유수량 = {krw_balance65}  |  평가금액 = ￦{bp65}")
            # 코인 보유 유무
            if bp65 > 10100:
                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                op_mode65 = False

                # 보유 및 매수 가능 출력.
                print(f" 코인 보유 : 보유중  |  매수가능 - {op_mode65} - 매수불가")
                print("")
            else:
                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                op_mode65 = True

                # 보유 및 매수 가능 출력.
                print(f" 코인 보유 : 없음  |  매수가능 - {op_mode65} - 매수가능")
                print("")
            #time.sleep(1)


            # 코인 현재가 불러오기
            price65 = pyupbit.get_current_price(krw_coin65)

            # MACD 조회.
            #macd65 = get_macd(krw_coin65)
            # 거래량 동반한 MACD 조회.
            macd65 = get_acc_macd(krw_coin65)
            # 20일 이평선 조회.
            #macd65 = get_ma20(krw_coin65)

            # 매수가능금액 불러오기
            krw65 = upbit.get_balance("KRW")

            # MACD 조건문
#            if macd65 >= 0:     # macd가 0보다 높을때는 매수
#                if op_mode65 == True:    # 매수 가능(True)일 경우 - 매수시도
#                    if krw65 > buy_krw:      # 매수가능금액 krw65 가 매수평균가 buy_krw 보다 클때
#                        if krw65 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
#                            if buy_krw > 10100:     # 매수평균가 buy_krw 가 10,100원 초과일 경우 : 매수
#                                # 매수금액은 매수평균가 buy_krw 로
#                                upbit.buy_market_order(krw_coin65, buy_krw * 0.99)   # 매수가능금액에서 1%를 빼고
#
#                                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
#                                op_mode65 = False
#
#                                # 1초 딜레이
#                                time.sleep(1)
#                                # 보유수량 불러오기
#                                krw_balance65 = upbit.get_balance(krw_coin65)
#                                # 코인 현재가 불러오기
#                                price65 = pyupbit.get_current_price(krw_coin65)
#                                # 보유코인 원화금액으로 계산하기
#                                bp65 = price65 * krw_balance65
#
#                                # 보유 및 매수 가능 출력.
#                                print(f"[ 65. {krw_coin65} 매수완료. ]")
#                                print(f"매수시간 : {now}  |  코인명 : {coin65}  |  현재가 = ￦{price65}  |  MACD = ￦{macd65}  |  보유수량 = {krw_balance65}  |  평가금액 = ￦{bp65}")
#                                print(f"매수가능 : {op_mode65} - 불가")
#                                print("")
#
#                            else:
#                                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
#                                op_mode65 = False
#
#                                print(f"[ 65. {krw_coin65} 잔고부족으로 매수불가. ]")
#                                print(f"현재시간 : {now}  |  코인명 : {coin65}")
#                                print(f"매수가능 : {op_mode65} - 불가")
#                                print("")
#
#                        else:
#                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
#                            op_mode65 = False
#
#                            print(f"[ 65. {krw_coin65} 잔고부족으로 매수불가. ]")
#                            print(f"현재시간 : {now}  |  코인명 : {coin65}")
#                            print(f"매수가능 : {op_mode65} - 불가")
#                            print("")
#
#                    elif krw65 <= buy_krw:   # 매수가능금액 krw65 가 매수평균가 buy_krw 보다 같거나 작을때
#                        if krw65 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
#                            # 매수금액은 매수가능금액인 krw65 로
#                            upbit.buy_market_order(krw_coin65, krw65 * 0.99)   # 매수가능금액에서 1%를 빼고
#
#                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
#                            op_mode65 = False
#
#                            # 1초 딜레이
#                            #time.sleep(1)
#                            # 보유수량 불러오기
#                            krw_balance65 = upbit.get_balance(krw_coin65)
#                            # 코인 현재가 불러오기
#                            price65 = pyupbit.get_current_price(krw_coin65)
#                            # 보유코인 원화금액으로 계산하기
#                            bp65 = price65 * krw_balance65
#
#                            # 보유 및 매수 가능 출력.
#                            print(f"[ 65. {krw_coin65} 매수완료. ]")
#                            print(f"매수시간 : {now}  |  코인명 : {coin65}  |  현재가 = ￦{price65}  |  MACD = ￦{macd65}  |  보유수량 = {krw_balance65}  |  평가금액 = ￦{bp65}")
#                            print(f"매수가능 : {op_mode65} - 불가")
#                            print("")
#
#                        else:
#                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
#                            op_mode65 = False
#
#                            print(f"[ 65. {krw_coin65} 잔고부족으로 매수불가. ]")
#                            print(f"현재시간 : {now}  |  코인명 : {coin65}")
#                            print(f"매수가능 : {op_mode65} - 불가")
#                            print("")
#
#            elif macd65 < 0:       # macd가 0보다 낮을때는 매도
            if macd65 < 0:       # macd가 0보다 낮을때는 매도
                if op_mode65 == False:   # 매수 불가(False)일 경우 - 매도시도
                    # 보유수량 불러오기
                    krw_balance65 = upbit.get_balance(krw_coin65)
                    # 현재가 불러오기
                    price65 = pyupbit.get_current_price(krw_coin65)
                    # 보유코인 원화금액으로 계산하기
                    bp65 = price65 * krw_balance65

                    # 보유코인 원화금액 매도시도
                    if  bp65 > 10100:   # 보유코인 평가 금액이 10,100원 초과일때 - 매도시도
                        # 매도할 코인명 - krw_coin65, 매도할 코인수량 - krw_balance65
                        upbit.sell_market_order(krw_coin65, krw_balance65)

                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode65 = True

                        # 1초 딜레이
                        #time.sleep(1)
                        # 보유수량 불러오기
                        krw_balance65 = upbit.get_balance(krw_coin65)
                        # 코인 현재가 불러오기
                        price65 = pyupbit.get_current_price(krw_coin65)
                        # 보유코인 원화금액으로 계산하기
                        bp65 = price65 * krw_balance65

                        # 보유 및 매수 가능 출력.
                        print(f"[ 65. {krw_coin65} 매도완료. ]")
                        print(f"매도시간 : {now}  |  코인명 : {coin65}  |  현재가 = ￦{price65}  |  MACD = ￦{macd65}  |  보유수량 = {krw_balance65}  |  평가금액 = ￦{bp65}")
                        print(f"매수가능 : {op_mode65} - 가능")
                        print("")

                    else:   # 보유코인 평가 금액이 10,100원 이하일때
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode65 = True

                        print(f"[ 65. {krw_coin65} 보유코인이 없으므로 매도불가. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin65}")
                        print(f"매수가능 : {op_mode65} - 가능")
                        print("")

            # 1초 딜레이.
            time.sleep(1)
            ##### 65번 코인 매매 종료 #####
            #############################


            ###############################
            ##### 매매 : 66번코인 시작. #####

            ##### 코인보유현황
            # 보유수량 불러오기
            krw_balance66 = upbit.get_balance(krw_coin66)
            # 코인 현재가 불러오기
            price66 = pyupbit.get_current_price(krw_coin66)
            # 보유코인 원화금액으로 계산하기
            bp66 = price66 * krw_balance66
            # 코인 현황 출력.
            print(f"66. 코인명 : {coin66}  |  현재가 = ￦{price66}  |  보유수량 = {krw_balance66}  |  평가금액 = ￦{bp66}")
            # 코인 보유 유무
            if bp66 > 10100:
                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                op_mode66 = False

                # 보유 및 매수 가능 출력.
                print(f" 코인 보유 : 보유중  |  매수가능 - {op_mode66} - 매수불가")
                print("")
            else:
                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                op_mode66 = True

                # 보유 및 매수 가능 출력.
                print(f" 코인 보유 : 없음  |  매수가능 - {op_mode66} - 매수가능")
                print("")
            #time.sleep(1)


            # 코인 현재가 불러오기
            price66 = pyupbit.get_current_price(krw_coin66)

            # MACD 조회.
            #macd66 = get_macd(krw_coin66)
            # 거래량 동반한 MACD 조회.
            macd66 = get_acc_macd(krw_coin66)
            # 20일 이평선 조회.
            #macd66 = get_ma20(krw_coin66)

            # 매수가능금액 불러오기
            krw66 = upbit.get_balance("KRW")

            # MACD 조건문
#            if macd66 >= 0:     # macd가 0보다 높을때는 매수
#                if op_mode66 == True:    # 매수 가능(True)일 경우 - 매수시도
#                    if krw66 > buy_krw:      # 매수가능금액 krw66 가 매수평균가 buy_krw 보다 클때
#                        if krw66 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
#                            if buy_krw > 10100:     # 매수평균가 buy_krw 가 10,100원 초과일 경우 : 매수
#                                # 매수금액은 매수평균가 buy_krw 로
#                                upbit.buy_market_order(krw_coin66, buy_krw * 0.99)   # 매수가능금액에서 1%를 빼고
#
#                                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
#                                op_mode66 = False
#
#                                # 1초 딜레이
#                                time.sleep(1)
#                                # 보유수량 불러오기
#                                krw_balance66 = upbit.get_balance(krw_coin66)
#                                # 코인 현재가 불러오기
#                                price66 = pyupbit.get_current_price(krw_coin66)
#                                # 보유코인 원화금액으로 계산하기
#                                bp66 = price66 * krw_balance66
#
#                                # 보유 및 매수 가능 출력.
#                                print(f"[ 66. {krw_coin66} 매수완료. ]")
#                                print(f"매수시간 : {now}  |  코인명 : {coin66}  |  현재가 = ￦{price66}  |  MACD = ￦{macd66}  |  보유수량 = {krw_balance66}  |  평가금액 = ￦{bp66}")
#                                print(f"매수가능 : {op_mode66} - 불가")
#                                print("")
#
#                            else:
#                                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
#                                op_mode66 = False
#
#                                print(f"[ 66. {krw_coin66} 잔고부족으로 매수불가. ]")
#                                print(f"현재시간 : {now}  |  코인명 : {coin66}")
#                                print(f"매수가능 : {op_mode66} - 불가")
#                                print("")
#
#                        else:
#                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
#                            op_mode66 = False
#
#                            print(f"[ 66. {krw_coin66} 잔고부족으로 매수불가. ]")
#                            print(f"현재시간 : {now}  |  코인명 : {coin66}")
#                            print(f"매수가능 : {op_mode66} - 불가")
#                            print("")
#
#                    elif krw66 <= buy_krw:   # 매수가능금액 krw66 가 매수평균가 buy_krw 보다 같거나 작을때
#                        if krw66 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
#                            # 매수금액은 매수가능금액인 krw66 로
#                            upbit.buy_market_order(krw_coin66, krw66 * 0.99)   # 매수가능금액에서 1%를 빼고
#
#                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
#                            op_mode66 = False
#
#                            # 1초 딜레이
#                            #time.sleep(1)
#                            # 보유수량 불러오기
#                            krw_balance66 = upbit.get_balance(krw_coin66)
#                            # 코인 현재가 불러오기
#                            price66 = pyupbit.get_current_price(krw_coin66)
#                            # 보유코인 원화금액으로 계산하기
#                            bp66 = price66 * krw_balance66
#
#                            # 보유 및 매수 가능 출력.
#                            print(f"[ 66. {krw_coin66} 매수완료. ]")
#                            print(f"매수시간 : {now}  |  코인명 : {coin66}  |  현재가 = ￦{price66}  |  MACD = ￦{macd66}  |  보유수량 = {krw_balance66}  |  평가금액 = ￦{bp66}")
#                            print(f"매수가능 : {op_mode66} - 불가")
#                            print("")
#
#                        else:
#                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
#                            op_mode66 = False
#
#                            print(f"[ 66. {krw_coin66} 잔고부족으로 매수불가. ]")
#                            print(f"현재시간 : {now}  |  코인명 : {coin66}")
#                            print(f"매수가능 : {op_mode66} - 불가")
#                            print("")
#
#            elif macd66 < 0:       # macd가 0보다 낮을때는 매도
            if macd66 < 0:       # macd가 0보다 낮을때는 매도
                if op_mode66 == False:   # 매수 불가(False)일 경우 - 매도시도
                    # 보유수량 불러오기
                    krw_balance66 = upbit.get_balance(krw_coin66)
                    # 현재가 불러오기
                    price66 = pyupbit.get_current_price(krw_coin66)
                    # 보유코인 원화금액으로 계산하기
                    bp66 = price66 * krw_balance66

                    # 보유코인 원화금액 매도시도
                    if  bp66 > 10100:   # 보유코인 평가 금액이 10,100원 초과일때 - 매도시도
                        # 매도할 코인명 - krw_coin66, 매도할 코인수량 - krw_balance66
                        upbit.sell_market_order(krw_coin66, krw_balance66)

                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode66 = True

                        # 1초 딜레이
                        #time.sleep(1)
                        # 보유수량 불러오기
                        krw_balance66 = upbit.get_balance(krw_coin66)
                        # 코인 현재가 불러오기
                        price66 = pyupbit.get_current_price(krw_coin66)
                        # 보유코인 원화금액으로 계산하기
                        bp66 = price66 * krw_balance66

                        # 보유 및 매수 가능 출력.
                        print(f"[ 66. {krw_coin66} 매도완료. ]")
                        print(f"매도시간 : {now}  |  코인명 : {coin66}  |  현재가 = ￦{price66}  |  MACD = ￦{macd66}  |  보유수량 = {krw_balance66}  |  평가금액 = ￦{bp66}")
                        print(f"매수가능 : {op_mode66} - 가능")
                        print("")

                    else:   # 보유코인 평가 금액이 10,100원 이하일때
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode66 = True

                        print(f"[ 66. {krw_coin66} 보유코인이 없으므로 매도불가. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin66}")
                        print(f"매수가능 : {op_mode66} - 가능")
                        print("")

            # 1초 딜레이.
            time.sleep(1)
            ##### 66번 코인 매매 종료 #####
            #############################


            ###############################
            ##### 매매 : 67번코인 시작. #####

            ##### 코인보유현황
            # 보유수량 불러오기
            krw_balance67 = upbit.get_balance(krw_coin67)
            # 코인 현재가 불러오기
            price67 = pyupbit.get_current_price(krw_coin67)
            # 보유코인 원화금액으로 계산하기
            bp67 = price67 * krw_balance67
            # 코인 현황 출력.
            print(f"67. 코인명 : {coin67}  |  현재가 = ￦{price67}  |  보유수량 = {krw_balance67}  |  평가금액 = ￦{bp67}")
            # 코인 보유 유무
            if bp67 > 10100:
                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                op_mode67 = False

                # 보유 및 매수 가능 출력.
                print(f" 코인 보유 : 보유중  |  매수가능 - {op_mode67} - 매수불가")
                print("")
            else:
                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                op_mode67 = True

                # 보유 및 매수 가능 출력.
                print(f" 코인 보유 : 없음  |  매수가능 - {op_mode67} - 매수가능")
                print("")
            #time.sleep(1)


            # 코인 현재가 불러오기
            price67 = pyupbit.get_current_price(krw_coin67)

            # MACD 조회.
            #macd67 = get_macd(krw_coin67)
            # 거래량 동반한 MACD 조회.
            macd67 = get_acc_macd(krw_coin67)
            # 20일 이평선 조회.
            #macd67 = get_ma20(krw_coin67)

            # 매수가능금액 불러오기
            krw67 = upbit.get_balance("KRW")

            # MACD 조건문
#            if macd67 >= 0:     # macd가 0보다 높을때는 매수
#                if op_mode67 == True:    # 매수 가능(True)일 경우 - 매수시도
#                    if krw67 > buy_krw:      # 매수가능금액 krw67 가 매수평균가 buy_krw 보다 클때
#                        if krw67 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
#                            if buy_krw > 10100:     # 매수평균가 buy_krw 가 10,100원 초과일 경우 : 매수
#                                # 매수금액은 매수평균가 buy_krw 로
#                                upbit.buy_market_order(krw_coin67, buy_krw * 0.99)   # 매수가능금액에서 1%를 빼고
#
#                                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
#                                op_mode67 = False
#
#                                # 1초 딜레이
#                                time.sleep(1)
#                                # 보유수량 불러오기
#                                krw_balance67 = upbit.get_balance(krw_coin67)
#                                # 코인 현재가 불러오기
#                                price67 = pyupbit.get_current_price(krw_coin67)
#                                # 보유코인 원화금액으로 계산하기
#                                bp67 = price67 * krw_balance67
#
#                                # 보유 및 매수 가능 출력.
#                                print(f"[ 67. {krw_coin67} 매수완료. ]")
#                                print(f"매수시간 : {now}  |  코인명 : {coin67}  |  현재가 = ￦{price67}  |  MACD = ￦{macd67}  |  보유수량 = {krw_balance67}  |  평가금액 = ￦{bp67}")
#                                print(f"매수가능 : {op_mode67} - 불가")
#                                print("")
#
#                            else:
#                                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
#                                op_mode67 = False
#
#                                print(f"[ 67. {krw_coin67} 잔고부족으로 매수불가. ]")
#                                print(f"현재시간 : {now}  |  코인명 : {coin67}")
#                                print(f"매수가능 : {op_mode67} - 불가")
#                                print("")
#
#                        else:
#                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
#                            op_mode67 = False
#
#                            print(f"[ 67. {krw_coin67} 잔고부족으로 매수불가. ]")
#                            print(f"현재시간 : {now}  |  코인명 : {coin67}")
#                            print(f"매수가능 : {op_mode67} - 불가")
#                            print("")
#
#                    elif krw67 <= buy_krw:   # 매수가능금액 krw67 가 매수평균가 buy_krw 보다 같거나 작을때
#                        if krw67 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
#                            # 매수금액은 매수가능금액인 krw67 로
#                            upbit.buy_market_order(krw_coin67, krw67 * 0.99)   # 매수가능금액에서 1%를 빼고
#
#                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
#                            op_mode67 = False
#
#                            # 1초 딜레이
#                            #time.sleep(1)
#                            # 보유수량 불러오기
#                            krw_balance67 = upbit.get_balance(krw_coin67)
#                            # 코인 현재가 불러오기
#                            price67 = pyupbit.get_current_price(krw_coin67)
#                            # 보유코인 원화금액으로 계산하기
#                            bp67 = price67 * krw_balance67
#
#                            # 보유 및 매수 가능 출력.
#                            print(f"[ 67. {krw_coin67} 매수완료. ]")
#                            print(f"매수시간 : {now}  |  코인명 : {coin67}  |  현재가 = ￦{price67}  |  MACD = ￦{macd67}  |  보유수량 = {krw_balance67}  |  평가금액 = ￦{bp67}")
#                            print(f"매수가능 : {op_mode67} - 불가")
#                            print("")
#
#                        else:
#                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
#                            op_mode67 = False
#
#                            print(f"[ 67. {krw_coin67} 잔고부족으로 매수불가. ]")
#                            print(f"현재시간 : {now}  |  코인명 : {coin67}")
#                            print(f"매수가능 : {op_mode67} - 불가")
#                            print("")
#
#            elif macd67 < 0:       # macd가 0보다 낮을때는 매도
            if macd67 < 0:       # macd가 0보다 낮을때는 매도
                if op_mode67 == False:   # 매수 불가(False)일 경우 - 매도시도
                    # 보유수량 불러오기
                    krw_balance67 = upbit.get_balance(krw_coin67)
                    # 현재가 불러오기
                    price67 = pyupbit.get_current_price(krw_coin67)
                    # 보유코인 원화금액으로 계산하기
                    bp67 = price67 * krw_balance67

                    # 보유코인 원화금액 매도시도
                    if  bp67 > 10100:   # 보유코인 평가 금액이 10,100원 초과일때 - 매도시도
                        # 매도할 코인명 - krw_coin67, 매도할 코인수량 - krw_balance67
                        upbit.sell_market_order(krw_coin67, krw_balance67)

                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode67 = True

                        # 1초 딜레이
                        #time.sleep(1)
                        # 보유수량 불러오기
                        krw_balance67 = upbit.get_balance(krw_coin67)
                        # 코인 현재가 불러오기
                        price67 = pyupbit.get_current_price(krw_coin67)
                        # 보유코인 원화금액으로 계산하기
                        bp67 = price67 * krw_balance67

                        # 보유 및 매수 가능 출력.
                        print(f"[ 67. {krw_coin67} 매도완료. ]")
                        print(f"매도시간 : {now}  |  코인명 : {coin67}  |  현재가 = ￦{price67}  |  MACD = ￦{macd67}  |  보유수량 = {krw_balance67}  |  평가금액 = ￦{bp67}")
                        print(f"매수가능 : {op_mode67} - 가능")
                        print("")

                    else:   # 보유코인 평가 금액이 10,100원 이하일때
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode67 = True

                        print(f"[ 67. {krw_coin67} 보유코인이 없으므로 매도불가. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin67}")
                        print(f"매수가능 : {op_mode67} - 가능")
                        print("")

            # 1초 딜레이.
            time.sleep(1)
            ##### 67번 코인 매매 종료 #####
            #############################


            ###############################
            ##### 매매 : 68번코인 시작. #####

            ##### 코인보유현황
            # 보유수량 불러오기
            krw_balance68 = upbit.get_balance(krw_coin68)
            # 코인 현재가 불러오기
            price68 = pyupbit.get_current_price(krw_coin68)
            # 보유코인 원화금액으로 계산하기
            bp68 = price68 * krw_balance68
            # 코인 현황 출력.
            print(f"68. 코인명 : {coin68}  |  현재가 = ￦{price68}  |  보유수량 = {krw_balance68}  |  평가금액 = ￦{bp68}")
            # 코인 보유 유무
            if bp68 > 10100:
                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                op_mode68 = False

                # 보유 및 매수 가능 출력.
                print(f" 코인 보유 : 보유중  |  매수가능 - {op_mode68} - 매수불가")
                print("")
            else:
                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                op_mode68 = True

                # 보유 및 매수 가능 출력.
                print(f" 코인 보유 : 없음  |  매수가능 - {op_mode68} - 매수가능")
                print("")
            #time.sleep(1)


            # 코인 현재가 불러오기
            price68 = pyupbit.get_current_price(krw_coin68)

            # MACD 조회.
            #macd68 = get_macd(krw_coin68)
            # 거래량 동반한 MACD 조회.
            macd68 = get_acc_macd(krw_coin68)
            # 20일 이평선 조회.
            #macd68 = get_ma20(krw_coin68)

            # 매수가능금액 불러오기
            krw68 = upbit.get_balance("KRW")

            # MACD 조건문
#            if macd68 >= 0:     # macd가 0보다 높을때는 매수
#                if op_mode68 == True:    # 매수 가능(True)일 경우 - 매수시도
#                    if krw68 > buy_krw:      # 매수가능금액 krw68 가 매수평균가 buy_krw 보다 클때
#                        if krw68 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
#                            if buy_krw > 10100:     # 매수평균가 buy_krw 가 10,100원 초과일 경우 : 매수
#                                # 매수금액은 매수평균가 buy_krw 로
#                                upbit.buy_market_order(krw_coin68, buy_krw * 0.99)   # 매수가능금액에서 1%를 빼고
#
#                                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
#                                op_mode68 = False
#
#                                # 1초 딜레이
#                                time.sleep(1)
#                                # 보유수량 불러오기
#                                krw_balance68 = upbit.get_balance(krw_coin68)
#                                # 코인 현재가 불러오기
#                                price68 = pyupbit.get_current_price(krw_coin68)
#                                # 보유코인 원화금액으로 계산하기
#                                bp68 = price68 * krw_balance68
#
#                                # 보유 및 매수 가능 출력.
#                                print(f"[ 68. {krw_coin68} 매수완료. ]")
#                                print(f"매수시간 : {now}  |  코인명 : {coin68}  |  현재가 = ￦{price68}  |  MACD = ￦{macd68}  |  보유수량 = {krw_balance68}  |  평가금액 = ￦{bp68}")
#                                print(f"매수가능 : {op_mode68} - 불가")
#                                print("")
#
#                            else:
#                                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
#                                op_mode68 = False
#
#                                print(f"[ 68. {krw_coin68} 잔고부족으로 매수불가. ]")
#                                print(f"현재시간 : {now}  |  코인명 : {coin68}")
#                                print(f"매수가능 : {op_mode68} - 불가")
#                                print("")
#
#                        else:
#                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
#                            op_mode68 = False
#
#                            print(f"[ 68. {krw_coin68} 잔고부족으로 매수불가. ]")
#                            print(f"현재시간 : {now}  |  코인명 : {coin68}")
#                            print(f"매수가능 : {op_mode68} - 불가")
#                            print("")
#
#                    elif krw68 <= buy_krw:   # 매수가능금액 krw68 가 매수평균가 buy_krw 보다 같거나 작을때
#                        if krw68 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
#                            # 매수금액은 매수가능금액인 krw68 로
#                            upbit.buy_market_order(krw_coin68, krw68 * 0.99)   # 매수가능금액에서 1%를 빼고
#
#                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
#                            op_mode68 = False
#
#                            # 1초 딜레이
#                            #time.sleep(1)
#                            # 보유수량 불러오기
#                            krw_balance68 = upbit.get_balance(krw_coin68)
#                            # 코인 현재가 불러오기
#                            price68 = pyupbit.get_current_price(krw_coin68)
#                            # 보유코인 원화금액으로 계산하기
#                            bp68 = price68 * krw_balance68
#
#                            # 보유 및 매수 가능 출력.
#                            print(f"[ 68. {krw_coin68} 매수완료. ]")
#                            print(f"매수시간 : {now}  |  코인명 : {coin68}  |  현재가 = ￦{price68}  |  MACD = ￦{macd68}  |  보유수량 = {krw_balance68}  |  평가금액 = ￦{bp68}")
#                            print(f"매수가능 : {op_mode68} - 불가")
#                            print("")
#
#                        else:
#                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
#                            op_mode68 = False
#
#                            print(f"[ 68. {krw_coin68} 잔고부족으로 매수불가. ]")
#                            print(f"현재시간 : {now}  |  코인명 : {coin68}")
#                            print(f"매수가능 : {op_mode68} - 불가")
#                            print("")
#
#            elif macd68 < 0:       # macd가 0보다 낮을때는 매도
            if macd68 < 0:       # macd가 0보다 낮을때는 매도
                if op_mode68 == False:   # 매수 불가(False)일 경우 - 매도시도
                    # 보유수량 불러오기
                    krw_balance68 = upbit.get_balance(krw_coin68)
                    # 현재가 불러오기
                    price68 = pyupbit.get_current_price(krw_coin68)
                    # 보유코인 원화금액으로 계산하기
                    bp68 = price68 * krw_balance68

                    # 보유코인 원화금액 매도시도
                    if  bp68 > 10100:   # 보유코인 평가 금액이 10,100원 초과일때 - 매도시도
                        # 매도할 코인명 - krw_coin68, 매도할 코인수량 - krw_balance68
                        upbit.sell_market_order(krw_coin68, krw_balance68)

                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode68 = True

                        # 1초 딜레이
                        #time.sleep(1)
                        # 보유수량 불러오기
                        krw_balance68 = upbit.get_balance(krw_coin68)
                        # 코인 현재가 불러오기
                        price68 = pyupbit.get_current_price(krw_coin68)
                        # 보유코인 원화금액으로 계산하기
                        bp68 = price68 * krw_balance68

                        # 보유 및 매수 가능 출력.
                        print(f"[ 68. {krw_coin68} 매도완료. ]")
                        print(f"매도시간 : {now}  |  코인명 : {coin68}  |  현재가 = ￦{price68}  |  MACD = ￦{macd68}  |  보유수량 = {krw_balance68}  |  평가금액 = ￦{bp68}")
                        print(f"매수가능 : {op_mode68} - 가능")
                        print("")

                    else:   # 보유코인 평가 금액이 10,100원 이하일때
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode68 = True

                        print(f"[ 68. {krw_coin68} 보유코인이 없으므로 매도불가. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin68}")
                        print(f"매수가능 : {op_mode68} - 가능")
                        print("")

            # 1초 딜레이.
            time.sleep(1)
            ##### 68번 코인 매매 종료 #####
            #############################


            ###############################
            ##### 매매 : 69번코인 시작. #####

            ##### 코인보유현황
            # 보유수량 불러오기
            krw_balance69 = upbit.get_balance(krw_coin69)
            # 코인 현재가 불러오기
            price69 = pyupbit.get_current_price(krw_coin69)
            # 보유코인 원화금액으로 계산하기
            bp69 = price69 * krw_balance69
            # 코인 현황 출력.
            print(f"69. 코인명 : {coin69}  |  현재가 = ￦{price69}  |  보유수량 = {krw_balance69}  |  평가금액 = ￦{bp69}")
            # 코인 보유 유무
            if bp69 > 10100:
                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                op_mode69 = False

                # 보유 및 매수 가능 출력.
                print(f" 코인 보유 : 보유중  |  매수가능 - {op_mode69} - 매수불가")
                print("")
            else:
                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                op_mode69 = True

                # 보유 및 매수 가능 출력.
                print(f" 코인 보유 : 없음  |  매수가능 - {op_mode69} - 매수가능")
                print("")
            #time.sleep(1)


            # 코인 현재가 불러오기
            price69 = pyupbit.get_current_price(krw_coin69)

            # MACD 조회.
            #macd69 = get_macd(krw_coin69)
            # 거래량 동반한 MACD 조회.
            macd69 = get_acc_macd(krw_coin69)
            # 20일 이평선 조회.
            #macd69 = get_ma20(krw_coin69)

            # 매수가능금액 불러오기
            krw69 = upbit.get_balance("KRW")

            # MACD 조건문
#            if macd69 >= 0:     # macd가 0보다 높을때는 매수
#                if op_mode69 == True:    # 매수 가능(True)일 경우 - 매수시도
#                    if krw69 > buy_krw:      # 매수가능금액 krw69 가 매수평균가 buy_krw 보다 클때
#                        if krw69 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
#                            if buy_krw > 10100:     # 매수평균가 buy_krw 가 10,100원 초과일 경우 : 매수
#                                # 매수금액은 매수평균가 buy_krw 로
#                                upbit.buy_market_order(krw_coin69, buy_krw * 0.99)   # 매수가능금액에서 1%를 빼고
#
#                                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
#                                op_mode69 = False
#
#                                # 1초 딜레이
#                                time.sleep(1)
#                                # 보유수량 불러오기
#                                krw_balance69 = upbit.get_balance(krw_coin69)
#                                # 코인 현재가 불러오기
#                                price69 = pyupbit.get_current_price(krw_coin69)
#                                # 보유코인 원화금액으로 계산하기
#                                bp69 = price69 * krw_balance69
#
#                                # 보유 및 매수 가능 출력.
#                                print(f"[ 69. {krw_coin69} 매수완료. ]")
#                                print(f"매수시간 : {now}  |  코인명 : {coin69}  |  현재가 = ￦{price69}  |  MACD = ￦{macd69}  |  보유수량 = {krw_balance69}  |  평가금액 = ￦{bp69}")
#                                print(f"매수가능 : {op_mode69} - 불가")
#                                print("")
#
#                            else:
#                                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
#                                op_mode69 = False
#
#                                print(f"[ 69. {krw_coin69} 잔고부족으로 매수불가. ]")
#                                print(f"현재시간 : {now}  |  코인명 : {coin69}")
#                                print(f"매수가능 : {op_mode69} - 불가")
#                                print("")
#
#                        else:
#                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
#                            op_mode69 = False
#
#                            print(f"[ 69. {krw_coin69} 잔고부족으로 매수불가. ]")
#                            print(f"현재시간 : {now}  |  코인명 : {coin69}")
#                            print(f"매수가능 : {op_mode69} - 불가")
#                            print("")
#
#                    elif krw69 <= buy_krw:   # 매수가능금액 krw69 가 매수평균가 buy_krw 보다 같거나 작을때
#                        if krw69 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
#                            # 매수금액은 매수가능금액인 krw69 로
#                            upbit.buy_market_order(krw_coin69, krw69 * 0.99)   # 매수가능금액에서 1%를 빼고
#
#                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
#                            op_mode69 = False
#
#                            # 1초 딜레이
#                            #time.sleep(1)
#                            # 보유수량 불러오기
#                            krw_balance69 = upbit.get_balance(krw_coin69)
#                            # 코인 현재가 불러오기
#                            price69 = pyupbit.get_current_price(krw_coin69)
#                            # 보유코인 원화금액으로 계산하기
#                            bp69 = price69 * krw_balance69
#
#                            # 보유 및 매수 가능 출력.
#                            print(f"[ 69. {krw_coin69} 매수완료. ]")
#                            print(f"매수시간 : {now}  |  코인명 : {coin69}  |  현재가 = ￦{price69}  |  MACD = ￦{macd69}  |  보유수량 = {krw_balance69}  |  평가금액 = ￦{bp69}")
#                            print(f"매수가능 : {op_mode69} - 불가")
#                            print("")
#
#                        else:
#                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
#                            op_mode69 = False
#
#                            print(f"[ 69. {krw_coin69} 잔고부족으로 매수불가. ]")
#                            print(f"현재시간 : {now}  |  코인명 : {coin69}")
#                            print(f"매수가능 : {op_mode69} - 불가")
#                            print("")
#
#            elif macd69 < 0:       # macd가 0보다 낮을때는 매도
            if macd69 < 0:       # macd가 0보다 낮을때는 매도
                if op_mode69 == False:   # 매수 불가(False)일 경우 - 매도시도
                    # 보유수량 불러오기
                    krw_balance69 = upbit.get_balance(krw_coin69)
                    # 현재가 불러오기
                    price69 = pyupbit.get_current_price(krw_coin69)
                    # 보유코인 원화금액으로 계산하기
                    bp69 = price69 * krw_balance69

                    # 보유코인 원화금액 매도시도
                    if  bp69 > 10100:   # 보유코인 평가 금액이 10,100원 초과일때 - 매도시도
                        # 매도할 코인명 - krw_coin69, 매도할 코인수량 - krw_balance69
                        upbit.sell_market_order(krw_coin69, krw_balance69)

                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode69 = True

                        # 1초 딜레이
                        #time.sleep(1)
                        # 보유수량 불러오기
                        krw_balance69 = upbit.get_balance(krw_coin69)
                        # 코인 현재가 불러오기
                        price69 = pyupbit.get_current_price(krw_coin69)
                        # 보유코인 원화금액으로 계산하기
                        bp69 = price69 * krw_balance69

                        # 보유 및 매수 가능 출력.
                        print(f"[ 69. {krw_coin69} 매도완료. ]")
                        print(f"매도시간 : {now}  |  코인명 : {coin69}  |  현재가 = ￦{price69}  |  MACD = ￦{macd69}  |  보유수량 = {krw_balance69}  |  평가금액 = ￦{bp69}")
                        print(f"매수가능 : {op_mode69} - 가능")
                        print("")

                    else:   # 보유코인 평가 금액이 10,100원 이하일때
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode69 = True

                        print(f"[ 69. {krw_coin69} 보유코인이 없으므로 매도불가. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin69}")
                        print(f"매수가능 : {op_mode69} - 가능")
                        print("")

            # 1초 딜레이.
            time.sleep(1)
            ##### 69번 코인 매매 종료 #####
            #############################


            ###############################
            ##### 매매 : 70번코인 시작. #####

            ##### 코인보유현황
            # 보유수량 불러오기
            krw_balance70 = upbit.get_balance(krw_coin70)
            # 코인 현재가 불러오기
            price70 = pyupbit.get_current_price(krw_coin70)
            # 보유코인 원화금액으로 계산하기
            bp70 = price70 * krw_balance70
            # 코인 현황 출력.
            print(f"70. 코인명 : {coin70}  |  현재가 = ￦{price70}  |  보유수량 = {krw_balance70}  |  평가금액 = ￦{bp70}")
            # 코인 보유 유무
            if bp70 > 10100:
                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                op_mode70 = False

                # 보유 및 매수 가능 출력.
                print(f" 코인 보유 : 보유중  |  매수가능 - {op_mode70} - 매수불가")
                print("")
            else:
                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                op_mode70 = True

                # 보유 및 매수 가능 출력.
                print(f" 코인 보유 : 없음  |  매수가능 - {op_mode70} - 매수가능")
                print("")
            #time.sleep(1)


            # 코인 현재가 불러오기
            price70 = pyupbit.get_current_price(krw_coin70)

            # MACD 조회.
            #macd70 = get_macd(krw_coin70)
            # 거래량 동반한 MACD 조회.
            macd70 = get_acc_macd(krw_coin70)
            # 20일 이평선 조회.
            #macd70 = get_ma20(krw_coin70)

            # 매수가능금액 불러오기
            krw70 = upbit.get_balance("KRW")

            # MACD 조건문
#            if macd70 >= 0:     # macd가 0보다 높을때는 매수
#                if op_mode70 == True:    # 매수 가능(True)일 경우 - 매수시도
#                    if krw70 > buy_krw:      # 매수가능금액 krw70 가 매수평균가 buy_krw 보다 클때
#                        if krw70 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
#                            if buy_krw > 10100:     # 매수평균가 buy_krw 가 10,100원 초과일 경우 : 매수
#                                # 매수금액은 매수평균가 buy_krw 로
#                                upbit.buy_market_order(krw_coin70, buy_krw * 0.99)   # 매수가능금액에서 1%를 빼고
#
#                                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
#                                op_mode70 = False
#
#                                # 1초 딜레이
#                                time.sleep(1)
#                                # 보유수량 불러오기
#                                krw_balance70 = upbit.get_balance(krw_coin70)
#                                # 코인 현재가 불러오기
#                                price70 = pyupbit.get_current_price(krw_coin70)
#                                # 보유코인 원화금액으로 계산하기
#                                bp70 = price70 * krw_balance70
#
#                                # 보유 및 매수 가능 출력.
#                                print(f"[ 70. {krw_coin70} 매수완료. ]")
#                                print(f"매수시간 : {now}  |  코인명 : {coin70}  |  현재가 = ￦{price70}  |  MACD = ￦{macd70}  |  보유수량 = {krw_balance70}  |  평가금액 = ￦{bp70}")
#                                print(f"매수가능 : {op_mode70} - 불가")
#                                print("")
#
#                            else:
#                                # 금일 코인 매수 가능 - 가능 = True , 불가 = False
#                                op_mode70 = False
#
#                                print(f"[ 70. {krw_coin70} 잔고부족으로 매수불가. ]")
#                                print(f"현재시간 : {now}  |  코인명 : {coin70}")
#                                print(f"매수가능 : {op_mode70} - 불가")
#                                print("")
#
#                        else:
#                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
#                            op_mode70 = False
#
#                            print(f"[ 70. {krw_coin70} 잔고부족으로 매수불가. ]")
#                            print(f"현재시간 : {now}  |  코인명 : {coin70}")
#                            print(f"매수가능 : {op_mode70} - 불가")
#                            print("")
#
#                    elif krw70 <= buy_krw:   # 매수가능금액 krw70 가 매수평균가 buy_krw 보다 같거나 작을때
#                        if krw70 > 10100:    # 매수가능금액이 10,100원 초과일 경우: 매수
#                            # 매수금액은 매수가능금액인 krw70 로
#                            upbit.buy_market_order(krw_coin70, krw70 * 0.99)   # 매수가능금액에서 1%를 빼고
#
#                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
#                            op_mode70 = False
#
#                            # 1초 딜레이
#                            #time.sleep(1)
#                            # 보유수량 불러오기
#                            krw_balance70 = upbit.get_balance(krw_coin70)
#                            # 코인 현재가 불러오기
#                            price70 = pyupbit.get_current_price(krw_coin70)
#                            # 보유코인 원화금액으로 계산하기
#                            bp70 = price70 * krw_balance70
#
#                            # 보유 및 매수 가능 출력.
#                            print(f"[ 70. {krw_coin70} 매수완료. ]")
#                            print(f"매수시간 : {now}  |  코인명 : {coin70}  |  현재가 = ￦{price70}  |  MACD = ￦{macd70}  |  보유수량 = {krw_balance70}  |  평가금액 = ￦{bp70}")
#                            print(f"매수가능 : {op_mode70} - 불가")
#                            print("")
#
#                        else:
#                            # 금일 코인 매수 가능 - 가능 = True , 불가 = False
#                            op_mode70 = False
#
#                            print(f"[ 70. {krw_coin70} 잔고부족으로 매수불가. ]")
#                            print(f"현재시간 : {now}  |  코인명 : {coin70}")
#                            print(f"매수가능 : {op_mode70} - 불가")
#                            print("")
#
#            elif macd70 < 0:       # macd가 0보다 낮을때는 매도
            if macd70 < 0:       # macd가 0보다 낮을때는 매도
                if op_mode70 == False:   # 매수 불가(False)일 경우 - 매도시도
                    # 보유수량 불러오기
                    krw_balance70 = upbit.get_balance(krw_coin70)
                    # 현재가 불러오기
                    price70 = pyupbit.get_current_price(krw_coin70)
                    # 보유코인 원화금액으로 계산하기
                    bp70 = price70 * krw_balance70

                    # 보유코인 원화금액 매도시도
                    if  bp70 > 10100:   # 보유코인 평가 금액이 10,100원 초과일때 - 매도시도
                        # 매도할 코인명 - krw_coin70, 매도할 코인수량 - krw_balance70
                        upbit.sell_market_order(krw_coin70, krw_balance70)

                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode70 = True

                        # 1초 딜레이
                        #time.sleep(1)
                        # 보유수량 불러오기
                        krw_balance70 = upbit.get_balance(krw_coin70)
                        # 코인 현재가 불러오기
                        price70 = pyupbit.get_current_price(krw_coin70)
                        # 보유코인 원화금액으로 계산하기
                        bp70 = price70 * krw_balance70

                        # 보유 및 매수 가능 출력.
                        print(f"[ 70. {krw_coin70} 매도완료. ]")
                        print(f"매도시간 : {now}  |  코인명 : {coin70}  |  현재가 = ￦{price70}  |  MACD = ￦{macd70}  |  보유수량 = {krw_balance70}  |  평가금액 = ￦{bp70}")
                        print(f"매수가능 : {op_mode70} - 가능")
                        print("")

                    else:   # 보유코인 평가 금액이 10,100원 이하일때
                        # 금일 코인 매수 가능 - 가능 = True , 불가 = False
                        op_mode70 = True

                        print(f"[ 70. {krw_coin70} 보유코인이 없으므로 매도불가. ]")
                        print(f"현재시간 : {now}  |  코인명 : {coin70}")
                        print(f"매수가능 : {op_mode70} - 가능")
                        print("")

            # 1초 딜레이.
            time.sleep(1)
            ##### 70번 코인 매매 종료 #####
            #############################


            ######################################################################################################################################################
            ######################################################################################################################################################
            ######################################################################################################################################################
            ######################################################################################################################################################
            ######################################################################################################################################################


            # 60초 딜레이.
            time.sleep(60)