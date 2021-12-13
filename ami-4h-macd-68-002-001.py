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
coin8 = "CRO" # 크립토닷컴체인
coinMode8 = 1 # 0 = 매매중지, 1 = 매도매수가능, 2 = 매수만가능, 3 = 매도만가능
coin9 = "LTC" # 라이트코인 - 크라켄 상장, 그레이스케일 상장
coinMode9 = 1 # 0 = 매매중지, 1 = 매도매수가능, 2 = 매수만가능, 3 = 매도만가능
coin10 = "MATIC" # 폴리곤 - 크라켄 상장
coinMode10 = 1 # 0 = 매매중지, 1 = 매도매수가능, 2 = 매수만가능, 3 = 매도만가능

coin11 = "LINK" # 체인링크 - 크라켄 상장, 그레이스케일 상장
coinMode11 = 1 # 0 = 매매중지, 1 = 매도매수가능, 2 = 매수만가능, 3 = 매도만가능
coin12 = "BCH" # 비트코인캐시 - 크라켄 상장, 그레이스케일 상장
coinMode12 = 1 # 0 = 매매중지, 1 = 매도매수가능, 2 = 매수만가능, 3 = 매도만가능
coin13 = "ALGO" # 알고랜드 - 크라켄 상장
coinMode13 = 1 # 0 = 매매중지, 1 = 매도매수가능, 2 = 매수만가능, 3 = 매도만가능
coin14 = "MANA" # 디센트럴랜드 - 크라켄 상장, 그레이스케일 상장
coinMode14 = 1 # 0 = 매매중지, 1 = 매도매수가능, 2 = 매수만가능, 3 = 매도만가능
coin15 = "XLM" # 스텔라루멘 - 크라켄 상장, 그레이스케일 상장
coinMode15 = 1 # 0 = 매매중지, 1 = 매도매수가능, 2 = 매수만가능, 3 = 매도만가능

coin16 = "AXS" # 엑시인피니티 - 크라켄 상장
coinMode16 = 1 # 0 = 매매중지, 1 = 매도매수가능, 2 = 매수만가능, 3 = 매도만가능
coin17 = "VET" # 비체인
coinMode17 = 1 # 0 = 매매중지, 1 = 매도매수가능, 2 = 매수만가능, 3 = 매도만가능
coin18 = "TRX" # 트론 - 크라켄 상장
coinMode18 = 1 # 0 = 매매중지, 1 = 매도매수가능, 2 = 매수만가능, 3 = 매도만가능
coin19 = "THETA" # 쎄타토큰
coinMode19 = 1 # 0 = 매매중지, 1 = 매도매수가능, 2 = 매수만가능, 3 = 매도만가능
coin20 = "SAND" # 샌드박스 - 크라켄 상장
coinMode20 = 1 # 0 = 매매중지, 1 = 매도매수가능, 2 = 매수만가능, 3 = 매도만가능

coin21 = "ETC" # 이더리움클래식 - 크라켄 상장, 그레이스케일 상장
coinMode21 = 1 # 0 = 매매중지, 1 = 매도매수가능, 2 = 매수만가능, 3 = 매도만가능
coin22 = "ATOM" # 코스모스 - 크라켄 상장
coinMode22 = 1 # 0 = 매매중지, 1 = 매도매수가능, 2 = 매수만가능, 3 = 매도만가능
coin23 = "HBAR" # 헤데라
coinMode23 = 1 # 0 = 매매중지, 1 = 매도매수가능, 2 = 매수만가능, 3 = 매도만가능
coin24 = "XTZ" # 테조스 - 크라켄 상장
coinMode24 = 1 # 0 = 매매중지, 1 = 매도매수가능, 2 = 매수만가능, 3 = 매도만가능
coin25 = "IOTA" # 아이오타
coinMode25 = 1 # 0 = 매매중지, 1 = 매도매수가능, 2 = 매수만가능, 3 = 매도만가능

coin26 = "EOS" # 이오스 - 크라켄 상장
coinMode26 = 1 # 0 = 매매중지, 1 = 매도매수가능, 2 = 매수만가능, 3 = 매도만가능
coin27 = "FLOW" # 플로우 - 크라켄 상장
coinMode27 = 1 # 0 = 매매중지, 1 = 매도매수가능, 2 = 매수만가능, 3 = 매도만가능
coin28 = "ENJ" # 엔진코인 - 크라켄 상장
coinMode28 = 1 # 0 = 매매중지, 1 = 매도매수가능, 2 = 매수만가능, 3 = 매도만가능
coin29 = "AAVE" # 에이브 - 크라켄 상장, 그레이스케일 상장
coinMode29 = 1 # 0 = 매매중지, 1 = 매도매수가능, 2 = 매수만가능, 3 = 매도만가능
coin30 = "BSV" # 비트코인에스브이
coinMode30 = 1 # 0 = 매매중지, 1 = 매도매수가능, 2 = 매수만가능, 3 = 매도만가능

coin31 = "XEC" # 이캐시
coinMode31 = 1 # 0 = 매매중지, 1 = 매도매수가능, 2 = 매수만가능, 3 = 매도만가능
coin32 = "NEO" # 네오
coinMode32 = 1 # 0 = 매매중지, 1 = 매도매수가능, 2 = 매수만가능, 3 = 매도만가능
coin33 = "CHZ" # 칠리즈 - 크라켄 상장
coinMode33 = 1 # 0 = 매매중지, 1 = 매도매수가능, 2 = 매수만가능, 3 = 매도만가능
coin34 = "STX" # 스택스
coinMode34 = 1 # 0 = 매매중지, 1 = 매도매수가능, 2 = 매수만가능, 3 = 매도만가능
coin35 = "BAT" # 베이직어텐션토큰 - 크라켄 상장, 그레이스케일
coinMode35 = 1 # 0 = 매매중지, 1 = 매도매수가능, 2 = 매수만가능, 3 = 매도만가능

coin36 = "WAVES" # 웨이브 - 크라켄 상장
coinMode36 = 1 # 0 = 매매중지, 1 = 매도매수가능, 2 = 매수만가능, 3 = 매도만가능
coin37 = "BTT" # 비트토렌트
coinMode37 = 1 # 0 = 매매중지, 1 = 매도매수가능, 2 = 매수만가능, 3 = 매도만가능
coin38 = "TFUEL" # 쎄타퓨엘
coinMode38 = 1 # 0 = 매매중지, 1 = 매도매수가능, 2 = 매수만가능, 3 = 매도만가능
coin39 = "XEM" # 넴
coinMode39 = 1 # 0 = 매매중지, 1 = 매도매수가능, 2 = 매수만가능, 3 = 매도만가능
coin40 = "QTUM" # 퀀텀 - 크라켄 상장
coinMode40 = 1 # 0 = 매매중지, 1 = 매도매수가능, 2 = 매수만가능, 3 = 매도만가능

coin41 = "WAXP" # 왁스
coinMode41 = 1 # 0 = 매매중지, 1 = 매도매수가능, 2 = 매수만가능, 3 = 매도만가능
coin42 = "SC" # 시아코인 - 크라켄 상장
coinMode42 = 1 # 0 = 매매중지, 1 = 매도매수가능, 2 = 매수만가능, 3 = 매도만가능
coin43 = "ICX" # 아이콘 - 크라켄 상장
coinMode43 = 1 # 0 = 매매중지, 1 = 매도매수가능, 2 = 매수만가능, 3 = 매도만가능
coin44 = "ANKR" # 앵커 - 크라켄 상장
coinMode44 = 1 # 0 = 매매중지, 1 = 매도매수가능, 2 = 매수만가능, 3 = 매도만가능
coin45 = "OMG" # 오미세고 - 크라켄 상장
coinMode45 = 1 # 0 = 매매중지, 1 = 매도매수가능, 2 = 매수만가능, 3 = 매도만가능

coin46 = "BORA" # 보라
coinMode46 = 1 # 0 = 매매중지, 1 = 매도매수가능, 2 = 매수만가능, 3 = 매도만가능
coin47 = "ZIL" # 질리카
coinMode47 = 1 # 0 = 매매중지, 1 = 매도매수가능, 2 = 매수만가능, 3 = 매도만가능
coin48 = "STORJ" # 스토리지 - 크라켄 상장
coinMode48 = 1 # 0 = 매매중지, 1 = 매도매수가능, 2 = 매수만가능, 3 = 매도만가능
coin49 = "BTG" # 비트코인골드
coinMode49 = 1 # 0 = 매매중지, 1 = 매도매수가능, 2 = 매수만가능, 3 = 매도만가능
coin50 = "ZRX" # 제로엑스
coinMode50 = 1 # 0 = 매매중지, 1 = 매도매수가능, 2 = 매수만가능, 3 = 매도만가능

coin51 = "HIVE" # 하이브
coinMode51 = 1 # 0 = 매매중지, 1 = 매도매수가능, 2 = 매수만가능, 3 = 매도만가능
coin52 = "KAVA" # 카바 - 크라켄 상장
coinMode52 = 1 # 0 = 매매중지, 1 = 매도매수가능, 2 = 매수만가능, 3 = 매도만가능
coin53 = "SRM" # 세럼 - 크라켄 상장
coinMode53 = 1 # 0 = 매매중지, 1 = 매도매수가능, 2 = 매수만가능, 3 = 매도만가능
coin54 = "1INCH" # 1인치네트워크 - 크라켄 상장
coinMode54 = 1 # 0 = 매매중지, 1 = 매도매수가능, 2 = 매수만가능, 3 = 매도만가능
coin55 = "PLA" # 플레이댑
coinMode55 = 1 # 0 = 매매중지, 1 = 매도매수가능, 2 = 매수만가능, 3 = 매도만가능

coin56 = "NU" # 누사이퍼
coinMode56 = 1 # 0 = 매매중지, 1 = 매도매수가능, 2 = 매수만가능, 3 = 매도만가능
coin57 = "LSK" # 리스크 - 크라켄 상장
coinMode57 = 1 # 0 = 매매중지, 1 = 매도매수가능, 2 = 매수만가능, 3 = 매도만가능
coin58 = "SNT" # 스테이터스네트워크토큰
coinMode58 = 1 # 0 = 매매중지, 1 = 매도매수가능, 2 = 매수만가능, 3 = 매도만가능
coin59 = "KNC" # 카이버네트워크 - 크라켄 상장
coinMode59 = 1 # 0 = 매매중지, 1 = 매도매수가능, 2 = 매수만가능, 3 = 매도만가능
coin60 = "HUM" # 휴먼스케이프 - 김치코인
coinMode60 = 1 # 0 = 매매중지, 1 = 매도매수가능, 2 = 매수만가능, 3 = 매도만가능

coin61 = "ORBS" # 오브스 - 오뽀가디언
coinMode61 = 1 # 0 = 매매중지, 1 = 매도매수가능, 2 = 매수만가능, 3 = 매도만가능
coin62 = "DKA" # 디카르고 - 김치코인
coinMode62 = 1 # 0 = 매매중지, 1 = 매도매수가능, 2 = 매수만가능, 3 = 매도만가능
coin63 = "MLK" # 밀크
coinMode63 = 1 # 0 = 매매중지, 1 = 매도매수가능, 2 = 매수만가능, 3 = 매도만가능
coin64 = "AQT" # 알파쿼크 - 김치토큰
coinMode64 = 1 # 0 = 매매중지, 1 = 매도매수가능, 2 = 매수만가능, 3 = 매도만가능
coin65 = "CBK" # 코박토큰
coinMode65 = 1 # 0 = 매매중지, 1 = 매도매수가능, 2 = 매수만가능, 3 = 매도만가능

coin66 = "AHT" # 아하토큰
coinMode66 = 1 # 0 = 매매중지, 1 = 매도매수가능, 2 = 매수만가능, 3 = 매도만가능
coin67 = "TON" # 톤
coinMode67 = 1 # 0 = 매매중지, 1 = 매도매수가능, 2 = 매수만가능, 3 = 매도만가능
coin68 = "META" # 메타디움
coinMode68 = 1 # 0 = 매매중지, 1 = 매도매수가능, 2 = 매수만가능, 3 = 매도만가능



##### 여기까지 매매 #####







coin69 = "MED" # 메디블록
coin70 = "CVC" # 시빅

coin71 = "ELF" # 엘프
coin72 = "STRAX" # 스트라티스
coin73 = "REP" # 어거
coin74 = "ARK" # 아크
coin75 = "DAWN" # 던프로토콜

coin76 = "STEEM" # 스팀
coin77 = "MTL" # 메탈
coin78 = "STRK" # 스트라이크
coin79 = "MVL" # 엠블 - 김치코인
coin80 = "QKC" # 쿼크체인

coin81 = "IQ" # 에브리피디아
coin82 = "JST" # 저스트
coin83 = "POWR" # 파워렛저
coin84 = "STPT" # 에스티피
coin85 = "SSX" # 썸씽 - 김치코인

coin86 = "PUNDIX" # 펀디엑스
coin87 = "SXP" # 스와이프
coin88 = "ARDR" # 아더
coin89 = "MFT" # 메인프레임
coin90 = "TT" # 썬더토큰

coin91 = "LOOM" # 룸네트워크
coin92 = "CRE" # 캐리프로토콜 - 김치코인
coin93 = "STMX" # 스톰엑스
coin94 = "UPP" # 센티넬프로토콜 - 김치코인
coin95 = "ONT" # 온톨로지

coin96 = "HUNT" # 헌트
coin97 = "GAS" # 가스
coin98 = "AERGO" # 아르고
coin99 = "RFR" # 리퍼리움 - 김치코인
coin100 = "GRS" # 그로스톨코인

coin101 = "MOC" # 모스코인 - 김치코인
coin102 = "SBD" # 스팀달러
coin103 = "MBL" # 무비블록 - 김치코인
coin104 = "FCT2" # 피르마체인 - 김치코인
coin105 = "POLY" # 폴리매쓰

coin106 = "IOST" # 아이오에스티
coin107 = "GLM" # 골렘
coin108 = "ONG" # 온톨로지가스


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





# 매매금액비율 산정

per1 = 5
per2 = 0.5

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
if macd1 >= 0:
    # 다음 코인 매매 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
    op_mode1 = 1

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd1}  |  매수가능 - {op_mode1} - 매수불가-매도가능")
    print("")
else:
    # 다음 코인 매매 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
    op_mode1 = 3

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd1}  |  매수가능 - {op_mode1} - 매수가능 매도불가")
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
if macd2 >= 0:
    # 다음 코인 매매 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
    op_mode2 = 1

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd2}  |  매수가능 - {op_mode2} - 매수불가-매도가능")
    print("")
else:
    # 다음 코인 매매 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
    op_mode2 = 3

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd2}  |  매수가능 - {op_mode2} - 매수가능-매도불가")
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
if macd3 >= 0:
    # 다음 코인 매매 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
    op_mode3 = 1

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd3}  |  매수가능 - {op_mode3} - 매수불가-매도가능")
    print("")
else:
    # 다음 코인 매매 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
    op_mode3 = 3

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd3}  |  매수가능 - {op_mode3} - 매수가능-매도불가")
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
if macd4 >= 0:
    # 다음 코인 매매 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
    op_mode4 = 1

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd4}  |  매수가능 - {op_mode4} - 매수불가-매도가능")
    print("")
else:
    # 다음 코인 매매 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
    op_mode4 = 3

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd4}  |  매수가능 - {op_mode4} - 매수가능-매도불가")
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
if macd5 >= 0:
    # 다음 코인 매매 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
    op_mode5 = 1

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd5}  |  매수가능 - {op_mode5} - 매수불가-매도가능")
    print("")
else:
    # 다음 코인 매매 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
    op_mode5 = 3

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd5}  |  매수가능 - {op_mode5} - 매수가능-매도불가")
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
if macd6 >= 0:
    # 다음 코인 매매 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
    op_mode6 = 1

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd6}  |  매수가능 - {op_mode6} - 매수불가-매도가능")
    print("")
else:
    # 다음 코인 매매 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
    op_mode6 = 3

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd6}  |  매수가능 - {op_mode6} - 매수가능-매도불가")
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
if macd7 >= 0:
    # 다음 코인 매매 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
    op_mode7 = 1

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd7}  |  매수가능 - {op_mode7} - 매수불가-매도가능")
    print("")
else:
    # 다음 코인 매매 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
    op_mode7 = 3

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd7}  |  매수가능 - {op_mode7} - 매수가능-매도불가")
    print("")

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
if macd8 >= 0:
    # 다음 코인 매매 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
    op_mode8 = 1

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd8}  |  매수가능 - {op_mode8} - 매수불가-매도가능")
    print("")
else:
    # 다음 코인 매매 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
    op_mode8 = 3

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd8}  |  매수가능 - {op_mode8} - 매수가능-매도불가")
    print("")

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
if macd9 >= 0:
    # 다음 코인 매매 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
    op_mode9 = 1

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd9}  |  매수가능 - {op_mode9} - 매수불가-매도가능")
    print("")
else:
    # 다음 코인 매매 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
    op_mode9 = 3

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd9}  |  매수가능 - {op_mode9} - 매수가능-매도불가")
    print("")

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
if macd10 >= 0:
    # 다음 코인 매매 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
    op_mode10 = 1

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd10}  |  매수가능 - {op_mode10} - 매수불가-매도가능")
    print("")
else:
    # 다음 코인 매매 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
    op_mode10 = 3

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd10}  |  매수가능 - {op_mode10} - 매수가능-매도불가")
    print("")

# 1초 딜레이.
time.sleep(1)
###############################





######################################################################################################################################################
######################################################################################################################################################
######################################################################################################################################################





###############################
# 코인11

# 보유수량 불러오기
krw_balance11 = upbit.get_balance(krw_coin11)
# 코인 현재가 불러오기
price11 = pyupbit.get_current_price(krw_coin11)
# 보유코인 원화금액으로 계산하기
bp11 = price11 * krw_balance11
# 코인 보유 현황 출력.
print(f"11. 코인명 : {coin11}  |  현재가 = ￦{price11}  |  보유수량 = {krw_balance11}  |  평가금액 = ￦{bp11}")

# MACD 조회.
#macd11 = get_macd(krw_coin11)
# 거래량 동반한 MACD 조회.
macd11 = get_acc_macd(krw_coin11)
# 5, 20일 이평선 조회.
#macd11 = get_ma20(krw_coin11)
# 거래량 동반한 5, 20일 이평선 조회.
#macd11 = get_acc_ma20(krw_coin11)

# 코인 보유 유무
if macd11 >= 0:
    # 다음 코인 매매 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
    op_mode11 = 1

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd11}  |  매수가능 - {op_mode11} - 매수불가-매도가능")
    print("")
else:
    # 다음 코인 매매 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
    op_mode11 = 3

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd11}  |  매수가능 - {op_mode11} - 매수가능 매도불가")
    print("")

# 1초 딜레이.
time.sleep(1)
###############################


###############################
# 코인12

# 보유수량 불러오기
krw_balance12 = upbit.get_balance(krw_coin12)
# 코인 현재가 불러오기
price12 = pyupbit.get_current_price(krw_coin12)
# 보유코인 원화금액으로 계산하기
bp12 = price12 * krw_balance12
# 코인 보유 현황 출력.
print(f"12. 코인명 : {coin12}  |  현재가 = ￦{price12}  |  보유수량 = {krw_balance12}  |  평가금액 = ￦{bp12}")

# MACD 조회.
#macd12 = get_macd(krw_coin12)
# 거래량 동반한 MACD 조회.
macd12 = get_acc_macd(krw_coin12)
# 5, 20일 이평선 조회.
#macd12 = get_ma20(krw_coin12)
# 거래량 동반한 5, 20일 이평선 조회.
#macd12 = get_acc_ma20(krw_coin12)

# 코인 보유 유무
if macd12 >= 0:
    # 다음 코인 매매 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
    op_mode12 = 1

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd12}  |  매수가능 - {op_mode12} - 매수불가-매도가능")
    print("")
else:
    # 다음 코인 매매 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
    op_mode12 = 3

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd12}  |  매수가능 - {op_mode12} - 매수가능-매도불가")
    print("")

# 1초 딜레이.
time.sleep(1)
###############################


###############################
# 코인13

# 보유수량 불러오기
krw_balance13 = upbit.get_balance(krw_coin13)
# 코인 현재가 불러오기
price13 = pyupbit.get_current_price(krw_coin13)
# 보유코인 원화금액으로 계산하기
bp13 = price13 * krw_balance13
# 코인 보유 현황 출력.
print(f"13. 코인명 : {coin13}  |  현재가 = ￦{price13}  |  보유수량 = {krw_balance13}  |  평가금액 = ￦{bp13}")

# MACD 조회.
#macd13 = get_macd(krw_coin13)
# 거래량 동반한 MACD 조회.
macd13 = get_acc_macd(krw_coin13)
# 5, 20일 이평선 조회.
#macd13 = get_ma20(krw_coin13)
# 거래량 동반한 5, 20일 이평선 조회.
#macd13 = get_acc_ma20(krw_coin13)

# 코인 보유 유무
if macd13 >= 0:
    # 다음 코인 매매 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
    op_mode13 = 1

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd13}  |  매수가능 - {op_mode13} - 매수불가-매도가능")
    print("")
else:
    # 다음 코인 매매 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
    op_mode13 = 3

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd13}  |  매수가능 - {op_mode13} - 매수가능-매도불가")
    print("")

# 1초 딜레이.
time.sleep(1)
###############################


###############################
# 코인14

# 보유수량 불러오기
krw_balance14 = upbit.get_balance(krw_coin14)
# 코인 현재가 불러오기
price14 = pyupbit.get_current_price(krw_coin14)
# 보유코인 원화금액으로 계산하기
bp14 = price14 * krw_balance14
# 코인 보유 현황 출력.
print(f"14. 코인명 : {coin14}  |  현재가 = ￦{price14}  |  보유수량 = {krw_balance14}  |  평가금액 = ￦{bp14}")

# MACD 조회.
#macd14 = get_macd(krw_coin14)
# 거래량 동반한 MACD 조회.
macd14 = get_acc_macd(krw_coin14)
# 5, 20일 이평선 조회.
#macd14 = get_ma20(krw_coin14)
# 거래량 동반한 5, 20일 이평선 조회.
#macd14 = get_acc_ma20(krw_coin14)

# 코인 보유 유무
if macd14 >= 0:
    # 다음 코인 매매 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
    op_mode14 = 1

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd14}  |  매수가능 - {op_mode14} - 매수불가-매도가능")
    print("")
else:
    # 다음 코인 매매 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
    op_mode14 = 3

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd14}  |  매수가능 - {op_mode14} - 매수가능-매도불가")
    print("")

# 1초 딜레이.
time.sleep(1)
###############################


###############################
# 코인15

# 보유수량 불러오기
krw_balance15 = upbit.get_balance(krw_coin15)
# 코인 현재가 불러오기
price15 = pyupbit.get_current_price(krw_coin15)
# 보유코인 원화금액으로 계산하기
bp15 = price15 * krw_balance15
# 코인 보유 현황 출력.
print(f"15. 코인명 : {coin15}  |  현재가 = ￦{price15}  |  보유수량 = {krw_balance15}  |  평가금액 = ￦{bp15}")

# MACD 조회.
#macd15 = get_macd(krw_coin15)
# 거래량 동반한 MACD 조회.
macd15 = get_acc_macd(krw_coin15)
# 5, 20일 이평선 조회.
#macd15 = get_ma20(krw_coin15)
# 거래량 동반한 5, 20일 이평선 조회.
#macd15 = get_acc_ma20(krw_coin15)

# 코인 보유 유무
if macd15 >= 0:
    # 다음 코인 매매 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
    op_mode15 = 1

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd15}  |  매수가능 - {op_mode15} - 매수불가-매도가능")
    print("")
else:
    # 다음 코인 매매 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
    op_mode15 = 3

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd15}  |  매수가능 - {op_mode15} - 매수가능-매도불가")
    print("")

# 1초 딜레이.
time.sleep(1)
###############################


###############################
# 코인16

# 보유수량 불러오기
krw_balance16 = upbit.get_balance(krw_coin16)
# 코인 현재가 불러오기
price16 = pyupbit.get_current_price(krw_coin16)
# 보유코인 원화금액으로 계산하기
bp16 = price16 * krw_balance16
# 코인 보유 현황 출력.
print(f"16. 코인명 : {coin16}  |  현재가 = ￦{price16}  |  보유수량 = {krw_balance16}  |  평가금액 = ￦{bp16}")

# MACD 조회.
#macd16 = get_macd(krw_coin16)
# 거래량 동반한 MACD 조회.
macd16 = get_acc_macd(krw_coin16)
# 5, 20일 이평선 조회.
#macd16 = get_ma20(krw_coin16)
# 거래량 동반한 5, 20일 이평선 조회.
#macd16 = get_acc_ma20(krw_coin16)

# 코인 보유 유무
if macd16 >= 0:
    # 다음 코인 매매 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
    op_mode16 = 1

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd16}  |  매수가능 - {op_mode16} - 매수불가-매도가능")
    print("")
else:
    # 다음 코인 매매 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
    op_mode16 = 3

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd16}  |  매수가능 - {op_mode16} - 매수가능-매도불가")
    print("")

# 1초 딜레이.
time.sleep(1)
###############################


###############################
# 코인17

# 보유수량 불러오기
krw_balance17 = upbit.get_balance(krw_coin17)
# 코인 현재가 불러오기
price17 = pyupbit.get_current_price(krw_coin17)
# 보유코인 원화금액으로 계산하기
bp17 = price17 * krw_balance17
# 코인 보유 현황 출력.
print(f"17. 코인명 : {coin17}  |  현재가 = ￦{price17}  |  보유수량 = {krw_balance17}  |  평가금액 = ￦{bp17}")

# MACD 조회.
#macd17 = get_macd(krw_coin17)
# 거래량 동반한 MACD 조회.
macd17 = get_acc_macd(krw_coin17)
# 5, 20일 이평선 조회.
#macd17 = get_ma20(krw_coin17)
# 거래량 동반한 5, 20일 이평선 조회.
#macd17 = get_acc_ma20(krw_coin17)

# 코인 보유 유무
if macd17 >= 0:
    # 다음 코인 매매 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
    op_mode17 = 1

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd17}  |  매수가능 - {op_mode17} - 매수불가-매도가능")
    print("")
else:
    # 다음 코인 매매 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
    op_mode17 = 3

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd17}  |  매수가능 - {op_mode17} - 매수가능-매도불가")
    print("")

# 1초 딜레이.
time.sleep(1)
###############################


###############################
# 코인18

# 보유수량 불러오기
krw_balance18 = upbit.get_balance(krw_coin18)
# 코인 현재가 불러오기
price18 = pyupbit.get_current_price(krw_coin18)
# 보유코인 원화금액으로 계산하기
bp18 = price18 * krw_balance18
# 코인 보유 현황 출력.
print(f"18. 코인명 : {coin18}  |  현재가 = ￦{price18}  |  보유수량 = {krw_balance18}  |  평가금액 = ￦{bp18}")

# MACD 조회.
#macd18 = get_macd(krw_coin18)
# 거래량 동반한 MACD 조회.
macd18 = get_acc_macd(krw_coin18)
# 5, 20일 이평선 조회.
#macd18 = get_ma20(krw_coin18)
# 거래량 동반한 5, 20일 이평선 조회.
#macd18 = get_acc_ma20(krw_coin18)

# 코인 보유 유무
if macd18 >= 0:
    # 다음 코인 매매 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
    op_mode18 = 1

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd18}  |  매수가능 - {op_mode18} - 매수불가-매도가능")
    print("")
else:
    # 다음 코인 매매 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
    op_mode18 = 3

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd18}  |  매수가능 - {op_mode18} - 매수가능-매도불가")
    print("")

# 1초 딜레이.
time.sleep(1)
###############################


###############################
# 코인19

# 보유수량 불러오기
krw_balance19 = upbit.get_balance(krw_coin19)
# 코인 현재가 불러오기
price19 = pyupbit.get_current_price(krw_coin19)
# 보유코인 원화금액으로 계산하기
bp19 = price19 * krw_balance19
# 코인 보유 현황 출력.
print(f"19. 코인명 : {coin19}  |  현재가 = ￦{price19}  |  보유수량 = {krw_balance19}  |  평가금액 = ￦{bp19}")

# MACD 조회.
#macd19 = get_macd(krw_coin19)
# 거래량 동반한 MACD 조회.
macd19 = get_acc_macd(krw_coin19)
# 5, 20일 이평선 조회.
#macd19 = get_ma20(krw_coin19)
# 거래량 동반한 5, 20일 이평선 조회.
#macd19 = get_acc_ma20(krw_coin19)

# 코인 보유 유무
if macd19 >= 0:
    # 다음 코인 매매 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
    op_mode19 = 1

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd19}  |  매수가능 - {op_mode19} - 매수불가-매도가능")
    print("")
else:
    # 다음 코인 매매 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
    op_mode19 = 3

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd19}  |  매수가능 - {op_mode19} - 매수가능-매도불가")
    print("")

# 1초 딜레이.
time.sleep(1)
###############################


###############################
# 코인20

# 보유수량 불러오기
krw_balance20 = upbit.get_balance(krw_coin20)
# 코인 현재가 불러오기
price20 = pyupbit.get_current_price(krw_coin20)
# 보유코인 원화금액으로 계산하기
bp20 = price20 * krw_balance20
# 코인 보유 현황 출력.
print(f"20. 코인명 : {coin20}  |  현재가 = ￦{price20}  |  보유수량 = {krw_balance20}  |  평가금액 = ￦{bp20}")

# MACD 조회.
#macd20 = get_macd(krw_coin20)
# 거래량 동반한 MACD 조회.
macd20 = get_acc_macd(krw_coin20)
# 5, 20일 이평선 조회.
#macd20 = get_ma20(krw_coin20)
# 거래량 동반한 5, 20일 이평선 조회.
#macd20 = get_acc_ma20(krw_coin20)

# 코인 보유 유무
if macd20 >= 0:
    # 다음 코인 매매 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
    op_mode20 = 1

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd20}  |  매수가능 - {op_mode20} - 매수불가-매도가능")
    print("")
else:
    # 다음 코인 매매 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
    op_mode20 = 3

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd20}  |  매수가능 - {op_mode20} - 매수가능-매도불가")
    print("")

# 1초 딜레이.
time.sleep(1)
###############################





######################################################################################################################################################
######################################################################################################################################################
######################################################################################################################################################





###############################
# 코인21

# 보유수량 불러오기
krw_balance21 = upbit.get_balance(krw_coin21)
# 코인 현재가 불러오기
price21 = pyupbit.get_current_price(krw_coin21)
# 보유코인 원화금액으로 계산하기
bp21 = price21 * krw_balance21
# 코인 보유 현황 출력.
print(f"21. 코인명 : {coin21}  |  현재가 = ￦{price21}  |  보유수량 = {krw_balance21}  |  평가금액 = ￦{bp21}")

# MACD 조회.
#macd21 = get_macd(krw_coin21)
# 거래량 동반한 MACD 조회.
macd21 = get_acc_macd(krw_coin21)
# 5, 20일 이평선 조회.
#macd21 = get_ma20(krw_coin21)
# 거래량 동반한 5, 20일 이평선 조회.
#macd21 = get_acc_ma20(krw_coin21)

# 코인 보유 유무
if macd21 >= 0:
    # 다음 코인 매매 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
    op_mode21 = 1

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd21}  |  매수가능 - {op_mode21} - 매수불가-매도가능")
    print("")
else:
    # 다음 코인 매매 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
    op_mode21 = 3

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd21}  |  매수가능 - {op_mode21} - 매수가능 매도불가")
    print("")

# 1초 딜레이.
time.sleep(1)
###############################


###############################
# 코인22

# 보유수량 불러오기
krw_balance22 = upbit.get_balance(krw_coin22)
# 코인 현재가 불러오기
price22 = pyupbit.get_current_price(krw_coin22)
# 보유코인 원화금액으로 계산하기
bp22 = price22 * krw_balance22
# 코인 보유 현황 출력.
print(f"22. 코인명 : {coin22}  |  현재가 = ￦{price22}  |  보유수량 = {krw_balance22}  |  평가금액 = ￦{bp22}")

# MACD 조회.
#macd22 = get_macd(krw_coin22)
# 거래량 동반한 MACD 조회.
macd22 = get_acc_macd(krw_coin22)
# 5, 20일 이평선 조회.
#macd22 = get_ma20(krw_coin22)
# 거래량 동반한 5, 20일 이평선 조회.
#macd22 = get_acc_ma20(krw_coin22)

# 코인 보유 유무
if macd22 >= 0:
    # 다음 코인 매매 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
    op_mode22 = 1

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd22}  |  매수가능 - {op_mode22} - 매수불가-매도가능")
    print("")
else:
    # 다음 코인 매매 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
    op_mode22 = 3

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd22}  |  매수가능 - {op_mode22} - 매수가능-매도불가")
    print("")

# 1초 딜레이.
time.sleep(1)
###############################


###############################
# 코인23

# 보유수량 불러오기
krw_balance23 = upbit.get_balance(krw_coin23)
# 코인 현재가 불러오기
price23 = pyupbit.get_current_price(krw_coin23)
# 보유코인 원화금액으로 계산하기
bp23 = price23 * krw_balance23
# 코인 보유 현황 출력.
print(f"23. 코인명 : {coin23}  |  현재가 = ￦{price23}  |  보유수량 = {krw_balance23}  |  평가금액 = ￦{bp23}")

# MACD 조회.
#macd23 = get_macd(krw_coin23)
# 거래량 동반한 MACD 조회.
macd23 = get_acc_macd(krw_coin23)
# 5, 20일 이평선 조회.
#macd23 = get_ma20(krw_coin23)
# 거래량 동반한 5, 20일 이평선 조회.
#macd23 = get_acc_ma20(krw_coin23)

# 코인 보유 유무
if macd23 >= 0:
    # 다음 코인 매매 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
    op_mode23 = 1

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd23}  |  매수가능 - {op_mode23} - 매수불가-매도가능")
    print("")
else:
    # 다음 코인 매매 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
    op_mode23 = 3

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd23}  |  매수가능 - {op_mode23} - 매수가능-매도불가")
    print("")

# 1초 딜레이.
time.sleep(1)
###############################


###############################
# 코인24

# 보유수량 불러오기
krw_balance24 = upbit.get_balance(krw_coin24)
# 코인 현재가 불러오기
price24 = pyupbit.get_current_price(krw_coin24)
# 보유코인 원화금액으로 계산하기
bp24 = price24 * krw_balance24
# 코인 보유 현황 출력.
print(f"24. 코인명 : {coin24}  |  현재가 = ￦{price24}  |  보유수량 = {krw_balance24}  |  평가금액 = ￦{bp24}")

# MACD 조회.
#macd24 = get_macd(krw_coin24)
# 거래량 동반한 MACD 조회.
macd24 = get_acc_macd(krw_coin24)
# 5, 20일 이평선 조회.
#macd24 = get_ma20(krw_coin24)
# 거래량 동반한 5, 20일 이평선 조회.
#macd24 = get_acc_ma20(krw_coin24)

# 코인 보유 유무
if macd24 >= 0:
    # 다음 코인 매매 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
    op_mode24 = 1

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd24}  |  매수가능 - {op_mode24} - 매수불가-매도가능")
    print("")
else:
    # 다음 코인 매매 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
    op_mode24 = 3

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd24}  |  매수가능 - {op_mode24} - 매수가능-매도불가")
    print("")

# 1초 딜레이.
time.sleep(1)
###############################


###############################
# 코인25

# 보유수량 불러오기
krw_balance25 = upbit.get_balance(krw_coin25)
# 코인 현재가 불러오기
price25 = pyupbit.get_current_price(krw_coin25)
# 보유코인 원화금액으로 계산하기
bp25 = price25 * krw_balance25
# 코인 보유 현황 출력.
print(f"25. 코인명 : {coin25}  |  현재가 = ￦{price25}  |  보유수량 = {krw_balance25}  |  평가금액 = ￦{bp25}")

# MACD 조회.
#macd25 = get_macd(krw_coin25)
# 거래량 동반한 MACD 조회.
macd25 = get_acc_macd(krw_coin25)
# 5, 20일 이평선 조회.
#macd25 = get_ma20(krw_coin25)
# 거래량 동반한 5, 20일 이평선 조회.
#macd25 = get_acc_ma20(krw_coin25)

# 코인 보유 유무
if macd25 >= 0:
    # 다음 코인 매매 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
    op_mode25 = 1

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd25}  |  매수가능 - {op_mode25} - 매수불가-매도가능")
    print("")
else:
    # 다음 코인 매매 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
    op_mode25 = 3

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd25}  |  매수가능 - {op_mode25} - 매수가능-매도불가")
    print("")

# 1초 딜레이.
time.sleep(1)
###############################


###############################
# 코인26

# 보유수량 불러오기
krw_balance26 = upbit.get_balance(krw_coin26)
# 코인 현재가 불러오기
price26 = pyupbit.get_current_price(krw_coin26)
# 보유코인 원화금액으로 계산하기
bp26 = price26 * krw_balance26
# 코인 보유 현황 출력.
print(f"26. 코인명 : {coin26}  |  현재가 = ￦{price26}  |  보유수량 = {krw_balance26}  |  평가금액 = ￦{bp26}")

# MACD 조회.
#macd26 = get_macd(krw_coin26)
# 거래량 동반한 MACD 조회.
macd26 = get_acc_macd(krw_coin26)
# 5, 20일 이평선 조회.
#macd26 = get_ma20(krw_coin26)
# 거래량 동반한 5, 20일 이평선 조회.
#macd26 = get_acc_ma20(krw_coin26)

# 코인 보유 유무
if macd26 >= 0:
    # 다음 코인 매매 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
    op_mode26 = 1

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd26}  |  매수가능 - {op_mode26} - 매수불가-매도가능")
    print("")
else:
    # 다음 코인 매매 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
    op_mode26 = 3

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd26}  |  매수가능 - {op_mode26} - 매수가능-매도불가")
    print("")

# 1초 딜레이.
time.sleep(1)
###############################


###############################
# 코인27

# 보유수량 불러오기
krw_balance27 = upbit.get_balance(krw_coin27)
# 코인 현재가 불러오기
price27 = pyupbit.get_current_price(krw_coin27)
# 보유코인 원화금액으로 계산하기
bp27 = price27 * krw_balance27
# 코인 보유 현황 출력.
print(f"27. 코인명 : {coin27}  |  현재가 = ￦{price27}  |  보유수량 = {krw_balance27}  |  평가금액 = ￦{bp27}")

# MACD 조회.
#macd27 = get_macd(krw_coin27)
# 거래량 동반한 MACD 조회.
macd27 = get_acc_macd(krw_coin27)
# 5, 20일 이평선 조회.
#macd27 = get_ma20(krw_coin27)
# 거래량 동반한 5, 20일 이평선 조회.
#macd27 = get_acc_ma20(krw_coin27)

# 코인 보유 유무
if macd27 >= 0:
    # 다음 코인 매매 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
    op_mode27 = 1

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd27}  |  매수가능 - {op_mode27} - 매수불가-매도가능")
    print("")
else:
    # 다음 코인 매매 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
    op_mode27 = 3

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd27}  |  매수가능 - {op_mode27} - 매수가능-매도불가")
    print("")

# 1초 딜레이.
time.sleep(1)
###############################


###############################
# 코인28

# 보유수량 불러오기
krw_balance28 = upbit.get_balance(krw_coin28)
# 코인 현재가 불러오기
price28 = pyupbit.get_current_price(krw_coin28)
# 보유코인 원화금액으로 계산하기
bp28 = price28 * krw_balance28
# 코인 보유 현황 출력.
print(f"28. 코인명 : {coin28}  |  현재가 = ￦{price28}  |  보유수량 = {krw_balance28}  |  평가금액 = ￦{bp28}")

# MACD 조회.
#macd28 = get_macd(krw_coin28)
# 거래량 동반한 MACD 조회.
macd28 = get_acc_macd(krw_coin28)
# 5, 20일 이평선 조회.
#macd28 = get_ma20(krw_coin28)
# 거래량 동반한 5, 20일 이평선 조회.
#macd28 = get_acc_ma20(krw_coin28)

# 코인 보유 유무
if macd28 >= 0:
    # 다음 코인 매매 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
    op_mode28 = 1

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd28}  |  매수가능 - {op_mode28} - 매수불가-매도가능")
    print("")
else:
    # 다음 코인 매매 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
    op_mode28 = 3

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd28}  |  매수가능 - {op_mode28} - 매수가능-매도불가")
    print("")

# 1초 딜레이.
time.sleep(1)
###############################


###############################
# 코인29

# 보유수량 불러오기
krw_balance29 = upbit.get_balance(krw_coin29)
# 코인 현재가 불러오기
price29 = pyupbit.get_current_price(krw_coin29)
# 보유코인 원화금액으로 계산하기
bp29 = price29 * krw_balance29
# 코인 보유 현황 출력.
print(f"29. 코인명 : {coin29}  |  현재가 = ￦{price29}  |  보유수량 = {krw_balance29}  |  평가금액 = ￦{bp29}")

# MACD 조회.
#macd29 = get_macd(krw_coin29)
# 거래량 동반한 MACD 조회.
macd29 = get_acc_macd(krw_coin29)
# 5, 20일 이평선 조회.
#macd29 = get_ma20(krw_coin29)
# 거래량 동반한 5, 20일 이평선 조회.
#macd29 = get_acc_ma20(krw_coin29)

# 코인 보유 유무
if macd29 >= 0:
    # 다음 코인 매매 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
    op_mode29 = 1

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd29}  |  매수가능 - {op_mode29} - 매수불가-매도가능")
    print("")
else:
    # 다음 코인 매매 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
    op_mode29 = 3

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd29}  |  매수가능 - {op_mode29} - 매수가능-매도불가")
    print("")

# 1초 딜레이.
time.sleep(1)
###############################


###############################
# 코인30

# 보유수량 불러오기
krw_balance30 = upbit.get_balance(krw_coin30)
# 코인 현재가 불러오기
price30 = pyupbit.get_current_price(krw_coin30)
# 보유코인 원화금액으로 계산하기
bp30 = price30 * krw_balance30
# 코인 보유 현황 출력.
print(f"30. 코인명 : {coin30}  |  현재가 = ￦{price30}  |  보유수량 = {krw_balance30}  |  평가금액 = ￦{bp30}")

# MACD 조회.
#macd30 = get_macd(krw_coin30)
# 거래량 동반한 MACD 조회.
macd30 = get_acc_macd(krw_coin30)
# 5, 20일 이평선 조회.
#macd30 = get_ma20(krw_coin30)
# 거래량 동반한 5, 20일 이평선 조회.
#macd30 = get_acc_ma20(krw_coin30)

# 코인 보유 유무
if macd30 >= 0:
    # 다음 코인 매매 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
    op_mode30 = 1

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd30}  |  매수가능 - {op_mode30} - 매수불가-매도가능")
    print("")
else:
    # 다음 코인 매매 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
    op_mode30 = 3

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd30}  |  매수가능 - {op_mode30} - 매수가능-매도불가")
    print("")

# 1초 딜레이.
time.sleep(1)
###############################





######################################################################################################################################################
######################################################################################################################################################
######################################################################################################################################################





###############################
# 코인31

# 보유수량 불러오기
krw_balance31 = upbit.get_balance(krw_coin31)
# 코인 현재가 불러오기
price31 = pyupbit.get_current_price(krw_coin31)
# 보유코인 원화금액으로 계산하기
bp31 = price31 * krw_balance31
# 코인 보유 현황 출력.
print(f"31. 코인명 : {coin31}  |  현재가 = ￦{price31}  |  보유수량 = {krw_balance31}  |  평가금액 = ￦{bp31}")

# MACD 조회.
#macd31 = get_macd(krw_coin31)
# 거래량 동반한 MACD 조회.
macd31 = get_acc_macd(krw_coin31)
# 5, 20일 이평선 조회.
#macd31 = get_ma20(krw_coin31)
# 거래량 동반한 5, 20일 이평선 조회.
#macd31 = get_acc_ma20(krw_coin31)

# 코인 보유 유무
if macd31 >= 0:
    # 다음 코인 매매 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
    op_mode31 = 1

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd31}  |  매수가능 - {op_mode31} - 매수불가-매도가능")
    print("")
else:
    # 다음 코인 매매 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
    op_mode31 = 3

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd31}  |  매수가능 - {op_mode31} - 매수가능 매도불가")
    print("")

# 1초 딜레이.
time.sleep(1)
###############################


###############################
# 코인32

# 보유수량 불러오기
krw_balance32 = upbit.get_balance(krw_coin32)
# 코인 현재가 불러오기
price32 = pyupbit.get_current_price(krw_coin32)
# 보유코인 원화금액으로 계산하기
bp32 = price32 * krw_balance32
# 코인 보유 현황 출력.
print(f"32. 코인명 : {coin32}  |  현재가 = ￦{price32}  |  보유수량 = {krw_balance32}  |  평가금액 = ￦{bp32}")

# MACD 조회.
#macd32 = get_macd(krw_coin32)
# 거래량 동반한 MACD 조회.
macd32 = get_acc_macd(krw_coin32)
# 5, 20일 이평선 조회.
#macd32 = get_ma20(krw_coin32)
# 거래량 동반한 5, 20일 이평선 조회.
#macd32 = get_acc_ma20(krw_coin32)

# 코인 보유 유무
if macd32 >= 0:
    # 다음 코인 매매 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
    op_mode32 = 1

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd32}  |  매수가능 - {op_mode32} - 매수불가-매도가능")
    print("")
else:
    # 다음 코인 매매 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
    op_mode32 = 3

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd32}  |  매수가능 - {op_mode32} - 매수가능-매도불가")
    print("")

# 1초 딜레이.
time.sleep(1)
###############################


###############################
# 코인33

# 보유수량 불러오기
krw_balance33 = upbit.get_balance(krw_coin33)
# 코인 현재가 불러오기
price33 = pyupbit.get_current_price(krw_coin33)
# 보유코인 원화금액으로 계산하기
bp33 = price33 * krw_balance33
# 코인 보유 현황 출력.
print(f"33. 코인명 : {coin33}  |  현재가 = ￦{price33}  |  보유수량 = {krw_balance33}  |  평가금액 = ￦{bp33}")

# MACD 조회.
#macd33 = get_macd(krw_coin33)
# 거래량 동반한 MACD 조회.
macd33 = get_acc_macd(krw_coin33)
# 5, 20일 이평선 조회.
#macd33 = get_ma20(krw_coin33)
# 거래량 동반한 5, 20일 이평선 조회.
#macd33 = get_acc_ma20(krw_coin33)

# 코인 보유 유무
if macd33 >= 0:
    # 다음 코인 매매 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
    op_mode33 = 1

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd33}  |  매수가능 - {op_mode33} - 매수불가-매도가능")
    print("")
else:
    # 다음 코인 매매 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
    op_mode33 = 3

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd33}  |  매수가능 - {op_mode33} - 매수가능-매도불가")
    print("")

# 1초 딜레이.
time.sleep(1)
###############################


###############################
# 코인34

# 보유수량 불러오기
krw_balance34 = upbit.get_balance(krw_coin34)
# 코인 현재가 불러오기
price34 = pyupbit.get_current_price(krw_coin34)
# 보유코인 원화금액으로 계산하기
bp34 = price34 * krw_balance34
# 코인 보유 현황 출력.
print(f"34. 코인명 : {coin34}  |  현재가 = ￦{price34}  |  보유수량 = {krw_balance34}  |  평가금액 = ￦{bp34}")

# MACD 조회.
#macd34 = get_macd(krw_coin34)
# 거래량 동반한 MACD 조회.
macd34 = get_acc_macd(krw_coin34)
# 5, 20일 이평선 조회.
#macd34 = get_ma20(krw_coin34)
# 거래량 동반한 5, 20일 이평선 조회.
#macd34 = get_acc_ma20(krw_coin34)

# 코인 보유 유무
if macd34 >= 0:
    # 다음 코인 매매 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
    op_mode34 = 1

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd34}  |  매수가능 - {op_mode34} - 매수불가-매도가능")
    print("")
else:
    # 다음 코인 매매 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
    op_mode34 = 3

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd34}  |  매수가능 - {op_mode34} - 매수가능-매도불가")
    print("")

# 1초 딜레이.
time.sleep(1)
###############################


###############################
# 코인35

# 보유수량 불러오기
krw_balance35 = upbit.get_balance(krw_coin35)
# 코인 현재가 불러오기
price35 = pyupbit.get_current_price(krw_coin35)
# 보유코인 원화금액으로 계산하기
bp35 = price35 * krw_balance35
# 코인 보유 현황 출력.
print(f"35. 코인명 : {coin35}  |  현재가 = ￦{price35}  |  보유수량 = {krw_balance35}  |  평가금액 = ￦{bp35}")

# MACD 조회.
#macd35 = get_macd(krw_coin35)
# 거래량 동반한 MACD 조회.
macd35 = get_acc_macd(krw_coin35)
# 5, 20일 이평선 조회.
#macd35 = get_ma20(krw_coin35)
# 거래량 동반한 5, 20일 이평선 조회.
#macd35 = get_acc_ma20(krw_coin35)

# 코인 보유 유무
if macd35 >= 0:
    # 다음 코인 매매 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
    op_mode35 = 1

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd35}  |  매수가능 - {op_mode35} - 매수불가-매도가능")
    print("")
else:
    # 다음 코인 매매 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
    op_mode35 = 3

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd35}  |  매수가능 - {op_mode35} - 매수가능-매도불가")
    print("")

# 1초 딜레이.
time.sleep(1)
###############################


###############################
# 코인36

# 보유수량 불러오기
krw_balance36 = upbit.get_balance(krw_coin36)
# 코인 현재가 불러오기
price36 = pyupbit.get_current_price(krw_coin36)
# 보유코인 원화금액으로 계산하기
bp36 = price36 * krw_balance36
# 코인 보유 현황 출력.
print(f"36. 코인명 : {coin36}  |  현재가 = ￦{price36}  |  보유수량 = {krw_balance36}  |  평가금액 = ￦{bp36}")

# MACD 조회.
#macd36 = get_macd(krw_coin36)
# 거래량 동반한 MACD 조회.
macd36 = get_acc_macd(krw_coin36)
# 5, 20일 이평선 조회.
#macd36 = get_ma20(krw_coin36)
# 거래량 동반한 5, 20일 이평선 조회.
#macd36 = get_acc_ma20(krw_coin36)

# 코인 보유 유무
if macd36 >= 0:
    # 다음 코인 매매 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
    op_mode36 = 1

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd36}  |  매수가능 - {op_mode36} - 매수불가-매도가능")
    print("")
else:
    # 다음 코인 매매 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
    op_mode36 = 3

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd36}  |  매수가능 - {op_mode36} - 매수가능-매도불가")
    print("")

# 1초 딜레이.
time.sleep(1)
###############################


###############################
# 코인37

# 보유수량 불러오기
krw_balance37 = upbit.get_balance(krw_coin37)
# 코인 현재가 불러오기
price37 = pyupbit.get_current_price(krw_coin37)
# 보유코인 원화금액으로 계산하기
bp37 = price37 * krw_balance37
# 코인 보유 현황 출력.
print(f"37. 코인명 : {coin37}  |  현재가 = ￦{price37}  |  보유수량 = {krw_balance37}  |  평가금액 = ￦{bp37}")

# MACD 조회.
#macd37 = get_macd(krw_coin37)
# 거래량 동반한 MACD 조회.
macd37 = get_acc_macd(krw_coin37)
# 5, 20일 이평선 조회.
#macd37 = get_ma20(krw_coin37)
# 거래량 동반한 5, 20일 이평선 조회.
#macd37 = get_acc_ma20(krw_coin37)

# 코인 보유 유무
if macd37 >= 0:
    # 다음 코인 매매 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
    op_mode37 = 1

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd37}  |  매수가능 - {op_mode37} - 매수불가-매도가능")
    print("")
else:
    # 다음 코인 매매 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
    op_mode37 = 3

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd37}  |  매수가능 - {op_mode37} - 매수가능-매도불가")
    print("")

# 1초 딜레이.
time.sleep(1)
###############################


###############################
# 코인38

# 보유수량 불러오기
krw_balance38 = upbit.get_balance(krw_coin38)
# 코인 현재가 불러오기
price38 = pyupbit.get_current_price(krw_coin38)
# 보유코인 원화금액으로 계산하기
bp38 = price38 * krw_balance38
# 코인 보유 현황 출력.
print(f"38. 코인명 : {coin38}  |  현재가 = ￦{price38}  |  보유수량 = {krw_balance38}  |  평가금액 = ￦{bp38}")

# MACD 조회.
#macd38 = get_macd(krw_coin38)
# 거래량 동반한 MACD 조회.
macd38 = get_acc_macd(krw_coin38)
# 5, 20일 이평선 조회.
#macd38 = get_ma20(krw_coin38)
# 거래량 동반한 5, 20일 이평선 조회.
#macd38 = get_acc_ma20(krw_coin38)

# 코인 보유 유무
if macd38 >= 0:
    # 다음 코인 매매 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
    op_mode38 = 1

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd38}  |  매수가능 - {op_mode38} - 매수불가-매도가능")
    print("")
else:
    # 다음 코인 매매 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
    op_mode38 = 3

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd38}  |  매수가능 - {op_mode38} - 매수가능-매도불가")
    print("")

# 1초 딜레이.
time.sleep(1)
###############################


###############################
# 코인39

# 보유수량 불러오기
krw_balance39 = upbit.get_balance(krw_coin39)
# 코인 현재가 불러오기
price39 = pyupbit.get_current_price(krw_coin39)
# 보유코인 원화금액으로 계산하기
bp39 = price39 * krw_balance39
# 코인 보유 현황 출력.
print(f"39. 코인명 : {coin39}  |  현재가 = ￦{price39}  |  보유수량 = {krw_balance39}  |  평가금액 = ￦{bp39}")

# MACD 조회.
#macd39 = get_macd(krw_coin39)
# 거래량 동반한 MACD 조회.
macd39 = get_acc_macd(krw_coin39)
# 5, 20일 이평선 조회.
#macd39 = get_ma20(krw_coin39)
# 거래량 동반한 5, 20일 이평선 조회.
#macd39 = get_acc_ma20(krw_coin39)

# 코인 보유 유무
if macd39 >= 0:
    # 다음 코인 매매 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
    op_mode39 = 1

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd39}  |  매수가능 - {op_mode39} - 매수불가-매도가능")
    print("")
else:
    # 다음 코인 매매 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
    op_mode39 = 3

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd39}  |  매수가능 - {op_mode39} - 매수가능-매도불가")
    print("")

# 1초 딜레이.
time.sleep(1)
###############################


###############################
# 코인40

# 보유수량 불러오기
krw_balance40 = upbit.get_balance(krw_coin40)
# 코인 현재가 불러오기
price40 = pyupbit.get_current_price(krw_coin40)
# 보유코인 원화금액으로 계산하기
bp40 = price40 * krw_balance40
# 코인 보유 현황 출력.
print(f"40. 코인명 : {coin40}  |  현재가 = ￦{price40}  |  보유수량 = {krw_balance40}  |  평가금액 = ￦{bp40}")

# MACD 조회.
#macd40 = get_macd(krw_coin40)
# 거래량 동반한 MACD 조회.
macd40 = get_acc_macd(krw_coin40)
# 5, 20일 이평선 조회.
#macd40 = get_ma20(krw_coin40)
# 거래량 동반한 5, 20일 이평선 조회.
#macd40 = get_acc_ma20(krw_coin40)

# 코인 보유 유무
if macd40 >= 0:
    # 다음 코인 매매 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
    op_mode40 = 1

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd40}  |  매수가능 - {op_mode40} - 매수불가-매도가능")
    print("")
else:
    # 다음 코인 매매 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
    op_mode40 = 3

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd40}  |  매수가능 - {op_mode40} - 매수가능-매도불가")
    print("")

# 1초 딜레이.
time.sleep(1)
###############################





######################################################################################################################################################
######################################################################################################################################################
######################################################################################################################################################





###############################
# 코인41

# 보유수량 불러오기
krw_balance41 = upbit.get_balance(krw_coin41)
# 코인 현재가 불러오기
price41 = pyupbit.get_current_price(krw_coin41)
# 보유코인 원화금액으로 계산하기
bp41 = price41 * krw_balance41
# 코인 보유 현황 출력.
print(f"41. 코인명 : {coin41}  |  현재가 = ￦{price41}  |  보유수량 = {krw_balance41}  |  평가금액 = ￦{bp41}")

# MACD 조회.
#macd41 = get_macd(krw_coin41)
# 거래량 동반한 MACD 조회.
macd41 = get_acc_macd(krw_coin41)
# 5, 20일 이평선 조회.
#macd41 = get_ma20(krw_coin41)
# 거래량 동반한 5, 20일 이평선 조회.
#macd41 = get_acc_ma20(krw_coin41)

# 코인 보유 유무
if macd41 >= 0:
    # 다음 코인 매매 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
    op_mode41 = 1

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd41}  |  매수가능 - {op_mode41} - 매수불가-매도가능")
    print("")
else:
    # 다음 코인 매매 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
    op_mode41 = 3

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd41}  |  매수가능 - {op_mode41} - 매수가능 매도불가")
    print("")

# 1초 딜레이.
time.sleep(1)
###############################


###############################
# 코인42

# 보유수량 불러오기
krw_balance42 = upbit.get_balance(krw_coin42)
# 코인 현재가 불러오기
price42 = pyupbit.get_current_price(krw_coin42)
# 보유코인 원화금액으로 계산하기
bp42 = price42 * krw_balance42
# 코인 보유 현황 출력.
print(f"42. 코인명 : {coin42}  |  현재가 = ￦{price42}  |  보유수량 = {krw_balance42}  |  평가금액 = ￦{bp42}")

# MACD 조회.
#macd42 = get_macd(krw_coin42)
# 거래량 동반한 MACD 조회.
macd42 = get_acc_macd(krw_coin42)
# 5, 20일 이평선 조회.
#macd42 = get_ma20(krw_coin42)
# 거래량 동반한 5, 20일 이평선 조회.
#macd42 = get_acc_ma20(krw_coin42)

# 코인 보유 유무
if macd42 >= 0:
    # 다음 코인 매매 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
    op_mode42 = 1

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd42}  |  매수가능 - {op_mode42} - 매수불가-매도가능")
    print("")
else:
    # 다음 코인 매매 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
    op_mode42 = 3

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd42}  |  매수가능 - {op_mode42} - 매수가능-매도불가")
    print("")

# 1초 딜레이.
time.sleep(1)
###############################


###############################
# 코인43

# 보유수량 불러오기
krw_balance43 = upbit.get_balance(krw_coin43)
# 코인 현재가 불러오기
price43 = pyupbit.get_current_price(krw_coin43)
# 보유코인 원화금액으로 계산하기
bp43 = price43 * krw_balance43
# 코인 보유 현황 출력.
print(f"43. 코인명 : {coin43}  |  현재가 = ￦{price43}  |  보유수량 = {krw_balance43}  |  평가금액 = ￦{bp43}")

# MACD 조회.
#macd43 = get_macd(krw_coin43)
# 거래량 동반한 MACD 조회.
macd43 = get_acc_macd(krw_coin43)
# 5, 20일 이평선 조회.
#macd43 = get_ma20(krw_coin43)
# 거래량 동반한 5, 20일 이평선 조회.
#macd43 = get_acc_ma20(krw_coin43)

# 코인 보유 유무
if macd43 >= 0:
    # 다음 코인 매매 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
    op_mode43 = 1

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd43}  |  매수가능 - {op_mode43} - 매수불가-매도가능")
    print("")
else:
    # 다음 코인 매매 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
    op_mode43 = 3

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd43}  |  매수가능 - {op_mode43} - 매수가능-매도불가")
    print("")

# 1초 딜레이.
time.sleep(1)
###############################


###############################
# 코인44

# 보유수량 불러오기
krw_balance44 = upbit.get_balance(krw_coin44)
# 코인 현재가 불러오기
price44 = pyupbit.get_current_price(krw_coin44)
# 보유코인 원화금액으로 계산하기
bp44 = price44 * krw_balance44
# 코인 보유 현황 출력.
print(f"44. 코인명 : {coin44}  |  현재가 = ￦{price44}  |  보유수량 = {krw_balance44}  |  평가금액 = ￦{bp44}")

# MACD 조회.
#macd44 = get_macd(krw_coin44)
# 거래량 동반한 MACD 조회.
macd44 = get_acc_macd(krw_coin44)
# 5, 20일 이평선 조회.
#macd44 = get_ma20(krw_coin44)
# 거래량 동반한 5, 20일 이평선 조회.
#macd44 = get_acc_ma20(krw_coin44)

# 코인 보유 유무
if macd44 >= 0:
    # 다음 코인 매매 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
    op_mode44 = 1

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd44}  |  매수가능 - {op_mode44} - 매수불가-매도가능")
    print("")
else:
    # 다음 코인 매매 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
    op_mode44 = 3

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd44}  |  매수가능 - {op_mode44} - 매수가능-매도불가")
    print("")

# 1초 딜레이.
time.sleep(1)
###############################


###############################
# 코인45

# 보유수량 불러오기
krw_balance45 = upbit.get_balance(krw_coin45)
# 코인 현재가 불러오기
price45 = pyupbit.get_current_price(krw_coin45)
# 보유코인 원화금액으로 계산하기
bp45 = price45 * krw_balance45
# 코인 보유 현황 출력.
print(f"45. 코인명 : {coin45}  |  현재가 = ￦{price45}  |  보유수량 = {krw_balance45}  |  평가금액 = ￦{bp45}")

# MACD 조회.
#macd45 = get_macd(krw_coin45)
# 거래량 동반한 MACD 조회.
macd45 = get_acc_macd(krw_coin45)
# 5, 20일 이평선 조회.
#macd45 = get_ma20(krw_coin45)
# 거래량 동반한 5, 20일 이평선 조회.
#macd45 = get_acc_ma20(krw_coin45)

# 코인 보유 유무
if macd45 >= 0:
    # 다음 코인 매매 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
    op_mode45 = 1

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd45}  |  매수가능 - {op_mode45} - 매수불가-매도가능")
    print("")
else:
    # 다음 코인 매매 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
    op_mode45 = 3

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd45}  |  매수가능 - {op_mode45} - 매수가능-매도불가")
    print("")

# 1초 딜레이.
time.sleep(1)
###############################


###############################
# 코인46

# 보유수량 불러오기
krw_balance46 = upbit.get_balance(krw_coin46)
# 코인 현재가 불러오기
price46 = pyupbit.get_current_price(krw_coin46)
# 보유코인 원화금액으로 계산하기
bp46 = price46 * krw_balance46
# 코인 보유 현황 출력.
print(f"46. 코인명 : {coin46}  |  현재가 = ￦{price46}  |  보유수량 = {krw_balance46}  |  평가금액 = ￦{bp46}")

# MACD 조회.
#macd46 = get_macd(krw_coin46)
# 거래량 동반한 MACD 조회.
macd46 = get_acc_macd(krw_coin46)
# 5, 20일 이평선 조회.
#macd46 = get_ma20(krw_coin46)
# 거래량 동반한 5, 20일 이평선 조회.
#macd46 = get_acc_ma20(krw_coin46)

# 코인 보유 유무
if macd46 >= 0:
    # 다음 코인 매매 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
    op_mode46 = 1

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd46}  |  매수가능 - {op_mode46} - 매수불가-매도가능")
    print("")
else:
    # 다음 코인 매매 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
    op_mode46 = 3

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd46}  |  매수가능 - {op_mode46} - 매수가능-매도불가")
    print("")

# 1초 딜레이.
time.sleep(1)
###############################


###############################
# 코인47

# 보유수량 불러오기
krw_balance47 = upbit.get_balance(krw_coin47)
# 코인 현재가 불러오기
price47 = pyupbit.get_current_price(krw_coin47)
# 보유코인 원화금액으로 계산하기
bp47 = price47 * krw_balance47
# 코인 보유 현황 출력.
print(f"47. 코인명 : {coin47}  |  현재가 = ￦{price47}  |  보유수량 = {krw_balance47}  |  평가금액 = ￦{bp47}")

# MACD 조회.
#macd47 = get_macd(krw_coin47)
# 거래량 동반한 MACD 조회.
macd47 = get_acc_macd(krw_coin47)
# 5, 20일 이평선 조회.
#macd47 = get_ma20(krw_coin47)
# 거래량 동반한 5, 20일 이평선 조회.
#macd47 = get_acc_ma20(krw_coin47)

# 코인 보유 유무
if macd47 >= 0:
    # 다음 코인 매매 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
    op_mode47 = 1

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd47}  |  매수가능 - {op_mode47} - 매수불가-매도가능")
    print("")
else:
    # 다음 코인 매매 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
    op_mode47 = 3

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd47}  |  매수가능 - {op_mode47} - 매수가능-매도불가")
    print("")

# 1초 딜레이.
time.sleep(1)
###############################


###############################
# 코인48

# 보유수량 불러오기
krw_balance48 = upbit.get_balance(krw_coin48)
# 코인 현재가 불러오기
price48 = pyupbit.get_current_price(krw_coin48)
# 보유코인 원화금액으로 계산하기
bp48 = price48 * krw_balance48
# 코인 보유 현황 출력.
print(f"48. 코인명 : {coin48}  |  현재가 = ￦{price48}  |  보유수량 = {krw_balance48}  |  평가금액 = ￦{bp48}")

# MACD 조회.
#macd48 = get_macd(krw_coin48)
# 거래량 동반한 MACD 조회.
macd48 = get_acc_macd(krw_coin48)
# 5, 20일 이평선 조회.
#macd48 = get_ma20(krw_coin48)
# 거래량 동반한 5, 20일 이평선 조회.
#macd48 = get_acc_ma20(krw_coin48)

# 코인 보유 유무
if macd48 >= 0:
    # 다음 코인 매매 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
    op_mode48 = 1

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd48}  |  매수가능 - {op_mode48} - 매수불가-매도가능")
    print("")
else:
    # 다음 코인 매매 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
    op_mode48 = 3

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd48}  |  매수가능 - {op_mode48} - 매수가능-매도불가")
    print("")

# 1초 딜레이.
time.sleep(1)
###############################


###############################
# 코인49

# 보유수량 불러오기
krw_balance49 = upbit.get_balance(krw_coin49)
# 코인 현재가 불러오기
price49 = pyupbit.get_current_price(krw_coin49)
# 보유코인 원화금액으로 계산하기
bp49 = price49 * krw_balance49
# 코인 보유 현황 출력.
print(f"49. 코인명 : {coin49}  |  현재가 = ￦{price49}  |  보유수량 = {krw_balance49}  |  평가금액 = ￦{bp49}")

# MACD 조회.
#macd49 = get_macd(krw_coin49)
# 거래량 동반한 MACD 조회.
macd49 = get_acc_macd(krw_coin49)
# 5, 20일 이평선 조회.
#macd49 = get_ma20(krw_coin49)
# 거래량 동반한 5, 20일 이평선 조회.
#macd49 = get_acc_ma20(krw_coin49)

# 코인 보유 유무
if macd49 >= 0:
    # 다음 코인 매매 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
    op_mode49 = 1

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd49}  |  매수가능 - {op_mode49} - 매수불가-매도가능")
    print("")
else:
    # 다음 코인 매매 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
    op_mode49 = 3

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd49}  |  매수가능 - {op_mode49} - 매수가능-매도불가")
    print("")

# 1초 딜레이.
time.sleep(1)
###############################


###############################
# 코인50

# 보유수량 불러오기
krw_balance50 = upbit.get_balance(krw_coin50)
# 코인 현재가 불러오기
price50 = pyupbit.get_current_price(krw_coin50)
# 보유코인 원화금액으로 계산하기
bp50 = price50 * krw_balance50
# 코인 보유 현황 출력.
print(f"50. 코인명 : {coin50}  |  현재가 = ￦{price50}  |  보유수량 = {krw_balance50}  |  평가금액 = ￦{bp50}")

# MACD 조회.
#macd50 = get_macd(krw_coin50)
# 거래량 동반한 MACD 조회.
macd50 = get_acc_macd(krw_coin50)
# 5, 20일 이평선 조회.
#macd50 = get_ma20(krw_coin50)
# 거래량 동반한 5, 20일 이평선 조회.
#macd50 = get_acc_ma20(krw_coin50)

# 코인 보유 유무
if macd50 >= 0:
    # 다음 코인 매매 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
    op_mode50 = 1

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd50}  |  매수가능 - {op_mode50} - 매수불가-매도가능")
    print("")
else:
    # 다음 코인 매매 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
    op_mode50 = 3

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd50}  |  매수가능 - {op_mode50} - 매수가능-매도불가")
    print("")

# 1초 딜레이.
time.sleep(1)
###############################





######################################################################################################################################################
######################################################################################################################################################
######################################################################################################################################################




###############################
# 코인51

# 보유수량 불러오기
krw_balance51 = upbit.get_balance(krw_coin51)
# 코인 현재가 불러오기
price51 = pyupbit.get_current_price(krw_coin51)
# 보유코인 원화금액으로 계산하기
bp51 = price51 * krw_balance51
# 코인 보유 현황 출력.
print(f"51. 코인명 : {coin51}  |  현재가 = ￦{price51}  |  보유수량 = {krw_balance51}  |  평가금액 = ￦{bp51}")

# MACD 조회.
#macd51 = get_macd(krw_coin51)
# 거래량 동반한 MACD 조회.
macd51 = get_acc_macd(krw_coin51)
# 5, 20일 이평선 조회.
#macd51 = get_ma20(krw_coin51)
# 거래량 동반한 5, 20일 이평선 조회.
#macd51 = get_acc_ma20(krw_coin51)

# 코인 보유 유무
if macd51 >= 0:
    # 다음 코인 매매 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
    op_mode51 = 1

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd51}  |  매수가능 - {op_mode51} - 매수불가-매도가능")
    print("")
else:
    # 다음 코인 매매 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
    op_mode51 = 3

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd51}  |  매수가능 - {op_mode51} - 매수가능-매도불가")
    print("")

# 1초 딜레이.
time.sleep(1)
###############################


###############################
# 코인52

# 보유수량 불러오기
krw_balance52 = upbit.get_balance(krw_coin52)
# 코인 현재가 불러오기
price52 = pyupbit.get_current_price(krw_coin52)
# 보유코인 원화금액으로 계산하기
bp52 = price52 * krw_balance52
# 코인 보유 현황 출력.
print(f"52. 코인명 : {coin52}  |  현재가 = ￦{price52}  |  보유수량 = {krw_balance52}  |  평가금액 = ￦{bp52}")

# MACD 조회.
#macd52 = get_macd(krw_coin52)
# 거래량 동반한 MACD 조회.
macd52 = get_acc_macd(krw_coin52)
# 5, 20일 이평선 조회.
#macd52 = get_ma20(krw_coin52)
# 거래량 동반한 5, 20일 이평선 조회.
#macd52 = get_acc_ma20(krw_coin52)

# 코인 보유 유무
if macd52 >= 0:
    # 다음 코인 매매 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
    op_mode52 = 1

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd52}  |  매수가능 - {op_mode52} - 매수불가-매도가능")
    print("")
else:
    # 다음 코인 매매 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
    op_mode52 = 3

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd52}  |  매수가능 - {op_mode52} - 매수가능-매도불가")
    print("")

# 1초 딜레이.
time.sleep(1)
###############################


###############################
# 코인53

# 보유수량 불러오기
krw_balance53 = upbit.get_balance(krw_coin53)
# 코인 현재가 불러오기
price53 = pyupbit.get_current_price(krw_coin53)
# 보유코인 원화금액으로 계산하기
bp53 = price53 * krw_balance53
# 코인 보유 현황 출력.
print(f"53. 코인명 : {coin53}  |  현재가 = ￦{price53}  |  보유수량 = {krw_balance53}  |  평가금액 = ￦{bp53}")

# MACD 조회.
#macd53 = get_macd(krw_coin53)
# 거래량 동반한 MACD 조회.
macd53 = get_acc_macd(krw_coin53)
# 5, 20일 이평선 조회.
#macd53 = get_ma20(krw_coin53)
# 거래량 동반한 5, 20일 이평선 조회.
#macd53 = get_acc_ma20(krw_coin53)

# 코인 보유 유무
if macd53 >= 0:
    # 다음 코인 매매 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
    op_mode53 = 1

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd53}  |  매수가능 - {op_mode53} - 매수불가-매도가능")
    print("")
else:
    # 다음 코인 매매 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
    op_mode53 = 3

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd53}  |  매수가능 - {op_mode53} - 매수가능-매도불가")
    print("")

# 1초 딜레이.
time.sleep(1)
###############################


###############################
# 코인54

# 보유수량 불러오기
krw_balance54 = upbit.get_balance(krw_coin54)
# 코인 현재가 불러오기
price54 = pyupbit.get_current_price(krw_coin54)
# 보유코인 원화금액으로 계산하기
bp54 = price54 * krw_balance54
# 코인 보유 현황 출력.
print(f"54. 코인명 : {coin54}  |  현재가 = ￦{price54}  |  보유수량 = {krw_balance54}  |  평가금액 = ￦{bp54}")

# MACD 조회.
#macd54 = get_macd(krw_coin54)
# 거래량 동반한 MACD 조회.
macd54 = get_acc_macd(krw_coin54)
# 5, 20일 이평선 조회.
#macd54 = get_ma20(krw_coin54)
# 거래량 동반한 5, 20일 이평선 조회.
#macd54 = get_acc_ma20(krw_coin54)

# 코인 보유 유무
if macd54 >= 0:
    # 다음 코인 매매 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
    op_mode54 = 1

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd54}  |  매수가능 - {op_mode54} - 매수불가-매도가능")
    print("")
else:
    # 다음 코인 매매 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
    op_mode54 = 3

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd54}  |  매수가능 - {op_mode54} - 매수가능-매도불가")
    print("")

# 1초 딜레이.
time.sleep(1)
###############################


###############################
# 코인55

# 보유수량 불러오기
krw_balance55 = upbit.get_balance(krw_coin55)
# 코인 현재가 불러오기
price55 = pyupbit.get_current_price(krw_coin55)
# 보유코인 원화금액으로 계산하기
bp55 = price55 * krw_balance55
# 코인 보유 현황 출력.
print(f"55. 코인명 : {coin55}  |  현재가 = ￦{price55}  |  보유수량 = {krw_balance55}  |  평가금액 = ￦{bp55}")

# MACD 조회.
#macd55 = get_macd(krw_coin55)
# 거래량 동반한 MACD 조회.
macd55 = get_acc_macd(krw_coin55)
# 5, 20일 이평선 조회.
#macd55 = get_ma20(krw_coin55)
# 거래량 동반한 5, 20일 이평선 조회.
#macd55 = get_acc_ma20(krw_coin55)

# 코인 보유 유무
if macd55 >= 0:
    # 다음 코인 매매 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
    op_mode55 = 1

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd55}  |  매수가능 - {op_mode55} - 매수불가-매도가능")
    print("")
else:
    # 다음 코인 매매 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
    op_mode55 = 3

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd55}  |  매수가능 - {op_mode55} - 매수가능-매도불가")
    print("")

# 1초 딜레이.
time.sleep(1)
###############################


###############################
# 코인56

# 보유수량 불러오기
krw_balance56 = upbit.get_balance(krw_coin56)
# 코인 현재가 불러오기
price56 = pyupbit.get_current_price(krw_coin56)
# 보유코인 원화금액으로 계산하기
bp56 = price56 * krw_balance56
# 코인 보유 현황 출력.
print(f"56. 코인명 : {coin56}  |  현재가 = ￦{price56}  |  보유수량 = {krw_balance56}  |  평가금액 = ￦{bp56}")

# MACD 조회.
#macd56 = get_macd(krw_coin56)
# 거래량 동반한 MACD 조회.
macd56 = get_acc_macd(krw_coin56)
# 5, 20일 이평선 조회.
#macd56 = get_ma20(krw_coin56)
# 거래량 동반한 5, 20일 이평선 조회.
#macd56 = get_acc_ma20(krw_coin56)

# 코인 보유 유무
if macd56 >= 0:
    # 다음 코인 매매 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
    op_mode56 = 1

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd56}  |  매수가능 - {op_mode56} - 매수불가-매도가능")
    print("")
else:
    # 다음 코인 매매 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
    op_mode56 = 3

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd56}  |  매수가능 - {op_mode56} - 매수가능-매도불가")
    print("")

# 1초 딜레이.
time.sleep(1)
###############################


###############################
# 코인57

# 보유수량 불러오기
krw_balance57 = upbit.get_balance(krw_coin57)
# 코인 현재가 불러오기
price57 = pyupbit.get_current_price(krw_coin57)
# 보유코인 원화금액으로 계산하기
bp57 = price57 * krw_balance57
# 코인 보유 현황 출력.
print(f"57. 코인명 : {coin57}  |  현재가 = ￦{price57}  |  보유수량 = {krw_balance57}  |  평가금액 = ￦{bp57}")

# MACD 조회.
#macd57 = get_macd(krw_coin57)
# 거래량 동반한 MACD 조회.
macd57 = get_acc_macd(krw_coin57)
# 5, 20일 이평선 조회.
#macd57 = get_ma20(krw_coin57)
# 거래량 동반한 5, 20일 이평선 조회.
#macd57 = get_acc_ma20(krw_coin57)

# 코인 보유 유무
if macd57 >= 0:
    # 다음 코인 매매 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
    op_mode57 = 1

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd57}  |  매수가능 - {op_mode57} - 매수불가-매도가능")
    print("")
else:
    # 다음 코인 매매 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
    op_mode57 = 3

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd57}  |  매수가능 - {op_mode57} - 매수가능-매도불가")
    print("")

# 1초 딜레이.
time.sleep(1)
###############################


###############################
# 코인58

# 보유수량 불러오기
krw_balance58 = upbit.get_balance(krw_coin58)
# 코인 현재가 불러오기
price58 = pyupbit.get_current_price(krw_coin58)
# 보유코인 원화금액으로 계산하기
bp58 = price58 * krw_balance58
# 코인 보유 현황 출력.
print(f"58. 코인명 : {coin58}  |  현재가 = ￦{price58}  |  보유수량 = {krw_balance58}  |  평가금액 = ￦{bp58}")

# MACD 조회.
#macd58 = get_macd(krw_coin58)
# 거래량 동반한 MACD 조회.
macd58 = get_acc_macd(krw_coin58)
# 5, 20일 이평선 조회.
#macd58 = get_ma20(krw_coin58)
# 거래량 동반한 5, 20일 이평선 조회.
#macd58 = get_acc_ma20(krw_coin58)

# 코인 보유 유무
if macd58 >= 0:
    # 다음 코인 매매 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
    op_mode58 = 1

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd58}  |  매수가능 - {op_mode58} - 매수불가-매도가능")
    print("")
else:
    # 다음 코인 매매 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
    op_mode58 = 3

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd58}  |  매수가능 - {op_mode58} - 매수가능-매도불가")
    print("")

# 1초 딜레이.
time.sleep(1)
###############################


###############################
# 코인59

# 보유수량 불러오기
krw_balance59 = upbit.get_balance(krw_coin59)
# 코인 현재가 불러오기
price59 = pyupbit.get_current_price(krw_coin59)
# 보유코인 원화금액으로 계산하기
bp59 = price59 * krw_balance59
# 코인 보유 현황 출력.
print(f"59. 코인명 : {coin59}  |  현재가 = ￦{price59}  |  보유수량 = {krw_balance59}  |  평가금액 = ￦{bp59}")

# MACD 조회.
#macd59 = get_macd(krw_coin59)
# 거래량 동반한 MACD 조회.
macd59 = get_acc_macd(krw_coin59)
# 5, 20일 이평선 조회.
#macd59 = get_ma20(krw_coin59)
# 거래량 동반한 5, 20일 이평선 조회.
#macd59 = get_acc_ma20(krw_coin59)

# 코인 보유 유무
if macd59 >= 0:
    # 다음 코인 매매 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
    op_mode59 = 1

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd59}  |  매수가능 - {op_mode59} - 매수불가-매도가능")
    print("")
else:
    # 다음 코인 매매 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
    op_mode59 = 3

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd59}  |  매수가능 - {op_mode59} - 매수가능-매도불가")
    print("")

# 1초 딜레이.
time.sleep(1)
###############################


###############################
# 코인60

# 보유수량 불러오기
krw_balance60 = upbit.get_balance(krw_coin60)
# 코인 현재가 불러오기
price60 = pyupbit.get_current_price(krw_coin60)
# 보유코인 원화금액으로 계산하기
bp60 = price60 * krw_balance60
# 코인 보유 현황 출력.
print(f"60. 코인명 : {coin60}  |  현재가 = ￦{price60}  |  보유수량 = {krw_balance60}  |  평가금액 = ￦{bp60}")

# MACD 조회.
#macd60 = get_macd(krw_coin60)
# 거래량 동반한 MACD 조회.
macd60 = get_acc_macd(krw_coin60)
# 5, 20일 이평선 조회.
#macd60 = get_ma20(krw_coin60)
# 거래량 동반한 5, 20일 이평선 조회.
#macd60 = get_acc_ma20(krw_coin60)

# 코인 보유 유무
if macd60 >= 0:
    # 다음 코인 매매 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
    op_mode60 = 1

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd60}  |  매수가능 - {op_mode60} - 매수불가-매도가능")
    print("")
else:
    # 다음 코인 매매 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
    op_mode60 = 3

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd60}  |  매수가능 - {op_mode60} - 매수가능-매도불가")
    print("")

# 1초 딜레이.
time.sleep(1)
###############################


######################################################################################################################################################
######################################################################################################################################################
######################################################################################################################################################


###############################
# 코인61

# 보유수량 불러오기
krw_balance61 = upbit.get_balance(krw_coin61)
# 코인 현재가 불러오기
price61 = pyupbit.get_current_price(krw_coin61)
# 보유코인 원화금액으로 계산하기
bp61 = price61 * krw_balance61
# 코인 보유 현황 출력.
print(f"61. 코인명 : {coin61}  |  현재가 = ￦{price61}  |  보유수량 = {krw_balance61}  |  평가금액 = ￦{bp61}")

# MACD 조회.
#macd61 = get_macd(krw_coin61)
# 거래량 동반한 MACD 조회.
macd61 = get_acc_macd(krw_coin61)
# 5, 20일 이평선 조회.
#macd61 = get_ma20(krw_coin61)
# 거래량 동반한 5, 20일 이평선 조회.
#macd61 = get_acc_ma20(krw_coin61)

# 코인 보유 유무
if macd61 >= 0:
    # 다음 코인 매매 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
    op_mode61 = 1

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd61}  |  매수가능 - {op_mode61} - 매수불가-매도가능")
    print("")
else:
    # 다음 코인 매매 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
    op_mode61 = 3

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd61}  |  매수가능 - {op_mode61} - 매수가능-매도불가")
    print("")

# 1초 딜레이.
time.sleep(1)
###############################


###############################
# 코인62

# 보유수량 불러오기
krw_balance62 = upbit.get_balance(krw_coin62)
# 코인 현재가 불러오기
price62 = pyupbit.get_current_price(krw_coin62)
# 보유코인 원화금액으로 계산하기
bp62 = price62 * krw_balance62
# 코인 보유 현황 출력.
print(f"62. 코인명 : {coin62}  |  현재가 = ￦{price62}  |  보유수량 = {krw_balance62}  |  평가금액 = ￦{bp62}")

# MACD 조회.
#macd62 = get_macd(krw_coin62)
# 거래량 동반한 MACD 조회.
macd62 = get_acc_macd(krw_coin62)
# 5, 20일 이평선 조회.
#macd62 = get_ma20(krw_coin62)
# 거래량 동반한 5, 20일 이평선 조회.
#macd62 = get_acc_ma20(krw_coin62)

# 코인 보유 유무
if macd62 >= 0:
    # 다음 코인 매매 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
    op_mode62 = 1

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd62}  |  매수가능 - {op_mode62} - 매수불가-매도가능")
    print("")
else:
    # 다음 코인 매매 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
    op_mode62 = 3

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd62}  |  매수가능 - {op_mode62} - 매수가능-매도불가")
    print("")

# 1초 딜레이.
time.sleep(1)
###############################


###############################
# 코인63

# 보유수량 불러오기
krw_balance63 = upbit.get_balance(krw_coin63)
# 코인 현재가 불러오기
price63 = pyupbit.get_current_price(krw_coin63)
# 보유코인 원화금액으로 계산하기
bp63 = price63 * krw_balance63
# 코인 보유 현황 출력.
print(f"63. 코인명 : {coin63}  |  현재가 = ￦{price63}  |  보유수량 = {krw_balance63}  |  평가금액 = ￦{bp63}")

# MACD 조회.
#macd63 = get_macd(krw_coin63)
# 거래량 동반한 MACD 조회.
macd63 = get_acc_macd(krw_coin63)
# 5, 20일 이평선 조회.
#macd63 = get_ma20(krw_coin63)
# 거래량 동반한 5, 20일 이평선 조회.
#macd63 = get_acc_ma20(krw_coin63)

# 코인 보유 유무
if macd63 >= 0:
    # 다음 코인 매매 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
    op_mode63 = 1

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd63}  |  매수가능 - {op_mode63} - 매수불가-매도가능")
    print("")
else:
    # 다음 코인 매매 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
    op_mode63 = 3

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd63}  |  매수가능 - {op_mode63} - 매수가능-매도불가")
    print("")

# 1초 딜레이.
time.sleep(1)
###############################


###############################
# 코인64

# 보유수량 불러오기
krw_balance64 = upbit.get_balance(krw_coin64)
# 코인 현재가 불러오기
price64 = pyupbit.get_current_price(krw_coin64)
# 보유코인 원화금액으로 계산하기
bp64 = price64 * krw_balance64
# 코인 보유 현황 출력.
print(f"64. 코인명 : {coin64}  |  현재가 = ￦{price64}  |  보유수량 = {krw_balance64}  |  평가금액 = ￦{bp64}")

# MACD 조회.
#macd64 = get_macd(krw_coin64)
# 거래량 동반한 MACD 조회.
macd64 = get_acc_macd(krw_coin64)
# 5, 20일 이평선 조회.
#macd64 = get_ma20(krw_coin64)
# 거래량 동반한 5, 20일 이평선 조회.
#macd64 = get_acc_ma20(krw_coin64)

# 코인 보유 유무
if macd64 >= 0:
    # 다음 코인 매매 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
    op_mode64 = 1

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd64}  |  매수가능 - {op_mode64} - 매수불가-매도가능")
    print("")
else:
    # 다음 코인 매매 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
    op_mode64 = 3

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd64}  |  매수가능 - {op_mode64} - 매수가능-매도불가")
    print("")

# 1초 딜레이.
time.sleep(1)
###############################


###############################
# 코인65

# 보유수량 불러오기
krw_balance65 = upbit.get_balance(krw_coin65)
# 코인 현재가 불러오기
price65 = pyupbit.get_current_price(krw_coin65)
# 보유코인 원화금액으로 계산하기
bp65 = price65 * krw_balance65
# 코인 보유 현황 출력.
print(f"65. 코인명 : {coin65}  |  현재가 = ￦{price65}  |  보유수량 = {krw_balance65}  |  평가금액 = ￦{bp65}")

# MACD 조회.
#macd65 = get_macd(krw_coin65)
# 거래량 동반한 MACD 조회.
macd65 = get_acc_macd(krw_coin65)
# 5, 20일 이평선 조회.
#macd65 = get_ma20(krw_coin65)
# 거래량 동반한 5, 20일 이평선 조회.
#macd65 = get_acc_ma20(krw_coin65)

# 코인 보유 유무
if macd65 >= 0:
    # 다음 코인 매매 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
    op_mode65 = 1

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd65}  |  매수가능 - {op_mode65} - 매수불가-매도가능")
    print("")
else:
    # 다음 코인 매매 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
    op_mode65 = 3

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd65}  |  매수가능 - {op_mode65} - 매수가능-매도불가")
    print("")

# 1초 딜레이.
time.sleep(1)
###############################


###############################
# 코인66

# 보유수량 불러오기
krw_balance66 = upbit.get_balance(krw_coin66)
# 코인 현재가 불러오기
price66 = pyupbit.get_current_price(krw_coin66)
# 보유코인 원화금액으로 계산하기
bp66 = price66 * krw_balance66
# 코인 보유 현황 출력.
print(f"66. 코인명 : {coin66}  |  현재가 = ￦{price66}  |  보유수량 = {krw_balance66}  |  평가금액 = ￦{bp66}")

# MACD 조회.
#macd66 = get_macd(krw_coin66)
# 거래량 동반한 MACD 조회.
macd66 = get_acc_macd(krw_coin66)
# 5, 20일 이평선 조회.
#macd66 = get_ma20(krw_coin66)
# 거래량 동반한 5, 20일 이평선 조회.
#macd66 = get_acc_ma20(krw_coin66)

# 코인 보유 유무
if macd66 >= 0:
    # 다음 코인 매매 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
    op_mode66 = 1

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd66}  |  매수가능 - {op_mode66} - 매수불가-매도가능")
    print("")
else:
    # 다음 코인 매매 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
    op_mode66 = 3

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd66}  |  매수가능 - {op_mode66} - 매수가능-매도불가")
    print("")

# 1초 딜레이.
time.sleep(1)
###############################


###############################
# 코인67

# 보유수량 불러오기
krw_balance67 = upbit.get_balance(krw_coin67)
# 코인 현재가 불러오기
price67 = pyupbit.get_current_price(krw_coin67)
# 보유코인 원화금액으로 계산하기
bp67 = price67 * krw_balance67
# 코인 보유 현황 출력.
print(f"67. 코인명 : {coin67}  |  현재가 = ￦{price67}  |  보유수량 = {krw_balance67}  |  평가금액 = ￦{bp67}")

# MACD 조회.
#macd67 = get_macd(krw_coin67)
# 거래량 동반한 MACD 조회.
macd67 = get_acc_macd(krw_coin67)
# 5, 20일 이평선 조회.
#macd67 = get_ma20(krw_coin67)
# 거래량 동반한 5, 20일 이평선 조회.
#macd67 = get_acc_ma20(krw_coin67)

# 코인 보유 유무
if macd67 >= 0:
    # 다음 코인 매매 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
    op_mode67 = 1

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd67}  |  매수가능 - {op_mode67} - 매수불가-매도가능")
    print("")
else:
    # 다음 코인 매매 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
    op_mode67 = 3

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd67}  |  매수가능 - {op_mode67} - 매수가능-매도불가")
    print("")

# 1초 딜레이.
time.sleep(1)
###############################


###############################
# 코인68

# 보유수량 불러오기
krw_balance68 = upbit.get_balance(krw_coin68)
# 코인 현재가 불러오기
price68 = pyupbit.get_current_price(krw_coin68)
# 보유코인 원화금액으로 계산하기
bp68 = price68 * krw_balance68
# 코인 보유 현황 출력.
print(f"68. 코인명 : {coin68}  |  현재가 = ￦{price68}  |  보유수량 = {krw_balance68}  |  평가금액 = ￦{bp68}")

# MACD 조회.
#macd68 = get_macd(krw_coin68)
# 거래량 동반한 MACD 조회.
macd68 = get_acc_macd(krw_coin68)
# 5, 20일 이평선 조회.
#macd68 = get_ma20(krw_coin68)
# 거래량 동반한 5, 20일 이평선 조회.
#macd68 = get_acc_ma20(krw_coin68)

# 코인 보유 유무
if macd68 >= 0:
    # 다음 코인 매매 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
    op_mode68 = 1

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd68}  |  매수가능 - {op_mode68} - 매수불가-매도가능")
    print("")
else:
    # 다음 코인 매매 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
    op_mode68 = 3

    # 보유 및 매수 가능 출력.
    print(f"MACD = {macd68}  |  매수가능 - {op_mode68} - 매수가능-매도불가")
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


            ###############################
            # 코인11

            # 보유수량 불러오기
            krw_balance11 = upbit.get_balance(krw_coin11)
            # 코인 현재가 불러오기
            price11 = pyupbit.get_current_price(krw_coin11)
            # 보유코인 원화금액으로 계산하기
            bp11 = price11 * krw_balance11

            # MACD 조회.
            #macd11 = get_macd(krw_coin11)
            # 거래량 동반한 MACD 조회.
            macd11 = get_acc_macd(krw_coin11)
            # 5, 20일 이평선 조회.
            #macd11 = get_ma20(krw_coin11)
            # 거래량 동반한 5, 20일 이평선 조회.
            #macd11 = get_acc_ma20(krw_coin11)

            # 1초 딜레이.
            time.sleep(1)
            ###############################


            ###############################
            # 코인12

            # 보유수량 불러오기
            krw_balance12 = upbit.get_balance(krw_coin12)
            # 코인 현재가 불러오기
            price12 = pyupbit.get_current_price(krw_coin12)
            # 보유코인 원화금액으로 계산하기
            bp12 = price12 * krw_balance12

            # MACD 조회.
            #macd12 = get_macd(krw_coin12)
            # 거래량 동반한 MACD 조회.
            macd12 = get_acc_macd(krw_coin12)
            # 5, 20일 이평선 조회.
            #macd12 = get_ma20(krw_coin12)
            # 거래량 동반한 5, 20일 이평선 조회.
            #macd12 = get_acc_ma20(krw_coin12)

            # 1초 딜레이.
            time.sleep(1)
            ###############################


            ###############################
            # 코인13

            # 보유수량 불러오기
            krw_balance13 = upbit.get_balance(krw_coin13)
            # 코인 현재가 불러오기
            price13 = pyupbit.get_current_price(krw_coin13)
            # 보유코인 원화금액으로 계산하기
            bp13 = price13 * krw_balance13

            # MACD 조회.
            #macd13 = get_macd(krw_coin13)
            # 거래량 동반한 MACD 조회.
            macd13 = get_acc_macd(krw_coin13)
            # 5, 20일 이평선 조회.
            #macd13 = get_ma20(krw_coin13)
            # 거래량 동반한 5, 20일 이평선 조회.
            #macd13 = get_acc_ma20(krw_coin13)

            # 1초 딜레이.
            time.sleep(1)
            ###############################


            ###############################
            # 코인14

            # 보유수량 불러오기
            krw_balance14 = upbit.get_balance(krw_coin14)
            # 코인 현재가 불러오기
            price14 = pyupbit.get_current_price(krw_coin14)
            # 보유코인 원화금액으로 계산하기
            bp14 = price14 * krw_balance14

            # MACD 조회.
            #macd14 = get_macd(krw_coin14)
            # 거래량 동반한 MACD 조회.
            macd14 = get_acc_macd(krw_coin14)
            # 5, 20일 이평선 조회.
            #macd14 = get_ma20(krw_coin14)
            # 거래량 동반한 5, 20일 이평선 조회.
            #macd14 = get_acc_ma20(krw_coin14)

            # 1초 딜레이.
            time.sleep(1)
            ###############################


            ###############################
            # 코인15

            # 보유수량 불러오기
            krw_balance15 = upbit.get_balance(krw_coin15)
            # 코인 현재가 불러오기
            price15 = pyupbit.get_current_price(krw_coin15)
            # 보유코인 원화금액으로 계산하기
            bp15 = price15 * krw_balance15

            # MACD 조회.
            #macd15 = get_macd(krw_coin15)
            # 거래량 동반한 MACD 조회.
            macd15 = get_acc_macd(krw_coin15)
            # 5, 20일 이평선 조회.
            #macd15 = get_ma20(krw_coin15)
            # 거래량 동반한 5, 20일 이평선 조회.
            #macd15 = get_acc_ma20(krw_coin15)

            # 1초 딜레이.
            time.sleep(1)
            ###############################


            ###############################
            # 코인16

            # 보유수량 불러오기
            krw_balance16 = upbit.get_balance(krw_coin16)
            # 코인 현재가 불러오기
            price16 = pyupbit.get_current_price(krw_coin16)
            # 보유코인 원화금액으로 계산하기
            bp16 = price16 * krw_balance16

            # MACD 조회.
            #macd16 = get_macd(krw_coin16)
            # 거래량 동반한 MACD 조회.
            macd16 = get_acc_macd(krw_coin16)
            # 5, 20일 이평선 조회.
            #macd16 = get_ma20(krw_coin16)
            # 거래량 동반한 5, 20일 이평선 조회.
            #macd16 = get_acc_ma20(krw_coin16)

            # 1초 딜레이.
            time.sleep(1)
            ###############################


            ###############################
            # 코인17

            # 보유수량 불러오기
            krw_balance17 = upbit.get_balance(krw_coin17)
            # 코인 현재가 불러오기
            price17 = pyupbit.get_current_price(krw_coin17)
            # 보유코인 원화금액으로 계산하기
            bp17 = price17 * krw_balance17

            # MACD 조회.
            #macd17 = get_macd(krw_coin17)
            # 거래량 동반한 MACD 조회.
            macd17 = get_acc_macd(krw_coin17)
            # 5, 20일 이평선 조회.
            #macd17 = get_ma20(krw_coin17)
            # 거래량 동반한 5, 20일 이평선 조회.
            #macd17 = get_acc_ma20(krw_coin17)

            # 1초 딜레이.
            time.sleep(1)
            ###############################


            ###############################
            # 코인18

            # 보유수량 불러오기
            krw_balance18 = upbit.get_balance(krw_coin18)
            # 코인 현재가 불러오기
            price18 = pyupbit.get_current_price(krw_coin18)
            # 보유코인 원화금액으로 계산하기
            bp18 = price18 * krw_balance18

            # MACD 조회.
            #macd18 = get_macd(krw_coin18)
            # 거래량 동반한 MACD 조회.
            macd18 = get_acc_macd(krw_coin18)
            # 5, 20일 이평선 조회.
            #macd18 = get_ma20(krw_coin18)
            # 거래량 동반한 5, 20일 이평선 조회.
            #macd18 = get_acc_ma20(krw_coin18)

            # 1초 딜레이.
            time.sleep(1)
            ###############################


            ###############################
            # 코인19

            # 보유수량 불러오기
            krw_balance19 = upbit.get_balance(krw_coin19)
            # 코인 현재가 불러오기
            price19 = pyupbit.get_current_price(krw_coin19)
            # 보유코인 원화금액으로 계산하기
            bp19 = price19 * krw_balance19

            # MACD 조회.
            #macd19 = get_macd(krw_coin19)
            # 거래량 동반한 MACD 조회.
            macd19 = get_acc_macd(krw_coin19)
            # 5, 20일 이평선 조회.
            #macd19 = get_ma20(krw_coin19)
            # 거래량 동반한 5, 20일 이평선 조회.
            #macd19 = get_acc_ma20(krw_coin19)

            # 1초 딜레이.
            time.sleep(1)
            ###############################


            ###############################
            # 코인20

            # 보유수량 불러오기
            krw_balance20 = upbit.get_balance(krw_coin20)
            # 코인 현재가 불러오기
            price20 = pyupbit.get_current_price(krw_coin20)
            # 보유코인 원화금액으로 계산하기
            bp20 = price20 * krw_balance20

            # MACD 조회.
            #macd20 = get_macd(krw_coin20)
            # 거래량 동반한 MACD 조회.
            macd20 = get_acc_macd(krw_coin20)
            # 5, 20일 이평선 조회.
            #macd20 = get_ma20(krw_coin20)
            # 거래량 동반한 5, 20일 이평선 조회.
            #macd20 = get_acc_ma20(krw_coin20)

            # 1초 딜레이.
            time.sleep(1)
            ###############################


            ######################################################################################################################################################


            ###############################
            # 코인21

            # 보유수량 불러오기
            krw_balance21 = upbit.get_balance(krw_coin21)
            # 코인 현재가 불러오기
            price21 = pyupbit.get_current_price(krw_coin21)
            # 보유코인 원화금액으로 계산하기
            bp21 = price21 * krw_balance21

            # MACD 조회.
            #macd21 = get_macd(krw_coin21)
            # 거래량 동반한 MACD 조회.
            macd21 = get_acc_macd(krw_coin21)
            # 5, 20일 이평선 조회.
            #macd21 = get_ma20(krw_coin21)
            # 거래량 동반한 5, 20일 이평선 조회.
            #macd21 = get_acc_ma20(krw_coin21)

            # 1초 딜레이.
            time.sleep(1)
            ###############################


            ###############################
            # 코인22

            # 보유수량 불러오기
            krw_balance22 = upbit.get_balance(krw_coin22)
            # 코인 현재가 불러오기
            price22 = pyupbit.get_current_price(krw_coin22)
            # 보유코인 원화금액으로 계산하기
            bp22 = price22 * krw_balance22

            # MACD 조회.
            #macd22 = get_macd(krw_coin22)
            # 거래량 동반한 MACD 조회.
            macd22 = get_acc_macd(krw_coin22)
            # 5, 20일 이평선 조회.
            #macd22 = get_ma20(krw_coin22)
            # 거래량 동반한 5, 20일 이평선 조회.
            #macd22 = get_acc_ma20(krw_coin22)

            # 1초 딜레이.
            time.sleep(1)
            ###############################


            ###############################
            # 코인23

            # 보유수량 불러오기
            krw_balance23 = upbit.get_balance(krw_coin23)
            # 코인 현재가 불러오기
            price23 = pyupbit.get_current_price(krw_coin23)
            # 보유코인 원화금액으로 계산하기
            bp23 = price23 * krw_balance23

            # MACD 조회.
            #macd23 = get_macd(krw_coin23)
            # 거래량 동반한 MACD 조회.
            macd23 = get_acc_macd(krw_coin23)
            # 5, 20일 이평선 조회.
            #macd23 = get_ma20(krw_coin23)
            # 거래량 동반한 5, 20일 이평선 조회.
            #macd23 = get_acc_ma20(krw_coin23)

            # 1초 딜레이.
            time.sleep(1)
            ###############################


            ###############################
            # 코인24

            # 보유수량 불러오기
            krw_balance24 = upbit.get_balance(krw_coin24)
            # 코인 현재가 불러오기
            price24 = pyupbit.get_current_price(krw_coin24)
            # 보유코인 원화금액으로 계산하기
            bp24 = price24 * krw_balance24

            # MACD 조회.
            #macd24 = get_macd(krw_coin24)
            # 거래량 동반한 MACD 조회.
            macd24 = get_acc_macd(krw_coin24)
            # 5, 20일 이평선 조회.
            #macd24 = get_ma20(krw_coin24)
            # 거래량 동반한 5, 20일 이평선 조회.
            #macd24 = get_acc_ma20(krw_coin24)

            # 1초 딜레이.
            time.sleep(1)
            ###############################


            ###############################
            # 코인25

            # 보유수량 불러오기
            krw_balance25 = upbit.get_balance(krw_coin25)
            # 코인 현재가 불러오기
            price25 = pyupbit.get_current_price(krw_coin25)
            # 보유코인 원화금액으로 계산하기
            bp25 = price25 * krw_balance25

            # MACD 조회.
            #macd25 = get_macd(krw_coin25)
            # 거래량 동반한 MACD 조회.
            macd25 = get_acc_macd(krw_coin25)
            # 5, 20일 이평선 조회.
            #macd25 = get_ma20(krw_coin25)
            # 거래량 동반한 5, 20일 이평선 조회.
            #macd25 = get_acc_ma20(krw_coin25)

            # 1초 딜레이.
            time.sleep(1)
            ###############################


            ###############################
            # 코인26

            # 보유수량 불러오기
            krw_balance26 = upbit.get_balance(krw_coin26)
            # 코인 현재가 불러오기
            price26 = pyupbit.get_current_price(krw_coin26)
            # 보유코인 원화금액으로 계산하기
            bp26 = price26 * krw_balance26

            # MACD 조회.
            #macd26 = get_macd(krw_coin26)
            # 거래량 동반한 MACD 조회.
            macd26 = get_acc_macd(krw_coin26)
            # 5, 20일 이평선 조회.
            #macd26 = get_ma20(krw_coin26)
            # 거래량 동반한 5, 20일 이평선 조회.
            #macd26 = get_acc_ma20(krw_coin26)

            # 1초 딜레이.
            time.sleep(1)
            ###############################


            ###############################
            # 코인27

            # 보유수량 불러오기
            krw_balance27 = upbit.get_balance(krw_coin27)
            # 코인 현재가 불러오기
            price27 = pyupbit.get_current_price(krw_coin27)
            # 보유코인 원화금액으로 계산하기
            bp27 = price27 * krw_balance27

            # MACD 조회.
            #macd27 = get_macd(krw_coin27)
            # 거래량 동반한 MACD 조회.
            macd27 = get_acc_macd(krw_coin27)
            # 5, 20일 이평선 조회.
            #macd27 = get_ma20(krw_coin27)
            # 거래량 동반한 5, 20일 이평선 조회.
            #macd27 = get_acc_ma20(krw_coin27)

            # 1초 딜레이.
            time.sleep(1)
            ###############################


            ###############################
            # 코인28

            # 보유수량 불러오기
            krw_balance28 = upbit.get_balance(krw_coin28)
            # 코인 현재가 불러오기
            price28 = pyupbit.get_current_price(krw_coin28)
            # 보유코인 원화금액으로 계산하기
            bp28 = price28 * krw_balance28

            # MACD 조회.
            #macd28 = get_macd(krw_coin28)
            # 거래량 동반한 MACD 조회.
            macd28 = get_acc_macd(krw_coin28)
            # 5, 20일 이평선 조회.
            #macd28 = get_ma20(krw_coin28)
            # 거래량 동반한 5, 20일 이평선 조회.
            #macd28 = get_acc_ma20(krw_coin28)

            # 1초 딜레이.
            time.sleep(1)
            ###############################


            ###############################
            # 코인29

            # 보유수량 불러오기
            krw_balance29 = upbit.get_balance(krw_coin29)
            # 코인 현재가 불러오기
            price29 = pyupbit.get_current_price(krw_coin29)
            # 보유코인 원화금액으로 계산하기
            bp29 = price29 * krw_balance29

            # MACD 조회.
            #macd29 = get_macd(krw_coin29)
            # 거래량 동반한 MACD 조회.
            macd29 = get_acc_macd(krw_coin29)
            # 5, 20일 이평선 조회.
            #macd29 = get_ma20(krw_coin29)
            # 거래량 동반한 5, 20일 이평선 조회.
            #macd29 = get_acc_ma20(krw_coin29)

            # 1초 딜레이.
            time.sleep(1)
            ###############################


            ###############################
            # 코인30

            # 보유수량 불러오기
            krw_balance30 = upbit.get_balance(krw_coin30)
            # 코인 현재가 불러오기
            price30 = pyupbit.get_current_price(krw_coin30)
            # 보유코인 원화금액으로 계산하기
            bp30 = price30 * krw_balance30

            # MACD 조회.
            #macd30 = get_macd(krw_coin30)
            # 거래량 동반한 MACD 조회.
            macd30 = get_acc_macd(krw_coin30)
            # 5, 20일 이평선 조회.
            #macd30 = get_ma20(krw_coin30)
            # 거래량 동반한 5, 20일 이평선 조회.
            #macd30 = get_acc_ma20(krw_coin30)

            # 1초 딜레이.
            time.sleep(1)
            ###############################


            ######################################################################################################################################################


            ###############################
            # 코인31

            # 보유수량 불러오기
            krw_balance31 = upbit.get_balance(krw_coin31)
            # 코인 현재가 불러오기
            price31 = pyupbit.get_current_price(krw_coin31)
            # 보유코인 원화금액으로 계산하기
            bp31 = price31 * krw_balance31

            # MACD 조회.
            #macd31 = get_macd(krw_coin31)
            # 거래량 동반한 MACD 조회.
            macd31 = get_acc_macd(krw_coin31)
            # 5, 20일 이평선 조회.
            #macd31 = get_ma20(krw_coin31)
            # 거래량 동반한 5, 20일 이평선 조회.
            #macd31 = get_acc_ma20(krw_coin31)

            # 1초 딜레이.
            time.sleep(1)
            ###############################


            ###############################
            # 코인32

            # 보유수량 불러오기
            krw_balance32 = upbit.get_balance(krw_coin32)
            # 코인 현재가 불러오기
            price32 = pyupbit.get_current_price(krw_coin32)
            # 보유코인 원화금액으로 계산하기
            bp32 = price32 * krw_balance32

            # MACD 조회.
            #macd32 = get_macd(krw_coin32)
            # 거래량 동반한 MACD 조회.
            macd32 = get_acc_macd(krw_coin32)
            # 5, 20일 이평선 조회.
            #macd32 = get_ma20(krw_coin32)
            # 거래량 동반한 5, 20일 이평선 조회.
            #macd32 = get_acc_ma20(krw_coin32)

            # 1초 딜레이.
            time.sleep(1)
            ###############################


            ###############################
            # 코인33

            # 보유수량 불러오기
            krw_balance33 = upbit.get_balance(krw_coin33)
            # 코인 현재가 불러오기
            price33 = pyupbit.get_current_price(krw_coin33)
            # 보유코인 원화금액으로 계산하기
            bp33 = price33 * krw_balance33

            # MACD 조회.
            #macd33 = get_macd(krw_coin33)
            # 거래량 동반한 MACD 조회.
            macd33 = get_acc_macd(krw_coin33)
            # 5, 20일 이평선 조회.
            #macd33 = get_ma20(krw_coin33)
            # 거래량 동반한 5, 20일 이평선 조회.
            #macd33 = get_acc_ma20(krw_coin33)

            # 1초 딜레이.
            time.sleep(1)
            ###############################


            ###############################
            # 코인34

            # 보유수량 불러오기
            krw_balance34 = upbit.get_balance(krw_coin34)
            # 코인 현재가 불러오기
            price34 = pyupbit.get_current_price(krw_coin34)
            # 보유코인 원화금액으로 계산하기
            bp34 = price34 * krw_balance34

            # MACD 조회.
            #macd34 = get_macd(krw_coin34)
            # 거래량 동반한 MACD 조회.
            macd34 = get_acc_macd(krw_coin34)
            # 5, 20일 이평선 조회.
            #macd34 = get_ma20(krw_coin34)
            # 거래량 동반한 5, 20일 이평선 조회.
            #macd34 = get_acc_ma20(krw_coin34)

            # 1초 딜레이.
            time.sleep(1)
            ###############################


            ###############################
            # 코인35

            # 보유수량 불러오기
            krw_balance35 = upbit.get_balance(krw_coin35)
            # 코인 현재가 불러오기
            price35 = pyupbit.get_current_price(krw_coin35)
            # 보유코인 원화금액으로 계산하기
            bp35 = price35 * krw_balance35

            # MACD 조회.
            #macd35 = get_macd(krw_coin35)
            # 거래량 동반한 MACD 조회.
            macd35 = get_acc_macd(krw_coin35)
            # 5, 20일 이평선 조회.
            #macd35 = get_ma20(krw_coin35)
            # 거래량 동반한 5, 20일 이평선 조회.
            #macd35 = get_acc_ma20(krw_coin35)

            # 1초 딜레이.
            time.sleep(1)
            ###############################


            ###############################
            # 코인36

            # 보유수량 불러오기
            krw_balance36 = upbit.get_balance(krw_coin36)
            # 코인 현재가 불러오기
            price36 = pyupbit.get_current_price(krw_coin36)
            # 보유코인 원화금액으로 계산하기
            bp36 = price36 * krw_balance36

            # MACD 조회.
            #macd36 = get_macd(krw_coin36)
            # 거래량 동반한 MACD 조회.
            macd36 = get_acc_macd(krw_coin36)
            # 5, 20일 이평선 조회.
            #macd36 = get_ma20(krw_coin36)
            # 거래량 동반한 5, 20일 이평선 조회.
            #macd36 = get_acc_ma20(krw_coin36)

            # 1초 딜레이.
            time.sleep(1)
            ###############################


            ###############################
            # 코인37

            # 보유수량 불러오기
            krw_balance37 = upbit.get_balance(krw_coin37)
            # 코인 현재가 불러오기
            price37 = pyupbit.get_current_price(krw_coin37)
            # 보유코인 원화금액으로 계산하기
            bp37 = price37 * krw_balance37

            # MACD 조회.
            #macd37 = get_macd(krw_coin37)
            # 거래량 동반한 MACD 조회.
            macd37 = get_acc_macd(krw_coin37)
            # 5, 20일 이평선 조회.
            #macd37 = get_ma20(krw_coin37)
            # 거래량 동반한 5, 20일 이평선 조회.
            #macd37 = get_acc_ma20(krw_coin37)

            # 1초 딜레이.
            time.sleep(1)
            ###############################


            ###############################
            # 코인38

            # 보유수량 불러오기
            krw_balance38 = upbit.get_balance(krw_coin38)
            # 코인 현재가 불러오기
            price38 = pyupbit.get_current_price(krw_coin38)
            # 보유코인 원화금액으로 계산하기
            bp38 = price38 * krw_balance38

            # MACD 조회.
            #macd38 = get_macd(krw_coin38)
            # 거래량 동반한 MACD 조회.
            macd38 = get_acc_macd(krw_coin38)
            # 5, 20일 이평선 조회.
            #macd38 = get_ma20(krw_coin38)
            # 거래량 동반한 5, 20일 이평선 조회.
            #macd38 = get_acc_ma20(krw_coin38)

            # 1초 딜레이.
            time.sleep(1)
            ###############################


            ###############################
            # 코인39

            # 보유수량 불러오기
            krw_balance39 = upbit.get_balance(krw_coin39)
            # 코인 현재가 불러오기
            price39 = pyupbit.get_current_price(krw_coin39)
            # 보유코인 원화금액으로 계산하기
            bp39 = price39 * krw_balance39

            # MACD 조회.
            #macd39 = get_macd(krw_coin39)
            # 거래량 동반한 MACD 조회.
            macd39 = get_acc_macd(krw_coin39)
            # 5, 20일 이평선 조회.
            #macd39 = get_ma20(krw_coin39)
            # 거래량 동반한 5, 20일 이평선 조회.
            #macd39 = get_acc_ma20(krw_coin39)

            # 1초 딜레이.
            time.sleep(1)
            ###############################


            ###############################
            # 코인40

            # 보유수량 불러오기
            krw_balance40 = upbit.get_balance(krw_coin40)
            # 코인 현재가 불러오기
            price40 = pyupbit.get_current_price(krw_coin40)
            # 보유코인 원화금액으로 계산하기
            bp40 = price40 * krw_balance40

            # MACD 조회.
            #macd40 = get_macd(krw_coin40)
            # 거래량 동반한 MACD 조회.
            macd40 = get_acc_macd(krw_coin40)
            # 5, 20일 이평선 조회.
            #macd40 = get_ma20(krw_coin40)
            # 거래량 동반한 5, 20일 이평선 조회.
            #macd40 = get_acc_ma20(krw_coin40)

            # 1초 딜레이.
            time.sleep(1)
            ###############################


            ######################################################################################################################################################


            ###############################
            # 코인41

            # 보유수량 불러오기
            krw_balance41 = upbit.get_balance(krw_coin41)
            # 코인 현재가 불러오기
            price41 = pyupbit.get_current_price(krw_coin41)
            # 보유코인 원화금액으로 계산하기
            bp41 = price41 * krw_balance41

            # MACD 조회.
            #macd41 = get_macd(krw_coin41)
            # 거래량 동반한 MACD 조회.
            macd41 = get_acc_macd(krw_coin41)
            # 5, 20일 이평선 조회.
            #macd41 = get_ma20(krw_coin41)
            # 거래량 동반한 5, 20일 이평선 조회.
            #macd41 = get_acc_ma20(krw_coin41)

            # 1초 딜레이.
            time.sleep(1)
            ###############################


            ###############################
            # 코인42

            # 보유수량 불러오기
            krw_balance42 = upbit.get_balance(krw_coin42)
            # 코인 현재가 불러오기
            price42 = pyupbit.get_current_price(krw_coin42)
            # 보유코인 원화금액으로 계산하기
            bp42 = price42 * krw_balance42

            # MACD 조회.
            #macd42 = get_macd(krw_coin42)
            # 거래량 동반한 MACD 조회.
            macd42 = get_acc_macd(krw_coin42)
            # 5, 20일 이평선 조회.
            #macd42 = get_ma20(krw_coin42)
            # 거래량 동반한 5, 20일 이평선 조회.
            #macd42 = get_acc_ma20(krw_coin42)

            # 1초 딜레이.
            time.sleep(1)
            ###############################


            ###############################
            # 코인43

            # 보유수량 불러오기
            krw_balance43 = upbit.get_balance(krw_coin43)
            # 코인 현재가 불러오기
            price43 = pyupbit.get_current_price(krw_coin43)
            # 보유코인 원화금액으로 계산하기
            bp43 = price43 * krw_balance43

            # MACD 조회.
            #macd43 = get_macd(krw_coin43)
            # 거래량 동반한 MACD 조회.
            macd43 = get_acc_macd(krw_coin43)
            # 5, 20일 이평선 조회.
            #macd43 = get_ma20(krw_coin43)
            # 거래량 동반한 5, 20일 이평선 조회.
            #macd43 = get_acc_ma20(krw_coin43)

            # 1초 딜레이.
            time.sleep(1)
            ###############################


            ###############################
            # 코인44

            # 보유수량 불러오기
            krw_balance44 = upbit.get_balance(krw_coin44)
            # 코인 현재가 불러오기
            price44 = pyupbit.get_current_price(krw_coin44)
            # 보유코인 원화금액으로 계산하기
            bp44 = price44 * krw_balance44

            # MACD 조회.
            #macd44 = get_macd(krw_coin44)
            # 거래량 동반한 MACD 조회.
            macd44 = get_acc_macd(krw_coin44)
            # 5, 20일 이평선 조회.
            #macd44 = get_ma20(krw_coin44)
            # 거래량 동반한 5, 20일 이평선 조회.
            #macd44 = get_acc_ma20(krw_coin44)

            # 1초 딜레이.
            time.sleep(1)
            ###############################


            ###############################
            # 코인45

            # 보유수량 불러오기
            krw_balance45 = upbit.get_balance(krw_coin45)
            # 코인 현재가 불러오기
            price45 = pyupbit.get_current_price(krw_coin45)
            # 보유코인 원화금액으로 계산하기
            bp45 = price45 * krw_balance45

            # MACD 조회.
            #macd45 = get_macd(krw_coin45)
            # 거래량 동반한 MACD 조회.
            macd45 = get_acc_macd(krw_coin45)
            # 5, 20일 이평선 조회.
            #macd45 = get_ma20(krw_coin45)
            # 거래량 동반한 5, 20일 이평선 조회.
            #macd45 = get_acc_ma20(krw_coin45)

            # 1초 딜레이.
            time.sleep(1)
            ###############################


            ###############################
            # 코인46

            # 보유수량 불러오기
            krw_balance46 = upbit.get_balance(krw_coin46)
            # 코인 현재가 불러오기
            price46 = pyupbit.get_current_price(krw_coin46)
            # 보유코인 원화금액으로 계산하기
            bp46 = price46 * krw_balance46

            # MACD 조회.
            #macd46 = get_macd(krw_coin46)
            # 거래량 동반한 MACD 조회.
            macd46 = get_acc_macd(krw_coin46)
            # 5, 20일 이평선 조회.
            #macd46 = get_ma20(krw_coin46)
            # 거래량 동반한 5, 20일 이평선 조회.
            #macd46 = get_acc_ma20(krw_coin46)

            # 1초 딜레이.
            time.sleep(1)
            ###############################


            ###############################
            # 코인47

            # 보유수량 불러오기
            krw_balance47 = upbit.get_balance(krw_coin47)
            # 코인 현재가 불러오기
            price47 = pyupbit.get_current_price(krw_coin47)
            # 보유코인 원화금액으로 계산하기
            bp47 = price47 * krw_balance47

            # MACD 조회.
            #macd47 = get_macd(krw_coin47)
            # 거래량 동반한 MACD 조회.
            macd47 = get_acc_macd(krw_coin47)
            # 5, 20일 이평선 조회.
            #macd47 = get_ma20(krw_coin47)
            # 거래량 동반한 5, 20일 이평선 조회.
            #macd47 = get_acc_ma20(krw_coin47)

            # 1초 딜레이.
            time.sleep(1)
            ###############################


            ###############################
            # 코인48

            # 보유수량 불러오기
            krw_balance48 = upbit.get_balance(krw_coin48)
            # 코인 현재가 불러오기
            price48 = pyupbit.get_current_price(krw_coin48)
            # 보유코인 원화금액으로 계산하기
            bp48 = price48 * krw_balance48

            # MACD 조회.
            #macd48 = get_macd(krw_coin48)
            # 거래량 동반한 MACD 조회.
            macd48 = get_acc_macd(krw_coin48)
            # 5, 20일 이평선 조회.
            #macd48 = get_ma20(krw_coin48)
            # 거래량 동반한 5, 20일 이평선 조회.
            #macd48 = get_acc_ma20(krw_coin48)

            # 1초 딜레이.
            time.sleep(1)
            ###############################


            ###############################
            # 코인49

            # 보유수량 불러오기
            krw_balance49 = upbit.get_balance(krw_coin49)
            # 코인 현재가 불러오기
            price49 = pyupbit.get_current_price(krw_coin49)
            # 보유코인 원화금액으로 계산하기
            bp49 = price49 * krw_balance49

            # MACD 조회.
            #macd49 = get_macd(krw_coin49)
            # 거래량 동반한 MACD 조회.
            macd49 = get_acc_macd(krw_coin49)
            # 5, 20일 이평선 조회.
            #macd49 = get_ma20(krw_coin49)
            # 거래량 동반한 5, 20일 이평선 조회.
            #macd49 = get_acc_ma20(krw_coin49)

            # 1초 딜레이.
            time.sleep(1)
            ###############################


            ###############################
            # 코인50

            # 보유수량 불러오기
            krw_balance50 = upbit.get_balance(krw_coin50)
            # 코인 현재가 불러오기
            price50 = pyupbit.get_current_price(krw_coin50)
            # 보유코인 원화금액으로 계산하기
            bp50 = price50 * krw_balance50

            # MACD 조회.
            #macd50 = get_macd(krw_coin50)
            # 거래량 동반한 MACD 조회.
            macd50 = get_acc_macd(krw_coin50)
            # 5, 20일 이평선 조회.
            #macd50 = get_ma20(krw_coin50)
            # 거래량 동반한 5, 20일 이평선 조회.
            #macd50 = get_acc_ma20(krw_coin50)

            # 1초 딜레이.
            time.sleep(1)
            ###############################


            ######################################################################################################################################################


            ###############################
            # 코인51

            # 보유수량 불러오기
            krw_balance51 = upbit.get_balance(krw_coin51)
            # 코인 현재가 불러오기
            price51 = pyupbit.get_current_price(krw_coin51)
            # 보유코인 원화금액으로 계산하기
            bp51 = price51 * krw_balance51

            # MACD 조회.
            #macd51 = get_macd(krw_coin51)
            # 거래량 동반한 MACD 조회.
            macd51 = get_acc_macd(krw_coin51)
            # 5, 20일 이평선 조회.
            #macd51 = get_ma20(krw_coin51)
            # 거래량 동반한 5, 20일 이평선 조회.
            #macd51 = get_acc_ma20(krw_coin51)

            # 1초 딜레이.
            time.sleep(1)
            ###############################


            ###############################
            # 코인52

            # 보유수량 불러오기
            krw_balance52 = upbit.get_balance(krw_coin52)
            # 코인 현재가 불러오기
            price52 = pyupbit.get_current_price(krw_coin52)
            # 보유코인 원화금액으로 계산하기
            bp52 = price52 * krw_balance52

            # MACD 조회.
            #macd52 = get_macd(krw_coin52)
            # 거래량 동반한 MACD 조회.
            macd52 = get_acc_macd(krw_coin52)
            # 5, 20일 이평선 조회.
            #macd52 = get_ma20(krw_coin52)
            # 거래량 동반한 5, 20일 이평선 조회.
            #macd52 = get_acc_ma20(krw_coin52)

            # 1초 딜레이.
            time.sleep(1)
            ###############################


            ###############################
            # 코인53

            # 보유수량 불러오기
            krw_balance53 = upbit.get_balance(krw_coin53)
            # 코인 현재가 불러오기
            price53 = pyupbit.get_current_price(krw_coin53)
            # 보유코인 원화금액으로 계산하기
            bp53 = price53 * krw_balance53

            # MACD 조회.
            #macd53 = get_macd(krw_coin53)
            # 거래량 동반한 MACD 조회.
            macd53 = get_acc_macd(krw_coin53)
            # 5, 20일 이평선 조회.
            #macd53 = get_ma20(krw_coin53)
            # 거래량 동반한 5, 20일 이평선 조회.
            #macd53 = get_acc_ma20(krw_coin53)

            # 1초 딜레이.
            time.sleep(1)
            ###############################


            ###############################
            # 코인54

            # 보유수량 불러오기
            krw_balance54 = upbit.get_balance(krw_coin54)
            # 코인 현재가 불러오기
            price54 = pyupbit.get_current_price(krw_coin54)
            # 보유코인 원화금액으로 계산하기
            bp54 = price54 * krw_balance54

            # MACD 조회.
            #macd54 = get_macd(krw_coin54)
            # 거래량 동반한 MACD 조회.
            macd54 = get_acc_macd(krw_coin54)
            # 5, 20일 이평선 조회.
            #macd54 = get_ma20(krw_coin54)
            # 거래량 동반한 5, 20일 이평선 조회.
            #macd54 = get_acc_ma20(krw_coin54)

            # 1초 딜레이.
            time.sleep(1)
            ###############################


            ###############################
            # 코인55

            # 보유수량 불러오기
            krw_balance55 = upbit.get_balance(krw_coin55)
            # 코인 현재가 불러오기
            price55 = pyupbit.get_current_price(krw_coin55)
            # 보유코인 원화금액으로 계산하기
            bp55 = price55 * krw_balance55

            # MACD 조회.
            #macd55 = get_macd(krw_coin55)
            # 거래량 동반한 MACD 조회.
            macd55 = get_acc_macd(krw_coin55)
            # 5, 20일 이평선 조회.
            #macd55 = get_ma20(krw_coin55)
            # 거래량 동반한 5, 20일 이평선 조회.
            #macd55 = get_acc_ma20(krw_coin55)

            # 1초 딜레이.
            time.sleep(1)
            ###############################


            ######################################################################################################################################################


            # 매도전용 코인 불러오기


            ######################################################################################################################################################


            ###############################
            # 코인56

            # 보유수량 불러오기
            krw_balance56 = upbit.get_balance(krw_coin56)
            # 코인 현재가 불러오기
            price56 = pyupbit.get_current_price(krw_coin56)
            # 보유코인 원화금액으로 계산하기
            bp56 = price56 * krw_balance56

            # MACD 조회.
            #macd56 = get_macd(krw_coin56)
            # 거래량 동반한 MACD 조회.
            macd56 = get_acc_macd(krw_coin56)
            # 5, 20일 이평선 조회.
            #macd56 = get_ma20(krw_coin56)
            # 거래량 동반한 5, 20일 이평선 조회.
            #macd56 = get_acc_ma20(krw_coin56)

            # 1초 딜레이.
            time.sleep(1)
            ###############################


            ###############################
            # 코인57

            # 보유수량 불러오기
            krw_balance57 = upbit.get_balance(krw_coin57)
            # 코인 현재가 불러오기
            price57 = pyupbit.get_current_price(krw_coin57)
            # 보유코인 원화금액으로 계산하기
            bp57 = price57 * krw_balance57

            # MACD 조회.
            #macd57 = get_macd(krw_coin57)
            # 거래량 동반한 MACD 조회.
            macd57 = get_acc_macd(krw_coin57)
            # 5, 20일 이평선 조회.
            #macd57 = get_ma20(krw_coin57)
            # 거래량 동반한 5, 20일 이평선 조회.
            #macd57 = get_acc_ma20(krw_coin57)

            # 1초 딜레이.
            time.sleep(1)
            ###############################


            ###############################
            # 코인58

            # 보유수량 불러오기
            krw_balance58 = upbit.get_balance(krw_coin58)
            # 코인 현재가 불러오기
            price58 = pyupbit.get_current_price(krw_coin58)
            # 보유코인 원화금액으로 계산하기
            bp58 = price58 * krw_balance58

            # MACD 조회.
            #macd58 = get_macd(krw_coin58)
            # 거래량 동반한 MACD 조회.
            macd58 = get_acc_macd(krw_coin58)
            # 5, 20일 이평선 조회.
            #macd58 = get_ma20(krw_coin58)
            # 거래량 동반한 5, 20일 이평선 조회.
            #macd58 = get_acc_ma20(krw_coin58)

            # 1초 딜레이.
            time.sleep(1)
            ###############################


            ###############################
            # 코인59

            # 보유수량 불러오기
            krw_balance59 = upbit.get_balance(krw_coin59)
            # 코인 현재가 불러오기
            price59 = pyupbit.get_current_price(krw_coin59)
            # 보유코인 원화금액으로 계산하기
            bp59 = price59 * krw_balance59

            # MACD 조회.
            #macd59 = get_macd(krw_coin59)
            # 거래량 동반한 MACD 조회.
            macd59 = get_acc_macd(krw_coin59)
            # 5, 20일 이평선 조회.
            #macd59 = get_ma20(krw_coin59)
            # 거래량 동반한 5, 20일 이평선 조회.
            #macd59 = get_acc_ma20(krw_coin59)

            # 1초 딜레이.
            time.sleep(1)
            ###############################


            ###############################
            # 코인60

            # 보유수량 불러오기
            krw_balance60 = upbit.get_balance(krw_coin60)
            # 코인 현재가 불러오기
            price60 = pyupbit.get_current_price(krw_coin60)
            # 보유코인 원화금액으로 계산하기
            bp60 = price60 * krw_balance60

            # MACD 조회.
            #macd60 = get_macd(krw_coin60)
            # 거래량 동반한 MACD 조회.
            macd60 = get_acc_macd(krw_coin60)
            # 5, 20일 이평선 조회.
            #macd60 = get_ma20(krw_coin60)
            # 거래량 동반한 5, 20일 이평선 조회.
            #macd60 = get_acc_ma20(krw_coin60)

            # 1초 딜레이.
            time.sleep(1)
            ###############################


            ######################################################################################################################################################


            ###############################
            # 코인61

            # 보유수량 불러오기
            krw_balance61 = upbit.get_balance(krw_coin61)
            # 코인 현재가 불러오기
            price61 = pyupbit.get_current_price(krw_coin61)
            # 보유코인 원화금액으로 계산하기
            bp61 = price61 * krw_balance61

            # MACD 조회.
            #macd61 = get_macd(krw_coin61)
            # 거래량 동반한 MACD 조회.
            macd61 = get_acc_macd(krw_coin61)
            # 5, 20일 이평선 조회.
            #macd61 = get_ma20(krw_coin61)
            # 거래량 동반한 5, 20일 이평선 조회.
            #macd61 = get_acc_ma20(krw_coin61)

            # 1초 딜레이.
            time.sleep(1)
            ###############################


            ###############################
            # 코인62

            # 보유수량 불러오기
            krw_balance62 = upbit.get_balance(krw_coin62)
            # 코인 현재가 불러오기
            price62 = pyupbit.get_current_price(krw_coin62)
            # 보유코인 원화금액으로 계산하기
            bp62 = price62 * krw_balance62

            # MACD 조회.
            #macd62 = get_macd(krw_coin62)
            # 거래량 동반한 MACD 조회.
            macd62 = get_acc_macd(krw_coin62)
            # 5, 20일 이평선 조회.
            #macd62 = get_ma20(krw_coin62)
            # 거래량 동반한 5, 20일 이평선 조회.
            #macd62 = get_acc_ma20(krw_coin62)

            # 1초 딜레이.
            time.sleep(1)
            ###############################


            ###############################
            # 코인63

            # 보유수량 불러오기
            krw_balance63 = upbit.get_balance(krw_coin63)
            # 코인 현재가 불러오기
            price63 = pyupbit.get_current_price(krw_coin63)
            # 보유코인 원화금액으로 계산하기
            bp63 = price63 * krw_balance63

            # MACD 조회.
            #macd63 = get_macd(krw_coin63)
            # 거래량 동반한 MACD 조회.
            macd63 = get_acc_macd(krw_coin63)
            # 5, 20일 이평선 조회.
            #macd63 = get_ma20(krw_coin63)
            # 거래량 동반한 5, 20일 이평선 조회.
            #macd63 = get_acc_ma20(krw_coin63)

            # 1초 딜레이.
            time.sleep(1)
            ###############################


            ###############################
            # 코인64

            # 보유수량 불러오기
            krw_balance64 = upbit.get_balance(krw_coin64)
            # 코인 현재가 불러오기
            price64 = pyupbit.get_current_price(krw_coin64)
            # 보유코인 원화금액으로 계산하기
            bp64 = price64 * krw_balance64

            # MACD 조회.
            #macd64 = get_macd(krw_coin64)
            # 거래량 동반한 MACD 조회.
            macd64 = get_acc_macd(krw_coin64)
            # 5, 20일 이평선 조회.
            #macd64 = get_ma20(krw_coin64)
            # 거래량 동반한 5, 20일 이평선 조회.
            #macd64 = get_acc_ma20(krw_coin64)

            # 1초 딜레이.
            time.sleep(1)
            ###############################


            ###############################
            # 코인65

            # 보유수량 불러오기
            krw_balance65 = upbit.get_balance(krw_coin65)
            # 코인 현재가 불러오기
            price65 = pyupbit.get_current_price(krw_coin65)
            # 보유코인 원화금액으로 계산하기
            bp65 = price65 * krw_balance65

            # MACD 조회.
            #macd65 = get_macd(krw_coin65)
            # 거래량 동반한 MACD 조회.
            macd65 = get_acc_macd(krw_coin65)
            # 5, 20일 이평선 조회.
            #macd65 = get_ma20(krw_coin65)
            # 거래량 동반한 5, 20일 이평선 조회.
            #macd65 = get_acc_ma20(krw_coin65)

            # 1초 딜레이.
            time.sleep(1)
            ###############################


            ###############################
            # 코인66

            # 보유수량 불러오기
            krw_balance66 = upbit.get_balance(krw_coin66)
            # 코인 현재가 불러오기
            price66 = pyupbit.get_current_price(krw_coin66)
            # 보유코인 원화금액으로 계산하기
            bp66 = price66 * krw_balance66

            # MACD 조회.
            #macd66 = get_macd(krw_coin66)
            # 거래량 동반한 MACD 조회.
            macd66 = get_acc_macd(krw_coin66)
            # 5, 20일 이평선 조회.
            #macd66 = get_ma20(krw_coin66)
            # 거래량 동반한 5, 20일 이평선 조회.
            #macd66 = get_acc_ma20(krw_coin66)

            # 1초 딜레이.
            time.sleep(1)
            ###############################


            ###############################
            # 코인67

            # 보유수량 불러오기
            krw_balance67 = upbit.get_balance(krw_coin67)
            # 코인 현재가 불러오기
            price67 = pyupbit.get_current_price(krw_coin67)
            # 보유코인 원화금액으로 계산하기
            bp67 = price67 * krw_balance67

            # MACD 조회.
            #macd67 = get_macd(krw_coin67)
            # 거래량 동반한 MACD 조회.
            macd67 = get_acc_macd(krw_coin67)
            # 5, 20일 이평선 조회.
            #macd67 = get_ma20(krw_coin67)
            # 거래량 동반한 5, 20일 이평선 조회.
            #macd67 = get_acc_ma20(krw_coin67)

            # 1초 딜레이.
            time.sleep(1)
            ###############################


            ###############################
            # 코인68

            # 보유수량 불러오기
            krw_balance68 = upbit.get_balance(krw_coin68)
            # 코인 현재가 불러오기
            price68 = pyupbit.get_current_price(krw_coin68)
            # 보유코인 원화금액으로 계산하기
            bp68 = price68 * krw_balance68

            # MACD 조회.
            #macd68 = get_macd(krw_coin68)
            # 거래량 동반한 MACD 조회.
            macd68 = get_acc_macd(krw_coin68)
            # 5, 20일 이평선 조회.
            #macd68 = get_ma20(krw_coin68)
            # 거래량 동반한 5, 20일 이평선 조회.
            #macd68 = get_acc_ma20(krw_coin68)

            # 1초 딜레이.
            time.sleep(1)
            ###############################


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
            bpAve2 = bp11 + bp12 + bp13 + bp14 + bp15 + bp16 + bp17 + bp18 + bp19 + bp20
            bpAve3 = bp21 + bp22 + bp23 + bp24 + bp25 + bp26 + bp27 + bp28 + bp29 + bp30
            bpAve4 = bp31 + bp32 + bp33 + bp34 + bp35 + bp36 + bp37 + bp38 + bp39 + bp40
            bpAve5 = bp41 + bp42 + bp43 + bp44 + bp45 + bp46 + bp47 + bp48 + bp49 + bp50
            bpAve6 = bp51 + bp52 + bp53 + bp54 + bp55 + bp56 + bp57 + bp58 + bp59 + bp60
            bpAve7 = bp61 + bp62 + bp63 + bp64 + bp65 + bp66 + bp67 + bp68

            bpAve = (bpAve1 + bpAve2 + bpAve3 + bpAve4 + bpAve5 + bpAve6 + bpAve7 ) / 69
            

            print("")
            print("")
            print("********** ********** ********** ********** **********")
            print("")
            print("[[[매도시작]]]")
            print(f"[ 현재시간 : {now}  ||  보유금액 = ￦{krw}  |  매도평균가 = ￦{bpAve} ]")
            print("")
            print("********** ********** ********** ********** **********")
            print("")






            ###############################
            # 코인1

            # 코인별 금액 비율조정
            sell_bpAve1 = bpAve * bpPer1

            # MACD 조건문
            if macd1 < 0:     # macd가 0보다 작을때는 매도
                if coinMode1 == 1 or coinMode1 == 3:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = 매수만가능 , 3 = >>>매도만가능<<<
                    if op_mode1 == 1 or op_mode1 == 4:   # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                        print("")
                        print(f"[ 1. 매도시간 : {now}  |  코인명 : {coin1}  |  현재가 = ￦{price1}  |  MACD = ￦{macd1}  |  보유수량 = {krw_balance1}  |  평가금액 = ￦{bp1}  ||  매도평균금액 = ￦{sell_bpAve1} ]")

                        if bp1 > sell_bpAve1: # 보유금액이 평균가보다 높을때
                            # 매도할 코인 금액 = 코인보유금액 - 평균가
                            sell_krw_price1 = bp1 - sell_bpAve1

                            if sell_krw_price1 >= 10000:    # 매도할 금액이 ￦10,000 보다 높을때 매도
                                # 매도할 코인 갯수 = 매도할 코인 금액 - 현재가
                                sell_krw_balance1 = sell_krw_price1 / price1

                                # 보유코인 초과금액 매도시도
                                # 매도할 코인명 - krw_coin1, 매도할 코인수량 - sell_krw_balance1
                                upbit.sell_market_order(krw_coin1, sell_krw_balance1)

                                # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                op_mode1 = 2

                                print("평균 이상 금액 매도")
                                print(f"매도한금액 = ￦{sell_krw_price1}  |  매도한수량 = {sell_krw_balance1}  |  매수가능여부 - {op_mode1} - 매수가능-매도불가")
                                print("")
                            else:
                                # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                op_mode1 = 2

                                print("￦10,000 이하 금액 매도불가")
                                print(f"매수가능여부 - {op_mode1} - 매수가능-매도불가")
                                print("")

                        else:
                            # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                            op_mode1 = 2

                            print("평균 이하 금액 매도불가")
                            print(f"매수가능여부 - {op_mode1} - 매수가능-매도불가")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################


            ###############################
            # 코인2

            # 코인별 금액 비율조정
            sell_bpAve2 = bpAve * bpPer2

            # MACD 조건문
            if macd2 < 0:     # macd가 0보다 작을때는 매도
                if coinMode2 == 1 or coinMode2 == 3:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = 매수만가능 , 3 = >>>매도만가능<<<
                    if op_mode2 == 1 or op_mode2 == 4:   # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                        print("")
                        print(f"[ 2. 매도시간 : {now}  |  코인명 : {coin2}  |  현재가 = ￦{price2}  |  MACD = ￦{macd2}  |  보유수량 = {krw_balance2}  |  평가금액 = ￦{bp2}  ||  매도평균금액 = ￦{sell_bpAve2} ]")

                        if bp2 > sell_bpAve2: # 보유금액이 평균가보다 높을때
                            # 매도할 코인 금액 = 코인보유금액 - 평균가
                            sell_krw_price2 = bp2 - sell_bpAve2

                            if sell_krw_price2 >= 10000:    # 매도할 금액이 ￦10,000 보다 높을때 매도
                                # 매도할 코인 갯수 = 매도할 코인 금액 - 현재가
                                sell_krw_balance2 = sell_krw_price2 / price2

                                # 보유코인 초과금액 매도시도
                                # 매도할 코인명 - krw_coin2, 매도할 코인수량 - sell_krw_balance2
                                upbit.sell_market_order(krw_coin2, sell_krw_balance2)

                                # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                op_mode2 = 2

                                print("평균 이상 금액 매도")
                                print(f"매도한금액 = ￦{sell_krw_price2}  |  매도한수량 = {sell_krw_balance2}  |  매수가능여부 - {op_mode2} - 매수가능-매도불가")
                                print("")
                            else:
                                # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                op_mode2 = 2

                                print("￦10,000 이하 금액 매도불가")
                                print(f"매수가능여부 - {op_mode2} - 매수가능-매도불가")
                                print("")

                        else:
                            # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                            op_mode2 = 2

                            print("평균 이하 금액 매도불가")
                            print(f"매수가능여부 - {op_mode2} - 매수가능-매도불가")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################


            ###############################
            # 코인3

            # 코인별 금액 비율조정
            sell_bpAve3 = bpAve * bpPer3

            # MACD 조건문
            if macd3 < 0:     # macd가 0보다 작을때는 매도
                if coinMode3 == 1 or coinMode3 == 3:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = 매수만가능 , 3 = >>>매도만가능<<<
                    if op_mode3 == 1 or op_mode3 == 4:   # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                        print("")
                        print(f"[ 3. 매도시간 : {now}  |  코인명 : {coin3}  |  현재가 = ￦{price3}  |  MACD = ￦{macd3}  |  보유수량 = {krw_balance3}  |  평가금액 = ￦{bp3}  ||  매도평균금액 = ￦{sell_bpAve3} ]")

                        if bp3 > sell_bpAve3: # 보유금액이 평균가보다 높을때
                            # 매도할 코인 금액 = 코인보유금액 - 평균가
                            sell_krw_price3 = bp3 - sell_bpAve3

                            if sell_krw_price3 >= 10000:    # 매도할 금액이 ￦10,000 보다 높을때 매도
                                # 매도할 코인 갯수 = 매도할 코인 금액 - 현재가
                                sell_krw_balance3 = sell_krw_price3 / price3

                                # 보유코인 초과금액 매도시도
                                # 매도할 코인명 - krw_coin3, 매도할 코인수량 - sell_krw_balance3
                                upbit.sell_market_order(krw_coin3, sell_krw_balance3)

                                # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                op_mode3 = 2

                                print("평균 이상 금액 매도")
                                print(f"매도한금액 = ￦{sell_krw_price3}  |  매도한수량 = {sell_krw_balance3}  |  매수가능여부 - {op_mode3} - 매수가능-매도불가")
                                print("")
                            else:
                                # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                op_mode3 = 2

                                print("￦10,000 이하 금액 매도불가")
                                print(f"매수가능여부 - {op_mode3} - 매수가능-매도불가")
                                print("")

                        else:
                            # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                            op_mode3 = 2

                            print("평균 이하 금액 매도불가")
                            print(f"매수가능여부 - {op_mode3} - 매수가능-매도불가")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################


            ###############################
            # 코인4

            # 코인별 금액 비율조정
            sell_bpAve4 = bpAve * bpPer4

            # MACD 조건문
            if macd4 < 0:     # macd가 0보다 작을때는 매도
                if coinMode4 == 1 or coinMode4 == 3:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = 매수만가능 , 3 = >>>매도만가능<<<
                    if op_mode4 == 1 or op_mode4 == 4:   # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                        print("")
                        print(f"[ 4. 매도시간 : {now}  |  코인명 : {coin4}  |  현재가 = ￦{price4}  |  MACD = ￦{macd4}  |  보유수량 = {krw_balance4}  |  평가금액 = ￦{bp4}  ||  매도평균금액 = ￦{sell_bpAve4} ]")

                        if bp4 > sell_bpAve4: # 보유금액이 평균가보다 높을때
                            # 매도할 코인 금액 = 코인보유금액 - 평균가
                            sell_krw_price4 = bp4 - sell_bpAve4

                            if sell_krw_price4 >= 10000:    # 매도할 금액이 ￦10,000 보다 높을때 매도
                                # 매도할 코인 갯수 = 매도할 코인 금액 - 현재가
                                sell_krw_balance4 = sell_krw_price4 / price4

                                # 보유코인 초과금액 매도시도
                                # 매도할 코인명 - krw_coin4, 매도할 코인수량 - sell_krw_balance4
                                upbit.sell_market_order(krw_coin4, sell_krw_balance4)

                                # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                op_mode4 = 2

                                print("평균 이상 금액 매도")
                                print(f"매도한금액 = ￦{sell_krw_price4}  |  매도한수량 = {sell_krw_balance4}  |  매수가능여부 - {op_mode4} - 매수가능-매도불가")
                                print("")
                            else:
                                # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                op_mode4 = 2

                                print("￦10,000 이하 금액 매도불가")
                                print(f"매수가능여부 - {op_mode4} - 매수가능-매도불가")
                                print("")

                        else:
                            # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                            op_mode4 = 2

                            print("평균 이하 금액 매도불가")
                            print(f"매수가능여부 - {op_mode4} - 매수가능-매도불가")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################


            ###############################
            # 코인5

            # 코인별 금액 비율조정
            sell_bpAve5 = bpAve * bpPer5

            # MACD 조건문
            if macd5 < 0:     # macd가 0보다 작을때는 매도
                if coinMode5 == 1 or coinMode5 == 3:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = 매수만가능 , 3 = >>>매도만가능<<<
                    if op_mode5 == 1 or op_mode5 == 4:   # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                        print("")
                        print(f"[ 5. 매도시간 : {now}  |  코인명 : {coin5}  |  현재가 = ￦{price5}  |  MACD = ￦{macd5}  |  보유수량 = {krw_balance5}  |  평가금액 = ￦{bp5}  ||  매도평균금액 = ￦{sell_bpAve5} ]")

                        if bp5 > sell_bpAve5: # 보유금액이 평균가보다 높을때
                            # 매도할 코인 금액 = 코인보유금액 - 평균가
                            sell_krw_price5 = bp5 - sell_bpAve5

                            if sell_krw_price5 >= 10000:    # 매도할 금액이 ￦10,000 보다 높을때 매도
                                # 매도할 코인 갯수 = 매도할 코인 금액 - 현재가
                                sell_krw_balance5 = sell_krw_price5 / price5

                                # 보유코인 초과금액 매도시도
                                # 매도할 코인명 - krw_coin5, 매도할 코인수량 - sell_krw_balance5
                                upbit.sell_market_order(krw_coin5, sell_krw_balance5)

                                # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                op_mode5 = 2

                                print("평균 이상 금액 매도")
                                print(f"매도한금액 = ￦{sell_krw_price5}  |  매도한수량 = {sell_krw_balance5}  |  매수가능여부 - {op_mode5} - 매수가능-매도불가")
                                print("")
                            else:
                                # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                op_mode5 = 2

                                print("￦10,000 이하 금액 매도불가")
                                print(f"매수가능여부 - {op_mode5} - 매수가능-매도불가")
                                print("")

                        else:
                            # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                            op_mode5 = 2

                            print("평균 이하 금액 매도불가")
                            print(f"매수가능여부 - {op_mode5} - 매수가능-매도불가")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################


            ###############################
            # 코인6

            # 코인별 금액 비율조정
            sell_bpAve6 = bpAve * bpPer6

            # MACD 조건문
            if macd6 < 0:     # macd가 0보다 작을때는 매도
                if coinMode6 == 1 or coinMode6 == 3:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = 매수만가능 , 3 = >>>매도만가능<<<
                    if op_mode6 == 1 or op_mode6 == 4:   # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                        print("")
                        print(f"[ 6. 매도시간 : {now}  |  코인명 : {coin6}  |  현재가 = ￦{price6}  |  MACD = ￦{macd6}  |  보유수량 = {krw_balance6}  |  평가금액 = ￦{bp6}  ||  매도평균금액 = ￦{sell_bpAve6} ]")

                        if bp6 > sell_bpAve6: # 보유금액이 평균가보다 높을때
                            # 매도할 코인 금액 = 코인보유금액 - 평균가
                            sell_krw_price6 = bp6 - sell_bpAve6

                            if sell_krw_price6 >= 10000:    # 매도할 금액이 ￦10,000 보다 높을때 매도
                                # 매도할 코인 갯수 = 매도할 코인 금액 - 현재가
                                sell_krw_balance6 = sell_krw_price6 / price6

                                # 보유코인 초과금액 매도시도
                                # 매도할 코인명 - krw_coin6, 매도할 코인수량 - sell_krw_balance6
                                upbit.sell_market_order(krw_coin6, sell_krw_balance6)

                                # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                op_mode6 = 2

                                print("평균 이상 금액 매도")
                                print(f"매도한금액 = ￦{sell_krw_price6}  |  매도한수량 = {sell_krw_balance6}  |  매수가능여부 - {op_mode6} - 매수가능-매도불가")
                                print("")
                            else:
                                # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                op_mode6 = 2

                                print("￦10,000 이하 금액 매도불가")
                                print(f"매수가능여부 - {op_mode6} - 매수가능-매도불가")
                                print("")

                        else:
                            # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                            op_mode6 = 2

                            print("평균 이하 금액 매도불가")
                            print(f"매수가능여부 - {op_mode6} - 매수가능-매도불가")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################


            ###############################
            # 코인7

            # 코인별 금액 비율조정
            sell_bpAve7 = bpAve * bpPer7

            # MACD 조건문
            if macd7 < 0:     # macd가 0보다 작을때는 매도
                if coinMode7 == 1 or coinMode7 == 3:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = 매수만가능 , 3 = >>>매도만가능<<<
                    if op_mode7 == 1 or op_mode7 == 4:   # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                        print("")
                        print(f"[ 7. 매도시간 : {now}  |  코인명 : {coin7}  |  현재가 = ￦{price7}  |  MACD = ￦{macd7}  |  보유수량 = {krw_balance7}  |  평가금액 = ￦{bp7}  ||  매도평균금액 = ￦{sell_bpAve7} ]")

                        if bp7 > sell_bpAve7: # 보유금액이 평균가보다 높을때
                            # 매도할 코인 금액 = 코인보유금액 - 평균가
                            sell_krw_price7 = bp7 - sell_bpAve7

                            if sell_krw_price7 >= 10000:    # 매도할 금액이 ￦10,000 보다 높을때 매도
                                # 매도할 코인 갯수 = 매도할 코인 금액 - 현재가
                                sell_krw_balance7 = sell_krw_price7 / price7

                                # 보유코인 초과금액 매도시도
                                # 매도할 코인명 - krw_coin7, 매도할 코인수량 - sell_krw_balance7
                                upbit.sell_market_order(krw_coin7, sell_krw_balance7)

                                # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                op_mode7 = 2

                                print("평균 이상 금액 매도")
                                print(f"매도한금액 = ￦{sell_krw_price7}  |  매도한수량 = {sell_krw_balance7}  |  매수가능여부 - {op_mode7} - 매수가능-매도불가")
                                print("")
                            else:
                                # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                op_mode7 = 2

                                print("￦10,000 이하 금액 매도불가")
                                print(f"매수가능여부 - {op_mode7} - 매수가능-매도불가")
                                print("")

                        else:
                            # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                            op_mode7 = 2

                            print("평균 이하 금액 매도불가")
                            print(f"매수가능여부 - {op_mode7} - 매수가능-매도불가")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################


            ###############################
            # 코인8

            # 코인별 금액 비율조정
            sell_bpAve8 = bpAve * bpPer8

            # MACD 조건문
            if macd8 < 0:     # macd가 0보다 작을때는 매도
                if coinMode8 == 1 or coinMode8 == 3:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = 매수만가능 , 3 = >>>매도만가능<<<
                    if op_mode8 == 1 or op_mode8 == 4:   # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                        print("")
                        print(f"[ 8. 매도시간 : {now}  |  코인명 : {coin8}  |  현재가 = ￦{price8}  |  MACD = ￦{macd8}  |  보유수량 = {krw_balance8}  |  평가금액 = ￦{bp8}  ||  매도평균금액 = ￦{sell_bpAve8} ]")

                        if bp8 > sell_bpAve8: # 보유금액이 평균가보다 높을때
                            # 매도할 코인 금액 = 코인보유금액 - 평균가
                            sell_krw_price8 = bp8 - sell_bpAve8

                            if sell_krw_price8 >= 10000:    # 매도할 금액이 ￦10,000 보다 높을때 매도
                                # 매도할 코인 갯수 = 매도할 코인 금액 - 현재가
                                sell_krw_balance8 = sell_krw_price8 / price8

                                # 보유코인 초과금액 매도시도
                                # 매도할 코인명 - krw_coin8, 매도할 코인수량 - sell_krw_balance8
                                upbit.sell_market_order(krw_coin8, sell_krw_balance8)

                                # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                op_mode8 = 2

                                print("평균 이상 금액 매도")
                                print(f"매도한금액 = ￦{sell_krw_price8}  |  매도한수량 = {sell_krw_balance8}  |  매수가능여부 - {op_mode8} - 매수가능-매도불가")
                                print("")
                            else:
                                # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                op_mode8 = 2

                                print("￦10,000 이하 금액 매도불가")
                                print(f"매수가능여부 - {op_mode8} - 매수가능-매도불가")
                                print("")

                        else:
                            # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                            op_mode8 = 2

                            print("평균 이하 금액 매도불가")
                            print(f"매수가능여부 - {op_mode8} - 매수가능-매도불가")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################


            ###############################
            # 코인9

            # 코인별 금액 비율조정
            sell_bpAve9 = bpAve * bpPer9

            # MACD 조건문
            if macd9 < 0:     # macd가 0보다 작을때는 매도
                if coinMode9 == 1 or coinMode9 == 3:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = 매수만가능 , 3 = >>>매도만가능<<<
                    if op_mode9 == 1 or op_mode9 == 4:   # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                        print("")
                        print(f"[ 9. 매도시간 : {now}  |  코인명 : {coin9}  |  현재가 = ￦{price9}  |  MACD = ￦{macd9}  |  보유수량 = {krw_balance9}  |  평가금액 = ￦{bp9}  ||  매도평균금액 = ￦{sell_bpAve9} ]")

                        if bp9 > sell_bpAve9: # 보유금액이 평균가보다 높을때
                            # 매도할 코인 금액 = 코인보유금액 - 평균가
                            sell_krw_price9 = bp9 - sell_bpAve9

                            if sell_krw_price9 >= 10000:    # 매도할 금액이 ￦10,000 보다 높을때 매도
                                # 매도할 코인 갯수 = 매도할 코인 금액 - 현재가
                                sell_krw_balance9 = sell_krw_price9 / price9

                                # 보유코인 초과금액 매도시도
                                # 매도할 코인명 - krw_coin9, 매도할 코인수량 - sell_krw_balance9
                                upbit.sell_market_order(krw_coin9, sell_krw_balance9)

                                # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                op_mode9 = 2

                                print("평균 이상 금액 매도")
                                print(f"매도한금액 = ￦{sell_krw_price9}  |  매도한수량 = {sell_krw_balance9}  |  매수가능여부 - {op_mode9} - 매수가능-매도불가")
                                print("")
                            else:
                                # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                op_mode9 = 2

                                print("￦10,000 이하 금액 매도불가")
                                print(f"매수가능여부 - {op_mode9} - 매수가능-매도불가")
                                print("")

                        else:
                            # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                            op_mode9 = 2

                            print("평균 이하 금액 매도불가")
                            print(f"매수가능여부 - {op_mode9} - 매수가능-매도불가")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################


            ###############################
            # 코인10

            # 코인별 금액 비율조정
            sell_bpAve10 = bpAve * bpPer10

            # MACD 조건문
            if macd10 < 0:     # macd가 0보다 작을때는 매도
                if coinMode10 == 1 or coinMode10 == 3:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = 매수만가능 , 3 = >>>매도만가능<<<
                    if op_mode10 == 1 or op_mode10 == 4:   # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                        print("")
                        print(f"[ 10. 매도시간 : {now}  |  코인명 : {coin10}  |  현재가 = ￦{price10}  |  MACD = ￦{macd10}  |  보유수량 = {krw_balance10}  |  평가금액 = ￦{bp10}  ||  매도평균금액 = ￦{sell_bpAve10} ]")

                        if bp10 > sell_bpAve10: # 보유금액이 평균가보다 높을때
                            # 매도할 코인 금액 = 코인보유금액 - 평균가
                            sell_krw_price10 = bp10 - sell_bpAve10

                            if sell_krw_price10 >= 10000:    # 매도할 금액이 ￦10,000 보다 높을때 매도
                                # 매도할 코인 갯수 = 매도할 코인 금액 - 현재가
                                sell_krw_balance10 = sell_krw_price10 / price10

                                # 보유코인 초과금액 매도시도
                                # 매도할 코인명 - krw_coin10, 매도할 코인수량 - sell_krw_balance10
                                upbit.sell_market_order(krw_coin10, sell_krw_balance10)

                                # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                op_mode10 = 2

                                print("평균 이상 금액 매도")
                                print(f"매도한금액 = ￦{sell_krw_price10}  |  매도한수량 = {sell_krw_balance10}  |  매수가능여부 - {op_mode10} - 매수가능-매도불가")
                                print("")
                            else:
                                # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                op_mode10 = 2

                                print("￦10,000 이하 금액 매도불가")
                                print(f"매수가능여부 - {op_mode10} - 매수가능-매도불가")
                                print("")

                        else:
                            # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                            op_mode10 = 2

                            print("평균 이하 금액 매도불가")
                            print(f"매수가능여부 - {op_mode10} - 매수가능-매도불가")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################





            ######################################################################################################################################################
            ######################################################################################################################################################
            ######################################################################################################################################################




            ###############################
            # 코인11

            # 코인별 금액 비율조정
            sell_bpAve11 = bpAve * bpPer11

            # MACD 조건문
            if macd11 < 0:     # macd가 0보다 작을때는 매도
                if coinMode11 == 1 or coinMode11 == 3:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = 매수만가능 , 3 = >>>매도만가능<<<
                    if op_mode11 == 1 or op_mode11 == 4:   # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                        print("")
                        print(f"[ 11. 매도시간 : {now}  |  코인명 : {coin11}  |  현재가 = ￦{price11}  |  MACD = ￦{macd11}  |  보유수량 = {krw_balance11}  |  평가금액 = ￦{bp11}  ||  매도평균금액 = ￦{sell_bpAve11} ]")

                        if bp11 > sell_bpAve11: # 보유금액이 평균가보다 높을때
                            # 매도할 코인 금액 = 코인보유금액 - 평균가
                            sell_krw_price11 = bp11 - sell_bpAve11

                            if sell_krw_price11 >= 10000:    # 매도할 금액이 ￦10,000 보다 높을때 매도
                                # 매도할 코인 갯수 = 매도할 코인 금액 - 현재가
                                sell_krw_balance11 = sell_krw_price11 / price11

                                # 보유코인 초과금액 매도시도
                                # 매도할 코인명 - krw_coin11, 매도할 코인수량 - sell_krw_balance11
                                upbit.sell_market_order(krw_coin11, sell_krw_balance11)

                                # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                op_mode11 = 2

                                print("평균 이상 금액 매도")
                                print(f"매도한금액 = ￦{sell_krw_price11}  |  매도한수량 = {sell_krw_balance11}  |  매수가능여부 - {op_mode11} - 매수가능-매도불가")
                                print("")
                            else:
                                # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                op_mode11 = 2

                                print("￦10,000 이하 금액 매도불가")
                                print(f"매수가능여부 - {op_mode11} - 매수가능-매도불가")
                                print("")

                        else:
                            # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                            op_mode11 = 2

                            print("평균 이하 금액 매도불가")
                            print(f"매수가능여부 - {op_mode11} - 매수가능-매도불가")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################


            ###############################
            # 코인12

            # 코인별 금액 비율조정
            sell_bpAve12 = bpAve * bpPer12

            # MACD 조건문
            if macd12 < 0:     # macd가 0보다 작을때는 매도
                if coinMode12 == 1 or coinMode12 == 3:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = 매수만가능 , 3 = >>>매도만가능<<<
                    if op_mode12 == 1 or op_mode12 == 4:   # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                        print("")
                        print(f"[ 12. 매도시간 : {now}  |  코인명 : {coin12}  |  현재가 = ￦{price12}  |  MACD = ￦{macd12}  |  보유수량 = {krw_balance12}  |  평가금액 = ￦{bp12}  ||  매도평균금액 = ￦{sell_bpAve12} ]")

                        if bp12 > sell_bpAve12: # 보유금액이 평균가보다 높을때
                            # 매도할 코인 금액 = 코인보유금액 - 평균가
                            sell_krw_price12 = bp12 - sell_bpAve12

                            if sell_krw_price12 >= 10000:    # 매도할 금액이 ￦10,000 보다 높을때 매도
                                # 매도할 코인 갯수 = 매도할 코인 금액 - 현재가
                                sell_krw_balance12 = sell_krw_price12 / price12

                                # 보유코인 초과금액 매도시도
                                # 매도할 코인명 - krw_coin12, 매도할 코인수량 - sell_krw_balance12
                                upbit.sell_market_order(krw_coin12, sell_krw_balance12)

                                # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                op_mode12 = 2

                                print("평균 이상 금액 매도")
                                print(f"매도한금액 = ￦{sell_krw_price12}  |  매도한수량 = {sell_krw_balance12}  |  매수가능여부 - {op_mode12} - 매수가능-매도불가")
                                print("")
                            else:
                                # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                op_mode12 = 2

                                print("￦10,000 이하 금액 매도불가")
                                print(f"매수가능여부 - {op_mode12} - 매수가능-매도불가")
                                print("")

                        else:
                            # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                            op_mode12 = 2

                            print("평균 이하 금액 매도불가")
                            print(f"매수가능여부 - {op_mode12} - 매수가능-매도불가")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################


            ###############################
            # 코인13

            # 코인별 금액 비율조정
            sell_bpAve13 = bpAve * bpPer13

            # MACD 조건문
            if macd13 < 0:     # macd가 0보다 작을때는 매도
                if coinMode13 == 1 or coinMode13 == 3:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = 매수만가능 , 3 = >>>매도만가능<<<
                    if op_mode13 == 1 or op_mode13 == 4:   # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                        print("")
                        print(f"[ 13. 매도시간 : {now}  |  코인명 : {coin13}  |  현재가 = ￦{price13}  |  MACD = ￦{macd13}  |  보유수량 = {krw_balance13}  |  평가금액 = ￦{bp13}  ||  매도평균금액 = ￦{sell_bpAve13} ]")

                        if bp13 > sell_bpAve13: # 보유금액이 평균가보다 높을때
                            # 매도할 코인 금액 = 코인보유금액 - 평균가
                            sell_krw_price13 = bp13 - sell_bpAve13

                            if sell_krw_price13 >= 10000:    # 매도할 금액이 ￦10,000 보다 높을때 매도
                                # 매도할 코인 갯수 = 매도할 코인 금액 - 현재가
                                sell_krw_balance13 = sell_krw_price13 / price13

                                # 보유코인 초과금액 매도시도
                                # 매도할 코인명 - krw_coin13, 매도할 코인수량 - sell_krw_balance13
                                upbit.sell_market_order(krw_coin13, sell_krw_balance13)

                                # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                op_mode13 = 2

                                print("평균 이상 금액 매도")
                                print(f"매도한금액 = ￦{sell_krw_price13}  |  매도한수량 = {sell_krw_balance13}  |  매수가능여부 - {op_mode13} - 매수가능-매도불가")
                                print("")
                            else:
                                # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                op_mode13 = 2

                                print("￦10,000 이하 금액 매도불가")
                                print(f"매수가능여부 - {op_mode13} - 매수가능-매도불가")
                                print("")

                        else:
                            # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                            op_mode13 = 2

                            print("평균 이하 금액 매도불가")
                            print(f"매수가능여부 - {op_mode13} - 매수가능-매도불가")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################


            ###############################
            # 코인14

            # 코인별 금액 비율조정
            sell_bpAve14 = bpAve * bpPer14

            # MACD 조건문
            if macd14 < 0:     # macd가 0보다 작을때는 매도
                if coinMode14 == 1 or coinMode14 == 3:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = 매수만가능 , 3 = >>>매도만가능<<<
                    if op_mode14 == 1 or op_mode14 == 4:   # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                        print("")
                        print(f"[ 14. 매도시간 : {now}  |  코인명 : {coin14}  |  현재가 = ￦{price14}  |  MACD = ￦{macd14}  |  보유수량 = {krw_balance14}  |  평가금액 = ￦{bp14}  ||  매도평균금액 = ￦{sell_bpAve14} ]")

                        if bp14 > sell_bpAve14: # 보유금액이 평균가보다 높을때
                            # 매도할 코인 금액 = 코인보유금액 - 평균가
                            sell_krw_price14 = bp14 - sell_bpAve14

                            if sell_krw_price14 >= 10000:    # 매도할 금액이 ￦10,000 보다 높을때 매도
                                # 매도할 코인 갯수 = 매도할 코인 금액 - 현재가
                                sell_krw_balance14 = sell_krw_price14 / price14

                                # 보유코인 초과금액 매도시도
                                # 매도할 코인명 - krw_coin14, 매도할 코인수량 - sell_krw_balance14
                                upbit.sell_market_order(krw_coin14, sell_krw_balance14)

                                # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                op_mode14 = 2

                                print("평균 이상 금액 매도")
                                print(f"매도한금액 = ￦{sell_krw_price14}  |  매도한수량 = {sell_krw_balance14}  |  매수가능여부 - {op_mode14} - 매수가능-매도불가")
                                print("")
                            else:
                                # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                op_mode14 = 2

                                print("￦10,000 이하 금액 매도불가")
                                print(f"매수가능여부 - {op_mode14} - 매수가능-매도불가")
                                print("")

                        else:
                            # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                            op_mode14 = 2

                            print("평균 이하 금액 매도불가")
                            print(f"매수가능여부 - {op_mode14} - 매수가능-매도불가")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################


            ###############################
            # 코인15

            # 코인별 금액 비율조정
            sell_bpAve15 = bpAve * bpPer15

            # MACD 조건문
            if macd15 < 0:     # macd가 0보다 작을때는 매도
                if coinMode15 == 1 or coinMode15 == 3:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = 매수만가능 , 3 = >>>매도만가능<<<
                    if op_mode15 == 1 or op_mode15 == 4:   # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                        print("")
                        print(f"[ 15. 매도시간 : {now}  |  코인명 : {coin15}  |  현재가 = ￦{price15}  |  MACD = ￦{macd15}  |  보유수량 = {krw_balance15}  |  평가금액 = ￦{bp15}  ||  매도평균금액 = ￦{sell_bpAve15} ]")

                        if bp15 > sell_bpAve15: # 보유금액이 평균가보다 높을때
                            # 매도할 코인 금액 = 코인보유금액 - 평균가
                            sell_krw_price15 = bp15 - sell_bpAve15

                            if sell_krw_price15 >= 10000:    # 매도할 금액이 ￦10,000 보다 높을때 매도
                                # 매도할 코인 갯수 = 매도할 코인 금액 - 현재가
                                sell_krw_balance15 = sell_krw_price15 / price15

                                # 보유코인 초과금액 매도시도
                                # 매도할 코인명 - krw_coin15, 매도할 코인수량 - sell_krw_balance15
                                upbit.sell_market_order(krw_coin15, sell_krw_balance15)

                                # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                op_mode15 = 2

                                print("평균 이상 금액 매도")
                                print(f"매도한금액 = ￦{sell_krw_price15}  |  매도한수량 = {sell_krw_balance15}  |  매수가능여부 - {op_mode15} - 매수가능-매도불가")
                                print("")
                            else:
                                # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                op_mode15 = 2

                                print("￦10,000 이하 금액 매도불가")
                                print(f"매수가능여부 - {op_mode15} - 매수가능-매도불가")
                                print("")

                        else:
                            # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                            op_mode15 = 2

                            print("평균 이하 금액 매도불가")
                            print(f"매수가능여부 - {op_mode15} - 매수가능-매도불가")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################


            ###############################
            # 코인16

            # 코인별 금액 비율조정
            sell_bpAve16 = bpAve * bpPer16

            # MACD 조건문
            if macd16 < 0:     # macd가 0보다 작을때는 매도
                if coinMode16 == 1 or coinMode16 == 3:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = 매수만가능 , 3 = >>>매도만가능<<<
                    if op_mode16 == 1 or op_mode16 == 4:   # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                        print("")
                        print(f"[ 16. 매도시간 : {now}  |  코인명 : {coin16}  |  현재가 = ￦{price16}  |  MACD = ￦{macd16}  |  보유수량 = {krw_balance16}  |  평가금액 = ￦{bp16}  ||  매도평균금액 = ￦{sell_bpAve16} ]")

                        if bp16 > sell_bpAve16: # 보유금액이 평균가보다 높을때
                            # 매도할 코인 금액 = 코인보유금액 - 평균가
                            sell_krw_price16 = bp16 - sell_bpAve16

                            if sell_krw_price16 >= 10000:    # 매도할 금액이 ￦10,000 보다 높을때 매도
                                # 매도할 코인 갯수 = 매도할 코인 금액 - 현재가
                                sell_krw_balance16 = sell_krw_price16 / price16

                                # 보유코인 초과금액 매도시도
                                # 매도할 코인명 - krw_coin16, 매도할 코인수량 - sell_krw_balance16
                                upbit.sell_market_order(krw_coin16, sell_krw_balance16)

                                # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                op_mode16 = 2

                                print("평균 이상 금액 매도")
                                print(f"매도한금액 = ￦{sell_krw_price16}  |  매도한수량 = {sell_krw_balance16}  |  매수가능여부 - {op_mode16} - 매수가능-매도불가")
                                print("")
                            else:
                                # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                op_mode16 = 2

                                print("￦10,000 이하 금액 매도불가")
                                print(f"매수가능여부 - {op_mode16} - 매수가능-매도불가")
                                print("")

                        else:
                            # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                            op_mode16 = 2

                            print("평균 이하 금액 매도불가")
                            print(f"매수가능여부 - {op_mode16} - 매수가능-매도불가")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################


            ###############################
            # 코인17

            # 코인별 금액 비율조정
            sell_bpAve17 = bpAve * bpPer17

            # MACD 조건문
            if macd17 < 0:     # macd가 0보다 작을때는 매도
                if coinMode17 == 1 or coinMode17 == 3:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = 매수만가능 , 3 = >>>매도만가능<<<
                    if op_mode17 == 1 or op_mode17 == 4:   # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                        print("")
                        print(f"[ 17. 매도시간 : {now}  |  코인명 : {coin17}  |  현재가 = ￦{price17}  |  MACD = ￦{macd17}  |  보유수량 = {krw_balance17}  |  평가금액 = ￦{bp17}  ||  매도평균금액 = ￦{sell_bpAve17} ]")

                        if bp17 > sell_bpAve17: # 보유금액이 평균가보다 높을때
                            # 매도할 코인 금액 = 코인보유금액 - 평균가
                            sell_krw_price17 = bp17 - sell_bpAve17

                            if sell_krw_price17 >= 10000:    # 매도할 금액이 ￦10,000 보다 높을때 매도
                                # 매도할 코인 갯수 = 매도할 코인 금액 - 현재가
                                sell_krw_balance17 = sell_krw_price17 / price17

                                # 보유코인 초과금액 매도시도
                                # 매도할 코인명 - krw_coin17, 매도할 코인수량 - sell_krw_balance17
                                upbit.sell_market_order(krw_coin17, sell_krw_balance17)

                                # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                op_mode17 = 2

                                print("평균 이상 금액 매도")
                                print(f"매도한금액 = ￦{sell_krw_price17}  |  매도한수량 = {sell_krw_balance17}  |  매수가능여부 - {op_mode17} - 매수가능-매도불가")
                                print("")
                            else:
                                # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                op_mode17 = 2

                                print("￦10,000 이하 금액 매도불가")
                                print(f"매수가능여부 - {op_mode17} - 매수가능-매도불가")
                                print("")

                        else:
                            # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                            op_mode17 = 2

                            print("평균 이하 금액 매도불가")
                            print(f"매수가능여부 - {op_mode17} - 매수가능-매도불가")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################


            ###############################
            # 코인18

            # 코인별 금액 비율조정
            sell_bpAve18 = bpAve * bpPer18

            # MACD 조건문
            if macd18 < 0:     # macd가 0보다 작을때는 매도
                if coinMode18 == 1 or coinMode18 == 3:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = 매수만가능 , 3 = >>>매도만가능<<<
                    if op_mode18 == 1 or op_mode18 == 4:   # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                        print("")
                        print(f"[ 18. 매도시간 : {now}  |  코인명 : {coin18}  |  현재가 = ￦{price18}  |  MACD = ￦{macd18}  |  보유수량 = {krw_balance18}  |  평가금액 = ￦{bp18}  ||  매도평균금액 = ￦{sell_bpAve18} ]")

                        if bp18 > sell_bpAve18: # 보유금액이 평균가보다 높을때
                            # 매도할 코인 금액 = 코인보유금액 - 평균가
                            sell_krw_price18 = bp18 - sell_bpAve18

                            if sell_krw_price18 >= 10000:    # 매도할 금액이 ￦10,000 보다 높을때 매도
                                # 매도할 코인 갯수 = 매도할 코인 금액 - 현재가
                                sell_krw_balance18 = sell_krw_price18 / price18

                                # 보유코인 초과금액 매도시도
                                # 매도할 코인명 - krw_coin18, 매도할 코인수량 - sell_krw_balance18
                                upbit.sell_market_order(krw_coin18, sell_krw_balance18)

                                # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                op_mode18 = 2

                                print("평균 이상 금액 매도")
                                print(f"매도한금액 = ￦{sell_krw_price18}  |  매도한수량 = {sell_krw_balance18}  |  매수가능여부 - {op_mode18} - 매수가능-매도불가")
                                print("")
                            else:
                                # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                op_mode18 = 2

                                print("￦10,000 이하 금액 매도불가")
                                print(f"매수가능여부 - {op_mode18} - 매수가능-매도불가")
                                print("")

                        else:
                            # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                            op_mode18 = 2

                            print("평균 이하 금액 매도불가")
                            print(f"매수가능여부 - {op_mode18} - 매수가능-매도불가")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################


            ###############################
            # 코인19

            # 코인별 금액 비율조정
            sell_bpAve19 = bpAve * bpPer19

            # MACD 조건문
            if macd19 < 0:     # macd가 0보다 작을때는 매도
                if coinMode19 == 1 or coinMode19 == 3:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = 매수만가능 , 3 = >>>매도만가능<<<
                    if op_mode19 == 1 or op_mode19 == 4:   # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                        print("")
                        print(f"[ 19. 매도시간 : {now}  |  코인명 : {coin19}  |  현재가 = ￦{price19}  |  MACD = ￦{macd19}  |  보유수량 = {krw_balance19}  |  평가금액 = ￦{bp19}  ||  매도평균금액 = ￦{sell_bpAve19} ]")

                        if bp19 > sell_bpAve19: # 보유금액이 평균가보다 높을때
                            # 매도할 코인 금액 = 코인보유금액 - 평균가
                            sell_krw_price19 = bp19 - sell_bpAve19

                            if sell_krw_price19 >= 10000:    # 매도할 금액이 ￦10,000 보다 높을때 매도
                                # 매도할 코인 갯수 = 매도할 코인 금액 - 현재가
                                sell_krw_balance19 = sell_krw_price19 / price19

                                # 보유코인 초과금액 매도시도
                                # 매도할 코인명 - krw_coin19, 매도할 코인수량 - sell_krw_balance19
                                upbit.sell_market_order(krw_coin19, sell_krw_balance19)

                                # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                op_mode19 = 2

                                print("평균 이상 금액 매도")
                                print(f"매도한금액 = ￦{sell_krw_price19}  |  매도한수량 = {sell_krw_balance19}  |  매수가능여부 - {op_mode19} - 매수가능-매도불가")
                                print("")
                            else:
                                # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                op_mode19 = 2

                                print("￦10,000 이하 금액 매도불가")
                                print(f"매수가능여부 - {op_mode19} - 매수가능-매도불가")
                                print("")

                        else:
                            # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                            op_mode19 = 2

                            print("평균 이하 금액 매도불가")
                            print(f"매수가능여부 - {op_mode19} - 매수가능-매도불가")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################


            ###############################
            # 코인20

            # 코인별 금액 비율조정
            sell_bpAve20 = bpAve * bpPer20

            # MACD 조건문
            if macd20 < 0:     # macd가 0보다 작을때는 매도
                if coinMode20 == 1 or coinMode20 == 3:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = 매수만가능 , 3 = >>>매도만가능<<<
                    if op_mode20 == 1 or op_mode20 == 4:   # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                        print("")
                        print(f"[ 20. 매도시간 : {now}  |  코인명 : {coin20}  |  현재가 = ￦{price20}  |  MACD = ￦{macd20}  |  보유수량 = {krw_balance20}  |  평가금액 = ￦{bp20}  ||  매도평균금액 = ￦{sell_bpAve20} ]")

                        if bp20 > sell_bpAve20: # 보유금액이 평균가보다 높을때
                            # 매도할 코인 금액 = 코인보유금액 - 평균가
                            sell_krw_price20 = bp20 - sell_bpAve20

                            if sell_krw_price20 >= 10000:    # 매도할 금액이 ￦10,000 보다 높을때 매도
                                # 매도할 코인 갯수 = 매도할 코인 금액 - 현재가
                                sell_krw_balance20 = sell_krw_price20 / price20

                                # 보유코인 초과금액 매도시도
                                # 매도할 코인명 - krw_coin20, 매도할 코인수량 - sell_krw_balance20
                                upbit.sell_market_order(krw_coin20, sell_krw_balance20)

                                # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                op_mode20 = 2

                                print("평균 이상 금액 매도")
                                print(f"매도한금액 = ￦{sell_krw_price20}  |  매도한수량 = {sell_krw_balance20}  |  매수가능여부 - {op_mode20} - 매수가능-매도불가")
                                print("")
                            else:
                                # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                op_mode20 = 2

                                print("￦10,000 이하 금액 매도불가")
                                print(f"매수가능여부 - {op_mode20} - 매수가능-매도불가")
                                print("")

                        else:
                            # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                            op_mode20 = 2

                            print("평균 이하 금액 매도불가")
                            print(f"매수가능여부 - {op_mode20} - 매수가능-매도불가")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################





            ######################################################################################################################################################
            ######################################################################################################################################################
            ######################################################################################################################################################





            ###############################
            # 코인21

            # 코인별 금액 비율조정
            sell_bpAve21 = bpAve * bpPer21

            # MACD 조건문
            if macd21 < 0:     # macd가 0보다 작을때는 매도
                if coinMode21 == 1 or coinMode21 == 3:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = 매수만가능 , 3 = >>>매도만가능<<<
                    if op_mode21 == 1 or op_mode21 == 4:   # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                        print("")
                        print(f"[ 21. 매도시간 : {now}  |  코인명 : {coin21}  |  현재가 = ￦{price21}  |  MACD = ￦{macd21}  |  보유수량 = {krw_balance21}  |  평가금액 = ￦{bp21}  ||  매도평균금액 = ￦{sell_bpAve21} ]")

                        if bp21 > sell_bpAve21: # 보유금액이 평균가보다 높을때
                            # 매도할 코인 금액 = 코인보유금액 - 평균가
                            sell_krw_price21 = bp21 - sell_bpAve21

                            if sell_krw_price21 >= 10000:    # 매도할 금액이 ￦10,000 보다 높을때 매도
                                # 매도할 코인 갯수 = 매도할 코인 금액 - 현재가
                                sell_krw_balance21 = sell_krw_price21 / price21

                                # 보유코인 초과금액 매도시도
                                # 매도할 코인명 - krw_coin21, 매도할 코인수량 - sell_krw_balance21
                                upbit.sell_market_order(krw_coin21, sell_krw_balance21)

                                # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                op_mode21 = 2

                                print("평균 이상 금액 매도")
                                print(f"매도한금액 = ￦{sell_krw_price21}  |  매도한수량 = {sell_krw_balance21}  |  매수가능여부 - {op_mode21} - 매수가능-매도불가")
                                print("")
                            else:
                                # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                op_mode21 = 2

                                print("￦10,000 이하 금액 매도불가")
                                print(f"매수가능여부 - {op_mode21} - 매수가능-매도불가")
                                print("")

                        else:
                            # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                            op_mode21 = 2

                            print("평균 이하 금액 매도불가")
                            print(f"매수가능여부 - {op_mode21} - 매수가능-매도불가")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################


            ###############################
            # 코인22

            # 코인별 금액 비율조정
            sell_bpAve22 = bpAve * bpPer22

            # MACD 조건문
            if macd22 < 0:     # macd가 0보다 작을때는 매도
                if coinMode22 == 1 or coinMode22 == 3:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = 매수만가능 , 3 = >>>매도만가능<<<
                    if op_mode22 == 1 or op_mode22 == 4:   # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                        print("")
                        print(f"[ 22. 매도시간 : {now}  |  코인명 : {coin22}  |  현재가 = ￦{price22}  |  MACD = ￦{macd22}  |  보유수량 = {krw_balance22}  |  평가금액 = ￦{bp22}  ||  매도평균금액 = ￦{sell_bpAve22} ]")

                        if bp22 > sell_bpAve22: # 보유금액이 평균가보다 높을때
                            # 매도할 코인 금액 = 코인보유금액 - 평균가
                            sell_krw_price22 = bp22 - sell_bpAve22

                            if sell_krw_price22 >= 10000:    # 매도할 금액이 ￦10,000 보다 높을때 매도
                                # 매도할 코인 갯수 = 매도할 코인 금액 - 현재가
                                sell_krw_balance22 = sell_krw_price22 / price22

                                # 보유코인 초과금액 매도시도
                                # 매도할 코인명 - krw_coin22, 매도할 코인수량 - sell_krw_balance22
                                upbit.sell_market_order(krw_coin22, sell_krw_balance22)

                                # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                op_mode22 = 2

                                print("평균 이상 금액 매도")
                                print(f"매도한금액 = ￦{sell_krw_price22}  |  매도한수량 = {sell_krw_balance22}  |  매수가능여부 - {op_mode22} - 매수가능-매도불가")
                                print("")
                            else:
                                # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                op_mode22 = 2

                                print("￦10,000 이하 금액 매도불가")
                                print(f"매수가능여부 - {op_mode22} - 매수가능-매도불가")
                                print("")

                        else:
                            # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                            op_mode22 = 2

                            print("평균 이하 금액 매도불가")
                            print(f"매수가능여부 - {op_mode22} - 매수가능-매도불가")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################


            ###############################
            # 코인23

            # 코인별 금액 비율조정
            sell_bpAve23 = bpAve * bpPer23

            # MACD 조건문
            if macd23 < 0:     # macd가 0보다 작을때는 매도
                if coinMode23 == 1 or coinMode23 == 3:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = 매수만가능 , 3 = >>>매도만가능<<<
                    if op_mode23 == 1 or op_mode23 == 4:   # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                        print("")
                        print(f"[ 23. 매도시간 : {now}  |  코인명 : {coin23}  |  현재가 = ￦{price23}  |  MACD = ￦{macd23}  |  보유수량 = {krw_balance23}  |  평가금액 = ￦{bp23}  ||  매도평균금액 = ￦{sell_bpAve23} ]")

                        if bp23 > sell_bpAve23: # 보유금액이 평균가보다 높을때
                            # 매도할 코인 금액 = 코인보유금액 - 평균가
                            sell_krw_price23 = bp23 - sell_bpAve23

                            if sell_krw_price23 >= 10000:    # 매도할 금액이 ￦10,000 보다 높을때 매도
                                # 매도할 코인 갯수 = 매도할 코인 금액 - 현재가
                                sell_krw_balance23 = sell_krw_price23 / price23

                                # 보유코인 초과금액 매도시도
                                # 매도할 코인명 - krw_coin23, 매도할 코인수량 - sell_krw_balance23
                                upbit.sell_market_order(krw_coin23, sell_krw_balance23)

                                # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                op_mode23 = 2

                                print("평균 이상 금액 매도")
                                print(f"매도한금액 = ￦{sell_krw_price23}  |  매도한수량 = {sell_krw_balance23}  |  매수가능여부 - {op_mode23} - 매수가능-매도불가")
                                print("")
                            else:
                                # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                op_mode23 = 2

                                print("￦10,000 이하 금액 매도불가")
                                print(f"매수가능여부 - {op_mode23} - 매수가능-매도불가")
                                print("")

                        else:
                            # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                            op_mode23 = 2

                            print("평균 이하 금액 매도불가")
                            print(f"매수가능여부 - {op_mode23} - 매수가능-매도불가")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################


            ###############################
            # 코인24

            # 코인별 금액 비율조정
            sell_bpAve24 = bpAve * bpPer24

            # MACD 조건문
            if macd24 < 0:     # macd가 0보다 작을때는 매도
                if coinMode24 == 1 or coinMode24 == 3:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = 매수만가능 , 3 = >>>매도만가능<<<
                    if op_mode24 == 1 or op_mode24 == 4:   # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                        print("")
                        print(f"[ 24. 매도시간 : {now}  |  코인명 : {coin24}  |  현재가 = ￦{price24}  |  MACD = ￦{macd24}  |  보유수량 = {krw_balance24}  |  평가금액 = ￦{bp24}  ||  매도평균금액 = ￦{sell_bpAve24} ]")

                        if bp24 > sell_bpAve24: # 보유금액이 평균가보다 높을때
                            # 매도할 코인 금액 = 코인보유금액 - 평균가
                            sell_krw_price24 = bp24 - sell_bpAve24

                            if sell_krw_price24 >= 10000:    # 매도할 금액이 ￦10,000 보다 높을때 매도
                                # 매도할 코인 갯수 = 매도할 코인 금액 - 현재가
                                sell_krw_balance24 = sell_krw_price24 / price24

                                # 보유코인 초과금액 매도시도
                                # 매도할 코인명 - krw_coin24, 매도할 코인수량 - sell_krw_balance24
                                upbit.sell_market_order(krw_coin24, sell_krw_balance24)

                                # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                op_mode24 = 2

                                print("평균 이상 금액 매도")
                                print(f"매도한금액 = ￦{sell_krw_price24}  |  매도한수량 = {sell_krw_balance24}  |  매수가능여부 - {op_mode24} - 매수가능-매도불가")
                                print("")
                            else:
                                # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                op_mode24 = 2

                                print("￦10,000 이하 금액 매도불가")
                                print(f"매수가능여부 - {op_mode24} - 매수가능-매도불가")
                                print("")

                        else:
                            # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                            op_mode24 = 2

                            print("평균 이하 금액 매도불가")
                            print(f"매수가능여부 - {op_mode24} - 매수가능-매도불가")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################


            ###############################
            # 코인25

            # 코인별 금액 비율조정
            sell_bpAve25 = bpAve * bpPer25

            # MACD 조건문
            if macd25 < 0:     # macd가 0보다 작을때는 매도
                if coinMode25 == 1 or coinMode25 == 3:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = 매수만가능 , 3 = >>>매도만가능<<<
                    if op_mode25 == 1 or op_mode25 == 4:   # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                        print("")
                        print(f"[ 25. 매도시간 : {now}  |  코인명 : {coin25}  |  현재가 = ￦{price25}  |  MACD = ￦{macd25}  |  보유수량 = {krw_balance25}  |  평가금액 = ￦{bp25}  ||  매도평균금액 = ￦{sell_bpAve25} ]")

                        if bp25 > sell_bpAve25: # 보유금액이 평균가보다 높을때
                            # 매도할 코인 금액 = 코인보유금액 - 평균가
                            sell_krw_price25 = bp25 - sell_bpAve25

                            if sell_krw_price25 >= 10000:    # 매도할 금액이 ￦10,000 보다 높을때 매도
                                # 매도할 코인 갯수 = 매도할 코인 금액 - 현재가
                                sell_krw_balance25 = sell_krw_price25 / price25

                                # 보유코인 초과금액 매도시도
                                # 매도할 코인명 - krw_coin25, 매도할 코인수량 - sell_krw_balance25
                                upbit.sell_market_order(krw_coin25, sell_krw_balance25)

                                # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                op_mode25 = 2

                                print("평균 이상 금액 매도")
                                print(f"매도한금액 = ￦{sell_krw_price25}  |  매도한수량 = {sell_krw_balance25}  |  매수가능여부 - {op_mode25} - 매수가능-매도불가")
                                print("")
                            else:
                                # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                op_mode25 = 2

                                print("￦10,000 이하 금액 매도불가")
                                print(f"매수가능여부 - {op_mode25} - 매수가능-매도불가")
                                print("")

                        else:
                            # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                            op_mode25 = 2

                            print("평균 이하 금액 매도불가")
                            print(f"매수가능여부 - {op_mode25} - 매수가능-매도불가")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################


            ###############################
            # 코인26

            # 코인별 금액 비율조정
            sell_bpAve26 = bpAve * bpPer26

            # MACD 조건문
            if macd26 < 0:     # macd가 0보다 작을때는 매도
                if coinMode26 == 1 or coinMode26 == 3:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = 매수만가능 , 3 = >>>매도만가능<<<
                    if op_mode26 == 1 or op_mode26 == 4:   # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                        print("")
                        print(f"[ 26. 매도시간 : {now}  |  코인명 : {coin26}  |  현재가 = ￦{price26}  |  MACD = ￦{macd26}  |  보유수량 = {krw_balance26}  |  평가금액 = ￦{bp26}  ||  매도평균금액 = ￦{sell_bpAve26} ]")

                        if bp26 > sell_bpAve26: # 보유금액이 평균가보다 높을때
                            # 매도할 코인 금액 = 코인보유금액 - 평균가
                            sell_krw_price26 = bp26 - sell_bpAve26

                            if sell_krw_price26 >= 10000:    # 매도할 금액이 ￦10,000 보다 높을때 매도
                                # 매도할 코인 갯수 = 매도할 코인 금액 - 현재가
                                sell_krw_balance26 = sell_krw_price26 / price26

                                # 보유코인 초과금액 매도시도
                                # 매도할 코인명 - krw_coin26, 매도할 코인수량 - sell_krw_balance26
                                upbit.sell_market_order(krw_coin26, sell_krw_balance26)

                                # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                op_mode26 = 2

                                print("평균 이상 금액 매도")
                                print(f"매도한금액 = ￦{sell_krw_price26}  |  매도한수량 = {sell_krw_balance26}  |  매수가능여부 - {op_mode26} - 매수가능-매도불가")
                                print("")
                            else:
                                # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                op_mode26 = 2

                                print("￦10,000 이하 금액 매도불가")
                                print(f"매수가능여부 - {op_mode26} - 매수가능-매도불가")
                                print("")

                        else:
                            # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                            op_mode26 = 2

                            print("평균 이하 금액 매도불가")
                            print(f"매수가능여부 - {op_mode26} - 매수가능-매도불가")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################


            ###############################
            # 코인27

            # 코인별 금액 비율조정
            sell_bpAve27 = bpAve * bpPer27

            # MACD 조건문
            if macd27 < 0:     # macd가 0보다 작을때는 매도
                if coinMode27 == 1 or coinMode27 == 3:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = 매수만가능 , 3 = >>>매도만가능<<<
                    if op_mode27 == 1 or op_mode27 == 4:   # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                        print("")
                        print(f"[ 27. 매도시간 : {now}  |  코인명 : {coin27}  |  현재가 = ￦{price27}  |  MACD = ￦{macd27}  |  보유수량 = {krw_balance27}  |  평가금액 = ￦{bp27}  ||  매도평균금액 = ￦{sell_bpAve27} ]")

                        if bp27 > sell_bpAve27: # 보유금액이 평균가보다 높을때
                            # 매도할 코인 금액 = 코인보유금액 - 평균가
                            sell_krw_price27 = bp27 - sell_bpAve27

                            if sell_krw_price27 >= 10000:    # 매도할 금액이 ￦10,000 보다 높을때 매도
                                # 매도할 코인 갯수 = 매도할 코인 금액 - 현재가
                                sell_krw_balance27 = sell_krw_price27 / price27

                                # 보유코인 초과금액 매도시도
                                # 매도할 코인명 - krw_coin27, 매도할 코인수량 - sell_krw_balance27
                                upbit.sell_market_order(krw_coin27, sell_krw_balance27)

                                # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                op_mode27 = 2

                                print("평균 이상 금액 매도")
                                print(f"매도한금액 = ￦{sell_krw_price27}  |  매도한수량 = {sell_krw_balance27}  |  매수가능여부 - {op_mode27} - 매수가능-매도불가")
                                print("")
                            else:
                                # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                op_mode27 = 2

                                print("￦10,000 이하 금액 매도불가")
                                print(f"매수가능여부 - {op_mode27} - 매수가능-매도불가")
                                print("")

                        else:
                            # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                            op_mode27 = 2

                            print("평균 이하 금액 매도불가")
                            print(f"매수가능여부 - {op_mode27} - 매수가능-매도불가")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################


            ###############################
            # 코인28

            # 코인별 금액 비율조정
            sell_bpAve28 = bpAve * bpPer28

            # MACD 조건문
            if macd28 < 0:     # macd가 0보다 작을때는 매도
                if coinMode28 == 1 or coinMode28 == 3:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = 매수만가능 , 3 = >>>매도만가능<<<
                    if op_mode28 == 1 or op_mode28 == 4:   # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                        print("")
                        print(f"[ 28. 매도시간 : {now}  |  코인명 : {coin28}  |  현재가 = ￦{price28}  |  MACD = ￦{macd28}  |  보유수량 = {krw_balance28}  |  평가금액 = ￦{bp28}  ||  매도평균금액 = ￦{sell_bpAve28} ]")

                        if bp28 > sell_bpAve28: # 보유금액이 평균가보다 높을때
                            # 매도할 코인 금액 = 코인보유금액 - 평균가
                            sell_krw_price28 = bp28 - sell_bpAve28

                            if sell_krw_price28 >= 10000:    # 매도할 금액이 ￦10,000 보다 높을때 매도
                                # 매도할 코인 갯수 = 매도할 코인 금액 - 현재가
                                sell_krw_balance28 = sell_krw_price28 / price28

                                # 보유코인 초과금액 매도시도
                                # 매도할 코인명 - krw_coin28, 매도할 코인수량 - sell_krw_balance28
                                upbit.sell_market_order(krw_coin28, sell_krw_balance28)

                                # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                op_mode28 = 2

                                print("평균 이상 금액 매도")
                                print(f"매도한금액 = ￦{sell_krw_price28}  |  매도한수량 = {sell_krw_balance28}  |  매수가능여부 - {op_mode28} - 매수가능-매도불가")
                                print("")
                            else:
                                # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                op_mode28 = 2

                                print("￦10,000 이하 금액 매도불가")
                                print(f"매수가능여부 - {op_mode28} - 매수가능-매도불가")
                                print("")

                        else:
                            # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                            op_mode28 = 2

                            print("평균 이하 금액 매도불가")
                            print(f"매수가능여부 - {op_mode28} - 매수가능-매도불가")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################


            ###############################
            # 코인29

            # 코인별 금액 비율조정
            sell_bpAve29 = bpAve * bpPer29

            # MACD 조건문
            if macd29 < 0:     # macd가 0보다 작을때는 매도
                if coinMode29 == 1 or coinMode29 == 3:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = 매수만가능 , 3 = >>>매도만가능<<<
                    if op_mode29 == 1 or op_mode29 == 4:   # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                        print("")
                        print(f"[ 29. 매도시간 : {now}  |  코인명 : {coin29}  |  현재가 = ￦{price29}  |  MACD = ￦{macd29}  |  보유수량 = {krw_balance29}  |  평가금액 = ￦{bp29}  ||  매도평균금액 = ￦{sell_bpAve29} ]")

                        if bp29 > sell_bpAve29: # 보유금액이 평균가보다 높을때
                            # 매도할 코인 금액 = 코인보유금액 - 평균가
                            sell_krw_price29 = bp29 - sell_bpAve29

                            if sell_krw_price29 >= 10000:    # 매도할 금액이 ￦10,000 보다 높을때 매도
                                # 매도할 코인 갯수 = 매도할 코인 금액 - 현재가
                                sell_krw_balance29 = sell_krw_price29 / price29

                                # 보유코인 초과금액 매도시도
                                # 매도할 코인명 - krw_coin29, 매도할 코인수량 - sell_krw_balance29
                                upbit.sell_market_order(krw_coin29, sell_krw_balance29)

                                # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                op_mode29 = 2

                                print("평균 이상 금액 매도")
                                print(f"매도한금액 = ￦{sell_krw_price29}  |  매도한수량 = {sell_krw_balance29}  |  매수가능여부 - {op_mode29} - 매수가능-매도불가")
                                print("")
                            else:
                                # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                op_mode29 = 2

                                print("￦10,000 이하 금액 매도불가")
                                print(f"매수가능여부 - {op_mode29} - 매수가능-매도불가")
                                print("")

                        else:
                            # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                            op_mode29 = 2

                            print("평균 이하 금액 매도불가")
                            print(f"매수가능여부 - {op_mode29} - 매수가능-매도불가")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################


            ###############################
            # 코인30

            # 코인별 금액 비율조정
            sell_bpAve30 = bpAve * bpPer30

            # MACD 조건문
            if macd30 < 0:     # macd가 0보다 작을때는 매도
                if coinMode30 == 1 or coinMode30 == 3:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = 매수만가능 , 3 = >>>매도만가능<<<
                    if op_mode30 == 1 or op_mode30 == 4:   # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                        print("")
                        print(f"[ 30. 매도시간 : {now}  |  코인명 : {coin30}  |  현재가 = ￦{price30}  |  MACD = ￦{macd30}  |  보유수량 = {krw_balance30}  |  평가금액 = ￦{bp30}  ||  매도평균금액 = ￦{sell_bpAve30} ]")

                        if bp30 > sell_bpAve30: # 보유금액이 평균가보다 높을때
                            # 매도할 코인 금액 = 코인보유금액 - 평균가
                            sell_krw_price30 = bp30 - sell_bpAve30

                            if sell_krw_price30 >= 10000:    # 매도할 금액이 ￦10,000 보다 높을때 매도
                                # 매도할 코인 갯수 = 매도할 코인 금액 - 현재가
                                sell_krw_balance30 = sell_krw_price30 / price30

                                # 보유코인 초과금액 매도시도
                                # 매도할 코인명 - krw_coin30, 매도할 코인수량 - sell_krw_balance30
                                upbit.sell_market_order(krw_coin30, sell_krw_balance30)

                                # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                op_mode30 = 2

                                print("평균 이상 금액 매도")
                                print(f"매도한금액 = ￦{sell_krw_price30}  |  매도한수량 = {sell_krw_balance30}  |  매수가능여부 - {op_mode30} - 매수가능-매도불가")
                                print("")
                            else:
                                # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                op_mode30 = 2

                                print("￦10,000 이하 금액 매도불가")
                                print(f"매수가능여부 - {op_mode30} - 매수가능-매도불가")
                                print("")

                        else:
                            # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                            op_mode30 = 2

                            print("평균 이하 금액 매도불가")
                            print(f"매수가능여부 - {op_mode30} - 매수가능-매도불가")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################





            ######################################################################################################################################################
            ######################################################################################################################################################
            ######################################################################################################################################################
            




            ###############################
            # 코인31

            # 코인별 금액 비율조정
            sell_bpAve31 = bpAve * bpPer31

            # MACD 조건문
            if macd31 < 0:     # macd가 0보다 작을때는 매도
                if coinMode31 == 1 or coinMode31 == 3:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = 매수만가능 , 3 = >>>매도만가능<<<
                    if op_mode31 == 1 or op_mode31 == 4:   # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                        print("")
                        print(f"[ 31. 매도시간 : {now}  |  코인명 : {coin31}  |  현재가 = ￦{price31}  |  MACD = ￦{macd31}  |  보유수량 = {krw_balance31}  |  평가금액 = ￦{bp31}  ||  매도평균금액 = ￦{sell_bpAve31} ]")

                        if bp31 > sell_bpAve31: # 보유금액이 평균가보다 높을때
                            # 매도할 코인 금액 = 코인보유금액 - 평균가
                            sell_krw_price31 = bp31 - sell_bpAve31

                            if sell_krw_price31 >= 10000:    # 매도할 금액이 ￦10,000 보다 높을때 매도
                                # 매도할 코인 갯수 = 매도할 코인 금액 - 현재가
                                sell_krw_balance31 = sell_krw_price31 / price31

                                # 보유코인 초과금액 매도시도
                                # 매도할 코인명 - krw_coin31, 매도할 코인수량 - sell_krw_balance31
                                upbit.sell_market_order(krw_coin31, sell_krw_balance31)

                                # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                op_mode31 = 2

                                print("평균 이상 금액 매도")
                                print(f"매도한금액 = ￦{sell_krw_price31}  |  매도한수량 = {sell_krw_balance31}  |  매수가능여부 - {op_mode31} - 매수가능-매도불가")
                                print("")
                            else:
                                # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                op_mode31 = 2

                                print("￦10,000 이하 금액 매도불가")
                                print(f"매수가능여부 - {op_mode31} - 매수가능-매도불가")
                                print("")

                        else:
                            # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                            op_mode31 = 2

                            print("평균 이하 금액 매도불가")
                            print(f"매수가능여부 - {op_mode31} - 매수가능-매도불가")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################


            ###############################
            # 코인32

            # 코인별 금액 비율조정
            sell_bpAve32 = bpAve * bpPer32

            # MACD 조건문
            if macd32 < 0:     # macd가 0보다 작을때는 매도
                if coinMode32 == 1 or coinMode32 == 3:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = 매수만가능 , 3 = >>>매도만가능<<<
                    if op_mode32 == 1 or op_mode32 == 4:   # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                        print("")
                        print(f"[ 32. 매도시간 : {now}  |  코인명 : {coin32}  |  현재가 = ￦{price32}  |  MACD = ￦{macd32}  |  보유수량 = {krw_balance32}  |  평가금액 = ￦{bp32}  ||  매도평균금액 = ￦{sell_bpAve32} ]")

                        if bp32 > sell_bpAve32: # 보유금액이 평균가보다 높을때
                            # 매도할 코인 금액 = 코인보유금액 - 평균가
                            sell_krw_price32 = bp32 - sell_bpAve32

                            if sell_krw_price32 >= 10000:    # 매도할 금액이 ￦10,000 보다 높을때 매도
                                # 매도할 코인 갯수 = 매도할 코인 금액 - 현재가
                                sell_krw_balance32 = sell_krw_price32 / price32

                                # 보유코인 초과금액 매도시도
                                # 매도할 코인명 - krw_coin32, 매도할 코인수량 - sell_krw_balance32
                                upbit.sell_market_order(krw_coin32, sell_krw_balance32)

                                # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                op_mode32 = 2

                                print("평균 이상 금액 매도")
                                print(f"매도한금액 = ￦{sell_krw_price32}  |  매도한수량 = {sell_krw_balance32}  |  매수가능여부 - {op_mode32} - 매수가능-매도불가")
                                print("")
                            else:
                                # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                op_mode32 = 2

                                print("￦10,000 이하 금액 매도불가")
                                print(f"매수가능여부 - {op_mode32} - 매수가능-매도불가")
                                print("")

                        else:
                            # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                            op_mode32 = 2

                            print("평균 이하 금액 매도불가")
                            print(f"매수가능여부 - {op_mode32} - 매수가능-매도불가")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################


            ###############################
            # 코인33

            # 코인별 금액 비율조정
            sell_bpAve33 = bpAve * bpPer33

            # MACD 조건문
            if macd33 < 0:     # macd가 0보다 작을때는 매도
                if coinMode33 == 1 or coinMode33 == 3:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = 매수만가능 , 3 = >>>매도만가능<<<
                    if op_mode33 == 1 or op_mode33 == 4:   # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                        print("")
                        print(f"[ 33. 매도시간 : {now}  |  코인명 : {coin33}  |  현재가 = ￦{price33}  |  MACD = ￦{macd33}  |  보유수량 = {krw_balance33}  |  평가금액 = ￦{bp33}  ||  매도평균금액 = ￦{sell_bpAve33} ]")

                        if bp33 > sell_bpAve33: # 보유금액이 평균가보다 높을때
                            # 매도할 코인 금액 = 코인보유금액 - 평균가
                            sell_krw_price33 = bp33 - sell_bpAve33

                            if sell_krw_price33 >= 10000:    # 매도할 금액이 ￦10,000 보다 높을때 매도
                                # 매도할 코인 갯수 = 매도할 코인 금액 - 현재가
                                sell_krw_balance33 = sell_krw_price33 / price33

                                # 보유코인 초과금액 매도시도
                                # 매도할 코인명 - krw_coin33, 매도할 코인수량 - sell_krw_balance33
                                upbit.sell_market_order(krw_coin33, sell_krw_balance33)

                                # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                op_mode33 = 2

                                print("평균 이상 금액 매도")
                                print(f"매도한금액 = ￦{sell_krw_price33}  |  매도한수량 = {sell_krw_balance33}  |  매수가능여부 - {op_mode33} - 매수가능-매도불가")
                                print("")
                            else:
                                # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                op_mode33 = 2

                                print("￦10,000 이하 금액 매도불가")
                                print(f"매수가능여부 - {op_mode33} - 매수가능-매도불가")
                                print("")

                        else:
                            # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                            op_mode33 = 2

                            print("평균 이하 금액 매도불가")
                            print(f"매수가능여부 - {op_mode33} - 매수가능-매도불가")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################


            ###############################
            # 코인34

            # 코인별 금액 비율조정
            sell_bpAve34 = bpAve * bpPer34

            # MACD 조건문
            if macd34 < 0:     # macd가 0보다 작을때는 매도
                if coinMode34 == 1 or coinMode34 == 3:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = 매수만가능 , 3 = >>>매도만가능<<<
                    if op_mode34 == 1 or op_mode34 == 4:   # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                        print("")
                        print(f"[ 34. 매도시간 : {now}  |  코인명 : {coin34}  |  현재가 = ￦{price34}  |  MACD = ￦{macd34}  |  보유수량 = {krw_balance34}  |  평가금액 = ￦{bp34}  ||  매도평균금액 = ￦{sell_bpAve34} ]")

                        if bp34 > sell_bpAve34: # 보유금액이 평균가보다 높을때
                            # 매도할 코인 금액 = 코인보유금액 - 평균가
                            sell_krw_price34 = bp34 - sell_bpAve34

                            if sell_krw_price34 >= 10000:    # 매도할 금액이 ￦10,000 보다 높을때 매도
                                # 매도할 코인 갯수 = 매도할 코인 금액 - 현재가
                                sell_krw_balance34 = sell_krw_price34 / price34

                                # 보유코인 초과금액 매도시도
                                # 매도할 코인명 - krw_coin34, 매도할 코인수량 - sell_krw_balance34
                                upbit.sell_market_order(krw_coin34, sell_krw_balance34)

                                # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                op_mode34 = 2

                                print("평균 이상 금액 매도")
                                print(f"매도한금액 = ￦{sell_krw_price34}  |  매도한수량 = {sell_krw_balance34}  |  매수가능여부 - {op_mode34} - 매수가능-매도불가")
                                print("")
                            else:
                                # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                op_mode34 = 2

                                print("￦10,000 이하 금액 매도불가")
                                print(f"매수가능여부 - {op_mode34} - 매수가능-매도불가")
                                print("")

                        else:
                            # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                            op_mode34 = 2

                            print("평균 이하 금액 매도불가")
                            print(f"매수가능여부 - {op_mode34} - 매수가능-매도불가")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################


            ###############################
            # 코인35

            # 코인별 금액 비율조정
            sell_bpAve35 = bpAve * bpPer35

            # MACD 조건문
            if macd35 < 0:     # macd가 0보다 작을때는 매도
                if coinMode35 == 1 or coinMode35 == 3:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = 매수만가능 , 3 = >>>매도만가능<<<
                    if op_mode35 == 1 or op_mode35 == 4:   # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                        print("")
                        print(f"[ 35. 매도시간 : {now}  |  코인명 : {coin35}  |  현재가 = ￦{price35}  |  MACD = ￦{macd35}  |  보유수량 = {krw_balance35}  |  평가금액 = ￦{bp35}  ||  매도평균금액 = ￦{sell_bpAve35} ]")

                        if bp35 > sell_bpAve35: # 보유금액이 평균가보다 높을때
                            # 매도할 코인 금액 = 코인보유금액 - 평균가
                            sell_krw_price35 = bp35 - sell_bpAve35

                            if sell_krw_price35 >= 10000:    # 매도할 금액이 ￦10,000 보다 높을때 매도
                                # 매도할 코인 갯수 = 매도할 코인 금액 - 현재가
                                sell_krw_balance35 = sell_krw_price35 / price35

                                # 보유코인 초과금액 매도시도
                                # 매도할 코인명 - krw_coin35, 매도할 코인수량 - sell_krw_balance35
                                upbit.sell_market_order(krw_coin35, sell_krw_balance35)

                                # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                op_mode35 = 2

                                print("평균 이상 금액 매도")
                                print(f"매도한금액 = ￦{sell_krw_price35}  |  매도한수량 = {sell_krw_balance35}  |  매수가능여부 - {op_mode35} - 매수가능-매도불가")
                                print("")
                            else:
                                # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                op_mode35 = 2

                                print("￦10,000 이하 금액 매도불가")
                                print(f"매수가능여부 - {op_mode35} - 매수가능-매도불가")
                                print("")

                        else:
                            # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                            op_mode35 = 2

                            print("평균 이하 금액 매도불가")
                            print(f"매수가능여부 - {op_mode35} - 매수가능-매도불가")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################


            ###############################
            # 코인36

            # 코인별 금액 비율조정
            sell_bpAve36 = bpAve * bpPer36

            # MACD 조건문
            if macd36 < 0:     # macd가 0보다 작을때는 매도
                if coinMode36 == 1 or coinMode36 == 3:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = 매수만가능 , 3 = >>>매도만가능<<<
                    if op_mode36 == 1 or op_mode36 == 4:   # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                        print("")
                        print(f"[ 36. 매도시간 : {now}  |  코인명 : {coin36}  |  현재가 = ￦{price36}  |  MACD = ￦{macd36}  |  보유수량 = {krw_balance36}  |  평가금액 = ￦{bp36}  ||  매도평균금액 = ￦{sell_bpAve36} ]")

                        if bp36 > sell_bpAve36: # 보유금액이 평균가보다 높을때
                            # 매도할 코인 금액 = 코인보유금액 - 평균가
                            sell_krw_price36 = bp36 - sell_bpAve36

                            if sell_krw_price36 >= 10000:    # 매도할 금액이 ￦10,000 보다 높을때 매도
                                # 매도할 코인 갯수 = 매도할 코인 금액 - 현재가
                                sell_krw_balance36 = sell_krw_price36 / price36

                                # 보유코인 초과금액 매도시도
                                # 매도할 코인명 - krw_coin36, 매도할 코인수량 - sell_krw_balance36
                                upbit.sell_market_order(krw_coin36, sell_krw_balance36)

                                # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                op_mode36 = 2

                                print("평균 이상 금액 매도")
                                print(f"매도한금액 = ￦{sell_krw_price36}  |  매도한수량 = {sell_krw_balance36}  |  매수가능여부 - {op_mode36} - 매수가능-매도불가")
                                print("")
                            else:
                                # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                op_mode36 = 2

                                print("￦10,000 이하 금액 매도불가")
                                print(f"매수가능여부 - {op_mode36} - 매수가능-매도불가")
                                print("")

                        else:
                            # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                            op_mode36 = 2

                            print("평균 이하 금액 매도불가")
                            print(f"매수가능여부 - {op_mode36} - 매수가능-매도불가")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################


            ###############################
            # 코인37

            # 코인별 금액 비율조정
            sell_bpAve37 = bpAve * bpPer37

            # MACD 조건문
            if macd37 < 0:     # macd가 0보다 작을때는 매도
                if coinMode37 == 1 or coinMode37 == 3:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = 매수만가능 , 3 = >>>매도만가능<<<
                    if op_mode37 == 1 or op_mode37 == 4:   # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                        print("")
                        print(f"[ 37. 매도시간 : {now}  |  코인명 : {coin37}  |  현재가 = ￦{price37}  |  MACD = ￦{macd37}  |  보유수량 = {krw_balance37}  |  평가금액 = ￦{bp37}  ||  매도평균금액 = ￦{sell_bpAve37} ]")

                        if bp37 > sell_bpAve37: # 보유금액이 평균가보다 높을때
                            # 매도할 코인 금액 = 코인보유금액 - 평균가
                            sell_krw_price37 = bp37 - sell_bpAve37

                            if sell_krw_price37 >= 10000:    # 매도할 금액이 ￦10,000 보다 높을때 매도
                                # 매도할 코인 갯수 = 매도할 코인 금액 - 현재가
                                sell_krw_balance37 = sell_krw_price37 / price37

                                # 보유코인 초과금액 매도시도
                                # 매도할 코인명 - krw_coin37, 매도할 코인수량 - sell_krw_balance37
                                upbit.sell_market_order(krw_coin37, sell_krw_balance37)

                                # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                op_mode37 = 2

                                print("평균 이상 금액 매도")
                                print(f"매도한금액 = ￦{sell_krw_price37}  |  매도한수량 = {sell_krw_balance37}  |  매수가능여부 - {op_mode37} - 매수가능-매도불가")
                                print("")
                            else:
                                # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                op_mode37 = 2

                                print("￦10,000 이하 금액 매도불가")
                                print(f"매수가능여부 - {op_mode37} - 매수가능-매도불가")
                                print("")

                        else:
                            # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                            op_mode37 = 2

                            print("평균 이하 금액 매도불가")
                            print(f"매수가능여부 - {op_mode37} - 매수가능-매도불가")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################


            ###############################
            # 코인38

            # 코인별 금액 비율조정
            sell_bpAve38 = bpAve * bpPer38

            # MACD 조건문
            if macd38 < 0:     # macd가 0보다 작을때는 매도
                if coinMode38 == 1 or coinMode38 == 3:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = 매수만가능 , 3 = >>>매도만가능<<<
                    if op_mode38 == 1 or op_mode38 == 4:   # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                        print("")
                        print(f"[ 38. 매도시간 : {now}  |  코인명 : {coin38}  |  현재가 = ￦{price38}  |  MACD = ￦{macd38}  |  보유수량 = {krw_balance38}  |  평가금액 = ￦{bp38}  ||  매도평균금액 = ￦{sell_bpAve38} ]")

                        if bp38 > sell_bpAve38: # 보유금액이 평균가보다 높을때
                            # 매도할 코인 금액 = 코인보유금액 - 평균가
                            sell_krw_price38 = bp38 - sell_bpAve38

                            if sell_krw_price38 >= 10000:    # 매도할 금액이 ￦10,000 보다 높을때 매도
                                # 매도할 코인 갯수 = 매도할 코인 금액 - 현재가
                                sell_krw_balance38 = sell_krw_price38 / price38

                                # 보유코인 초과금액 매도시도
                                # 매도할 코인명 - krw_coin38, 매도할 코인수량 - sell_krw_balance38
                                upbit.sell_market_order(krw_coin38, sell_krw_balance38)

                                # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                op_mode38 = 2

                                print("평균 이상 금액 매도")
                                print(f"매도한금액 = ￦{sell_krw_price38}  |  매도한수량 = {sell_krw_balance38}  |  매수가능여부 - {op_mode38} - 매수가능-매도불가")
                                print("")
                            else:
                                # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                op_mode38 = 2

                                print("￦10,000 이하 금액 매도불가")
                                print(f"매수가능여부 - {op_mode38} - 매수가능-매도불가")
                                print("")

                        else:
                            # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                            op_mode38 = 2

                            print("평균 이하 금액 매도불가")
                            print(f"매수가능여부 - {op_mode38} - 매수가능-매도불가")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################


            ###############################
            # 코인39

            # 코인별 금액 비율조정
            sell_bpAve39 = bpAve * bpPer39

            # MACD 조건문
            if macd39 < 0:     # macd가 0보다 작을때는 매도
                if coinMode39 == 1 or coinMode39 == 3:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = 매수만가능 , 3 = >>>매도만가능<<<
                    if op_mode39 == 1 or op_mode39 == 4:   # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                        print("")
                        print(f"[ 39. 매도시간 : {now}  |  코인명 : {coin39}  |  현재가 = ￦{price39}  |  MACD = ￦{macd39}  |  보유수량 = {krw_balance39}  |  평가금액 = ￦{bp39}  ||  매도평균금액 = ￦{sell_bpAve39} ]")

                        if bp39 > sell_bpAve39: # 보유금액이 평균가보다 높을때
                            # 매도할 코인 금액 = 코인보유금액 - 평균가
                            sell_krw_price39 = bp39 - sell_bpAve39

                            if sell_krw_price39 >= 10000:    # 매도할 금액이 ￦10,000 보다 높을때 매도
                                # 매도할 코인 갯수 = 매도할 코인 금액 - 현재가
                                sell_krw_balance39 = sell_krw_price39 / price39

                                # 보유코인 초과금액 매도시도
                                # 매도할 코인명 - krw_coin39, 매도할 코인수량 - sell_krw_balance39
                                upbit.sell_market_order(krw_coin39, sell_krw_balance39)

                                # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                op_mode39 = 2

                                print("평균 이상 금액 매도")
                                print(f"매도한금액 = ￦{sell_krw_price39}  |  매도한수량 = {sell_krw_balance39}  |  매수가능여부 - {op_mode39} - 매수가능-매도불가")
                                print("")
                            else:
                                # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                op_mode39 = 2

                                print("￦10,000 이하 금액 매도불가")
                                print(f"매수가능여부 - {op_mode39} - 매수가능-매도불가")
                                print("")

                        else:
                            # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                            op_mode39 = 2

                            print("평균 이하 금액 매도불가")
                            print(f"매수가능여부 - {op_mode39} - 매수가능-매도불가")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################


            ###############################
            # 코인40

            # 코인별 금액 비율조정
            sell_bpAve40 = bpAve * bpPer40

            # MACD 조건문
            if macd40 < 0:     # macd가 0보다 작을때는 매도
                if coinMode40 == 1 or coinMode40 == 3:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = 매수만가능 , 3 = >>>매도만가능<<<
                    if op_mode40 == 1 or op_mode40 == 4:   # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                        print("")
                        print(f"[ 40. 매도시간 : {now}  |  코인명 : {coin40}  |  현재가 = ￦{price40}  |  MACD = ￦{macd40}  |  보유수량 = {krw_balance40}  |  평가금액 = ￦{bp40}  ||  매도평균금액 = ￦{sell_bpAve40} ]")

                        if bp40 > sell_bpAve40: # 보유금액이 평균가보다 높을때
                            # 매도할 코인 금액 = 코인보유금액 - 평균가
                            sell_krw_price40 = bp40 - sell_bpAve40

                            if sell_krw_price40 >= 10000:    # 매도할 금액이 ￦10,000 보다 높을때 매도
                                # 매도할 코인 갯수 = 매도할 코인 금액 - 현재가
                                sell_krw_balance40 = sell_krw_price40 / price40

                                # 보유코인 초과금액 매도시도
                                # 매도할 코인명 - krw_coin40, 매도할 코인수량 - sell_krw_balance40
                                upbit.sell_market_order(krw_coin40, sell_krw_balance40)

                                # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                op_mode40 = 2

                                print("평균 이상 금액 매도")
                                print(f"매도한금액 = ￦{sell_krw_price40}  |  매도한수량 = {sell_krw_balance40}  |  매수가능여부 - {op_mode40} - 매수가능-매도불가")
                                print("")
                            else:
                                # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                op_mode40 = 2

                                print("￦10,000 이하 금액 매도불가")
                                print(f"매수가능여부 - {op_mode40} - 매수가능-매도불가")
                                print("")

                        else:
                            # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                            op_mode40 = 2

                            print("평균 이하 금액 매도불가")
                            print(f"매수가능여부 - {op_mode40} - 매수가능-매도불가")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################





            ######################################################################################################################################################
            ######################################################################################################################################################
            ######################################################################################################################################################
            




            ###############################
            # 코인41

            # 코인별 금액 비율조정
            sell_bpAve41 = bpAve * bpPer41

            # MACD 조건문
            if macd41 < 0:     # macd가 0보다 작을때는 매도
                if coinMode41 == 1 or coinMode41 == 3:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = 매수만가능 , 3 = >>>매도만가능<<<
                    if op_mode41 == 1 or op_mode41 == 4:   # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                        print("")
                        print(f"[ 41. 매도시간 : {now}  |  코인명 : {coin41}  |  현재가 = ￦{price41}  |  MACD = ￦{macd41}  |  보유수량 = {krw_balance41}  |  평가금액 = ￦{bp41}  ||  매도평균금액 = ￦{sell_bpAve41} ]")

                        if bp41 > sell_bpAve41: # 보유금액이 평균가보다 높을때
                            # 매도할 코인 금액 = 코인보유금액 - 평균가
                            sell_krw_price41 = bp41 - sell_bpAve41

                            if sell_krw_price41 >= 10000:    # 매도할 금액이 ￦10,000 보다 높을때 매도
                                # 매도할 코인 갯수 = 매도할 코인 금액 - 현재가
                                sell_krw_balance41 = sell_krw_price41 / price41

                                # 보유코인 초과금액 매도시도
                                # 매도할 코인명 - krw_coin41, 매도할 코인수량 - sell_krw_balance41
                                upbit.sell_market_order(krw_coin41, sell_krw_balance41)

                                # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                op_mode41 = 2

                                print("평균 이상 금액 매도")
                                print(f"매도한금액 = ￦{sell_krw_price41}  |  매도한수량 = {sell_krw_balance41}  |  매수가능여부 - {op_mode41} - 매수가능-매도불가")
                                print("")
                            else:
                                # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                op_mode41 = 2

                                print("￦10,000 이하 금액 매도불가")
                                print(f"매수가능여부 - {op_mode41} - 매수가능-매도불가")
                                print("")

                        else:
                            # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                            op_mode41 = 2

                            print("평균 이하 금액 매도불가")
                            print(f"매수가능여부 - {op_mode41} - 매수가능-매도불가")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################


            ###############################
            # 코인42

            # 코인별 금액 비율조정
            sell_bpAve42 = bpAve * bpPer42

            # MACD 조건문
            if macd42 < 0:     # macd가 0보다 작을때는 매도
                if coinMode42 == 1 or coinMode42 == 3:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = 매수만가능 , 3 = >>>매도만가능<<<
                    if op_mode42 == 1 or op_mode42 == 4:   # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                        print("")
                        print(f"[ 42. 매도시간 : {now}  |  코인명 : {coin42}  |  현재가 = ￦{price42}  |  MACD = ￦{macd42}  |  보유수량 = {krw_balance42}  |  평가금액 = ￦{bp42}  ||  매도평균금액 = ￦{sell_bpAve42} ]")

                        if bp42 > sell_bpAve42: # 보유금액이 평균가보다 높을때
                            # 매도할 코인 금액 = 코인보유금액 - 평균가
                            sell_krw_price42 = bp42 - sell_bpAve42

                            if sell_krw_price42 >= 10000:    # 매도할 금액이 ￦10,000 보다 높을때 매도
                                # 매도할 코인 갯수 = 매도할 코인 금액 - 현재가
                                sell_krw_balance42 = sell_krw_price42 / price42

                                # 보유코인 초과금액 매도시도
                                # 매도할 코인명 - krw_coin42, 매도할 코인수량 - sell_krw_balance42
                                upbit.sell_market_order(krw_coin42, sell_krw_balance42)

                                # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                op_mode42 = 2

                                print("평균 이상 금액 매도")
                                print(f"매도한금액 = ￦{sell_krw_price42}  |  매도한수량 = {sell_krw_balance42}  |  매수가능여부 - {op_mode42} - 매수가능-매도불가")
                                print("")
                            else:
                                # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                op_mode42 = 2

                                print("￦10,000 이하 금액 매도불가")
                                print(f"매수가능여부 - {op_mode42} - 매수가능-매도불가")
                                print("")

                        else:
                            # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                            op_mode42 = 2

                            print("평균 이하 금액 매도불가")
                            print(f"매수가능여부 - {op_mode42} - 매수가능-매도불가")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################


            ###############################
            # 코인43

            # 코인별 금액 비율조정
            sell_bpAve43 = bpAve * bpPer43

            # MACD 조건문
            if macd43 < 0:     # macd가 0보다 작을때는 매도
                if coinMode43 == 1 or coinMode43 == 3:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = 매수만가능 , 3 = >>>매도만가능<<<
                    if op_mode43 == 1 or op_mode43 == 4:   # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                        print("")
                        print(f"[ 43. 매도시간 : {now}  |  코인명 : {coin43}  |  현재가 = ￦{price43}  |  MACD = ￦{macd43}  |  보유수량 = {krw_balance43}  |  평가금액 = ￦{bp43}  ||  매도평균금액 = ￦{sell_bpAve43} ]")

                        if bp43 > sell_bpAve43: # 보유금액이 평균가보다 높을때
                            # 매도할 코인 금액 = 코인보유금액 - 평균가
                            sell_krw_price43 = bp43 - sell_bpAve43

                            if sell_krw_price43 >= 10000:    # 매도할 금액이 ￦10,000 보다 높을때 매도
                                # 매도할 코인 갯수 = 매도할 코인 금액 - 현재가
                                sell_krw_balance43 = sell_krw_price43 / price43

                                # 보유코인 초과금액 매도시도
                                # 매도할 코인명 - krw_coin43, 매도할 코인수량 - sell_krw_balance43
                                upbit.sell_market_order(krw_coin43, sell_krw_balance43)

                                # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                op_mode43 = 2

                                print("평균 이상 금액 매도")
                                print(f"매도한금액 = ￦{sell_krw_price43}  |  매도한수량 = {sell_krw_balance43}  |  매수가능여부 - {op_mode43} - 매수가능-매도불가")
                                print("")
                            else:
                                # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                op_mode43 = 2

                                print("￦10,000 이하 금액 매도불가")
                                print(f"매수가능여부 - {op_mode43} - 매수가능-매도불가")
                                print("")

                        else:
                            # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                            op_mode43 = 2

                            print("평균 이하 금액 매도불가")
                            print(f"매수가능여부 - {op_mode43} - 매수가능-매도불가")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################


            ###############################
            # 코인44

            # 코인별 금액 비율조정
            sell_bpAve44 = bpAve * bpPer44

            # MACD 조건문
            if macd44 < 0:     # macd가 0보다 작을때는 매도
                if coinMode44 == 1 or coinMode44 == 3:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = 매수만가능 , 3 = >>>매도만가능<<<
                    if op_mode44 == 1 or op_mode44 == 4:   # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                        print("")
                        print(f"[ 44. 매도시간 : {now}  |  코인명 : {coin44}  |  현재가 = ￦{price44}  |  MACD = ￦{macd44}  |  보유수량 = {krw_balance44}  |  평가금액 = ￦{bp44}  ||  매도평균금액 = ￦{sell_bpAve44} ]")

                        if bp44 > sell_bpAve44: # 보유금액이 평균가보다 높을때
                            # 매도할 코인 금액 = 코인보유금액 - 평균가
                            sell_krw_price44 = bp44 - sell_bpAve44

                            if sell_krw_price44 >= 10000:    # 매도할 금액이 ￦10,000 보다 높을때 매도
                                # 매도할 코인 갯수 = 매도할 코인 금액 - 현재가
                                sell_krw_balance44 = sell_krw_price44 / price44

                                # 보유코인 초과금액 매도시도
                                # 매도할 코인명 - krw_coin44, 매도할 코인수량 - sell_krw_balance44
                                upbit.sell_market_order(krw_coin44, sell_krw_balance44)

                                # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                op_mode44 = 2

                                print("평균 이상 금액 매도")
                                print(f"매도한금액 = ￦{sell_krw_price44}  |  매도한수량 = {sell_krw_balance44}  |  매수가능여부 - {op_mode44} - 매수가능-매도불가")
                                print("")
                            else:
                                # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                op_mode44 = 2

                                print("￦10,000 이하 금액 매도불가")
                                print(f"매수가능여부 - {op_mode44} - 매수가능-매도불가")
                                print("")

                        else:
                            # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                            op_mode44 = 2

                            print("평균 이하 금액 매도불가")
                            print(f"매수가능여부 - {op_mode44} - 매수가능-매도불가")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################


            ###############################
            # 코인45

            # 코인별 금액 비율조정
            sell_bpAve45 = bpAve * bpPer45

            # MACD 조건문
            if macd45 < 0:     # macd가 0보다 작을때는 매도
                if coinMode45 == 1 or coinMode45 == 3:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = 매수만가능 , 3 = >>>매도만가능<<<
                    if op_mode45 == 1 or op_mode45 == 4:   # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                        print("")
                        print(f"[ 45. 매도시간 : {now}  |  코인명 : {coin45}  |  현재가 = ￦{price45}  |  MACD = ￦{macd45}  |  보유수량 = {krw_balance45}  |  평가금액 = ￦{bp45}  ||  매도평균금액 = ￦{sell_bpAve45} ]")

                        if bp45 > sell_bpAve45: # 보유금액이 평균가보다 높을때
                            # 매도할 코인 금액 = 코인보유금액 - 평균가
                            sell_krw_price45 = bp45 - sell_bpAve45

                            if sell_krw_price45 >= 10000:    # 매도할 금액이 ￦10,000 보다 높을때 매도
                                # 매도할 코인 갯수 = 매도할 코인 금액 - 현재가
                                sell_krw_balance45 = sell_krw_price45 / price45

                                # 보유코인 초과금액 매도시도
                                # 매도할 코인명 - krw_coin45, 매도할 코인수량 - sell_krw_balance45
                                upbit.sell_market_order(krw_coin45, sell_krw_balance45)

                                # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                op_mode45 = 2

                                print("평균 이상 금액 매도")
                                print(f"매도한금액 = ￦{sell_krw_price45}  |  매도한수량 = {sell_krw_balance45}  |  매수가능여부 - {op_mode45} - 매수가능-매도불가")
                                print("")
                            else:
                                # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                op_mode45 = 2

                                print("￦10,000 이하 금액 매도불가")
                                print(f"매수가능여부 - {op_mode45} - 매수가능-매도불가")
                                print("")

                        else:
                            # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                            op_mode45 = 2

                            print("평균 이하 금액 매도불가")
                            print(f"매수가능여부 - {op_mode45} - 매수가능-매도불가")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################


            ###############################
            # 코인46

            # 코인별 금액 비율조정
            sell_bpAve46 = bpAve * bpPer46

            # MACD 조건문
            if macd46 < 0:     # macd가 0보다 작을때는 매도
                if coinMode46 == 1 or coinMode46 == 3:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = 매수만가능 , 3 = >>>매도만가능<<<
                    if op_mode46 == 1 or op_mode46 == 4:   # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                        print("")
                        print(f"[ 46. 매도시간 : {now}  |  코인명 : {coin46}  |  현재가 = ￦{price46}  |  MACD = ￦{macd46}  |  보유수량 = {krw_balance46}  |  평가금액 = ￦{bp46}  ||  매도평균금액 = ￦{sell_bpAve46} ]")

                        if bp46 > sell_bpAve46: # 보유금액이 평균가보다 높을때
                            # 매도할 코인 금액 = 코인보유금액 - 평균가
                            sell_krw_price46 = bp46 - sell_bpAve46

                            if sell_krw_price46 >= 10000:    # 매도할 금액이 ￦10,000 보다 높을때 매도
                                # 매도할 코인 갯수 = 매도할 코인 금액 - 현재가
                                sell_krw_balance46 = sell_krw_price46 / price46

                                # 보유코인 초과금액 매도시도
                                # 매도할 코인명 - krw_coin46, 매도할 코인수량 - sell_krw_balance46
                                upbit.sell_market_order(krw_coin46, sell_krw_balance46)

                                # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                op_mode46 = 2

                                print("평균 이상 금액 매도")
                                print(f"매도한금액 = ￦{sell_krw_price46}  |  매도한수량 = {sell_krw_balance46}  |  매수가능여부 - {op_mode46} - 매수가능-매도불가")
                                print("")
                            else:
                                # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                op_mode46 = 2

                                print("￦10,000 이하 금액 매도불가")
                                print(f"매수가능여부 - {op_mode46} - 매수가능-매도불가")
                                print("")

                        else:
                            # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                            op_mode46 = 2

                            print("평균 이하 금액 매도불가")
                            print(f"매수가능여부 - {op_mode46} - 매수가능-매도불가")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################


            ###############################
            # 코인47

            # 코인별 금액 비율조정
            sell_bpAve47 = bpAve * bpPer47

            # MACD 조건문
            if macd47 < 0:     # macd가 0보다 작을때는 매도
                if coinMode47 == 1 or coinMode47 == 3:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = 매수만가능 , 3 = >>>매도만가능<<<
                    if op_mode47 == 1 or op_mode47 == 4:   # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                        print("")
                        print(f"[ 47. 매도시간 : {now}  |  코인명 : {coin47}  |  현재가 = ￦{price47}  |  MACD = ￦{macd47}  |  보유수량 = {krw_balance47}  |  평가금액 = ￦{bp47}  ||  매도평균금액 = ￦{sell_bpAve47} ]")

                        if bp47 > sell_bpAve47: # 보유금액이 평균가보다 높을때
                            # 매도할 코인 금액 = 코인보유금액 - 평균가
                            sell_krw_price47 = bp47 - sell_bpAve47

                            if sell_krw_price47 >= 10000:    # 매도할 금액이 ￦10,000 보다 높을때 매도
                                # 매도할 코인 갯수 = 매도할 코인 금액 - 현재가
                                sell_krw_balance47 = sell_krw_price47 / price47

                                # 보유코인 초과금액 매도시도
                                # 매도할 코인명 - krw_coin47, 매도할 코인수량 - sell_krw_balance47
                                upbit.sell_market_order(krw_coin47, sell_krw_balance47)

                                # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                op_mode47 = 2

                                print("평균 이상 금액 매도")
                                print(f"매도한금액 = ￦{sell_krw_price47}  |  매도한수량 = {sell_krw_balance47}  |  매수가능여부 - {op_mode47} - 매수가능-매도불가")
                                print("")
                            else:
                                # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                op_mode47 = 2

                                print("￦10,000 이하 금액 매도불가")
                                print(f"매수가능여부 - {op_mode47} - 매수가능-매도불가")
                                print("")

                        else:
                            # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                            op_mode47 = 2

                            print("평균 이하 금액 매도불가")
                            print(f"매수가능여부 - {op_mode47} - 매수가능-매도불가")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################


            ###############################
            # 코인48

            # 코인별 금액 비율조정
            sell_bpAve48 = bpAve * bpPer48

            # MACD 조건문
            if macd48 < 0:     # macd가 0보다 작을때는 매도
                if coinMode48 == 1 or coinMode48 == 3:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = 매수만가능 , 3 = >>>매도만가능<<<
                    if op_mode48 == 1 or op_mode48 == 4:   # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                        print("")
                        print(f"[ 48. 매도시간 : {now}  |  코인명 : {coin48}  |  현재가 = ￦{price48}  |  MACD = ￦{macd48}  |  보유수량 = {krw_balance48}  |  평가금액 = ￦{bp48}  ||  매도평균금액 = ￦{sell_bpAve48} ]")

                        if bp48 > sell_bpAve48: # 보유금액이 평균가보다 높을때
                            # 매도할 코인 금액 = 코인보유금액 - 평균가
                            sell_krw_price48 = bp48 - sell_bpAve48

                            if sell_krw_price48 >= 10000:    # 매도할 금액이 ￦10,000 보다 높을때 매도
                                # 매도할 코인 갯수 = 매도할 코인 금액 - 현재가
                                sell_krw_balance48 = sell_krw_price48 / price48

                                # 보유코인 초과금액 매도시도
                                # 매도할 코인명 - krw_coin48, 매도할 코인수량 - sell_krw_balance48
                                upbit.sell_market_order(krw_coin48, sell_krw_balance48)

                                # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                op_mode48 = 2

                                print("평균 이상 금액 매도")
                                print(f"매도한금액 = ￦{sell_krw_price48}  |  매도한수량 = {sell_krw_balance48}  |  매수가능여부 - {op_mode48} - 매수가능-매도불가")
                                print("")
                            else:
                                # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                op_mode48 = 2

                                print("￦10,000 이하 금액 매도불가")
                                print(f"매수가능여부 - {op_mode48} - 매수가능-매도불가")
                                print("")

                        else:
                            # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                            op_mode48 = 2

                            print("평균 이하 금액 매도불가")
                            print(f"매수가능여부 - {op_mode48} - 매수가능-매도불가")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################


            ###############################
            # 코인49

            # 코인별 금액 비율조정
            sell_bpAve49 = bpAve * bpPer49

            # MACD 조건문
            if macd49 < 0:     # macd가 0보다 작을때는 매도
                if coinMode49 == 1 or coinMode49 == 3:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = 매수만가능 , 3 = >>>매도만가능<<<
                    if op_mode49 == 1 or op_mode49 == 4:   # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                        print("")
                        print(f"[ 49. 매도시간 : {now}  |  코인명 : {coin49}  |  현재가 = ￦{price49}  |  MACD = ￦{macd49}  |  보유수량 = {krw_balance49}  |  평가금액 = ￦{bp49}  ||  매도평균금액 = ￦{sell_bpAve49} ]")

                        if bp49 > sell_bpAve49: # 보유금액이 평균가보다 높을때
                            # 매도할 코인 금액 = 코인보유금액 - 평균가
                            sell_krw_price49 = bp49 - sell_bpAve49

                            if sell_krw_price49 >= 10000:    # 매도할 금액이 ￦10,000 보다 높을때 매도
                                # 매도할 코인 갯수 = 매도할 코인 금액 - 현재가
                                sell_krw_balance49 = sell_krw_price49 / price49

                                # 보유코인 초과금액 매도시도
                                # 매도할 코인명 - krw_coin49, 매도할 코인수량 - sell_krw_balance49
                                upbit.sell_market_order(krw_coin49, sell_krw_balance49)

                                # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                op_mode49 = 2

                                print("평균 이상 금액 매도")
                                print(f"매도한금액 = ￦{sell_krw_price49}  |  매도한수량 = {sell_krw_balance49}  |  매수가능여부 - {op_mode49} - 매수가능-매도불가")
                                print("")
                            else:
                                # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                op_mode49 = 2

                                print("￦10,000 이하 금액 매도불가")
                                print(f"매수가능여부 - {op_mode49} - 매수가능-매도불가")
                                print("")

                        else:
                            # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                            op_mode49 = 2

                            print("평균 이하 금액 매도불가")
                            print(f"매수가능여부 - {op_mode49} - 매수가능-매도불가")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################


            ###############################
            # 코인50

            # 코인별 금액 비율조정
            sell_bpAve50 = bpAve * bpPer50

            # MACD 조건문
            if macd50 < 0:     # macd가 0보다 작을때는 매도
                if coinMode50 == 1 or coinMode50 == 3:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = 매수만가능 , 3 = >>>매도만가능<<<
                    if op_mode50 == 1 or op_mode50 == 4:   # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                        print("")
                        print(f"[ 50. 매도시간 : {now}  |  코인명 : {coin50}  |  현재가 = ￦{price50}  |  MACD = ￦{macd50}  |  보유수량 = {krw_balance50}  |  평가금액 = ￦{bp50}  ||  매도평균금액 = ￦{sell_bpAve50} ]")

                        if bp50 > sell_bpAve50: # 보유금액이 평균가보다 높을때
                            # 매도할 코인 금액 = 코인보유금액 - 평균가
                            sell_krw_price50 = bp50 - sell_bpAve50

                            if sell_krw_price50 >= 10000:    # 매도할 금액이 ￦10,000 보다 높을때 매도
                                # 매도할 코인 갯수 = 매도할 코인 금액 - 현재가
                                sell_krw_balance50 = sell_krw_price50 / price50

                                # 보유코인 초과금액 매도시도
                                # 매도할 코인명 - krw_coin50, 매도할 코인수량 - sell_krw_balance50
                                upbit.sell_market_order(krw_coin50, sell_krw_balance50)

                                # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                op_mode50 = 2

                                print("평균 이상 금액 매도")
                                print(f"매도한금액 = ￦{sell_krw_price50}  |  매도한수량 = {sell_krw_balance50}  |  매수가능여부 - {op_mode50} - 매수가능-매도불가")
                                print("")
                            else:
                                # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                op_mode50 = 2

                                print("￦10,000 이하 금액 매도불가")
                                print(f"매수가능여부 - {op_mode50} - 매수가능-매도불가")
                                print("")

                        else:
                            # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                            op_mode50 = 2

                            print("평균 이하 금액 매도불가")
                            print(f"매수가능여부 - {op_mode50} - 매수가능-매도불가")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################





            ######################################################################################################################################################
            ######################################################################################################################################################
            ######################################################################################################################################################





            ###############################
            # 코인51

            # 코인별 금액 비율조정
            sell_bpAve51 = bpAve * bpPer51

            # MACD 조건문
            if macd51 < 0:     # macd가 0보다 작을때는 매도
                if coinMode51 == 1 or coinMode51 == 3:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = 매수만가능 , 3 = >>>매도만가능<<<
                    if op_mode51 == 1 or op_mode51 == 4:   # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                        print("")
                        print(f"[ 51. 매도시간 : {now}  |  코인명 : {coin51}  |  현재가 = ￦{price51}  |  MACD = ￦{macd51}  |  보유수량 = {krw_balance51}  |  평가금액 = ￦{bp51}  ||  매도평균금액 = ￦{sell_bpAve51} ]")

                        if bp51 > sell_bpAve51: # 보유금액이 평균가보다 높을때
                            # 매도할 코인 금액 = 코인보유금액 - 평균가
                            sell_krw_price51 = bp51 - sell_bpAve51

                            if sell_krw_price51 >= 10000:    # 매도할 금액이 ￦10,000 보다 높을때 매도
                                # 매도할 코인 갯수 = 매도할 코인 금액 - 현재가
                                sell_krw_balance51 = sell_krw_price51 / price51

                                # 보유코인 초과금액 매도시도
                                # 매도할 코인명 - krw_coin51, 매도할 코인수량 - sell_krw_balance51
                                upbit.sell_market_order(krw_coin51, sell_krw_balance51)

                                # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                op_mode51 = 2

                                print("평균 이상 금액 매도")
                                print(f"매도한금액 = ￦{sell_krw_price51}  |  매도한수량 = {sell_krw_balance51}  |  매수가능여부 - {op_mode51} - 매수가능-매도불가")
                                print("")
                            else:
                                # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                op_mode51 = 2

                                print("￦10,000 이하 금액 매도불가")
                                print(f"매수가능여부 - {op_mode51} - 매수가능-매도불가")
                                print("")

                        else:
                            # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                            op_mode51 = 2

                            print("평균 이하 금액 매도불가")
                            print(f"매수가능여부 - {op_mode51} - 매수가능-매도불가")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################


            ###############################
            # 코인52

            # 코인별 금액 비율조정
            sell_bpAve52 = bpAve * bpPer52

            # MACD 조건문
            if macd52 < 0:     # macd가 0보다 작을때는 매도
                if coinMode52 == 1 or coinMode52 == 3:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = 매수만가능 , 3 = >>>매도만가능<<<
                    if op_mode52 == 1 or op_mode52 == 4:   # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                        print("")
                        print(f"[ 52. 매도시간 : {now}  |  코인명 : {coin52}  |  현재가 = ￦{price52}  |  MACD = ￦{macd52}  |  보유수량 = {krw_balance52}  |  평가금액 = ￦{bp52}  ||  매도평균금액 = ￦{sell_bpAve52} ]")

                        if bp52 > sell_bpAve52: # 보유금액이 평균가보다 높을때
                            # 매도할 코인 금액 = 코인보유금액 - 평균가
                            sell_krw_price52 = bp52 - sell_bpAve52

                            if sell_krw_price52 >= 10000:    # 매도할 금액이 ￦10,000 보다 높을때 매도
                                # 매도할 코인 갯수 = 매도할 코인 금액 - 현재가
                                sell_krw_balance52 = sell_krw_price52 / price52

                                # 보유코인 초과금액 매도시도
                                # 매도할 코인명 - krw_coin52, 매도할 코인수량 - sell_krw_balance52
                                upbit.sell_market_order(krw_coin52, sell_krw_balance52)

                                # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                op_mode52 = 2

                                print("평균 이상 금액 매도")
                                print(f"매도한금액 = ￦{sell_krw_price52}  |  매도한수량 = {sell_krw_balance52}  |  매수가능여부 - {op_mode52} - 매수가능-매도불가")
                                print("")
                            else:
                                # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                op_mode52 = 2

                                print("￦10,000 이하 금액 매도불가")
                                print(f"매수가능여부 - {op_mode52} - 매수가능-매도불가")
                                print("")

                        else:
                            # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                            op_mode52 = 2

                            print("평균 이하 금액 매도불가")
                            print(f"매수가능여부 - {op_mode52} - 매수가능-매도불가")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################


            ###############################
            # 코인53

            # 코인별 금액 비율조정
            sell_bpAve53 = bpAve * bpPer53

            # MACD 조건문
            if macd53 < 0:     # macd가 0보다 작을때는 매도
                if coinMode53 == 1 or coinMode53 == 3:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = 매수만가능 , 3 = >>>매도만가능<<<
                    if op_mode53 == 1 or op_mode53 == 4:   # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                        print("")
                        print(f"[ 53. 매도시간 : {now}  |  코인명 : {coin53}  |  현재가 = ￦{price53}  |  MACD = ￦{macd53}  |  보유수량 = {krw_balance53}  |  평가금액 = ￦{bp53}  ||  매도평균금액 = ￦{sell_bpAve53} ]")

                        if bp53 > sell_bpAve53: # 보유금액이 평균가보다 높을때
                            # 매도할 코인 금액 = 코인보유금액 - 평균가
                            sell_krw_price53 = bp53 - sell_bpAve53

                            if sell_krw_price53 >= 10000:    # 매도할 금액이 ￦10,000 보다 높을때 매도
                                # 매도할 코인 갯수 = 매도할 코인 금액 - 현재가
                                sell_krw_balance53 = sell_krw_price53 / price53

                                # 보유코인 초과금액 매도시도
                                # 매도할 코인명 - krw_coin53, 매도할 코인수량 - sell_krw_balance53
                                upbit.sell_market_order(krw_coin53, sell_krw_balance53)

                                # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                op_mode53 = 2

                                print("평균 이상 금액 매도")
                                print(f"매도한금액 = ￦{sell_krw_price53}  |  매도한수량 = {sell_krw_balance53}  |  매수가능여부 - {op_mode53} - 매수가능-매도불가")
                                print("")
                            else:
                                # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                op_mode53 = 2

                                print("￦10,000 이하 금액 매도불가")
                                print(f"매수가능여부 - {op_mode53} - 매수가능-매도불가")
                                print("")

                        else:
                            # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                            op_mode53 = 2

                            print("평균 이하 금액 매도불가")
                            print(f"매수가능여부 - {op_mode53} - 매수가능-매도불가")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################


            ###############################
            # 코인54

            # 코인별 금액 비율조정
            sell_bpAve54 = bpAve * bpPer54

            # MACD 조건문
            if macd54 < 0:     # macd가 0보다 작을때는 매도
                if coinMode54 == 1 or coinMode54 == 3:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = 매수만가능 , 3 = >>>매도만가능<<<
                    if op_mode54 == 1 or op_mode54 == 4:   # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                        print("")
                        print(f"[ 54. 매도시간 : {now}  |  코인명 : {coin54}  |  현재가 = ￦{price54}  |  MACD = ￦{macd54}  |  보유수량 = {krw_balance54}  |  평가금액 = ￦{bp54}  ||  매도평균금액 = ￦{sell_bpAve54} ]")

                        if bp54 > sell_bpAve54: # 보유금액이 평균가보다 높을때
                            # 매도할 코인 금액 = 코인보유금액 - 평균가
                            sell_krw_price54 = bp54 - sell_bpAve54

                            if sell_krw_price54 >= 10000:    # 매도할 금액이 ￦10,000 보다 높을때 매도
                                # 매도할 코인 갯수 = 매도할 코인 금액 - 현재가
                                sell_krw_balance54 = sell_krw_price54 / price54

                                # 보유코인 초과금액 매도시도
                                # 매도할 코인명 - krw_coin54, 매도할 코인수량 - sell_krw_balance54
                                upbit.sell_market_order(krw_coin54, sell_krw_balance54)

                                # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                op_mode54 = 2

                                print("평균 이상 금액 매도")
                                print(f"매도한금액 = ￦{sell_krw_price54}  |  매도한수량 = {sell_krw_balance54}  |  매수가능여부 - {op_mode54} - 매수가능-매도불가")
                                print("")
                            else:
                                # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                op_mode54 = 2

                                print("￦10,000 이하 금액 매도불가")
                                print(f"매수가능여부 - {op_mode54} - 매수가능-매도불가")
                                print("")

                        else:
                            # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                            op_mode54 = 2

                            print("평균 이하 금액 매도불가")
                            print(f"매수가능여부 - {op_mode54} - 매수가능-매도불가")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################


            ###############################
            # 코인55

            # 코인별 금액 비율조정
            sell_bpAve55 = bpAve * bpPer55

            # MACD 조건문
            if macd55 < 0:     # macd가 0보다 작을때는 매도
                if coinMode55 == 1 or coinMode55 == 3:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = 매수만가능 , 3 = >>>매도만가능<<<
                    if op_mode55 == 1 or op_mode55 == 4:   # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                        print("")
                        print(f"[ 55. 매도시간 : {now}  |  코인명 : {coin55}  |  현재가 = ￦{price55}  |  MACD = ￦{macd55}  |  보유수량 = {krw_balance55}  |  평가금액 = ￦{bp55}  ||  매도평균금액 = ￦{sell_bpAve55} ]")

                        if bp55 > sell_bpAve55: # 보유금액이 평균가보다 높을때
                            # 매도할 코인 금액 = 코인보유금액 - 평균가
                            sell_krw_price55 = bp55 - sell_bpAve55

                            if sell_krw_price55 >= 10000:    # 매도할 금액이 ￦10,000 보다 높을때 매도
                                # 매도할 코인 갯수 = 매도할 코인 금액 - 현재가
                                sell_krw_balance55 = sell_krw_price55 / price55

                                # 보유코인 초과금액 매도시도
                                # 매도할 코인명 - krw_coin55, 매도할 코인수량 - sell_krw_balance55
                                upbit.sell_market_order(krw_coin55, sell_krw_balance55)

                                # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                op_mode55 = 2

                                print("평균 이상 금액 매도")
                                print(f"매도한금액 = ￦{sell_krw_price55}  |  매도한수량 = {sell_krw_balance55}  |  매수가능여부 - {op_mode55} - 매수가능-매도불가")
                                print("")
                            else:
                                # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                op_mode55 = 2

                                print("￦10,000 이하 금액 매도불가")
                                print(f"매수가능여부 - {op_mode55} - 매수가능-매도불가")
                                print("")

                        else:
                            # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                            op_mode55 = 2

                            print("평균 이하 금액 매도불가")
                            print(f"매수가능여부 - {op_mode55} - 매수가능-매도불가")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################


            ###############################
            # 코인56

            # 코인별 금액 비율조정
            sell_bpAve56 = bpAve * bpPer56

            # MACD 조건문
            if macd56 < 0:     # macd가 0보다 작을때는 매도
                if coinMode56 == 1 or coinMode56 == 3:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = 매수만가능 , 3 = >>>매도만가능<<<
                    if op_mode56 == 1 or op_mode56 == 4:   # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                        print("")
                        print(f"[ 56. 매도시간 : {now}  |  코인명 : {coin56}  |  현재가 = ￦{price56}  |  MACD = ￦{macd56}  |  보유수량 = {krw_balance56}  |  평가금액 = ￦{bp56}  ||  매도평균금액 = ￦{sell_bpAve56} ]")

                        if bp56 > sell_bpAve56: # 보유금액이 평균가보다 높을때
                            # 매도할 코인 금액 = 코인보유금액 - 평균가
                            sell_krw_price56 = bp56 - sell_bpAve56

                            if sell_krw_price56 >= 10000:    # 매도할 금액이 ￦10,000 보다 높을때 매도
                                # 매도할 코인 갯수 = 매도할 코인 금액 - 현재가
                                sell_krw_balance56 = sell_krw_price56 / price56

                                # 보유코인 초과금액 매도시도
                                # 매도할 코인명 - krw_coin56, 매도할 코인수량 - sell_krw_balance56
                                upbit.sell_market_order(krw_coin56, sell_krw_balance56)

                                # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                op_mode56 = 2

                                print("평균 이상 금액 매도")
                                print(f"매도한금액 = ￦{sell_krw_price56}  |  매도한수량 = {sell_krw_balance56}  |  매수가능여부 - {op_mode56} - 매수가능-매도불가")
                                print("")
                            else:
                                # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                op_mode56 = 2

                                print("￦10,000 이하 금액 매도불가")
                                print(f"매수가능여부 - {op_mode56} - 매수가능-매도불가")
                                print("")

                        else:
                            # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                            op_mode56 = 2

                            print("평균 이하 금액 매도불가")
                            print(f"매수가능여부 - {op_mode56} - 매수가능-매도불가")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################


            ###############################
            # 코인57

            # 코인별 금액 비율조정
            sell_bpAve57 = bpAve * bpPer57

            # MACD 조건문
            if macd57 < 0:     # macd가 0보다 작을때는 매도
                if coinMode57 == 1 or coinMode57 == 3:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = 매수만가능 , 3 = >>>매도만가능<<<
                    if op_mode57 == 1 or op_mode57 == 4:   # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                        print("")
                        print(f"[ 57. 매도시간 : {now}  |  코인명 : {coin57}  |  현재가 = ￦{price57}  |  MACD = ￦{macd57}  |  보유수량 = {krw_balance57}  |  평가금액 = ￦{bp57}  ||  매도평균금액 = ￦{sell_bpAve57} ]")

                        if bp57 > sell_bpAve57: # 보유금액이 평균가보다 높을때
                            # 매도할 코인 금액 = 코인보유금액 - 평균가
                            sell_krw_price57 = bp57 - sell_bpAve57

                            if sell_krw_price57 >= 10000:    # 매도할 금액이 ￦10,000 보다 높을때 매도
                                # 매도할 코인 갯수 = 매도할 코인 금액 - 현재가
                                sell_krw_balance57 = sell_krw_price57 / price57

                                # 보유코인 초과금액 매도시도
                                # 매도할 코인명 - krw_coin57, 매도할 코인수량 - sell_krw_balance57
                                upbit.sell_market_order(krw_coin57, sell_krw_balance57)

                                # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                op_mode57 = 2

                                print("평균 이상 금액 매도")
                                print(f"매도한금액 = ￦{sell_krw_price57}  |  매도한수량 = {sell_krw_balance57}  |  매수가능여부 - {op_mode57} - 매수가능-매도불가")
                                print("")
                            else:
                                # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                op_mode57 = 2

                                print("￦10,000 이하 금액 매도불가")
                                print(f"매수가능여부 - {op_mode57} - 매수가능-매도불가")
                                print("")

                        else:
                            # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                            op_mode57 = 2

                            print("평균 이하 금액 매도불가")
                            print(f"매수가능여부 - {op_mode57} - 매수가능-매도불가")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################


            ###############################
            # 코인58

            # 코인별 금액 비율조정
            sell_bpAve58 = bpAve * bpPer58

            # MACD 조건문
            if macd58 < 0:     # macd가 0보다 작을때는 매도
                if coinMode58 == 1 or coinMode58 == 3:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = 매수만가능 , 3 = >>>매도만가능<<<
                    if op_mode58 == 1 or op_mode58 == 4:   # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                        print("")
                        print(f"[ 58. 매도시간 : {now}  |  코인명 : {coin58}  |  현재가 = ￦{price58}  |  MACD = ￦{macd58}  |  보유수량 = {krw_balance58}  |  평가금액 = ￦{bp58}  ||  매도평균금액 = ￦{sell_bpAve58} ]")

                        if bp58 > sell_bpAve58: # 보유금액이 평균가보다 높을때
                            # 매도할 코인 금액 = 코인보유금액 - 평균가
                            sell_krw_price58 = bp58 - sell_bpAve58

                            if sell_krw_price58 >= 10000:    # 매도할 금액이 ￦10,000 보다 높을때 매도
                                # 매도할 코인 갯수 = 매도할 코인 금액 - 현재가
                                sell_krw_balance58 = sell_krw_price58 / price58

                                # 보유코인 초과금액 매도시도
                                # 매도할 코인명 - krw_coin58, 매도할 코인수량 - sell_krw_balance58
                                upbit.sell_market_order(krw_coin58, sell_krw_balance58)

                                # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                op_mode58 = 2

                                print("평균 이상 금액 매도")
                                print(f"매도한금액 = ￦{sell_krw_price58}  |  매도한수량 = {sell_krw_balance58}  |  매수가능여부 - {op_mode58} - 매수가능-매도불가")
                                print("")
                            else:
                                # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                op_mode58 = 2

                                print("￦10,000 이하 금액 매도불가")
                                print(f"매수가능여부 - {op_mode58} - 매수가능-매도불가")
                                print("")

                        else:
                            # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                            op_mode58 = 2

                            print("평균 이하 금액 매도불가")
                            print(f"매수가능여부 - {op_mode58} - 매수가능-매도불가")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################


            ###############################
            # 코인59

            # 코인별 금액 비율조정
            sell_bpAve59 = bpAve * bpPer59

            # MACD 조건문
            if macd59 < 0:     # macd가 0보다 작을때는 매도
                if coinMode59 == 1 or coinMode59 == 3:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = 매수만가능 , 3 = >>>매도만가능<<<
                    if op_mode59 == 1 or op_mode59 == 4:   # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                        print("")
                        print(f"[ 59. 매도시간 : {now}  |  코인명 : {coin59}  |  현재가 = ￦{price59}  |  MACD = ￦{macd59}  |  보유수량 = {krw_balance59}  |  평가금액 = ￦{bp59}  ||  매도평균금액 = ￦{sell_bpAve59} ]")

                        if bp59 > sell_bpAve59: # 보유금액이 평균가보다 높을때
                            # 매도할 코인 금액 = 코인보유금액 - 평균가
                            sell_krw_price59 = bp59 - sell_bpAve59

                            if sell_krw_price59 >= 10000:    # 매도할 금액이 ￦10,000 보다 높을때 매도
                                # 매도할 코인 갯수 = 매도할 코인 금액 - 현재가
                                sell_krw_balance59 = sell_krw_price59 / price59

                                # 보유코인 초과금액 매도시도
                                # 매도할 코인명 - krw_coin59, 매도할 코인수량 - sell_krw_balance59
                                upbit.sell_market_order(krw_coin59, sell_krw_balance59)

                                # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                op_mode59 = 2

                                print("평균 이상 금액 매도")
                                print(f"매도한금액 = ￦{sell_krw_price59}  |  매도한수량 = {sell_krw_balance59}  |  매수가능여부 - {op_mode59} - 매수가능-매도불가")
                                print("")
                            else:
                                # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                op_mode59 = 2

                                print("￦10,000 이하 금액 매도불가")
                                print(f"매수가능여부 - {op_mode59} - 매수가능-매도불가")
                                print("")

                        else:
                            # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                            op_mode59 = 2

                            print("평균 이하 금액 매도불가")
                            print(f"매수가능여부 - {op_mode59} - 매수가능-매도불가")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################


            ###############################
            # 코인60

            # 코인별 금액 비율조정
            sell_bpAve60 = bpAve * bpPer60

            # MACD 조건문
            if macd60 < 0:     # macd가 0보다 작을때는 매도
                if coinMode60 == 1 or coinMode60 == 3:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = 매수만가능 , 3 = >>>매도만가능<<<
                    if op_mode60 == 1 or op_mode60 == 4:   # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                        print("")
                        print(f"[ 60. 매도시간 : {now}  |  코인명 : {coin60}  |  현재가 = ￦{price60}  |  MACD = ￦{macd60}  |  보유수량 = {krw_balance60}  |  평가금액 = ￦{bp60}  ||  매도평균금액 = ￦{sell_bpAve60} ]")

                        if bp60 > sell_bpAve60: # 보유금액이 평균가보다 높을때
                            # 매도할 코인 금액 = 코인보유금액 - 평균가
                            sell_krw_price60 = bp60 - sell_bpAve60

                            if sell_krw_price60 >= 10000:    # 매도할 금액이 ￦10,000 보다 높을때 매도
                                # 매도할 코인 갯수 = 매도할 코인 금액 - 현재가
                                sell_krw_balance60 = sell_krw_price60 / price60

                                # 보유코인 초과금액 매도시도
                                # 매도할 코인명 - krw_coin60, 매도할 코인수량 - sell_krw_balance60
                                upbit.sell_market_order(krw_coin60, sell_krw_balance60)

                                # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                op_mode60 = 2

                                print("평균 이상 금액 매도")
                                print(f"매도한금액 = ￦{sell_krw_price60}  |  매도한수량 = {sell_krw_balance60}  |  매수가능여부 - {op_mode60} - 매수가능-매도불가")
                                print("")
                            else:
                                # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                op_mode60 = 2

                                print("￦10,000 이하 금액 매도불가")
                                print(f"매수가능여부 - {op_mode60} - 매수가능-매도불가")
                                print("")

                        else:
                            # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                            op_mode60 = 2

                            print("평균 이하 금액 매도불가")
                            print(f"매수가능여부 - {op_mode60} - 매수가능-매도불가")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################





            ######################################################################################################################################################
            ######################################################################################################################################################
            ######################################################################################################################################################





            ###############################
            # 코인61

            # 코인별 금액 비율조정
            sell_bpAve61 = bpAve * bpPer61

            # MACD 조건문
            if macd61 < 0:     # macd가 0보다 작을때는 매도
                if coinMode61 == 1 or coinMode61 == 3:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = 매수만가능 , 3 = >>>매도만가능<<<
                    if op_mode61 == 1 or op_mode61 == 4:   # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                        print("")
                        print(f"[ 61. 매도시간 : {now}  |  코인명 : {coin61}  |  현재가 = ￦{price61}  |  MACD = ￦{macd61}  |  보유수량 = {krw_balance61}  |  평가금액 = ￦{bp61}  ||  매도평균금액 = ￦{sell_bpAve61} ]")

                        if bp61 > sell_bpAve61: # 보유금액이 평균가보다 높을때
                            # 매도할 코인 금액 = 코인보유금액 - 평균가
                            sell_krw_price61 = bp61 - sell_bpAve61

                            if sell_krw_price61 >= 10000:    # 매도할 금액이 ￦10,000 보다 높을때 매도
                                # 매도할 코인 갯수 = 매도할 코인 금액 - 현재가
                                sell_krw_balance61 = sell_krw_price61 / price61

                                # 보유코인 초과금액 매도시도
                                # 매도할 코인명 - krw_coin61, 매도할 코인수량 - sell_krw_balance61
                                upbit.sell_market_order(krw_coin61, sell_krw_balance61)

                                # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                op_mode61 = 2

                                print("평균 이상 금액 매도")
                                print(f"매도한금액 = ￦{sell_krw_price61}  |  매도한수량 = {sell_krw_balance61}  |  매수가능여부 - {op_mode61} - 매수가능-매도불가")
                                print("")
                            else:
                                # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                op_mode61 = 2

                                print("￦10,000 이하 금액 매도불가")
                                print(f"매수가능여부 - {op_mode61} - 매수가능-매도불가")
                                print("")

                        else:
                            # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                            op_mode61 = 2

                            print("평균 이하 금액 매도불가")
                            print(f"매수가능여부 - {op_mode61} - 매수가능-매도불가")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################


            ###############################
            # 코인62

            # 코인별 금액 비율조정
            sell_bpAve62 = bpAve * bpPer62

            # MACD 조건문
            if macd62 < 0:     # macd가 0보다 작을때는 매도
                if coinMode62 == 1 or coinMode62 == 3:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = 매수만가능 , 3 = >>>매도만가능<<<
                    if op_mode62 == 1 or op_mode62 == 4:   # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                        print("")
                        print(f"[ 62. 매도시간 : {now}  |  코인명 : {coin62}  |  현재가 = ￦{price62}  |  MACD = ￦{macd62}  |  보유수량 = {krw_balance62}  |  평가금액 = ￦{bp62}  ||  매도평균금액 = ￦{sell_bpAve62} ]")

                        if bp62 > sell_bpAve62: # 보유금액이 평균가보다 높을때
                            # 매도할 코인 금액 = 코인보유금액 - 평균가
                            sell_krw_price62 = bp62 - sell_bpAve62

                            if sell_krw_price62 >= 10000:    # 매도할 금액이 ￦10,000 보다 높을때 매도
                                # 매도할 코인 갯수 = 매도할 코인 금액 - 현재가
                                sell_krw_balance62 = sell_krw_price62 / price62

                                # 보유코인 초과금액 매도시도
                                # 매도할 코인명 - krw_coin62, 매도할 코인수량 - sell_krw_balance62
                                upbit.sell_market_order(krw_coin62, sell_krw_balance62)

                                # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                op_mode62 = 2

                                print("평균 이상 금액 매도")
                                print(f"매도한금액 = ￦{sell_krw_price62}  |  매도한수량 = {sell_krw_balance62}  |  매수가능여부 - {op_mode62} - 매수가능-매도불가")
                                print("")
                            else:
                                # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                op_mode62 = 2

                                print("￦10,000 이하 금액 매도불가")
                                print(f"매수가능여부 - {op_mode62} - 매수가능-매도불가")
                                print("")

                        else:
                            # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                            op_mode62 = 2

                            print("평균 이하 금액 매도불가")
                            print(f"매수가능여부 - {op_mode62} - 매수가능-매도불가")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################


            ###############################
            # 코인63

            # 코인별 금액 비율조정
            sell_bpAve63 = bpAve * bpPer63

            # MACD 조건문
            if macd63 < 0:     # macd가 0보다 작을때는 매도
                if coinMode63 == 1 or coinMode63 == 3:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = 매수만가능 , 3 = >>>매도만가능<<<
                    if op_mode63 == 1 or op_mode63 == 4:   # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                        print("")
                        print(f"[ 63. 매도시간 : {now}  |  코인명 : {coin63}  |  현재가 = ￦{price63}  |  MACD = ￦{macd63}  |  보유수량 = {krw_balance63}  |  평가금액 = ￦{bp63}  ||  매도평균금액 = ￦{sell_bpAve63} ]")

                        if bp63 > sell_bpAve63: # 보유금액이 평균가보다 높을때
                            # 매도할 코인 금액 = 코인보유금액 - 평균가
                            sell_krw_price63 = bp63 - sell_bpAve63

                            if sell_krw_price63 >= 10000:    # 매도할 금액이 ￦10,000 보다 높을때 매도
                                # 매도할 코인 갯수 = 매도할 코인 금액 - 현재가
                                sell_krw_balance63 = sell_krw_price63 / price63

                                # 보유코인 초과금액 매도시도
                                # 매도할 코인명 - krw_coin63, 매도할 코인수량 - sell_krw_balance63
                                upbit.sell_market_order(krw_coin63, sell_krw_balance63)

                                # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                op_mode63 = 2

                                print("평균 이상 금액 매도")
                                print(f"매도한금액 = ￦{sell_krw_price63}  |  매도한수량 = {sell_krw_balance63}  |  매수가능여부 - {op_mode63} - 매수가능-매도불가")
                                print("")
                            else:
                                # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                op_mode63 = 2

                                print("￦10,000 이하 금액 매도불가")
                                print(f"매수가능여부 - {op_mode63} - 매수가능-매도불가")
                                print("")

                        else:
                            # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                            op_mode63 = 2

                            print("평균 이하 금액 매도불가")
                            print(f"매수가능여부 - {op_mode63} - 매수가능-매도불가")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################


            ###############################
            # 코인64

            # 코인별 금액 비율조정
            sell_bpAve64 = bpAve * bpPer64

            # MACD 조건문
            if macd64 < 0:     # macd가 0보다 작을때는 매도
                if coinMode64 == 1 or coinMode64 == 3:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = 매수만가능 , 3 = >>>매도만가능<<<
                    if op_mode64 == 1 or op_mode64 == 4:   # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                        print("")
                        print(f"[ 64. 매도시간 : {now}  |  코인명 : {coin64}  |  현재가 = ￦{price64}  |  MACD = ￦{macd64}  |  보유수량 = {krw_balance64}  |  평가금액 = ￦{bp64}  ||  매도평균금액 = ￦{sell_bpAve64} ]")

                        if bp64 > sell_bpAve64: # 보유금액이 평균가보다 높을때
                            # 매도할 코인 금액 = 코인보유금액 - 평균가
                            sell_krw_price64 = bp64 - sell_bpAve64

                            if sell_krw_price64 >= 10000:    # 매도할 금액이 ￦10,000 보다 높을때 매도
                                # 매도할 코인 갯수 = 매도할 코인 금액 - 현재가
                                sell_krw_balance64 = sell_krw_price64 / price64

                                # 보유코인 초과금액 매도시도
                                # 매도할 코인명 - krw_coin64, 매도할 코인수량 - sell_krw_balance64
                                upbit.sell_market_order(krw_coin64, sell_krw_balance64)

                                # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                op_mode64 = 2

                                print("평균 이상 금액 매도")
                                print(f"매도한금액 = ￦{sell_krw_price64}  |  매도한수량 = {sell_krw_balance64}  |  매수가능여부 - {op_mode64} - 매수가능-매도불가")
                                print("")
                            else:
                                # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                op_mode64 = 2

                                print("￦10,000 이하 금액 매도불가")
                                print(f"매수가능여부 - {op_mode64} - 매수가능-매도불가")
                                print("")

                        else:
                            # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                            op_mode64 = 2

                            print("평균 이하 금액 매도불가")
                            print(f"매수가능여부 - {op_mode64} - 매수가능-매도불가")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################


            ###############################
            # 코인65

            # 코인별 금액 비율조정
            sell_bpAve65 = bpAve * bpPer65

            # MACD 조건문
            if macd65 < 0:     # macd가 0보다 작을때는 매도
                if coinMode65 == 1 or coinMode65 == 3:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = 매수만가능 , 3 = >>>매도만가능<<<
                    if op_mode65 == 1 or op_mode65 == 4:   # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                        print("")
                        print(f"[ 65. 매도시간 : {now}  |  코인명 : {coin65}  |  현재가 = ￦{price65}  |  MACD = ￦{macd65}  |  보유수량 = {krw_balance65}  |  평가금액 = ￦{bp65}  ||  매도평균금액 = ￦{sell_bpAve65} ]")

                        if bp65 > sell_bpAve65: # 보유금액이 평균가보다 높을때
                            # 매도할 코인 금액 = 코인보유금액 - 평균가
                            sell_krw_price65 = bp65 - sell_bpAve65

                            if sell_krw_price65 >= 10000:    # 매도할 금액이 ￦10,000 보다 높을때 매도
                                # 매도할 코인 갯수 = 매도할 코인 금액 - 현재가
                                sell_krw_balance65 = sell_krw_price65 / price65

                                # 보유코인 초과금액 매도시도
                                # 매도할 코인명 - krw_coin65, 매도할 코인수량 - sell_krw_balance65
                                upbit.sell_market_order(krw_coin65, sell_krw_balance65)

                                # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                op_mode65 = 2

                                print("평균 이상 금액 매도")
                                print(f"매도한금액 = ￦{sell_krw_price65}  |  매도한수량 = {sell_krw_balance65}  |  매수가능여부 - {op_mode65} - 매수가능-매도불가")
                                print("")
                            else:
                                # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                op_mode65 = 2

                                print("￦10,000 이하 금액 매도불가")
                                print(f"매수가능여부 - {op_mode65} - 매수가능-매도불가")
                                print("")

                        else:
                            # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                            op_mode65 = 2

                            print("평균 이하 금액 매도불가")
                            print(f"매수가능여부 - {op_mode65} - 매수가능-매도불가")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################


            ###############################
            # 코인66

            # 코인별 금액 비율조정
            sell_bpAve66 = bpAve * bpPer66

            # MACD 조건문
            if macd66 < 0:     # macd가 0보다 작을때는 매도
                if coinMode66 == 1 or coinMode66 == 3:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = 매수만가능 , 3 = >>>매도만가능<<<
                    if op_mode66 == 1 or op_mode66 == 4:   # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                        print("")
                        print(f"[ 66. 매도시간 : {now}  |  코인명 : {coin66}  |  현재가 = ￦{price66}  |  MACD = ￦{macd66}  |  보유수량 = {krw_balance66}  |  평가금액 = ￦{bp66}  ||  매도평균금액 = ￦{sell_bpAve66} ]")

                        if bp66 > sell_bpAve66: # 보유금액이 평균가보다 높을때
                            # 매도할 코인 금액 = 코인보유금액 - 평균가
                            sell_krw_price66 = bp66 - sell_bpAve66

                            if sell_krw_price66 >= 10000:    # 매도할 금액이 ￦10,000 보다 높을때 매도
                                # 매도할 코인 갯수 = 매도할 코인 금액 - 현재가
                                sell_krw_balance66 = sell_krw_price66 / price66

                                # 보유코인 초과금액 매도시도
                                # 매도할 코인명 - krw_coin66, 매도할 코인수량 - sell_krw_balance66
                                upbit.sell_market_order(krw_coin66, sell_krw_balance66)

                                # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                op_mode66 = 2

                                print("평균 이상 금액 매도")
                                print(f"매도한금액 = ￦{sell_krw_price66}  |  매도한수량 = {sell_krw_balance66}  |  매수가능여부 - {op_mode66} - 매수가능-매도불가")
                                print("")
                            else:
                                # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                op_mode66 = 2

                                print("￦10,000 이하 금액 매도불가")
                                print(f"매수가능여부 - {op_mode66} - 매수가능-매도불가")
                                print("")

                        else:
                            # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                            op_mode66 = 2

                            print("평균 이하 금액 매도불가")
                            print(f"매수가능여부 - {op_mode66} - 매수가능-매도불가")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################


            ###############################
            # 코인67

            # 코인별 금액 비율조정
            sell_bpAve67 = bpAve * bpPer67

            # MACD 조건문
            if macd67 < 0:     # macd가 0보다 작을때는 매도
                if coinMode67 == 1 or coinMode67 == 3:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = 매수만가능 , 3 = >>>매도만가능<<<
                    if op_mode67 == 1 or op_mode67 == 4:   # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                        print("")
                        print(f"[ 67. 매도시간 : {now}  |  코인명 : {coin67}  |  현재가 = ￦{price67}  |  MACD = ￦{macd67}  |  보유수량 = {krw_balance67}  |  평가금액 = ￦{bp67}  ||  매도평균금액 = ￦{sell_bpAve67} ]")

                        if bp67 > sell_bpAve67: # 보유금액이 평균가보다 높을때
                            # 매도할 코인 금액 = 코인보유금액 - 평균가
                            sell_krw_price67 = bp67 - sell_bpAve67

                            if sell_krw_price67 >= 10000:    # 매도할 금액이 ￦10,000 보다 높을때 매도
                                # 매도할 코인 갯수 = 매도할 코인 금액 - 현재가
                                sell_krw_balance67 = sell_krw_price67 / price67

                                # 보유코인 초과금액 매도시도
                                # 매도할 코인명 - krw_coin67, 매도할 코인수량 - sell_krw_balance67
                                upbit.sell_market_order(krw_coin67, sell_krw_balance67)

                                # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                op_mode67 = 2

                                print("평균 이상 금액 매도")
                                print(f"매도한금액 = ￦{sell_krw_price67}  |  매도한수량 = {sell_krw_balance67}  |  매수가능여부 - {op_mode67} - 매수가능-매도불가")
                                print("")
                            else:
                                # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                op_mode67 = 2

                                print("￦10,000 이하 금액 매도불가")
                                print(f"매수가능여부 - {op_mode67} - 매수가능-매도불가")
                                print("")

                        else:
                            # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                            op_mode67 = 2

                            print("평균 이하 금액 매도불가")
                            print(f"매수가능여부 - {op_mode67} - 매수가능-매도불가")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################


            ###############################
            # 코인68

            # 코인별 금액 비율조정
            sell_bpAve68 = bpAve * bpPer68

            # MACD 조건문
            if macd68 < 0:     # macd가 0보다 작을때는 매도
                if coinMode68 == 1 or coinMode68 == 3:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = 매수만가능 , 3 = >>>매도만가능<<<
                    if op_mode68 == 1 or op_mode68 == 4:   # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                        print("")
                        print(f"[ 68. 매도시간 : {now}  |  코인명 : {coin68}  |  현재가 = ￦{price68}  |  MACD = ￦{macd68}  |  보유수량 = {krw_balance68}  |  평가금액 = ￦{bp68}  ||  매도평균금액 = ￦{sell_bpAve68} ]")

                        if bp68 > sell_bpAve68: # 보유금액이 평균가보다 높을때
                            # 매도할 코인 금액 = 코인보유금액 - 평균가
                            sell_krw_price68 = bp68 - sell_bpAve68

                            if sell_krw_price68 >= 10000:    # 매도할 금액이 ￦10,000 보다 높을때 매도
                                # 매도할 코인 갯수 = 매도할 코인 금액 - 현재가
                                sell_krw_balance68 = sell_krw_price68 / price68

                                # 보유코인 초과금액 매도시도
                                # 매도할 코인명 - krw_coin68, 매도할 코인수량 - sell_krw_balance68
                                upbit.sell_market_order(krw_coin68, sell_krw_balance68)

                                # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                op_mode68 = 2

                                print("평균 이상 금액 매도")
                                print(f"매도한금액 = ￦{sell_krw_price68}  |  매도한수량 = {sell_krw_balance68}  |  매수가능여부 - {op_mode68} - 매수가능-매도불가")
                                print("")
                            else:
                                # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                op_mode68 = 2

                                print("￦10,000 이하 금액 매도불가")
                                print(f"매수가능여부 - {op_mode68} - 매수가능-매도불가")
                                print("")

                        else:
                            # 코인 매도 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                            op_mode68 = 2

                            print("평균 이하 금액 매도불가")
                            print(f"매수가능여부 - {op_mode68} - 매수가능-매도불가")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################





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
            bpAve2 = bp11 + bp12 + bp13 + bp14 + bp15 + bp16 + bp17 + bp18 + bp19 + bp20
            bpAve3 = bp21 + bp22 + bp23 + bp24 + bp25 + bp26 + bp27 + bp28 + bp29 + bp30
            bpAve4 = bp31 + bp32 + bp33 + bp34 + bp35 + bp36 + bp37 + bp38 + bp39 + bp40
            bpAve5 = bp41 + bp42 + bp43 + bp44 + bp45 + bp46 + bp47 + bp48 + bp49 + bp50
            bpAve6 = bp51 + bp52 + bp53 + bp54 + bp55 + bp56 + bp57 + bp58 + bp59 + bp60
            bpAve7 = bp61 + bp62 + bp63 + bp64 + bp65 + bp66 + bp67 + bp68

            bpAve = (bpAve1 + bpAve2 + bpAve3 + bpAve4 + bpAve5 + bpAve6 + bpAve7 ) / 69

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

            # 코인별 금액 비율조정
            buy_bpAve1 = bpAve * bpPer1

            # MACD 조건문
            if macd1 >= 0:     # macd가 0보다 크거나 같을때는 매수
                # 매수가능금액 불러오기
                krw1 = upbit.get_balance("KRW")

                if coinMode1 == 1 or coinMode1 == 2:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = >>>매수만가능<<< , 3 = 매도만가능
                    if op_mode1 == 2 or op_mode1 == 3:   # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                        print("")
                        print(f"[ 1. 매수시간 : {now}  |  코인명 : {coin1}  |  현재가 = ￦{price1}  |  MACD = ￦{macd1}  |  보유수량 = {krw_balance1}  |  평가금액 = ￦{bp1}  ||  매수평균금액 = ￦{buy_bpAve1} ]")

                        if bp1 < buy_bpAve1: # 코인보유금액이 평균가보다 낮을때 매수시도
                            # 매수할 코인 금액 = 평균가 - 코인보유금액
                            buy_krw_price1 = buy_bpAve1 - bp1
                            # 매수할 코인 갯수 = 매수할 코인 금액 - 현재가
                            buy_krw_balance1 = buy_krw_price1 / price1

                            if krw1 >= buy_krw_price1: # 매수가능금액이 매수할금액보다 클때 매수시도
                                if buy_krw_price1 >= 10000:    # 매수가능금액이 최소주문가능금액인 ￦10,000원보다 높을때 매수시도

                                    # 매수할 코인명 - krw_coin1, 매수할 코인금액 - buy_krw_price1
                                    upbit.buy_market_order(krw_coin1, buy_krw_price1 * 0.9)

                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode1 = 1

                                    print("평균 이하 금액 매수")
                                    print(f"매수한금액 = ￦{buy_krw_price1}  |  매수한수량 = {buy_krw_balance1}  |  매수가능여부 - {op_mode1} - 매수불가-매도가능")
                                    print("")

                                else:
                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode1 = 1

                                    print("매수금액이 ￦10,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode1} - 매수불가-매도가능")
                                    print("")
                            else:   # 보유금액이 평균가와의 차이보다 적을때 매수
                                if krw1 >= 10000:    # 보유금액이 최소주문가능금액인 ￦10,000원보다 높을때 매수시도
                                    # 매수할 코인명 - krw_coin1, 매수할 코인금액 - krw1
                                    upbit.buy_market_order(krw_coin1, krw1 * 0.9)

                                    op_mode1 = 1

                                    print("보유금액보다 매수금액보다 적어서 매수금지")
                                    print(f"매수한금액 = ￦{krw1}  |  매수한수량 = {buy_krw_balance1}  |  매수가능여부 - {op_mode1} - 매수불가-매도가능")
                                    print("")
                                else:
                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode1 = 1

                                    print("보유금액이 ￦10,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode1} - 매수불가-매도가능")
                                    print("")

                        else:
                            # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                            op_mode1 = 1

                            print("보유금액이 평균금액보다 높아서 매수불가")
                            print(f"매수가능여부 - {op_mode1} - 매수불가-매도가능")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################


            ###############################
            # 코인2

            # 코인별 금액 비율조정
            buy_bpAve2 = bpAve * bpPer2

            # MACD 조건문
            if macd2 >= 0:     # macd가 0보다 크거나 같을때는 매수
                # 매수가능금액 불러오기
                krw2 = upbit.get_balance("KRW")

                if coinMode2 == 1 or coinMode2 == 2:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = >>>매수만가능<<< , 3 = 매도만가능
                    if op_mode2 == 2 or op_mode2 == 3:   # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                        print("")
                        print(f"[ 2. 매수시간 : {now}  |  코인명 : {coin2}  |  현재가 = ￦{price2}  |  MACD = ￦{macd2}  |  보유수량 = {krw_balance2}  |  평가금액 = ￦{bp2}  ||  매수평균금액 = ￦{buy_bpAve2} ]")

                        if bp2 < buy_bpAve2: # 코인보유금액이 평균가보다 낮을때 매수시도
                            # 매수할 코인 금액 = 평균가 - 코인보유금액
                            buy_krw_price2 = buy_bpAve2 - bp2
                            # 매수할 코인 갯수 = 매수할 코인 금액 - 현재가
                            buy_krw_balance2 = buy_krw_price2 / price2

                            if krw2 >= buy_krw_price2: # 매수가능금액이 매수할금액보다 클때 매수시도
                                if buy_krw_price2 >= 10000:    # 매수가능금액이 최소주문가능금액인 ￦10,000원보다 높을때 매수시도

                                    # 매수할 코인명 - krw_coin2, 매수할 코인금액 - buy_krw_price2
                                    upbit.buy_market_order(krw_coin2, buy_krw_price2 * 0.9)

                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode2 = 1

                                    print("평균 이하 금액 매수")
                                    print(f"매수한금액 = ￦{buy_krw_price2}  |  매수한수량 = {buy_krw_balance2}  |  매수가능여부 - {op_mode2} - 매수불가-매도가능")
                                    print("")

                                else:
                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode2 = 1

                                    print("매수금액이 ￦10,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode2} - 매수불가-매도가능")
                                    print("")
                            else:   # 보유금액이 평균가와의 차이보다 적을때 매수
                                if krw2 >= 10000:    # 보유금액이 최소주문가능금액인 ￦10,000원보다 높을때 매수시도
                                    # 매수할 코인명 - krw_coin2, 매수할 코인금액 - krw2
                                    upbit.buy_market_order(krw_coin2, krw2 * 0.9)

                                    op_mode2 = 1

                                    print("보유금액보다 매수금액보다 적어서 매수금지")
                                    print(f"매수한금액 = ￦{krw2}  |  매수한수량 = {buy_krw_balance2}  |  매수가능여부 - {op_mode2} - 매수불가-매도가능")
                                    print("")
                                else:
                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode2 = 1

                                    print("보유금액이 ￦10,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode2} - 매수불가-매도가능")
                                    print("")

                        else:
                            # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                            op_mode2 = 1

                            print("보유금액이 평균금액보다 높아서 매수불가")
                            print(f"매수가능여부 - {op_mode2} - 매수불가-매도가능")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################


            ###############################
            # 코인3

            # 코인별 금액 비율조정
            buy_bpAve3 = bpAve * bpPer3

            # MACD 조건문
            if macd3 >= 0:     # macd가 0보다 크거나 같을때는 매수
                # 매수가능금액 불러오기
                krw3 = upbit.get_balance("KRW")

                if coinMode3 == 1 or coinMode3 == 2:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = >>>매수만가능<<< , 3 = 매도만가능
                    if op_mode3 == 2 or op_mode3 == 3:   # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                        print("")
                        print(f"[ 3. 매수시간 : {now}  |  코인명 : {coin3}  |  현재가 = ￦{price3}  |  MACD = ￦{macd3}  |  보유수량 = {krw_balance3}  |  평가금액 = ￦{bp3}  ||  매수평균금액 = ￦{buy_bpAve3} ]")

                        if bp3 < buy_bpAve3: # 코인보유금액이 평균가보다 낮을때 매수시도
                            # 매수할 코인 금액 = 평균가 - 코인보유금액
                            buy_krw_price3 = buy_bpAve3 - bp3
                            # 매수할 코인 갯수 = 매수할 코인 금액 - 현재가
                            buy_krw_balance3 = buy_krw_price3 / price3

                            if krw3 >= buy_krw_price3: # 매수가능금액이 매수할금액보다 클때 매수시도
                                if buy_krw_price3 >= 10000:    # 매수가능금액이 최소주문가능금액인 ￦10,000원보다 높을때 매수시도

                                    # 매수할 코인명 - krw_coin3, 매수할 코인금액 - buy_krw_price3
                                    upbit.buy_market_order(krw_coin3, buy_krw_price3 * 0.9)

                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode3 = 1

                                    print("평균 이하 금액 매수")
                                    print(f"매수한금액 = ￦{buy_krw_price3}  |  매수한수량 = {buy_krw_balance3}  |  매수가능여부 - {op_mode3} - 매수불가-매도가능")
                                    print("")

                                else:
                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode3 = 1

                                    print("매수금액이 ￦10,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode3} - 매수불가-매도가능")
                                    print("")
                            else:   # 보유금액이 평균가와의 차이보다 적을때 매수
                                if krw3 >= 10000:    # 보유금액이 최소주문가능금액인 ￦10,000원보다 높을때 매수시도
                                    # 매수할 코인명 - krw_coin3, 매수할 코인금액 - krw3
                                    upbit.buy_market_order(krw_coin3, krw3 * 0.9)

                                    op_mode3 = 1

                                    print("보유금액보다 매수금액보다 적어서 매수금지")
                                    print(f"매수한금액 = ￦{krw3}  |  매수한수량 = {buy_krw_balance3}  |  매수가능여부 - {op_mode3} - 매수불가-매도가능")
                                    print("")
                                else:
                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode3 = 1

                                    print("보유금액이 ￦10,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode3} - 매수불가-매도가능")
                                    print("")

                        else:
                            # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                            op_mode3 = 1

                            print("보유금액이 평균금액보다 높아서 매수불가")
                            print(f"매수가능여부 - {op_mode3} - 매수불가-매도가능")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################


            ###############################
            # 코인4

            # 코인별 금액 비율조정
            buy_bpAve4 = bpAve * bpPer4

            # MACD 조건문
            if macd4 >= 0:     # macd가 0보다 크거나 같을때는 매수
                # 매수가능금액 불러오기
                krw4 = upbit.get_balance("KRW")

                if coinMode4 == 1 or coinMode4 == 2:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = >>>매수만가능<<< , 3 = 매도만가능
                    if op_mode4 == 2 or op_mode4 == 3:   # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                        print("")
                        print(f"[ 4. 매수시간 : {now}  |  코인명 : {coin4}  |  현재가 = ￦{price4}  |  MACD = ￦{macd4}  |  보유수량 = {krw_balance4}  |  평가금액 = ￦{bp4}  ||  매수평균금액 = ￦{buy_bpAve4} ]")

                        if bp4 < buy_bpAve4: # 코인보유금액이 평균가보다 낮을때 매수시도
                            # 매수할 코인 금액 = 평균가 - 코인보유금액
                            buy_krw_price4 = buy_bpAve4 - bp4
                            # 매수할 코인 갯수 = 매수할 코인 금액 - 현재가
                            buy_krw_balance4 = buy_krw_price4 / price4

                            if krw4 >= buy_krw_price4: # 매수가능금액이 매수할금액보다 클때 매수시도
                                if buy_krw_price4 >= 10000:    # 매수가능금액이 최소주문가능금액인 ￦10,000원보다 높을때 매수시도

                                    # 매수할 코인명 - krw_coin4, 매수할 코인금액 - buy_krw_price4
                                    upbit.buy_market_order(krw_coin4, buy_krw_price4 * 0.9)

                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode4 = 1

                                    print("평균 이하 금액 매수")
                                    print(f"매수한금액 = ￦{buy_krw_price4}  |  매수한수량 = {buy_krw_balance4}  |  매수가능여부 - {op_mode4} - 매수불가-매도가능")
                                    print("")

                                else:
                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode4 = 1

                                    print("매수금액이 ￦10,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode4} - 매수불가-매도가능")
                                    print("")
                            else:   # 보유금액이 평균가와의 차이보다 적을때 매수
                                if krw4 >= 10000:    # 보유금액이 최소주문가능금액인 ￦10,000원보다 높을때 매수시도
                                    # 매수할 코인명 - krw_coin4, 매수할 코인금액 - krw4
                                    upbit.buy_market_order(krw_coin4, krw4 * 0.9)

                                    op_mode4 = 1

                                    print("보유금액보다 매수금액보다 적어서 매수금지")
                                    print(f"매수한금액 = ￦{krw4}  |  매수한수량 = {buy_krw_balance4}  |  매수가능여부 - {op_mode4} - 매수불가-매도가능")
                                    print("")
                                else:
                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode4 = 1

                                    print("보유금액이 ￦10,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode4} - 매수불가-매도가능")
                                    print("")

                        else:
                            # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                            op_mode4 = 1

                            print("보유금액이 평균금액보다 높아서 매수불가")
                            print(f"매수가능여부 - {op_mode4} - 매수불가-매도가능")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################


            ###############################
            # 코인5

            # 코인별 금액 비율조정
            buy_bpAve5 = bpAve * bpPer5

            # MACD 조건문
            if macd5 >= 0:     # macd가 0보다 크거나 같을때는 매수
                # 매수가능금액 불러오기
                krw5 = upbit.get_balance("KRW")

                if coinMode5 == 1 or coinMode5 == 2:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = >>>매수만가능<<< , 3 = 매도만가능
                    if op_mode5 == 2 or op_mode5 == 3:   # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                        print("")
                        print(f"[ 5. 매수시간 : {now}  |  코인명 : {coin5}  |  현재가 = ￦{price5}  |  MACD = ￦{macd5}  |  보유수량 = {krw_balance5}  |  평가금액 = ￦{bp5}  ||  매수평균금액 = ￦{buy_bpAve5} ]")

                        if bp5 < buy_bpAve5: # 코인보유금액이 평균가보다 낮을때 매수시도
                            # 매수할 코인 금액 = 평균가 - 코인보유금액
                            buy_krw_price5 = buy_bpAve5 - bp5
                            # 매수할 코인 갯수 = 매수할 코인 금액 - 현재가
                            buy_krw_balance5 = buy_krw_price5 / price5

                            if krw5 >= buy_krw_price5: # 매수가능금액이 매수할금액보다 클때 매수시도
                                if buy_krw_price5 >= 10000:    # 매수가능금액이 최소주문가능금액인 ￦10,000원보다 높을때 매수시도

                                    # 매수할 코인명 - krw_coin5, 매수할 코인금액 - buy_krw_price5
                                    upbit.buy_market_order(krw_coin5, buy_krw_price5 * 0.9)

                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode5 = 1

                                    print("평균 이하 금액 매수")
                                    print(f"매수한금액 = ￦{buy_krw_price5}  |  매수한수량 = {buy_krw_balance5}  |  매수가능여부 - {op_mode5} - 매수불가-매도가능")
                                    print("")

                                else:
                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode5 = 1

                                    print("매수금액이 ￦10,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode5} - 매수불가-매도가능")
                                    print("")
                            else:   # 보유금액이 평균가와의 차이보다 적을때 매수
                                if krw5 >= 10000:    # 보유금액이 최소주문가능금액인 ￦10,000원보다 높을때 매수시도
                                    # 매수할 코인명 - krw_coin5, 매수할 코인금액 - krw5
                                    upbit.buy_market_order(krw_coin5, krw5 * 0.9)

                                    op_mode5 = 1

                                    print("보유금액보다 매수금액보다 적어서 매수금지")
                                    print(f"매수한금액 = ￦{krw5}  |  매수한수량 = {buy_krw_balance5}  |  매수가능여부 - {op_mode5} - 매수불가-매도가능")
                                    print("")
                                else:
                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode5 = 1

                                    print("보유금액이 ￦10,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode5} - 매수불가-매도가능")
                                    print("")
                            

                        else:
                            # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                            op_mode5 = 1

                            print("보유금액이 평균금액보다 높아서 매수불가")
                            print(f"매수가능여부 - {op_mode5} - 매수불가-매도가능")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################


            ###############################
            # 코인6

            # 코인별 금액 비율조정
            buy_bpAve6 = bpAve * bpPer6

            # MACD 조건문
            if macd6 >= 0:     # macd가 0보다 크거나 같을때는 매수
                # 매수가능금액 불러오기
                krw6 = upbit.get_balance("KRW")

                if coinMode6 == 1 or coinMode6 == 2:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = >>>매수만가능<<< , 3 = 매도만가능
                    if op_mode6 == 2 or op_mode6 == 3:   # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                        print("")
                        print(f"[ 6. 매수시간 : {now}  |  코인명 : {coin6}  |  현재가 = ￦{price6}  |  MACD = ￦{macd6}  |  보유수량 = {krw_balance6}  |  평가금액 = ￦{bp6}  ||  매수평균금액 = ￦{buy_bpAve6} ]")

                        if bp6 < buy_bpAve6: # 코인보유금액이 평균가보다 낮을때 매수시도
                            # 매수할 코인 금액 = 평균가 - 코인보유금액
                            buy_krw_price6 = buy_bpAve6 - bp6
                            # 매수할 코인 갯수 = 매수할 코인 금액 - 현재가
                            buy_krw_balance6 = buy_krw_price6 / price6

                            if krw6 >= buy_krw_price6: # 매수가능금액이 매수할금액보다 클때 매수시도
                                if buy_krw_price6 >= 10000:    # 매수가능금액이 최소주문가능금액인 ￦10,000원보다 높을때 매수시도

                                    # 매수할 코인명 - krw_coin6, 매수할 코인금액 - buy_krw_price6
                                    upbit.buy_market_order(krw_coin6, buy_krw_price6 * 0.9)

                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode6 = 1

                                    print("평균 이하 금액 매수")
                                    print(f"매수한금액 = ￦{buy_krw_price6}  |  매수한수량 = {buy_krw_balance6}  |  매수가능여부 - {op_mode6} - 매수불가-매도가능")
                                    print("")

                                else:
                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode6 = 1

                                    print("매수금액이 ￦10,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode6} - 매수불가-매도가능")
                                    print("")
                            else:   # 보유금액이 평균가와의 차이보다 적을때 매수
                                if krw6 >= 10000:    # 보유금액이 최소주문가능금액인 ￦10,000원보다 높을때 매수시도
                                    # 매수할 코인명 - krw_coin6, 매수할 코인금액 - krw6
                                    upbit.buy_market_order(krw_coin6, krw6 * 0.9)

                                    op_mode6 = 1

                                    print("보유금액보다 매수금액보다 적어서 매수금지")
                                    print(f"매수한금액 = ￦{krw6}  |  매수한수량 = {buy_krw_balance6}  |  매수가능여부 - {op_mode6} - 매수불가-매도가능")
                                    print("")
                                else:
                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode6 = 1

                                    print("보유금액이 ￦10,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode6} - 매수불가-매도가능")
                                    print("")

                        else:
                            # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                            op_mode6 = 1

                            print("보유금액이 평균금액보다 높아서 매수불가")
                            print(f"매수가능여부 - {op_mode6} - 매수불가-매도가능")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################


            ###############################
            # 코인7

            # 코인별 금액 비율조정
            buy_bpAve7 = bpAve * bpPer7

            # MACD 조건문
            if macd7 >= 0:     # macd가 0보다 크거나 같을때는 매수
                # 매수가능금액 불러오기
                krw7 = upbit.get_balance("KRW")

                if coinMode7 == 1 or coinMode7 == 2:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = >>>매수만가능<<< , 3 = 매도만가능
                    if op_mode7 == 2 or op_mode7 == 3:   # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                        print("")
                        print(f"[ 7. 매수시간 : {now}  |  코인명 : {coin7}  |  현재가 = ￦{price7}  |  MACD = ￦{macd7}  |  보유수량 = {krw_balance7}  |  평가금액 = ￦{bp7}  ||  매수평균금액 = ￦{buy_bpAve7} ]")

                        if bp7 < buy_bpAve7: # 코인보유금액이 평균가보다 낮을때 매수시도
                            # 매수할 코인 금액 = 평균가 - 코인보유금액
                            buy_krw_price7 = buy_bpAve7 - bp7
                            # 매수할 코인 갯수 = 매수할 코인 금액 - 현재가
                            buy_krw_balance7 = buy_krw_price7 / price7

                            if krw7 >= buy_krw_price7: # 매수가능금액이 매수할금액보다 클때 매수시도
                                if buy_krw_price7 >= 10000:    # 매수가능금액이 최소주문가능금액인 ￦10,000원보다 높을때 매수시도

                                    # 매수할 코인명 - krw_coin7, 매수할 코인금액 - buy_krw_price7
                                    upbit.buy_market_order(krw_coin7, buy_krw_price7 * 0.9)

                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode7 = 1

                                    print("평균 이하 금액 매수")
                                    print(f"매수한금액 = ￦{buy_krw_price7}  |  매수한수량 = {buy_krw_balance7}  |  매수가능여부 - {op_mode7} - 매수불가-매도가능")
                                    print("")

                                else:
                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode7 = 1

                                    print("매수금액이 ￦10,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode7} - 매수불가-매도가능")
                                    print("")
                            else:   # 보유금액이 평균가와의 차이보다 적을때 매수
                                if krw7 >= 10000:    # 보유금액이 최소주문가능금액인 ￦10,000원보다 높을때 매수시도
                                    # 매수할 코인명 - krw_coin7, 매수할 코인금액 - krw7
                                    upbit.buy_market_order(krw_coin7, krw7 * 0.9)

                                    op_mode7 = 1

                                    print("보유금액보다 매수금액보다 적어서 매수금지")
                                    print(f"매수한금액 = ￦{krw7}  |  매수한수량 = {buy_krw_balance7}  |  매수가능여부 - {op_mode7} - 매수불가-매도가능")
                                    print("")
                                else:
                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode7 = 1

                                    print("보유금액이 ￦10,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode7} - 매수불가-매도가능")
                                    print("")

                        else:
                            # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                            op_mode7 = 1

                            print("보유금액이 평균금액보다 높아서 매수불가")
                            print(f"매수가능여부 - {op_mode7} - 매수불가-매도가능")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################


            ###############################
            # 코인8

            # 코인별 금액 비율조정
            buy_bpAve8 = bpAve * bpPer8

            # MACD 조건문
            if macd8 >= 0:     # macd가 0보다 크거나 같을때는 매수
                # 매수가능금액 불러오기
                krw8 = upbit.get_balance("KRW")

                if coinMode8 == 1 or coinMode8 == 2:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = >>>매수만가능<<< , 3 = 매도만가능
                    if op_mode8 == 2 or op_mode8 == 3:   # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                        print("")
                        print(f"[ 8. 매수시간 : {now}  |  코인명 : {coin8}  |  현재가 = ￦{price8}  |  MACD = ￦{macd8}  |  보유수량 = {krw_balance8}  |  평가금액 = ￦{bp8}  ||  매수평균금액 = ￦{buy_bpAve8} ]")

                        if bp8 < buy_bpAve8: # 코인보유금액이 평균가보다 낮을때 매수시도
                            # 매수할 코인 금액 = 평균가 - 코인보유금액
                            buy_krw_price8 = buy_bpAve8 - bp8
                            # 매수할 코인 갯수 = 매수할 코인 금액 - 현재가
                            buy_krw_balance8 = buy_krw_price8 / price8

                            if krw8 >= buy_krw_price8: # 매수가능금액이 매수할금액보다 클때 매수시도
                                if buy_krw_price8 >= 10000:    # 매수가능금액이 최소주문가능금액인 ￦10,000원보다 높을때 매수시도

                                    # 매수할 코인명 - krw_coin8, 매수할 코인금액 - buy_krw_price8
                                    upbit.buy_market_order(krw_coin8, buy_krw_price8 * 0.9)

                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode8 = 1

                                    print("평균 이하 금액 매수")
                                    print(f"매수한금액 = ￦{buy_krw_price8}  |  매수한수량 = {buy_krw_balance8}  |  매수가능여부 - {op_mode8} - 매수불가-매도가능")
                                    print("")

                                else:
                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode8 = 1

                                    print("매수금액이 ￦10,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode8} - 매수불가-매도가능")
                                    print("")
                            else:   # 보유금액이 평균가와의 차이보다 적을때 매수
                                if krw8 >= 10000:    # 보유금액이 최소주문가능금액인 ￦10,000원보다 높을때 매수시도
                                    # 매수할 코인명 - krw_coin8, 매수할 코인금액 - krw8
                                    upbit.buy_market_order(krw_coin8, krw8 * 0.9)

                                    op_mode8 = 1

                                    print("보유금액보다 매수금액보다 적어서 매수금지")
                                    print(f"매수한금액 = ￦{krw8}  |  매수한수량 = {buy_krw_balance8}  |  매수가능여부 - {op_mode8} - 매수불가-매도가능")
                                    print("")
                                else:
                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode8 = 1

                                    print("보유금액이 ￦10,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode8} - 매수불가-매도가능")
                                    print("")

                        else:
                            # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                            op_mode8 = 1

                            print("보유금액이 평균금액보다 높아서 매수불가")
                            print(f"매수가능여부 - {op_mode8} - 매수불가-매도가능")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################


            ###############################
            # 코인9

            # 코인별 금액 비율조정
            buy_bpAve9 = bpAve * bpPer9

            # MACD 조건문
            if macd9 >= 0:     # macd가 0보다 크거나 같을때는 매수
                # 매수가능금액 불러오기
                krw9 = upbit.get_balance("KRW")

                if coinMode9 == 1 or coinMode9 == 2:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = >>>매수만가능<<< , 3 = 매도만가능
                    if op_mode9 == 2 or op_mode9 == 3:   # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                        print("")
                        print(f"[ 9. 매수시간 : {now}  |  코인명 : {coin9}  |  현재가 = ￦{price9}  |  MACD = ￦{macd9}  |  보유수량 = {krw_balance9}  |  평가금액 = ￦{bp9}  ||  매수평균금액 = ￦{buy_bpAve9} ]")

                        if bp9 < buy_bpAve9: # 코인보유금액이 평균가보다 낮을때 매수시도
                            # 매수할 코인 금액 = 평균가 - 코인보유금액
                            buy_krw_price9 = buy_bpAve9 - bp9
                            # 매수할 코인 갯수 = 매수할 코인 금액 - 현재가
                            buy_krw_balance9 = buy_krw_price9 / price9

                            if krw9 >= buy_krw_price9: # 매수가능금액이 매수할금액보다 클때 매수시도
                                if buy_krw_price9 >= 10000:    # 매수가능금액이 최소주문가능금액인 ￦10,000원보다 높을때 매수시도

                                    # 매수할 코인명 - krw_coin9, 매수할 코인금액 - buy_krw_price9
                                    upbit.buy_market_order(krw_coin9, buy_krw_price9 * 0.9)

                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode9 = 1

                                    print("평균 이하 금액 매수")
                                    print(f"매수한금액 = ￦{buy_krw_price9}  |  매수한수량 = {buy_krw_balance9}  |  매수가능여부 - {op_mode9} - 매수불가-매도가능")
                                    print("")

                                else:
                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode9 = 1

                                    print("매수금액이 ￦10,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode9} - 매수불가-매도가능")
                                    print("")
                            else:   # 보유금액이 평균가와의 차이보다 적을때 매수
                                if krw9 >= 10000:    # 보유금액이 최소주문가능금액인 ￦10,000원보다 높을때 매수시도
                                    # 매수할 코인명 - krw_coin9, 매수할 코인금액 - krw9
                                    upbit.buy_market_order(krw_coin9, krw9 * 0.9)

                                    op_mode9 = 1

                                    print("보유금액보다 매수금액보다 적어서 매수금지")
                                    print(f"매수한금액 = ￦{krw9}  |  매수한수량 = {buy_krw_balance9}  |  매수가능여부 - {op_mode9} - 매수불가-매도가능")
                                    print("")
                                else:
                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode9 = 1

                                    print("보유금액이 ￦10,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode9} - 매수불가-매도가능")
                                    print("")

                        else:
                            # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                            op_mode9 = 1

                            print("보유금액이 평균금액보다 높아서 매수불가")
                            print(f"매수가능여부 - {op_mode9} - 매수불가-매도가능")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################


            ###############################
            # 코인10

            # 코인별 금액 비율조정
            buy_bpAve10 = bpAve * bpPer10

            # MACD 조건문
            if macd10 >= 0:     # macd가 0보다 크거나 같을때는 매수
                # 매수가능금액 불러오기
                krw10 = upbit.get_balance("KRW")

                if coinMode10 == 1 or coinMode10 == 2:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = >>>매수만가능<<< , 3 = 매도만가능
                    if op_mode10 == 2 or op_mode10 == 3:   # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                        print("")
                        print(f"[ 10. 매수시간 : {now}  |  코인명 : {coin10}  |  현재가 = ￦{price10}  |  MACD = ￦{macd10}  |  보유수량 = {krw_balance10}  |  평가금액 = ￦{bp10}  ||  매수평균금액 = ￦{buy_bpAve10} ]")

                        if bp10 < buy_bpAve10: # 코인보유금액이 평균가보다 낮을때 매수시도
                            # 매수할 코인 금액 = 평균가 - 코인보유금액
                            buy_krw_price10 = buy_bpAve10 - bp10
                            # 매수할 코인 갯수 = 매수할 코인 금액 - 현재가
                            buy_krw_balance10 = buy_krw_price10 / price10

                            if krw10 >= buy_krw_price10: # 매수가능금액이 매수할금액보다 클때 매수시도
                                if buy_krw_price10 >= 10000:    # 매수가능금액이 최소주문가능금액인 ￦10,000원보다 높을때 매수시도

                                    # 매수할 코인명 - krw_coin10, 매수할 코인금액 - buy_krw_price10
                                    upbit.buy_market_order(krw_coin10, buy_krw_price10 * 0.9)

                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode10 = 1

                                    print("평균 이하 금액 매수")
                                    print(f"매수한금액 = ￦{buy_krw_price10}  |  매수한수량 = {buy_krw_balance10}  |  매수가능여부 - {op_mode10} - 매수불가-매도가능")
                                    print("")

                                else:
                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode10 = 1

                                    print("매수금액이 ￦10,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode10} - 매수불가-매도가능")
                                    print("")
                            else:   # 보유금액이 평균가와의 차이보다 적을때 매수
                                if krw10 >= 10000:    # 보유금액이 최소주문가능금액인 ￦10,000원보다 높을때 매수시도
                                    # 매수할 코인명 - krw_coin10, 매수할 코인금액 - krw10
                                    upbit.buy_market_order(krw_coin10, krw10 * 0.9)

                                    op_mode10 = 1

                                    print("보유금액보다 매수금액보다 적어서 매수금지")
                                    print(f"매수한금액 = ￦{krw10}  |  매수한수량 = {buy_krw_balance10}  |  매수가능여부 - {op_mode10} - 매수불가-매도가능")
                                    print("")
                                else:
                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode10 = 1

                                    print("보유금액이 ￦10,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode10} - 매수불가-매도가능")
                                    print("")

                        else:
                            # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
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





            ###############################
            # 코인11

            # 코인별 금액 비율조정
            buy_bpAve11 = bpAve * bpPer11

            # MACD 조건문
            if macd11 >= 0:     # macd가 0보다 크거나 같을때는 매수
                # 매수가능금액 불러오기
                krw11 = upbit.get_balance("KRW")

                if coinMode11 == 1 or coinMode11 == 2:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = >>>매수만가능<<< , 3 = 매도만가능
                    if op_mode11 == 2 or op_mode11 == 3:   # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                        print("")
                        print(f"[ 11. 매수시간 : {now}  |  코인명 : {coin11}  |  현재가 = ￦{price11}  |  MACD = ￦{macd11}  |  보유수량 = {krw_balance11}  |  평가금액 = ￦{bp11}  ||  매수평균금액 = ￦{buy_bpAve11} ]")

                        if bp11 < buy_bpAve11: # 코인보유금액이 평균가보다 낮을때 매수시도
                            # 매수할 코인 금액 = 평균가 - 코인보유금액
                            buy_krw_price11 = buy_bpAve11 - bp11
                            # 매수할 코인 갯수 = 매수할 코인 금액 - 현재가
                            buy_krw_balance11 = buy_krw_price11 / price11

                            if krw11 >= buy_krw_price11: # 매수가능금액이 매수할금액보다 클때 매수시도
                                if buy_krw_price11 >= 10000:    # 매수가능금액이 최소주문가능금액인 ￦10,000원보다 높을때 매수시도

                                    # 매수할 코인명 - krw_coin11, 매수할 코인금액 - buy_krw_price11
                                    upbit.buy_market_order(krw_coin11, buy_krw_price11 * 0.9)

                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode11 = 1

                                    print("평균 이하 금액 매수")
                                    print(f"매수한금액 = ￦{buy_krw_price11}  |  매수한수량 = {buy_krw_balance11}  |  매수가능여부 - {op_mode11} - 매수불가-매도가능")
                                    print("")

                                else:
                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode11 = 1

                                    print("매수금액이 ￦10,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode11} - 매수불가-매도가능")
                                    print("")
                            else:   # 보유금액이 평균가와의 차이보다 적을때 매수
                                if krw11 >= 10000:    # 보유금액이 최소주문가능금액인 ￦10,000원보다 높을때 매수시도
                                    # 매수할 코인명 - krw_coin11, 매수할 코인금액 - krw11
                                    upbit.buy_market_order(krw_coin11, krw11 * 0.9)

                                    op_mode11 = 1

                                    print("보유금액보다 매수금액보다 적어서 매수금지")
                                    print(f"매수한금액 = ￦{krw11}  |  매수한수량 = {buy_krw_balance11}  |  매수가능여부 - {op_mode11} - 매수불가-매도가능")
                                    print("")
                                else:
                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode11 = 1

                                    print("보유금액이 ￦10,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode11} - 매수불가-매도가능")
                                    print("")

                        else:
                            # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                            op_mode11 = 1

                            print("보유금액이 평균금액보다 높아서 매수불가")
                            print(f"매수가능여부 - {op_mode11} - 매수불가-매도가능")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################


            ###############################
            # 코인12

            # 코인별 금액 비율조정
            buy_bpAve12 = bpAve * bpPer12

            # MACD 조건문
            if macd12 >= 0:     # macd가 0보다 크거나 같을때는 매수
                # 매수가능금액 불러오기
                krw12 = upbit.get_balance("KRW")

                if coinMode12 == 1 or coinMode12 == 2:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = >>>매수만가능<<< , 3 = 매도만가능
                    if op_mode12 == 2 or op_mode12 == 3:   # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                        print("")
                        print(f"[ 12. 매수시간 : {now}  |  코인명 : {coin12}  |  현재가 = ￦{price12}  |  MACD = ￦{macd12}  |  보유수량 = {krw_balance12}  |  평가금액 = ￦{bp12}  ||  매수평균금액 = ￦{buy_bpAve12} ]")

                        if bp12 < buy_bpAve12: # 코인보유금액이 평균가보다 낮을때 매수시도
                            # 매수할 코인 금액 = 평균가 - 코인보유금액
                            buy_krw_price12 = buy_bpAve12 - bp12
                            # 매수할 코인 갯수 = 매수할 코인 금액 - 현재가
                            buy_krw_balance12 = buy_krw_price12 / price12

                            if krw12 >= buy_krw_price12: # 매수가능금액이 매수할금액보다 클때 매수시도
                                if buy_krw_price12 >= 10000:    # 매수가능금액이 최소주문가능금액인 ￦10,000원보다 높을때 매수시도

                                    # 매수할 코인명 - krw_coin12, 매수할 코인금액 - buy_krw_price12
                                    upbit.buy_market_order(krw_coin12, buy_krw_price12 * 0.9)

                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode12 = 1

                                    print("평균 이하 금액 매수")
                                    print(f"매수한금액 = ￦{buy_krw_price12}  |  매수한수량 = {buy_krw_balance12}  |  매수가능여부 - {op_mode12} - 매수불가-매도가능")
                                    print("")

                                else:
                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode12 = 1

                                    print("매수금액이 ￦10,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode12} - 매수불가-매도가능")
                                    print("")
                            else:   # 보유금액이 평균가와의 차이보다 적을때 매수
                                if krw12 >= 10000:    # 보유금액이 최소주문가능금액인 ￦10,000원보다 높을때 매수시도
                                    # 매수할 코인명 - krw_coin12, 매수할 코인금액 - krw12
                                    upbit.buy_market_order(krw_coin12, krw12 * 0.9)

                                    op_mode12 = 1

                                    print("보유금액보다 매수금액보다 적어서 매수금지")
                                    print(f"매수한금액 = ￦{krw12}  |  매수한수량 = {buy_krw_balance12}  |  매수가능여부 - {op_mode12} - 매수불가-매도가능")
                                    print("")
                                else:
                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode12 = 1

                                    print("보유금액이 ￦10,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode12} - 매수불가-매도가능")
                                    print("")

                        else:
                            # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                            op_mode12 = 1

                            print("보유금액이 평균금액보다 높아서 매수불가")
                            print(f"매수가능여부 - {op_mode12} - 매수불가-매도가능")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################


            ###############################
            # 코인13

            # 코인별 금액 비율조정
            buy_bpAve13 = bpAve * bpPer13

            # MACD 조건문
            if macd13 >= 0:     # macd가 0보다 크거나 같을때는 매수
                # 매수가능금액 불러오기
                krw13 = upbit.get_balance("KRW")

                if coinMode13 == 1 or coinMode13 == 2:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = >>>매수만가능<<< , 3 = 매도만가능
                    if op_mode13 == 2 or op_mode13 == 3:   # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                        print("")
                        print(f"[ 13. 매수시간 : {now}  |  코인명 : {coin13}  |  현재가 = ￦{price13}  |  MACD = ￦{macd13}  |  보유수량 = {krw_balance13}  |  평가금액 = ￦{bp13}  ||  매수평균금액 = ￦{buy_bpAve13} ]")

                        if bp13 < buy_bpAve13: # 코인보유금액이 평균가보다 낮을때 매수시도
                            # 매수할 코인 금액 = 평균가 - 코인보유금액
                            buy_krw_price13 = buy_bpAve13 - bp13
                            # 매수할 코인 갯수 = 매수할 코인 금액 - 현재가
                            buy_krw_balance13 = buy_krw_price13 / price13

                            if krw13 >= buy_krw_price13: # 매수가능금액이 매수할금액보다 클때 매수시도
                                if buy_krw_price13 >= 10000:    # 매수가능금액이 최소주문가능금액인 ￦10,000원보다 높을때 매수시도

                                    # 매수할 코인명 - krw_coin13, 매수할 코인금액 - buy_krw_price13
                                    upbit.buy_market_order(krw_coin13, buy_krw_price13 * 0.9)

                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode13 = 1

                                    print("평균 이하 금액 매수")
                                    print(f"매수한금액 = ￦{buy_krw_price13}  |  매수한수량 = {buy_krw_balance13}  |  매수가능여부 - {op_mode13} - 매수불가-매도가능")
                                    print("")

                                else:
                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode13 = 1

                                    print("매수금액이 ￦10,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode13} - 매수불가-매도가능")
                                    print("")
                            else:   # 보유금액이 평균가와의 차이보다 적을때 매수
                                if krw13 >= 10000:    # 보유금액이 최소주문가능금액인 ￦10,000원보다 높을때 매수시도
                                    # 매수할 코인명 - krw_coin13, 매수할 코인금액 - krw13
                                    upbit.buy_market_order(krw_coin13, krw13 * 0.9)

                                    op_mode13 = 1

                                    print("보유금액보다 매수금액보다 적어서 매수금지")
                                    print(f"매수한금액 = ￦{krw13}  |  매수한수량 = {buy_krw_balance13}  |  매수가능여부 - {op_mode13} - 매수불가-매도가능")
                                    print("")
                                else:
                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode13 = 1

                                    print("보유금액이 ￦10,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode13} - 매수불가-매도가능")
                                    print("")

                        else:
                            # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                            op_mode13 = 1

                            print("보유금액이 평균금액보다 높아서 매수불가")
                            print(f"매수가능여부 - {op_mode13} - 매수불가-매도가능")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################


            ###############################
            # 코인14

            # 코인별 금액 비율조정
            buy_bpAve14 = bpAve * bpPer14

            # MACD 조건문
            if macd14 >= 0:     # macd가 0보다 크거나 같을때는 매수
                # 매수가능금액 불러오기
                krw14 = upbit.get_balance("KRW")

                if coinMode14 == 1 or coinMode14 == 2:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = >>>매수만가능<<< , 3 = 매도만가능
                    if op_mode14 == 2 or op_mode14 == 3:   # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                        print("")
                        print(f"[ 14. 매수시간 : {now}  |  코인명 : {coin14}  |  현재가 = ￦{price14}  |  MACD = ￦{macd14}  |  보유수량 = {krw_balance14}  |  평가금액 = ￦{bp14}  ||  매수평균금액 = ￦{buy_bpAve14} ]")

                        if bp14 < buy_bpAve14: # 코인보유금액이 평균가보다 낮을때 매수시도
                            # 매수할 코인 금액 = 평균가 - 코인보유금액
                            buy_krw_price14 = buy_bpAve14 - bp14
                            # 매수할 코인 갯수 = 매수할 코인 금액 - 현재가
                            buy_krw_balance14 = buy_krw_price14 / price14

                            if krw14 >= buy_krw_price14: # 매수가능금액이 매수할금액보다 클때 매수시도
                                if buy_krw_price14 >= 10000:    # 매수가능금액이 최소주문가능금액인 ￦10,000원보다 높을때 매수시도

                                    # 매수할 코인명 - krw_coin14, 매수할 코인금액 - buy_krw_price14
                                    upbit.buy_market_order(krw_coin14, buy_krw_price14 * 0.9)

                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode14 = 1

                                    print("평균 이하 금액 매수")
                                    print(f"매수한금액 = ￦{buy_krw_price14}  |  매수한수량 = {buy_krw_balance14}  |  매수가능여부 - {op_mode14} - 매수불가-매도가능")
                                    print("")

                                else:
                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode14 = 1

                                    print("매수금액이 ￦10,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode14} - 매수불가-매도가능")
                                    print("")
                            else:   # 보유금액이 평균가와의 차이보다 적을때 매수
                                if krw14 >= 10000:    # 보유금액이 최소주문가능금액인 ￦10,000원보다 높을때 매수시도
                                    # 매수할 코인명 - krw_coin14, 매수할 코인금액 - krw14
                                    upbit.buy_market_order(krw_coin14, krw14 * 0.9)

                                    op_mode14 = 1

                                    print("보유금액보다 매수금액보다 적어서 매수금지")
                                    print(f"매수한금액 = ￦{krw14}  |  매수한수량 = {buy_krw_balance14}  |  매수가능여부 - {op_mode14} - 매수불가-매도가능")
                                    print("")
                                else:
                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode14 = 1

                                    print("보유금액이 ￦10,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode14} - 매수불가-매도가능")
                                    print("")

                        else:
                            # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                            op_mode14 = 1

                            print("보유금액이 평균금액보다 높아서 매수불가")
                            print(f"매수가능여부 - {op_mode14} - 매수불가-매도가능")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################


            ###############################
            # 코인15

            # 코인별 금액 비율조정
            buy_bpAve15 = bpAve * bpPer15

            # MACD 조건문
            if macd15 >= 0:     # macd가 0보다 크거나 같을때는 매수
                # 매수가능금액 불러오기
                krw15 = upbit.get_balance("KRW")

                if coinMode15 == 1 or coinMode15 == 2:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = >>>매수만가능<<< , 3 = 매도만가능
                    if op_mode15 == 2 or op_mode15 == 3:   # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                        print("")
                        print(f"[ 15. 매수시간 : {now}  |  코인명 : {coin15}  |  현재가 = ￦{price15}  |  MACD = ￦{macd15}  |  보유수량 = {krw_balance15}  |  평가금액 = ￦{bp15}  ||  매수평균금액 = ￦{buy_bpAve15} ]")

                        if bp15 < buy_bpAve15: # 코인보유금액이 평균가보다 낮을때 매수시도
                            # 매수할 코인 금액 = 평균가 - 코인보유금액
                            buy_krw_price15 = buy_bpAve15 - bp15
                            # 매수할 코인 갯수 = 매수할 코인 금액 - 현재가
                            buy_krw_balance15 = buy_krw_price15 / price15

                            if krw15 >= buy_krw_price15: # 매수가능금액이 매수할금액보다 클때 매수시도
                                if buy_krw_price15 >= 10000:    # 매수가능금액이 최소주문가능금액인 ￦10,000원보다 높을때 매수시도

                                    # 매수할 코인명 - krw_coin15, 매수할 코인금액 - buy_krw_price15
                                    upbit.buy_market_order(krw_coin15, buy_krw_price15 * 0.9)

                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode15 = 1

                                    print("평균 이하 금액 매수")
                                    print(f"매수한금액 = ￦{buy_krw_price15}  |  매수한수량 = {buy_krw_balance15}  |  매수가능여부 - {op_mode15} - 매수불가-매도가능")
                                    print("")

                                else:
                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode15 = 1

                                    print("매수금액이 ￦10,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode15} - 매수불가-매도가능")
                                    print("")
                            else:   # 보유금액이 평균가와의 차이보다 적을때 매수
                                if krw15 >= 10000:    # 보유금액이 최소주문가능금액인 ￦10,000원보다 높을때 매수시도
                                    # 매수할 코인명 - krw_coin15, 매수할 코인금액 - krw15
                                    upbit.buy_market_order(krw_coin15, krw15 * 0.9)

                                    op_mode15 = 1

                                    print("보유금액보다 매수금액보다 적어서 매수금지")
                                    print(f"매수한금액 = ￦{krw15}  |  매수한수량 = {buy_krw_balance15}  |  매수가능여부 - {op_mode15} - 매수불가-매도가능")
                                    print("")
                                else:
                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode15 = 1

                                    print("보유금액이 ￦10,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode15} - 매수불가-매도가능")
                                    print("")

                        else:
                            # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                            op_mode15 = 1

                            print("보유금액이 평균금액보다 높아서 매수불가")
                            print(f"매수가능여부 - {op_mode15} - 매수불가-매도가능")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################


            ###############################
            # 코인16

            # 코인별 금액 비율조정
            buy_bpAve16 = bpAve * bpPer16

            # MACD 조건문
            if macd16 >= 0:     # macd가 0보다 크거나 같을때는 매수
                # 매수가능금액 불러오기
                krw16 = upbit.get_balance("KRW")

                if coinMode16 == 1 or coinMode16 == 2:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = >>>매수만가능<<< , 3 = 매도만가능
                    if op_mode16 == 2 or op_mode16 == 3:   # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                        print("")
                        print(f"[ 16. 매수시간 : {now}  |  코인명 : {coin16}  |  현재가 = ￦{price16}  |  MACD = ￦{macd16}  |  보유수량 = {krw_balance16}  |  평가금액 = ￦{bp16}  ||  매수평균금액 = ￦{buy_bpAve16} ]")

                        if bp16 < buy_bpAve16: # 코인보유금액이 평균가보다 낮을때 매수시도
                            # 매수할 코인 금액 = 평균가 - 코인보유금액
                            buy_krw_price16 = buy_bpAve16 - bp16
                            # 매수할 코인 갯수 = 매수할 코인 금액 - 현재가
                            buy_krw_balance16 = buy_krw_price16 / price16

                            if krw16 >= buy_krw_price16: # 매수가능금액이 매수할금액보다 클때 매수시도
                                if buy_krw_price16 >= 10000:    # 매수가능금액이 최소주문가능금액인 ￦10,000원보다 높을때 매수시도

                                    # 매수할 코인명 - krw_coin16, 매수할 코인금액 - buy_krw_price16
                                    upbit.buy_market_order(krw_coin16, buy_krw_price16 * 0.9)

                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode16 = 1

                                    print("평균 이하 금액 매수")
                                    print(f"매수한금액 = ￦{buy_krw_price16}  |  매수한수량 = {buy_krw_balance16}  |  매수가능여부 - {op_mode16} - 매수불가-매도가능")
                                    print("")

                                else:
                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode16 = 1

                                    print("매수금액이 ￦10,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode16} - 매수불가-매도가능")
                                    print("")
                            else:   # 보유금액이 평균가와의 차이보다 적을때 매수
                                if krw16 >= 10000:    # 보유금액이 최소주문가능금액인 ￦10,000원보다 높을때 매수시도
                                    # 매수할 코인명 - krw_coin16, 매수할 코인금액 - krw16
                                    upbit.buy_market_order(krw_coin16, krw16 * 0.9)

                                    op_mode16 = 1

                                    print("보유금액보다 매수금액보다 적어서 매수금지")
                                    print(f"매수한금액 = ￦{krw16}  |  매수한수량 = {buy_krw_balance16}  |  매수가능여부 - {op_mode16} - 매수불가-매도가능")
                                    print("")
                                else:
                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode16 = 1

                                    print("보유금액이 ￦10,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode16} - 매수불가-매도가능")
                                    print("")

                        else:
                            # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                            op_mode16 = 1

                            print("보유금액이 평균금액보다 높아서 매수불가")
                            print(f"매수가능여부 - {op_mode16} - 매수불가-매도가능")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################


            ###############################
            # 코인17

            # 코인별 금액 비율조정
            buy_bpAve17 = bpAve * bpPer17

            # MACD 조건문
            if macd17 >= 0:     # macd가 0보다 크거나 같을때는 매수
                # 매수가능금액 불러오기
                krw17 = upbit.get_balance("KRW")

                if coinMode17 == 1 or coinMode17 == 2:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = >>>매수만가능<<< , 3 = 매도만가능
                    if op_mode17 == 2 or op_mode17 == 3:   # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                        print("")
                        print(f"[ 17. 매수시간 : {now}  |  코인명 : {coin17}  |  현재가 = ￦{price17}  |  MACD = ￦{macd17}  |  보유수량 = {krw_balance17}  |  평가금액 = ￦{bp17}  ||  매수평균금액 = ￦{buy_bpAve17} ]")

                        if bp17 < buy_bpAve17: # 코인보유금액이 평균가보다 낮을때 매수시도
                            # 매수할 코인 금액 = 평균가 - 코인보유금액
                            buy_krw_price17 = buy_bpAve17 - bp17
                            # 매수할 코인 갯수 = 매수할 코인 금액 - 현재가
                            buy_krw_balance17 = buy_krw_price17 / price17

                            if krw17 >= buy_krw_price17: # 매수가능금액이 매수할금액보다 클때 매수시도
                                if buy_krw_price17 >= 10000:    # 매수가능금액이 최소주문가능금액인 ￦10,000원보다 높을때 매수시도

                                    # 매수할 코인명 - krw_coin17, 매수할 코인금액 - buy_krw_price17
                                    upbit.buy_market_order(krw_coin17, buy_krw_price17 * 0.9)

                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode17 = 1

                                    print("평균 이하 금액 매수")
                                    print(f"매수한금액 = ￦{buy_krw_price17}  |  매수한수량 = {buy_krw_balance17}  |  매수가능여부 - {op_mode17} - 매수불가-매도가능")
                                    print("")

                                else:
                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode17 = 1

                                    print("매수금액이 ￦10,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode17} - 매수불가-매도가능")
                                    print("")
                            else:   # 보유금액이 평균가와의 차이보다 적을때 매수
                                if krw17 >= 10000:    # 보유금액이 최소주문가능금액인 ￦10,000원보다 높을때 매수시도
                                    # 매수할 코인명 - krw_coin17, 매수할 코인금액 - krw17
                                    upbit.buy_market_order(krw_coin17, krw17 * 0.9)

                                    op_mode17 = 1

                                    print("보유금액보다 매수금액보다 적어서 매수금지")
                                    print(f"매수한금액 = ￦{krw17}  |  매수한수량 = {buy_krw_balance17}  |  매수가능여부 - {op_mode17} - 매수불가-매도가능")
                                    print("")
                                else:
                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode17 = 1

                                    print("보유금액이 ￦10,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode17} - 매수불가-매도가능")
                                    print("")

                        else:
                            # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                            op_mode17 = 1

                            print("보유금액이 평균금액보다 높아서 매수불가")
                            print(f"매수가능여부 - {op_mode17} - 매수불가-매도가능")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################


            ###############################
            # 코인18

            # 코인별 금액 비율조정
            buy_bpAve18 = bpAve * bpPer18

            # MACD 조건문
            if macd18 >= 0:     # macd가 0보다 크거나 같을때는 매수
                # 매수가능금액 불러오기
                krw18 = upbit.get_balance("KRW")

                if coinMode18 == 1 or coinMode18 == 2:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = >>>매수만가능<<< , 3 = 매도만가능
                    if op_mode18 == 2 or op_mode18 == 3:   # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                        print("")
                        print(f"[ 18. 매수시간 : {now}  |  코인명 : {coin18}  |  현재가 = ￦{price18}  |  MACD = ￦{macd18}  |  보유수량 = {krw_balance18}  |  평가금액 = ￦{bp18}  ||  매수평균금액 = ￦{buy_bpAve18} ]")

                        if bp18 < buy_bpAve18: # 코인보유금액이 평균가보다 낮을때 매수시도
                            # 매수할 코인 금액 = 평균가 - 코인보유금액
                            buy_krw_price18 = buy_bpAve18 - bp18
                            # 매수할 코인 갯수 = 매수할 코인 금액 - 현재가
                            buy_krw_balance18 = buy_krw_price18 / price18

                            if krw18 >= buy_krw_price18: # 매수가능금액이 매수할금액보다 클때 매수시도
                                if buy_krw_price18 >= 10000:    # 매수가능금액이 최소주문가능금액인 ￦10,000원보다 높을때 매수시도

                                    # 매수할 코인명 - krw_coin18, 매수할 코인금액 - buy_krw_price18
                                    upbit.buy_market_order(krw_coin18, buy_krw_price18 * 0.9)

                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode18 = 1

                                    print("평균 이하 금액 매수")
                                    print(f"매수한금액 = ￦{buy_krw_price18}  |  매수한수량 = {buy_krw_balance18}  |  매수가능여부 - {op_mode18} - 매수불가-매도가능")
                                    print("")

                                else:
                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode18 = 1

                                    print("매수금액이 ￦10,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode18} - 매수불가-매도가능")
                                    print("")
                            else:   # 보유금액이 평균가와의 차이보다 적을때 매수
                                if krw18 >= 10000:    # 보유금액이 최소주문가능금액인 ￦10,000원보다 높을때 매수시도
                                    # 매수할 코인명 - krw_coin18, 매수할 코인금액 - krw18
                                    upbit.buy_market_order(krw_coin18, krw18 * 0.9)

                                    op_mode18 = 1

                                    print("보유금액보다 매수금액보다 적어서 매수금지")
                                    print(f"매수한금액 = ￦{krw18}  |  매수한수량 = {buy_krw_balance18}  |  매수가능여부 - {op_mode18} - 매수불가-매도가능")
                                    print("")
                                else:
                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode18 = 1

                                    print("보유금액이 ￦10,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode18} - 매수불가-매도가능")
                                    print("")

                        else:
                            # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                            op_mode18 = 1

                            print("보유금액이 평균금액보다 높아서 매수불가")
                            print(f"매수가능여부 - {op_mode18} - 매수불가-매도가능")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################


            ###############################
            # 코인19

            # 코인별 금액 비율조정
            buy_bpAve19 = bpAve * bpPer19

            # MACD 조건문
            if macd19 >= 0:     # macd가 0보다 크거나 같을때는 매수
                # 매수가능금액 불러오기
                krw19 = upbit.get_balance("KRW")

                if coinMode19 == 1 or coinMode19 == 2:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = >>>매수만가능<<< , 3 = 매도만가능
                    if op_mode19 == 2 or op_mode19 == 3:   # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                        print("")
                        print(f"[ 19. 매수시간 : {now}  |  코인명 : {coin19}  |  현재가 = ￦{price19}  |  MACD = ￦{macd19}  |  보유수량 = {krw_balance19}  |  평가금액 = ￦{bp19}  ||  매수평균금액 = ￦{buy_bpAve19} ]")

                        if bp19 < buy_bpAve19: # 코인보유금액이 평균가보다 낮을때 매수시도
                            # 매수할 코인 금액 = 평균가 - 코인보유금액
                            buy_krw_price19 = buy_bpAve19 - bp19
                            # 매수할 코인 갯수 = 매수할 코인 금액 - 현재가
                            buy_krw_balance19 = buy_krw_price19 / price19

                            if krw19 >= buy_krw_price19: # 매수가능금액이 매수할금액보다 클때 매수시도
                                if buy_krw_price19 >= 10000:    # 매수가능금액이 최소주문가능금액인 ￦10,000원보다 높을때 매수시도

                                    # 매수할 코인명 - krw_coin19, 매수할 코인금액 - buy_krw_price19
                                    upbit.buy_market_order(krw_coin19, buy_krw_price19 * 0.9)

                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode19 = 1

                                    print("평균 이하 금액 매수")
                                    print(f"매수한금액 = ￦{buy_krw_price19}  |  매수한수량 = {buy_krw_balance19}  |  매수가능여부 - {op_mode19} - 매수불가-매도가능")
                                    print("")

                                else:
                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode19 = 1

                                    print("매수금액이 ￦10,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode19} - 매수불가-매도가능")
                                    print("")
                            else:   # 보유금액이 평균가와의 차이보다 적을때 매수
                                if krw19 >= 10000:    # 보유금액이 최소주문가능금액인 ￦10,000원보다 높을때 매수시도
                                    # 매수할 코인명 - krw_coin19, 매수할 코인금액 - krw19
                                    upbit.buy_market_order(krw_coin19, krw19 * 0.9)

                                    op_mode19 = 1

                                    print("보유금액보다 매수금액보다 적어서 매수금지")
                                    print(f"매수한금액 = ￦{krw19}  |  매수한수량 = {buy_krw_balance19}  |  매수가능여부 - {op_mode19} - 매수불가-매도가능")
                                    print("")
                                else:
                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode19 = 1

                                    print("보유금액이 ￦10,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode19} - 매수불가-매도가능")
                                    print("")

                        else:
                            # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                            op_mode19 = 1

                            print("보유금액이 평균금액보다 높아서 매수불가")
                            print(f"매수가능여부 - {op_mode19} - 매수불가-매도가능")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################


            ###############################
            # 코인20

            # 코인별 금액 비율조정
            buy_bpAve20 = bpAve * bpPer20

            # MACD 조건문
            if macd20 >= 0:     # macd가 0보다 크거나 같을때는 매수
                # 매수가능금액 불러오기
                krw20 = upbit.get_balance("KRW")

                if coinMode20 == 1 or coinMode20 == 2:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = >>>매수만가능<<< , 3 = 매도만가능
                    if op_mode20 == 2 or op_mode20 == 3:   # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                        print("")
                        print(f"[ 20. 매수시간 : {now}  |  코인명 : {coin20}  |  현재가 = ￦{price20}  |  MACD = ￦{macd20}  |  보유수량 = {krw_balance20}  |  평가금액 = ￦{bp20}  ||  매수평균금액 = ￦{buy_bpAve20} ]")

                        if bp20 < buy_bpAve20: # 코인보유금액이 평균가보다 낮을때 매수시도
                            # 매수할 코인 금액 = 평균가 - 코인보유금액
                            buy_krw_price20 = buy_bpAve20 - bp20
                            # 매수할 코인 갯수 = 매수할 코인 금액 - 현재가
                            buy_krw_balance20 = buy_krw_price20 / price20

                            if krw20 >= buy_krw_price20: # 매수가능금액이 매수할금액보다 클때 매수시도
                                if buy_krw_price20 >= 10000:    # 매수가능금액이 최소주문가능금액인 ￦10,000원보다 높을때 매수시도

                                    # 매수할 코인명 - krw_coin20, 매수할 코인금액 - buy_krw_price20
                                    upbit.buy_market_order(krw_coin20, buy_krw_price20 * 0.9)

                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode20 = 1

                                    print("평균 이하 금액 매수")
                                    print(f"매수한금액 = ￦{buy_krw_price20}  |  매수한수량 = {buy_krw_balance20}  |  매수가능여부 - {op_mode20} - 매수불가-매도가능")
                                    print("")

                                else:
                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode20 = 1

                                    print("매수금액이 ￦10,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode20} - 매수불가-매도가능")
                                    print("")
                            else:   # 보유금액이 평균가와의 차이보다 적을때 매수
                                if krw20 >= 10000:    # 보유금액이 최소주문가능금액인 ￦10,000원보다 높을때 매수시도
                                    # 매수할 코인명 - krw_coin20, 매수할 코인금액 - krw20
                                    upbit.buy_market_order(krw_coin20, krw20 * 0.9)

                                    op_mode20 = 1

                                    print("보유금액보다 매수금액보다 적어서 매수금지")
                                    print(f"매수한금액 = ￦{krw20}  |  매수한수량 = {buy_krw_balance20}  |  매수가능여부 - {op_mode20} - 매수불가-매도가능")
                                    print("")
                                else:
                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode20 = 1

                                    print("보유금액이 ￦10,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode20} - 매수불가-매도가능")
                                    print("")

                        else:
                            # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                            op_mode20 = 1

                            print("보유금액이 평균금액보다 높아서 매수불가")
                            print(f"매수가능여부 - {op_mode20} - 매수불가-매도가능")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################





            ######################################################################################################################################################
            ######################################################################################################################################################
            ######################################################################################################################################################





            ###############################
            # 코인21

            # 코인별 금액 비율조정
            buy_bpAve21 = bpAve * bpPer21

            # MACD 조건문
            if macd21 >= 0:     # macd가 0보다 크거나 같을때는 매수
                # 매수가능금액 불러오기
                krw21 = upbit.get_balance("KRW")

                if coinMode21 == 1 or coinMode21 == 2:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = >>>매수만가능<<< , 3 = 매도만가능
                    if op_mode21 == 2 or op_mode21 == 3:   # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                        print("")
                        print(f"[ 21. 매수시간 : {now}  |  코인명 : {coin21}  |  현재가 = ￦{price21}  |  MACD = ￦{macd21}  |  보유수량 = {krw_balance21}  |  평가금액 = ￦{bp21}  ||  매수평균금액 = ￦{buy_bpAve21} ]")

                        if bp21 < buy_bpAve21: # 코인보유금액이 평균가보다 낮을때 매수시도
                            # 매수할 코인 금액 = 평균가 - 코인보유금액
                            buy_krw_price21 = buy_bpAve21 - bp21
                            # 매수할 코인 갯수 = 매수할 코인 금액 - 현재가
                            buy_krw_balance21 = buy_krw_price21 / price21

                            if krw21 >= buy_krw_price21: # 매수가능금액이 매수할금액보다 클때 매수시도
                                if buy_krw_price21 >= 10000:    # 매수가능금액이 최소주문가능금액인 ￦10,000원보다 높을때 매수시도

                                    # 매수할 코인명 - krw_coin21, 매수할 코인금액 - buy_krw_price21
                                    upbit.buy_market_order(krw_coin21, buy_krw_price21 * 0.9)

                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode21 = 1

                                    print("평균 이하 금액 매수")
                                    print(f"매수한금액 = ￦{buy_krw_price21}  |  매수한수량 = {buy_krw_balance21}  |  매수가능여부 - {op_mode21} - 매수불가-매도가능")
                                    print("")

                                else:
                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode21 = 1

                                    print("매수금액이 ￦10,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode21} - 매수불가-매도가능")
                                    print("")
                            else:   # 보유금액이 평균가와의 차이보다 적을때 매수
                                if krw21 >= 10000:    # 보유금액이 최소주문가능금액인 ￦10,000원보다 높을때 매수시도
                                    # 매수할 코인명 - krw_coin21, 매수할 코인금액 - krw21
                                    upbit.buy_market_order(krw_coin21, krw21 * 0.9)

                                    op_mode21 = 1

                                    print("보유금액보다 매수금액보다 적어서 매수금지")
                                    print(f"매수한금액 = ￦{krw21}  |  매수한수량 = {buy_krw_balance21}  |  매수가능여부 - {op_mode21} - 매수불가-매도가능")
                                    print("")
                                else:
                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode21 = 1

                                    print("보유금액이 ￦10,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode21} - 매수불가-매도가능")
                                    print("")

                        else:
                            # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                            op_mode21 = 1

                            print("보유금액이 평균금액보다 높아서 매수불가")
                            print(f"매수가능여부 - {op_mode21} - 매수불가-매도가능")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################


            ###############################
            # 코인22

            # 코인별 금액 비율조정
            buy_bpAve22 = bpAve * bpPer22

            # MACD 조건문
            if macd22 >= 0:     # macd가 0보다 크거나 같을때는 매수
                # 매수가능금액 불러오기
                krw22 = upbit.get_balance("KRW")

                if coinMode22 == 1 or coinMode22 == 2:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = >>>매수만가능<<< , 3 = 매도만가능
                    if op_mode22 == 2 or op_mode22 == 3:   # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                        print("")
                        print(f"[ 22. 매수시간 : {now}  |  코인명 : {coin22}  |  현재가 = ￦{price22}  |  MACD = ￦{macd22}  |  보유수량 = {krw_balance22}  |  평가금액 = ￦{bp22}  ||  매수평균금액 = ￦{buy_bpAve22} ]")

                        if bp22 < buy_bpAve22: # 코인보유금액이 평균가보다 낮을때 매수시도
                            # 매수할 코인 금액 = 평균가 - 코인보유금액
                            buy_krw_price22 = buy_bpAve22 - bp22
                            # 매수할 코인 갯수 = 매수할 코인 금액 - 현재가
                            buy_krw_balance22 = buy_krw_price22 / price22

                            if krw22 >= buy_krw_price22: # 매수가능금액이 매수할금액보다 클때 매수시도
                                if buy_krw_price22 >= 10000:    # 매수가능금액이 최소주문가능금액인 ￦10,000원보다 높을때 매수시도

                                    # 매수할 코인명 - krw_coin22, 매수할 코인금액 - buy_krw_price22
                                    upbit.buy_market_order(krw_coin22, buy_krw_price22 * 0.9)

                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode22 = 1

                                    print("평균 이하 금액 매수")
                                    print(f"매수한금액 = ￦{buy_krw_price22}  |  매수한수량 = {buy_krw_balance22}  |  매수가능여부 - {op_mode22} - 매수불가-매도가능")
                                    print("")

                                else:
                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode22 = 1

                                    print("매수금액이 ￦10,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode22} - 매수불가-매도가능")
                                    print("")
                            else:   # 보유금액이 평균가와의 차이보다 적을때 매수
                                if krw22 >= 10000:    # 보유금액이 최소주문가능금액인 ￦10,000원보다 높을때 매수시도
                                    # 매수할 코인명 - krw_coin22, 매수할 코인금액 - krw22
                                    upbit.buy_market_order(krw_coin22, krw22 * 0.9)

                                    op_mode22 = 1

                                    print("보유금액보다 매수금액보다 적어서 매수금지")
                                    print(f"매수한금액 = ￦{krw22}  |  매수한수량 = {buy_krw_balance22}  |  매수가능여부 - {op_mode22} - 매수불가-매도가능")
                                    print("")
                                else:
                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode22 = 1

                                    print("보유금액이 ￦10,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode22} - 매수불가-매도가능")
                                    print("")

                        else:
                            # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                            op_mode22 = 1

                            print("보유금액이 평균금액보다 높아서 매수불가")
                            print(f"매수가능여부 - {op_mode22} - 매수불가-매도가능")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################


            ###############################
            # 코인23

            # 코인별 금액 비율조정
            buy_bpAve23 = bpAve * bpPer23

            # MACD 조건문
            if macd23 >= 0:     # macd가 0보다 크거나 같을때는 매수
                # 매수가능금액 불러오기
                krw23 = upbit.get_balance("KRW")

                if coinMode23 == 1 or coinMode23 == 2:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = >>>매수만가능<<< , 3 = 매도만가능
                    if op_mode23 == 2 or op_mode23 == 3:   # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                        print("")
                        print(f"[ 23. 매수시간 : {now}  |  코인명 : {coin23}  |  현재가 = ￦{price23}  |  MACD = ￦{macd23}  |  보유수량 = {krw_balance23}  |  평가금액 = ￦{bp23}  ||  매수평균금액 = ￦{buy_bpAve23} ]")

                        if bp23 < buy_bpAve23: # 코인보유금액이 평균가보다 낮을때 매수시도
                            # 매수할 코인 금액 = 평균가 - 코인보유금액
                            buy_krw_price23 = buy_bpAve23 - bp23
                            # 매수할 코인 갯수 = 매수할 코인 금액 - 현재가
                            buy_krw_balance23 = buy_krw_price23 / price23

                            if krw23 >= buy_krw_price23: # 매수가능금액이 매수할금액보다 클때 매수시도
                                if buy_krw_price23 >= 10000:    # 매수가능금액이 최소주문가능금액인 ￦10,000원보다 높을때 매수시도

                                    # 매수할 코인명 - krw_coin23, 매수할 코인금액 - buy_krw_price23
                                    upbit.buy_market_order(krw_coin23, buy_krw_price23 * 0.9)

                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode23 = 1

                                    print("평균 이하 금액 매수")
                                    print(f"매수한금액 = ￦{buy_krw_price23}  |  매수한수량 = {buy_krw_balance23}  |  매수가능여부 - {op_mode23} - 매수불가-매도가능")
                                    print("")

                                else:
                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode23 = 1

                                    print("매수금액이 ￦10,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode23} - 매수불가-매도가능")
                                    print("")
                            else:   # 보유금액이 평균가와의 차이보다 적을때 매수
                                if krw23 >= 10000:    # 보유금액이 최소주문가능금액인 ￦10,000원보다 높을때 매수시도
                                    # 매수할 코인명 - krw_coin23, 매수할 코인금액 - krw23
                                    upbit.buy_market_order(krw_coin23, krw23 * 0.9)

                                    op_mode23 = 1

                                    print("보유금액보다 매수금액보다 적어서 매수금지")
                                    print(f"매수한금액 = ￦{krw23}  |  매수한수량 = {buy_krw_balance23}  |  매수가능여부 - {op_mode23} - 매수불가-매도가능")
                                    print("")
                                else:
                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode23 = 1

                                    print("보유금액이 ￦10,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode23} - 매수불가-매도가능")
                                    print("")

                        else:
                            # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                            op_mode23 = 1

                            print("보유금액이 평균금액보다 높아서 매수불가")
                            print(f"매수가능여부 - {op_mode23} - 매수불가-매도가능")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################


            ###############################
            # 코인24

            # 코인별 금액 비율조정
            buy_bpAve24 = bpAve * bpPer24

            # MACD 조건문
            if macd24 >= 0:     # macd가 0보다 크거나 같을때는 매수
                # 매수가능금액 불러오기
                krw24 = upbit.get_balance("KRW")

                if coinMode24 == 1 or coinMode24 == 2:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = >>>매수만가능<<< , 3 = 매도만가능
                    if op_mode24 == 2 or op_mode24 == 3:   # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                        print("")
                        print(f"[ 24. 매수시간 : {now}  |  코인명 : {coin24}  |  현재가 = ￦{price24}  |  MACD = ￦{macd24}  |  보유수량 = {krw_balance24}  |  평가금액 = ￦{bp24}  ||  매수평균금액 = ￦{buy_bpAve24} ]")

                        if bp24 < buy_bpAve24: # 코인보유금액이 평균가보다 낮을때 매수시도
                            # 매수할 코인 금액 = 평균가 - 코인보유금액
                            buy_krw_price24 = buy_bpAve24 - bp24
                            # 매수할 코인 갯수 = 매수할 코인 금액 - 현재가
                            buy_krw_balance24 = buy_krw_price24 / price24

                            if krw24 >= buy_krw_price24: # 매수가능금액이 매수할금액보다 클때 매수시도
                                if buy_krw_price24 >= 10000:    # 매수가능금액이 최소주문가능금액인 ￦10,000원보다 높을때 매수시도

                                    # 매수할 코인명 - krw_coin24, 매수할 코인금액 - buy_krw_price24
                                    upbit.buy_market_order(krw_coin24, buy_krw_price24 * 0.9)

                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode24 = 1

                                    print("평균 이하 금액 매수")
                                    print(f"매수한금액 = ￦{buy_krw_price24}  |  매수한수량 = {buy_krw_balance24}  |  매수가능여부 - {op_mode24} - 매수불가-매도가능")
                                    print("")

                                else:
                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode24 = 1

                                    print("매수금액이 ￦10,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode24} - 매수불가-매도가능")
                                    print("")
                            else:   # 보유금액이 평균가와의 차이보다 적을때 매수
                                if krw24 >= 10000:    # 보유금액이 최소주문가능금액인 ￦10,000원보다 높을때 매수시도
                                    # 매수할 코인명 - krw_coin24, 매수할 코인금액 - krw24
                                    upbit.buy_market_order(krw_coin24, krw24 * 0.9)

                                    op_mode24 = 1

                                    print("보유금액보다 매수금액보다 적어서 매수금지")
                                    print(f"매수한금액 = ￦{krw24}  |  매수한수량 = {buy_krw_balance24}  |  매수가능여부 - {op_mode24} - 매수불가-매도가능")
                                    print("")
                                else:
                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode24 = 1

                                    print("보유금액이 ￦10,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode24} - 매수불가-매도가능")
                                    print("")

                        else:
                            # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                            op_mode24 = 1

                            print("보유금액이 평균금액보다 높아서 매수불가")
                            print(f"매수가능여부 - {op_mode24} - 매수불가-매도가능")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################


            ###############################
            # 코인25

            # 코인별 금액 비율조정
            buy_bpAve25 = bpAve * bpPer25

            # MACD 조건문
            if macd25 >= 0:     # macd가 0보다 크거나 같을때는 매수
                # 매수가능금액 불러오기
                krw25 = upbit.get_balance("KRW")

                if coinMode25 == 1 or coinMode25 == 2:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = >>>매수만가능<<< , 3 = 매도만가능
                    if op_mode25 == 2 or op_mode25 == 3:   # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                        print("")
                        print(f"[ 25. 매수시간 : {now}  |  코인명 : {coin25}  |  현재가 = ￦{price25}  |  MACD = ￦{macd25}  |  보유수량 = {krw_balance25}  |  평가금액 = ￦{bp25}  ||  매수평균금액 = ￦{buy_bpAve25} ]")

                        if bp25 < buy_bpAve25: # 코인보유금액이 평균가보다 낮을때 매수시도
                            # 매수할 코인 금액 = 평균가 - 코인보유금액
                            buy_krw_price25 = buy_bpAve25 - bp25
                            # 매수할 코인 갯수 = 매수할 코인 금액 - 현재가
                            buy_krw_balance25 = buy_krw_price25 / price25

                            if krw25 >= buy_krw_price25: # 매수가능금액이 매수할금액보다 클때 매수시도
                                if buy_krw_price25 >= 10000:    # 매수가능금액이 최소주문가능금액인 ￦10,000원보다 높을때 매수시도

                                    # 매수할 코인명 - krw_coin25, 매수할 코인금액 - buy_krw_price25
                                    upbit.buy_market_order(krw_coin25, buy_krw_price25 * 0.9)

                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode25 = 1

                                    print("평균 이하 금액 매수")
                                    print(f"매수한금액 = ￦{buy_krw_price25}  |  매수한수량 = {buy_krw_balance25}  |  매수가능여부 - {op_mode25} - 매수불가-매도가능")
                                    print("")

                                else:
                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode25 = 1

                                    print("매수금액이 ￦10,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode25} - 매수불가-매도가능")
                                    print("")
                            else:   # 보유금액이 평균가와의 차이보다 적을때 매수
                                if krw25 >= 10000:    # 보유금액이 최소주문가능금액인 ￦10,000원보다 높을때 매수시도
                                    # 매수할 코인명 - krw_coin25, 매수할 코인금액 - krw25
                                    upbit.buy_market_order(krw_coin25, krw25 * 0.9)

                                    op_mode25 = 1

                                    print("보유금액보다 매수금액보다 적어서 매수금지")
                                    print(f"매수한금액 = ￦{krw25}  |  매수한수량 = {buy_krw_balance25}  |  매수가능여부 - {op_mode25} - 매수불가-매도가능")
                                    print("")
                                else:
                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode25 = 1

                                    print("보유금액이 ￦10,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode25} - 매수불가-매도가능")
                                    print("")

                        else:
                            # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                            op_mode25 = 1

                            print("보유금액이 평균금액보다 높아서 매수불가")
                            print(f"매수가능여부 - {op_mode25} - 매수불가-매도가능")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################


            ###############################
            # 코인26

            # 코인별 금액 비율조정
            buy_bpAve26 = bpAve * bpPer26

            # MACD 조건문
            if macd26 >= 0:     # macd가 0보다 크거나 같을때는 매수
                # 매수가능금액 불러오기
                krw26 = upbit.get_balance("KRW")

                if coinMode26 == 1 or coinMode26 == 2:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = >>>매수만가능<<< , 3 = 매도만가능
                    if op_mode26 == 2 or op_mode26 == 3:   # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                        print("")
                        print(f"[ 26. 매수시간 : {now}  |  코인명 : {coin26}  |  현재가 = ￦{price26}  |  MACD = ￦{macd26}  |  보유수량 = {krw_balance26}  |  평가금액 = ￦{bp26}  ||  매수평균금액 = ￦{buy_bpAve26} ]")

                        if bp26 < buy_bpAve26: # 코인보유금액이 평균가보다 낮을때 매수시도
                            # 매수할 코인 금액 = 평균가 - 코인보유금액
                            buy_krw_price26 = buy_bpAve26 - bp26
                            # 매수할 코인 갯수 = 매수할 코인 금액 - 현재가
                            buy_krw_balance26 = buy_krw_price26 / price26

                            if krw26 >= buy_krw_price26: # 매수가능금액이 매수할금액보다 클때 매수시도
                                if buy_krw_price26 >= 10000:    # 매수가능금액이 최소주문가능금액인 ￦10,000원보다 높을때 매수시도

                                    # 매수할 코인명 - krw_coin26, 매수할 코인금액 - buy_krw_price26
                                    upbit.buy_market_order(krw_coin26, buy_krw_price26 * 0.9)

                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode26 = 1

                                    print("평균 이하 금액 매수")
                                    print(f"매수한금액 = ￦{buy_krw_price26}  |  매수한수량 = {buy_krw_balance26}  |  매수가능여부 - {op_mode26} - 매수불가-매도가능")
                                    print("")

                                else:
                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode26 = 1

                                    print("매수금액이 ￦10,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode26} - 매수불가-매도가능")
                                    print("")
                            else:   # 보유금액이 평균가와의 차이보다 적을때 매수
                                if krw26 >= 10000:    # 보유금액이 최소주문가능금액인 ￦10,000원보다 높을때 매수시도
                                    # 매수할 코인명 - krw_coin26, 매수할 코인금액 - krw26
                                    upbit.buy_market_order(krw_coin26, krw26 * 0.9)

                                    op_mode26 = 1

                                    print("보유금액보다 매수금액보다 적어서 매수금지")
                                    print(f"매수한금액 = ￦{krw26}  |  매수한수량 = {buy_krw_balance26}  |  매수가능여부 - {op_mode26} - 매수불가-매도가능")
                                    print("")
                                else:
                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode26 = 1

                                    print("보유금액이 ￦10,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode26} - 매수불가-매도가능")
                                    print("")

                        else:
                            # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                            op_mode26 = 1

                            print("보유금액이 평균금액보다 높아서 매수불가")
                            print(f"매수가능여부 - {op_mode26} - 매수불가-매도가능")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################


            ###############################
            # 코인27

            # 코인별 금액 비율조정
            buy_bpAve27 = bpAve * bpPer27

            # MACD 조건문
            if macd27 >= 0:     # macd가 0보다 크거나 같을때는 매수
                # 매수가능금액 불러오기
                krw27 = upbit.get_balance("KRW")

                if coinMode27 == 1 or coinMode27 == 2:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = >>>매수만가능<<< , 3 = 매도만가능
                    if op_mode27 == 2 or op_mode27 == 3:   # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                        print("")
                        print(f"[ 27. 매수시간 : {now}  |  코인명 : {coin27}  |  현재가 = ￦{price27}  |  MACD = ￦{macd27}  |  보유수량 = {krw_balance27}  |  평가금액 = ￦{bp27}  ||  매수평균금액 = ￦{buy_bpAve27} ]")

                        if bp27 < buy_bpAve27: # 코인보유금액이 평균가보다 낮을때 매수시도
                            # 매수할 코인 금액 = 평균가 - 코인보유금액
                            buy_krw_price27 = buy_bpAve27 - bp27
                            # 매수할 코인 갯수 = 매수할 코인 금액 - 현재가
                            buy_krw_balance27 = buy_krw_price27 / price27

                            if krw27 >= buy_krw_price27: # 매수가능금액이 매수할금액보다 클때 매수시도
                                if buy_krw_price27 >= 10000:    # 매수가능금액이 최소주문가능금액인 ￦10,000원보다 높을때 매수시도

                                    # 매수할 코인명 - krw_coin27, 매수할 코인금액 - buy_krw_price27
                                    upbit.buy_market_order(krw_coin27, buy_krw_price27 * 0.9)

                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode27 = 1

                                    print("평균 이하 금액 매수")
                                    print(f"매수한금액 = ￦{buy_krw_price27}  |  매수한수량 = {buy_krw_balance27}  |  매수가능여부 - {op_mode27} - 매수불가-매도가능")
                                    print("")

                                else:
                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode27 = 1

                                    print("매수금액이 ￦10,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode27} - 매수불가-매도가능")
                                    print("")
                            else:   # 보유금액이 평균가와의 차이보다 적을때 매수
                                if krw27 >= 10000:    # 보유금액이 최소주문가능금액인 ￦10,000원보다 높을때 매수시도
                                    # 매수할 코인명 - krw_coin27, 매수할 코인금액 - krw27
                                    upbit.buy_market_order(krw_coin27, krw27 * 0.9)

                                    op_mode27 = 1

                                    print("보유금액보다 매수금액보다 적어서 매수금지")
                                    print(f"매수한금액 = ￦{krw27}  |  매수한수량 = {buy_krw_balance27}  |  매수가능여부 - {op_mode27} - 매수불가-매도가능")
                                    print("")
                                else:
                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode27 = 1

                                    print("보유금액이 ￦10,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode27} - 매수불가-매도가능")
                                    print("")

                        else:
                            # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                            op_mode27 = 1

                            print("보유금액이 평균금액보다 높아서 매수불가")
                            print(f"매수가능여부 - {op_mode27} - 매수불가-매도가능")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################


            ###############################
            # 코인28

            # 코인별 금액 비율조정
            buy_bpAve28 = bpAve * bpPer28

            # MACD 조건문
            if macd28 >= 0:     # macd가 0보다 크거나 같을때는 매수
                # 매수가능금액 불러오기
                krw28 = upbit.get_balance("KRW")

                if coinMode28 == 1 or coinMode28 == 2:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = >>>매수만가능<<< , 3 = 매도만가능
                    if op_mode28 == 2 or op_mode28 == 3:   # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                        print("")
                        print(f"[ 28. 매수시간 : {now}  |  코인명 : {coin28}  |  현재가 = ￦{price28}  |  MACD = ￦{macd28}  |  보유수량 = {krw_balance28}  |  평가금액 = ￦{bp28}  ||  매수평균금액 = ￦{buy_bpAve28} ]")

                        if bp28 < buy_bpAve28: # 코인보유금액이 평균가보다 낮을때 매수시도
                            # 매수할 코인 금액 = 평균가 - 코인보유금액
                            buy_krw_price28 = buy_bpAve28 - bp28
                            # 매수할 코인 갯수 = 매수할 코인 금액 - 현재가
                            buy_krw_balance28 = buy_krw_price28 / price28

                            if krw28 >= buy_krw_price28: # 매수가능금액이 매수할금액보다 클때 매수시도
                                if buy_krw_price28 >= 10000:    # 매수가능금액이 최소주문가능금액인 ￦10,000원보다 높을때 매수시도

                                    # 매수할 코인명 - krw_coin28, 매수할 코인금액 - buy_krw_price28
                                    upbit.buy_market_order(krw_coin28, buy_krw_price28 * 0.9)

                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode28 = 1

                                    print("평균 이하 금액 매수")
                                    print(f"매수한금액 = ￦{buy_krw_price28}  |  매수한수량 = {buy_krw_balance28}  |  매수가능여부 - {op_mode28} - 매수불가-매도가능")
                                    print("")

                                else:
                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode28 = 1

                                    print("매수금액이 ￦10,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode28} - 매수불가-매도가능")
                                    print("")
                            else:   # 보유금액이 평균가와의 차이보다 적을때 매수
                                if krw28 >= 10000:    # 보유금액이 최소주문가능금액인 ￦10,000원보다 높을때 매수시도
                                    # 매수할 코인명 - krw_coin28, 매수할 코인금액 - krw28
                                    upbit.buy_market_order(krw_coin28, krw28 * 0.9)

                                    op_mode28 = 1

                                    print("보유금액보다 매수금액보다 적어서 매수금지")
                                    print(f"매수한금액 = ￦{krw28}  |  매수한수량 = {buy_krw_balance28}  |  매수가능여부 - {op_mode28} - 매수불가-매도가능")
                                    print("")
                                else:
                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode28 = 1

                                    print("보유금액이 ￦10,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode28} - 매수불가-매도가능")
                                    print("")

                        else:
                            # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                            op_mode28 = 1

                            print("보유금액이 평균금액보다 높아서 매수불가")
                            print(f"매수가능여부 - {op_mode28} - 매수불가-매도가능")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################


            ###############################
            # 코인29

            # 코인별 금액 비율조정
            buy_bpAve29 = bpAve * bpPer29

            # MACD 조건문
            if macd29 >= 0:     # macd가 0보다 크거나 같을때는 매수
                # 매수가능금액 불러오기
                krw29 = upbit.get_balance("KRW")

                if coinMode29 == 1 or coinMode29 == 2:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = >>>매수만가능<<< , 3 = 매도만가능
                    if op_mode29 == 2 or op_mode29 == 3:   # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                        print("")
                        print(f"[ 29. 매수시간 : {now}  |  코인명 : {coin29}  |  현재가 = ￦{price29}  |  MACD = ￦{macd29}  |  보유수량 = {krw_balance29}  |  평가금액 = ￦{bp29}  ||  매수평균금액 = ￦{buy_bpAve29} ]")

                        if bp29 < buy_bpAve29: # 코인보유금액이 평균가보다 낮을때 매수시도
                            # 매수할 코인 금액 = 평균가 - 코인보유금액
                            buy_krw_price29 = buy_bpAve29 - bp29
                            # 매수할 코인 갯수 = 매수할 코인 금액 - 현재가
                            buy_krw_balance29 = buy_krw_price29 / price29

                            if krw29 >= buy_krw_price29: # 매수가능금액이 매수할금액보다 클때 매수시도
                                if buy_krw_price29 >= 10000:    # 매수가능금액이 최소주문가능금액인 ￦10,000원보다 높을때 매수시도

                                    # 매수할 코인명 - krw_coin29, 매수할 코인금액 - buy_krw_price29
                                    upbit.buy_market_order(krw_coin29, buy_krw_price29 * 0.9)

                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode29 = 1

                                    print("평균 이하 금액 매수")
                                    print(f"매수한금액 = ￦{buy_krw_price29}  |  매수한수량 = {buy_krw_balance29}  |  매수가능여부 - {op_mode29} - 매수불가-매도가능")
                                    print("")

                                else:
                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode29 = 1

                                    print("매수금액이 ￦10,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode29} - 매수불가-매도가능")
                                    print("")
                            else:   # 보유금액이 평균가와의 차이보다 적을때 매수
                                if krw29 >= 10000:    # 보유금액이 최소주문가능금액인 ￦10,000원보다 높을때 매수시도
                                    # 매수할 코인명 - krw_coin29, 매수할 코인금액 - krw29
                                    upbit.buy_market_order(krw_coin29, krw29 * 0.9)

                                    op_mode29 = 1

                                    print("보유금액보다 매수금액보다 적어서 매수금지")
                                    print(f"매수한금액 = ￦{krw29}  |  매수한수량 = {buy_krw_balance29}  |  매수가능여부 - {op_mode29} - 매수불가-매도가능")
                                    print("")
                                else:
                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode29 = 1

                                    print("보유금액이 ￦10,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode29} - 매수불가-매도가능")
                                    print("")

                        else:
                            # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                            op_mode29 = 1

                            print("보유금액이 평균금액보다 높아서 매수불가")
                            print(f"매수가능여부 - {op_mode29} - 매수불가-매도가능")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################


            ###############################
            # 코인30

            # 코인별 금액 비율조정
            buy_bpAve30 = bpAve * bpPer30

            # MACD 조건문
            if macd30 >= 0:     # macd가 0보다 크거나 같을때는 매수
                # 매수가능금액 불러오기
                krw30 = upbit.get_balance("KRW")

                if coinMode30 == 1 or coinMode30 == 2:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = >>>매수만가능<<< , 3 = 매도만가능
                    if op_mode30 == 2 or op_mode30 == 3:   # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                        print("")
                        print(f"[ 30. 매수시간 : {now}  |  코인명 : {coin30}  |  현재가 = ￦{price30}  |  MACD = ￦{macd30}  |  보유수량 = {krw_balance30}  |  평가금액 = ￦{bp30}  ||  매수평균금액 = ￦{buy_bpAve30} ]")

                        if bp30 < buy_bpAve30: # 코인보유금액이 평균가보다 낮을때 매수시도
                            # 매수할 코인 금액 = 평균가 - 코인보유금액
                            buy_krw_price30 = buy_bpAve30 - bp30
                            # 매수할 코인 갯수 = 매수할 코인 금액 - 현재가
                            buy_krw_balance30 = buy_krw_price30 / price30

                            if krw30 >= buy_krw_price30: # 매수가능금액이 매수할금액보다 클때 매수시도
                                if buy_krw_price30 >= 10000:    # 매수가능금액이 최소주문가능금액인 ￦10,000원보다 높을때 매수시도

                                    # 매수할 코인명 - krw_coin30, 매수할 코인금액 - buy_krw_price30
                                    upbit.buy_market_order(krw_coin30, buy_krw_price30 * 0.9)

                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode30 = 1

                                    print("평균 이하 금액 매수")
                                    print(f"매수한금액 = ￦{buy_krw_price30}  |  매수한수량 = {buy_krw_balance30}  |  매수가능여부 - {op_mode30} - 매수불가-매도가능")
                                    print("")

                                else:
                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode30 = 1

                                    print("매수금액이 ￦10,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode30} - 매수불가-매도가능")
                                    print("")
                            else:   # 보유금액이 평균가와의 차이보다 적을때 매수
                                if krw30 >= 10000:    # 보유금액이 최소주문가능금액인 ￦10,000원보다 높을때 매수시도
                                    # 매수할 코인명 - krw_coin30, 매수할 코인금액 - krw30
                                    upbit.buy_market_order(krw_coin30, krw30 * 0.9)

                                    op_mode30 = 1

                                    print("보유금액보다 매수금액보다 적어서 매수금지")
                                    print(f"매수한금액 = ￦{krw30}  |  매수한수량 = {buy_krw_balance30}  |  매수가능여부 - {op_mode30} - 매수불가-매도가능")
                                    print("")
                                else:
                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode30 = 1

                                    print("보유금액이 ￦10,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode30} - 매수불가-매도가능")
                                    print("")

                        else:
                            # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                            op_mode30 = 1

                            print("보유금액이 평균금액보다 높아서 매수불가")
                            print(f"매수가능여부 - {op_mode30} - 매수불가-매도가능")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################





            ######################################################################################################################################################
            ######################################################################################################################################################
            ######################################################################################################################################################





            ###############################
            # 코인31

            # 코인별 금액 비율조정
            buy_bpAve31 = bpAve * bpPer31

            # MACD 조건문
            if macd31 >= 0:     # macd가 0보다 크거나 같을때는 매수
                # 매수가능금액 불러오기
                krw31 = upbit.get_balance("KRW")

                if coinMode31 == 1 or coinMode31 == 2:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = >>>매수만가능<<< , 3 = 매도만가능
                    if op_mode31 == 2 or op_mode31 == 3:   # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                        print("")
                        print(f"[ 31. 매수시간 : {now}  |  코인명 : {coin31}  |  현재가 = ￦{price31}  |  MACD = ￦{macd31}  |  보유수량 = {krw_balance31}  |  평가금액 = ￦{bp31}  ||  매수평균금액 = ￦{buy_bpAve31} ]")

                        if bp31 < buy_bpAve31: # 코인보유금액이 평균가보다 낮을때 매수시도
                            # 매수할 코인 금액 = 평균가 - 코인보유금액
                            buy_krw_price31 = buy_bpAve31 - bp31
                            # 매수할 코인 갯수 = 매수할 코인 금액 - 현재가
                            buy_krw_balance31 = buy_krw_price31 / price31

                            if krw31 >= buy_krw_price31: # 매수가능금액이 매수할금액보다 클때 매수시도
                                if buy_krw_price31 >= 10000:    # 매수가능금액이 최소주문가능금액인 ￦10,000원보다 높을때 매수시도

                                    # 매수할 코인명 - krw_coin31, 매수할 코인금액 - buy_krw_price31
                                    upbit.buy_market_order(krw_coin31, buy_krw_price31 * 0.9)

                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode31 = 1

                                    print("평균 이하 금액 매수")
                                    print(f"매수한금액 = ￦{buy_krw_price31}  |  매수한수량 = {buy_krw_balance31}  |  매수가능여부 - {op_mode31} - 매수불가-매도가능")
                                    print("")

                                else:
                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode31 = 1

                                    print("매수금액이 ￦10,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode31} - 매수불가-매도가능")
                                    print("")
                            else:   # 보유금액이 평균가와의 차이보다 적을때 매수
                                if krw31 >= 10000:    # 보유금액이 최소주문가능금액인 ￦10,000원보다 높을때 매수시도
                                    # 매수할 코인명 - krw_coin31, 매수할 코인금액 - krw31
                                    upbit.buy_market_order(krw_coin31, krw31 * 0.9)

                                    op_mode31 = 1

                                    print("보유금액보다 매수금액보다 적어서 매수금지")
                                    print(f"매수한금액 = ￦{krw31}  |  매수한수량 = {buy_krw_balance31}  |  매수가능여부 - {op_mode31} - 매수불가-매도가능")
                                    print("")
                                else:
                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode31 = 1

                                    print("보유금액이 ￦10,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode31} - 매수불가-매도가능")
                                    print("")

                        else:
                            # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                            op_mode31 = 1

                            print("보유금액이 평균금액보다 높아서 매수불가")
                            print(f"매수가능여부 - {op_mode31} - 매수불가-매도가능")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################


            ###############################
            # 코인32

            # 코인별 금액 비율조정
            buy_bpAve32 = bpAve * bpPer32

            # MACD 조건문
            if macd32 >= 0:     # macd가 0보다 크거나 같을때는 매수
                # 매수가능금액 불러오기
                krw32 = upbit.get_balance("KRW")

                if coinMode32 == 1 or coinMode32 == 2:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = >>>매수만가능<<< , 3 = 매도만가능
                    if op_mode32 == 2 or op_mode32 == 3:   # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                        print("")
                        print(f"[ 32. 매수시간 : {now}  |  코인명 : {coin32}  |  현재가 = ￦{price32}  |  MACD = ￦{macd32}  |  보유수량 = {krw_balance32}  |  평가금액 = ￦{bp32}  ||  매수평균금액 = ￦{buy_bpAve32} ]")

                        if bp32 < buy_bpAve32: # 코인보유금액이 평균가보다 낮을때 매수시도
                            # 매수할 코인 금액 = 평균가 - 코인보유금액
                            buy_krw_price32 = buy_bpAve32 - bp32
                            # 매수할 코인 갯수 = 매수할 코인 금액 - 현재가
                            buy_krw_balance32 = buy_krw_price32 / price32

                            if krw32 >= buy_krw_price32: # 매수가능금액이 매수할금액보다 클때 매수시도
                                if buy_krw_price32 >= 10000:    # 매수가능금액이 최소주문가능금액인 ￦10,000원보다 높을때 매수시도

                                    # 매수할 코인명 - krw_coin32, 매수할 코인금액 - buy_krw_price32
                                    upbit.buy_market_order(krw_coin32, buy_krw_price32 * 0.9)

                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode32 = 1

                                    print("평균 이하 금액 매수")
                                    print(f"매수한금액 = ￦{buy_krw_price32}  |  매수한수량 = {buy_krw_balance32}  |  매수가능여부 - {op_mode32} - 매수불가-매도가능")
                                    print("")

                                else:
                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode32 = 1

                                    print("매수금액이 ￦10,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode32} - 매수불가-매도가능")
                                    print("")
                            else:   # 보유금액이 평균가와의 차이보다 적을때 매수
                                if krw32 >= 10000:    # 보유금액이 최소주문가능금액인 ￦10,000원보다 높을때 매수시도
                                    # 매수할 코인명 - krw_coin32, 매수할 코인금액 - krw32
                                    upbit.buy_market_order(krw_coin32, krw32 * 0.9)

                                    op_mode32 = 1

                                    print("보유금액보다 매수금액보다 적어서 매수금지")
                                    print(f"매수한금액 = ￦{krw32}  |  매수한수량 = {buy_krw_balance32}  |  매수가능여부 - {op_mode32} - 매수불가-매도가능")
                                    print("")
                                else:
                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode32 = 1

                                    print("보유금액이 ￦10,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode32} - 매수불가-매도가능")
                                    print("")

                        else:
                            # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                            op_mode32 = 1

                            print("보유금액이 평균금액보다 높아서 매수불가")
                            print(f"매수가능여부 - {op_mode32} - 매수불가-매도가능")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################


            ###############################
            # 코인33

            # 코인별 금액 비율조정
            buy_bpAve33 = bpAve * bpPer33

            # MACD 조건문
            if macd33 >= 0:     # macd가 0보다 크거나 같을때는 매수
                # 매수가능금액 불러오기
                krw33 = upbit.get_balance("KRW")

                if coinMode33 == 1 or coinMode33 == 2:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = >>>매수만가능<<< , 3 = 매도만가능
                    if op_mode33 == 2 or op_mode33 == 3:   # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                        print("")
                        print(f"[ 33. 매수시간 : {now}  |  코인명 : {coin33}  |  현재가 = ￦{price33}  |  MACD = ￦{macd33}  |  보유수량 = {krw_balance33}  |  평가금액 = ￦{bp33}  ||  매수평균금액 = ￦{buy_bpAve33} ]")

                        if bp33 < buy_bpAve33: # 코인보유금액이 평균가보다 낮을때 매수시도
                            # 매수할 코인 금액 = 평균가 - 코인보유금액
                            buy_krw_price33 = buy_bpAve33 - bp33
                            # 매수할 코인 갯수 = 매수할 코인 금액 - 현재가
                            buy_krw_balance33 = buy_krw_price33 / price33

                            if krw33 >= buy_krw_price33: # 매수가능금액이 매수할금액보다 클때 매수시도
                                if buy_krw_price33 >= 10000:    # 매수가능금액이 최소주문가능금액인 ￦10,000원보다 높을때 매수시도

                                    # 매수할 코인명 - krw_coin33, 매수할 코인금액 - buy_krw_price33
                                    upbit.buy_market_order(krw_coin33, buy_krw_price33 * 0.9)

                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode33 = 1

                                    print("평균 이하 금액 매수")
                                    print(f"매수한금액 = ￦{buy_krw_price33}  |  매수한수량 = {buy_krw_balance33}  |  매수가능여부 - {op_mode33} - 매수불가-매도가능")
                                    print("")

                                else:
                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode33 = 1

                                    print("매수금액이 ￦10,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode33} - 매수불가-매도가능")
                                    print("")
                            else:   # 보유금액이 평균가와의 차이보다 적을때 매수
                                if krw33 >= 10000:    # 보유금액이 최소주문가능금액인 ￦10,000원보다 높을때 매수시도
                                    # 매수할 코인명 - krw_coin33, 매수할 코인금액 - krw33
                                    upbit.buy_market_order(krw_coin33, krw33 * 0.9)

                                    op_mode33 = 1

                                    print("보유금액보다 매수금액보다 적어서 매수금지")
                                    print(f"매수한금액 = ￦{krw33}  |  매수한수량 = {buy_krw_balance33}  |  매수가능여부 - {op_mode33} - 매수불가-매도가능")
                                    print("")
                                else:
                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode33 = 1

                                    print("보유금액이 ￦10,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode33} - 매수불가-매도가능")
                                    print("")

                        else:
                            # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                            op_mode33 = 1

                            print("보유금액이 평균금액보다 높아서 매수불가")
                            print(f"매수가능여부 - {op_mode33} - 매수불가-매도가능")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################


            ###############################
            # 코인34

            # 코인별 금액 비율조정
            buy_bpAve34 = bpAve * bpPer34

            # MACD 조건문
            if macd34 >= 0:     # macd가 0보다 크거나 같을때는 매수
                # 매수가능금액 불러오기
                krw34 = upbit.get_balance("KRW")

                if coinMode34 == 1 or coinMode34 == 2:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = >>>매수만가능<<< , 3 = 매도만가능
                    if op_mode34 == 2 or op_mode34 == 3:   # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                        print("")
                        print(f"[ 34. 매수시간 : {now}  |  코인명 : {coin34}  |  현재가 = ￦{price34}  |  MACD = ￦{macd34}  |  보유수량 = {krw_balance34}  |  평가금액 = ￦{bp34}  ||  매수평균금액 = ￦{buy_bpAve34} ]")

                        if bp34 < buy_bpAve34: # 코인보유금액이 평균가보다 낮을때 매수시도
                            # 매수할 코인 금액 = 평균가 - 코인보유금액
                            buy_krw_price34 = buy_bpAve34 - bp34
                            # 매수할 코인 갯수 = 매수할 코인 금액 - 현재가
                            buy_krw_balance34 = buy_krw_price34 / price34

                            if krw34 >= buy_krw_price34: # 매수가능금액이 매수할금액보다 클때 매수시도
                                if buy_krw_price34 >= 10000:    # 매수가능금액이 최소주문가능금액인 ￦10,000원보다 높을때 매수시도

                                    # 매수할 코인명 - krw_coin34, 매수할 코인금액 - buy_krw_price34
                                    upbit.buy_market_order(krw_coin34, buy_krw_price34 * 0.9)

                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode34 = 1

                                    print("평균 이하 금액 매수")
                                    print(f"매수한금액 = ￦{buy_krw_price34}  |  매수한수량 = {buy_krw_balance34}  |  매수가능여부 - {op_mode34} - 매수불가-매도가능")
                                    print("")

                                else:
                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode34 = 1

                                    print("매수금액이 ￦10,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode34} - 매수불가-매도가능")
                                    print("")
                            else:   # 보유금액이 평균가와의 차이보다 적을때 매수
                                if krw34 >= 10000:    # 보유금액이 최소주문가능금액인 ￦10,000원보다 높을때 매수시도
                                    # 매수할 코인명 - krw_coin34, 매수할 코인금액 - krw34
                                    upbit.buy_market_order(krw_coin34, krw34 * 0.9)

                                    op_mode34 = 1

                                    print("보유금액보다 매수금액보다 적어서 매수금지")
                                    print(f"매수한금액 = ￦{krw34}  |  매수한수량 = {buy_krw_balance34}  |  매수가능여부 - {op_mode34} - 매수불가-매도가능")
                                    print("")
                                else:
                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode34 = 1

                                    print("보유금액이 ￦10,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode34} - 매수불가-매도가능")
                                    print("")

                        else:
                            # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                            op_mode34 = 1

                            print("보유금액이 평균금액보다 높아서 매수불가")
                            print(f"매수가능여부 - {op_mode34} - 매수불가-매도가능")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################


            ###############################
            # 코인35

            # 코인별 금액 비율조정
            buy_bpAve35 = bpAve * bpPer35

            # MACD 조건문
            if macd35 >= 0:     # macd가 0보다 크거나 같을때는 매수
                # 매수가능금액 불러오기
                krw35 = upbit.get_balance("KRW")

                if coinMode35 == 1 or coinMode35 == 2:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = >>>매수만가능<<< , 3 = 매도만가능
                    if op_mode35 == 2 or op_mode35 == 3:   # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                        print("")
                        print(f"[ 35. 매수시간 : {now}  |  코인명 : {coin35}  |  현재가 = ￦{price35}  |  MACD = ￦{macd35}  |  보유수량 = {krw_balance35}  |  평가금액 = ￦{bp35}  ||  매수평균금액 = ￦{buy_bpAve35} ]")

                        if bp35 < buy_bpAve35: # 코인보유금액이 평균가보다 낮을때 매수시도
                            # 매수할 코인 금액 = 평균가 - 코인보유금액
                            buy_krw_price35 = buy_bpAve35 - bp35
                            # 매수할 코인 갯수 = 매수할 코인 금액 - 현재가
                            buy_krw_balance35 = buy_krw_price35 / price35

                            if krw35 >= buy_krw_price35: # 매수가능금액이 매수할금액보다 클때 매수시도
                                if buy_krw_price35 >= 10000:    # 매수가능금액이 최소주문가능금액인 ￦10,000원보다 높을때 매수시도

                                    # 매수할 코인명 - krw_coin35, 매수할 코인금액 - buy_krw_price35
                                    upbit.buy_market_order(krw_coin35, buy_krw_price35 * 0.9)

                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode35 = 1

                                    print("평균 이하 금액 매수")
                                    print(f"매수한금액 = ￦{buy_krw_price35}  |  매수한수량 = {buy_krw_balance35}  |  매수가능여부 - {op_mode35} - 매수불가-매도가능")
                                    print("")

                                else:
                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode35 = 1

                                    print("매수금액이 ￦10,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode35} - 매수불가-매도가능")
                                    print("")
                            else:   # 보유금액이 평균가와의 차이보다 적을때 매수
                                if krw35 >= 10000:    # 보유금액이 최소주문가능금액인 ￦10,000원보다 높을때 매수시도
                                    # 매수할 코인명 - krw_coin35, 매수할 코인금액 - krw35
                                    upbit.buy_market_order(krw_coin35, krw35 * 0.9)

                                    op_mode35 = 1

                                    print("보유금액보다 매수금액보다 적어서 매수금지")
                                    print(f"매수한금액 = ￦{krw35}  |  매수한수량 = {buy_krw_balance35}  |  매수가능여부 - {op_mode35} - 매수불가-매도가능")
                                    print("")
                                else:
                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode35 = 1

                                    print("보유금액이 ￦10,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode35} - 매수불가-매도가능")
                                    print("")

                        else:
                            # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                            op_mode35 = 1

                            print("보유금액이 평균금액보다 높아서 매수불가")
                            print(f"매수가능여부 - {op_mode35} - 매수불가-매도가능")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################


            ###############################
            # 코인36

            # 코인별 금액 비율조정
            buy_bpAve36 = bpAve * bpPer36

            # MACD 조건문
            if macd36 >= 0:     # macd가 0보다 크거나 같을때는 매수
                # 매수가능금액 불러오기
                krw36 = upbit.get_balance("KRW")

                if coinMode36 == 1 or coinMode36 == 2:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = >>>매수만가능<<< , 3 = 매도만가능
                    if op_mode36 == 2 or op_mode36 == 3:   # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                        print("")
                        print(f"[ 36. 매수시간 : {now}  |  코인명 : {coin36}  |  현재가 = ￦{price36}  |  MACD = ￦{macd36}  |  보유수량 = {krw_balance36}  |  평가금액 = ￦{bp36}  ||  매수평균금액 = ￦{buy_bpAve36} ]")

                        if bp36 < buy_bpAve36: # 코인보유금액이 평균가보다 낮을때 매수시도
                            # 매수할 코인 금액 = 평균가 - 코인보유금액
                            buy_krw_price36 = buy_bpAve36 - bp36
                            # 매수할 코인 갯수 = 매수할 코인 금액 - 현재가
                            buy_krw_balance36 = buy_krw_price36 / price36

                            if krw36 >= buy_krw_price36: # 매수가능금액이 매수할금액보다 클때 매수시도
                                if buy_krw_price36 >= 10000:    # 매수가능금액이 최소주문가능금액인 ￦10,000원보다 높을때 매수시도

                                    # 매수할 코인명 - krw_coin36, 매수할 코인금액 - buy_krw_price36
                                    upbit.buy_market_order(krw_coin36, buy_krw_price36 * 0.9)

                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode36 = 1

                                    print("평균 이하 금액 매수")
                                    print(f"매수한금액 = ￦{buy_krw_price36}  |  매수한수량 = {buy_krw_balance36}  |  매수가능여부 - {op_mode36} - 매수불가-매도가능")
                                    print("")

                                else:
                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode36 = 1

                                    print("매수금액이 ￦10,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode36} - 매수불가-매도가능")
                                    print("")
                            else:   # 보유금액이 평균가와의 차이보다 적을때 매수
                                if krw36 >= 10000:    # 보유금액이 최소주문가능금액인 ￦10,000원보다 높을때 매수시도
                                    # 매수할 코인명 - krw_coin36, 매수할 코인금액 - krw36
                                    upbit.buy_market_order(krw_coin36, krw36 * 0.9)

                                    op_mode36 = 1

                                    print("보유금액보다 매수금액보다 적어서 매수금지")
                                    print(f"매수한금액 = ￦{krw36}  |  매수한수량 = {buy_krw_balance36}  |  매수가능여부 - {op_mode36} - 매수불가-매도가능")
                                    print("")
                                else:
                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode36 = 1

                                    print("보유금액이 ￦10,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode36} - 매수불가-매도가능")
                                    print("")

                        else:
                            # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                            op_mode36 = 1

                            print("보유금액이 평균금액보다 높아서 매수불가")
                            print(f"매수가능여부 - {op_mode36} - 매수불가-매도가능")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################


            ###############################
            # 코인37

            # 코인별 금액 비율조정
            buy_bpAve37 = bpAve * bpPer37

            # MACD 조건문
            if macd37 >= 0:     # macd가 0보다 크거나 같을때는 매수
                # 매수가능금액 불러오기
                krw37 = upbit.get_balance("KRW")

                if coinMode37 == 1 or coinMode37 == 2:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = >>>매수만가능<<< , 3 = 매도만가능
                    if op_mode37 == 2 or op_mode37 == 3:   # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                        print("")
                        print(f"[ 37. 매수시간 : {now}  |  코인명 : {coin37}  |  현재가 = ￦{price37}  |  MACD = ￦{macd37}  |  보유수량 = {krw_balance37}  |  평가금액 = ￦{bp37}  ||  매수평균금액 = ￦{buy_bpAve37} ]")

                        if bp37 < buy_bpAve37: # 코인보유금액이 평균가보다 낮을때 매수시도
                            # 매수할 코인 금액 = 평균가 - 코인보유금액
                            buy_krw_price37 = buy_bpAve37 - bp37
                            # 매수할 코인 갯수 = 매수할 코인 금액 - 현재가
                            buy_krw_balance37 = buy_krw_price37 / price37

                            if krw37 >= buy_krw_price37: # 매수가능금액이 매수할금액보다 클때 매수시도
                                if buy_krw_price37 >= 10000:    # 매수가능금액이 최소주문가능금액인 ￦10,000원보다 높을때 매수시도

                                    # 매수할 코인명 - krw_coin37, 매수할 코인금액 - buy_krw_price37
                                    upbit.buy_market_order(krw_coin37, buy_krw_price37 * 0.9)

                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode37 = 1

                                    print("평균 이하 금액 매수")
                                    print(f"매수한금액 = ￦{buy_krw_price37}  |  매수한수량 = {buy_krw_balance37}  |  매수가능여부 - {op_mode37} - 매수불가-매도가능")
                                    print("")

                                else:
                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode37 = 1

                                    print("매수금액이 ￦10,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode37} - 매수불가-매도가능")
                                    print("")
                            else:   # 보유금액이 평균가와의 차이보다 적을때 매수
                                if krw37 >= 10000:    # 보유금액이 최소주문가능금액인 ￦10,000원보다 높을때 매수시도
                                    # 매수할 코인명 - krw_coin37, 매수할 코인금액 - krw37
                                    upbit.buy_market_order(krw_coin37, krw37 * 0.9)

                                    op_mode37 = 1

                                    print("보유금액보다 매수금액보다 적어서 매수금지")
                                    print(f"매수한금액 = ￦{krw37}  |  매수한수량 = {buy_krw_balance37}  |  매수가능여부 - {op_mode37} - 매수불가-매도가능")
                                    print("")
                                else:
                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode37 = 1

                                    print("보유금액이 ￦10,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode37} - 매수불가-매도가능")
                                    print("")

                        else:
                            # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                            op_mode37 = 1

                            print("보유금액이 평균금액보다 높아서 매수불가")
                            print(f"매수가능여부 - {op_mode37} - 매수불가-매도가능")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################


            ###############################
            # 코인38

            # 코인별 금액 비율조정
            buy_bpAve38 = bpAve * bpPer38

            # MACD 조건문
            if macd38 >= 0:     # macd가 0보다 크거나 같을때는 매수
                # 매수가능금액 불러오기
                krw38 = upbit.get_balance("KRW")

                if coinMode38 == 1 or coinMode38 == 2:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = >>>매수만가능<<< , 3 = 매도만가능
                    if op_mode38 == 2 or op_mode38 == 3:   # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                        print("")
                        print(f"[ 38. 매수시간 : {now}  |  코인명 : {coin38}  |  현재가 = ￦{price38}  |  MACD = ￦{macd38}  |  보유수량 = {krw_balance38}  |  평가금액 = ￦{bp38}  ||  매수평균금액 = ￦{buy_bpAve38} ]")

                        if bp38 < buy_bpAve38: # 코인보유금액이 평균가보다 낮을때 매수시도
                            # 매수할 코인 금액 = 평균가 - 코인보유금액
                            buy_krw_price38 = buy_bpAve38 - bp38
                            # 매수할 코인 갯수 = 매수할 코인 금액 - 현재가
                            buy_krw_balance38 = buy_krw_price38 / price38

                            if krw38 >= buy_krw_price38: # 매수가능금액이 매수할금액보다 클때 매수시도
                                if buy_krw_price38 >= 10000:    # 매수가능금액이 최소주문가능금액인 ￦10,000원보다 높을때 매수시도

                                    # 매수할 코인명 - krw_coin38, 매수할 코인금액 - buy_krw_price38
                                    upbit.buy_market_order(krw_coin38, buy_krw_price38 * 0.9)

                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode38 = 1

                                    print("평균 이하 금액 매수")
                                    print(f"매수한금액 = ￦{buy_krw_price38}  |  매수한수량 = {buy_krw_balance38}  |  매수가능여부 - {op_mode38} - 매수불가-매도가능")
                                    print("")

                                else:
                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode38 = 1

                                    print("매수금액이 ￦10,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode38} - 매수불가-매도가능")
                                    print("")
                            else:   # 보유금액이 평균가와의 차이보다 적을때 매수
                                if krw38 >= 10000:    # 보유금액이 최소주문가능금액인 ￦10,000원보다 높을때 매수시도
                                    # 매수할 코인명 - krw_coin38, 매수할 코인금액 - krw38
                                    upbit.buy_market_order(krw_coin38, krw38 * 0.9)

                                    op_mode38 = 1

                                    print("보유금액보다 매수금액보다 적어서 매수금지")
                                    print(f"매수한금액 = ￦{krw38}  |  매수한수량 = {buy_krw_balance38}  |  매수가능여부 - {op_mode38} - 매수불가-매도가능")
                                    print("")
                                else:
                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode38 = 1

                                    print("보유금액이 ￦10,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode38} - 매수불가-매도가능")
                                    print("")

                        else:
                            # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                            op_mode38 = 1

                            print("보유금액이 평균금액보다 높아서 매수불가")
                            print(f"매수가능여부 - {op_mode38} - 매수불가-매도가능")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################


            ###############################
            # 코인39

            # 코인별 금액 비율조정
            buy_bpAve39 = bpAve * bpPer39

            # MACD 조건문
            if macd39 >= 0:     # macd가 0보다 크거나 같을때는 매수
                # 매수가능금액 불러오기
                krw39 = upbit.get_balance("KRW")

                if coinMode39 == 1 or coinMode39 == 2:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = >>>매수만가능<<< , 3 = 매도만가능
                    if op_mode39 == 2 or op_mode39 == 3:   # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                        print("")
                        print(f"[ 39. 매수시간 : {now}  |  코인명 : {coin39}  |  현재가 = ￦{price39}  |  MACD = ￦{macd39}  |  보유수량 = {krw_balance39}  |  평가금액 = ￦{bp39}  ||  매수평균금액 = ￦{buy_bpAve39} ]")

                        if bp39 < buy_bpAve39: # 코인보유금액이 평균가보다 낮을때 매수시도
                            # 매수할 코인 금액 = 평균가 - 코인보유금액
                            buy_krw_price39 = buy_bpAve39 - bp39
                            # 매수할 코인 갯수 = 매수할 코인 금액 - 현재가
                            buy_krw_balance39 = buy_krw_price39 / price39

                            if krw39 >= buy_krw_price39: # 매수가능금액이 매수할금액보다 클때 매수시도
                                if buy_krw_price39 >= 10000:    # 매수가능금액이 최소주문가능금액인 ￦10,000원보다 높을때 매수시도

                                    # 매수할 코인명 - krw_coin39, 매수할 코인금액 - buy_krw_price39
                                    upbit.buy_market_order(krw_coin39, buy_krw_price39 * 0.9)

                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode39 = 1

                                    print("평균 이하 금액 매수")
                                    print(f"매수한금액 = ￦{buy_krw_price39}  |  매수한수량 = {buy_krw_balance39}  |  매수가능여부 - {op_mode39} - 매수불가-매도가능")
                                    print("")

                                else:
                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode39 = 1

                                    print("매수금액이 ￦10,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode39} - 매수불가-매도가능")
                                    print("")
                            else:   # 보유금액이 평균가와의 차이보다 적을때 매수
                                if krw39 >= 10000:    # 보유금액이 최소주문가능금액인 ￦10,000원보다 높을때 매수시도
                                    # 매수할 코인명 - krw_coin39, 매수할 코인금액 - krw39
                                    upbit.buy_market_order(krw_coin39, krw39 * 0.9)

                                    op_mode39 = 1

                                    print("보유금액보다 매수금액보다 적어서 매수금지")
                                    print(f"매수한금액 = ￦{krw39}  |  매수한수량 = {buy_krw_balance39}  |  매수가능여부 - {op_mode39} - 매수불가-매도가능")
                                    print("")
                                else:
                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode39 = 1

                                    print("보유금액이 ￦10,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode39} - 매수불가-매도가능")
                                    print("")

                        else:
                            # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                            op_mode39 = 1

                            print("보유금액이 평균금액보다 높아서 매수불가")
                            print(f"매수가능여부 - {op_mode39} - 매수불가-매도가능")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################


            ###############################
            # 코인40

            # 코인별 금액 비율조정
            buy_bpAve40 = bpAve * bpPer40

            # MACD 조건문
            if macd40 >= 0:     # macd가 0보다 크거나 같을때는 매수
                # 매수가능금액 불러오기
                krw40 = upbit.get_balance("KRW")

                if coinMode40 == 1 or coinMode40 == 2:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = >>>매수만가능<<< , 3 = 매도만가능
                    if op_mode40 == 2 or op_mode40 == 3:   # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                        print("")
                        print(f"[ 40. 매수시간 : {now}  |  코인명 : {coin40}  |  현재가 = ￦{price40}  |  MACD = ￦{macd40}  |  보유수량 = {krw_balance40}  |  평가금액 = ￦{bp40}  ||  매수평균금액 = ￦{buy_bpAve40} ]")

                        if bp40 < buy_bpAve40: # 코인보유금액이 평균가보다 낮을때 매수시도
                            # 매수할 코인 금액 = 평균가 - 코인보유금액
                            buy_krw_price40 = buy_bpAve40 - bp40
                            # 매수할 코인 갯수 = 매수할 코인 금액 - 현재가
                            buy_krw_balance40 = buy_krw_price40 / price40

                            if krw40 >= buy_krw_price40: # 매수가능금액이 매수할금액보다 클때 매수시도
                                if buy_krw_price40 >= 10000:    # 매수가능금액이 최소주문가능금액인 ￦10,000원보다 높을때 매수시도

                                    # 매수할 코인명 - krw_coin40, 매수할 코인금액 - buy_krw_price40
                                    upbit.buy_market_order(krw_coin40, buy_krw_price40 * 0.9)

                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode40 = 1

                                    print("평균 이하 금액 매수")
                                    print(f"매수한금액 = ￦{buy_krw_price40}  |  매수한수량 = {buy_krw_balance40}  |  매수가능여부 - {op_mode40} - 매수불가-매도가능")
                                    print("")

                                else:
                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode40 = 1

                                    print("매수금액이 ￦10,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode40} - 매수불가-매도가능")
                                    print("")
                            else:   # 보유금액이 평균가와의 차이보다 적을때 매수
                                if krw40 >= 10000:    # 보유금액이 최소주문가능금액인 ￦10,000원보다 높을때 매수시도
                                    # 매수할 코인명 - krw_coin40, 매수할 코인금액 - krw40
                                    upbit.buy_market_order(krw_coin40, krw40 * 0.9)

                                    op_mode40 = 1

                                    print("보유금액보다 매수금액보다 적어서 매수금지")
                                    print(f"매수한금액 = ￦{krw40}  |  매수한수량 = {buy_krw_balance40}  |  매수가능여부 - {op_mode40} - 매수불가-매도가능")
                                    print("")
                                else:
                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode40 = 1

                                    print("보유금액이 ￦10,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode40} - 매수불가-매도가능")
                                    print("")

                        else:
                            # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                            op_mode40 = 1

                            print("보유금액이 평균금액보다 높아서 매수불가")
                            print(f"매수가능여부 - {op_mode40} - 매수불가-매도가능")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################





            ######################################################################################################################################################
            ######################################################################################################################################################
            ######################################################################################################################################################





            ###############################
            # 코인41

            # 코인별 금액 비율조정
            buy_bpAve41 = bpAve * bpPer41

            # MACD 조건문
            if macd41 >= 0:     # macd가 0보다 크거나 같을때는 매수
                # 매수가능금액 불러오기
                krw41 = upbit.get_balance("KRW")

                if coinMode41 == 1 or coinMode41 == 2:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = >>>매수만가능<<< , 3 = 매도만가능
                    if op_mode41 == 2 or op_mode41 == 3:   # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                        print("")
                        print(f"[ 41. 매수시간 : {now}  |  코인명 : {coin41}  |  현재가 = ￦{price41}  |  MACD = ￦{macd41}  |  보유수량 = {krw_balance41}  |  평가금액 = ￦{bp41}  ||  매수평균금액 = ￦{buy_bpAve41} ]")

                        if bp41 < buy_bpAve41: # 코인보유금액이 평균가보다 낮을때 매수시도
                            # 매수할 코인 금액 = 평균가 - 코인보유금액
                            buy_krw_price41 = buy_bpAve41 - bp41
                            # 매수할 코인 갯수 = 매수할 코인 금액 - 현재가
                            buy_krw_balance41 = buy_krw_price41 / price41

                            if krw41 >= buy_krw_price41: # 매수가능금액이 매수할금액보다 클때 매수시도
                                if buy_krw_price41 >= 10000:    # 매수가능금액이 최소주문가능금액인 ￦10,000원보다 높을때 매수시도

                                    # 매수할 코인명 - krw_coin41, 매수할 코인금액 - buy_krw_price41
                                    upbit.buy_market_order(krw_coin41, buy_krw_price41 * 0.9)

                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode41 = 1

                                    print("평균 이하 금액 매수")
                                    print(f"매수한금액 = ￦{buy_krw_price41}  |  매수한수량 = {buy_krw_balance41}  |  매수가능여부 - {op_mode41} - 매수불가-매도가능")
                                    print("")

                                else:
                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode41 = 1

                                    print("매수금액이 ￦10,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode41} - 매수불가-매도가능")
                                    print("")
                            else:   # 보유금액이 평균가와의 차이보다 적을때 매수
                                if krw41 >= 10000:    # 보유금액이 최소주문가능금액인 ￦10,000원보다 높을때 매수시도
                                    # 매수할 코인명 - krw_coin41, 매수할 코인금액 - krw41
                                    upbit.buy_market_order(krw_coin41, krw41 * 0.9)

                                    op_mode41 = 1

                                    print("보유금액보다 매수금액보다 적어서 매수금지")
                                    print(f"매수한금액 = ￦{krw41}  |  매수한수량 = {buy_krw_balance41}  |  매수가능여부 - {op_mode41} - 매수불가-매도가능")
                                    print("")
                                else:
                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode41 = 1

                                    print("보유금액이 ￦10,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode41} - 매수불가-매도가능")
                                    print("")

                        else:
                            # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                            op_mode41 = 1

                            print("보유금액이 평균금액보다 높아서 매수불가")
                            print(f"매수가능여부 - {op_mode41} - 매수불가-매도가능")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################


            ###############################
            # 코인42

            # 코인별 금액 비율조정
            buy_bpAve42 = bpAve * bpPer42

            # MACD 조건문
            if macd42 >= 0:     # macd가 0보다 크거나 같을때는 매수
                # 매수가능금액 불러오기
                krw42 = upbit.get_balance("KRW")

                if coinMode42 == 1 or coinMode42 == 2:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = >>>매수만가능<<< , 3 = 매도만가능
                    if op_mode42 == 2 or op_mode42 == 3:   # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                        print("")
                        print(f"[ 42. 매수시간 : {now}  |  코인명 : {coin42}  |  현재가 = ￦{price42}  |  MACD = ￦{macd42}  |  보유수량 = {krw_balance42}  |  평가금액 = ￦{bp42}  ||  매수평균금액 = ￦{buy_bpAve42} ]")

                        if bp42 < buy_bpAve42: # 코인보유금액이 평균가보다 낮을때 매수시도
                            # 매수할 코인 금액 = 평균가 - 코인보유금액
                            buy_krw_price42 = buy_bpAve42 - bp42
                            # 매수할 코인 갯수 = 매수할 코인 금액 - 현재가
                            buy_krw_balance42 = buy_krw_price42 / price42

                            if krw42 >= buy_krw_price42: # 매수가능금액이 매수할금액보다 클때 매수시도
                                if buy_krw_price42 >= 10000:    # 매수가능금액이 최소주문가능금액인 ￦10,000원보다 높을때 매수시도

                                    # 매수할 코인명 - krw_coin42, 매수할 코인금액 - buy_krw_price42
                                    upbit.buy_market_order(krw_coin42, buy_krw_price42 * 0.9)

                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode42 = 1

                                    print("평균 이하 금액 매수")
                                    print(f"매수한금액 = ￦{buy_krw_price42}  |  매수한수량 = {buy_krw_balance42}  |  매수가능여부 - {op_mode42} - 매수불가-매도가능")
                                    print("")

                                else:
                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode42 = 1

                                    print("매수금액이 ￦10,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode42} - 매수불가-매도가능")
                                    print("")
                            else:   # 보유금액이 평균가와의 차이보다 적을때 매수
                                if krw42 >= 10000:    # 보유금액이 최소주문가능금액인 ￦10,000원보다 높을때 매수시도
                                    # 매수할 코인명 - krw_coin42, 매수할 코인금액 - krw42
                                    upbit.buy_market_order(krw_coin42, krw42 * 0.9)

                                    op_mode42 = 1

                                    print("보유금액보다 매수금액보다 적어서 매수금지")
                                    print(f"매수한금액 = ￦{krw42}  |  매수한수량 = {buy_krw_balance42}  |  매수가능여부 - {op_mode42} - 매수불가-매도가능")
                                    print("")
                                else:
                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode42 = 1

                                    print("보유금액이 ￦10,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode42} - 매수불가-매도가능")
                                    print("")

                        else:
                            # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                            op_mode42 = 1

                            print("보유금액이 평균금액보다 높아서 매수불가")
                            print(f"매수가능여부 - {op_mode42} - 매수불가-매도가능")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################


            ###############################
            # 코인43

            # 코인별 금액 비율조정
            buy_bpAve43 = bpAve * bpPer43

            # MACD 조건문
            if macd43 >= 0:     # macd가 0보다 크거나 같을때는 매수
                # 매수가능금액 불러오기
                krw43 = upbit.get_balance("KRW")

                if coinMode43 == 1 or coinMode43 == 2:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = >>>매수만가능<<< , 3 = 매도만가능
                    if op_mode43 == 2 or op_mode43 == 3:   # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                        print("")
                        print(f"[ 43. 매수시간 : {now}  |  코인명 : {coin43}  |  현재가 = ￦{price43}  |  MACD = ￦{macd43}  |  보유수량 = {krw_balance43}  |  평가금액 = ￦{bp43}  ||  매수평균금액 = ￦{buy_bpAve43} ]")

                        if bp43 < buy_bpAve43: # 코인보유금액이 평균가보다 낮을때 매수시도
                            # 매수할 코인 금액 = 평균가 - 코인보유금액
                            buy_krw_price43 = buy_bpAve43 - bp43
                            # 매수할 코인 갯수 = 매수할 코인 금액 - 현재가
                            buy_krw_balance43 = buy_krw_price43 / price43

                            if krw43 >= buy_krw_price43: # 매수가능금액이 매수할금액보다 클때 매수시도
                                if buy_krw_price43 >= 10000:    # 매수가능금액이 최소주문가능금액인 ￦10,000원보다 높을때 매수시도

                                    # 매수할 코인명 - krw_coin43, 매수할 코인금액 - buy_krw_price43
                                    upbit.buy_market_order(krw_coin43, buy_krw_price43 * 0.9)

                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode43 = 1

                                    print("평균 이하 금액 매수")
                                    print(f"매수한금액 = ￦{buy_krw_price43}  |  매수한수량 = {buy_krw_balance43}  |  매수가능여부 - {op_mode43} - 매수불가-매도가능")
                                    print("")

                                else:
                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode43 = 1

                                    print("매수금액이 ￦10,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode43} - 매수불가-매도가능")
                                    print("")
                            else:   # 보유금액이 평균가와의 차이보다 적을때 매수
                                if krw43 >= 10000:    # 보유금액이 최소주문가능금액인 ￦10,000원보다 높을때 매수시도
                                    # 매수할 코인명 - krw_coin43, 매수할 코인금액 - krw43
                                    upbit.buy_market_order(krw_coin43, krw43 * 0.9)

                                    op_mode43 = 1

                                    print("보유금액보다 매수금액보다 적어서 매수금지")
                                    print(f"매수한금액 = ￦{krw43}  |  매수한수량 = {buy_krw_balance43}  |  매수가능여부 - {op_mode43} - 매수불가-매도가능")
                                    print("")
                                else:
                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode43 = 1

                                    print("보유금액이 ￦10,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode43} - 매수불가-매도가능")
                                    print("")

                        else:
                            # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                            op_mode43 = 1

                            print("보유금액이 평균금액보다 높아서 매수불가")
                            print(f"매수가능여부 - {op_mode43} - 매수불가-매도가능")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################


            ###############################
            # 코인44

            # 코인별 금액 비율조정
            buy_bpAve44 = bpAve * bpPer44

            # MACD 조건문
            if macd44 >= 0:     # macd가 0보다 크거나 같을때는 매수
                # 매수가능금액 불러오기
                krw44 = upbit.get_balance("KRW")

                if coinMode44 == 1 or coinMode44 == 2:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = >>>매수만가능<<< , 3 = 매도만가능
                    if op_mode44 == 2 or op_mode44 == 3:   # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                        print("")
                        print(f"[ 44. 매수시간 : {now}  |  코인명 : {coin44}  |  현재가 = ￦{price44}  |  MACD = ￦{macd44}  |  보유수량 = {krw_balance44}  |  평가금액 = ￦{bp44}  ||  매수평균금액 = ￦{buy_bpAve44} ]")

                        if bp44 < buy_bpAve44: # 코인보유금액이 평균가보다 낮을때 매수시도
                            # 매수할 코인 금액 = 평균가 - 코인보유금액
                            buy_krw_price44 = buy_bpAve44 - bp44
                            # 매수할 코인 갯수 = 매수할 코인 금액 - 현재가
                            buy_krw_balance44 = buy_krw_price44 / price44

                            if krw44 >= buy_krw_price44: # 매수가능금액이 매수할금액보다 클때 매수시도
                                if buy_krw_price44 >= 10000:    # 매수가능금액이 최소주문가능금액인 ￦10,000원보다 높을때 매수시도

                                    # 매수할 코인명 - krw_coin44, 매수할 코인금액 - buy_krw_price44
                                    upbit.buy_market_order(krw_coin44, buy_krw_price44 * 0.9)

                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode44 = 1

                                    print("평균 이하 금액 매수")
                                    print(f"매수한금액 = ￦{buy_krw_price44}  |  매수한수량 = {buy_krw_balance44}  |  매수가능여부 - {op_mode44} - 매수불가-매도가능")
                                    print("")

                                else:
                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode44 = 1

                                    print("매수금액이 ￦10,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode44} - 매수불가-매도가능")
                                    print("")
                            else:   # 보유금액이 평균가와의 차이보다 적을때 매수
                                if krw44 >= 10000:    # 보유금액이 최소주문가능금액인 ￦10,000원보다 높을때 매수시도
                                    # 매수할 코인명 - krw_coin44, 매수할 코인금액 - krw44
                                    upbit.buy_market_order(krw_coin44, krw44 * 0.9)

                                    op_mode44 = 1

                                    print("보유금액보다 매수금액보다 적어서 매수금지")
                                    print(f"매수한금액 = ￦{krw44}  |  매수한수량 = {buy_krw_balance44}  |  매수가능여부 - {op_mode44} - 매수불가-매도가능")
                                    print("")
                                else:
                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode44 = 1

                                    print("보유금액이 ￦10,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode44} - 매수불가-매도가능")
                                    print("")

                        else:
                            # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                            op_mode44 = 1

                            print("보유금액이 평균금액보다 높아서 매수불가")
                            print(f"매수가능여부 - {op_mode44} - 매수불가-매도가능")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################


            ###############################
            # 코인45

            # 코인별 금액 비율조정
            buy_bpAve45 = bpAve * bpPer45

            # MACD 조건문
            if macd45 >= 0:     # macd가 0보다 크거나 같을때는 매수
                # 매수가능금액 불러오기
                krw45 = upbit.get_balance("KRW")

                if coinMode45 == 1 or coinMode45 == 2:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = >>>매수만가능<<< , 3 = 매도만가능
                    if op_mode45 == 2 or op_mode45 == 3:   # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                        print("")
                        print(f"[ 45. 매수시간 : {now}  |  코인명 : {coin45}  |  현재가 = ￦{price45}  |  MACD = ￦{macd45}  |  보유수량 = {krw_balance45}  |  평가금액 = ￦{bp45}  ||  매수평균금액 = ￦{buy_bpAve45} ]")

                        if bp45 < buy_bpAve45: # 코인보유금액이 평균가보다 낮을때 매수시도
                            # 매수할 코인 금액 = 평균가 - 코인보유금액
                            buy_krw_price45 = buy_bpAve45 - bp45
                            # 매수할 코인 갯수 = 매수할 코인 금액 - 현재가
                            buy_krw_balance45 = buy_krw_price45 / price45

                            if krw45 >= buy_krw_price45: # 매수가능금액이 매수할금액보다 클때 매수시도
                                if buy_krw_price45 >= 10000:    # 매수가능금액이 최소주문가능금액인 ￦10,000원보다 높을때 매수시도

                                    # 매수할 코인명 - krw_coin45, 매수할 코인금액 - buy_krw_price45
                                    upbit.buy_market_order(krw_coin45, buy_krw_price45 * 0.9)

                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode45 = 1

                                    print("평균 이하 금액 매수")
                                    print(f"매수한금액 = ￦{buy_krw_price45}  |  매수한수량 = {buy_krw_balance45}  |  매수가능여부 - {op_mode45} - 매수불가-매도가능")
                                    print("")

                                else:
                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode45 = 1

                                    print("매수금액이 ￦10,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode45} - 매수불가-매도가능")
                                    print("")
                            else:   # 보유금액이 평균가와의 차이보다 적을때 매수
                                if krw45 >= 10000:    # 보유금액이 최소주문가능금액인 ￦10,000원보다 높을때 매수시도
                                    # 매수할 코인명 - krw_coin45, 매수할 코인금액 - krw45
                                    upbit.buy_market_order(krw_coin45, krw45 * 0.9)

                                    op_mode45 = 1

                                    print("보유금액보다 매수금액보다 적어서 매수금지")
                                    print(f"매수한금액 = ￦{krw45}  |  매수한수량 = {buy_krw_balance45}  |  매수가능여부 - {op_mode45} - 매수불가-매도가능")
                                    print("")
                                else:
                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode45 = 1

                                    print("보유금액이 ￦10,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode45} - 매수불가-매도가능")
                                    print("")

                        else:
                            # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                            op_mode45 = 1

                            print("보유금액이 평균금액보다 높아서 매수불가")
                            print(f"매수가능여부 - {op_mode45} - 매수불가-매도가능")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################


            ###############################
            # 코인46

            # 코인별 금액 비율조정
            buy_bpAve46 = bpAve * bpPer46

            # MACD 조건문
            if macd46 >= 0:     # macd가 0보다 크거나 같을때는 매수
                # 매수가능금액 불러오기
                krw46 = upbit.get_balance("KRW")

                if coinMode46 == 1 or coinMode46 == 2:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = >>>매수만가능<<< , 3 = 매도만가능
                    if op_mode46 == 2 or op_mode46 == 3:   # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                        print("")
                        print(f"[ 46. 매수시간 : {now}  |  코인명 : {coin46}  |  현재가 = ￦{price46}  |  MACD = ￦{macd46}  |  보유수량 = {krw_balance46}  |  평가금액 = ￦{bp46}  ||  매수평균금액 = ￦{buy_bpAve46} ]")

                        if bp46 < buy_bpAve46: # 코인보유금액이 평균가보다 낮을때 매수시도
                            # 매수할 코인 금액 = 평균가 - 코인보유금액
                            buy_krw_price46 = buy_bpAve46 - bp46
                            # 매수할 코인 갯수 = 매수할 코인 금액 - 현재가
                            buy_krw_balance46 = buy_krw_price46 / price46

                            if krw46 >= buy_krw_price46: # 매수가능금액이 매수할금액보다 클때 매수시도
                                if buy_krw_price46 >= 10000:    # 매수가능금액이 최소주문가능금액인 ￦10,000원보다 높을때 매수시도

                                    # 매수할 코인명 - krw_coin46, 매수할 코인금액 - buy_krw_price46
                                    upbit.buy_market_order(krw_coin46, buy_krw_price46 * 0.9)

                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode46 = 1

                                    print("평균 이하 금액 매수")
                                    print(f"매수한금액 = ￦{buy_krw_price46}  |  매수한수량 = {buy_krw_balance46}  |  매수가능여부 - {op_mode46} - 매수불가-매도가능")
                                    print("")

                                else:
                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode46 = 1

                                    print("매수금액이 ￦10,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode46} - 매수불가-매도가능")
                                    print("")
                            else:   # 보유금액이 평균가와의 차이보다 적을때 매수
                                if krw46 >= 10000:    # 보유금액이 최소주문가능금액인 ￦10,000원보다 높을때 매수시도
                                    # 매수할 코인명 - krw_coin46, 매수할 코인금액 - krw46
                                    upbit.buy_market_order(krw_coin46, krw46 * 0.9)

                                    op_mode46 = 1

                                    print("보유금액보다 매수금액보다 적어서 매수금지")
                                    print(f"매수한금액 = ￦{krw46}  |  매수한수량 = {buy_krw_balance46}  |  매수가능여부 - {op_mode46} - 매수불가-매도가능")
                                    print("")
                                else:
                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode46 = 1

                                    print("보유금액이 ￦10,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode46} - 매수불가-매도가능")
                                    print("")

                        else:
                            # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                            op_mode46 = 1

                            print("보유금액이 평균금액보다 높아서 매수불가")
                            print(f"매수가능여부 - {op_mode46} - 매수불가-매도가능")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################


            ###############################
            # 코인47

            # 코인별 금액 비율조정
            buy_bpAve47 = bpAve * bpPer47

            # MACD 조건문
            if macd47 >= 0:     # macd가 0보다 크거나 같을때는 매수
                # 매수가능금액 불러오기
                krw47 = upbit.get_balance("KRW")

                if coinMode47 == 1 or coinMode47 == 2:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = >>>매수만가능<<< , 3 = 매도만가능
                    if op_mode47 == 2 or op_mode47 == 3:   # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                        print("")
                        print(f"[ 47. 매수시간 : {now}  |  코인명 : {coin47}  |  현재가 = ￦{price47}  |  MACD = ￦{macd47}  |  보유수량 = {krw_balance47}  |  평가금액 = ￦{bp47}  ||  매수평균금액 = ￦{buy_bpAve47} ]")

                        if bp47 < buy_bpAve47: # 코인보유금액이 평균가보다 낮을때 매수시도
                            # 매수할 코인 금액 = 평균가 - 코인보유금액
                            buy_krw_price47 = buy_bpAve47 - bp47
                            # 매수할 코인 갯수 = 매수할 코인 금액 - 현재가
                            buy_krw_balance47 = buy_krw_price47 / price47

                            if krw47 >= buy_krw_price47: # 매수가능금액이 매수할금액보다 클때 매수시도
                                if buy_krw_price47 >= 10000:    # 매수가능금액이 최소주문가능금액인 ￦10,000원보다 높을때 매수시도

                                    # 매수할 코인명 - krw_coin47, 매수할 코인금액 - buy_krw_price47
                                    upbit.buy_market_order(krw_coin47, buy_krw_price47 * 0.9)

                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode47 = 1

                                    print("평균 이하 금액 매수")
                                    print(f"매수한금액 = ￦{buy_krw_price47}  |  매수한수량 = {buy_krw_balance47}  |  매수가능여부 - {op_mode47} - 매수불가-매도가능")
                                    print("")

                                else:
                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode47 = 1

                                    print("매수금액이 ￦10,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode47} - 매수불가-매도가능")
                                    print("")
                            else:   # 보유금액이 평균가와의 차이보다 적을때 매수
                                if krw47 >= 10000:    # 보유금액이 최소주문가능금액인 ￦10,000원보다 높을때 매수시도
                                    # 매수할 코인명 - krw_coin47, 매수할 코인금액 - krw47
                                    upbit.buy_market_order(krw_coin47, krw47 * 0.9)

                                    op_mode47 = 1

                                    print("보유금액보다 매수금액보다 적어서 매수금지")
                                    print(f"매수한금액 = ￦{krw47}  |  매수한수량 = {buy_krw_balance47}  |  매수가능여부 - {op_mode47} - 매수불가-매도가능")
                                    print("")
                                else:
                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode47 = 1

                                    print("보유금액이 ￦10,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode47} - 매수불가-매도가능")
                                    print("")

                        else:
                            # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                            op_mode47 = 1

                            print("보유금액이 평균금액보다 높아서 매수불가")
                            print(f"매수가능여부 - {op_mode47} - 매수불가-매도가능")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################


            ###############################
            # 코인48

            # 코인별 금액 비율조정
            buy_bpAve48 = bpAve * bpPer48

            # MACD 조건문
            if macd48 >= 0:     # macd가 0보다 크거나 같을때는 매수
                # 매수가능금액 불러오기
                krw48 = upbit.get_balance("KRW")

                if coinMode48 == 1 or coinMode48 == 2:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = >>>매수만가능<<< , 3 = 매도만가능
                    if op_mode48 == 2 or op_mode48 == 3:   # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                        print("")
                        print(f"[ 48. 매수시간 : {now}  |  코인명 : {coin48}  |  현재가 = ￦{price48}  |  MACD = ￦{macd48}  |  보유수량 = {krw_balance48}  |  평가금액 = ￦{bp48}  ||  매수평균금액 = ￦{buy_bpAve48} ]")

                        if bp48 < buy_bpAve48: # 코인보유금액이 평균가보다 낮을때 매수시도
                            # 매수할 코인 금액 = 평균가 - 코인보유금액
                            buy_krw_price48 = buy_bpAve48 - bp48
                            # 매수할 코인 갯수 = 매수할 코인 금액 - 현재가
                            buy_krw_balance48 = buy_krw_price48 / price48

                            if krw48 >= buy_krw_price48: # 매수가능금액이 매수할금액보다 클때 매수시도
                                if buy_krw_price48 >= 10000:    # 매수가능금액이 최소주문가능금액인 ￦10,000원보다 높을때 매수시도

                                    # 매수할 코인명 - krw_coin48, 매수할 코인금액 - buy_krw_price48
                                    upbit.buy_market_order(krw_coin48, buy_krw_price48 * 0.9)

                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode48 = 1

                                    print("평균 이하 금액 매수")
                                    print(f"매수한금액 = ￦{buy_krw_price48}  |  매수한수량 = {buy_krw_balance48}  |  매수가능여부 - {op_mode48} - 매수불가-매도가능")
                                    print("")

                                else:
                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode48 = 1

                                    print("매수금액이 ￦10,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode48} - 매수불가-매도가능")
                                    print("")
                            else:   # 보유금액이 평균가와의 차이보다 적을때 매수
                                if krw48 >= 10000:    # 보유금액이 최소주문가능금액인 ￦10,000원보다 높을때 매수시도
                                    # 매수할 코인명 - krw_coin48, 매수할 코인금액 - krw48
                                    upbit.buy_market_order(krw_coin48, krw48 * 0.9)

                                    op_mode48 = 1

                                    print("보유금액보다 매수금액보다 적어서 매수금지")
                                    print(f"매수한금액 = ￦{krw48}  |  매수한수량 = {buy_krw_balance48}  |  매수가능여부 - {op_mode48} - 매수불가-매도가능")
                                    print("")
                                else:
                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode48 = 1

                                    print("보유금액이 ￦10,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode48} - 매수불가-매도가능")
                                    print("")

                        else:
                            # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                            op_mode48 = 1

                            print("보유금액이 평균금액보다 높아서 매수불가")
                            print(f"매수가능여부 - {op_mode48} - 매수불가-매도가능")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################


            ###############################
            # 코인49

            # 코인별 금액 비율조정
            buy_bpAve49 = bpAve * bpPer49

            # MACD 조건문
            if macd49 >= 0:     # macd가 0보다 크거나 같을때는 매수
                # 매수가능금액 불러오기
                krw49 = upbit.get_balance("KRW")

                if coinMode49 == 1 or coinMode49 == 2:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = >>>매수만가능<<< , 3 = 매도만가능
                    if op_mode49 == 2 or op_mode49 == 3:   # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                        print("")
                        print(f"[ 49. 매수시간 : {now}  |  코인명 : {coin49}  |  현재가 = ￦{price49}  |  MACD = ￦{macd49}  |  보유수량 = {krw_balance49}  |  평가금액 = ￦{bp49}  ||  매수평균금액 = ￦{buy_bpAve49} ]")

                        if bp49 < buy_bpAve49: # 코인보유금액이 평균가보다 낮을때 매수시도
                            # 매수할 코인 금액 = 평균가 - 코인보유금액
                            buy_krw_price49 = buy_bpAve49 - bp49
                            # 매수할 코인 갯수 = 매수할 코인 금액 - 현재가
                            buy_krw_balance49 = buy_krw_price49 / price49

                            if krw49 >= buy_krw_price49: # 매수가능금액이 매수할금액보다 클때 매수시도
                                if buy_krw_price49 >= 10000:    # 매수가능금액이 최소주문가능금액인 ￦10,000원보다 높을때 매수시도

                                    # 매수할 코인명 - krw_coin49, 매수할 코인금액 - buy_krw_price49
                                    upbit.buy_market_order(krw_coin49, buy_krw_price49 * 0.9)

                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode49 = 1

                                    print("평균 이하 금액 매수")
                                    print(f"매수한금액 = ￦{buy_krw_price49}  |  매수한수량 = {buy_krw_balance49}  |  매수가능여부 - {op_mode49} - 매수불가-매도가능")
                                    print("")

                                else:
                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode49 = 1

                                    print("매수금액이 ￦10,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode49} - 매수불가-매도가능")
                                    print("")
                            else:   # 보유금액이 평균가와의 차이보다 적을때 매수
                                if krw49 >= 10000:    # 보유금액이 최소주문가능금액인 ￦10,000원보다 높을때 매수시도
                                    # 매수할 코인명 - krw_coin49, 매수할 코인금액 - krw49
                                    upbit.buy_market_order(krw_coin49, krw49 * 0.9)

                                    op_mode49 = 1

                                    print("보유금액보다 매수금액보다 적어서 매수금지")
                                    print(f"매수한금액 = ￦{krw49}  |  매수한수량 = {buy_krw_balance49}  |  매수가능여부 - {op_mode49} - 매수불가-매도가능")
                                    print("")
                                else:
                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode49 = 1

                                    print("보유금액이 ￦10,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode49} - 매수불가-매도가능")
                                    print("")

                        else:
                            # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                            op_mode49 = 1

                            print("보유금액이 평균금액보다 높아서 매수불가")
                            print(f"매수가능여부 - {op_mode49} - 매수불가-매도가능")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################


            ###############################
            # 코인50

            # 코인별 금액 비율조정
            buy_bpAve50 = bpAve * bpPer50

            # MACD 조건문
            if macd50 >= 0:     # macd가 0보다 크거나 같을때는 매수
                # 매수가능금액 불러오기
                krw50 = upbit.get_balance("KRW")

                if coinMode50 == 1 or coinMode50 == 2:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = >>>매수만가능<<< , 3 = 매도만가능
                    if op_mode50 == 2 or op_mode50 == 3:   # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                        print("")
                        print(f"[ 50. 매수시간 : {now}  |  코인명 : {coin50}  |  현재가 = ￦{price50}  |  MACD = ￦{macd50}  |  보유수량 = {krw_balance50}  |  평가금액 = ￦{bp50}  ||  매수평균금액 = ￦{buy_bpAve50} ]")

                        if bp50 < buy_bpAve50: # 코인보유금액이 평균가보다 낮을때 매수시도
                            # 매수할 코인 금액 = 평균가 - 코인보유금액
                            buy_krw_price50 = buy_bpAve50 - bp50
                            # 매수할 코인 갯수 = 매수할 코인 금액 - 현재가
                            buy_krw_balance50 = buy_krw_price50 / price50

                            if krw50 >= buy_krw_price50: # 매수가능금액이 매수할금액보다 클때 매수시도
                                if buy_krw_price50 >= 10000:    # 매수가능금액이 최소주문가능금액인 ￦10,000원보다 높을때 매수시도

                                    # 매수할 코인명 - krw_coin50, 매수할 코인금액 - buy_krw_price50
                                    upbit.buy_market_order(krw_coin50, buy_krw_price50 * 0.9)

                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode50 = 1

                                    print("평균 이하 금액 매수")
                                    print(f"매수한금액 = ￦{buy_krw_price50}  |  매수한수량 = {buy_krw_balance50}  |  매수가능여부 - {op_mode50} - 매수불가-매도가능")
                                    print("")

                                else:
                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode50 = 1

                                    print("매수금액이 ￦10,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode50} - 매수불가-매도가능")
                                    print("")
                            else:   # 보유금액이 평균가와의 차이보다 적을때 매수
                                if krw50 >= 10000:    # 보유금액이 최소주문가능금액인 ￦10,000원보다 높을때 매수시도
                                    # 매수할 코인명 - krw_coin50, 매수할 코인금액 - krw50
                                    upbit.buy_market_order(krw_coin50, krw50 * 0.9)

                                    op_mode50 = 1

                                    print("보유금액보다 매수금액보다 적어서 매수금지")
                                    print(f"매수한금액 = ￦{krw50}  |  매수한수량 = {buy_krw_balance50}  |  매수가능여부 - {op_mode50} - 매수불가-매도가능")
                                    print("")
                                else:
                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode50 = 1

                                    print("보유금액이 ￦10,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode50} - 매수불가-매도가능")
                                    print("")

                        else:
                            # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                            op_mode50 = 1

                            print("보유금액이 평균금액보다 높아서 매수불가")
                            print(f"매수가능여부 - {op_mode50} - 매수불가-매도가능")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################





            ######################################################################################################################################################
            ######################################################################################################################################################
            ######################################################################################################################################################
            ######################################################################################################################################################
            ######################################################################################################################################################




            ###############################
            # 코인51

            # 코인별 금액 비율조정
            buy_bpAve51 = bpAve * bpPer51

            # MACD 조건문
            if macd51 >= 0:     # macd가 0보다 크거나 같을때는 매수
                # 매수가능금액 불러오기
                krw51 = upbit.get_balance("KRW")

                if coinMode51 == 1 or coinMode51 == 2:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = >>>매수만가능<<< , 3 = 매도만가능
                    if op_mode51 == 2 or op_mode51 == 3:   # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                        print("")
                        print(f"[ 51. 매수시간 : {now}  |  코인명 : {coin51}  |  현재가 = ￦{price51}  |  MACD = ￦{macd51}  |  보유수량 = {krw_balance51}  |  평가금액 = ￦{bp51}  ||  매수평균금액 = ￦{buy_bpAve51} ]")

                        if bp51 < buy_bpAve51: # 코인보유금액이 평균가보다 낮을때 매수시도
                            # 매수할 코인 금액 = 평균가 - 코인보유금액
                            buy_krw_price51 = buy_bpAve51 - bp51
                            # 매수할 코인 갯수 = 매수할 코인 금액 - 현재가
                            buy_krw_balance51 = buy_krw_price51 / price51

                            if krw51 >= buy_krw_price51: # 매수가능금액이 매수할금액보다 클때 매수시도
                                if buy_krw_price51 >= 10000:    # 매수가능금액이 최소주문가능금액인 ￦10,000원보다 높을때 매수시도

                                    # 매수할 코인명 - krw_coin51, 매수할 코인금액 - buy_krw_price51
                                    upbit.buy_market_order(krw_coin51, buy_krw_price51 * 0.9)

                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode51 = 1

                                    print("평균 이하 금액 매수")
                                    print(f"매수한금액 = ￦{buy_krw_price51}  |  매수한수량 = {buy_krw_balance51}  |  매수가능여부 - {op_mode51} - 매수불가-매도가능")
                                    print("")

                                else:
                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode51 = 1

                                    print("매수금액이 ￦10,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode51} - 매수불가-매도가능")
                                    print("")
                            else:   # 보유금액이 평균가와의 차이보다 적을때 매수
                                if krw51 >= 10000:    # 보유금액이 최소주문가능금액인 ￦10,000원보다 높을때 매수시도
                                    # 매수할 코인명 - krw_coin51, 매수할 코인금액 - krw51
                                    upbit.buy_market_order(krw_coin51, krw51 * 0.9)

                                    op_mode51 = 1

                                    print("보유금액보다 매수금액보다 적어서 매수금지")
                                    print(f"매수한금액 = ￦{krw51}  |  매수한수량 = {buy_krw_balance51}  |  매수가능여부 - {op_mode51} - 매수불가-매도가능")
                                    print("")
                                else:
                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode51 = 1

                                    print("보유금액이 ￦10,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode51} - 매수불가-매도가능")
                                    print("")

                        else:
                            # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                            op_mode51 = 1

                            print("보유금액이 평균금액보다 높아서 매수불가")
                            print(f"매수가능여부 - {op_mode51} - 매수불가-매도가능")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################


            ###############################
            # 코인52

            # 코인별 금액 비율조정
            buy_bpAve52 = bpAve * bpPer52

            # MACD 조건문
            if macd52 >= 0:     # macd가 0보다 크거나 같을때는 매수
                # 매수가능금액 불러오기
                krw52 = upbit.get_balance("KRW")

                if coinMode52 == 1 or coinMode52 == 2:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = >>>매수만가능<<< , 3 = 매도만가능
                    if op_mode52 == 2 or op_mode52 == 3:   # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                        print("")
                        print(f"[ 52. 매수시간 : {now}  |  코인명 : {coin52}  |  현재가 = ￦{price52}  |  MACD = ￦{macd52}  |  보유수량 = {krw_balance52}  |  평가금액 = ￦{bp52}  ||  매수평균금액 = ￦{buy_bpAve52} ]")

                        if bp52 < buy_bpAve52: # 코인보유금액이 평균가보다 낮을때 매수시도
                            # 매수할 코인 금액 = 평균가 - 코인보유금액
                            buy_krw_price52 = buy_bpAve52 - bp52
                            # 매수할 코인 갯수 = 매수할 코인 금액 - 현재가
                            buy_krw_balance52 = buy_krw_price52 / price52

                            if krw52 >= buy_krw_price52: # 매수가능금액이 매수할금액보다 클때 매수시도
                                if buy_krw_price52 >= 10000:    # 매수가능금액이 최소주문가능금액인 ￦10,000원보다 높을때 매수시도

                                    # 매수할 코인명 - krw_coin52, 매수할 코인금액 - buy_krw_price52
                                    upbit.buy_market_order(krw_coin52, buy_krw_price52 * 0.9)

                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode52 = 1

                                    print("평균 이하 금액 매수")
                                    print(f"매수한금액 = ￦{buy_krw_price52}  |  매수한수량 = {buy_krw_balance52}  |  매수가능여부 - {op_mode52} - 매수불가-매도가능")
                                    print("")

                                else:
                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode52 = 1

                                    print("매수금액이 ￦10,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode52} - 매수불가-매도가능")
                                    print("")
                            else:   # 보유금액이 평균가와의 차이보다 적을때 매수
                                if krw52 >= 10000:    # 보유금액이 최소주문가능금액인 ￦10,000원보다 높을때 매수시도
                                    # 매수할 코인명 - krw_coin52, 매수할 코인금액 - krw52
                                    upbit.buy_market_order(krw_coin52, krw52 * 0.9)

                                    op_mode52 = 1

                                    print("보유금액보다 매수금액보다 적어서 매수금지")
                                    print(f"매수한금액 = ￦{krw52}  |  매수한수량 = {buy_krw_balance52}  |  매수가능여부 - {op_mode52} - 매수불가-매도가능")
                                    print("")
                                else:
                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode52 = 1

                                    print("보유금액이 ￦10,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode52} - 매수불가-매도가능")
                                    print("")

                        else:
                            # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                            op_mode52 = 1

                            print("보유금액이 평균금액보다 높아서 매수불가")
                            print(f"매수가능여부 - {op_mode52} - 매수불가-매도가능")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################


            ###############################
            # 코인53

            # 코인별 금액 비율조정
            buy_bpAve53 = bpAve * bpPer53

            # MACD 조건문
            if macd53 >= 0:     # macd가 0보다 크거나 같을때는 매수
                # 매수가능금액 불러오기
                krw53 = upbit.get_balance("KRW")

                if coinMode53 == 1 or coinMode53 == 2:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = >>>매수만가능<<< , 3 = 매도만가능
                    if op_mode53 == 2 or op_mode53 == 3:   # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                        print("")
                        print(f"[ 53. 매수시간 : {now}  |  코인명 : {coin53}  |  현재가 = ￦{price53}  |  MACD = ￦{macd53}  |  보유수량 = {krw_balance53}  |  평가금액 = ￦{bp53}  ||  매수평균금액 = ￦{buy_bpAve53} ]")

                        if bp53 < buy_bpAve53: # 코인보유금액이 평균가보다 낮을때 매수시도
                            # 매수할 코인 금액 = 평균가 - 코인보유금액
                            buy_krw_price53 = buy_bpAve53 - bp53
                            # 매수할 코인 갯수 = 매수할 코인 금액 - 현재가
                            buy_krw_balance53 = buy_krw_price53 / price53

                            if krw53 >= buy_krw_price53: # 매수가능금액이 매수할금액보다 클때 매수시도
                                if buy_krw_price53 >= 10000:    # 매수가능금액이 최소주문가능금액인 ￦10,000원보다 높을때 매수시도

                                    # 매수할 코인명 - krw_coin53, 매수할 코인금액 - buy_krw_price53
                                    upbit.buy_market_order(krw_coin53, buy_krw_price53 * 0.9)

                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode53 = 1

                                    print("평균 이하 금액 매수")
                                    print(f"매수한금액 = ￦{buy_krw_price53}  |  매수한수량 = {buy_krw_balance53}  |  매수가능여부 - {op_mode53} - 매수불가-매도가능")
                                    print("")

                                else:
                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode53 = 1

                                    print("매수금액이 ￦10,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode53} - 매수불가-매도가능")
                                    print("")
                            else:   # 보유금액이 평균가와의 차이보다 적을때 매수
                                if krw53 >= 10000:    # 보유금액이 최소주문가능금액인 ￦10,000원보다 높을때 매수시도
                                    # 매수할 코인명 - krw_coin53, 매수할 코인금액 - krw53
                                    upbit.buy_market_order(krw_coin53, krw53 * 0.9)

                                    op_mode53 = 1

                                    print("보유금액보다 매수금액보다 적어서 매수금지")
                                    print(f"매수한금액 = ￦{krw53}  |  매수한수량 = {buy_krw_balance53}  |  매수가능여부 - {op_mode53} - 매수불가-매도가능")
                                    print("")
                                else:
                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode53 = 1

                                    print("보유금액이 ￦10,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode53} - 매수불가-매도가능")
                                    print("")

                        else:
                            # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                            op_mode53 = 1

                            print("보유금액이 평균금액보다 높아서 매수불가")
                            print(f"매수가능여부 - {op_mode53} - 매수불가-매도가능")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################


            ###############################
            # 코인54

            # 코인별 금액 비율조정
            buy_bpAve54 = bpAve * bpPer54

            # MACD 조건문
            if macd54 >= 0:     # macd가 0보다 크거나 같을때는 매수
                # 매수가능금액 불러오기
                krw54 = upbit.get_balance("KRW")

                if coinMode54 == 1 or coinMode54 == 2:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = >>>매수만가능<<< , 3 = 매도만가능
                    if op_mode54 == 2 or op_mode54 == 3:   # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                        print("")
                        print(f"[ 54. 매수시간 : {now}  |  코인명 : {coin54}  |  현재가 = ￦{price54}  |  MACD = ￦{macd54}  |  보유수량 = {krw_balance54}  |  평가금액 = ￦{bp54}  ||  매수평균금액 = ￦{buy_bpAve54} ]")

                        if bp54 < buy_bpAve54: # 코인보유금액이 평균가보다 낮을때 매수시도
                            # 매수할 코인 금액 = 평균가 - 코인보유금액
                            buy_krw_price54 = buy_bpAve54 - bp54
                            # 매수할 코인 갯수 = 매수할 코인 금액 - 현재가
                            buy_krw_balance54 = buy_krw_price54 / price54

                            if krw54 >= buy_krw_price54: # 매수가능금액이 매수할금액보다 클때 매수시도
                                if buy_krw_price54 >= 10000:    # 매수가능금액이 최소주문가능금액인 ￦10,000원보다 높을때 매수시도

                                    # 매수할 코인명 - krw_coin54, 매수할 코인금액 - buy_krw_price54
                                    upbit.buy_market_order(krw_coin54, buy_krw_price54 * 0.9)

                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode54 = 1

                                    print("평균 이하 금액 매수")
                                    print(f"매수한금액 = ￦{buy_krw_price54}  |  매수한수량 = {buy_krw_balance54}  |  매수가능여부 - {op_mode54} - 매수불가-매도가능")
                                    print("")

                                else:
                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode54 = 1

                                    print("매수금액이 ￦10,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode54} - 매수불가-매도가능")
                                    print("")
                            else:   # 보유금액이 평균가와의 차이보다 적을때 매수
                                if krw54 >= 10000:    # 보유금액이 최소주문가능금액인 ￦10,000원보다 높을때 매수시도
                                    # 매수할 코인명 - krw_coin54, 매수할 코인금액 - krw54
                                    upbit.buy_market_order(krw_coin54, krw54 * 0.9)

                                    op_mode54 = 1

                                    print("보유금액보다 매수금액보다 적어서 매수금지")
                                    print(f"매수한금액 = ￦{krw54}  |  매수한수량 = {buy_krw_balance54}  |  매수가능여부 - {op_mode54} - 매수불가-매도가능")
                                    print("")
                                else:
                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode54 = 1

                                    print("보유금액이 ￦10,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode54} - 매수불가-매도가능")
                                    print("")

                        else:
                            # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                            op_mode54 = 1

                            print("보유금액이 평균금액보다 높아서 매수불가")
                            print(f"매수가능여부 - {op_mode54} - 매수불가-매도가능")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################


            ###############################
            # 코인55

            # 코인별 금액 비율조정
            buy_bpAve55 = bpAve * bpPer55

            # MACD 조건문
            if macd55 >= 0:     # macd가 0보다 크거나 같을때는 매수
                # 매수가능금액 불러오기
                krw55 = upbit.get_balance("KRW")

                if coinMode55 == 1 or coinMode55 == 2:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = >>>매수만가능<<< , 3 = 매도만가능
                    if op_mode55 == 2 or op_mode55 == 3:   # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                        print("")
                        print(f"[ 55. 매수시간 : {now}  |  코인명 : {coin55}  |  현재가 = ￦{price55}  |  MACD = ￦{macd55}  |  보유수량 = {krw_balance55}  |  평가금액 = ￦{bp55}  ||  매수평균금액 = ￦{buy_bpAve55} ]")

                        if bp55 < buy_bpAve55: # 코인보유금액이 평균가보다 낮을때 매수시도
                            # 매수할 코인 금액 = 평균가 - 코인보유금액
                            buy_krw_price55 = buy_bpAve55 - bp55
                            # 매수할 코인 갯수 = 매수할 코인 금액 - 현재가
                            buy_krw_balance55 = buy_krw_price55 / price55

                            if krw55 >= buy_krw_price55: # 매수가능금액이 매수할금액보다 클때 매수시도
                                if buy_krw_price55 >= 10000:    # 매수가능금액이 최소주문가능금액인 ￦10,000원보다 높을때 매수시도

                                    # 매수할 코인명 - krw_coin55, 매수할 코인금액 - buy_krw_price55
                                    upbit.buy_market_order(krw_coin55, buy_krw_price55 * 0.9)

                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode55 = 1

                                    print("평균 이하 금액 매수")
                                    print(f"매수한금액 = ￦{buy_krw_price55}  |  매수한수량 = {buy_krw_balance55}  |  매수가능여부 - {op_mode55} - 매수불가-매도가능")
                                    print("")

                                else:
                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode55 = 1

                                    print("매수금액이 ￦10,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode55} - 매수불가-매도가능")
                                    print("")
                            else:   # 보유금액이 평균가와의 차이보다 적을때 매수
                                if krw55 >= 10000:    # 보유금액이 최소주문가능금액인 ￦10,000원보다 높을때 매수시도
                                    # 매수할 코인명 - krw_coin55, 매수할 코인금액 - krw55
                                    upbit.buy_market_order(krw_coin55, krw55 * 0.9)

                                    op_mode55 = 1

                                    print("보유금액보다 매수금액보다 적어서 매수금지")
                                    print(f"매수한금액 = ￦{krw55}  |  매수한수량 = {buy_krw_balance55}  |  매수가능여부 - {op_mode55} - 매수불가-매도가능")
                                    print("")
                                else:
                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode55 = 1

                                    print("보유금액이 ￦10,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode55} - 매수불가-매도가능")
                                    print("")

                        else:
                            # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                            op_mode55 = 1

                            print("보유금액이 평균금액보다 높아서 매수불가")
                            print(f"매수가능여부 - {op_mode55} - 매수불가-매도가능")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################


            ###############################
            # 코인56

            # 코인별 금액 비율조정
            buy_bpAve56 = bpAve * bpPer56

            # MACD 조건문
            if macd56 >= 0:     # macd가 0보다 크거나 같을때는 매수
                # 매수가능금액 불러오기
                krw56 = upbit.get_balance("KRW")

                if coinMode56 == 1 or coinMode56 == 2:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = >>>매수만가능<<< , 3 = 매도만가능
                    if op_mode56 == 2 or op_mode56 == 3:   # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                        print("")
                        print(f"[ 56. 매수시간 : {now}  |  코인명 : {coin56}  |  현재가 = ￦{price56}  |  MACD = ￦{macd56}  |  보유수량 = {krw_balance56}  |  평가금액 = ￦{bp56}  ||  매수평균금액 = ￦{buy_bpAve56} ]")

                        if bp56 < buy_bpAve56: # 코인보유금액이 평균가보다 낮을때 매수시도
                            # 매수할 코인 금액 = 평균가 - 코인보유금액
                            buy_krw_price56 = buy_bpAve56 - bp56
                            # 매수할 코인 갯수 = 매수할 코인 금액 - 현재가
                            buy_krw_balance56 = buy_krw_price56 / price56

                            if krw56 >= buy_krw_price56: # 매수가능금액이 매수할금액보다 클때 매수시도
                                if buy_krw_price56 >= 10000:    # 매수가능금액이 최소주문가능금액인 ￦10,000원보다 높을때 매수시도

                                    # 매수할 코인명 - krw_coin56, 매수할 코인금액 - buy_krw_price56
                                    upbit.buy_market_order(krw_coin56, buy_krw_price56 * 0.9)

                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode56 = 1

                                    print("평균 이하 금액 매수")
                                    print(f"매수한금액 = ￦{buy_krw_price56}  |  매수한수량 = {buy_krw_balance56}  |  매수가능여부 - {op_mode56} - 매수불가-매도가능")
                                    print("")

                                else:
                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode56 = 1

                                    print("매수금액이 ￦10,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode56} - 매수불가-매도가능")
                                    print("")
                            else:   # 보유금액이 평균가와의 차이보다 적을때 매수
                                if krw56 >= 10000:    # 보유금액이 최소주문가능금액인 ￦10,000원보다 높을때 매수시도
                                    # 매수할 코인명 - krw_coin56, 매수할 코인금액 - krw56
                                    upbit.buy_market_order(krw_coin56, krw56 * 0.9)

                                    op_mode56 = 1

                                    print("보유금액보다 매수금액보다 적어서 매수금지")
                                    print(f"매수한금액 = ￦{krw56}  |  매수한수량 = {buy_krw_balance56}  |  매수가능여부 - {op_mode56} - 매수불가-매도가능")
                                    print("")
                                else:
                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode56 = 1

                                    print("보유금액이 ￦10,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode56} - 매수불가-매도가능")
                                    print("")

                        else:
                            # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                            op_mode56 = 1

                            print("보유금액이 평균금액보다 높아서 매수불가")
                            print(f"매수가능여부 - {op_mode56} - 매수불가-매도가능")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################


            ###############################
            # 코인57

            # 코인별 금액 비율조정
            buy_bpAve57 = bpAve * bpPer57

            # MACD 조건문
            if macd57 >= 0:     # macd가 0보다 크거나 같을때는 매수
                # 매수가능금액 불러오기
                krw57 = upbit.get_balance("KRW")

                if coinMode57 == 1 or coinMode57 == 2:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = >>>매수만가능<<< , 3 = 매도만가능
                    if op_mode57 == 2 or op_mode57 == 3:   # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                        print("")
                        print(f"[ 57. 매수시간 : {now}  |  코인명 : {coin57}  |  현재가 = ￦{price57}  |  MACD = ￦{macd57}  |  보유수량 = {krw_balance57}  |  평가금액 = ￦{bp57}  ||  매수평균금액 = ￦{buy_bpAve57} ]")

                        if bp57 < buy_bpAve57: # 코인보유금액이 평균가보다 낮을때 매수시도
                            # 매수할 코인 금액 = 평균가 - 코인보유금액
                            buy_krw_price57 = buy_bpAve57 - bp57
                            # 매수할 코인 갯수 = 매수할 코인 금액 - 현재가
                            buy_krw_balance57 = buy_krw_price57 / price57

                            if krw57 >= buy_krw_price57: # 매수가능금액이 매수할금액보다 클때 매수시도
                                if buy_krw_price57 >= 10000:    # 매수가능금액이 최소주문가능금액인 ￦10,000원보다 높을때 매수시도

                                    # 매수할 코인명 - krw_coin57, 매수할 코인금액 - buy_krw_price57
                                    upbit.buy_market_order(krw_coin57, buy_krw_price57 * 0.9)

                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode57 = 1

                                    print("평균 이하 금액 매수")
                                    print(f"매수한금액 = ￦{buy_krw_price57}  |  매수한수량 = {buy_krw_balance57}  |  매수가능여부 - {op_mode57} - 매수불가-매도가능")
                                    print("")

                                else:
                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode57 = 1

                                    print("매수금액이 ￦10,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode57} - 매수불가-매도가능")
                                    print("")
                            else:   # 보유금액이 평균가와의 차이보다 적을때 매수
                                if krw57 >= 10000:    # 보유금액이 최소주문가능금액인 ￦10,000원보다 높을때 매수시도
                                    # 매수할 코인명 - krw_coin57, 매수할 코인금액 - krw57
                                    upbit.buy_market_order(krw_coin57, krw57 * 0.9)

                                    op_mode57 = 1

                                    print("보유금액보다 매수금액보다 적어서 매수금지")
                                    print(f"매수한금액 = ￦{krw57}  |  매수한수량 = {buy_krw_balance57}  |  매수가능여부 - {op_mode57} - 매수불가-매도가능")
                                    print("")
                                else:
                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode57 = 1

                                    print("보유금액이 ￦10,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode57} - 매수불가-매도가능")
                                    print("")

                        else:
                            # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                            op_mode57 = 1

                            print("보유금액이 평균금액보다 높아서 매수불가")
                            print(f"매수가능여부 - {op_mode57} - 매수불가-매도가능")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################


            ###############################
            # 코인58

            # 코인별 금액 비율조정
            buy_bpAve58 = bpAve * bpPer58

            # MACD 조건문
            if macd58 >= 0:     # macd가 0보다 크거나 같을때는 매수
                # 매수가능금액 불러오기
                krw58 = upbit.get_balance("KRW")

                if coinMode58 == 1 or coinMode58 == 2:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = >>>매수만가능<<< , 3 = 매도만가능
                    if op_mode58 == 2 or op_mode58 == 3:   # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                        print("")
                        print(f"[ 58. 매수시간 : {now}  |  코인명 : {coin58}  |  현재가 = ￦{price58}  |  MACD = ￦{macd58}  |  보유수량 = {krw_balance58}  |  평가금액 = ￦{bp58}  ||  매수평균금액 = ￦{buy_bpAve58} ]")

                        if bp58 < buy_bpAve58: # 코인보유금액이 평균가보다 낮을때 매수시도
                            # 매수할 코인 금액 = 평균가 - 코인보유금액
                            buy_krw_price58 = buy_bpAve58 - bp58
                            # 매수할 코인 갯수 = 매수할 코인 금액 - 현재가
                            buy_krw_balance58 = buy_krw_price58 / price58

                            if krw58 >= buy_krw_price58: # 매수가능금액이 매수할금액보다 클때 매수시도
                                if buy_krw_price58 >= 10000:    # 매수가능금액이 최소주문가능금액인 ￦10,000원보다 높을때 매수시도

                                    # 매수할 코인명 - krw_coin58, 매수할 코인금액 - buy_krw_price58
                                    upbit.buy_market_order(krw_coin58, buy_krw_price58 * 0.9)

                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode58 = 1

                                    print("평균 이하 금액 매수")
                                    print(f"매수한금액 = ￦{buy_krw_price58}  |  매수한수량 = {buy_krw_balance58}  |  매수가능여부 - {op_mode58} - 매수불가-매도가능")
                                    print("")

                                else:
                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode58 = 1

                                    print("매수금액이 ￦10,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode58} - 매수불가-매도가능")
                                    print("")
                            else:   # 보유금액이 평균가와의 차이보다 적을때 매수
                                if krw58 >= 10000:    # 보유금액이 최소주문가능금액인 ￦10,000원보다 높을때 매수시도
                                    # 매수할 코인명 - krw_coin58, 매수할 코인금액 - krw58
                                    upbit.buy_market_order(krw_coin58, krw58 * 0.9)

                                    op_mode58 = 1

                                    print("보유금액보다 매수금액보다 적어서 매수금지")
                                    print(f"매수한금액 = ￦{krw58}  |  매수한수량 = {buy_krw_balance58}  |  매수가능여부 - {op_mode58} - 매수불가-매도가능")
                                    print("")
                                else:
                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode58 = 1

                                    print("보유금액이 ￦10,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode58} - 매수불가-매도가능")
                                    print("")

                        else:
                            # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                            op_mode58 = 1

                            print("보유금액이 평균금액보다 높아서 매수불가")
                            print(f"매수가능여부 - {op_mode58} - 매수불가-매도가능")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################


            ###############################
            # 코인59

            # 코인별 금액 비율조정
            buy_bpAve59 = bpAve * bpPer59

            # MACD 조건문
            if macd59 >= 0:     # macd가 0보다 크거나 같을때는 매수
                # 매수가능금액 불러오기
                krw59 = upbit.get_balance("KRW")

                if coinMode59 == 1 or coinMode59 == 2:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = >>>매수만가능<<< , 3 = 매도만가능
                    if op_mode59 == 2 or op_mode59 == 3:   # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                        print("")
                        print(f"[ 59. 매수시간 : {now}  |  코인명 : {coin59}  |  현재가 = ￦{price59}  |  MACD = ￦{macd59}  |  보유수량 = {krw_balance59}  |  평가금액 = ￦{bp59}  ||  매수평균금액 = ￦{buy_bpAve59} ]")

                        if bp59 < buy_bpAve59: # 코인보유금액이 평균가보다 낮을때 매수시도
                            # 매수할 코인 금액 = 평균가 - 코인보유금액
                            buy_krw_price59 = buy_bpAve59 - bp59
                            # 매수할 코인 갯수 = 매수할 코인 금액 - 현재가
                            buy_krw_balance59 = buy_krw_price59 / price59

                            if krw59 >= buy_krw_price59: # 매수가능금액이 매수할금액보다 클때 매수시도
                                if buy_krw_price59 >= 10000:    # 매수가능금액이 최소주문가능금액인 ￦10,000원보다 높을때 매수시도

                                    # 매수할 코인명 - krw_coin59, 매수할 코인금액 - buy_krw_price59
                                    upbit.buy_market_order(krw_coin59, buy_krw_price59 * 0.9)

                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode59 = 1

                                    print("평균 이하 금액 매수")
                                    print(f"매수한금액 = ￦{buy_krw_price59}  |  매수한수량 = {buy_krw_balance59}  |  매수가능여부 - {op_mode59} - 매수불가-매도가능")
                                    print("")

                                else:
                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode59 = 1

                                    print("매수금액이 ￦10,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode59} - 매수불가-매도가능")
                                    print("")
                            else:   # 보유금액이 평균가와의 차이보다 적을때 매수
                                if krw59 >= 10000:    # 보유금액이 최소주문가능금액인 ￦10,000원보다 높을때 매수시도
                                    # 매수할 코인명 - krw_coin59, 매수할 코인금액 - krw59
                                    upbit.buy_market_order(krw_coin59, krw59 * 0.9)

                                    op_mode59 = 1

                                    print("보유금액보다 매수금액보다 적어서 매수금지")
                                    print(f"매수한금액 = ￦{krw59}  |  매수한수량 = {buy_krw_balance59}  |  매수가능여부 - {op_mode59} - 매수불가-매도가능")
                                    print("")
                                else:
                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode59 = 1

                                    print("보유금액이 ￦10,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode59} - 매수불가-매도가능")
                                    print("")

                        else:
                            # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                            op_mode59 = 1

                            print("보유금액이 평균금액보다 높아서 매수불가")
                            print(f"매수가능여부 - {op_mode59} - 매수불가-매도가능")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################


            ###############################
            # 코인60

            # 코인별 금액 비율조정
            buy_bpAve60 = bpAve * bpPer60

            # MACD 조건문
            if macd60 >= 0:     # macd가 0보다 크거나 같을때는 매수
                # 매수가능금액 불러오기
                krw60 = upbit.get_balance("KRW")

                if coinMode60 == 1 or coinMode60 == 2:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = >>>매수만가능<<< , 3 = 매도만가능
                    if op_mode60 == 2 or op_mode60 == 3:   # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                        print("")
                        print(f"[ 60. 매수시간 : {now}  |  코인명 : {coin60}  |  현재가 = ￦{price60}  |  MACD = ￦{macd60}  |  보유수량 = {krw_balance60}  |  평가금액 = ￦{bp60}  ||  매수평균금액 = ￦{buy_bpAve60} ]")

                        if bp60 < buy_bpAve60: # 코인보유금액이 평균가보다 낮을때 매수시도
                            # 매수할 코인 금액 = 평균가 - 코인보유금액
                            buy_krw_price60 = buy_bpAve60 - bp60
                            # 매수할 코인 갯수 = 매수할 코인 금액 - 현재가
                            buy_krw_balance60 = buy_krw_price60 / price60

                            if krw60 >= buy_krw_price60: # 매수가능금액이 매수할금액보다 클때 매수시도
                                if buy_krw_price60 >= 10000:    # 매수가능금액이 최소주문가능금액인 ￦10,000원보다 높을때 매수시도

                                    # 매수할 코인명 - krw_coin60, 매수할 코인금액 - buy_krw_price60
                                    upbit.buy_market_order(krw_coin60, buy_krw_price60 * 0.9)

                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode60 = 1

                                    print("평균 이하 금액 매수")
                                    print(f"매수한금액 = ￦{buy_krw_price60}  |  매수한수량 = {buy_krw_balance60}  |  매수가능여부 - {op_mode60} - 매수불가-매도가능")
                                    print("")

                                else:
                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode60 = 1

                                    print("매수금액이 ￦10,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode60} - 매수불가-매도가능")
                                    print("")
                            else:   # 보유금액이 평균가와의 차이보다 적을때 매수
                                if krw60 >= 10000:    # 보유금액이 최소주문가능금액인 ￦10,000원보다 높을때 매수시도
                                    # 매수할 코인명 - krw_coin60, 매수할 코인금액 - krw60
                                    upbit.buy_market_order(krw_coin60, krw60 * 0.9)

                                    op_mode60 = 1

                                    print("보유금액보다 매수금액보다 적어서 매수금지")
                                    print(f"매수한금액 = ￦{krw60}  |  매수한수량 = {buy_krw_balance60}  |  매수가능여부 - {op_mode60} - 매수불가-매도가능")
                                    print("")
                                else:
                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode60 = 1

                                    print("보유금액이 ￦10,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode60} - 매수불가-매도가능")
                                    print("")

                        else:
                            # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                            op_mode60 = 1

                            print("보유금액이 평균금액보다 높아서 매수불가")
                            print(f"매수가능여부 - {op_mode60} - 매수불가-매도가능")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################





            ######################################################################################################################################################
            ######################################################################################################################################################
            ######################################################################################################################################################
            ######################################################################################################################################################
            ######################################################################################################################################################




            ###############################
            # 코인61

            # 코인별 금액 비율조정
            buy_bpAve61 = bpAve * bpPer61

            # MACD 조건문
            if macd61 >= 0:     # macd가 0보다 크거나 같을때는 매수
                # 매수가능금액 불러오기
                krw61 = upbit.get_balance("KRW")

                if coinMode61 == 1 or coinMode61 == 2:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = >>>매수만가능<<< , 3 = 매도만가능
                    if op_mode61 == 2 or op_mode61 == 3:   # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                        print("")
                        print(f"[ 61. 매수시간 : {now}  |  코인명 : {coin61}  |  현재가 = ￦{price61}  |  MACD = ￦{macd61}  |  보유수량 = {krw_balance61}  |  평가금액 = ￦{bp61}  ||  매수평균금액 = ￦{buy_bpAve61} ]")

                        if bp61 < buy_bpAve61: # 코인보유금액이 평균가보다 낮을때 매수시도
                            # 매수할 코인 금액 = 평균가 - 코인보유금액
                            buy_krw_price61 = buy_bpAve61 - bp61
                            # 매수할 코인 갯수 = 매수할 코인 금액 - 현재가
                            buy_krw_balance61 = buy_krw_price61 / price61

                            if krw61 >= buy_krw_price61: # 매수가능금액이 매수할금액보다 클때 매수시도
                                if buy_krw_price61 >= 10000:    # 매수가능금액이 최소주문가능금액인 ￦10,000원보다 높을때 매수시도

                                    # 매수할 코인명 - krw_coin61, 매수할 코인금액 - buy_krw_price61
                                    upbit.buy_market_order(krw_coin61, buy_krw_price61 * 0.9)

                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode61 = 1

                                    print("평균 이하 금액 매수")
                                    print(f"매수한금액 = ￦{buy_krw_price61}  |  매수한수량 = {buy_krw_balance61}  |  매수가능여부 - {op_mode61} - 매수불가-매도가능")
                                    print("")

                                else:
                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode61 = 1

                                    print("매수금액이 ￦10,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode61} - 매수불가-매도가능")
                                    print("")
                            else:   # 보유금액이 평균가와의 차이보다 적을때 매수
                                if krw61 >= 10000:    # 보유금액이 최소주문가능금액인 ￦10,000원보다 높을때 매수시도
                                    # 매수할 코인명 - krw_coin61, 매수할 코인금액 - krw61
                                    upbit.buy_market_order(krw_coin61, krw61 * 0.9)

                                    op_mode61 = 1

                                    print("보유금액보다 매수금액보다 적어서 매수금지")
                                    print(f"매수한금액 = ￦{krw61}  |  매수한수량 = {buy_krw_balance61}  |  매수가능여부 - {op_mode61} - 매수불가-매도가능")
                                    print("")
                                else:
                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode61 = 1

                                    print("보유금액이 ￦10,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode61} - 매수불가-매도가능")
                                    print("")

                        else:
                            # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                            op_mode61 = 1

                            print("보유금액이 평균금액보다 높아서 매수불가")
                            print(f"매수가능여부 - {op_mode61} - 매수불가-매도가능")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################


            ###############################
            # 코인62

            # 코인별 금액 비율조정
            buy_bpAve62 = bpAve * bpPer62

            # MACD 조건문
            if macd62 >= 0:     # macd가 0보다 크거나 같을때는 매수
                # 매수가능금액 불러오기
                krw62 = upbit.get_balance("KRW")

                if coinMode62 == 1 or coinMode62 == 2:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = >>>매수만가능<<< , 3 = 매도만가능
                    if op_mode62 == 2 or op_mode62 == 3:   # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                        print("")
                        print(f"[ 62. 매수시간 : {now}  |  코인명 : {coin62}  |  현재가 = ￦{price62}  |  MACD = ￦{macd62}  |  보유수량 = {krw_balance62}  |  평가금액 = ￦{bp62}  ||  매수평균금액 = ￦{buy_bpAve62} ]")

                        if bp62 < buy_bpAve62: # 코인보유금액이 평균가보다 낮을때 매수시도
                            # 매수할 코인 금액 = 평균가 - 코인보유금액
                            buy_krw_price62 = buy_bpAve62 - bp62
                            # 매수할 코인 갯수 = 매수할 코인 금액 - 현재가
                            buy_krw_balance62 = buy_krw_price62 / price62

                            if krw62 >= buy_krw_price62: # 매수가능금액이 매수할금액보다 클때 매수시도
                                if buy_krw_price62 >= 10000:    # 매수가능금액이 최소주문가능금액인 ￦10,000원보다 높을때 매수시도

                                    # 매수할 코인명 - krw_coin62, 매수할 코인금액 - buy_krw_price62
                                    upbit.buy_market_order(krw_coin62, buy_krw_price62 * 0.9)

                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode62 = 1

                                    print("평균 이하 금액 매수")
                                    print(f"매수한금액 = ￦{buy_krw_price62}  |  매수한수량 = {buy_krw_balance62}  |  매수가능여부 - {op_mode62} - 매수불가-매도가능")
                                    print("")

                                else:
                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode62 = 1

                                    print("매수금액이 ￦10,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode62} - 매수불가-매도가능")
                                    print("")
                            else:   # 보유금액이 평균가와의 차이보다 적을때 매수
                                if krw62 >= 10000:    # 보유금액이 최소주문가능금액인 ￦10,000원보다 높을때 매수시도
                                    # 매수할 코인명 - krw_coin62, 매수할 코인금액 - krw62
                                    upbit.buy_market_order(krw_coin62, krw62 * 0.9)

                                    op_mode62 = 1

                                    print("보유금액보다 매수금액보다 적어서 매수금지")
                                    print(f"매수한금액 = ￦{krw62}  |  매수한수량 = {buy_krw_balance62}  |  매수가능여부 - {op_mode62} - 매수불가-매도가능")
                                    print("")
                                else:
                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode62 = 1

                                    print("보유금액이 ￦10,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode62} - 매수불가-매도가능")
                                    print("")

                        else:
                            # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                            op_mode62 = 1

                            print("보유금액이 평균금액보다 높아서 매수불가")
                            print(f"매수가능여부 - {op_mode62} - 매수불가-매도가능")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################


            ###############################
            # 코인63

            # 코인별 금액 비율조정
            buy_bpAve63 = bpAve * bpPer63

            # MACD 조건문
            if macd63 >= 0:     # macd가 0보다 크거나 같을때는 매수
                # 매수가능금액 불러오기
                krw63 = upbit.get_balance("KRW")

                if coinMode63 == 1 or coinMode63 == 2:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = >>>매수만가능<<< , 3 = 매도만가능
                    if op_mode63 == 2 or op_mode63 == 3:   # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                        print("")
                        print(f"[ 63. 매수시간 : {now}  |  코인명 : {coin63}  |  현재가 = ￦{price63}  |  MACD = ￦{macd63}  |  보유수량 = {krw_balance63}  |  평가금액 = ￦{bp63}  ||  매수평균금액 = ￦{buy_bpAve63} ]")

                        if bp63 < buy_bpAve63: # 코인보유금액이 평균가보다 낮을때 매수시도
                            # 매수할 코인 금액 = 평균가 - 코인보유금액
                            buy_krw_price63 = buy_bpAve63 - bp63
                            # 매수할 코인 갯수 = 매수할 코인 금액 - 현재가
                            buy_krw_balance63 = buy_krw_price63 / price63

                            if krw63 >= buy_krw_price63: # 매수가능금액이 매수할금액보다 클때 매수시도
                                if buy_krw_price63 >= 10000:    # 매수가능금액이 최소주문가능금액인 ￦10,000원보다 높을때 매수시도

                                    # 매수할 코인명 - krw_coin63, 매수할 코인금액 - buy_krw_price63
                                    upbit.buy_market_order(krw_coin63, buy_krw_price63 * 0.9)

                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode63 = 1

                                    print("평균 이하 금액 매수")
                                    print(f"매수한금액 = ￦{buy_krw_price63}  |  매수한수량 = {buy_krw_balance63}  |  매수가능여부 - {op_mode63} - 매수불가-매도가능")
                                    print("")

                                else:
                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode63 = 1

                                    print("매수금액이 ￦10,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode63} - 매수불가-매도가능")
                                    print("")
                            else:   # 보유금액이 평균가와의 차이보다 적을때 매수
                                if krw63 >= 10000:    # 보유금액이 최소주문가능금액인 ￦10,000원보다 높을때 매수시도
                                    # 매수할 코인명 - krw_coin63, 매수할 코인금액 - krw63
                                    upbit.buy_market_order(krw_coin63, krw63 * 0.9)

                                    op_mode63 = 1

                                    print("보유금액보다 매수금액보다 적어서 매수금지")
                                    print(f"매수한금액 = ￦{krw63}  |  매수한수량 = {buy_krw_balance63}  |  매수가능여부 - {op_mode63} - 매수불가-매도가능")
                                    print("")
                                else:
                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode63 = 1

                                    print("보유금액이 ￦10,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode63} - 매수불가-매도가능")
                                    print("")

                        else:
                            # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                            op_mode63 = 1

                            print("보유금액이 평균금액보다 높아서 매수불가")
                            print(f"매수가능여부 - {op_mode63} - 매수불가-매도가능")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################


            ###############################
            # 코인64

            # 코인별 금액 비율조정
            buy_bpAve64 = bpAve * bpPer64

            # MACD 조건문
            if macd64 >= 0:     # macd가 0보다 크거나 같을때는 매수
                # 매수가능금액 불러오기
                krw64 = upbit.get_balance("KRW")

                if coinMode64 == 1 or coinMode64 == 2:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = >>>매수만가능<<< , 3 = 매도만가능
                    if op_mode64 == 2 or op_mode64 == 3:   # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                        print("")
                        print(f"[ 64. 매수시간 : {now}  |  코인명 : {coin64}  |  현재가 = ￦{price64}  |  MACD = ￦{macd64}  |  보유수량 = {krw_balance64}  |  평가금액 = ￦{bp64}  ||  매수평균금액 = ￦{buy_bpAve64} ]")

                        if bp64 < buy_bpAve64: # 코인보유금액이 평균가보다 낮을때 매수시도
                            # 매수할 코인 금액 = 평균가 - 코인보유금액
                            buy_krw_price64 = buy_bpAve64 - bp64
                            # 매수할 코인 갯수 = 매수할 코인 금액 - 현재가
                            buy_krw_balance64 = buy_krw_price64 / price64

                            if krw64 >= buy_krw_price64: # 매수가능금액이 매수할금액보다 클때 매수시도
                                if buy_krw_price64 >= 10000:    # 매수가능금액이 최소주문가능금액인 ￦10,000원보다 높을때 매수시도

                                    # 매수할 코인명 - krw_coin64, 매수할 코인금액 - buy_krw_price64
                                    upbit.buy_market_order(krw_coin64, buy_krw_price64 * 0.9)

                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode64 = 1

                                    print("평균 이하 금액 매수")
                                    print(f"매수한금액 = ￦{buy_krw_price64}  |  매수한수량 = {buy_krw_balance64}  |  매수가능여부 - {op_mode64} - 매수불가-매도가능")
                                    print("")

                                else:
                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode64 = 1

                                    print("매수금액이 ￦10,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode64} - 매수불가-매도가능")
                                    print("")
                            else:   # 보유금액이 평균가와의 차이보다 적을때 매수
                                if krw64 >= 10000:    # 보유금액이 최소주문가능금액인 ￦10,000원보다 높을때 매수시도
                                    # 매수할 코인명 - krw_coin64, 매수할 코인금액 - krw64
                                    upbit.buy_market_order(krw_coin64, krw64 * 0.9)

                                    op_mode64 = 1

                                    print("보유금액보다 매수금액보다 적어서 매수금지")
                                    print(f"매수한금액 = ￦{krw64}  |  매수한수량 = {buy_krw_balance64}  |  매수가능여부 - {op_mode64} - 매수불가-매도가능")
                                    print("")
                                else:
                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode64 = 1

                                    print("보유금액이 ￦10,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode64} - 매수불가-매도가능")
                                    print("")

                        else:
                            # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                            op_mode64 = 1

                            print("보유금액이 평균금액보다 높아서 매수불가")
                            print(f"매수가능여부 - {op_mode64} - 매수불가-매도가능")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################


            ###############################
            # 코인65

            # 코인별 금액 비율조정
            buy_bpAve65 = bpAve * bpPer65

            # MACD 조건문
            if macd65 >= 0:     # macd가 0보다 크거나 같을때는 매수
                # 매수가능금액 불러오기
                krw65 = upbit.get_balance("KRW")

                if coinMode65 == 1 or coinMode65 == 2:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = >>>매수만가능<<< , 3 = 매도만가능
                    if op_mode65 == 2 or op_mode65 == 3:   # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                        print("")
                        print(f"[ 65. 매수시간 : {now}  |  코인명 : {coin65}  |  현재가 = ￦{price65}  |  MACD = ￦{macd65}  |  보유수량 = {krw_balance65}  |  평가금액 = ￦{bp65}  ||  매수평균금액 = ￦{buy_bpAve65} ]")

                        if bp65 < buy_bpAve65: # 코인보유금액이 평균가보다 낮을때 매수시도
                            # 매수할 코인 금액 = 평균가 - 코인보유금액
                            buy_krw_price65 = buy_bpAve65 - bp65
                            # 매수할 코인 갯수 = 매수할 코인 금액 - 현재가
                            buy_krw_balance65 = buy_krw_price65 / price65

                            if krw65 >= buy_krw_price65: # 매수가능금액이 매수할금액보다 클때 매수시도
                                if buy_krw_price65 >= 10000:    # 매수가능금액이 최소주문가능금액인 ￦10,000원보다 높을때 매수시도

                                    # 매수할 코인명 - krw_coin65, 매수할 코인금액 - buy_krw_price65
                                    upbit.buy_market_order(krw_coin65, buy_krw_price65 * 0.9)

                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode65 = 1

                                    print("평균 이하 금액 매수")
                                    print(f"매수한금액 = ￦{buy_krw_price65}  |  매수한수량 = {buy_krw_balance65}  |  매수가능여부 - {op_mode65} - 매수불가-매도가능")
                                    print("")

                                else:
                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode65 = 1

                                    print("매수금액이 ￦10,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode65} - 매수불가-매도가능")
                                    print("")
                            else:   # 보유금액이 평균가와의 차이보다 적을때 매수
                                if krw65 >= 10000:    # 보유금액이 최소주문가능금액인 ￦10,000원보다 높을때 매수시도
                                    # 매수할 코인명 - krw_coin65, 매수할 코인금액 - krw65
                                    upbit.buy_market_order(krw_coin65, krw65 * 0.9)

                                    op_mode65 = 1

                                    print("보유금액보다 매수금액보다 적어서 매수금지")
                                    print(f"매수한금액 = ￦{krw65}  |  매수한수량 = {buy_krw_balance65}  |  매수가능여부 - {op_mode65} - 매수불가-매도가능")
                                    print("")
                                else:
                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode65 = 1

                                    print("보유금액이 ￦10,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode65} - 매수불가-매도가능")
                                    print("")

                        else:
                            # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                            op_mode65 = 1

                            print("보유금액이 평균금액보다 높아서 매수불가")
                            print(f"매수가능여부 - {op_mode65} - 매수불가-매도가능")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################


            ###############################
            # 코인66

            # 코인별 금액 비율조정
            buy_bpAve66 = bpAve * bpPer66

            # MACD 조건문
            if macd66 >= 0:     # macd가 0보다 크거나 같을때는 매수
                # 매수가능금액 불러오기
                krw66 = upbit.get_balance("KRW")

                if coinMode66 == 1 or coinMode66 == 2:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = >>>매수만가능<<< , 3 = 매도만가능
                    if op_mode66 == 2 or op_mode66 == 3:   # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                        print("")
                        print(f"[ 66. 매수시간 : {now}  |  코인명 : {coin66}  |  현재가 = ￦{price66}  |  MACD = ￦{macd66}  |  보유수량 = {krw_balance66}  |  평가금액 = ￦{bp66}  ||  매수평균금액 = ￦{buy_bpAve66} ]")

                        if bp66 < buy_bpAve66: # 코인보유금액이 평균가보다 낮을때 매수시도
                            # 매수할 코인 금액 = 평균가 - 코인보유금액
                            buy_krw_price66 = buy_bpAve66 - bp66
                            # 매수할 코인 갯수 = 매수할 코인 금액 - 현재가
                            buy_krw_balance66 = buy_krw_price66 / price66

                            if krw66 >= buy_krw_price66: # 매수가능금액이 매수할금액보다 클때 매수시도
                                if buy_krw_price66 >= 10000:    # 매수가능금액이 최소주문가능금액인 ￦10,000원보다 높을때 매수시도

                                    # 매수할 코인명 - krw_coin66, 매수할 코인금액 - buy_krw_price66
                                    upbit.buy_market_order(krw_coin66, buy_krw_price66 * 0.9)

                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode66 = 1

                                    print("평균 이하 금액 매수")
                                    print(f"매수한금액 = ￦{buy_krw_price66}  |  매수한수량 = {buy_krw_balance66}  |  매수가능여부 - {op_mode66} - 매수불가-매도가능")
                                    print("")

                                else:
                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode66 = 1

                                    print("매수금액이 ￦10,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode66} - 매수불가-매도가능")
                                    print("")
                            else:   # 보유금액이 평균가와의 차이보다 적을때 매수
                                if krw66 >= 10000:    # 보유금액이 최소주문가능금액인 ￦10,000원보다 높을때 매수시도
                                    # 매수할 코인명 - krw_coin66, 매수할 코인금액 - krw66
                                    upbit.buy_market_order(krw_coin66, krw66 * 0.9)

                                    op_mode66 = 1

                                    print("보유금액보다 매수금액보다 적어서 매수금지")
                                    print(f"매수한금액 = ￦{krw66}  |  매수한수량 = {buy_krw_balance66}  |  매수가능여부 - {op_mode66} - 매수불가-매도가능")
                                    print("")
                                else:
                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode66 = 1

                                    print("보유금액이 ￦10,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode66} - 매수불가-매도가능")
                                    print("")

                        else:
                            # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                            op_mode66 = 1

                            print("보유금액이 평균금액보다 높아서 매수불가")
                            print(f"매수가능여부 - {op_mode66} - 매수불가-매도가능")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################


            ###############################
            # 코인67

            # 코인별 금액 비율조정
            buy_bpAve67 = bpAve * bpPer67

            # MACD 조건문
            if macd67 >= 0:     # macd가 0보다 크거나 같을때는 매수
                # 매수가능금액 불러오기
                krw67 = upbit.get_balance("KRW")

                if coinMode67 == 1 or coinMode67 == 2:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = >>>매수만가능<<< , 3 = 매도만가능
                    if op_mode67 == 2 or op_mode67 == 3:   # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                        print("")
                        print(f"[ 67. 매수시간 : {now}  |  코인명 : {coin67}  |  현재가 = ￦{price67}  |  MACD = ￦{macd67}  |  보유수량 = {krw_balance67}  |  평가금액 = ￦{bp67}  ||  매수평균금액 = ￦{buy_bpAve67} ]")

                        if bp67 < buy_bpAve67: # 코인보유금액이 평균가보다 낮을때 매수시도
                            # 매수할 코인 금액 = 평균가 - 코인보유금액
                            buy_krw_price67 = buy_bpAve67 - bp67
                            # 매수할 코인 갯수 = 매수할 코인 금액 - 현재가
                            buy_krw_balance67 = buy_krw_price67 / price67

                            if krw67 >= buy_krw_price67: # 매수가능금액이 매수할금액보다 클때 매수시도
                                if buy_krw_price67 >= 10000:    # 매수가능금액이 최소주문가능금액인 ￦10,000원보다 높을때 매수시도

                                    # 매수할 코인명 - krw_coin67, 매수할 코인금액 - buy_krw_price67
                                    upbit.buy_market_order(krw_coin67, buy_krw_price67 * 0.9)

                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode67 = 1

                                    print("평균 이하 금액 매수")
                                    print(f"매수한금액 = ￦{buy_krw_price67}  |  매수한수량 = {buy_krw_balance67}  |  매수가능여부 - {op_mode67} - 매수불가-매도가능")
                                    print("")

                                else:
                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode67 = 1

                                    print("매수금액이 ￦10,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode67} - 매수불가-매도가능")
                                    print("")
                            else:   # 보유금액이 평균가와의 차이보다 적을때 매수
                                if krw67 >= 10000:    # 보유금액이 최소주문가능금액인 ￦10,000원보다 높을때 매수시도
                                    # 매수할 코인명 - krw_coin67, 매수할 코인금액 - krw67
                                    upbit.buy_market_order(krw_coin67, krw67 * 0.9)

                                    op_mode67 = 1

                                    print("보유금액보다 매수금액보다 적어서 매수금지")
                                    print(f"매수한금액 = ￦{krw67}  |  매수한수량 = {buy_krw_balance67}  |  매수가능여부 - {op_mode67} - 매수불가-매도가능")
                                    print("")
                                else:
                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode67 = 1

                                    print("보유금액이 ￦10,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode67} - 매수불가-매도가능")
                                    print("")

                        else:
                            # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                            op_mode67 = 1

                            print("보유금액이 평균금액보다 높아서 매수불가")
                            print(f"매수가능여부 - {op_mode67} - 매수불가-매도가능")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################


            ###############################
            # 코인68

            # 코인별 금액 비율조정
            buy_bpAve68 = bpAve * bpPer68

            # MACD 조건문
            if macd68 >= 0:     # macd가 0보다 크거나 같을때는 매수
                # 매수가능금액 불러오기
                krw68 = upbit.get_balance("KRW")

                if coinMode68 == 1 or coinMode68 == 2:  # 0 = 매매중지 , 1 = >>>매도매수가능<<< , 2 = >>>매수만가능<<< , 3 = 매도만가능
                    if op_mode68 == 2 or op_mode68 == 3:   # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                        print("")
                        print(f"[ 68. 매수시간 : {now}  |  코인명 : {coin68}  |  현재가 = ￦{price68}  |  MACD = ￦{macd68}  |  보유수량 = {krw_balance68}  |  평가금액 = ￦{bp68}  ||  매수평균금액 = ￦{buy_bpAve68} ]")

                        if bp68 < buy_bpAve68: # 코인보유금액이 평균가보다 낮을때 매수시도
                            # 매수할 코인 금액 = 평균가 - 코인보유금액
                            buy_krw_price68 = buy_bpAve68 - bp68
                            # 매수할 코인 갯수 = 매수할 코인 금액 - 현재가
                            buy_krw_balance68 = buy_krw_price68 / price68

                            if krw68 >= buy_krw_price68: # 매수가능금액이 매수할금액보다 클때 매수시도
                                if buy_krw_price68 >= 10000:    # 매수가능금액이 최소주문가능금액인 ￦10,000원보다 높을때 매수시도

                                    # 매수할 코인명 - krw_coin68, 매수할 코인금액 - buy_krw_price68
                                    upbit.buy_market_order(krw_coin68, buy_krw_price68 * 0.9)

                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode68 = 1

                                    print("평균 이하 금액 매수")
                                    print(f"매수한금액 = ￦{buy_krw_price68}  |  매수한수량 = {buy_krw_balance68}  |  매수가능여부 - {op_mode68} - 매수불가-매도가능")
                                    print("")

                                else:
                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode68 = 1

                                    print("매수금액이 ￦10,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode68} - 매수불가-매도가능")
                                    print("")
                            else:   # 보유금액이 평균가와의 차이보다 적을때 매수
                                if krw68 >= 10000:    # 보유금액이 최소주문가능금액인 ￦10,000원보다 높을때 매수시도
                                    # 매수할 코인명 - krw_coin68, 매수할 코인금액 - krw68
                                    upbit.buy_market_order(krw_coin68, krw68 * 0.9)

                                    op_mode68 = 1

                                    print("보유금액보다 매수금액보다 적어서 매수금지")
                                    print(f"매수한금액 = ￦{krw68}  |  매수한수량 = {buy_krw_balance68}  |  매수가능여부 - {op_mode68} - 매수불가-매도가능")
                                    print("")
                                else:
                                    # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                                    op_mode68 = 1

                                    print("보유금액이 ￦10,000 미만이여서 매수금지")
                                    print(f"매수가능여부 - {op_mode68} - 매수불가-매도가능")
                                    print("")

                        else:
                            # 코인 매수 가능유무  -  1 = 평균이상-<매수불가>-매도가능 , 2 = 평균이하-<매수가능>-매도불가 , 3 = 평균이하-<매도불가>-매수가능 , 4 = 평균이상-<매도가능>-매수불가
                            op_mode68 = 1

                            print("보유금액이 평균금액보다 높아서 매수불가")
                            print(f"매수가능여부 - {op_mode68} - 매수불가-매도가능")
                            print("")

            # 1초 딜레이.
            time.sleep(1)

            ###############################





            ######################################################################################################################################################
            ######################################################################################################################################################
            ######################################################################################################################################################
            ######################################################################################################################################################
            ######################################################################################################################################################





            # 60초 딜레이.
            time.sleep(60)