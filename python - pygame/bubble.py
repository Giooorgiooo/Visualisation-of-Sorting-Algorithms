# bubble sort made by Markimark, aka GiorDior, aka Giorgio
import pygame
from data.scripts.ArrayAndVisualisationSystem import Root, Render, Array, event

# using the bubble sort to sort an array
# In the bubble phase, the input list is scrolled from left to right. In each step, 
# the current element is compared with its neighbour on the right. If the two elements violate the sorting criterion, 
# they are swapped. At the end of the phase, the largest or smallest element of the input is at the end of the list in 
# ascending or descending order.
def sort(root: Root, array: list[int]):
    n = len(array)
    for i in range(n):
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                Array.swapElements(array, j, j + 1) 
                Render.array(root, array, "white", [[j, "red"], [j + 1, "red"]])   
    return array

if __name__ == "__main__":
    pygame.init()
    root = Root((1500, 800), "bubble sort")

    unsorted_array = Array.generate(1, 100)

    sorted_array = sort(root, unsorted_array)

    # rendering the finally sorted array, all elements are green
    Render.array(root, sorted_array, ('green'))

    # program will still run, even if the array is already sorted
    while True:
        event()
