def getProductsOfAllExceptAtIndex(given_array):
    products = [1] 

    for i in range (1, len(given_array)):
        products.append(given_array[i-1] * products[-1])

    products_right = 1
    
    for i in range((len(given_array)-1), -1, -1):
        products[i]*= products_right
        products_right*= given_array[i]

    return products


# Drive code
array = [4, 3, 2, 1]
result = getProductsOfAllExceptAtIndex(array)
print(result)
