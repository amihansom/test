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
# 5, 20 이동평균선 조회.
def get_ma20(ticker):
    # interval 받는 시간 "minute1", "minute5", "minute10", "minute20", "minute60"(1시간), "minute240"(4시간), "day", "week" 등등
    df = pyupbit.get_ohlcv(ticker, interval="minute240", count=30)
    
    # 5 이동평균선
    ma5_1 = df['close'].rolling(5).mean().iloc[-1]
    ma5_2 = df['close'].rolling(5).mean().iloc[-2]
    # 20 이동평균선
    ma20_1 = df['close'].rolling(20).mean().iloc[-1]
    ma20_2 = df['close'].rolling(20).mean().iloc[-2]

    # 20 이동평균선값보다 5 이동평균선이 높으면 양수.
    ma20 = ma5_1 - ma20_1

    return ma20


####################
# 거래량 동반한 5, 20 이동평균선 조회.
def get_acc_ma20(ticker):
    # 링크와 가져오는 캔들 지정 ~minutes/시간 - 1, 5, 10, 20, 60(1시간), 240(4시간), day(1,440분), week(10,080분)
    url = "https://api.upbit.com/v1/candles/minutes/240"

    # 가져올려는 코인명과, 캔들수
    querystring = {"market":ticker,"count":"30"}

    headers = {"Accept": "application/json"}

    response = requests.request("GET", url, headers=headers, params=querystring)


    data = response.json()


    # 종가받기 30개
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


    # 캔들 거래량 30개
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


    ###################################
    ##### 거래량 동반한 macd 산출. #####


    # 캔들 누적거래금액 30개
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


    # 단기 5일 거래량 합산
    acc_volume5_0 = volume_0 + volume_1 + volume_2 + volume_3 + volume_4
    # 여기부터
    acc_volume5_1 = volume_1 + volume_2 + volume_3 + volume_4 + volume_5
    # 여기까지


    # 거래량 동반한 단기 12이평선
    acc_ma5_0 = ( acc_trade_price_0 + acc_trade_price_1 + acc_trade_price_2 + acc_trade_price_3 + acc_trade_price_4 ) / acc_volume5_0
    # 여기부터
    acc_ma5_1 = ( acc_trade_price_1 + acc_trade_price_2 + acc_trade_price_3 + acc_trade_price_4 + acc_trade_price_5 ) / acc_volume5_1
    # 여기까지


    # 장기 20일 거래량 합산
    acc_volume20_0 = volume_0 + volume_1 + volume_2 + volume_3 + volume_4 + volume_5 + volume_6 + volume_7 + volume_8 + volume_9 + volume_10 + volume_11 + volume_12 + volume_13 + volume_14 + volume_15 + volume_16 + volume_17 + volume_18 + volume_19
    # 여기부터
    acc_volume20_1 = volume_1 + volume_2 + volume_3 + volume_4 + volume_5 + volume_6 + volume_7 + volume_8 + volume_9 + volume_10 + volume_11 + volume_12 + volume_13 + volume_14 + volume_15 + volume_16 + volume_17 + volume_18 + volume_19 + volume_20
    # 여기까지


    # 거래량 동반한 장기 20이평선
    acc_ma20_0 = ( acc_trade_price_0 + acc_trade_price_1 + acc_trade_price_2 + acc_trade_price_3 + acc_trade_price_4 + acc_trade_price_5 + acc_trade_price_6 + acc_trade_price_7 + acc_trade_price_8 + acc_trade_price_9 + acc_trade_price_10 + acc_trade_price_11 + acc_trade_price_12 + acc_trade_price_13 + acc_trade_price_14 + acc_trade_price_15 + acc_trade_price_16 + acc_trade_price_17 + acc_trade_price_18 + acc_trade_price_19 ) / acc_volume20_0
    # 여기부터
    acc_ma20_1 = ( acc_trade_price_1 + acc_trade_price_2 + acc_trade_price_3 + acc_trade_price_4 + acc_trade_price_5 + acc_trade_price_6 + acc_trade_price_7 + acc_trade_price_8 + acc_trade_price_9 + acc_trade_price_10 + acc_trade_price_11 + acc_trade_price_12 + acc_trade_price_13 + acc_trade_price_14 + acc_trade_price_15 + acc_trade_price_16 + acc_trade_price_17 + acc_trade_price_18 + acc_trade_price_19 + acc_trade_price_20 ) / acc_volume20_1
    # 여기까지


    # 20 이동평균선값보다 5 이동평균선이 높으면 양수.
    acc_ma5_20 = acc_ma5_1 - acc_ma20_1

    return acc_ma5_20


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

    # 링크와 가져오는 캔들 지정 ~minutes/시간 - 1, 5, 10, 20, 60(1시간), 240(4시간), day(1,440분), week(10,080분)
    url = "https://api.upbit.com/v1/candles/minutes/60"

    # 가져올려는 코인명과, 캔들수
    querystring = {"market":ticker,"count":"150"}

    headers = {"Accept": "application/json"}

    response = requests.request("GET", url, headers=headers, params=querystring)


    data = response.json()


    # 종가받기 40개
    # 0은 현재
    price_0 = data[0]["trade_price"]
    # 1은 전종가. 여기부터
    price_1_1 = data[1]["trade_price"]
    price_1_2 = data[2]["trade_price"]
    price_1_3 = data[3]["trade_price"]
    price_1_4 = data[4]["trade_price"]

    price_2_5 = data[5]["trade_price"]
    price_2_6 = data[6]["trade_price"]
    price_2_7 = data[7]["trade_price"]
    price_2_8 = data[8]["trade_price"]
    
    price_3_9 = data[9]["trade_price"]
    price_3_10 = data[10]["trade_price"]
    price_3_11 = data[11]["trade_price"]
    price_3_12 = data[12]["trade_price"]

    price_4_13 = data[13]["trade_price"]
    price_4_14 = data[14]["trade_price"]
    price_4_15 = data[15]["trade_price"]
    price_4_16 = data[16]["trade_price"]

    price_5_17 = data[17]["trade_price"]
    price_5_18 = data[18]["trade_price"]
    price_5_19 = data[19]["trade_price"]
    price_5_20 = data[20]["trade_price"]

    price_6_21 = data[21]["trade_price"]
    price_6_22 = data[22]["trade_price"]
    price_6_23 = data[23]["trade_price"]
    price_6_24 = data[24]["trade_price"]

    price_7_25 = data[25]["trade_price"]
    price_7_26 = data[26]["trade_price"]
    price_7_27 = data[27]["trade_price"]
    price_7_28 = data[28]["trade_price"]

    price_8_29 = data[29]["trade_price"]
    price_8_30 = data[30]["trade_price"]
    price_8_31 = data[31]["trade_price"]
    price_8_32 = data[32]["trade_price"]

    price_9_33 = data[33]["trade_price"]
    price_9_34 = data[34]["trade_price"]
    price_9_35 = data[35]["trade_price"]
    price_9_36 = data[36]["trade_price"]

    price_10_37 = data[37]["trade_price"]
    price_10_38 = data[38]["trade_price"]
    price_10_39 = data[39]["trade_price"]
    price_10_40 = data[40]["trade_price"]

    price_11_41 = data[41]["trade_price"]
    price_11_42 = data[42]["trade_price"]
    price_11_43 = data[43]["trade_price"]
    price_11_44 = data[44]["trade_price"]

    price_12_45 = data[45]["trade_price"]
    price_12_46 = data[46]["trade_price"]
    price_12_47 = data[47]["trade_price"]
    price_12_48 = data[48]["trade_price"]

    price_13_49 = data[49]["trade_price"]
    price_13_50 = data[50]["trade_price"]
    price_13_51 = data[51]["trade_price"]
    price_13_52 = data[52]["trade_price"]

    price_14_53 = data[53]["trade_price"]
    price_14_54 = data[54]["trade_price"]
    price_14_55 = data[55]["trade_price"]
    price_14_56 = data[56]["trade_price"]

    price_15_57 = data[57]["trade_price"]
    price_15_58 = data[58]["trade_price"]
    price_15_59 = data[59]["trade_price"]
    price_15_60 = data[60]["trade_price"]

    price_16_61 = data[61]["trade_price"]
    price_16_62 = data[62]["trade_price"]
    price_16_63 = data[63]["trade_price"]
    price_16_64 = data[64]["trade_price"]

    price_17_65 = data[65]["trade_price"]
    price_17_66 = data[66]["trade_price"]
    price_17_67 = data[67]["trade_price"]
    price_17_68 = data[68]["trade_price"]

    price_18_69 = data[69]["trade_price"]
    price_18_70 = data[70]["trade_price"]
    price_18_71 = data[71]["trade_price"]
    price_18_72 = data[72]["trade_price"]

    price_19_73 = data[73]["trade_price"]
    price_19_74 = data[74]["trade_price"]
    price_19_75 = data[75]["trade_price"]
    price_19_76 = data[76]["trade_price"]

    price_20_77 = data[77]["trade_price"]
    price_20_78 = data[78]["trade_price"]
    price_20_79 = data[79]["trade_price"]
    price_20_80 = data[80]["trade_price"]

    price_21_81 = data[81]["trade_price"]
    price_21_82 = data[82]["trade_price"]
    price_21_83 = data[83]["trade_price"]
    price_21_84 = data[84]["trade_price"]

    price_22_85 = data[85]["trade_price"]
    price_22_86 = data[86]["trade_price"]
    price_22_87 = data[87]["trade_price"]
    price_22_88 = data[88]["trade_price"]

    price_23_89 = data[89]["trade_price"]
    price_23_90 = data[90]["trade_price"]
    price_23_91 = data[91]["trade_price"]
    price_23_92 = data[92]["trade_price"]

    price_24_93 = data[93]["trade_price"]
    price_24_94 = data[94]["trade_price"]
    price_24_95 = data[95]["trade_price"]
    price_24_96 = data[96]["trade_price"]

    price_25_97 = data[97]["trade_price"]
    price_25_98 = data[98]["trade_price"]
    price_25_99 = data[99]["trade_price"]
    price_25_100 = data[100]["trade_price"]

    price_26_101 = data[101]["trade_price"]
    price_26_102 = data[102]["trade_price"]
    price_26_103 = data[103]["trade_price"]
    price_26_104 = data[104]["trade_price"]

    price_27_105 = data[105]["trade_price"]
    price_27_106 = data[106]["trade_price"]
    price_27_107 = data[107]["trade_price"]
    price_27_108 = data[108]["trade_price"]

    price_28_109 = data[109]["trade_price"]
    price_28_110 = data[110]["trade_price"]
    price_28_111 = data[111]["trade_price"]
    price_28_112 = data[112]["trade_price"]

    price_29_113 = data[113]["trade_price"]
    price_29_114 = data[114]["trade_price"]
    price_29_115 = data[115]["trade_price"]
    price_29_116 = data[116]["trade_price"]

    price_30_117 = data[117]["trade_price"]
    price_30_118 = data[118]["trade_price"]
    price_30_119 = data[119]["trade_price"]
    price_30_120 = data[120]["trade_price"]

    price_31_121 = data[121]["trade_price"]
    price_31_122 = data[122]["trade_price"]
    price_31_123 = data[123]["trade_price"]
    price_31_124 = data[124]["trade_price"]

    price_32_125 = data[125]["trade_price"]
    price_32_126 = data[126]["trade_price"]
    price_32_127 = data[127]["trade_price"]
    price_32_128 = data[128]["trade_price"]

    price_33_129 = data[129]["trade_price"]
    price_33_130 = data[130]["trade_price"]
    price_33_131 = data[131]["trade_price"]
    price_33_132 = data[132]["trade_price"]

    price_34_133 = data[133]["trade_price"]
    price_34_134 = data[134]["trade_price"]
    price_34_135 = data[135]["trade_price"]
    price_34_136 = data[136]["trade_price"]

    price_35_137 = data[137]["trade_price"]
    price_35_138 = data[138]["trade_price"]
    price_35_139 = data[139]["trade_price"]
    price_35_140 = data[140]["trade_price"]




    # 캔들 거래량 40개
    volume_0 = data[0]["candle_acc_trade_volume"]
    # 여기부터
    volume_1_1 = data[1]["candle_acc_trade_volume"]
    volume_1_2 = data[2]["candle_acc_trade_volume"]
    volume_1_3 = data[3]["candle_acc_trade_volume"]
    volume_1_4 = data[4]["candle_acc_trade_volume"]

    volume_2_5 = data[5]["candle_acc_trade_volume"]
    volume_2_6 = data[6]["candle_acc_trade_volume"]
    volume_2_7 = data[7]["candle_acc_trade_volume"]
    volume_2_8 = data[8]["candle_acc_trade_volume"]

    volume_3_9 = data[9]["candle_acc_trade_volume"]
    volume_3_10 = data[10]["candle_acc_trade_volume"]
    volume_3_11 = data[11]["candle_acc_trade_volume"]
    volume_3_12 = data[12]["candle_acc_trade_volume"]

    volume_4_13 = data[13]["candle_acc_trade_volume"]
    volume_4_14 = data[14]["candle_acc_trade_volume"]
    volume_4_15 = data[15]["candle_acc_trade_volume"]
    volume_4_16 = data[16]["candle_acc_trade_volume"]

    volume_5_17 = data[17]["candle_acc_trade_volume"]
    volume_5_18 = data[18]["candle_acc_trade_volume"]
    volume_5_19 = data[19]["candle_acc_trade_volume"]
    volume_5_20 = data[20]["candle_acc_trade_volume"]

    volume_6_21 = data[21]["candle_acc_trade_volume"]
    volume_6_22 = data[22]["candle_acc_trade_volume"]
    volume_6_23 = data[23]["candle_acc_trade_volume"]
    volume_6_24 = data[24]["candle_acc_trade_volume"]

    volume_7_25 = data[25]["candle_acc_trade_volume"]
    volume_7_26 = data[26]["candle_acc_trade_volume"]
    volume_7_27 = data[27]["candle_acc_trade_volume"]
    volume_7_28 = data[28]["candle_acc_trade_volume"]

    volume_8_29 = data[29]["candle_acc_trade_volume"]
    volume_8_30 = data[30]["candle_acc_trade_volume"]
    volume_8_31 = data[31]["candle_acc_trade_volume"]
    volume_8_32 = data[32]["candle_acc_trade_volume"]

    volume_9_33 = data[33]["candle_acc_trade_volume"]
    volume_9_34 = data[34]["candle_acc_trade_volume"]
    volume_9_35 = data[35]["candle_acc_trade_volume"]
    volume_9_36 = data[36]["candle_acc_trade_volume"]

    volume_10_37 = data[37]["candle_acc_trade_volume"]
    volume_10_38 = data[38]["candle_acc_trade_volume"]
    volume_10_39 = data[39]["candle_acc_trade_volume"]
    volume_10_40 = data[40]["candle_acc_trade_volume"]

    volume_11_41 = data[41]["candle_acc_trade_volume"]
    volume_11_42 = data[42]["candle_acc_trade_volume"]
    volume_11_43 = data[43]["candle_acc_trade_volume"]
    volume_11_44 = data[44]["candle_acc_trade_volume"]

    volume_12_45 = data[45]["candle_acc_trade_volume"]
    volume_12_46 = data[46]["candle_acc_trade_volume"]
    volume_12_47 = data[47]["candle_acc_trade_volume"]
    volume_12_48 = data[48]["candle_acc_trade_volume"]

    volume_13_49 = data[49]["candle_acc_trade_volume"]
    volume_13_50 = data[50]["candle_acc_trade_volume"]
    volume_13_51 = data[51]["candle_acc_trade_volume"]
    volume_13_52 = data[52]["candle_acc_trade_volume"]

    volume_14_53 = data[53]["candle_acc_trade_volume"]
    volume_14_54 = data[54]["candle_acc_trade_volume"]
    volume_14_55 = data[55]["candle_acc_trade_volume"]
    volume_14_56 = data[56]["candle_acc_trade_volume"]

    volume_15_57 = data[57]["candle_acc_trade_volume"]
    volume_15_58 = data[58]["candle_acc_trade_volume"]
    volume_15_59 = data[59]["candle_acc_trade_volume"]
    volume_15_60 = data[60]["candle_acc_trade_volume"]

    volume_16_61 = data[61]["candle_acc_trade_volume"]
    volume_16_62 = data[62]["candle_acc_trade_volume"]
    volume_16_63 = data[63]["candle_acc_trade_volume"]
    volume_16_64 = data[64]["candle_acc_trade_volume"]

    volume_17_65 = data[65]["candle_acc_trade_volume"]
    volume_17_66 = data[66]["candle_acc_trade_volume"]
    volume_17_67 = data[67]["candle_acc_trade_volume"]
    volume_17_68 = data[68]["candle_acc_trade_volume"]

    volume_18_69 = data[69]["candle_acc_trade_volume"]
    volume_18_70 = data[70]["candle_acc_trade_volume"]
    volume_18_71 = data[71]["candle_acc_trade_volume"]
    volume_18_72 = data[72]["candle_acc_trade_volume"]

    volume_19_73 = data[73]["candle_acc_trade_volume"]
    volume_19_74 = data[74]["candle_acc_trade_volume"]
    volume_19_75 = data[75]["candle_acc_trade_volume"]
    volume_19_76 = data[76]["candle_acc_trade_volume"]

    volume_20_77 = data[77]["candle_acc_trade_volume"]
    volume_20_78 = data[78]["candle_acc_trade_volume"]
    volume_20_79 = data[79]["candle_acc_trade_volume"]
    volume_20_80 = data[80]["candle_acc_trade_volume"]

    volume_21_81 = data[81]["candle_acc_trade_volume"]
    volume_21_82 = data[82]["candle_acc_trade_volume"]
    volume_21_83 = data[83]["candle_acc_trade_volume"]
    volume_21_84 = data[84]["candle_acc_trade_volume"]

    volume_22_85 = data[85]["candle_acc_trade_volume"]
    volume_22_86 = data[86]["candle_acc_trade_volume"]
    volume_22_87 = data[87]["candle_acc_trade_volume"]
    volume_22_88 = data[88]["candle_acc_trade_volume"]

    volume_23_89 = data[89]["candle_acc_trade_volume"]
    volume_23_90 = data[90]["candle_acc_trade_volume"]
    volume_23_91 = data[91]["candle_acc_trade_volume"]
    volume_23_92 = data[92]["candle_acc_trade_volume"]

    volume_24_93 = data[93]["candle_acc_trade_volume"]
    volume_24_94 = data[94]["candle_acc_trade_volume"]
    volume_24_95 = data[95]["candle_acc_trade_volume"]
    volume_24_96 = data[96]["candle_acc_trade_volume"]

    volume_25_97 = data[97]["candle_acc_trade_volume"]
    volume_25_98 = data[98]["candle_acc_trade_volume"]
    volume_25_99 = data[99]["candle_acc_trade_volume"]
    volume_25_100 = data[100]["candle_acc_trade_volume"]

    volume_26_101 = data[101]["candle_acc_trade_volume"]
    volume_26_102 = data[102]["candle_acc_trade_volume"]
    volume_26_103 = data[103]["candle_acc_trade_volume"]
    volume_26_104 = data[104]["candle_acc_trade_volume"]

    volume_27_105 = data[105]["candle_acc_trade_volume"]
    volume_27_106 = data[106]["candle_acc_trade_volume"]
    volume_27_107 = data[107]["candle_acc_trade_volume"]
    volume_27_108 = data[108]["candle_acc_trade_volume"]

    volume_28_109 = data[109]["candle_acc_trade_volume"]
    volume_28_110 = data[110]["candle_acc_trade_volume"]
    volume_28_111 = data[111]["candle_acc_trade_volume"]
    volume_28_112 = data[112]["candle_acc_trade_volume"]

    volume_29_113 = data[113]["candle_acc_trade_volume"]
    volume_29_114 = data[114]["candle_acc_trade_volume"]
    volume_29_115 = data[115]["candle_acc_trade_volume"]
    volume_29_116 = data[116]["candle_acc_trade_volume"]

    volume_30_117 = data[117]["candle_acc_trade_volume"]
    volume_30_118 = data[118]["candle_acc_trade_volume"]
    volume_30_119 = data[119]["candle_acc_trade_volume"]
    volume_30_120 = data[120]["candle_acc_trade_volume"]

    volume_31_121 = data[121]["candle_acc_trade_volume"]
    volume_31_122 = data[122]["candle_acc_trade_volume"]
    volume_31_123 = data[123]["candle_acc_trade_volume"]
    volume_31_124 = data[124]["candle_acc_trade_volume"]

    volume_32_125 = data[125]["candle_acc_trade_volume"]
    volume_32_126 = data[126]["candle_acc_trade_volume"]
    volume_32_127 = data[127]["candle_acc_trade_volume"]
    volume_32_128 = data[128]["candle_acc_trade_volume"]

    volume_33_129 = data[129]["candle_acc_trade_volume"]
    volume_33_130 = data[130]["candle_acc_trade_volume"]
    volume_33_131 = data[131]["candle_acc_trade_volume"]
    volume_33_132 = data[132]["candle_acc_trade_volume"]

    volume_34_133 = data[133]["candle_acc_trade_volume"]
    volume_34_134 = data[134]["candle_acc_trade_volume"]
    volume_34_135 = data[135]["candle_acc_trade_volume"]
    volume_34_136 = data[136]["candle_acc_trade_volume"]

    volume_35_137 = data[137]["candle_acc_trade_volume"]
    volume_35_138 = data[138]["candle_acc_trade_volume"]
    volume_35_139 = data[139]["candle_acc_trade_volume"]
    volume_35_140 = data[140]["candle_acc_trade_volume"]



    ###################################
    ##### 거래량 동반한 macd 산출. #####


    # 캔들 누적거래금액 40개
    acc_trade_price_0 = price_0 * volume_0
    # 여기부터
    acc_trade_price_1_1 = price_1_1 * volume_1_1
    acc_trade_price_1_2 = price_1_2 * volume_1_2
    acc_trade_price_1_3 = price_1_3 * volume_1_3
    acc_trade_price_1_4 = price_1_4 * volume_1_4

    acc_trade_price_2_5 = price_2_5 * volume_2_5
    acc_trade_price_2_6 = price_2_6 * volume_2_6
    acc_trade_price_2_7 = price_2_7 * volume_2_7
    acc_trade_price_2_8 = price_2_8 * volume_2_8

    acc_trade_price_3_9 = price_3_9 * volume_3_9
    acc_trade_price_3_10 = price_3_10 * volume_3_10
    acc_trade_price_3_11 = price_3_11 * volume_3_11
    acc_trade_price_3_12 = price_3_12 * volume_3_12

    acc_trade_price_4_13 = price_4_13 * volume_4_13
    acc_trade_price_4_14 = price_4_14 * volume_4_14
    acc_trade_price_4_15 = price_4_15 * volume_4_15
    acc_trade_price_4_16 = price_4_16 * volume_4_16

    acc_trade_price_5_17 = price_5_17 * volume_5_17
    acc_trade_price_5_18 = price_5_18 * volume_5_18
    acc_trade_price_5_19 = price_5_19 * volume_5_19
    acc_trade_price_5_20 = price_5_20 * volume_5_20

    acc_trade_price_6_21 = price_6_21 * volume_6_21
    acc_trade_price_6_22 = price_6_22 * volume_6_22
    acc_trade_price_6_23 = price_6_23 * volume_6_23
    acc_trade_price_6_24 = price_6_24 * volume_6_24

    acc_trade_price_7_25 = price_7_25 * volume_7_25
    acc_trade_price_7_26 = price_7_26 * volume_7_26
    acc_trade_price_7_27 = price_7_27 * volume_7_27
    acc_trade_price_7_28 = price_7_28 * volume_7_28

    acc_trade_price_8_29 = price_8_29 * volume_8_29
    acc_trade_price_8_30 = price_8_30 * volume_8_30
    acc_trade_price_8_31 = price_8_31 * volume_8_31
    acc_trade_price_8_32 = price_8_32 * volume_8_32

    acc_trade_price_9_33 = price_9_33 * volume_9_33
    acc_trade_price_9_34 = price_9_34 * volume_9_34
    acc_trade_price_9_35 = price_9_35 * volume_9_35
    acc_trade_price_9_36 = price_9_36 * volume_9_36

    acc_trade_price_10_37 = price_10_37 * volume_10_37
    acc_trade_price_10_38 = price_10_38 * volume_10_38
    acc_trade_price_10_39 = price_10_39 * volume_10_39
    acc_trade_price_10_40 = price_10_40 * volume_10_40

    acc_trade_price_11_41 = price_11_41 * volume_11_41
    acc_trade_price_11_42 = price_11_42 * volume_11_42
    acc_trade_price_11_43 = price_11_43 * volume_11_43
    acc_trade_price_11_44 = price_11_44 * volume_11_44

    acc_trade_price_12_45 = price_12_45 * volume_12_45
    acc_trade_price_12_46 = price_12_46 * volume_12_46
    acc_trade_price_12_47 = price_12_47 * volume_12_47
    acc_trade_price_12_48 = price_12_48 * volume_12_48

    acc_trade_price_13_49 = price_13_49 * volume_13_49
    acc_trade_price_13_50 = price_13_50 * volume_13_50
    acc_trade_price_13_51 = price_13_51 * volume_13_51
    acc_trade_price_13_52 = price_13_52 * volume_13_52

    acc_trade_price_14_53 = price_14_53 * volume_14_53
    acc_trade_price_14_54 = price_14_54 * volume_14_54
    acc_trade_price_14_55 = price_14_55 * volume_14_55
    acc_trade_price_14_56 = price_14_56 * volume_14_56

    acc_trade_price_15_57 = price_15_57 * volume_15_57
    acc_trade_price_15_58 = price_15_58 * volume_15_58
    acc_trade_price_15_59 = price_15_59 * volume_15_59
    acc_trade_price_15_60 = price_15_60 * volume_15_60

    acc_trade_price_16_61 = price_16_61 * volume_16_61
    acc_trade_price_16_62 = price_16_62 * volume_16_62
    acc_trade_price_16_63 = price_16_63 * volume_16_63
    acc_trade_price_16_64 = price_16_64 * volume_16_64

    acc_trade_price_17_65 = price_17_65 * volume_17_65
    acc_trade_price_17_66 = price_17_66 * volume_17_66
    acc_trade_price_17_67 = price_17_67 * volume_17_67
    acc_trade_price_17_68 = price_17_68 * volume_17_68

    acc_trade_price_18_69 = price_18_69 * volume_18_69
    acc_trade_price_18_70 = price_18_70 * volume_18_70
    acc_trade_price_18_71 = price_18_71 * volume_18_71
    acc_trade_price_18_72 = price_18_72 * volume_18_72

    acc_trade_price_19_73 = price_19_73 * volume_19_73
    acc_trade_price_19_74 = price_19_74 * volume_19_74
    acc_trade_price_19_75 = price_19_75 * volume_19_75
    acc_trade_price_19_76 = price_19_76 * volume_19_76

    acc_trade_price_20_77 = price_20_77 * volume_20_77
    acc_trade_price_20_78 = price_20_78 * volume_20_78
    acc_trade_price_20_79 = price_20_79 * volume_20_79
    acc_trade_price_20_80 = price_20_80 * volume_20_80

    acc_trade_price_21_81 = price_21_81 * volume_21_81
    acc_trade_price_21_82 = price_21_82 * volume_21_82
    acc_trade_price_21_83 = price_21_83 * volume_21_83
    acc_trade_price_21_84 = price_21_84 * volume_21_84

    acc_trade_price_22_85 = price_22_85 * volume_22_85
    acc_trade_price_22_86 = price_22_86 * volume_22_86
    acc_trade_price_22_87 = price_22_87 * volume_22_87
    acc_trade_price_22_88 = price_22_88 * volume_22_88

    acc_trade_price_23_89 = price_23_89 * volume_23_89
    acc_trade_price_23_90 = price_23_90 * volume_23_90
    acc_trade_price_23_91 = price_23_91 * volume_23_91
    acc_trade_price_23_92 = price_23_92 * volume_23_92

    acc_trade_price_24_93 = price_24_93 * volume_24_93
    acc_trade_price_24_94 = price_24_94 * volume_24_94
    acc_trade_price_24_95 = price_24_95 * volume_24_95
    acc_trade_price_24_96 = price_24_96 * volume_24_96

    acc_trade_price_25_97 = price_25_97 * volume_25_97
    acc_trade_price_25_98 = price_25_98 * volume_25_98
    acc_trade_price_25_99 = price_25_99 * volume_25_99
    acc_trade_price_25_100 = price_25_100 * volume_25_100

    acc_trade_price_26_101 = price_26_101 * volume_26_101
    acc_trade_price_26_102 = price_26_102 * volume_26_102
    acc_trade_price_26_103 = price_26_103 * volume_26_103
    acc_trade_price_26_104 = price_26_104 * volume_26_104

    acc_trade_price_27_105 = price_27_105 * volume_27_105
    acc_trade_price_27_106 = price_27_106 * volume_27_106
    acc_trade_price_27_107 = price_27_107 * volume_27_107
    acc_trade_price_27_108 = price_27_108 * volume_27_108

    acc_trade_price_28_109 = price_28_109 * volume_28_109
    acc_trade_price_28_110 = price_28_110 * volume_28_110
    acc_trade_price_28_111 = price_28_111 * volume_28_111
    acc_trade_price_28_112 = price_28_112 * volume_28_112

    acc_trade_price_29_113 = price_29_113 * volume_29_113
    acc_trade_price_29_114 = price_29_114 * volume_29_114
    acc_trade_price_29_115 = price_29_115 * volume_29_115
    acc_trade_price_29_116 = price_29_116 * volume_29_116

    acc_trade_price_30_117 = price_30_117 * volume_30_117
    acc_trade_price_30_118 = price_30_118 * volume_30_118
    acc_trade_price_30_119 = price_30_119 * volume_30_119
    acc_trade_price_30_120 = price_30_120 * volume_30_120

    acc_trade_price_31_121 = price_31_121 * volume_31_121
    acc_trade_price_31_122 = price_31_122 * volume_31_122
    acc_trade_price_31_123 = price_31_123 * volume_31_123
    acc_trade_price_31_124 = price_31_124 * volume_31_124

    acc_trade_price_32_125 = price_32_125 * volume_32_125
    acc_trade_price_32_126 = price_32_126 * volume_32_126
    acc_trade_price_32_127 = price_32_127 * volume_32_127
    acc_trade_price_32_128 = price_32_128 * volume_32_128

    acc_trade_price_33_129 = price_33_129 * volume_33_129
    acc_trade_price_33_130 = price_33_130 * volume_33_130
    acc_trade_price_33_131 = price_33_131 * volume_33_131
    acc_trade_price_33_132 = price_33_132 * volume_33_132

    acc_trade_price_34_133 = price_34_133 * volume_34_133
    acc_trade_price_34_134 = price_34_134 * volume_34_134
    acc_trade_price_34_135 = price_34_135 * volume_34_135
    acc_trade_price_34_136 = price_34_136 * volume_34_136

    acc_trade_price_35_137 = price_35_137 * volume_35_137
    acc_trade_price_35_138 = price_35_138 * volume_35_138
    acc_trade_price_35_139 = price_35_139 * volume_35_139
    acc_trade_price_35_140 = price_35_140 * volume_35_140


    acc_trade_price_1 = acc_trade_price_1_1 + acc_trade_price_1_2 + acc_trade_price_1_3 + acc_trade_price_1_4
    acc_trade_price_2 = acc_trade_price_2_5 + acc_trade_price_2_6 + acc_trade_price_2_7 + acc_trade_price_2_8
    acc_trade_price_3 = acc_trade_price_3_9 + acc_trade_price_3_10 + acc_trade_price_3_11 + acc_trade_price_3_12
    acc_trade_price_4 = acc_trade_price_4_13 + acc_trade_price_4_14 + acc_trade_price_4_15 + acc_trade_price_4_16
    acc_trade_price_5 = acc_trade_price_5_17 + acc_trade_price_5_18 + acc_trade_price_5_19 + acc_trade_price_5_20
    acc_trade_price_6 = acc_trade_price_6_21 + acc_trade_price_6_22 + acc_trade_price_6_23 + acc_trade_price_6_24
    acc_trade_price_7 = acc_trade_price_7_25 + acc_trade_price_7_26 + acc_trade_price_7_27 + acc_trade_price_7_28
    acc_trade_price_8 = acc_trade_price_8_29 + acc_trade_price_8_30 + acc_trade_price_8_31 + acc_trade_price_8_32
    acc_trade_price_9 = acc_trade_price_9_33 + acc_trade_price_9_34 + acc_trade_price_9_35 + acc_trade_price_9_36
    acc_trade_price_10 = acc_trade_price_10_37 + acc_trade_price_10_38 + acc_trade_price_10_39 + acc_trade_price_10_40
    acc_trade_price_11 = acc_trade_price_11_41 + acc_trade_price_11_42 + acc_trade_price_11_43 + acc_trade_price_11_44
    acc_trade_price_12 = acc_trade_price_12_45 + acc_trade_price_12_46 + acc_trade_price_12_47 + acc_trade_price_12_48
    acc_trade_price_13 = acc_trade_price_13_49 + acc_trade_price_13_50 + acc_trade_price_13_51 + acc_trade_price_13_52
    acc_trade_price_14 = acc_trade_price_14_53 + acc_trade_price_14_54 + acc_trade_price_14_55 + acc_trade_price_14_56
    acc_trade_price_15 = acc_trade_price_15_57 + acc_trade_price_15_58 + acc_trade_price_15_59 + acc_trade_price_15_60
    acc_trade_price_16 = acc_trade_price_16_61 + acc_trade_price_16_62 + acc_trade_price_16_63 + acc_trade_price_16_64
    acc_trade_price_17 = acc_trade_price_17_65 + acc_trade_price_17_66 + acc_trade_price_17_67 + acc_trade_price_17_68
    acc_trade_price_18 = acc_trade_price_18_69 + acc_trade_price_18_70 + acc_trade_price_18_71 + acc_trade_price_18_72
    acc_trade_price_19 = acc_trade_price_19_73 + acc_trade_price_19_74 + acc_trade_price_19_75 + acc_trade_price_19_76
    acc_trade_price_20 = acc_trade_price_20_77 + acc_trade_price_20_78 + acc_trade_price_20_79 + acc_trade_price_20_80
    acc_trade_price_21 = acc_trade_price_21_81 + acc_trade_price_21_82 + acc_trade_price_21_83 + acc_trade_price_21_84
    acc_trade_price_22 = acc_trade_price_22_85 + acc_trade_price_22_86 + acc_trade_price_22_87 + acc_trade_price_22_88
    acc_trade_price_23 = acc_trade_price_23_89 + acc_trade_price_23_90 + acc_trade_price_23_91 + acc_trade_price_23_92
    acc_trade_price_24 = acc_trade_price_24_93 + acc_trade_price_24_94 + acc_trade_price_24_95 + acc_trade_price_24_96
    acc_trade_price_25 = acc_trade_price_25_97 + acc_trade_price_25_98 + acc_trade_price_25_99 + acc_trade_price_25_100
    acc_trade_price_26 = acc_trade_price_26_101 + acc_trade_price_26_102 + acc_trade_price_26_103 + acc_trade_price_26_104
    acc_trade_price_27 = acc_trade_price_27_105 + acc_trade_price_27_106 + acc_trade_price_27_107 + acc_trade_price_27_108
    acc_trade_price_28 = acc_trade_price_28_109 + acc_trade_price_28_110 + acc_trade_price_28_111 + acc_trade_price_28_112
    acc_trade_price_29 = acc_trade_price_29_113 + acc_trade_price_29_114 + acc_trade_price_29_115 + acc_trade_price_29_116
    acc_trade_price_30 = acc_trade_price_30_117 + acc_trade_price_30_118 + acc_trade_price_30_119 + acc_trade_price_30_120
    acc_trade_price_31 = acc_trade_price_31_121 + acc_trade_price_31_122 + acc_trade_price_31_123 + acc_trade_price_31_124
    acc_trade_price_32 = acc_trade_price_32_125 + acc_trade_price_32_126 + acc_trade_price_32_127 + acc_trade_price_32_128
    acc_trade_price_33 = acc_trade_price_33_129 + acc_trade_price_33_130 + acc_trade_price_33_131 + acc_trade_price_33_132
    acc_trade_price_34 = acc_trade_price_34_133 + acc_trade_price_34_134 + acc_trade_price_34_135 + acc_trade_price_34_136
    acc_trade_price_35 = acc_trade_price_35_137 + acc_trade_price_35_138 + acc_trade_price_35_139 + acc_trade_price_35_140


    # 거래량 합산
    volume_1 = volume_1_1 + volume_1_2 + volume_1_3 + volume_1_4
    volume_2 = volume_2_5 + volume_2_6 + volume_2_7 + volume_2_8
    volume_3 = volume_3_9 + volume_3_10 + volume_3_11 + volume_3_12
    volume_4 = volume_4_13 + volume_4_14 + volume_4_15 + volume_4_16
    volume_5 = volume_5_17 + volume_5_18 + volume_5_19 + volume_5_20
    volume_6 = volume_6_21 + volume_6_22 + volume_6_23 + volume_6_24
    volume_7 = volume_7_25 + volume_7_26 + volume_7_27 + volume_7_28
    volume_8 = volume_8_29 + volume_8_30 + volume_8_31 + volume_8_32
    volume_9 = volume_9_33 + volume_9_34 + volume_9_35 + volume_9_36
    volume_10 = volume_10_37 + volume_10_38 + volume_10_39 + volume_10_40
    volume_11 = volume_11_41 + volume_11_42 + volume_11_43 + volume_11_44
    volume_12 = volume_12_45 + volume_12_46 + volume_12_47 + volume_12_48
    volume_13 = volume_13_49 + volume_13_50 + volume_13_51 + volume_13_52
    volume_14 = volume_14_53 + volume_14_54 + volume_14_55 + volume_14_56
    volume_15 = volume_15_57 + volume_15_58 + volume_15_59 + volume_15_60
    volume_16 = volume_16_61 + volume_16_62 + volume_16_63 + volume_16_64
    volume_17 = volume_17_65 + volume_17_66 + volume_17_67 + volume_17_68
    volume_18 = volume_18_69 + volume_18_70 + volume_18_71 + volume_18_72
    volume_19 = volume_19_73 + volume_19_74 + volume_19_75 + volume_19_76
    volume_20 = volume_20_77 + volume_20_78 + volume_20_79 + volume_20_80
    volume_21 = volume_21_81 + volume_21_82 + volume_21_83 + volume_21_84
    volume_22 = volume_22_85 + volume_22_86 + volume_22_87 + volume_22_88
    volume_23 = volume_23_89 + volume_23_90 + volume_23_91 + volume_23_92
    volume_24 = volume_24_93 + volume_24_94 + volume_24_95 + volume_24_96
    volume_25 = volume_25_97 + volume_25_98 + volume_25_99 + volume_25_100
    volume_26 = volume_26_101 + volume_26_102 + volume_26_103 + volume_26_104
    volume_27 = volume_27_105 + volume_27_106 + volume_27_107 + volume_27_108
    volume_28 = volume_28_109 + volume_28_110 + volume_28_111 + volume_28_112
    volume_29 = volume_29_113 + volume_29_114 + volume_29_115 + volume_29_116
    volume_30 = volume_30_117 + volume_30_118 + volume_30_119 + volume_30_120
    volume_31 = volume_31_121 + volume_31_122 + volume_31_123 + volume_31_124
    volume_32 = volume_32_125 + volume_32_126 + volume_32_127 + volume_32_128
    volume_33 = volume_33_129 + volume_33_130 + volume_33_131 + volume_33_132
    volume_34 = volume_34_133 + volume_34_134 + volume_34_135 + volume_34_136
    volume_35 = volume_35_137 + volume_35_138 + volume_35_139 + volume_35_140



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


    #####################################
    ##### macd 매매선택              #####

    # acc_macd_select
    if acc_ma26_1 >= 0:
        if acc_macd1 >= 0:
            # acc_ma26_1이 기준선 위에 있을때, acc_macd1이 골든
            acc_macd_select = 1
        elif acc_macd1 < 0:
            # acc_ma26_1이 기준선 위에 있을때, acc_macd1이 데드
            acc_macd_select = 2
    elif acc_ma26_1 < 0:
        if acc_macd1 >= 0:
            # acc_ma26_1이 기준선 아래에 있을때, acc_macd1이 골든
            acc_macd_select = 3
        elif acc_macd1 < 0:
            # acc_ma26_1이 기준선 아래에 있을때, acc_macd1이 데드
            acc_macd_select = 4


    return acc_macd_select













































































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
coin1 = "BTC" # 비트코인 - 크라켄 상장, 그레이스케일 상장
coinMode1 = 1 # 0 = 매매중지, 1 = 매도매수가능, 2 = 매수만가능, 3 = 매도만가능
coin2 = "ETH" # 이더리움 - 크라켄 상장, 그레이스케일 상장
coinMode2 = 1 # 0 = 매매중지, 1 = 매도매수가능, 2 = 매수만가능, 3 = 매도만가능
coin3 = "SOL" # 솔라나 - 크라켄 상장
coinMode3 = 1 # 0 = 매매중지, 1 = 매도매수가능, 2 = 매수만가능, 3 = 매도만가능
coin4 = "ADA" # 에이다 - 크라켄 상장, 그레이스케일 상장
coinMode4 = 1 # 0 = 매매중지, 1 = 매도매수가능, 2 = 매수만가능, 3 = 매도만가능
coin5 = "XRP" # 리플 - 크라켄 상장
coinMode5 = 1 # 0 = 매매중지, 1 = 매도매수가능, 2 = 매수만가능, 3 = 매도만가능

