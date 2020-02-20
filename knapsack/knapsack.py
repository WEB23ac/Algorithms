#!/usr/bin/python

import sys
from collections import namedtuple


# class Item:
#     def __init__(self, index, size, value):
#         self.index = index
#         self.size = size
#         self.value = value

#     def __str__(self):
#         return f'{self.index}  {self.size}  {self.value}'


Item = namedtuple('Item', ['index', 'size', 'value'])


#  * Helper function to evaluate the value of an inventory
def evaluate_value(inventory_1, inventory_2):
    inventory_1_value = 0
    inventory_2_value = 0
    for i in range(0, len(inventory_1)-1):
        inventory_1_value = + inventory_1[i].value
    for j in range(0, len(inventory_2)-1):
        inventory_2_value += inventory_2[j].value


# * Start with capacity of 0, find items to add that meet capacity 0. Then, move on to capacity 1, find items that meet capacity 1


def knapsack_solver(items, capacity):
    print(items)
    # considered_items = []
    response = {
        "value": 0,
        "chosen": []
    }

    for i in range(0, len(items)-1, -1):
        print(items[i])
        index = items[i].index
        size = items[i].size
        value = items[i].value
        if len(items) == 0 or capacity == 0:
            return 0
        elif size > capacity:
          # * if the size of current item is greater than capacity, test out the item to the left
            return knapsack_solver(items[:index-1], capacity)
        else:
            inventory_1 = knapsack_solver(items[:index-1], capacity)
            response.value += value
            response.chosen.append(items[i])
            inventory_2 = knapsack_solver(items[:index-1], capacity-size)

        return response

        # result = evaluate_value(inventory_1, inventory_2)
        # capacity -= items[i].size
        # value += items[i].value

        knapsack_solver(items[:i], capacity)

# * Loop through an array of 0 - capacity
    # for i in range(0, capacity):

        # for j in range(0, items):
        #   if items[j].value <= capacity and items[j].value >= 0:
        #     inventory.append(items[j])

    # for item in items:
    #     # print(f'Currently looking at {item}')

    #     if item.size > inventory_space:
    #         pass

    #     else:
    #         inventory.append(item)
    #         capacity -= item.size
    #     knapsack_solver(items[item.index:], capacity, inventory)
    #     # if items[index]:

    # if evaluate_value(inventory) > evaluate_value(inventory_original):
    #     return inventory
    # else:
    #     return inventory_original


if __name__ == '__main__':
    if len(sys.argv) > 1:
        capacity = int(sys.argv[2])
        file_location = sys.argv[1].strip()
        file_contents = open(file_location, 'r')
        items = []

        for line in file_contents.readlines():
            data = line.rstrip().split()
            items.append(Item(int(data[0]), int(data[1]), int(data[2])))

        file_contents.close()
        print(knapsack_solver(items, capacity))
    else:
        print('Usage: knapsack.py [filename] [capacity]')
