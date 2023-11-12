import ccxt
import pprint
import pandas as pd
import time
import datetime
import math




# 사용중인 API이름
bithumb_access = "4d8b9112fdc6628c3e940e721972bffe"
bithumb_secret = "9ce1d414cd38f14d9fdc81736f305fae"

# 선물 현재가 출력하기

bithumb = ccxt.bithumb( config = {
    'apiKey' : bithumb_access, 
    'secret' : bithumb_secret,
    'enableRateLimit' : True
} )

bithumb_exchange = ccxt.bithumb(config = {
    'apiKey' : bithumb_access, 
    'secret' : bithumb_secret,
    'enableRateLimit' : True
} )


# 코인명 가져오기
bithumb_coin1 = "BTC" # 비트코인

# 원화코인 변수 설정
bithumb_symbol1 = bithumb_coin1 + "/KRW"



# 매수가능금액
bithumb_lowBuyPrice = 10000
# 최소 매도가능금액
bithumb_lowSellPrice = 5000




















# def 함수
####################################
# 거래가능한 선물 보유금 BTC 갯수설정 #
#def cal_amount( bithumb_usdt_balance, bithumb_cur_price ):
#    # 거래금액 비율
#    bithumb_portion = 1
#    # 거래금액산정
#    bithumb_usdt_trade = bithumb_usdt_balance * bithumb_portion
#    # btc 거래갯수산정
#    bithumb_amount = math.floor( ( usdt_trade * 10000 ) / cur_price ) / 10000
#
#    return bithumb_amount









################################################################################################################################################################
################################################################################################################################################################
################################################################################################################################################################



# BTC/KRW 일봉조회
bithumb_btc = bithumb_exchange.fetch_ohlcv(
    symbol = bithumb_symbol1,
    timeframe ='1d', 
    since = None, 
    limit = 5
    )

bithumb_df = pd.DataFrame( data = bithumb_btc, columns = [ 'datetime', 'open', 'high', 'low', 'close', 'volume' ] )
bithumb_df['datetime'] = pd.to_datetime( bithumb_df[ 'datetime' ], unit = 'ms' )
bithumb_df.set_index( 'datetime', inplace = True )



#df = pd.DataFrame(ohlcv, columns=['datetime', 'open', 'high', 'low', 'close', 'volume'])
#pd_ts = pd.to_datetime(df['datetime'], utc=True, unit='ms')     # unix timestamp to pandas Timeestamp
#pd_ts = pd_ts.dt.tz_convert("Asia/Seoul")                       # convert timezone
#pd_ts = pd_ts.dt.tz_localize(None)
#df.set_index(pd_ts, inplace=True)
#df = df[['open', 'high', 'low', 'close', 'volume']]



print( bithumb_df )
print()


# 종가받기 10개
print( f"[ 01-1. ========== { bithumb_symbol1 } 코인 일봉 차트 받기 ========== ]" )
print()
# 0은 아무것도 아님.
bithumb_price_0_close = bithumb_df.iloc[ 0 ][ 'close' ]
#bithumb_price_0_time = bithumb_df.iloc[ 0 ][ 'datetime' ]

########################################
# -1은 금일. 시작가.
bithumb_price_1_open = bithumb_df.iloc[ -1 ][ 'open' ]
print( f"[ 01-1. 오늘 시작가 = { bithumb_price_1_open } ]" )
bithumb_price_2_close = bithumb_df.iloc[ -2 ][ 'close' ]
print( f"[ 01-1. 어제 종가 = { bithumb_price_2_close } ]" )

########################################
# -2는 어제. 고가
bithumb_price_2_high = bithumb_df.iloc[ -2 ][ 'high' ]
print( f"[ 01-1. 어제 고가 = { bithumb_price_2_high } ]" )
bithumb_price_2_low = bithumb_df.iloc[ -2 ][ 'low' ]
print( f"[ 01-1. 어제 저가 = { bithumb_price_2_low } ]" )










