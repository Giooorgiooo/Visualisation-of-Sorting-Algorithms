#ifndef ARRAYSYS_HPP
#define ARRAYSYS_HPP
#include <iostream>
#include <time.h>
#include <SDL2/SDL.h>

// rendering the array to the sceen
void renderArray(float screenWidth, float screenHeight, SDL_Renderer * renderer, int array[], int length, int color[], int specialIndexes[] = {}){
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

// exiting the application in case the user quits
void quitEvent(SDL_Event event){
    if (SDL_PollEvent(&event)){
        switch(event.type){
            case SDL_QUIT:
                exit(0);
        }
    }
}

// returning a random number from min to max
int randint(int min, int max){
    srand (time(NULL));
    return min + (rand() % static_cast<int>(max - min + 1));
}

// class, which creates, shuffles, prints arrays and swaps
// 2 elements
class ArraySystem{
    public:
        void swap(int *firstElement, int *secondElement);
        void print(int array[], int size);
        void add(int array[], int min, int max);
        void shuffle(int array[], int length);
};

// swapping to elements
void ArraySystem::swap(int *firstElement, int *secondElement){
    int temp = *firstElement;
    *firstElement = *secondElement;
    *secondElement = temp;
}

// adding numbers to an array in a specific range
void ArraySystem::add(int array[], int min, int max){
    for (int i = min; i < max; i++){
        array[i] = i;
    }
    array[0] = 0;
}   

// shuffling the array
void ArraySystem::shuffle(int array[], int length){
    for (int i = 0; i < length; i++){
        swap(&array[i], &array[randint(i + 1, length)]);
    }
}

// printing the array to the terminal
void ArraySystem::print(int array[], int length){
    for (int i = 0; i < length; i++){
        std::cout << i << " | " << array[i] << "\n";
    }
}

#endif 
