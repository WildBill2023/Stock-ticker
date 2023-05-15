stocks_dict = {
  "META": "240.42",
  "ABBV":"148.76",
  "CAT":"210.60",
  "sofi":"6.16",
  "AMZM":"109.89",
  "MBLY":"32.98",
  "CROX":"118.18",
  "MPW":"8.56",
  "LUV":"29.41",
  "DPZ":"316.40"}

fini = False  # boolean flag variable
while not fini:  # keep looping until fini is set to True
    
    symbol = input("please enter your stock symbol: (enter to exit) ")
    if not symbol:  # user just pressed enter, no text
        fini = True
        continue  # loop around and exit
        
    stock = stocks_dict.get(symbol)
    if not stock:  # not found in dictionary
        print (f'stock {symbol} not found, please try again')
        continue  # loop around
    
    print(stock)