# 변동성돌파전략 변동폭
bithumb_price_2_length = bithumb_price_2_high - bithumb_price_2_low
bithumb_btc_buy_price1 = bithumb_price_1_open + bithumb_price_2_length
bithumb_btc_buy_price1_1 = bithumb_price_2_close + bithumb_price_2_length

print( f"[ 01-1. 어제 변동폭 = {bithumb_price_2_length } ]" )
print( f"[ 01-1. 오늘 돌파금액 = {bithumb_btc_buy_price1 } ]" )
print( f"[ 01-1. 오늘 돌파금액 = {bithumb_btc_buy_price1_1 } ]" )
print( "[ 01-1. ========== 일봉 차트 받기 ========== ]" )
print()

time.sleep(1)






################################################################################################################################################################
################################################################################################################################################################
################################################################################################################################################################

#################
# 선물 잔고 조회 #
#################

print( "01-1. ========== ========== ==========" )
print( "       현 금  잔 고  조 회" )
print( "01-1. ========== ========== ==========" )
print()


# 잔고 조회
# 빗썸_balance
bithumb_balance = bithumb_exchange.fetch_balance()
# 거래가능한 빗썸 원화 조회
bithumb_krw_balance = bithumb_balance['KRW']
print( f"[ 01-1. 현재 거래할 수 있는 총 금액은 = ￦ { bithumb_krw_balance['total'] } ]" )

# 거래가능한 빗썸 원화 90%
bithumb_buy_krw_balance = bithumb_krw_balance['total'] * 0.9
print( f"[ 01-1. 현재 매수 가능한 90% 금액은 = ￦ { bithumb_buy_krw_balance } ]" )


# 거래가능한 빗썸_BTC코인 갯수 조회
bithumb_coin_balance1 = bithumb_balance[bithumb_coin1]
print( f"[ 01-1. 현재 거래할 수 있는 빗썸 _ { bithumb_symbol1 } 코인 갯수는 = { bithumb_coin_balance1 } ]" )

bithumb_coin_balance_format1 = "{:.8f}".format( bithumb_coin_balance1['total'] )

print( f"[ 01-1. 현재 거래할 수 있는 빗썸 _ { bithumb_symbol1 } 코인 갯수는 = { bithumb_coin_balance_format1 } ]" )




# 지금시간 현재가
# 현재가 조회
# 빗썸_tickers
bithumb_tickers = bithumb_exchange.fetch_tickers()
bithumb_coin_krw1 = bithumb_tickers[bithumb_symbol1]
bithumb_coin_timestamp1 = bithumb_coin_krw1['timestamp'] / 100
bithumb_coin_close1 = bithumb_coin_krw1['close']

now = datetime.datetime.fromtimestamp( bithumb_coin_timestamp1 )
print( f"[ 01-1. 현재시간 = { now } ]" )
print( f"[ 01-1. 빗썸_BTC 현재가 = { bithumb_coin_close1 } ]")



# 코인 잔고 계산 = bithumb_coin_krw1 ( 현재가 ) * bithumb_coin_balance1 ( 보유코인갯수 )
bithumb_krw_coin_balance1 = float( bithumb_coin_close1 ) * float( bithumb_coin_balance_format1 )
print( f"[ 01-1. 현재 보유하고 있는 빗썸 _ { bithumb_symbol1 } 의 평가금액은 = ￦ { bithumb_krw_coin_balance1 } ]" )


# 보유원화 금액이 최소 매수 금액보다 높을때 매수가능
if bithumb_buy_krw_balance > bithumb_lowBuyPrice:
    # 코인 매매 가능유무  -  1 = 매수가능-매도불가 , 2 = 매수불가-매도가능
    bithumb_op_mode1 = 1

    # 매매 가능 출력
    print( f"[ 01-1. bithumb_op_mode1 = 1 매수가능 - 매도불가 ]" )
