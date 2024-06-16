import matplotlib.pyplot as plt
import numpy as np
import time

# Helper function to draw the current state of the array
def draw_array(arr, colors, title):
    plt.bar(range(len(arr)), arr, color=colors)
    plt.title(title)
    plt.show(block=False)
    plt.pause(0.1)
    plt.clf()

# Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    colors = ['blue'] * n
    explanation = "Bubble Sort: Repeatedly swaps adjacent elements if they are in the wrong order."
    for i in range(n):
        for j in range(0, n-i-1):
            colors[j] = 'red'
            colors[j+1] = 'red'
            draw_array(arr, colors, f'Bubble Sort\n{explanation}')
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            colors[j] = 'blue'
            colors[j+1] = 'blue'
        colors[n-i-1] = 'green'
    draw_array(arr, colors, f'Bubble Sort - Sorted\n{explanation}')

# Insertion Sort
def insertion_sort(arr):
    n = len(arr)
    colors = ['blue'] * n
    explanation = "Insertion Sort: Builds the sorted array one item at a time by repeatedly picking the next item and inserting it into its correct position."
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        colors[i] = 'red'
        draw_array(arr, colors, f'Insertion Sort\n{explanation}')
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            colors[j] = 'red'
            draw_array(arr, colors, f'Insertion Sort\n{explanation}')
            colors[j] = 'blue'
            j -= 1
        arr[j + 1] = key
        colors[i] = 'blue'
    colors = ['green'] * n
    draw_array(arr, colors, f'Insertion Sort - Sorted\n{explanation}')

# Selection Sort
def selection_sort(arr):
    n = len(arr)
    colors = ['blue'] * n
    explanation = "Selection Sort: Repeatedly selects the smallest remaining element and swaps it with the first unsorted element."
    for i in range(n):
        min_idx = i
        colors[i] = 'red'
        for j in range(i+1, n):
            colors[j] = 'red'
            draw_array(arr, colors, f'Selection Sort\n{explanation}')
            if arr[min_idx] > arr[j]:
                min_idx = j
            colors[j] = 'blue'
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        colors[min_idx] = 'blue'
        colors[i] = 'green'
    draw_array(arr, colors, f'Selection Sort - Sorted\n{explanation}')

# Quick Sort
def quick_sort(arr, low, high, draw_array, explanation, colors):
    if low < high:
        pi = partition(arr, low, high, draw_array, explanation, colors)
        quick_sort(arr, low, pi-1, draw_array, explanation, colors)
        quick_sort(arr, pi+1, high, draw_array, explanation, colors)

def partition(arr, low, high, draw_array, explanation, colors):
    i = low - 1
    pivot = arr[high]
    colors[high] = 'yellow'
    for j in range(low, high):
        colors[j] = 'red'
        draw_array(arr, colors, f'Quick Sort\n{explanation}')
        if arr[j] < pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
            colors[i] = 'green'
        colors[j] = 'blue'
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    colors[high] = 'blue'
    colors[i + 1] = 'green'
    draw_array(arr, colors, f'Quick Sort\n{explanation}')
    return i + 1

# Main function to execute sorting and visualize
def visualize_sorting():
    n = 20
    arr = np.random.randint(1, 100, n)
    arr_copy1 = arr.copy()
    arr_copy2 = arr.copy()
    arr_copy3 = arr.copy()

    plt.ion()
    plt.figure(figsize=(10, 6))

    # Bubble Sort
    bubble_sort(arr)
    time.sleep(1)
    
    # Insertion Sort
    plt.clf()
    insertion_sort(arr_copy1)
    time.sleep(1)
    
    # Selection Sort
    plt.clf()
    selection_sort(arr_copy2)
    time.sleep(1)
    
    # Quick Sort
    plt.clf()
    explanation = "Quick Sort: Divides the array into smaller sub-arrays around a pivot and recursively sorts the sub-arrays."
    colors = ['blue'] * len(arr_copy3)
    quick_sort(arr_copy3, 0, len(arr_copy3)-1, draw_array, explanation, colors)
    colors = ['green'] * len(arr_copy3)
    draw_array(arr_copy3, colors, f'Quick Sort - Sorted\n{explanation}')
    time.sleep(1)
    
    plt.ioff()
    plt.show()

if __name__ == "__main__":
    visualize_sorting()
