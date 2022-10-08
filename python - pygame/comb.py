# comb sort made by Markimark, aka GiorDior, aka Giorgio
import pygame
from data.scripts.ArrayAndVisualisationSystem import Root, Render, Array, event

# using the comb sort to sort an array
# Unlike Bubblesort, which only compares neighbouring elements and swaps them 
# if necessary, Combsort first starts with elements that are far apart (gap). 
# In this way, elements that have been sorted roughly incorrectly find their target position more quickly. 
# After each run, the gap is reduced by dividing by 1.3 and the process is repeated.
def sort(root: Root, array: list[int]):
    factor = int(len(array) / 1.3)
    while not Array.isSorted(array):
        for i in range(len(array)):
            if i + factor <= len(array) - 1:
                if array[i + factor] < array[i]:
                    Render.array(root, array, "white", [[i, "red"],[i+factor, "green"]])
                    Array.swapElements(array, i, i + factor)

            else:
                break

        factor = int(factor/1.3)
        if factor == 0:
            factor = 1

    return array

if __name__ == "__main__":
    pygame.init()
    root = Root((1500, 800), "comb sort")

    unsorted_array = Array.generate(1, 100)

    sorted_array = sort(root, unsorted_array)

    # rendering the finally sorted array, all elements are green
    Render.array(root, sorted_array, ('green'))

    # program will still run, even if the array is already sorted
    while True:
        event()