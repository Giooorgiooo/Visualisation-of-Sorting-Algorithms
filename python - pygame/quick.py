# quick sort made by Markimark, aka GiorDior, aka Giorgio
import pygame
from data.scripts.ArrayAndVisualisationSystem import Root, Render, Array, event

# using the quick sort to sort an array
# First, the list to be sorted is separated into two sub-lists ("left" and "right" sub-lists). 
# To do this, Quicksort selects a so-called pivot element from the list. All elements that are 
# smaller than the pivot element go into the left sub-list, and all that are larger go into the 
# right sub-list. The elements that are equal to the pivot element can be distributed among the 
# sub-lists as desired. After the distribution, the elements of the left list are smaller than or 
# equal to the elements of the right list.

# Afterwards, each sub-list must be sorted in itself to complete the sorting. To do this, 
# the quicksort algorithm is executed on the left and right sub-lists. Each sub-list is then split 
# into two sub-lists and the quicksort algorithm is applied to each of them again, and so on. These self-calls 
# are called recursion. If a partial list of length one or zero occurs, it has already been sorted and the recursion is aborted.

all_helping_arrays = []
big_helping_array = []
def sort(root, array) -> None:
    global all_helping_arrays, big_helping_array, index
    if not Array.isSorted(array):
        pivot_element = [array[0]]
        for a in range(len(pivot_element)):
            if len(big_helping_array) == 0:
                big_helping_array = array.copy()
                
            for i in range(len(big_helping_array)):
                if array[0] == big_helping_array[i]:
                    index = i

            for i in range(len(array)):
                if array[i] < pivot_element[a]:
                    before = array[i]
                    array.pop(i)
                    array.insert(array.index(pivot_element[a]), before)
                
                helping_array = []
                helping_array += big_helping_array[0:index]
                helping_array += array
                helping_array += big_helping_array[index + len(array):len(big_helping_array)]
                big_helping_array = helping_array.copy()
                Render.array(root, big_helping_array, "white")

            if Array.isSorted(array):
                all_helping_arrays.append(array)

            else: 
                if not len(array[0:array.index(pivot_element[a]) + 1]) == 0:
                    sort(root, array[0:array.index(pivot_element[a]) + 1])
                if not len(array[array.index(pivot_element[a])+1:len(array)]) == 0:
                    sort(root, array[array.index(pivot_element[a]) + 1:len(array)])
    else:
        all_helping_arrays.append(array)

if __name__ == "__main__":
    pygame.init()
    root = Root((1500, 800), "quick sort")

    unsorted_array = Array.generate(1, 100)

    sort(root, unsorted_array)
    sorted_array = []
    for i in range(len(all_helping_arrays)):
        for a in range(len(all_helping_arrays[i])):
            sorted_array.append(all_helping_arrays[i][a])
            
    # rendering the finally sorted array, all elements are green
    Render.array(root, sorted_array, ('green'))

    # program will still run, even if the array is already sorted
    while True:
        event()