# odd-even sort made by Markimark, aka GiorDior, aka Giorgio
import pygame
from data.scripts.ArrayAndVisualisationSystem import Root, Render, Array, event

# using the odd-even sort to sort an array
# This is fundamentally a variant of bubble sorting. This algorithm is divided into two phases - the odd phase and the even phase. 
# The algorithm runs until the array elements are sorted, and in each iteration there are two phases - the odd phase and the even phase.
# In the odd phase, we perform bubble sorting for odd indexed elements and in the even phase, 
# we perform bubble sorting for even indexed elements.
def sort(root: Root, array: list[int]):
    for a in range(len(array)):
        # even
        if a % 2 == 0:
            for i in range(0, len(array), 2):
                if not i + 1 == len(array):
                    if array[i+1] < array[i]:
                        Array.swapElements(array, i + 1, i)
                        Render.array(root, array, "white", [[i, "red"], [i + 1, "red"]])          
        else:
            for i in range(1, len(array) - 1, 2):
                if array[i+1] < array[i]:
                    Array.swapElements(array, i + 1, i)
                    Render.array(root, array, "white", [[i, "red"], [i + 1, "red"]])      
    
    return array

if __name__ == "__main__":
    pygame.init()
    root = Root((1500, 800), "odd-even sort")

    unsorted_array = Array.generate(1, 100)

    sorted_arary = sort(root, unsorted_array)

    # rendering the finally sorted array, all elements are green
    Render.array(root, sorted_arary, ('green'))

    # program will still run, even if the array is already sorted
    while True:
        event()