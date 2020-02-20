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


# print(find_max_profit([100, 90, 80, 50, 20, 10]))
if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
