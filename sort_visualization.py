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
    for i in range(n):
        for j in range(0, n-i-1):
            colors[j] = 'red'
            colors[j+1] = 'red'
            draw_array(arr, colors, 'Bubble Sort')
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            colors[j] = 'blue'
            colors[j+1] = 'blue'
        colors[n-i-1] = 'green'
    draw_array(arr, colors, 'Bubble Sort - Sorted')

# Insertion Sort
def insertion_sort(arr):
    n = len(arr)
    colors = ['blue'] * n
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        colors[i] = 'red'
        draw_array(arr, colors, 'Insertion Sort')
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            colors[j] = 'red'
            draw_array(arr, colors, 'Insertion Sort')
            colors[j] = 'blue'
            j -= 1
        arr[j + 1] = key
        colors[i] = 'blue'
    colors = ['green'] * n
    draw_array(arr, colors, 'Insertion Sort - Sorted')

# Selection Sort
def selection_sort(arr):
    n = len(arr)
    colors = ['blue'] * n
    for i in range(n):
        min_idx = i
        colors[i] = 'red'
        for j in range(i+1, n):
            colors[j] = 'red'
            draw_array(arr, colors, 'Selection Sort')
            if arr[min_idx] > arr[j]:
                min_idx = j
            colors[j] = 'blue'
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        colors[min_idx] = 'blue'
        colors[i] = 'green'
    draw_array(arr, colors, 'Selection Sort - Sorted')

# Main function to execute sorting and visualize
def visualize_sorting():
    n = 20
    arr = np.random.randint(1, 100, n)
    arr_copy1 = arr.copy()
    arr_copy2 = arr.copy()

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
    
    plt.ioff()
    plt.show()

if __name__ == "__main__":
    visualize_sorting()

