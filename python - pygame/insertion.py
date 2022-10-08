# selection sort made by Markimark, aka GiorDior, aka Giorgio
import pygame
from data.scripts.ArrayAndVisualisationSystem import Root, Render, Array, event

# using the selection sort to sort an array
# Selection sort works by taking the smallest element in an unsorted array and bringing it to the front.
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