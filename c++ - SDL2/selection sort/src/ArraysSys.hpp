#ifndef ARRAYSYS_HPP
#define ARRAYSYS_HPP
#include <iostream>
#include <time.h>
#include <SDL2/SDL.h>

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
