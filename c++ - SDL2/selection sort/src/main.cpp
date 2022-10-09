// selection sort by Markimark aka GiorDior aka Giorgio
// first project made in SDL2

#include "ArraysSys.hpp"
#include <iostream>
#include <SDL2/SDL.h>

const int screenHeight = 800;
const int screenWidth = 1500;

// rendering the array to the sceen
void renderArray(SDL_Renderer * renderer, int array[], int length, int color[], int specialIndexes[] = {}){
    // clearing the screen
    SDL_SetRenderDrawColor(renderer, 0, 0, 0, 255);
    SDL_RenderClear(renderer);

    SDL_Rect rect;
    // gap between the screen and the highest val in the array
    int gap = 100;
    // highest val in the array
    float maxVal = 100.0;
    for (int i = 0; i < length; i++){
        // value of the current element
        int val = array[i];
        // calcualting its height depending on the value
        float percentage = (val/maxVal);
        float elementWidth = screenWidth/length - 1; 
        float elementHeight = percentage * (screenHeight - gap);

        // element rect information
        rect.x = i * elementWidth + i;
        rect.y = screenHeight - elementHeight;
        rect.w = elementWidth;
        rect.h = elementHeight;

        // setting the color
        SDL_SetRenderDrawColor(renderer, color[0], color[1], color[2], 255);
        // giving special elements a different color
        for (int j = 0; j < 3; j++)
        {
            if (specialIndexes[j] == i){
                SDL_SetRenderDrawColor(renderer, 255, 0, 0, 255);
            }
        }
        
        // rendering the element
        SDL_RenderFillRect(renderer, &rect);
    }
    // update the screen
    SDL_RenderPresent(renderer);
}

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
            renderArray(renderer, array, length, color, specialIndexes);
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
    renderArray(renderer, unsortedArray, arrayLength, color, specialIndex);
    
    // program continues to run after the sort is done
    while (true){
        quitEvent(event);
    }
    return 0;
}