coin6 = "DOT" # 폴카닷 - 크라켄 상장
coinMode6 = 1 # 0 = 매매중지, 1 = 매도매수가능, 2 = 매수만가능, 3 = 매도만가능


coin7 = "DOGE" # 도지코인 - 크라켄 상장
coinMode7 = 1 # 0 = 매매중지, 1 = 매도매수가능, 2 = 매수만가능, 3 = 매도만가능
coin8 = "MATIC" # 폴리곤 - 크라켄 상장
coinMode8 = 1 # 0 = 매매중지, 1 = 매도매수가능, 2 = 매수만가능, 3 = 매도만가능
coin9 = "CRO" # 크립토닷컴체인
coinMode9 = 1 # 0 = 매매중지, 1 = 매도매수가능, 2 = 매수만가능, 3 = 매도만가능
coin10 = "ALGO" # 알고랜드 - 크라켄 상장
coinMode10 = 1 # 0 = 매매중지, 1 = 매도매수가능, 2 = 매수만가능, 3 = 매도만가능

coin11 = "LTC" # 라이트코인 - 크라켄 상장, 그레이스케일 상장
coinMode11 = 1 # 0 = 매매중지, 1 = 매도매수가능, 2 = 매수만가능, 3 = 매도만가능
coin12 = "LINK" # 체인링크 - 크라켄 상장, 그레이스케일 상장
coinMode12 = 1 # 0 = 매매중지, 1 = 매도매수가능, 2 = 매수만가능, 3 = 매도만가능
coin13 = "NEAR" # 니어프로토콜
coinMode13 = 1 # 0 = 매매중지, 1 = 매도매수가능, 2 = 매수만가능, 3 = 매도만가능
coin14 = "BCH" # 비트코인캐시 - 크라켄 상장, 그레이스케일 상장
coinMode14 = 1 # 0 = 매매중지, 1 = 매도매수가능, 2 = 매수만가능, 3 = 매도만가능
coin15 = "TRX" # 트론 - 크라켄 상장
coinMode15 = 1 # 0 = 매매중지, 1 = 매도매수가능, 2 = 매수만가능, 3 = 매도만가능

