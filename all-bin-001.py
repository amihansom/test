import ccxt
import pprint
import pandas as pd
import time
import datetime
import math




# 사용중인 API이름 - ami221210
api_key = "GZCPZlWu9ECOMiSfwP6TuhbbXeO08jxpMy3o61rWpWGHsE6NEeCRw3V3bXwZaW3m"
secret = "aFAIjvoZ85g3MNuEv31pPXGb7QRHkBCih5aSDVQ4BODIqaPZCzfKiCMTmxAtx33p"

# 선물 현재가 출력하기

binance = ccxt.binance( config = {
    'apiKey' : api_key, 
    'secret' : secret,
    'enableRateLimit' : True,
    'options' : {
        'defaultType' : 'future'
    }
} )

exchange = ccxt.binance()

symbol1 = "BTC/USDT"
























# def 함수
####################################
# 거래가능한 선물 보유금 BTC 갯수설정 #
def cal_amount( usdt_balance, cur_price ):
    # 거래금액 비율
    portion = 1
    # 거래금액산정
    usdt_trade = usdt_balance * portion
    # btc 거래갯수산정
    amount = math.floor( ( usdt_trade * 1000 ) / cur_price ) / 1000

    return amount









################################################################################################################################################################
################################################################################################################################################################
################################################################################################################################################################




btc = exchange.fetch_ohlcv(
    symbol=symbol1,
    timeframe='1d', 
    since=None, 
    limit=5
    )

df = pd.DataFrame( data = btc, columns = [ 'datetime', 'open', 'high', 'low', 'close', 'volume' ] )
df['datetime'] = pd.to_datetime( df[ 'datetime' ], unit = 'ms' )
df.set_index( 'datetime', inplace = True )

print( df )
print()


# 종가받기 10개
print( "========== 일봉 차트 받기 ==========" )
print()
# 0은 아무것도 아님.
price_0_close = df.iloc[ 0 ][ 'close' ]
#price_0_time = df.iloc[ 0 ][ 'datetime' ]

########################################
# -1은 금일. 시작가.
price_1_open = df.iloc[ -1 ][ 'open' ]
print( f"오늘 시작가 = {price_1_open}")
price_2_close = df.iloc[ -2 ][ 'close' ]
print( f"어제 종가 = {price_2_close}")

########################################
# -2는 어제. 고가
price_2_high = df.iloc[ -2 ][ 'high' ]
print( f"어제 고가 = {price_2_high}")
price_2_low = df.iloc[ -2 ][ 'low' ]
print( f"어제 저가 = {price_2_low}")





# 변동성돌파전략 변동폭
price_2_length = price_2_high - price_2_low
btc_buy_price1 = price_1_open + price_2_length
btc_buy_price1_1 = price_2_close + price_2_length

print(f"어제 변동폭 = {price_2_length}")
print(f"오늘 돌파금액 = {btc_buy_price1}")
print(f"오늘 돌파금액 = {btc_buy_price1_1}")
print()



time.sleep(1)






################################################################################################################################################################
################################################################################################################################################################
################################################################################################################################################################

#################
# 선물 잔고 조회 #
#################

print( "========== ========== ==========" )
print( "       선 물  잔 고  조 회" )
print( "========== ========== ==========" )
print()

balance = binance.fetch_balance()
print( "보유코인" )
pprint.pprint( balance[ 'total' ] )
pprint.pprint( balance[ 'total' ][ 'USDT' ] )
pprint.pprint( balance[ 'total' ][ 'BTC' ] )
print()

print( "포지션" )
positions = balance[ 'info' ][ 'positions' ]
print()

for position in positions:
    if position[ 'symbol' ] == "BTCUSDT":
        pprint.pprint( position )

        btc_position_amt = float( position[ 'positionAmt' ] )
        print( f"현재 포지션은 ? { btc_position_amt }" )
        print( f"진입한 btc코인의 변수타입은? { type( btc_position_amt ) }" )




        if btc_position_amt > 0:
            print( "1. 현재 롱포지션 진입상태" )
            btc_position_1 = 1

        elif btc_position_amt == 0:
            print( "2. 현재 포지션 진입을 안한상태" )
            btc_position_1 = 0

        elif btc_position_amt < 0:
            print( "3. 현재 숏포지션 진입상태" )
            btc_position_1 = -1

        btc_future_leverage = int( position[ 'leverage' ] )
        print( f"현재 레버리지의 변수타입은? { type( btc_future_leverage ) }" )



print()
print()