else:
    # 코인 매매 가능유무  -  1 = 매수가능-매도불가 , 2 = 매수불가-매도가능
    bithumb_op_mode1 = 2

    # 매매 가능 출력
    print( f"[ 01-1. bithumb_op_mode1 = 2 매수불가 - 매도가능 ]" )



# 2. 변동성 설정 후
bithumb_volatility_mode = 2
print( "[ 01-1. 변동성 설정 후 ]" )
print( "[ 01-1. ========== ========== ========== ]" )
print()
print( f"-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=" )





################################################################################################################################################################
################################################################################################################################################################
################################################################################################################################################################




print()
print( "----- =====  거래 시작 ===== -----" )
print()



























































################################################################################################################################################################
################################################################################################################################################################
################################################################################################################################################################



################################################################################################################################################################
################################################################################################################################################################
################################################################################################################################################################


















################################################################################################################################################################
################################################################################################################################################################
################################################################################################################################################################

















while True:
    # 현재 시간 불러오기
    now = datetime.datetime.now()


    ################################################################################################################################################################
    ################################################################################################################################################################
    ################################################################################################################################################################

    # 장 시작 전 코인 매도
    if now.hour == 23 and now.minute == 59 and 50 <= now.second <= 59:   # 23시 59분 50초~59초사이:
        # 매도 조건문
        if bithumb_volatility_mode == 2: # upbit_volatility_mode 가 1. 일괄매도 후 변동성설정 전 2. 변동성설정 후
            print( "==================================================" )
            print( "=  01-2. 업비트 일괄매도 - 시작                    =" )
            print( "--------------------------------------------------" )
        
            ###############################
            # 코인1 - 매도시작

            if bithumb_op_mode1 == 2:   # op_mode1가 2. 매도가능 - 매수불가일때
                print( "" )
                print( f"[ 01-2. 매도시간 : { now } ]" )
                print( f"[ 01-2. 코인명 : { bithumb_symbol1 } ]" )

                # 코인 현재가
                bithumb_tickers = bithumb_exchange.fetch_tickers()
                bithumb_coin_krw1 = bithumb_tickers[bithumb_symbol1]
                bithumb_coin_timestamp1 = bithumb_coin_krw1['timestamp'] / 100
                bithumb_coin_close1 = bithumb_coin_krw1['close']
                print( f"[ 01-2. 현재가 = ￦ { bithumb_coin_close1 } ]" )

                # 거래가능한 빗썸_BTC코인 갯수 조회
                bithumb_coin_balance1 = bithumb_balance[bithumb_coin1]
                bithumb_coin_balance_format1 = "{:.8f}".format( bithumb_coin_balance1['total'] )
                print( f"[ 01-2. 보유수량 = { bithumb_coin_balance_format1 } ]" )

                # 코인 잔고 계산 = bithumb_coin_krw1 ( 현재가 ) * bithumb_coin_balance1 ( 보유코인갯수 )
                bithumb_krw_coin_balance1 = float( bithumb_coin_close1 ) * float( bithumb_coin_balance_format1 )
                print( f"[ 01-2. 평가금액 = ￦ { bithumb_krw_coin_balance1 } ]" )

                # 
                # 비트코인 최소거래갯수
                bithumb_coin_sell_low_balance1 = 0.0001 * 2



                if bithumb_coin_balance_format1 > bithumb_coin_sell_low_balance1: # 거래가능 갯수가 최소가능갯수보다 높을때 매도
                #if bithumb_krw_coin_balance1 >= bithumb_lowSellPrice:    # 매도할 금액이 최소 매도가능금액인 bithumb_lowSellPrice 보다 높을때 매도
                    # 매도할 코인명 - bithumb_krw_coin1, 매도할 코인수량 - bithumb_krw_balance1
                    resp = bithumb_exchange.create_market_sell_order( symbol = bithumb_symbol1, amount = bithumb_coin_balance_format1 )



            # 코인 매수 가능유무  -  1 = 매수가능-매도불가 , 2 = 매수불가-매도가능
            bithumb_op_mode1 = 1

            # 코인1 - 매도종료
            ###############################

            print( "--------------------------------------------------" )
            print( "=  01-2. 빗썸 일괄매도 - 완료                    =" )
            print( "==================================================" )
            print()

            print()
            print()
            print( "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++" )
            print()
            print()



            # 1. 변동성 설정 전으로
            bithumb_volatility_mode = 1

        ################################################################################################################################################################
        ################################################################################################################################################################
        ################################################################################################################################################################









    else:
        # 장 시작 전 변동성돌파매매 금액 설정
        # 변동성 코드가 btc_mode = 1 -> 변동성 설정가능
        if bithumb_volatility_mode == 1 or now.hour == 00 and now.minute == 00 and 10 <= now.second <= 20:   # 00시 00분 10초~20초사이:
            ################################################################################################################################################################
            ##  돌파매매금액 설정 - 시작  ####################################################################################################################################
            ################################################################################################################################################################
            # BTC/KRW 일봉조회
            bithumb_btc = bithumb_exchange.fetch_ohlcv(
                symbol = bithumb_symbol1,
                timeframe ='1d', 
                since = None, 
                limit = 5
                )

            bithumb_df = pd.DataFrame( data = bithumb_btc, columns = [ 'datetime', 'open', 'high', 'low', 'close', 'volume' ] )
            bithumb_df['datetime'] = pd.to_datetime( bithumb_df[ 'datetime' ], unit = 'ms' )
            bithumb_df.set_index( 'datetime', inplace = True )



            #df = pd.DataFrame(ohlcv, columns=['datetime', 'open', 'high', 'low', 'close', 'volume'])
            #pd_ts = pd.to_datetime(df['datetime'], utc=True, unit='ms')     # unix timestamp to pandas Timeestamp
            #pd_ts = pd_ts.dt.tz_convert("Asia/Seoul")                       # convert timezone
            #pd_ts = pd_ts.dt.tz_localize(None)
            #df.set_index(pd_ts, inplace=True)
            #df = df[['open', 'high', 'low', 'close', 'volume']]



            print( bithumb_df )
            print()


            # 종가받기 10개
            print( f"[ 01-3. ========== { bithumb_symbol1 } 코인 일봉 차트 받기 ========== ]" )
            print()
            # 0은 아무것도 아님.
            bithumb_price_0_close = bithumb_df.iloc[ 0 ][ 'close' ]
            #bithumb_price_0_time = bithumb_df.iloc[ 0 ][ 'datetime' ]

            ########################################
            # -1은 금일. 시작가.
            bithumb_price_1_open = bithumb_df.iloc[ -1 ][ 'open' ]
            print( f"[ 01-3. 오늘 시작가 = { bithumb_price_1_open } ]" )
            bithumb_price_2_close = bithumb_df.iloc[ -2 ][ 'close' ]
            print( f"[ 01-3. 어제 종가 = { bithumb_price_2_close } ]" )

            ########################################
            # -2는 어제. 고가
            bithumb_price_2_high = bithumb_df.iloc[ -2 ][ 'high' ]
            print( f"[ 01-3. 어제 고가 = { bithumb_price_2_high } ]" )
            bithumb_price_2_low = bithumb_df.iloc[ -2 ][ 'low' ]
            print( f"[ 01-3. 어제 저가 = { bithumb_price_2_low } ]" )










            # 변동성돌파전략 변동폭
            bithumb_price_2_length = bithumb_price_2_high - bithumb_price_2_low
            bithumb_btc_buy_price1 = bithumb_price_1_open + bithumb_price_2_length
            bithumb_btc_buy_price1_1 = bithumb_price_2_close + bithumb_price_2_length

            print( f"[ 01-3. 어제 변동폭 = { bithumb_price_2_length } ]" )
            print( f"[ 01-3. 오늘 돌파금액 = { bithumb_btc_buy_price1 } ]" )
            print( f"[ 01-3. 오늘 돌파금액 = { bithumb_btc_buy_price1_1 } ]" )
            print( "[ 01-3. ========== 일봉 차트 받기 ========== ]" )
            print()

            time.sleep(1)





            #################################################################################################
            # bithumb__volatility_mode 중간새로시작 = 1, 변동성금액설정 후 = 2
            bithumb__volatility_mode = 2
            # 변동성금액 설정완료
            print( f"[ 01-3. 업비트 변동성모드 변경 = { bithumb_volatility_mode } = 변동성금액설정완료 ]" )

            # 잔고 조회
            # 빗썸_balance
            bithumb_balance = bithumb_exchange.fetch_balance()
            # 거래가능한 빗썸 원화 조회
            bithumb_krw_balance = bithumb_balance['KRW']
            print( f"[ 01-3. 현재 거래할 수 있는 총 금액은 = ￦ { bithumb_krw_balance['total'] } ]" )

            # 거래가능한 빗썸 원화 90%
            bithumb_buy_krw_balance = bithumb_krw_balance['total'] * 0.9
            print( f"[ 01-3. 현재 매수 가능한 90% 금액은 = ￦ { bithumb_buy_krw_balance } ]" )

            print( "--------------------------------------------------" )
            print( "=  01-3. 빗썸 변동성돌파 금액계산 - 완료          =" )
            print( "==================================================" )
            print()

            print()
            print()
            print( "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++" )
            print()
            print()
            #################################################################################################






            ################################################################################################################################################################
            ################################################################################################################################################################
            ################################################################################################################################################################

            

        else:
            ################################################################################################################################################################
            ##  돌파매매조건 매수  ##########################################################################################################################################
            ################################################################################################################################################################


            if bithumb_volatility_mode == 2:  # upbit_volatility_mode가 1. 일괄매도 후 변동성설정 전 2. 변동성설정 후
                # 1초 딜레이.
                time.sleep(1)
                # 코인 현재가 조회
                bithumb_tickers = bithumb_exchange.fetch_tickers()
                bithumb_coin_krw1 = bithumb_tickers[bithumb_symbol1]
                bithumb_coin_timestamp1 = bithumb_coin_krw1['timestamp'] / 100
                bithumb_coin_close1 = bithumb_coin_krw1['close']


                # bithumb_coin_close1 현재가
                # bithumb_btc_buy_price1_1 돌파금액
                if bithumb_coin_close1 > bithumb_btc_buy_price1_1:    # 코인현재가가 돌파매매가격 bithumb_btc_buy_price1_1 보다 높을 때 매수
                        print( "==================================================" )
                        print( "=  01-4. 빗섬 매수시도 - 시작                    =" )
                        print( "--------------------------------------------------" )


                        print( f"[ 01-4. 매수시간 : { now } ]" )
                        print( f"[ 01-4. 코인명 : { bithumb_symbol1 } ]" )
                        print( f"[ 01-4. 코인현재가 = ￦ { bithumb_coin_close1 } ]" )
                        print( f"[ 01-4. 변동성돌파금액 = ￦ { bithumb_btc_buy_price1_1 } ]" )

                        # 잔고 조회
                        # 빗썸_balance
                        bithumb_balance = bithumb_exchange.fetch_balance()
                        # 거래가능한 빗썸 원화 조회
                        bithumb_krw_balance = bithumb_balance['KRW']
                        print( f"[ 01-4. 현재 거래할 수 있는 총 금액은 = ￦ { bithumb_krw_balance['total'] } ]" )

                        # 거래가능한 빗썸 원화 90%
                        bithumb_buy_krw_balance = bithumb_krw_balance['total'] * 0.9
                        print( f"[ 01-4. 현재 매수 가능한 90% 금액은 = ￦ { bithumb_buy_krw_balance } ]" )
                        # 잔고 조회

                        # 매수할 코인의 갯수 구하기
                        bithumb_coin_buyPrice1 = bithumb_buy_krw_balance / bithumb_coin_close1
                        print( f"[ 01-4. 현재 매수할 빗썸 _ { bithumb_symbol1 } 코인 갯수는 = { bithumb_coin_buyPrice1 } ]" )

                        # 비트코인 매수는 0.0001부터라서 4자리수까지만
                        bithumb_coin_buyPrice_format1 = "{:.4f}".format( bithumb_coin_buyPrice1 )

                        print( f"[ 01-4. 현재 매수할 빗썸 _ { bithumb_symbol1 } 코인 갯수는 = { bithumb_coin_buyPrice_format1 } ]" )

                        # BTC 최소거래갯수
                        bithumb_coin_buy_low_balance1 = 0.0001 * 2



                        #if bithumb_buy_krw_balance > bithumb_lowSellPrice: # 거래가능 금액이 최소가능금액보다 높을때
                        if bithumb_coin_buyPrice_format1 > bithumb_coin_buy_low_balance1: # 거래가능 갯수가 최소가능갯수보다 높을때

                            print( "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++" )
                            print( f"[ 01-4. 변동성금액돌파 - 매수시도 전 ]" )
                            print()


                            # 시장가 매수
                            resp = bithumb_exchange.create_market_buy_order( symbol = bithumb_symbol1, amount = bithumb_coin_buyPrice_format1 )




                            # 1초 딜레이.
                            time.sleep(1)

                            print( f"[ 01-4. 변동성금액돌파 - 매수시도 후 ]" )
                            print()


                            # 코인 현재가
                            bithumb_tickers = bithumb_exchange.fetch_tickers()
                            bithumb_coin_krw1 = bithumb_tickers[bithumb_symbol1]
                            bithumb_coin_timestamp1 = bithumb_coin_krw1['timestamp'] / 100
                            bithumb_coin_close1 = bithumb_coin_krw1['close']
                            print( f"[ 01-4. 현재가 = ￦ { bithumb_coin_close1 } ]" )

                            # 거래가능한 빗썸_BTC코인 갯수 조회
                            bithumb_coin_balance1 = bithumb_balance[bithumb_coin1]
                            bithumb_coin_balance_format1 = "{:.8f}".format( bithumb_coin_balance1['total'] )
                            print( f"[ 01-4. 매수한 보유수량 = { bithumb_coin_balance_format1 } ]" )

                            # 코인 잔고 계산 = bithumb_coin_krw1 ( 현재가 ) * bithumb_coin_balance1 ( 보유코인갯수 )
                            bithumb_krw_coin_balance1 = float( bithumb_coin_close1 ) * float( bithumb_coin_balance_format1 )
                            print( f"[ 01-4. 매수한 평가금액 = ￦ { bithumb_krw_coin_balance1 } ]" )


                            # 코인 매수 가능유무  -  1 = 매수가능-매도불가 , 2 = 매수불가-매도가능
                            bithumb_op_mode1 = 2

                            print( f"[ 01-4. 매수불가-매도가능 ]" )
                            print()

                        else:   # 매수할 금액이 거래소 최소금액보다 작을때
                            print( f"[ 01-4. 매수할 금액( ￦ { bithumb_buy_krw_balance } )이 거래소 최소금액( ￦ { bithumb_lowSellPrice } )보다 적습니다. ]" )

                            # 코인 매수 가능유무  -  1 = 매수가능-매도불가 , 2 = 매수불가-매도가능
                            upbit_op_mode1 = 2
                            print( f"[ 01-4. 매수불가-매도가능 ]" )
                            print()

                        print( "--------------------------------------------------" )
                        print( "=  01-4. 빗썸 매수완료 - 완료                      =" )
                        print( "==================================================" )
                        print()

                        print()
                        print()
                        print( "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++" )
                        print()
                        print()

                # 코인1 - 매수종료
                ###############################

                ################################################################################################################################################################

                ################################################################################################################################################################






            # 1초 딜레이.
            time.sleep(1)


            