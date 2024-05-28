from typing import List
def get_max_profit(prices: List[int]) -> int:
    profit = 0  # initialize the thing which you have to return 
                # default profit as mentioned in the ques is 0. Since we are asked max_profit, we need to set it to min possible profit.
                # Here in this case it is 0. It can'e be -ve as we have to see only we get a stock price greater than buy_price 

    buy_price = prices[0]  # initliaizing the fist possible buy-price

    for stock_price in prices[1:]:
        
        curr_stock_price = stock_price # taking a new variable just for better understanding

        if curr_stock_price < buy_price:
            buy_price = curr_stock_price
            continue    # I added a continue statement just after buy_price = curr_stock_price, to save few milliseconds 
        
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

'''
Time Complexity: O(n) 
As we are iterating through the elements of the list only ONCE.

Space Complexity: O(1)
No Additional Data Structure has been used.


## 


'''