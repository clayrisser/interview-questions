def main():
    prices = [10, 7, 5, 8, 11, 9]
    print('get_max_profit1')
    profit = get_max_profit1(prices)
    print(profit)
    print('get_max_profit2')
    profit = get_max_profit2(prices)
    print(profit)

# O(n) time
# O(n) space
def get_max_profit1(prices):
    min_position = 0
    max_position = 0
    for i in range(len(prices)):
        if prices[i] < prices[min_position]:
            min_position = i
        if max_position < min_position:
            max_position = i
        if prices[i] > prices[max_position]:
            max_position = i
    return prices[max_position] - prices[min_position]

# O(n) time
# O(n) space
def get_max_profit2(prices):
    min_price = prices[0]
    profit = prices[1] - prices[0]
    for i in range(len(prices)):
        potential_profit = prices[i] - min_price
        profit = max(profit, potential_profit)
        min_price = min(min_price, prices[i])
    return profit

main()
