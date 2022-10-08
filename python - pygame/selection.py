# selection sort made by Markimark, aka GiorDior, aka Giorgio
import pygame
from data.scripts.ArrayAndVisualisationSystem import Root, Render, Array, event

# using the selection sort to sort an array
# Selection sort works by taking the smallest element in an unsorted array and bringing it to the front.
def sort(root: Root, array: list[int]):
    for i in range(len(array)):     
        smallest_element = array[i]
        index_of_smaller_element = i
        for j in range(i, len(array)):
            if array[j] < smallest_element:
                smallest_element = array[j]
                index_of_smaller_element = j

            # rendering the current state of the algorithm
            Render.array(root, array, ('white'), [[j, "red"], [index_of_smaller_element, "green"], [i, "red"]])

        original_element_index = i
        # must check whether the smallest element is really smaller in case there was no smaller element in the current run
        if array[index_of_smaller_element] < array[original_element_index]:
            Array.swapElements(array, original_element_index, index_of_smaller_element)

    return array

if __name__ == "__main__":
    pygame.init()
    root = Root((1500, 800), "selection sort")

    unsorted_array = Array.generate(1, 100)

    sorted_arary = sort(root, unsorted_array)

    # rendering the finally sorted array, all elements are green
    Render.array(root, sorted_arary, ('green'))

    # program will still run, even if the array is already sorted
    while True:
        event()