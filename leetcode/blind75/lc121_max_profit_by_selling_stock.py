from typing import List
def get_max_profit(prices: List[int]) -> int:
    profit = 0  # initialize the return value

    buy_price = prices[0]  # initliaizing the fist possible buy-price

    for stock_price in prices[1:]:
        
        curr_stock_price = stock_price # taking a new variable just for better understanding

        if curr_stock_price < buy_price:
            buy_price = curr_stock_price
        
        # else ccurrent stock_price >=  buy_price 
        # AND you can tecnically sell and book profit
        else:
            profit = max(profit, (curr_stock_price - buy_price)) # curr_profit =  curr_stock_price - buy_price 
        
        '''
        # or directly write this instead of else section  
        # else section has been written to easy understanding 
        profit = max(profit, (curr_stock_price - buy_price))
        '''

    return profit

# Driver code
if __name__ == "__main__":
   prices = [7,1,5,3,6,4]  # eg 1
   # prices = [7,6,4,3,1]  # eg 2
   max_profit = get_max_profit(prices)
   print("max_profit: ", max_profit) 