###################
# 선물 현재가 조회 #
###################
print( "========== ========== ==========" )
print( "      선 물  현 재 가  조 회" )
print( "========== ========== ==========" )
print()

btc = binance.fetch_ticker( "BTC/USDT" )
pprint.pprint( float( btc[ 'last' ] ) )
print( f"BTC/USDT 현재가 = { btc[ 'last' ] }" )
print()
print()



######################
# 거래가능한 USDT 갯수 #
######################
print( "========== ========== ==========" )
print( "        거래가능한 BTC 갯수" )
print( "========== ========== ==========" )
print()
balance = binance.fetch_balance()
usdt = float( balance[ 'total' ][ 'USDT' ] )
print( f"보유 USDT = { usdt }" )
print( f"보유 USDT 의 변수타입은? { type( usdt ) }" )

btc = binance.fetch_ticker( symbol = "BTC/USDT" )
cur_price = float( btc[ 'last' ] )
print( f"BTC 종가의 변수타입은? { type( cur_price ) }" )
amount_1 = cal_amount( usdt, cur_price )
print( f"보유 USDT로 BTC 거래가능한 갯수 = { amount_1 }" )
print( f"보유 USDT로 BTC 거래가능한 갯수의 변수타입은? { type( amount_1 ) }" )
print()
print()






################
# 레버리지 설정 #
################
#markets = binance.load_markets()
#coin_1 = "BTC/USDT"
#market_1 = binance.market(coin_1)
# 레버리지 3배
#leverage_1 = 3

#resp_1 = binance.fapiPrivate_post_leverage({
#    'symbol': market_1['id'],
#    'leverage': leverage_1
#})


















#_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+
#_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+
#_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+

# 포지션 진입 최대 usdt 금액
usdt_trade_MAX_price = 1100

#_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+
#_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+
#_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+


# 현재 레버리지 배율 10 배
#btc_leverage = 10  # 현재 레버리지 설정값
btc_leverage = btc_future_leverage  # 레버리지 가져옴

if btc_leverage > 1:   # 레버리지 비율이 1 초과면 
    btc_leverage_1 = btc_leverage - 1  # 진입시 사용할 레버리지 배율
elif btc_leverage <= 1:   # 레버리지 비율이 1 이하이면 
    btc_leverage_1 = 1  # 진입시 사용할 레버리지 배율


#_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+
#_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+
#_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+


print( f"-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=" )
print( f"0-1. 재시작시 포지션 유지중이면" )
print()
#print( f"0-2. 현재 매수매도조회 코드는? btc_mode = { btc_mode }" )
print()
print( f"0-3-1. 현재 거래중인 코인갯수는? btc_position_amt = { btc_position_amt }" )
print( f"0-3-2. 진입한 btc코인의 변수타입은? { type( btc_position_amt ) }" )
print( f"0-3-3. 현재 거래중인 코인의 포지션 코드는? btc_position_1 = { btc_position_1 }" )

if btc_position_amt > 0:
    print( "0-3-4. 현재 롱포지션 진입상태" )
    btc_position_1 = 1

elif btc_position_amt == 0:
    print( "0-3-5. 현재 포지션 진입을 안한상태" )
    btc_position_1 = 0

elif btc_position_amt < 0:
    print( "0-3-6. 현재 숏포지션 진입상태" )
    btc_position_1 = -1



print()
print( f"0-4-1. 현재 설정된 레버리지 배율은 btc_leverage = { btc_leverage }" )
print( f"0-4-2. 진입시 설정될 레버리지 배율은 btc_leverage_1 = { btc_leverage_1 }" )
# 변동성 코드가 btc_mode = 1 -> 변동성 설정가능
btc_mode = 1
print( f"0-5-1.  btc_mode = 1 -> 변동성 설정가능" )
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

    # 장 시작 전 포지션 정리
    if now.hour == 23 and now.minute == 59 and 50 <= now.second <= 59:   # 23시 59분 50초~59초사이:
        # 변동성 코드가 btc_mode = 2 -> 변동성 설정불가 일때 일괄 포지션 정리
        if btc_mode == 2:

            print()
            print()
            print( "-=-=-=-=-=- ********** -=-=-=-=-=- ********** -=-=-=-=-=-" )
            print( f"[ 현재시간 : {now} ]   -   선물포지션 정리 매매 - 시작" )
            print( "-=-=-=-=-=- ********** -=-=-=-=-=- ********** -=-=-=-=-=-" )
            print()




            ################
            # 레버리지 설정 #
            ################