coin16 = "ATOM" # 코스모스 - 크라켄 상장
coinMode16 = 1 # 0 = 매매중지, 1 = 매도매수가능, 2 = 매수만가능, 3 = 매도만가능
coin17 = "XLM" # 스텔라루멘 - 크라켄 상장, 그레이스케일 상장
coinMode17 = 1 # 0 = 매매중지, 1 = 매도매수가능, 2 = 매수만가능, 3 = 매도만가능
coin18 = "MANA" # 디센트럴랜드 - 크라켄 상장, 그레이스케일 상장
coinMode18 = 1 # 0 = 매매중지, 1 = 매도매수가능, 2 = 매수만가능, 3 = 매도만가능
coin19 = "AXS" # 엑시인피니티 - 크라켄 상장
coinMode19 = 1 # 0 = 매매중지, 1 = 매도매수가능, 2 = 매수만가능, 3 = 매도만가능
coin20 = "SAND" # 샌드박스 - 크라켄 상장
coinMode20 = 1 # 0 = 매매중지, 1 = 매도매수가능, 2 = 매수만가능, 3 = 매도만가능

coin21 = "HBAR" # 헤데라
coinMode21 = 1 # 0 = 매매중지, 1 = 매도매수가능, 2 = 매수만가능, 3 = 매도만가능
coin22 = "VET" # 비체인
coinMode22 = 1 # 0 = 매매중지, 1 = 매도매수가능, 2 = 매수만가능, 3 = 매도만가능
coin23 = "THETA" # 쎄타토큰
coinMode23 = 1 # 0 = 매매중지, 1 = 매도매수가능, 2 = 매수만가능, 3 = 매도만가능
coin24 = "ETC" # 이더리움클래식 - 크라켄 상장, 그레이스케일 상장
coinMode24 = 1 # 0 = 매매중지, 1 = 매도매수가능, 2 = 매수만가능, 3 = 매도만가능
coin25 = "IOTA" # 아이오타
coinMode25 = 1 # 0 = 매매중지, 1 = 매도매수가능, 2 = 매수만가능, 3 = 매도만가능

coin26 = "XTZ" # 테조스 - 크라켄 상장
coinMode26 = 1 # 0 = 매매중지, 1 = 매도매수가능, 2 = 매수만가능, 3 = 매도만가능
coin27 = "AAVE" # 에이브 - 크라켄 상장, 그레이스케일 상장
coinMode27 = 1 # 0 = 매매중지, 1 = 매도매수가능, 2 = 매수만가능, 3 = 매도만가능
coin28 = "EOS" # 이오스 - 크라켄 상장
coinMode28 = 1 # 0 = 매매중지, 1 = 매도매수가능, 2 = 매수만가능, 3 = 매도만가능
coin29 = "STX" # 스택스
coinMode29 = 1 # 0 = 매매중지, 1 = 매도매수가능, 2 = 매수만가능, 3 = 매도만가능
coin30 = "FLOW" # 플로우 - 크라켄 상장
coinMode30 = 1 # 0 = 매매중지, 1 = 매도매수가능, 2 = 매수만가능, 3 = 매도만가능

coin31 = "BTT" # 비트토렌트
coinMode31 = 1 # 0 = 매매중지, 1 = 매도매수가능, 2 = 매수만가능, 3 = 매도만가능
coin32 = "BSV" # 비트코인에스브이
coinMode32 = 1 # 0 = 매매중지, 1 = 매도매수가능, 2 = 매수만가능, 3 = 매도만가능
coin33 = "ENJ" # 엔진코인 - 크라켄 상장
coinMode33 = 1 # 0 = 매매중지, 1 = 매도매수가능, 2 = 매수만가능, 3 = 매도만가능
coin34 = "XEC" # 이캐시
coinMode34 = 1 # 0 = 매매중지, 1 = 매도매수가능, 2 = 매수만가능, 3 = 매도만가능
coin35 = "NEO" # 네오
coinMode35 = 1 # 0 = 매매중지, 1 = 매도매수가능, 2 = 매수만가능, 3 = 매도만가능

coin36 = "BAT" # 베이직어텐션토큰 - 크라켄 상장, 그레이스케일
coinMode36 = 1 # 0 = 매매중지, 1 = 매도매수가능, 2 = 매수만가능, 3 = 매도만가능
coin37 = "CHZ" # 칠리즈 - 크라켄 상장
coinMode37 = 1 # 0 = 매매중지, 1 = 매도매수가능, 2 = 매수만가능, 3 = 매도만가능
coin38 = "WAVES" # 웨이브 - 크라켄 상장
coinMode38 = 1 # 0 = 매매중지, 1 = 매도매수가능, 2 = 매수만가능, 3 = 매도만가능
coin39 = "XEM" # 넴
coinMode39 = 1 # 0 = 매매중지, 1 = 매도매수가능, 2 = 매수만가능, 3 = 매도만가능
coin40 = "1INCH" # 1인치네트워크 - 크라켄 상장
coinMode40 = 1 # 0 = 매매중지, 1 = 매도매수가능, 2 = 매수만가능, 3 = 매도만가능

coin41 = "TFUEL" # 쎄타퓨엘
coinMode41 = 1 # 0 = 매매중지, 1 = 매도매수가능, 2 = 매수만가능, 3 = 매도만가능
coin42 = "ZIL" # 질리카
coinMode42 = 1 # 0 = 매매중지, 1 = 매도매수가능, 2 = 매수만가능, 3 = 매도만가능
coin43 = "QTUM" # 퀀텀 - 크라켄 상장
coinMode43 = 1 # 0 = 매매중지, 1 = 매도매수가능, 2 = 매수만가능, 3 = 매도만가능
coin44 = "ICX" # 아이콘 - 크라켄 상장
coinMode44 = 1 # 0 = 매매중지, 1 = 매도매수가능, 2 = 매수만가능, 3 = 매도만가능
coin45 = "WAXP" # 왁스
coinMode45 = 1 # 0 = 매매중지, 1 = 매도매수가능, 2 = 매수만가능, 3 = 매도만가능

coin46 = "OMG" # 오미세고 - 크라켄 상장
coinMode46 = 1 # 0 = 매매중지, 1 = 매도매수가능, 2 = 매수만가능, 3 = 매도만가능
coin47 = "BORA" # 보라
coinMode47 = 1 # 0 = 매매중지, 1 = 매도매수가능, 2 = 매수만가능, 3 = 매도만가능
coin48 = "ANKR" # 앵커 - 크라켄 상장
coinMode48 = 1 # 0 = 매매중지, 1 = 매도매수가능, 2 = 매수만가능, 3 = 매도만가능
coin49 = "SC" # 시아코인 - 크라켄 상장
coinMode49 = 1 # 0 = 매매중지, 1 = 매도매수가능, 2 = 매수만가능, 3 = 매도만가능
coin50 = "BTG" # 비트코인골드
coinMode50 = 1 # 0 = 매매중지, 1 = 매도매수가능, 2 = 매수만가능, 3 = 매도만가능

coin51 = "ZRX" # 제로엑스 - 크라켄 상장
coinMode51 = 1 # 0 = 매매중지, 1 = 매도매수가능, 2 = 매수만가능, 3 = 매도만가능
coin52 = "STORJ" # 스토리지 - 크라켄 상장
coinMode52 = 1 # 0 = 매매중지, 1 = 매도매수가능, 2 = 매수만가능, 3 = 매도만가능





coin53 = "KAVA" # 카바 - 크라켄 상장
coinMode53 = 1 # 0 = 매매중지, 1 = 매도매수가능, 2 = 매수만가능, 3 = 매도만가능
coin54 = "SRM" # 세럼 - 크라켄 상장
coinMode54 = 1 # 0 = 매매중지, 1 = 매도매수가능, 2 = 매수만가능, 3 = 매도만가능
coin55 = "LSK" # 리스크 - 크라켄 상장
coinMode55 = 1 # 0 = 매매중지, 1 = 매도매수가능, 2 = 매수만가능, 3 = 매도만가능

coin56 = "KNC" # 카이버네트워크 - 크라켄 상장
coinMode56 = 1 # 0 = 매매중지, 1 = 매도매수가능, 2 = 매수만가능, 3 = 매도만가능
coin57 = "REP" # 어거 - 크라켄 상장
coinMode57 = 1 # 0 = 매매중지, 1 = 매도매수가능, 2 = 매수만가능, 3 = 매도만가능
coin58 = "ORBS" # 오브스 - 오뽀가디언
coinMode58 = 1 # 0 = 매매중지, 1 = 매도매수가능, 2 = 매수만가능, 3 = 매도만가능






coin59 = "ONT" # 온톨로지
coinMode59 = 1 # 0 = 매매중지, 1 = 매도매수가능, 2 = 매수만가능, 3 = 매도만가능
coin60 = "HIVE" # 하이브
coinMode60 = 1 # 0 = 매매중지, 1 = 매도매수가능, 2 = 매수만가능, 3 = 매도만가능

coin61 = "IOST" # 아이오에스티
coinMode61 = 1 # 0 = 매매중지, 1 = 매도매수가능, 2 = 매수만가능, 3 = 매도만가능
coin62 = "NU" # 누사이퍼
coinMode62 = 1 # 0 = 매매중지, 1 = 매도매수가능, 2 = 매수만가능, 3 = 매도만가능
coin63 = "GLM" # 골렘
coinMode63 = 1 # 0 = 매매중지, 1 = 매도매수가능, 2 = 매수만가능, 3 = 매도만가능
coin64 = "POLY" # 폴리매쓰
coinMode64 = 1 # 0 = 매매중지, 1 = 매도매수가능, 2 = 매수만가능, 3 = 매도만가능
coin65 = "SXP" # 스와이프
coinMode65 = 1 # 0 = 매매중지, 1 = 매도매수가능, 2 = 매수만가능, 3 = 매도만가능

coin66 = "JST" # 저스트
coinMode66 = 1 # 0 = 매매중지, 1 = 매도매수가능, 2 = 매수만가능, 3 = 매도만가능
coin67 = "PLA" # 플레이댑
coinMode67 = 1 # 0 = 매매중지, 1 = 매도매수가능, 2 = 매수만가능, 3 = 매도만가능
coin68 = "MED" # 메디블록
coinMode68 = 1 # 0 = 매매중지, 1 = 매도매수가능, 2 = 매수만가능, 3 = 매도만가능
coin69 = "PUNDIX" # 펀디엑스
coinMode69 = 1 # 0 = 매매중지, 1 = 매도매수가능, 2 = 매수만가능, 3 = 매도만가능
coin70 = "SNT" # 스테이터스네트워크토큰
coinMode70 = 1 # 0 = 매매중지, 1 = 매도매수가능, 2 = 매수만가능, 3 = 매도만가능

coin71 = "MLK" # 밀크
coinMode71 = 1 # 0 = 매매중지, 1 = 매도매수가능, 2 = 매수만가능, 3 = 매도만가능


##### 여기까지 매매 #####


##### 여기는 매도전용 #####

coin72 = "TON" # 톤
coinMode72 = 3 # 0 = 매매중지, 1 = 매도매수가능, 2 = 매수만가능, 3 = 매도만가능
coin73 = "HUM" # 휴먼스케이프 - 김치코인
coinMode73 = 3 # 0 = 매매중지, 1 = 매도매수가능, 2 = 매수만가능, 3 = 매도만가능
coin74 = "AQT" # 알파쿼크 - 김치토큰
coinMode74 = 3 # 0 = 매매중지, 1 = 매도매수가능, 2 = 매수만가능, 3 = 매도만가능
coin75 = "CBK" # 코박토큰
coinMode75 = 3 # 0 = 매매중지, 1 = 매도매수가능, 2 = 매수만가능, 3 = 매도만가능

