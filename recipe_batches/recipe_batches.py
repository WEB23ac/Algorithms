#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    batches_list = []
    # ! Base Case: if recipe contains ingredient that is not included, simply return 0
    # * instantiate a 'batches' list
    # * iterate over each recipe component

    # * While at recipe[i], check if it exists in ingredients -- ~~~find attr recipe[i] in ingredients

    # * If recipe component doesn't exist in ingredients, push zero to batches // OR simply return zero
    for component in recipe:
        if component in ingredients.keys():
            possible_batches = ingredients[component] // recipe[component]
            if possible_batches == 0:
                return 0
            else:
                batches_list.append(possible_batches)
        else:
            return 0
   # * implementation of selection sort
    for i in range(0, len(batches_list) - 1):
        cur_index = i
        smallest_index = cur_index
        for j in range(i+1, len(batches_list)):
            if batches_list[j] < batches_list[i] and batches_list[j] < batches_list[smallest_index]:
                batches_list[cur_index], batches_list[j] = batches_list[j], batches_list[cur_index]
                j += 1

    # * the first entry in batches_list will be smallest, return that
    return batches_list[0]

    # ! reduce number of checks -- if a match is made loop can skip

    # * If it exists in ingredient list, push to batches list this result: ingredient['ingredient_name'] // recipe['ingredient_name']

    # * iterate over the batches list and return the lowest value as the number of possible batches.


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
