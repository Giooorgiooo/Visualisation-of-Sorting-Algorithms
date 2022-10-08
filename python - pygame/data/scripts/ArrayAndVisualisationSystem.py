# general system for the visualization and creation of an random array

import pygame, random, sys

# creating the window
class Root:
    def __init__(self, size: tuple[int], caption: str) -> None:
        self.surface = pygame.display.set_mode(size)
        self.width = size[0]
        self.height = size[1]
        pygame.display.set_caption(caption)
        pygame.display.set_icon(pygame.image.load("data/images/image_icon.jpg"))

        # clock to limit the fps
        self.clock = pygame.time.Clock()
    
    def getSurface(self):
        return self.surface

    # updating the screen
    def update(self):
        pygame.display.update()

# checking events in case the user quits
def event():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

class Array:
    # checking if an array is sorted
    def isSorted(array: list[int]) -> bool:
        for index, element in enumerate(array):
            if not index + 1 == len(array):
                if array[index + 1] < element:
                    return False
        return True

    # generating a array, the smallest element is min, the highest is max
    # the array is shuffled at the end
    def generate(min: int, max: int) -> list[int]:
        array = []
        for num in range(min, max):
            array.append(num)
        random.shuffle(array)
        return array

    # swaping to elements of a given array
    def swapElements(array: list, first_index: int, second_index: int) -> list:
        first_element = array[first_index]
        second_element = array[second_index]
        array[first_index] = second_element
        array[second_index] = first_element
        return array

class Render:
    # visualizing the array to the screen
    def array(root: Root, array: list[int], color, 
    special_elements: list = []):
        
        root.getSurface().fill(('black'))
        
        # gap between the top of the screen and the highest element
        gap = 100
        maximal_height_of_element = root.height - gap
        element_width = root.width / len(array) - 1
        highest_element = max(array)
        elements_color = color

        for index, element in enumerate(array):
            # properties of the current element 
            width = element_width
            height = (element / highest_element) * maximal_height_of_element
            position_x = index * element_width + index 
            position_y = root.height - height
            
            # changing the color in case the current element is a special one (passed in the parameters)
            elements_color = color
            for special_element in special_elements:
                if special_element[0] == index:
                    # the color
                    elements_color = special_element[1]
            
            # drawing the element
            pygame.draw.rect(root.getSurface(), elements_color, (position_x, position_y, width, height))

        event()
        root.clock.tick(60)
        root.update()