# heap sort made by Markimark, aka GiorDior, aka Giorgio
import pygame
from data.scripts.ArrayAndVisualisationSystem import Root, Render, Array, event

# using the heap sort to sort an array
# Heap sorting is a comparison-based sorting technique. It is similar to selection sorting, where you first find the smallest 
# element and put it at the beginning. Repeat the same process for the remaining elements.
def sort(root: Root, array: list[int]):
    helping_array = []
    while True:
        i = 0
        while i < len(array):
            try:
                if array[i * 2 + 1] > array[i]:
                    Array.swapElements(array, i * 2 + 1, i)
                    Render.array(root, array + helping_array, "white", [[i, "red"], [i * 2 + 1, "green"]])
                    i = 0
                    continue
            
                if array[i * 2 + 2] > array[i]:
                    Array.swapElements(array, i * 2 + 2, i)
                    Render.array(root, array + helping_array, "white", [[i, "red"], [i * 2 + 2, "green"]])
                    i = 0
                    continue
            except:
                pass
                
            i += 1

        try:
            Array.swapElements(array, len(array) - 1, 0)   
            helping_array.insert(0, array[len(array) - 1])
            array.pop(len(array)-1)
        except:
            break
    
    array = helping_array.copy()
    return array

if __name__ == "__main__":
    pygame.init()
    root = Root((1500, 800), "heap sort")

    unsorted_array = Array.generate(1, 100)

    sorted_array = sort(root, unsorted_array)

    # rendering the finally sorted array, all elements are green
    Render.array(root, sorted_array, ('green'))

    # program will still run, even if the array is already sorted
    while True:
        event()