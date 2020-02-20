#!/usr/bin/python

import argparse


def selection_sort(arr):

    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        for j in range(i+1, len(arr)):
            if arr[j] < arr[i] and arr[j] < arr[smallest_index]:
                arr[cur_index], arr[j] = arr[j], arr[cur_index]
            j += 1
    return arr


# * takes list of stock prices

def find_max_profit(prices):
  # * loop through prices, find the lowest number that comes before the highest number
    purchase_prices = prices[:-1]
    sale_prices = prices[1:]
    differences = []


# * iterate through sale prices in order to subtract each purchase price from a sale price, appending the result to differences
    for i in range(0, len(purchase_prices)):
      # * j has range starting at  i to preserve the purchase-then-sale order.
        for j in range(i, len(sale_prices)):
            difference = sale_prices[j]-purchase_prices[i]
            differences.append(difference)

    differences = selection_sort(differences)
    return differences[len(differences)-1]
    # print(differences)

    # * iterate over zeroth through end-1 index of prices to fidn min vals


# # * iterate over prices to find max
    # for i in prices[1:]:
    #     if i > highest_price:
    #         highest_price = i
    #         highest_price_idx = prices.index(i)
# # * iterate over prices up to highest price, and create new array from highest_price minus current iteration value
#     for j in prices[:highest_price_idx]:
#         differences.append(highest_price-j)

#     # * Iterate over differences array and find largest value (similar to finding max value above). Assign profit to that value
#     for x in differences:
#         if x > profit:
#             profit = x

    # return profit


print(find_max_profit([100, 90, 80, 50, 20, 10]))

# if __name__ == '__main__':
#   # This is just some code to accept inputs from the command line
#     parser = argparse.ArgumentParser(
#         description='Find max profit from prices.')
#     parser.add_argument('integers', metavar='N', type=int,
#                         nargs='+', help='an integer price')
#     args = parser.parse_args()

#     print("A profit of ${profit} can be made from the stock prices {prices}.".format(
#         profit=find_max_profit(args.integers), prices=args.integers))
