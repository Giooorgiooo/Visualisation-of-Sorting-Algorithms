# insertion sort made by Markimark, aka GiorDior, aka Giorgio
import pygame
from data.scripts.ArrayAndVisualisationSystem import Root, Render, Array, event

# using the insertion sort to sort an array
#It runs through an array step by step and takes an element from the unsorted input sequence 
# and then inserts it again at the correspondingly correct position - "sorting by insertion". 
# The remaining elements of the array must then be moved behind the newly inserted value.
def sort(root: Root, array: list[int]):
    for i in range(1,len(array)):

        key = i
        j = i - 1

        while j >= 0 and array[key] < array[j]:
            Array.swapElements(array, j, key)
            Render.array(root, array, "white", [[j, "green"], [i, "red"]])
            j -= 1
            key -= 1
    return array

if __name__ == "__main__":
    pygame.init()
    root = Root((1500, 800), "insertion sort")

    unsorted_array = Array.generate(1, 20)

    sorted_arary = sort(root, unsorted_array)

    # rendering the finally sorted array, all elements are green
    Render.array(root, sorted_arary, ('green'))

    # program will still run, even if the array is already sorted
    while True:
        event()
