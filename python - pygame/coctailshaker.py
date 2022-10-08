# coctailshaker sort made by Markimark, aka GiorDior, aka Giorgio
import pygame
from data.scripts.ArrayAndVisualisationSystem import Root, Render, Array, event

# using the coctailshaker sort to sort an array
# The array to be sorted is scanned alternately upwards and downwards. 
# In the process, two neighbouring elements are compared and swapped if necessary.
def sort(root: Root, array: list[int]):
    while not Array.isSorted(array):
        for i in range(len(array)):
            if i != len(array)-1:
                if array[i+1] < array[i]:
                    Array.swapElements(array, i+1, i)
                    Render.array(root, array, "white", [[i, "red"], [i + 1, "red"]])   
        
        for i in reversed(range(len(array))):
            if i != 0:
                if array[i-1] > array[i]:
                    Array.swapElements(array, i-1, i)
                    Render.array(root, array, "white", [[i, "red"], [i + 1, "red"]])   

    return array

if __name__ == "__main__":
    pygame.init()
    root = Root((1500, 800), "coctailshaker sort")

    unsorted_array = Array.generate(1, 100)

    sorted_array = sort(root, unsorted_array)

    # rendering the finally sorted array, all elements are green
    Render.array(root, sorted_array, ('green'))

    # program will still run, even if the array is already sorted
    while True:
        event()