#            markets = binance.load_markets()
#            coin_1 = "BTC/USDT"
#            market_1 = binance.market(coin_1)
            # 레버리지 3배
#            leverage_1 = 3

#            resp_1 = binance.fapiPrivate_post_leverage({
#                'symbol': market_1['id'],
#                'leverage': leverage_1
#            })





            #################
            # 선물 잔고 조회 #
            #################
            print( "========== ========== ==========" )
            print( "       선 물  잔 고  조 회" )
            print( "========== ========== ==========" )
            print()

            balance = binance.fetch_balance()
            print( "보유코인" )
            pprint.pprint( balance[ 'total' ] )
            #pprint.pprint( balance[ 'total' ][ 'USDT' ] )
            #pprint.pprint( balance[ 'total' ][ 'BTC' ] )
            print( "포지션" )
            positions = balance[ 'info' ][ 'positions' ]

            for position in positions:
                if position[ 'symbol' ] == "BTCUSDT":
                    pprint.pprint( position )

                    btc_position_amt = float( position[ 'positionAmt' ] )
                    print( f"현재 포지션은 ? { btc_position_amt }" )
                    print( f"현재 포지션의 변수타입은? { type( btc_position_amt ) }" )


                    if btc_position_amt > 0:
                        print( "1. 현재 롱포지션 진입상태" )
                        btc_position_1 = 1

                    elif btc_position_amt == 0:
                        print( "2. 현재 포지션 진입을 안한상태" )
                        btc_position_1 = 0

                    elif btc_position_amt < 0:
                        print( "3. 현재 숏포지션 진입상태" )
                        btc_position_1 = -1
                    
                    # 레버리지 값 가져옴
                    btc_future_leverage = int( position[ 'leverage' ] )
                    btc_leverage = btc_future_leverage

                    if btc_leverage > 1:   # 레버리지 비율이 1 초과면 
                        btc_leverage_1 = btc_leverage - 1  # 진입시 사용할 레버리지 배율
                    elif btc_leverage <= 1:   # 레버리지 비율이 1 이하이면 
                        btc_leverage_1 = 1  # 진입시 사용할 레버리지 배율

                        

            print( f"현재 내 포지션 코드는? btc_position = { btc_position_1 }" )
            print()


            print( f"-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=" )
            print( f"1-1. 현재시간 포지션 유지중이면" )
            print( f"     값." )
            #print( f"1-2-1. 이전 macd 코드는? btc_mode = {btc_mode}" )
            #print( f"1-2-2. 현재 macd 코드는? btc_macd = {now_macd}" )
            print()
            print( f"1-3-1. 현재 거래중인 코인갯수는? btc_position_amt = { btc_position_amt }" )
            print( f"1-3-2. 진입한 btc코인의 변수타입은? { type( btc_position_amt ) }" )
            print( f"1-3-3. 현재 거래중인 코인의 포지션 코드는? btc_position_1 = { btc_position_1 }" )

            if btc_position_amt > 0:
                print( "1-3-4. 현재 롱포지션 진입상태" )
                btc_position_1 = 1

            elif btc_position_amt == 0:
                print( "1-3-5. 현재 포지션 진입을 안한상태" )
                btc_position_1 = 0

            elif btc_position_amt < 0:
                print( "1-3-6. 현재 숏포지션 진입상태" )
                btc_position_1 = -1

            print()
            print( f"1-4-1. 현재 설정된 레버리지 배율은 btc_leverage = { btc_leverage }" )
            print( f"1-4-2. 진입시 설정될 레버리지 배율은 btc_leverage_1 = { btc_leverage_1 }" )
            print( f"-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=" )
            print()
            print()

            time.sleep(1)


            # 롱 포지션 정리
            if btc_position_1 == 1:   # 롱 포지션 정리
                print( "1-1. 롱 포지션 정리" )
                print( f"1-2. 롱 포지션 정리할 코인 갯수 = { btc_position_amt }" )
                print( f"1-2. 롱 포지션 정리할 코인 갯수의 변수타입은? { type( btc_position_amt ) }" )
                print( f"1-3. 포지션 코드 = { btc_position_1 }" )

                if btc_position_amt != 0:
                    order = binance.create_market_sell_order( symbol = "BTC/USDT", amount = btc_position_amt )
                    print( "1-3. 롱 포지션 정리완료" )

                    time.sleep(1)

                    # 무 포지션으로 코드 변경
                    btc_position_1 = 0
                    print( f"1-4. btc_position_1 = { btc_position_1 } 무 포지션으로 변경" )
                    # 변동성 코드가 btc_mode = 1 -> 변동성 설정가능
                    btc_mode = 1
                    print( f"1-4-1.  btc_mode = 1 -> 변동성 설정가능" )
            

            # 숏 포지션 정리
            if btc_position_1 == -1:   # 숏 포지션 정리
                print( "3-1. 숏 포지션 정리" )
                print( f"3-2. 숏 포지션 정리할 코인 갯수 = { btc_position_amt }" )
                print( f"3-2. 숏 포지션 정리할 코인의 변수타입은? { type( btc_position_amt ) }" )
                print( f"3-3. 포지션 코드 = { btc_position_1 }" )

                if btc_position_amt != 0:
                    print( "3-3-0. 숏 포지션 정리하기 전 테스트용" )

                    print( f"3-3-1. 포지션 코인을 음수에서 양수로 바꾸기 전 = { btc_position_amt }" )
                    print( "3-3-1. 포지션 코인이 음수이면 양수로 바꿔쭌다." )  

                    if btc_position_amt < 0:    # 포지션 코인이 음수이면 양수로 바꿔준다.
                        btc_position_amt = -( btc_position_amt )
                        print( f"3-3-1. 포지션 코인을 음수에서 양수로 바꾼 후 = { btc_position_amt }" )
                        print( f"3-3-1. 포지션 코인의 변수타입은? { type( btc_position_amt ) }" )

                    print( "3-3-2. 숏포지션 정리전." )
                    order = binance.create_market_buy_order( symbol = "BTC/USDT", amount = btc_position_amt )

                    print( "3-3-3. 숏 포지션 정리완료" )

                    time.sleep(1)
                
                # 무 포지션으로 코드 변경
                btc_position_1 = 0
                print( f"3-4. btc_position = { btc_position_1 } 무 포지션으로 변경" )
                # 변동성 코드가 btc_mode = 1 -> 변동성 설정가능
                btc_mode = 1
                print( f"3-4-1.  btc_mode = 1 -> 변동성 설정가능" )

            print()
            print()
            print( "-=-=-=-=-=- ********** -=-=-=-=-=- ********** -=-=-=-=-=-" )
            print( f"[ 현재시간 : {now} ]   -   선물포지션 정리 매매 - 종료" )
            print( "-=-=-=-=-=- ********** -=-=-=-=-=- ********** -=-=-=-=-=-" )
            print()

        ################################################################################################################################################################
        ################################################################################################################################################################
        ################################################################################################################################################################









    else:
        # 장 시작 전 변동성돌파매매 금액 설정
        # 변동성 코드가 btc_mode = 1 -> 변동성 설정가능
        if btc_mode == 1 or now.hour == 00 and now.minute == 00 and 10 <= now.second <= 20:   # 00시 00분 10초~20초사이:
            ################################################################################################################################################################
            ##  돌파매매금액 설정 - 시작  ####################################################################################################################################
            ################################################################################################################################################################
            btc = exchange.fetch_ohlcv(
                symbol=symbol1,
                timeframe='1d', 
                since=None, 
                limit=5
                )

            df = pd.DataFrame( data = btc, columns = [ 'datetime', 'open', 'high', 'low', 'close', 'volume' ] )
            df['datetime'] = pd.to_datetime( df[ 'datetime' ], unit = 'ms' )
            df.set_index( 'datetime', inplace = True )

            print( df )
            print()


            # 종가받기 10개
            print( "========== 일봉 차트 받기 ==========" )
            print()
            # 0은 아무것도 아님.
            price_0_close = df.iloc[ 0 ][ 'close' ]
            #price_0_time = df.iloc[ 0 ][ 'datetime' ]

            ########################################
            # -1은 금일. 시작가.
            price_1_open = df.iloc[ -1 ][ 'open' ]
            print( f"오늘 시작가 = {price_1_open}")
            price_2_close = df.iloc[ -2 ][ 'close' ]
            print( f"어제 종가 = {price_2_close}")

            ########################################
            # -2는 어제. 고가
            price_2_high = df.iloc[ -2 ][ 'high' ]
            print( f"어제 고가 = {price_2_high}")
            price_2_low = df.iloc[ -2 ][ 'low' ]
            print( f"어제 저가 = {price_2_low}")





            # 변동성돌파전략 변동폭
            price_2_length = price_2_high - price_2_low
            btc_buy_price1 = price_1_open + price_2_length
            btc_buy_price1_1 = price_2_close + price_2_length

            print(f"어제 변동폭 = {price_2_length}")
            print(f"오늘 돌파금액 = {btc_buy_price1}")
            print(f"오늘 돌파금액 = {btc_buy_price1_1}")
            print()

            # 변동성 코드가 btc_mode = 2 -> 변동성 설정불가
            btc_mode = 2
            print( f"btc_mode = 2 -> 변동성 설정불가" )



            time.sleep(1)






            ################################################################################################################################################################
            ################################################################################################################################################################
            ################################################################################################################################################################

            

        else:
            ################################################################################################################################################################
            ##  돌파매매조건 롱포지션 진입  ##################################################################################################################################
            ################################################################################################################################################################

            # 코인 현재가 조회
            btc = binance.fetch_ticker( "BTC/USDT" )

            # btc[ 'last' ] 는 현재 가격임.
            if btc[ 'last' ] > btc_buy_price1_1:    # 코인현재가가 돌파매매가격 btc_buy_price1_1 보다 높을 때 롱포지션 진입
                #################
                # 선물 잔고 조회 #
                #################

                print()
                print( "========== ========== ==========" )
                print( "   돌파 매매 초과 롱포지션 진입" )
                print( "========== ========== ==========" )
                print()


                print( "========== ========== ==========" )
                print( "       선 물  잔 고  조 회" )
                print( "========== ========== ==========" )
                print()

                balance = binance.fetch_balance()
                print( "보유코인" )
                pprint.pprint( balance[ 'total' ] )
                pprint.pprint( balance[ 'total' ][ 'USDT' ] )
                pprint.pprint( balance[ 'total' ][ 'BTC' ] )
                print()

                print( "포지션" )
                positions = balance[ 'info' ][ 'positions' ]
                print()

                for position in positions:
                    if position[ 'symbol' ] == "BTCUSDT":
                        pprint.pprint( position )

                        btc_position_amt = float( position[ 'positionAmt' ] )
                        print( f"현재 포지션은 ? { btc_position_amt }" )
                        print( f"진입한 btc코인의 변수타입은? { type( btc_position_amt ) }" )




                        if btc_position_amt > 0:
                            print( "1. 현재 롱포지션 진입상태" )
                            btc_position_1 = 1

                        elif btc_position_amt == 0:
                            print( "2. 현재 포지션 진입을 안한상태" )
                            btc_position_1 = 0

                        elif btc_position_amt < 0:
                            print( "3. 현재 숏포지션 진입상태" )
                            btc_position_1 = -1

                        btc_future_leverage = int( position[ 'leverage' ] )
                        print( f"현재 레버리지의 변수타입은? { type( btc_future_leverage ) }" )



                print()
                print()






                ###################
                # 선물 현재가 조회 #
                ###################
                print( "========== ========== ==========" )
                print( "      선 물  현 재 가  조 회" )
                print( "========== ========== ==========" )
                print()

                btc = binance.fetch_ticker( "BTC/USDT" )
                pprint.pprint( float( btc[ 'last' ] ) )
                print( f"BTC/USDT 현재가 = { btc[ 'last' ] }" )
                print()
                print()



                ######################
                # 거래가능한 USDT 갯수 #
                ######################
                print( "========== ========== ==========" )
                print( "        거래가능한 BTC 갯수" )
                print( "========== ========== ==========" )
                print()
                balance = binance.fetch_balance()
                usdt = float( balance[ 'total' ][ 'USDT' ] )
                print( f"보유 USDT = { usdt }" )
                print( f"보유 USDT 의 변수타입은? { type( usdt ) }" )

                btc = binance.fetch_ticker( symbol = "BTC/USDT" )
                cur_price = float( btc[ 'last' ] )
                print( f"BTC 종가의 변수타입은? { type( cur_price ) }" )
                amount_1 = cal_amount( usdt, cur_price )
                print( f"보유 USDT로 BTC 거래가능한 갯수 = { amount_1 }" )
                print( f"보유 USDT로 BTC 거래가능한 갯수의 변수타입은? { type( amount_1 ) }" )
                print()
                print()






                ################
                # 레버리지 설정 #
                ################
                #markets = binance.load_markets()
                #coin_1 = "BTC/USDT"
                #market_1 = binance.market(coin_1)
                # 레버리지 3배
                #leverage_1 = 3

                #resp_1 = binance.fapiPrivate_post_leverage({
                #    'symbol': market_1['id'],
                #    'leverage': leverage_1
                #})


















                #_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+
                #_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+
                #_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+

                # 포지션 진입 최대 usdt 금액
                usdt_trade_MAX_price = 1100

                #_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+
                #_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+
                #_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+


                # 현재 레버리지 배율 10 배
                #btc_leverage = 10  # 현재 레버리지 설정값
                btc_leverage = btc_future_leverage  # 레버리지 가져옴

                if btc_leverage > 1:   # 레버리지 비율이 1 초과면 
                    btc_leverage_1 = btc_leverage - 1  # 진입시 사용할 레버리지 배율
                elif btc_leverage <= 1:   # 레버리지 비율이 1 이하이면 
                    btc_leverage_1 = 1  # 진입시 사용할 레버리지 배율


                #_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+
                #_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+
                #_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+


                print( f"-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=" )
                print( f"0-1. 재시작시 포지션 유지중이면" )
                print()
                #print( f"0-2. 현재 매수매도조회 코드는? btc_mode = { btc_mode }" )
                print()
                print( f"0-3-1. 현재 거래중인 코인갯수는? btc_position_amt = { btc_position_amt }" )
                print( f"0-3-2. 진입한 btc코인의 변수타입은? { type( btc_position_amt ) }" )
                print( f"0-3-3. 현재 거래중인 코인의 포지션 코드는? btc_position_1 = { btc_position_1 }" )

                if btc_position_amt > 0:
                    print( "0-3-4. 현재 롱포지션 진입상태" )
                    btc_position_1 = 1

                elif btc_position_amt == 0:
                    print( "0-3-5. 현재 포지션 진입을 안한상태" )
                    btc_position_1 = 0

                elif btc_position_amt < 0:
                    print( "0-3-6. 현재 숏포지션 진입상태" )
                    btc_position_1 = -1



                print()
                print( f"0-4-1. 현재 설정된 레버리지 배율은 btc_leverage = { btc_leverage }" )
                print( f"0-4-2. 진입시 설정될 레버리지 배율은 btc_leverage_1 = { btc_leverage_1 }" )
                
                print( f"-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=" )



                # 롱 포지션 진입
                if btc_position_1 == 0:   # 무 포지션 상태
                    balance = binance.fetch_balance()
                    usdt = float( balance[ 'total' ][ 'USDT' ] )
                    print( f"4-1. 보유 USDT = { usdt }" )
                    print( f"4-1. 보유 USDT 의 변수타입은? { type( usdt ) }" )

                    btc = binance.fetch_ticker(symbol = "BTC/USDT")
                    cur_price = float( btc['last'] )
                    print( f"4-1. BTC 종가의 변수타입은? { type( cur_price ) }" )
                    #amount_1 = float( cal_amount( usdt, cur_price ) )


                    print( f"4-1-5. 1,100usdt 이하. ▼" )

                    amount_1 = float( cal_amount( usdt, cur_price ) )
                    print( f"4-1-6. 진입할 1배 btc 코인 - { amount_1 }" )
                    print( f"4-1-7. 진입할 btc코인의 변수타입은? { type( amount_1 ) }" )

                    # btc_leverage_1 진입 레버리지 배율
                    amount_1_1 = amount_1 * btc_leverage_1
                    print( f"4-1-8. 진입할 { btc_leverage_1 }배 총 btc 코인 - { amount_1_1 }" )
                    print( f"4-1-8. 진입할 총코인의 변수타입은? { type( amount_1_1 ) }" )


                    print( "4-2. 롱 포지션 진입" )
                    print( f"4-3. 롱 포지션 진입할 코인 갯수 = { amount_1_1 }" )
                    order = binance.create_market_buy_order( symbol = "BTC/USDT", amount = amount_1_1 )
                    print( "4-4. 롱 포지션 진입완료" )


                    # 롱 포지션 진입시 들어간 코인 갯수
                    print( f"4-5. 진입코인갯수 저장 btc_position_amt = { amount_1_1 }" )

                    time.sleep(1)
                

                # 포지션 롱으로 코드 변경
                btc_position_1 = 1
                print( f"3, 4. 거래후 btc_position = 1 -> 롱 포지션" )


                    

                ######################
                # 매수/롱 포지션 진입 #
                ######################
                #order = binance.creat_market_buy_order( symbol = "BTC/USDT", amount = amount_1 )


                ######################
                # 매수/롱 포지션 정리 #
                ######################
                #order = binance.creat_market_sell_order( symbol = "BTC/USDT", amount = amount_1 )

            ################################################################################################################################################################

            ################################################################################################################################################################






            # 1초 딜레이.
            time.sleep(1)


            