coin76 = "AHT" # 아하토큰
coinMode76 = 3 # 0 = 매매중지, 1 = 매도매수가능, 2 = 매수만가능, 3 = 매도만가능
coin77 = "META" # 메타디움
coinMode77 = 3 # 0 = 매매중지, 1 = 매도매수가능, 2 = 매수만가능, 3 = 매도만가능
coin78 = "DKA" # 디카르고 - 김치코인
coinMode78 = 3 # 0 = 매매중지, 1 = 매도매수가능, 2 = 매수만가능, 3 = 매도만가능







coin79 = "MVL" # 엠블 - 김치코인
coin80 = "QKC" # 쿼크체인

coin81 = "IQ" # 에브리피디아
coin82 = "DAWN" # 던프로토콜
coin83 = "POWR" # 파워렛저
coin84 = "STPT" # 에스티피
coin85 = "SSX" # 썸씽 - 김치코인

coin86 = "STRK" # 스트라이크
coin87 = "MTL" # 메탈
coin88 = "ARDR" # 아더
coin89 = "MFT" # 메인프레임
coin90 = "TT" # 썬더토큰

coin91 = "LOOM" # 룸네트워크
coin92 = "CRE" # 캐리프로토콜 - 김치코인
coin93 = "STMX" # 스톰엑스
coin94 = "UPP" # 센티넬프로토콜 - 김치코인
coin95 = "STRAX" # 스트라티스

coin96 = "HUNT" # 헌트
coin97 = "GAS" # 가스
coin98 = "AERGO" # 아르고
coin99 = "RFR" # 리퍼리움 - 김치코인
coin100 = "GRS" # 그로스톨코인

coin101 = "MOC" # 모스코인 - 김치코인
coin102 = "SBD" # 스팀달러
coin103 = "MBL" # 무비블록 - 김치코인
coin104 = "FCT2" # 피르마체인 - 김치코인
coin105 = "STEEM" # 스팀

coin106 = "ELF" # 엘프
coin107 = "ARK" # 아크
coin108 = "ONG" # 온톨로지가스
coin109 = "CVC" # 시빅


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
krw_coin103 = "KRW-" + coin103
krw_coin104 = "KRW-" + coin104
krw_coin105 = "KRW-" + coin105

krw_coin106 = "KRW-" + coin106
krw_coin107 = "KRW-" + coin107
krw_coin108 = "KRW-" + coin108
krw_coin109 = "KRW-" + coin109





# 매매금액비율 산정

#per1 = 5
per1 = 1
#per2 = 0.63
per2 = 1

bpPer1 = per1
bpPer2 = per1
bpPer3 = per1
bpPer4 = per1
bpPer5 = per1

bpPer6 = per1
bpPer7 = per2
bpPer8 = per2
bpPer9 = per2
bpPer10 = per2

bpPer11 = per2
bpPer12 = per2
bpPer13 = per2
bpPer14 = per2
bpPer15 = per2

bpPer16 = per2
bpPer17 = per2
bpPer18 = per2
bpPer19 = per2
bpPer20 = per2

bpPer21 = per2
bpPer22 = per2
bpPer23 = per2
bpPer24 = per2
bpPer25 = per2

bpPer26 = per2
bpPer27 = per2
bpPer28 = per2
bpPer29 = per2
bpPer30 = per2

bpPer31 = per2
bpPer32 = per2
bpPer33 = per2
bpPer34 = per2
bpPer35 = per2

bpPer36 = per2
bpPer37 = per2
bpPer38 = per2
bpPer39 = per2
bpPer40 = per2

bpPer41 = per2
bpPer42 = per2
bpPer43 = per2
bpPer44 = per2
bpPer45 = per2

bpPer46 = per2
bpPer47 = per2
bpPer48 = per2
bpPer49 = per2
bpPer50 = per2

bpPer51 = per2
bpPer52 = per2
bpPer53 = per2
bpPer54 = per2
bpPer55 = per2

bpPer56 = per2
bpPer57 = per2
bpPer58 = per2
bpPer59 = per2
bpPer60 = per2

bpPer61 = per2
bpPer62 = per2
bpPer63 = per2
bpPer64 = per2
bpPer65 = per2

bpPer66 = per2
bpPer67 = per2
bpPer68 = per2
bpPer69 = per2
bpPer70 = per2

bpPer71 = per2















































print("")
print("")
print("---------- ---------- ---------- ---------- ----------")
print(" -----=====     매매시작전 보유 코인 현황     =====----- ")
print("---------- ---------- ---------- ---------- ----------")
print("")
print("")


######################################################################################################################################################

#######################################
##### 자동매매 시작전 보유 코인 현황 ####
#######################################





######################################################################################################################################################
######################################################################################################################################################
######################################################################################################################################################





###############################
# 코인1

# 보유수량 불러오기
krw_balance1 = upbit.get_balance(krw_coin1)
# 코인 현재가 불러오기
price1 = pyupbit.get_current_price(krw_coin1)
# 보유코인 원화금액으로 계산하기
bp1 = price1 * krw_balance1
# 코인 보유 현황 출력.
print(f"1. 코인명 : {coin1}  |  현재가 = ￦{price1}  |  보유수량 = {krw_balance1}  |  평가금액 = ￦{bp1}")

# MACD 조회.
#macd1 = get_macd(krw_coin1)
# 거래량 동반한 MACD 조회.
macd1 = get_acc_macd(krw_coin1)
# 5, 20일 이평선 조회.
#macd1 = get_ma20(krw_coin1)
# 거래량 동반한 5, 20일 이평선 조회.
#macd1 = get_acc_ma20(krw_coin1)

# 코인 보유 유무
if macd1 == 1 or macd1 == 3:
    # 다음 코인 매매 가능유무  -  1 = 골든크로스 , 2 = 데드크로스 , 3 = 골든크로스 , 4 = 데드크로스
    op_mode1 = 1

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd1}  |  매수가능 - {op_mode1} - 골든크로스")
    print("")
elif macd1 == 2 or macd1 == 4:
    # 다음 코인 매매 가능유무  -  1 = 골든크로스 , 2 = 데드크로스 , 3 = 골든크로스 , 4 = 데드크로스
    op_mode1 = 2

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd1}  |  매수가능 - {op_mode1} - 데드크로스")
    print("")


# 1초 딜레이.
time.sleep(1)
###############################


###############################
# 코인2

# 보유수량 불러오기
krw_balance2 = upbit.get_balance(krw_coin2)
# 코인 현재가 불러오기
price2 = pyupbit.get_current_price(krw_coin2)
# 보유코인 원화금액으로 계산하기
bp2 = price2 * krw_balance2
# 코인 보유 현황 출력.
print(f"2. 코인명 : {coin2}  |  현재가 = ￦{price2}  |  보유수량 = {krw_balance2}  |  평가금액 = ￦{bp2}")

# MACD 조회.
#macd2 = get_macd(krw_coin2)
# 거래량 동반한 MACD 조회.
macd2 = get_acc_macd(krw_coin2)
# 5, 20일 이평선 조회.
#macd2 = get_ma20(krw_coin2)
# 거래량 동반한 5, 20일 이평선 조회.
#macd2 = get_acc_ma20(krw_coin2)

# 코인 보유 유무
if macd2 == 1 or macd2 == 3:
    # 다음 코인 매매 가능유무  -  1 = 골든크로스 , 2 = 데드크로스 , 3 = 골든크로스 , 4 = 데드크로스
    op_mode2 = 1

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd2}  |  매수가능 - {op_mode2} - 골든크로스")
    print("")
elif macd2 == 2 or macd2 == 4:
    # 다음 코인 매매 가능유무  -  1 = 골든크로스 , 2 = 데드크로스 , 3 = 골든크로스 , 4 = 데드크로스
    op_mode2 = 2

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd2}  |  매수가능 - {op_mode2} - 데드크로스")
    print("")

# 1초 딜레이.
time.sleep(1)
###############################


###############################
# 코인3

# 보유수량 불러오기
krw_balance3 = upbit.get_balance(krw_coin3)
# 코인 현재가 불러오기
price3 = pyupbit.get_current_price(krw_coin3)
# 보유코인 원화금액으로 계산하기
bp3 = price3 * krw_balance3
# 코인 보유 현황 출력.
print(f"3. 코인명 : {coin3}  |  현재가 = ￦{price3}  |  보유수량 = {krw_balance3}  |  평가금액 = ￦{bp3}")

# MACD 조회.
#macd3 = get_macd(krw_coin3)
# 거래량 동반한 MACD 조회.
macd3 = get_acc_macd(krw_coin3)
# 5, 20일 이평선 조회.
#macd3 = get_ma20(krw_coin3)
# 거래량 동반한 5, 20일 이평선 조회.
#macd3 = get_acc_ma20(krw_coin3)

# 코인 보유 유무
if macd3 == 1 or macd3 == 3:
    # 다음 코인 매매 가능유무  -  1 = 골든크로스 , 2 = 데드크로스 , 3 = 골든크로스 , 4 = 데드크로스
    op_mode3 = 1

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd3}  |  매수가능 - {op_mode3} - 골든크로스")
    print("")
elif macd3 == 2 or macd3 == 4:
    # 다음 코인 매매 가능유무  -  1 = 골든크로스 , 2 = 데드크로스 , 3 = 골든크로스 , 4 = 데드크로스
    op_mode3 = 2

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd3}  |  매수가능 - {op_mode3} - 데드크로스")
    print("")

# 1초 딜레이.
time.sleep(1)
###############################


###############################
# 코인4

# 보유수량 불러오기
krw_balance4 = upbit.get_balance(krw_coin4)
# 코인 현재가 불러오기
price4 = pyupbit.get_current_price(krw_coin4)
# 보유코인 원화금액으로 계산하기
bp4 = price4 * krw_balance4
# 코인 보유 현황 출력.
print(f"4. 코인명 : {coin4}  |  현재가 = ￦{price4}  |  보유수량 = {krw_balance4}  |  평가금액 = ￦{bp4}")

# MACD 조회.
#macd4 = get_macd(krw_coin4)
# 거래량 동반한 MACD 조회.
macd4 = get_acc_macd(krw_coin4)
# 5, 20일 이평선 조회.
#macd4 = get_ma20(krw_coin4)
# 거래량 동반한 5, 20일 이평선 조회.
#macd4 = get_acc_ma20(krw_coin4)

# 코인 보유 유무
if macd4 == 1 or macd4 == 3:
    # 다음 코인 매매 가능유무  -  1 = 골든크로스 , 2 = 데드크로스 , 3 = 골든크로스 , 4 = 데드크로스
    op_mode4 = 1

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd4}  |  매수가능 - {op_mode4} - 골든크로스")
    print("")
elif macd4 == 2 or macd4 == 4:
    # 다음 코인 매매 가능유무  -  1 = 골든크로스 , 2 = 데드크로스 , 3 = 골든크로스 , 4 = 데드크로스
    op_mode4 = 2

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd4}  |  매수가능 - {op_mode4} - 데드크로스")
    print("")

# 1초 딜레이.
time.sleep(1)
###############################


###############################
# 코인5

# 보유수량 불러오기
krw_balance5 = upbit.get_balance(krw_coin5)
# 코인 현재가 불러오기
price5 = pyupbit.get_current_price(krw_coin5)
# 보유코인 원화금액으로 계산하기
bp5 = price5 * krw_balance5
# 코인 보유 현황 출력.
print(f"5. 코인명 : {coin5}  |  현재가 = ￦{price5}  |  보유수량 = {krw_balance5}  |  평가금액 = ￦{bp5}")

# MACD 조회.
#macd5 = get_macd(krw_coin5)
# 거래량 동반한 MACD 조회.
macd5 = get_acc_macd(krw_coin5)
# 5, 20일 이평선 조회.
#macd5 = get_ma20(krw_coin5)
# 거래량 동반한 5, 20일 이평선 조회.
#macd5 = get_acc_ma20(krw_coin5)

# 코인 보유 유무
if macd5 == 1 or macd5 == 3:
    # 다음 코인 매매 가능유무  -  1 = 골든크로스 , 2 = 데드크로스 , 3 = 골든크로스 , 4 = 데드크로스
    op_mode5 = 1

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd5}  |  매수가능 - {op_mode5} - 골든크로스")
    print("")
elif macd5 == 2 or macd5 == 4:
    # 다음 코인 매매 가능유무  -  1 = 골든크로스 , 2 = 데드크로스 , 3 = 골든크로스 , 4 = 데드크로스
    op_mode5 = 2

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd5}  |  매수가능 - {op_mode5} - 데드크로스")
    print("")

# 1초 딜레이.
time.sleep(1)
###############################


###############################
# 코인6

# 보유수량 불러오기
krw_balance6 = upbit.get_balance(krw_coin6)
# 코인 현재가 불러오기
price6 = pyupbit.get_current_price(krw_coin6)
# 보유코인 원화금액으로 계산하기
bp6 = price6 * krw_balance6
# 코인 보유 현황 출력.
print(f"6. 코인명 : {coin6}  |  현재가 = ￦{price6}  |  보유수량 = {krw_balance6}  |  평가금액 = ￦{bp6}")

# MACD 조회.
#macd6 = get_macd(krw_coin6)
# 거래량 동반한 MACD 조회.
macd6 = get_acc_macd(krw_coin6)
# 5, 20일 이평선 조회.
#macd6 = get_ma20(krw_coin6)
# 거래량 동반한 5, 20일 이평선 조회.
#macd6 = get_acc_ma20(krw_coin6)

# 코인 보유 유무
if macd6 == 1 or macd6 == 3:
    # 다음 코인 매매 가능유무  -  1 = 골든크로스 , 2 = 데드크로스 , 3 = 골든크로스 , 4 = 데드크로스
    op_mode6 = 1

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd6}  |  매수가능 - {op_mode6} - 골든크로스")
    print("")
elif macd6 == 2 or macd6 == 4:
    # 다음 코인 매매 가능유무  -  1 = 골든크로스 , 2 = 데드크로스 , 3 = 골든크로스 , 4 = 데드크로스
    op_mode6 = 2

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd6}  |  매수가능 - {op_mode6} - 데드크로스")
    print("")

# 1초 딜레이.
time.sleep(1)
###############################


###############################
# 코인7

# 보유수량 불러오기
krw_balance7 = upbit.get_balance(krw_coin7)
# 코인 현재가 불러오기
price7 = pyupbit.get_current_price(krw_coin7)
# 보유코인 원화금액으로 계산하기
bp7 = price7 * krw_balance7
# 코인 보유 현황 출력.
print(f"7. 코인명 : {coin7}  |  현재가 = ￦{price7}  |  보유수량 = {krw_balance7}  |  평가금액 = ￦{bp7}")

# MACD 조회.
#macd7 = get_macd(krw_coin7)
# 거래량 동반한 MACD 조회.
macd7 = get_acc_macd(krw_coin7)
# 5, 20일 이평선 조회.
#macd7 = get_ma20(krw_coin7)
# 거래량 동반한 5, 20일 이평선 조회.
#macd7 = get_acc_ma20(krw_coin7)

# 코인 보유 유무
if macd7 == 1 or macd7 == 3:
    # 다음 코인 매매 가능유무  -  1 = 골든크로스 , 2 = 데드크로스 , 3 = 골든크로스 , 4 = 데드크로스
    op_mode7 = 1

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd7}  |  매수가능 - {op_mode7} - 골든크로스")
    print("")
elif macd7 == 2 or macd7 == 4:
    # 다음 코인 매매 가능유무  -  1 = 골든크로스 , 2 = 데드크로스 , 3 = 골든크로스 , 4 = 데드크로스
    op_mode7 = 2

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd7}  |  매수가능 - {op_mode7} - 데드크로스")


# 1초 딜레이.
time.sleep(1)
###############################


###############################
# 코인8

# 보유수량 불러오기
krw_balance8 = upbit.get_balance(krw_coin8)
# 코인 현재가 불러오기
price8 = pyupbit.get_current_price(krw_coin8)
# 보유코인 원화금액으로 계산하기
bp8 = price8 * krw_balance8
# 코인 보유 현황 출력.
print(f"8. 코인명 : {coin8}  |  현재가 = ￦{price8}  |  보유수량 = {krw_balance8}  |  평가금액 = ￦{bp8}")

# MACD 조회.
#macd8 = get_macd(krw_coin8)
# 거래량 동반한 MACD 조회.
macd8 = get_acc_macd(krw_coin8)
# 5, 20일 이평선 조회.
#macd8 = get_ma20(krw_coin8)
# 거래량 동반한 5, 20일 이평선 조회.
#macd8 = get_acc_ma20(krw_coin8)

# 코인 보유 유무
if macd8 == 1 or macd8 == 3:
    # 다음 코인 매매 가능유무  -  1 = 골든크로스 , 2 = 데드크로스 , 3 = 골든크로스 , 4 = 데드크로스
    op_mode8 = 1

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd8}  |  매수가능 - {op_mode8} - 골든크로스")
    print("")
elif macd8 == 2 or macd8 == 4:
    # 다음 코인 매매 가능유무  -  1 = 골든크로스 , 2 = 데드크로스 , 3 = 골든크로스 , 4 = 데드크로스
    op_mode8 = 2

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd8}  |  매수가능 - {op_mode8} - 데드크로스")

# 1초 딜레이.
time.sleep(1)
###############################


###############################
# 코인9

# 보유수량 불러오기
krw_balance9 = upbit.get_balance(krw_coin9)
# 코인 현재가 불러오기
price9 = pyupbit.get_current_price(krw_coin9)
# 보유코인 원화금액으로 계산하기
bp9 = price9 * krw_balance9
# 코인 보유 현황 출력.
print(f"9. 코인명 : {coin9}  |  현재가 = ￦{price9}  |  보유수량 = {krw_balance9}  |  평가금액 = ￦{bp9}")

# MACD 조회.
#macd9 = get_macd(krw_coin9)
# 거래량 동반한 MACD 조회.
macd9 = get_acc_macd(krw_coin9)
# 5, 20일 이평선 조회.
#macd9 = get_ma20(krw_coin9)
# 거래량 동반한 5, 20일 이평선 조회.
#macd9 = get_acc_ma20(krw_coin9)

# 코인 보유 유무
if macd9 == 1 or macd9 == 3:
    # 다음 코인 매매 가능유무  -  1 = 골든크로스 , 2 = 데드크로스 , 3 = 골든크로스 , 4 = 데드크로스
    op_mode9 = 1

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd9}  |  매수가능 - {op_mode9} - 골든크로스")
    print("")
