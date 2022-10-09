// selection sort by Markimark aka GiorDior aka Giorgio
// first project made in SDL2

#include "ArraysSys.hpp"
#include <iostream>
#include <SDL2/SDL.h>

const int screenHeight = 800;
const int screenWidth = 1500;

// using the selection sort to sort an array
// Selection sort works by taking the smallest element in an unsorted array and bringing it to the front.

void selectionSort(ArraySystem * arraySystem, SDL_Renderer * renderer, SDL_Event e, int array[], int length){

    int smallest_element, index_of_smallest_element;
 
    for (int i = 0; i < length; i++)
    {
        smallest_element = array[i];
        index_of_smallest_element = i;
        for (int j = i; j < length; j++){
            // comparing elements
            if (array[j] < array[index_of_smallest_element]){
                smallest_element = array[j];
                index_of_smallest_element = j;
            }
            int color[3] = {255, 255, 255};
            int specialIndexes[] = {i, j, index_of_smallest_element};
            // rendering the array after every comparison
            quitEvent(e);
            renderArray(screenWidth, screenHeight, renderer, array, length, color, specialIndexes);
        }

        // checking if the element is really smaller in case
        // there was no smaller element in this run
        if(array[index_of_smallest_element] < array[i]){
            arraySystem->swap(&array[index_of_smallest_element], &array[i]);
        }
    }
}
 
int main(int argc, char** argv)
{   
    // init
    SDL_Init(SDL_INIT_EVERYTHING);
    
    SDL_Window * window = SDL_CreateWindow("selection sort", SDL_WINDOWPOS_UNDEFINED, SDL_WINDOWPOS_UNDEFINED, screenWidth, screenHeight, 0);
    SDL_Renderer * renderer = SDL_CreateRenderer(window, -1, SDL_RENDERER_ACCELERATED);
    SDL_Event event;
    
    // class, which creates, shuffles, prints arrays and swaps
    // 2 elements
    ArraySystem * arraySystem = new ArraySystem();
    int unsortedArray[100];
    int arrayLength = 100;

    // adding 100 values to the array from 1 to 100
    arraySystem->add(unsortedArray, 1, arrayLength + 1);
    arraySystem->shuffle(unsortedArray, arrayLength);

    // sorting
    selectionSort(arraySystem, renderer, event, unsortedArray, arrayLength);
    
    // printing the values to the terminal
    arraySystem->print(unsortedArray, arrayLength);
    
    // finally rendering the array in green
    int color[3] = {0, 255, 0};
    int specialIndex[1] = {0};
    renderArray(screenWidth, screenHeight, renderer, unsortedArray, arrayLength, color, specialIndex);
    
    // program continues to run after the sort is done
    while (true){
        quitEvent(event);
    }
    return 0;
}