elif macd9 == 2 or macd9 == 4:
    # 다음 코인 매매 가능유무  -  1 = 골든크로스 , 2 = 데드크로스 , 3 = 골든크로스 , 4 = 데드크로스
    op_mode9 = 2

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd9}  |  매수가능 - {op_mode9} - 데드크로스")

# 1초 딜레이.
time.sleep(1)
###############################


###############################
# 코인10

# 보유수량 불러오기
krw_balance10 = upbit.get_balance(krw_coin10)
# 코인 현재가 불러오기
price10 = pyupbit.get_current_price(krw_coin10)
# 보유코인 원화금액으로 계산하기
bp10 = price10 * krw_balance10
# 코인 보유 현황 출력.
print(f"10. 코인명 : {coin10}  |  현재가 = ￦{price10}  |  보유수량 = {krw_balance10}  |  평가금액 = ￦{bp10}")

# MACD 조회.
#macd10 = get_macd(krw_coin10)
# 거래량 동반한 MACD 조회.
macd10 = get_acc_macd(krw_coin10)
# 5, 20일 이평선 조회.
#macd10 = get_ma20(krw_coin10)
# 거래량 동반한 5, 20일 이평선 조회.
#macd10 = get_acc_ma20(krw_coin10)

# 코인 보유 유무
if macd10 == 1 or macd10 == 3:
    # 다음 코인 매매 가능유무  -  1 = 골든크로스 , 2 = 데드크로스 , 3 = 골든크로스 , 4 = 데드크로스
    op_mode10 = 1

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd10}  |  매수가능 - {op_mode10} - 골든크로스")
    print("")
elif macd10 == 2 or macd10 == 4:
    # 다음 코인 매매 가능유무  -  1 = 골든크로스 , 2 = 데드크로스 , 3 = 골든크로스 , 4 = 데드크로스
    op_mode10 = 2

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd10}  |  매수가능 - {op_mode10} - 데드크로스")
    print("")

# 1초 딜레이.
time.sleep(1)
###############################





######################################################################################################################################################
######################################################################################################################################################
######################################################################################################################################################































































































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
            print("")
            print("")
            print("********** ********** ********** ********** **********")
            print("")
            print(f"[ 현재시간 : {now} ]")
            print("")
            print("********** ********** ********** ********** **********")
            print("")
            print("")



































            ######   ######         ###            #########      ############
            ######   ######         ###            #########      ############
            ######   ######         ###            #########      ############
            ###   ###   ###      ###   ###      ###         ###   ###         ###
            ###   ###   ###      ###   ###      ###         ###   ###         ###
            ###   ###   ###      ###   ###      ###         ###   ###         ###
            ###         ###   ###         ###   ###               ###         ###
            ###         ###   ###         ###   ###               ###         ###
            ###         ###   ###         ###   ###               ###         ###
            ###         ###   ###############   ###         ###   ###         ###
            ###         ###   ###############   ###         ###   ###         ###
            ###         ###   ###############   ###         ###   ###         ###
            ###         ###   ###         ###      #########      ############
            ###         ###   ###         ###      #########      ############
            ###         ###   ###         ###      #########      ############





















            

            ######################################################################################################################################################


            ##### 코인보유현황 #####


            ###############################
            # 코인1

            # 보유수량 불러오기
            krw_balance1 = upbit.get_balance(krw_coin1)
            # 코인 현재가 불러오기
            price1 = pyupbit.get_current_price(krw_coin1)
            # 보유코인 원화금액으로 계산하기
            bp1 = price1 * krw_balance1

            # MACD 조회.
            #macd1 = get_macd(krw_coin1)
            # 거래량 동반한 MACD 조회.
            macd1 = get_acc_macd(krw_coin1)
            # 5, 20일 이평선 조회.
            #macd1 = get_ma20(krw_coin1)
            # 거래량 동반한 5, 20일 이평선 조회.
            #macd1 = get_acc_ma20(krw_coin1)

            # 1초 딜레이.
            time.sleep(1)
            ###############################


            ###############################
            # 코인2

            # 보유수량 불러오기
            krw_balance2 = upbit.get_balance(krw_coin2)
            # 코인 현재가 불러오기
            price2 = pyupbit.get_current_price(krw_coin2)
            # 보유코인 원화금액으로 계산하기
            bp2 = price2 * krw_balance2

            # MACD 조회.
            #macd2 = get_macd(krw_coin2)
            # 거래량 동반한 MACD 조회.
            macd2 = get_acc_macd(krw_coin2)
            # 5, 20일 이평선 조회.
            #macd2 = get_ma20(krw_coin2)
            # 거래량 동반한 5, 20일 이평선 조회.
            #macd2 = get_acc_ma20(krw_coin2)

            # 1초 딜레이.
            time.sleep(1)
            ###############################


            ###############################
            # 코인3

            # 보유수량 불러오기
            krw_balance3 = upbit.get_balance(krw_coin3)
            # 코인 현재가 불러오기
            price3 = pyupbit.get_current_price(krw_coin3)
            # 보유코인 원화금액으로 계산하기
            bp3 = price3 * krw_balance3

            # MACD 조회.
            #macd3 = get_macd(krw_coin3)
            # 거래량 동반한 MACD 조회.
            macd3 = get_acc_macd(krw_coin3)
            # 5, 20일 이평선 조회.
            #macd3 = get_ma20(krw_coin3)
            # 거래량 동반한 5, 20일 이평선 조회.
            #macd3 = get_acc_ma20(krw_coin3)

            # 1초 딜레이.
            time.sleep(1)
            ###############################


            ###############################
            # 코인4

            # 보유수량 불러오기
            krw_balance4 = upbit.get_balance(krw_coin4)
            # 코인 현재가 불러오기
            price4 = pyupbit.get_current_price(krw_coin4)
            # 보유코인 원화금액으로 계산하기
            bp4 = price4 * krw_balance4

            # MACD 조회.
            #macd4 = get_macd(krw_coin4)
            # 거래량 동반한 MACD 조회.
            macd4 = get_acc_macd(krw_coin4)
            # 5, 20일 이평선 조회.
            #macd4 = get_ma20(krw_coin4)
            # 거래량 동반한 5, 20일 이평선 조회.
            #macd4 = get_acc_ma20(krw_coin4)

            # 1초 딜레이.
            time.sleep(1)
            ###############################


            ###############################
            # 코인5

            # 보유수량 불러오기
            krw_balance5 = upbit.get_balance(krw_coin5)
            # 코인 현재가 불러오기
            price5 = pyupbit.get_current_price(krw_coin5)
            # 보유코인 원화금액으로 계산하기
            bp5 = price5 * krw_balance5

            # MACD 조회.
            #macd5 = get_macd(krw_coin5)
            # 거래량 동반한 MACD 조회.
            macd5 = get_acc_macd(krw_coin5)
            # 5, 20일 이평선 조회.
            #macd5 = get_ma20(krw_coin5)
            # 거래량 동반한 5, 20일 이평선 조회.
            #macd5 = get_acc_ma20(krw_coin5)

            # 1초 딜레이.
            time.sleep(1)
            ###############################


            ###############################
            # 코인6

            # 보유수량 불러오기
            krw_balance6 = upbit.get_balance(krw_coin6)
            # 코인 현재가 불러오기
            price6 = pyupbit.get_current_price(krw_coin6)
            # 보유코인 원화금액으로 계산하기
            bp6 = price6 * krw_balance6

            # MACD 조회.
            #macd6 = get_macd(krw_coin6)
            # 거래량 동반한 MACD 조회.
            macd6 = get_acc_macd(krw_coin6)
            # 5, 20일 이평선 조회.
            #macd6 = get_ma20(krw_coin6)
            # 거래량 동반한 5, 20일 이평선 조회.
            #macd6 = get_acc_ma20(krw_coin6)

            # 1초 딜레이.
            time.sleep(1)
            ###############################


            ###############################
            # 코인7

            # 보유수량 불러오기
            krw_balance7 = upbit.get_balance(krw_coin7)
            # 코인 현재가 불러오기
            price7 = pyupbit.get_current_price(krw_coin7)
            # 보유코인 원화금액으로 계산하기
            bp7 = price7 * krw_balance7

            # MACD 조회.
            #macd7 = get_macd(krw_coin7)
            # 거래량 동반한 MACD 조회.
            macd7 = get_acc_macd(krw_coin7)
            # 5, 20일 이평선 조회.
            #macd7 = get_ma20(krw_coin7)
            # 거래량 동반한 5, 20일 이평선 조회.
            #macd7 = get_acc_ma20(krw_coin7)

            # 1초 딜레이.
            time.sleep(1)
            ###############################


            ###############################
            # 코인8

            # 보유수량 불러오기
            krw_balance8 = upbit.get_balance(krw_coin8)
            # 코인 현재가 불러오기
            price8 = pyupbit.get_current_price(krw_coin8)
            # 보유코인 원화금액으로 계산하기
            bp8 = price8 * krw_balance8

            # MACD 조회.
            #macd8 = get_macd(krw_coin8)
            # 거래량 동반한 MACD 조회.
            macd8 = get_acc_macd(krw_coin8)
            # 5, 20일 이평선 조회.
            #macd8 = get_ma20(krw_coin8)
            # 거래량 동반한 5, 20일 이평선 조회.
            #macd8 = get_acc_ma20(krw_coin8)

            # 1초 딜레이.
            time.sleep(1)
            ###############################


            ###############################
            # 코인9

            # 보유수량 불러오기
            krw_balance9 = upbit.get_balance(krw_coin9)
            # 코인 현재가 불러오기
            price9 = pyupbit.get_current_price(krw_coin9)
            # 보유코인 원화금액으로 계산하기
            bp9 = price9 * krw_balance9

            # MACD 조회.
            #macd9 = get_macd(krw_coin9)
            # 거래량 동반한 MACD 조회.
            macd9 = get_acc_macd(krw_coin9)
            # 5, 20일 이평선 조회.
            #macd9 = get_ma20(krw_coin9)
            # 거래량 동반한 5, 20일 이평선 조회.
            #macd9 = get_acc_ma20(krw_coin9)

            # 1초 딜레이.
            time.sleep(1)
            ###############################


            ###############################
            # 코인10

            # 보유수량 불러오기
            krw_balance10 = upbit.get_balance(krw_coin10)
            # 코인 현재가 불러오기
            price10 = pyupbit.get_current_price(krw_coin10)
            # 보유코인 원화금액으로 계산하기
            bp10 = price10 * krw_balance10

            # MACD 조회.
            #macd10 = get_macd(krw_coin10)
            # 거래량 동반한 MACD 조회.
            macd10 = get_acc_macd(krw_coin10)
            # 5, 20일 이평선 조회.
            #macd10 = get_ma20(krw_coin10)
            # 거래량 동반한 5, 20일 이평선 조회.
            #macd10 = get_acc_ma20(krw_coin10)

            # 1초 딜레이.
            time.sleep(1)
            ###############################


            ######################################################################################################################################################



            ######################################################################################################################################################
            ######################################################################################################################################################
            ######################################################################################################################################################


















































            ##################      ######      ######      ##############################
            ##################      ######      ######      ##############################
            ##################      ######      ######      ##############################
            ######      ######      ######      ######      ######
            ######      ######      ######      ######      ######
            ######      ######      ######      ######      ######
            ######      ######      ##################      ##############################
            ######      ######      ##################      ##############################
            ######      ######      ##################      ##############################
            ######      ######      ######      ######                  ######
            ######      ######      ######      ######                  ######
            ######      ######      ######      ######                  ######
            ##################      ######      ######      ##############################
            ##################      ######      ######      ##############################
            ##################      ######      ######      ##############################





























            ######################################################################################################################################################
            ######################################################################################################################################################
            ######################################################################################################################################################





            ######################################################################################################################################################
            # 매도시작


            # 매수가능금액 불러오기
            krw = upbit.get_balance("KRW")

            # 총 코인 평가금액 평균값 구하기.
            bpAve1 = bp1 + bp2 + bp3 + bp4 + bp5 + bp6 + bp7 + bp8 + bp9 + bp10
            #bpAve1 = krw + bp1 + bp2 + bp3 + bp4 + bp5 + bp6 + bp7 + bp8 + bp9 + bp10
            #bpAve2 = bp11 + bp12 + bp13 + bp14 + bp15 + bp16 + bp17 + bp18 + bp19 + bp20
            #bpAve3 = bp21 + bp22 + bp23 + bp24 + bp25 + bp26 + bp27 + bp28 + bp29 + bp30
            #bpAve4 = bp31 + bp32 + bp33 + bp34 + bp35 + bp36 + bp37 + bp38 + bp39 + bp40
            #bpAve5 = bp41 + bp42 + bp43 + bp44 + bp45 + bp46 + bp47 + bp48 + bp49 + bp50
            #bpAve6 = bp51 + bp52 + bp53 + bp54 + bp55 + bp56 + bp57 + bp58 + bp59 + bp60
            #bpAve7 = bp61 + bp62 + bp63 + bp64 + bp65 + bp66 + bp67 + bp68 + bp69 + bp70
            #bpAve8 = bp71

            #bpAve = ( bpAve1 + bpAve2 + bpAve3 + bpAve4 + bpAve5 + bpAve6 + bpAve7 + bpAve8 ) / 72
            bpAve = ( bpAve1 ) / 12
            
            # 비트코인 macd 포인트. 1 = 기준선 위 골든크로스, 2 = 기준선 위 데드크로스, 3 = 기준선 아래 골든크로스, 4 = 기준선 아래 데드크로스
            btc_macd = macd1

            # 매도비율 기준선 위일 경우
            #sell_ave1 = 0.5
            sell_ave_1 = 1
            # 매도비율 기준선 아래일 경우
            sell_ave_2 = 1

            print("")
            print("")
            print("********** ********** ********** ********** **********")
            print("")
            print("[[[매도시작]]]")
            print(f"[ 현재시간 : {now}  ||  보유금액 = ￦{krw}  |  매도평균가 = ￦{bpAve} ]")
            print(f"[ 비트코인 macd 현황 = {btc_macd}  ||  1 = 기준선 위 골든크로스, 2 = 기준선 위 데드크로스, 3 = 기준선 아래 골든크로스, 4 = 기준선 아래 데드크로스 ]")
            print("")
            print("********** ********** ********** ********** **********")
            print("")






            ###############################
            # 코인1 - 비트코인(중심코인)

            # MACD 조건문
            if macd1 == 2 or macd1 == 4:     # macd가 데드크로스일때 매도
                if coinMode1 == 1 or coinMode1 == 3:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = 매수만가능 , 3 = >>>매도만가능<<<
                    if op_mode1 == 1:   # 다음 코인 매매 가능유무  -  1 = 골든크로스 , 2 = 데드크로스
                        print("")
                        print(f"[ 1. 매도시간 : {now}  |  코인명 : {coin1}  |  현재가 = ￦{price1}  |  MACD = ￦{macd1}  |  보유수량 = {krw_balance1}  |  평가금액 = ￦{bp1} ]")

                        if btc_macd == 2: # macd가 기준선 위에서 데드크로스일때
                            # 매도할 코인 수량 = 보유수량 * 매도비율
                            sell_krw_balance1 = krw_balance1 * sell_ave_1
                        elif btc_macd == 4: # macd가 기준선 아래에서 데드크로스일때
                            # 매도할 코인 수량 = 보유수량 * 매도비율
                            sell_krw_balance1 = krw_balance1 * sell_ave_2

                        # 매도할 코인 금액 = 현재가 * 매도할 코인 수량
                        sell_krw_price1 = price1 * sell_krw_balance1

                        if bp1 >= 20000:    # 매도할 금액이 ￦20,000 보다 높을때 매도
                            # 코인 매도
                            upbit.sell_market_order(krw_coin1, sell_krw_balance1)

                            # 다음 코인 매매 가능유무  -  1 = 골든크로스 , 2 = 데드크로스
                            op_mode1 = 2

                            print("￦20,000 이상 금액 매도")
                            print(f"매도한금액 = ￦{sell_krw_price1}  |  매도한수량 = {sell_krw_balance1}  |  매수가능여부 - {op_mode1} - 매수가능-매도불가")
                            print("")
                        else:
                            # 다음 코인 매매 가능유무  -  1 = 골든크로스 , 2 = 데드크로스
                            op_mode1 = 2

                            print("￦20,000 이하 금액 매도불가")
                            print(f"매수가능여부 - {op_mode1} - 매수가능-매도불가")
                            print("")


            # 1초 딜레이.
            time.sleep(1)

            ###############################


            ###############################
            # 코인2

            # MACD 조건문
            if macd2 == 2 or macd2 == 4:     # macd가 데드크로스일때 매도
                if coinMode2 == 1 or coinMode2 == 3:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = 매수만가능 , 3 = >>>매도만가능<<<
                    if op_mode2 == 1:   # 다음 코인 매매 가능유무  -  1 = 골든크로스 , 2 = 데드크로스
                        print("")
                        print(f"[ 2. 매도시간 : {now}  |  코인명 : {coin2}  |  현재가 = ￦{price2}  |  MACD = ￦{macd2}  |  보유수량 = {krw_balance2}  |  평가금액 = ￦{bp2} ]")

                        if btc_macd == 2: # macd가 기준선 위에서 데드크로스일때
                            # 매도할 코인 수량 = 보유수량 * 매도비율
                            sell_krw_balance2 = krw_balance2 * sell_ave_1
                        elif btc_macd == 4: # macd가 기준선 아래에서 데드크로스일때
                            # 매도할 코인 수량 = 보유수량 * 매도비율
                            sell_krw_balance2 = krw_balance2 * sell_ave_2

                        # 매도할 코인 금액 = 현재가 * 매도할 코인 수량
                        sell_krw_price2 = price2 * sell_krw_balance2

                        if bp2 >= 20000:    # 매도할 금액이 ￦20,000 보다 높을때 매도
                            # 코인 매도
                            upbit.sell_market_order(krw_coin2, sell_krw_balance2)

                            # 다음 코인 매매 가능유무  -  1 = 골든크로스 , 2 = 데드크로스
                            op_mode2 = 2

                            print("￦20,000 이상 금액 매도")
                            print(f"매도한금액 = ￦{sell_krw_price2}  |  매도한수량 = {sell_krw_balance2}  |  매수가능여부 - {op_mode2} - 매수가능-매도불가")
                            print("")
                        else:
                            # 다음 코인 매매 가능유무  -  1 = 골든크로스 , 2 = 데드크로스
                            op_mode2 = 2

                            print("￦20,000 이하 금액 매도불가")
                            print(f"매수가능여부 - {op_mode2} - 매수가능-매도불가")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################


            ###############################
            # 코인3

            # MACD 조건문
            if macd3 == 2 or macd3 == 4:     # macd가 데드크로스일때 매도
                if coinMode3 == 1 or coinMode3 == 3:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = 매수만가능 , 3 = >>>매도만가능<<<
                    if op_mode3 == 1:   # 다음 코인 매매 가능유무  -  1 = 골든크로스 , 2 = 데드크로스
                        print("")
                        print(f"[ 3. 매도시간 : {now}  |  코인명 : {coin3}  |  현재가 = ￦{price3}  |  MACD = ￦{macd3}  |  보유수량 = {krw_balance3}  |  평가금액 = ￦{bp3} ]")

                        if btc_macd == 2: # macd가 기준선 위에서 데드크로스일때
                            # 매도할 코인 수량 = 보유수량 * 매도비율
                            sell_krw_balance3 = krw_balance3 * sell_ave_1
                        elif btc_macd == 4: # macd가 기준선 아래에서 데드크로스일때
                            # 매도할 코인 수량 = 보유수량 * 매도비율
                            sell_krw_balance3 = krw_balance3 * sell_ave_2

                        # 매도할 코인 금액 = 현재가 * 매도할 코인 수량
                        sell_krw_price3 = price3 * sell_krw_balance3

                        if bp3 >= 20000:    # 매도할 금액이 ￦20,000 보다 높을때 매도
                            # 코인 매도
                            upbit.sell_market_order(krw_coin3, sell_krw_balance3)

                            # 다음 코인 매매 가능유무  -  1 = 골든크로스 , 2 = 데드크로스
                            op_mode3 = 2

                            print("￦20,000 이상 금액 매도")
                            print(f"매도한금액 = ￦{sell_krw_price3}  |  매도한수량 = {sell_krw_balance3}  |  매수가능여부 - {op_mode3} - 매수가능-매도불가")
                            print("")
                        else:
                            # 다음 코인 매매 가능유무  -  1 = 골든크로스 , 2 = 데드크로스
                            op_mode3 = 2

                            print("￦20,000 이하 금액 매도불가")
                            print(f"매수가능여부 - {op_mode3} - 매수가능-매도불가")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################


            ###############################
            # 코인4

            # MACD 조건문
            if macd4 == 2 or macd4 == 4:     # macd가 데드크로스일때 매도
                if coinMode4 == 1 or coinMode4 == 3:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = 매수만가능 , 3 = >>>매도만가능<<<
                    if op_mode4 == 1:   # 다음 코인 매매 가능유무  -  1 = 골든크로스 , 2 = 데드크로스
                        print("")
                        print(f"[ 4. 매도시간 : {now}  |  코인명 : {coin4}  |  현재가 = ￦{price4}  |  MACD = ￦{macd4}  |  보유수량 = {krw_balance4}  |  평가금액 = ￦{bp4} ]")

                        if btc_macd == 2: # macd가 기준선 위에서 데드크로스일때
                            # 매도할 코인 수량 = 보유수량 * 매도비율
                            sell_krw_balance4 = krw_balance4 * sell_ave_1
                        elif btc_macd == 4: # macd가 기준선 아래에서 데드크로스일때
                            # 매도할 코인 수량 = 보유수량 * 매도비율
                            sell_krw_balance4 = krw_balance4 * sell_ave_2

                        # 매도할 코인 금액 = 현재가 * 매도할 코인 수량
                        sell_krw_price4 = price4 * sell_krw_balance4

                        if bp4 >= 20000:    # 매도할 금액이 ￦20,000 보다 높을때 매도
                            # 코인 매도
                            upbit.sell_market_order(krw_coin4, sell_krw_balance4)

                            # 다음 코인 매매 가능유무  -  1 = 골든크로스 , 2 = 데드크로스
                            op_mode4 = 2

                            print("￦20,000 이상 금액 매도")
                            print(f"매도한금액 = ￦{sell_krw_price4}  |  매도한수량 = {sell_krw_balance4}  |  매수가능여부 - {op_mode4} - 매수가능-매도불가")
                            print("")
                        else:
                            # 다음 코인 매매 가능유무  -  1 = 골든크로스 , 2 = 데드크로스
                            op_mode4 = 2

                            print("￦20,000 이하 금액 매도불가")
                            print(f"매수가능여부 - {op_mode4} - 매수가능-매도불가")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################


            ###############################
            # 코인5

            # MACD 조건문
            if macd5 == 2 or macd5 == 4:     # macd가 데드크로스일때 매도
                if coinMode5 == 1 or coinMode5 == 3:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = 매수만가능 , 3 = >>>매도만가능<<<
                    if op_mode5 == 1:   # 다음 코인 매매 가능유무  -  1 = 골든크로스 , 2 = 데드크로스
                        print("")
                        print(f"[ 5. 매도시간 : {now}  |  코인명 : {coin5}  |  현재가 = ￦{price5}  |  MACD = ￦{macd5}  |  보유수량 = {krw_balance5}  |  평가금액 = ￦{bp5} ]")

                        if btc_macd == 2: # macd가 기준선 위에서 데드크로스일때
                            # 매도할 코인 수량 = 보유수량 * 매도비율
                            sell_krw_balance5 = krw_balance5 * sell_ave_1
                        elif btc_macd == 4: # macd가 기준선 아래에서 데드크로스일때
                            # 매도할 코인 수량 = 보유수량 * 매도비율
                            sell_krw_balance5 = krw_balance5 * sell_ave_2

                        # 매도할 코인 금액 = 현재가 * 매도할 코인 수량
                        sell_krw_price5 = price5 * sell_krw_balance5

                        if bp5 >= 20000:    # 매도할 금액이 ￦20,000 보다 높을때 매도
                            # 코인 매도
                            upbit.sell_market_order(krw_coin5, sell_krw_balance5)

                            # 다음 코인 매매 가능유무  -  1 = 골든크로스 , 2 = 데드크로스
                            op_mode5 = 2

                            print("￦20,000 이상 금액 매도")
                            print(f"매도한금액 = ￦{sell_krw_price5}  |  매도한수량 = {sell_krw_balance5}  |  매수가능여부 - {op_mode5} - 매수가능-매도불가")
                            print("")
                        else:
                            # 다음 코인 매매 가능유무  -  1 = 골든크로스 , 2 = 데드크로스
                            op_mode5 = 2

                            print("￦20,000 이하 금액 매도불가")
                            print(f"매수가능여부 - {op_mode5} - 매수가능-매도불가")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################


            ###############################
            # 코인6

            # MACD 조건문
            if macd6 == 2 or macd6 == 4:     # macd가 데드크로스일때 매도
                if coinMode6 == 1 or coinMode6 == 3:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = 매수만가능 , 3 = >>>매도만가능<<<
                    if op_mode6 == 1:   # 다음 코인 매매 가능유무  -  1 = 골든크로스 , 2 = 데드크로스
                        print("")
                        print(f"[ 6. 매도시간 : {now}  |  코인명 : {coin6}  |  현재가 = ￦{price6}  |  MACD = ￦{macd6}  |  보유수량 = {krw_balance6}  |  평가금액 = ￦{bp6} ]")

                        if btc_macd == 2: # macd가 기준선 위에서 데드크로스일때
                            # 매도할 코인 수량 = 보유수량 * 매도비율
                            sell_krw_balance6 = krw_balance6 * sell_ave_1
                        elif btc_macd == 4: # macd가 기준선 아래에서 데드크로스일때
                            # 매도할 코인 수량 = 보유수량 * 매도비율
                            sell_krw_balance6 = krw_balance6 * sell_ave_2

                        # 매도할 코인 금액 = 현재가 * 매도할 코인 수량
                        sell_krw_price6 = price6 * sell_krw_balance6

                        if bp6 >= 20000:    # 매도할 금액이 ￦20,000 보다 높을때 매도
                            # 코인 매도
                            upbit.sell_market_order(krw_coin6, sell_krw_balance6)

                            # 다음 코인 매매 가능유무  -  1 = 골든크로스 , 2 = 데드크로스
                            op_mode6 = 2

                            print("￦20,000 이상 금액 매도")
                            print(f"매도한금액 = ￦{sell_krw_price6}  |  매도한수량 = {sell_krw_balance6}  |  매수가능여부 - {op_mode6} - 매수가능-매도불가")
                            print("")
                        else:
                            # 다음 코인 매매 가능유무  -  1 = 골든크로스 , 2 = 데드크로스
                            op_mode6 = 2

                            print("￦20,000 이하 금액 매도불가")
                            print(f"매수가능여부 - {op_mode6} - 매수가능-매도불가")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################


            ###############################
            # 코인7

            # MACD 조건문
            if macd7 == 2 or macd7 == 4:     # macd가 데드크로스일때 매도
                if coinMode7 == 1 or coinMode7 == 3:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = 매수만가능 , 3 = >>>매도만가능<<<
                    if op_mode7 == 1:   # 다음 코인 매매 가능유무  -  1 = 골든크로스 , 2 = 데드크로스
                        print("")
                        print(f"[ 7. 매도시간 : {now}  |  코인명 : {coin7}  |  현재가 = ￦{price7}  |  MACD = ￦{macd7}  |  보유수량 = {krw_balance7}  |  평가금액 = ￦{bp7} ]")

                        if btc_macd == 2: # macd가 기준선 위에서 데드크로스일때
                            # 매도할 코인 수량 = 보유수량 * 매도비율
                            sell_krw_balance7 = krw_balance7 * sell_ave_1
                        elif btc_macd == 4: # macd가 기준선 아래에서 데드크로스일때
                            # 매도할 코인 수량 = 보유수량 * 매도비율
                            sell_krw_balance7 = krw_balance7 * sell_ave_2

                        # 매도할 코인 금액 = 현재가 * 매도할 코인 수량
                        sell_krw_price7 = price7 * sell_krw_balance7

                        if bp7 >= 20000:    # 매도할 금액이 ￦20,000 보다 높을때 매도
                            # 코인 매도
                            upbit.sell_market_order(krw_coin7, sell_krw_balance7)

                            # 다음 코인 매매 가능유무  -  1 = 골든크로스 , 2 = 데드크로스
                            op_mode7 = 2

                            print("￦20,000 이상 금액 매도")
                            print(f"매도한금액 = ￦{sell_krw_price7}  |  매도한수량 = {sell_krw_balance7}  |  매수가능여부 - {op_mode7} - 매수가능-매도불가")
                            print("")
                        else:
                            # 다음 코인 매매 가능유무  -  1 = 골든크로스 , 2 = 데드크로스
                            op_mode7 = 2

                            print("￦20,000 이하 금액 매도불가")
                            print(f"매수가능여부 - {op_mode7} - 매수가능-매도불가")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################


            ###############################
            # 코인8

            # MACD 조건문
            if macd8 == 2 or macd8 == 4:     # macd가 데드크로스일때 매도
                if coinMode8 == 1 or coinMode8 == 3:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = 매수만가능 , 3 = >>>매도만가능<<<
                    if op_mode8 == 1:   # 다음 코인 매매 가능유무  -  1 = 골든크로스 , 2 = 데드크로스
                        print("")
                        print(f"[ 8. 매도시간 : {now}  |  코인명 : {coin8}  |  현재가 = ￦{price8}  |  MACD = ￦{macd8}  |  보유수량 = {krw_balance8}  |  평가금액 = ￦{bp8} ]")

                        if btc_macd == 2: # macd가 기준선 위에서 데드크로스일때
                            # 매도할 코인 수량 = 보유수량 * 매도비율
                            sell_krw_balance8 = krw_balance8 * sell_ave_1
                        elif btc_macd == 4: # macd가 기준선 아래에서 데드크로스일때
                            # 매도할 코인 수량 = 보유수량 * 매도비율
                            sell_krw_balance8 = krw_balance8 * sell_ave_2

                        # 매도할 코인 금액 = 현재가 * 매도할 코인 수량
                        sell_krw_price8 = price8 * sell_krw_balance8

                        if bp8 >= 20000:    # 매도할 금액이 ￦20,000 보다 높을때 매도
                            # 코인 매도
                            upbit.sell_market_order(krw_coin8, sell_krw_balance8)

                            # 다음 코인 매매 가능유무  -  1 = 골든크로스 , 2 = 데드크로스
                            op_mode8 = 2

                            print("￦20,000 이상 금액 매도")
                            print(f"매도한금액 = ￦{sell_krw_price8}  |  매도한수량 = {sell_krw_balance8}  |  매수가능여부 - {op_mode8} - 매수가능-매도불가")
                            print("")
                        else:
                            # 다음 코인 매매 가능유무  -  1 = 골든크로스 , 2 = 데드크로스
                            op_mode8 = 2

                            print("￦20,000 이하 금액 매도불가")
                            print(f"매수가능여부 - {op_mode8} - 매수가능-매도불가")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################


            ###############################
            # 코인9

            # MACD 조건문
            if macd9 == 2 or macd9 == 4:     # macd가 데드크로스일때 매도
                if coinMode9 == 1 or coinMode9 == 3:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = 매수만가능 , 3 = >>>매도만가능<<<
                    if op_mode9 == 1:   # 다음 코인 매매 가능유무  -  1 = 골든크로스 , 2 = 데드크로스
                        print("")
                        print(f"[ 9. 매도시간 : {now}  |  코인명 : {coin9}  |  현재가 = ￦{price9}  |  MACD = ￦{macd9}  |  보유수량 = {krw_balance9}  |  평가금액 = ￦{bp9} ]")

                        if btc_macd == 2: # macd가 기준선 위에서 데드크로스일때
                            # 매도할 코인 수량 = 보유수량 * 매도비율
                            sell_krw_balance9 = krw_balance9 * sell_ave_1
                        elif btc_macd == 4: # macd가 기준선 아래에서 데드크로스일때
                            # 매도할 코인 수량 = 보유수량 * 매도비율
                            sell_krw_balance9 = krw_balance9 * sell_ave_2

                        # 매도할 코인 금액 = 현재가 * 매도할 코인 수량
                        sell_krw_price9 = price9 * sell_krw_balance9

                        if bp9 >= 20000:    # 매도할 금액이 ￦20,000 보다 높을때 매도
                            # 코인 매도
                            upbit.sell_market_order(krw_coin9, sell_krw_balance9)

                            # 다음 코인 매매 가능유무  -  1 = 골든크로스 , 2 = 데드크로스
                            op_mode9 = 2

                            print("￦20,000 이상 금액 매도")
                            print(f"매도한금액 = ￦{sell_krw_price9}  |  매도한수량 = {sell_krw_balance9}  |  매수가능여부 - {op_mode9} - 매수가능-매도불가")
                            print("")
                        else:
                            # 다음 코인 매매 가능유무  -  1 = 골든크로스 , 2 = 데드크로스
                            op_mode9 = 2

                            print("￦20,000 이하 금액 매도불가")
                            print(f"매수가능여부 - {op_mode9} - 매수가능-매도불가")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################


            ###############################
            # 코인10

            # MACD 조건문
            if macd10 == 2 or macd10 == 4:     # macd가 데드크로스일때 매도
                if coinMode10 == 1 or coinMode10 == 3:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = 매수만가능 , 3 = >>>매도만가능<<<
                    if op_mode10 == 1:   # 다음 코인 매매 가능유무  -  1 = 골든크로스 , 2 = 데드크로스
                        print("")
                        print(f"[ 10. 매도시간 : {now}  |  코인명 : {coin10}  |  현재가 = ￦{price10}  |  MACD = ￦{macd10}  |  보유수량 = {krw_balance10}  |  평가금액 = ￦{bp10} ]")

                        if btc_macd == 2: # macd가 기준선 위에서 데드크로스일때
                            # 매도할 코인 수량 = 보유수량 * 매도비율
                            sell_krw_balance10 = krw_balance10 * sell_ave_1
                        elif btc_macd == 4: # macd가 기준선 아래에서 데드크로스일때
                            # 매도할 코인 수량 = 보유수량 * 매도비율
                            sell_krw_balance10 = krw_balance10 * sell_ave_2

                        # 매도할 코인 금액 = 현재가 * 매도할 코인 수량
                        sell_krw_price10 = price10 * sell_krw_balance10

                        if bp10 >= 20000:    # 매도할 금액이 ￦20,000 보다 높을때 매도
                            # 코인 매도
                            upbit.sell_market_order(krw_coin10, sell_krw_balance10)

                            # 다음 코인 매매 가능유무  -  1 = 골든크로스 , 2 = 데드크로스
                            op_mode10 = 2

                            print("￦20,000 이상 금액 매도")
                            print(f"매도한금액 = ￦{sell_krw_price10}  |  매도한수량 = {sell_krw_balance10}  |  매수가능여부 - {op_mode10} - 매수가능-매도불가")
                            print("")
                        else:
                            # 다음 코인 매매 가능유무  -  1 = 골든크로스 , 2 = 데드크로스
                            op_mode10 = 2

                            print("￦20,000 이하 금액 매도불가")
                            print(f"매수가능여부 - {op_mode10} - 매수가능-매도불가")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################





            ######################################################################################################################################################
            ######################################################################################################################################################
            ######################################################################################################################################################





            ######################################################################################################################################################
            ######################################################################################################################################################
            ######################################################################################################################################################






































































            ##################      ######      ######            ##################
            ##################      ######      ######            ##################
            ##################      ######      ######            ##################
            ######      ######      ######      ######      ######                  ######
            ######      ######      ######      ######      ######                  ######
            ######      ######      ######      ######      ######                  ######
            ######      ######      ##################
            ######      ######      ##################
            ######      ######      ##################
            ######      ######      ######      ######      ##############################
            ######      ######      ######      ######      ##############################
            ######      ######      ######      ######      ##############################
            ##################      ######      ######                  ######
            ##################      ######      ######                  ######
            ##################      ######      ######                  ######




























            ######################################################################################################################################################
            ######################################################################################################################################################
            ######################################################################################################################################################





            ######################################################################################################################################################
            # 매수시작


            # 매수가능금액 불러오기
            krw = upbit.get_balance("KRW")

            # 총 코인 평가금액 평균값 구하기.
            bpAve1 = krw + bp1 + bp2 + bp3 + bp4 + bp5 + bp6 + bp7 + bp8 + bp9 + bp10
            #bpAve2 = bp11 + bp12 + bp13 + bp14 + bp15 + bp16 + bp17 + bp18 + bp19 + bp20
            #bpAve3 = bp21 + bp22 + bp23 + bp24 + bp25 + bp26 + bp27 + bp28 + bp29 + bp30
            #bpAve4 = bp31 + bp32 + bp33 + bp34 + bp35 + bp36 + bp37 + bp38 + bp39 + bp40
            #bpAve5 = bp41 + bp42 + bp43 + bp44 + bp45 + bp46 + bp47 + bp48 + bp49 + bp50
            #bpAve6 = bp51 + bp52 + bp53 + bp54 + bp55 + bp56 + bp57 + bp58 + bp59 + bp60
            #bpAve7 = bp61 + bp62 + bp63 + bp64 + bp65 + bp66 + bp67 + bp68 + bp69 + bp70
            #bpAve8 = bp71

            #bpAve = ( bpAve1 + bpAve2 + bpAve3 + bpAve4 + bpAve5 + bpAve6 + bpAve7 + bpAve8 ) / 72
            bpAve = ( bpAve1 ) / 11


            print("")
            print("")
            print("********** ********** ********** ********** **********")
            print("")
            print("[[[매수시작]]]")
            print(f"[ 현재시간 : {now}  ||  보유금액 = ￦{krw}  |  매수평균가 = ￦{bpAve} ]")
            print("")
            print("********** ********** ********** ********** **********")
            print("")





            ###############################
            # 코인1

            # 코인별 금액 비율조정 = 매수평균가 * 비율
            buy_bpAve1 = bpAve * bpPer1

            # MACD 조건문
            if macd1 == 1 or macd1 == 3:     # macd가 골든크로스일때 매수
                # 매수가능금액 불러오기
                krw1 = upbit.get_balance("KRW")

                if coinMode1 == 1 or coinMode1 == 2:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = >>>매수만가능<<< , 3 = 매도만가능
                    if op_mode1 == 2:   # 다음 코인 매매 가능유무  -  1 = 골든크로스 , 2 = 데드크로스
                        print("")
                        print(f"[ 1. 매수시간 : {now}  |  코인명 : {coin1}  |  현재가 = ￦{price1}  |  MACD = ￦{macd1}  |  보유수량 = {krw_balance1}  |  평가금액 = ￦{bp1}  ||  매수평균금액 = ￦{buy_bpAve1} ]")

                        if bp1 < buy_bpAve1: # 코인보유금액이 평균가보다 낮을때 매수시도
                            # 매수할 코인 금액 = 평균가 - 코인보유금액
                            buy_krw_price1 = buy_bpAve1 - bp1
                            # 매수할 코인 갯수 = 매수할 코인 금액 - 현재가
                            buy_krw_balance1 = buy_krw_price1 / price1

                            if krw1 >= buy_krw_price1: # 매수가능금액이 매수할금액보다 클때 매수시도
                                if buy_krw_price1 >= 22000:    # 매수가능금액이 최소주문가능금액인 ￦22,000원보다 높을때 매수시도
                                    # 매수할 코인명, 매수할 코인금액
                                    upbit.buy_market_order(krw_coin1, buy_krw_price1 * 0.9)

                                    # 코인 매수 가능유무  -  1 = 골든크로스 , 2 = 데드크로스
                                    op_mode1 = 1

                                    print("평균 이하 금액 매수")
                                    print(f"매수한금액 = ￦{buy_krw_price1}  |  매수한수량 = {buy_krw_balance1}  |  매수가능여부 - {op_mode1} - 매수불가-매도가능")
                                    print("")

                                else:
                                    # 코인 매수 가능유무  -  1 = 골든크로스 , 2 = 데드크로스
                                    op_mode1 = 1

                                    print("매수금액이 ￦22,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode1} - 매수불가-매도가능")
                                    print("")
                            else:   # 보유금액이 매수할 금액보다 적을때 매수시도
                                if krw1 >= 22000:    # 보유금액이 최소주문가능금액인 ￦22,000원보다 높을때 매수시도
                                    # 매수할 코인명, 매수할 코인금액
                                    upbit.buy_market_order(krw_coin1, krw1 * 0.9)

                                    op_mode1 = 1

                                    print("보유금액이 매수금액보다 적어서 보유금액만큼 매수")
                                    print(f"매수한금액 = ￦{krw1}  |  매수한수량 = {buy_krw_balance1}  |  매수가능여부 - {op_mode1} - 매수불가-매도가능")
                                    print("")
                                else:
                                    # 코인 매수 가능유무  -  1 = 골든크로스 , 2 = 데드크로스
                                    op_mode1 = 1

                                    print("보유금액이 ￦22,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode1} - 매수불가-매도가능")
                                    print("")

                        else:   # 코인보유금액이 평균가보다 높을때 매수금지
                            # 코인 매수 가능유무  -  1 = 골든크로스 , 2 = 데드크로스
                            op_mode1 = 1

                            print("보유금액이 평균금액보다 높아서 매수불가")
                            print(f"매수가능여부 - {op_mode1} - 매수불가-매도가능")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################


            ###############################
            # 코인2

            # 코인별 금액 비율조정 = 매수평균가 * 비율
            buy_bpAve2 = bpAve * bpPer2

            # MACD 조건문
            if macd2 == 1 or macd2 == 3:     # macd가 골든크로스일때 매수
                # 매수가능금액 불러오기
                krw2 = upbit.get_balance("KRW")

                if coinMode2 == 1 or coinMode2 == 2:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = >>>매수만가능<<< , 3 = 매도만가능
                    if op_mode2 == 2:   # 다음 코인 매매 가능유무  -  1 = 골든크로스 , 2 = 데드크로스
                        print("")
                        print(f"[ 2. 매수시간 : {now}  |  코인명 : {coin2}  |  현재가 = ￦{price2}  |  MACD = ￦{macd2}  |  보유수량 = {krw_balance2}  |  평가금액 = ￦{bp2}  ||  매수평균금액 = ￦{buy_bpAve2} ]")

                        if bp2 < buy_bpAve2: # 코인보유금액이 평균가보다 낮을때 매수시도
                            # 매수할 코인 금액 = 평균가 - 코인보유금액
                            buy_krw_price2 = buy_bpAve2 - bp2
                            # 매수할 코인 갯수 = 매수할 코인 금액 - 현재가
                            buy_krw_balance2 = buy_krw_price2 / price2

                            if krw2 >= buy_krw_price2: # 매수가능금액이 매수할금액보다 클때 매수시도
                                if buy_krw_price2 >= 22000:    # 매수가능금액이 최소주문가능금액인 ￦22,000원보다 높을때 매수시도
                                    # 매수할 코인명, 매수할 코인금액
                                    upbit.buy_market_order(krw_coin2, buy_krw_price2 * 0.9)

                                    # 코인 매수 가능유무  -  1 = 골든크로스 , 2 = 데드크로스
                                    op_mode2 = 1

                                    print("평균 이하 금액 매수")
                                    print(f"매수한금액 = ￦{buy_krw_price2}  |  매수한수량 = {buy_krw_balance2}  |  매수가능여부 - {op_mode2} - 매수불가-매도가능")
                                    print("")

                                else:
                                    # 코인 매수 가능유무  -  1 = 골든크로스 , 2 = 데드크로스
                                    op_mode2 = 2

                                    print("매수금액이 ￦22,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode2} - 매수불가-매도가능")
                                    print("")
                            else:   # 보유금액이 매수할 금액보다 적을때 매수시도
                                if krw2 >= 22000:    # 보유금액이 최소주문가능금액인 ￦22,000원보다 높을때 매수시도
                                    # 매수할 코인명, 매수할 코인금액
                                    upbit.buy_market_order(krw_coin2, krw2 * 0.9)

                                    op_mode2 = 1

                                    print("보유금액이 매수금액보다 적어서 보유금액만큼 매수")
                                    print(f"매수한금액 = ￦{krw2}  |  매수한수량 = {buy_krw_balance2}  |  매수가능여부 - {op_mode2} - 매수불가-매도가능")
                                    print("")
                                else:
                                    # 코인 매수 가능유무  -  1 = 골든크로스 , 2 = 데드크로스
                                    op_mode2 = 1

                                    print("보유금액이 ￦22,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode2} - 매수불가-매도가능")
                                    print("")

                        else:   # 코인보유금액이 평균가보다 높을때 매수금지
                            # 코인 매수 가능유무  -  1 = 골든크로스 , 2 = 데드크로스
                            op_mode2 = 1

                            print("보유금액이 평균금액보다 높아서 매수불가")
                            print(f"매수가능여부 - {op_mode2} - 매수불가-매도가능")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################


            ###############################
            # 코인3

            # 코인별 금액 비율조정 = 매수평균가 * 비율
            buy_bpAve3 = bpAve * bpPer3

            # MACD 조건문
            if macd3 == 1 or macd3 == 3:     # macd가 골든크로스일때 매수
                # 매수가능금액 불러오기
                krw3 = upbit.get_balance("KRW")

                if coinMode3 == 1 or coinMode3 == 2:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = >>>매수만가능<<< , 3 = 매도만가능
                    if op_mode3 == 2:   # 다음 코인 매매 가능유무  -  1 = 골든크로스 , 2 = 데드크로스
                        print("")
                        print(f"[ 3. 매수시간 : {now}  |  코인명 : {coin3}  |  현재가 = ￦{price3}  |  MACD = ￦{macd3}  |  보유수량 = {krw_balance3}  |  평가금액 = ￦{bp3}  ||  매수평균금액 = ￦{buy_bpAve3} ]")

                        if bp3 < buy_bpAve3: # 코인보유금액이 평균가보다 낮을때 매수시도
                            # 매수할 코인 금액 = 평균가 - 코인보유금액
                            buy_krw_price3 = buy_bpAve3 - bp3
                            # 매수할 코인 갯수 = 매수할 코인 금액 - 현재가
                            buy_krw_balance3 = buy_krw_price3 / price3

                            if krw3 >= buy_krw_price3: # 매수가능금액이 매수할금액보다 클때 매수시도
                                if buy_krw_price3 >= 22000:    # 매수가능금액이 최소주문가능금액인 ￦22,000원보다 높을때 매수시도
                                    # 매수할 코인명, 매수할 코인금액
                                    upbit.buy_market_order(krw_coin3, buy_krw_price3 * 0.9)

                                    # 코인 매수 가능유무  -  1 = 골든크로스 , 2 = 데드크로스
                                    op_mode3 = 1

                                    print("평균 이하 금액 매수")
                                    print(f"매수한금액 = ￦{buy_krw_price3}  |  매수한수량 = {buy_krw_balance3}  |  매수가능여부 - {op_mode3} - 매수불가-매도가능")
                                    print("")

                                else:
                                    # 코인 매수 가능유무  -  1 = 골든크로스 , 2 = 데드크로스
                                    op_mode3 = 2

                                    print("매수금액이 ￦22,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode3} - 매수불가-매도가능")
                                    print("")
                            else:   # 보유금액이 매수할 금액보다 적을때 매수시도
                                if krw3 >= 22000:    # 보유금액이 최소주문가능금액인 ￦22,000원보다 높을때 매수시도
                                    # 매수할 코인명, 매수할 코인금액
                                    upbit.buy_market_order(krw_coin3, krw3 * 0.9)

                                    op_mode3 = 1

                                    print("보유금액이 매수금액보다 적어서 보유금액만큼 매수")
                                    print(f"매수한금액 = ￦{krw3}  |  매수한수량 = {buy_krw_balance3}  |  매수가능여부 - {op_mode3} - 매수불가-매도가능")
                                    print("")
                                else:
                                    # 코인 매수 가능유무  -  1 = 골든크로스 , 2 = 데드크로스
                                    op_mode3 = 1

                                    print("보유금액이 ￦22,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode3} - 매수불가-매도가능")
                                    print("")

                        else:   # 코인보유금액이 평균가보다 높을때 매수금지
                            # 코인 매수 가능유무  -  1 = 골든크로스 , 2 = 데드크로스
                            op_mode3 = 1

                            print("보유금액이 평균금액보다 높아서 매수불가")
                            print(f"매수가능여부 - {op_mode3} - 매수불가-매도가능")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################


            ###############################
            # 코인4

            # 코인별 금액 비율조정 = 매수평균가 * 비율
            buy_bpAve4 = bpAve * bpPer4

            # MACD 조건문
            if macd4 == 1 or macd4 == 3:     # macd가 골든크로스일때 매수
                # 매수가능금액 불러오기
                krw4 = upbit.get_balance("KRW")

                if coinMode4 == 1 or coinMode4 == 2:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = >>>매수만가능<<< , 3 = 매도만가능
                    if op_mode4 == 2:   # 다음 코인 매매 가능유무  -  1 = 골든크로스 , 2 = 데드크로스
                        print("")
                        print(f"[ 4. 매수시간 : {now}  |  코인명 : {coin4}  |  현재가 = ￦{price4}  |  MACD = ￦{macd4}  |  보유수량 = {krw_balance4}  |  평가금액 = ￦{bp4}  ||  매수평균금액 = ￦{buy_bpAve4} ]")

                        if bp4 < buy_bpAve4: # 코인보유금액이 평균가보다 낮을때 매수시도
                            # 매수할 코인 금액 = 평균가 - 코인보유금액
                            buy_krw_price4 = buy_bpAve4 - bp4
                            # 매수할 코인 갯수 = 매수할 코인 금액 - 현재가
                            buy_krw_balance4 = buy_krw_price4 / price4

                            if krw4 >= buy_krw_price4: # 매수가능금액이 매수할금액보다 클때 매수시도
                                if buy_krw_price4 >= 22000:    # 매수가능금액이 최소주문가능금액인 ￦22,000원보다 높을때 매수시도
                                    # 매수할 코인명, 매수할 코인금액
                                    upbit.buy_market_order(krw_coin4, buy_krw_price4 * 0.9)

                                    # 코인 매수 가능유무  -  1 = 골든크로스 , 2 = 데드크로스
                                    op_mode4 = 1

                                    print("평균 이하 금액 매수")
                                    print(f"매수한금액 = ￦{buy_krw_price4}  |  매수한수량 = {buy_krw_balance4}  |  매수가능여부 - {op_mode4} - 매수불가-매도가능")
                                    print("")

                                else:
                                    # 코인 매수 가능유무  -  1 = 골든크로스 , 2 = 데드크로스
                                    op_mode4 = 2

                                    print("매수금액이 ￦22,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode4} - 매수불가-매도가능")
                                    print("")
                            else:   # 보유금액이 매수할 금액보다 적을때 매수시도
                                if krw4 >= 22000:    # 보유금액이 최소주문가능금액인 ￦22,000원보다 높을때 매수시도
                                    # 매수할 코인명, 매수할 코인금액
                                    upbit.buy_market_order(krw_coin4, krw4 * 0.9)

                                    op_mode4 = 1

                                    print("보유금액이 매수금액보다 적어서 보유금액만큼 매수")
                                    print(f"매수한금액 = ￦{krw4}  |  매수한수량 = {buy_krw_balance4}  |  매수가능여부 - {op_mode4} - 매수불가-매도가능")
                                    print("")
                                else:
                                    # 코인 매수 가능유무  -  1 = 골든크로스 , 2 = 데드크로스
                                    op_mode4 = 1

                                    print("보유금액이 ￦22,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode4} - 매수불가-매도가능")
                                    print("")

                        else:   # 코인보유금액이 평균가보다 높을때 매수금지
                            # 코인 매수 가능유무  -  1 = 골든크로스 , 2 = 데드크로스
                            op_mode4 = 1

                            print("보유금액이 평균금액보다 높아서 매수불가")
                            print(f"매수가능여부 - {op_mode4} - 매수불가-매도가능")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################


            ###############################
            # 코인5

            # 코인별 금액 비율조정 = 매수평균가 * 비율
            buy_bpAve5 = bpAve * bpPer5

            # MACD 조건문
            if macd5 == 1 or macd5 == 3:     # macd가 골든크로스일때 매수
                # 매수가능금액 불러오기
                krw5 = upbit.get_balance("KRW")

                if coinMode5 == 1 or coinMode5 == 2:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = >>>매수만가능<<< , 3 = 매도만가능
                    if op_mode5 == 2:   # 다음 코인 매매 가능유무  -  1 = 골든크로스 , 2 = 데드크로스
                        print("")
                        print(f"[ 5. 매수시간 : {now}  |  코인명 : {coin5}  |  현재가 = ￦{price5}  |  MACD = ￦{macd5}  |  보유수량 = {krw_balance5}  |  평가금액 = ￦{bp5}  ||  매수평균금액 = ￦{buy_bpAve5} ]")

                        if bp5 < buy_bpAve5: # 코인보유금액이 평균가보다 낮을때 매수시도
                            # 매수할 코인 금액 = 평균가 - 코인보유금액
                            buy_krw_price5 = buy_bpAve5 - bp5
                            # 매수할 코인 갯수 = 매수할 코인 금액 - 현재가
                            buy_krw_balance5 = buy_krw_price5 / price5

                            if krw5 >= buy_krw_price5: # 매수가능금액이 매수할금액보다 클때 매수시도
                                if buy_krw_price5 >= 22000:    # 매수가능금액이 최소주문가능금액인 ￦22,000원보다 높을때 매수시도
                                    # 매수할 코인명, 매수할 코인금액
                                    upbit.buy_market_order(krw_coin5, buy_krw_price5 * 0.9)

                                    # 코인 매수 가능유무  -  1 = 골든크로스 , 2 = 데드크로스
                                    op_mode5 = 1

                                    print("평균 이하 금액 매수")
                                    print(f"매수한금액 = ￦{buy_krw_price5}  |  매수한수량 = {buy_krw_balance5}  |  매수가능여부 - {op_mode5} - 매수불가-매도가능")
                                    print("")

                                else:
                                    # 코인 매수 가능유무  -  1 = 골든크로스 , 2 = 데드크로스
                                    op_mode5 = 2

                                    print("매수금액이 ￦22,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode5} - 매수불가-매도가능")
                                    print("")
                            else:   # 보유금액이 매수할 금액보다 적을때 매수시도
                                if krw5 >= 22000:    # 보유금액이 최소주문가능금액인 ￦22,000원보다 높을때 매수시도
                                    # 매수할 코인명, 매수할 코인금액
                                    upbit.buy_market_order(krw_coin5, krw5 * 0.9)

                                    op_mode5 = 1

                                    print("보유금액이 매수금액보다 적어서 보유금액만큼 매수")
                                    print(f"매수한금액 = ￦{krw5}  |  매수한수량 = {buy_krw_balance5}  |  매수가능여부 - {op_mode5} - 매수불가-매도가능")
                                    print("")
                                else:
                                    # 코인 매수 가능유무  -  1 = 골든크로스 , 2 = 데드크로스
                                    op_mode5 = 1

                                    print("보유금액이 ￦22,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode5} - 매수불가-매도가능")
                                    print("")

                        else:   # 코인보유금액이 평균가보다 높을때 매수금지
                            # 코인 매수 가능유무  -  1 = 골든크로스 , 2 = 데드크로스
                            op_mode5 = 1

                            print("보유금액이 평균금액보다 높아서 매수불가")
                            print(f"매수가능여부 - {op_mode5} - 매수불가-매도가능")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################


            ###############################
            # 코인6

            # 코인별 금액 비율조정 = 매수평균가 * 비율
            buy_bpAve6 = bpAve * bpPer6

            # MACD 조건문
            if macd6 == 1 or macd6 == 3:     # macd가 골든크로스일때 매수
                # 매수가능금액 불러오기
                krw6 = upbit.get_balance("KRW")

                if coinMode6 == 1 or coinMode6 == 2:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = >>>매수만가능<<< , 3 = 매도만가능
                    if op_mode6 == 2:   # 다음 코인 매매 가능유무  -  1 = 골든크로스 , 2 = 데드크로스
                        print("")
                        print(f"[ 6. 매수시간 : {now}  |  코인명 : {coin6}  |  현재가 = ￦{price6}  |  MACD = ￦{macd6}  |  보유수량 = {krw_balance6}  |  평가금액 = ￦{bp6}  ||  매수평균금액 = ￦{buy_bpAve6} ]")

                        if bp6 < buy_bpAve6: # 코인보유금액이 평균가보다 낮을때 매수시도
                            # 매수할 코인 금액 = 평균가 - 코인보유금액
                            buy_krw_price6 = buy_bpAve6 - bp6
                            # 매수할 코인 갯수 = 매수할 코인 금액 - 현재가
                            buy_krw_balance6 = buy_krw_price6 / price6

                            if krw6 >= buy_krw_price6: # 매수가능금액이 매수할금액보다 클때 매수시도
                                if buy_krw_price6 >= 22000:    # 매수가능금액이 최소주문가능금액인 ￦22,000원보다 높을때 매수시도
                                    # 매수할 코인명, 매수할 코인금액
                                    upbit.buy_market_order(krw_coin6, buy_krw_price6 * 0.9)

                                    # 코인 매수 가능유무  -  1 = 골든크로스 , 2 = 데드크로스
                                    op_mode6 = 1

                                    print("평균 이하 금액 매수")
                                    print(f"매수한금액 = ￦{buy_krw_price6}  |  매수한수량 = {buy_krw_balance6}  |  매수가능여부 - {op_mode6} - 매수불가-매도가능")
                                    print("")

                                else:
                                    # 코인 매수 가능유무  -  1 = 골든크로스 , 2 = 데드크로스
                                    op_mode6 = 2

                                    print("매수금액이 ￦22,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode6} - 매수불가-매도가능")
                                    print("")
                            else:   # 보유금액이 매수할 금액보다 적을때 매수시도
                                if krw6 >= 22000:    # 보유금액이 최소주문가능금액인 ￦22,000원보다 높을때 매수시도
                                    # 매수할 코인명, 매수할 코인금액
                                    upbit.buy_market_order(krw_coin6, krw6 * 0.9)

                                    op_mode6 = 1

                                    print("보유금액이 매수금액보다 적어서 보유금액만큼 매수")
                                    print(f"매수한금액 = ￦{krw6}  |  매수한수량 = {buy_krw_balance6}  |  매수가능여부 - {op_mode6} - 매수불가-매도가능")
                                    print("")
                                else:
                                    # 코인 매수 가능유무  -  1 = 골든크로스 , 2 = 데드크로스
                                    op_mode6 = 1

                                    print("보유금액이 ￦22,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode6} - 매수불가-매도가능")
                                    print("")

                        else:   # 코인보유금액이 평균가보다 높을때 매수금지
                            # 코인 매수 가능유무  -  1 = 골든크로스 , 2 = 데드크로스
                            op_mode6 = 1

                            print("보유금액이 평균금액보다 높아서 매수불가")
                            print(f"매수가능여부 - {op_mode6} - 매수불가-매도가능")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################


            ###############################
            # 코인7

            # 코인별 금액 비율조정 = 매수평균가 * 비율
            buy_bpAve7 = bpAve * bpPer7

            # MACD 조건문
            if macd7 == 1 or macd7 == 3:     # macd가 골든크로스일때 매수
                # 매수가능금액 불러오기
                krw7 = upbit.get_balance("KRW")

                if coinMode7 == 1 or coinMode7 == 2:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = >>>매수만가능<<< , 3 = 매도만가능
                    if op_mode7 == 2:   # 다음 코인 매매 가능유무  -  1 = 골든크로스 , 2 = 데드크로스
                        print("")
                        print(f"[ 7. 매수시간 : {now}  |  코인명 : {coin7}  |  현재가 = ￦{price7}  |  MACD = ￦{macd7}  |  보유수량 = {krw_balance7}  |  평가금액 = ￦{bp7}  ||  매수평균금액 = ￦{buy_bpAve7} ]")

                        if bp7 < buy_bpAve7: # 코인보유금액이 평균가보다 낮을때 매수시도
                            # 매수할 코인 금액 = 평균가 - 코인보유금액
                            buy_krw_price7 = buy_bpAve7 - bp7
                            # 매수할 코인 갯수 = 매수할 코인 금액 - 현재가
                            buy_krw_balance7 = buy_krw_price7 / price7

                            if krw7 >= buy_krw_price7: # 매수가능금액이 매수할금액보다 클때 매수시도
                                if buy_krw_price7 >= 22000:    # 매수가능금액이 최소주문가능금액인 ￦22,000원보다 높을때 매수시도
                                    # 매수할 코인명, 매수할 코인금액
                                    upbit.buy_market_order(krw_coin7, buy_krw_price7 * 0.9)

                                    # 코인 매수 가능유무  -  1 = 골든크로스 , 2 = 데드크로스
                                    op_mode7 = 1

                                    print("평균 이하 금액 매수")
                                    print(f"매수한금액 = ￦{buy_krw_price7}  |  매수한수량 = {buy_krw_balance7}  |  매수가능여부 - {op_mode7} - 매수불가-매도가능")
                                    print("")

                                else:
                                    # 코인 매수 가능유무  -  1 = 골든크로스 , 2 = 데드크로스
                                    op_mode7 = 2

                                    print("매수금액이 ￦22,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode7} - 매수불가-매도가능")
                                    print("")
                            else:   # 보유금액이 매수할 금액보다 적을때 매수시도
                                if krw7 >= 22000:    # 보유금액이 최소주문가능금액인 ￦22,000원보다 높을때 매수시도
                                    # 매수할 코인명, 매수할 코인금액
                                    upbit.buy_market_order(krw_coin7, krw7 * 0.9)

                                    op_mode7 = 1

                                    print("보유금액이 매수금액보다 적어서 보유금액만큼 매수")
                                    print(f"매수한금액 = ￦{krw7}  |  매수한수량 = {buy_krw_balance7}  |  매수가능여부 - {op_mode7} - 매수불가-매도가능")
                                    print("")
                                else:
                                    # 코인 매수 가능유무  -  1 = 골든크로스 , 2 = 데드크로스
                                    op_mode7 = 1

                                    print("보유금액이 ￦22,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode7} - 매수불가-매도가능")
                                    print("")

                        else:   # 코인보유금액이 평균가보다 높을때 매수금지
                            # 코인 매수 가능유무  -  1 = 골든크로스 , 2 = 데드크로스
                            op_mode7 = 1

                            print("보유금액이 평균금액보다 높아서 매수불가")
                            print(f"매수가능여부 - {op_mode7} - 매수불가-매도가능")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################


            ###############################
            # 코인8

            # 코인별 금액 비율조정 = 매수평균가 * 비율
            buy_bpAve8 = bpAve * bpPer8

            # MACD 조건문
            if macd8 == 1 or macd8 == 3:     # macd가 골든크로스일때 매수
                # 매수가능금액 불러오기
                krw8 = upbit.get_balance("KRW")

                if coinMode8 == 1 or coinMode8 == 2:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = >>>매수만가능<<< , 3 = 매도만가능
                    if op_mode8 == 2:   # 다음 코인 매매 가능유무  -  1 = 골든크로스 , 2 = 데드크로스
                        print("")
                        print(f"[ 8. 매수시간 : {now}  |  코인명 : {coin8}  |  현재가 = ￦{price8}  |  MACD = ￦{macd8}  |  보유수량 = {krw_balance8}  |  평가금액 = ￦{bp8}  ||  매수평균금액 = ￦{buy_bpAve8} ]")

                        if bp8 < buy_bpAve8: # 코인보유금액이 평균가보다 낮을때 매수시도
                            # 매수할 코인 금액 = 평균가 - 코인보유금액
                            buy_krw_price8 = buy_bpAve8 - bp8
                            # 매수할 코인 갯수 = 매수할 코인 금액 - 현재가
                            buy_krw_balance8 = buy_krw_price8 / price8

                            if krw8 >= buy_krw_price8: # 매수가능금액이 매수할금액보다 클때 매수시도
                                if buy_krw_price8 >= 22000:    # 매수가능금액이 최소주문가능금액인 ￦22,000원보다 높을때 매수시도
                                    # 매수할 코인명, 매수할 코인금액
                                    upbit.buy_market_order(krw_coin8, buy_krw_price8 * 0.9)

                                    # 코인 매수 가능유무  -  1 = 골든크로스 , 2 = 데드크로스
                                    op_mode8 = 1

                                    print("평균 이하 금액 매수")
                                    print(f"매수한금액 = ￦{buy_krw_price8}  |  매수한수량 = {buy_krw_balance8}  |  매수가능여부 - {op_mode8} - 매수불가-매도가능")
                                    print("")

                                else:
                                    # 코인 매수 가능유무  -  1 = 골든크로스 , 2 = 데드크로스
                                    op_mode8 = 2

                                    print("매수금액이 ￦22,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode8} - 매수불가-매도가능")
                                    print("")
                            else:   # 보유금액이 매수할 금액보다 적을때 매수시도
                                if krw8 >= 22000:    # 보유금액이 최소주문가능금액인 ￦22,000원보다 높을때 매수시도
                                    # 매수할 코인명, 매수할 코인금액
                                    upbit.buy_market_order(krw_coin8, krw8 * 0.9)

                                    op_mode8 = 1

                                    print("보유금액이 매수금액보다 적어서 보유금액만큼 매수")
                                    print(f"매수한금액 = ￦{krw8}  |  매수한수량 = {buy_krw_balance8}  |  매수가능여부 - {op_mode8} - 매수불가-매도가능")
                                    print("")
                                else:
                                    # 코인 매수 가능유무  -  1 = 골든크로스 , 2 = 데드크로스
                                    op_mode8 = 1

                                    print("보유금액이 ￦22,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode8} - 매수불가-매도가능")
                                    print("")

                        else:   # 코인보유금액이 평균가보다 높을때 매수금지
                            # 코인 매수 가능유무  -  1 = 골든크로스 , 2 = 데드크로스
                            op_mode8 = 1

                            print("보유금액이 평균금액보다 높아서 매수불가")
                            print(f"매수가능여부 - {op_mode8} - 매수불가-매도가능")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################


            ###############################
            # 코인9

            # 코인별 금액 비율조정 = 매수평균가 * 비율
            buy_bpAve9 = bpAve * bpPer9

            # MACD 조건문
            if macd9 == 1 or macd9 == 3:     # macd가 골든크로스일때 매수
                # 매수가능금액 불러오기
                krw9 = upbit.get_balance("KRW")

                if coinMode9 == 1 or coinMode9 == 2:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = >>>매수만가능<<< , 3 = 매도만가능
                    if op_mode9 == 2:   # 다음 코인 매매 가능유무  -  1 = 골든크로스 , 2 = 데드크로스
                        print("")
                        print(f"[ 9. 매수시간 : {now}  |  코인명 : {coin9}  |  현재가 = ￦{price9}  |  MACD = ￦{macd9}  |  보유수량 = {krw_balance9}  |  평가금액 = ￦{bp9}  ||  매수평균금액 = ￦{buy_bpAve9} ]")

                        if bp9 < buy_bpAve9: # 코인보유금액이 평균가보다 낮을때 매수시도
                            # 매수할 코인 금액 = 평균가 - 코인보유금액
                            buy_krw_price9 = buy_bpAve9 - bp9
                            # 매수할 코인 갯수 = 매수할 코인 금액 - 현재가
                            buy_krw_balance9 = buy_krw_price9 / price9

                            if krw9 >= buy_krw_price9: # 매수가능금액이 매수할금액보다 클때 매수시도
                                if buy_krw_price9 >= 22000:    # 매수가능금액이 최소주문가능금액인 ￦22,000원보다 높을때 매수시도
                                    # 매수할 코인명, 매수할 코인금액
                                    upbit.buy_market_order(krw_coin9, buy_krw_price9 * 0.9)

                                    # 코인 매수 가능유무  -  1 = 골든크로스 , 2 = 데드크로스
                                    op_mode9 = 1

                                    print("평균 이하 금액 매수")
                                    print(f"매수한금액 = ￦{buy_krw_price9}  |  매수한수량 = {buy_krw_balance9}  |  매수가능여부 - {op_mode9} - 매수불가-매도가능")
                                    print("")

                                else:
                                    # 코인 매수 가능유무  -  1 = 골든크로스 , 2 = 데드크로스
                                    op_mode9 = 2

                                    print("매수금액이 ￦22,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode9} - 매수불가-매도가능")
                                    print("")
                            else:   # 보유금액이 매수할 금액보다 적을때 매수시도
                                if krw9 >= 22000:    # 보유금액이 최소주문가능금액인 ￦22,000원보다 높을때 매수시도
                                    # 매수할 코인명, 매수할 코인금액
                                    upbit.buy_market_order(krw_coin9, krw9 * 0.9)

                                    op_mode9 = 1

                                    print("보유금액이 매수금액보다 적어서 보유금액만큼 매수")
                                    print(f"매수한금액 = ￦{krw9}  |  매수한수량 = {buy_krw_balance9}  |  매수가능여부 - {op_mode9} - 매수불가-매도가능")
                                    print("")
                                else:
                                    # 코인 매수 가능유무  -  1 = 골든크로스 , 2 = 데드크로스
                                    op_mode9 = 1

                                    print("보유금액이 ￦22,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode9} - 매수불가-매도가능")
                                    print("")

                        else:   # 코인보유금액이 평균가보다 높을때 매수금지
                            # 코인 매수 가능유무  -  1 = 골든크로스 , 2 = 데드크로스
                            op_mode9 = 1

                            print("보유금액이 평균금액보다 높아서 매수불가")
                            print(f"매수가능여부 - {op_mode9} - 매수불가-매도가능")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################


            ###############################
            # 코인10

            # 코인별 금액 비율조정 = 매수평균가 * 비율
            buy_bpAve10 = bpAve * bpPer10

            # MACD 조건문
            if macd10 == 1 or macd10 == 3:     # macd가 골든크로스일때 매수
                # 매수가능금액 불러오기
                krw10 = upbit.get_balance("KRW")

                if coinMode10 == 1 or coinMode10 == 2:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = >>>매수만가능<<< , 3 = 매도만가능
                    if op_mode10 == 2:   # 다음 코인 매매 가능유무  -  1 = 골든크로스 , 2 = 데드크로스
                        print("")
                        print(f"[ 10. 매수시간 : {now}  |  코인명 : {coin10}  |  현재가 = ￦{price10}  |  MACD = ￦{macd10}  |  보유수량 = {krw_balance10}  |  평가금액 = ￦{bp10}  ||  매수평균금액 = ￦{buy_bpAve10} ]")

                        if bp10 < buy_bpAve10: # 코인보유금액이 평균가보다 낮을때 매수시도
                            # 매수할 코인 금액 = 평균가 - 코인보유금액
                            buy_krw_price10 = buy_bpAve10 - bp10
                            # 매수할 코인 갯수 = 매수할 코인 금액 - 현재가
                            buy_krw_balance10 = buy_krw_price10 / price10

                            if krw10 >= buy_krw_price10: # 매수가능금액이 매수할금액보다 클때 매수시도
                                if buy_krw_price10 >= 22000:    # 매수가능금액이 최소주문가능금액인 ￦22,000원보다 높을때 매수시도
                                    # 매수할 코인명, 매수할 코인금액
                                    upbit.buy_market_order(krw_coin10, buy_krw_price10 * 0.9)

                                    # 코인 매수 가능유무  -  1 = 골든크로스 , 2 = 데드크로스
                                    op_mode10 = 1

                                    print("평균 이하 금액 매수")
                                    print(f"매수한금액 = ￦{buy_krw_price10}  |  매수한수량 = {buy_krw_balance10}  |  매수가능여부 - {op_mode10} - 매수불가-매도가능")
                                    print("")

                                else:
                                    # 코인 매수 가능유무  -  1 = 골든크로스 , 2 = 데드크로스
                                    op_mode10 = 2

                                    print("매수금액이 ￦22,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode10} - 매수불가-매도가능")
                                    print("")
                            else:   # 보유금액이 매수할 금액보다 적을때 매수시도
                                if krw10 >= 22000:    # 보유금액이 최소주문가능금액인 ￦22,000원보다 높을때 매수시도
                                    # 매수할 코인명, 매수할 코인금액
                                    upbit.buy_market_order(krw_coin10, krw10 * 0.9)

                                    op_mode10 = 1

                                    print("보유금액이 매수금액보다 적어서 보유금액만큼 매수")
                                    print(f"매수한금액 = ￦{krw10}  |  매수한수량 = {buy_krw_balance10}  |  매수가능여부 - {op_mode10} - 매수불가-매도가능")
                                    print("")
                                else:
                                    # 코인 매수 가능유무  -  1 = 골든크로스 , 2 = 데드크로스
                                    op_mode10 = 1

                                    print("보유금액이 ￦22,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode10} - 매수불가-매도가능")
                                    print("")

                        else:   # 코인보유금액이 평균가보다 높을때 매수금지
                            # 코인 매수 가능유무  -  1 = 골든크로스 , 2 = 데드크로스
                            op_mode10 = 1

                            print("보유금액이 평균금액보다 높아서 매수불가")
                            print(f"매수가능여부 - {op_mode10} - 매수불가-매도가능")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################


            





            ######################################################################################################################################################
            ######################################################################################################################################################
            ######################################################################################################################################################





            ######################################################################################################################################################
            ######################################################################################################################################################
            ######################################################################################################################################################
            ######################################################################################################################################################
            ######################################################################################################################################################





            # 60초 딜레이.
            time.sleep(60)