import matplotlib.pyplot as plt
import numpy as np
import time

# Helper function to draw the current state of the array
def draw_array(arr, colors, title):
    plt.bar(range(len(arr)), arr, color=colors)
    plt.title(title)
    plt.show(block=False)
    plt.pause(0.01)
    plt.clf()

# Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    step_counter = 0
    colors = ['blue'] * n
    explanation = "Tauscht wiederholt benachbarte Elemente, wenn sie in der falschen Reihenfolge sind."
    for i in range(n):
        for j in range(0, n-i-1):
            step_counter += 1
            colors[j] = 'red'
            colors[j+1] = 'red'
            draw_array(arr, colors, f'Bubble Sort\n{explanation}\nSchritte: {step_counter}')
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            colors[j] = 'blue'
            colors[j+1] = 'blue'
        colors[n-i-1] = 'green'
    draw_array(arr, colors, f'Bubble Sort - Sortiert\n{explanation}\nSchritte: {step_counter}')

def bubble_sort_alg(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            
def insertion_sort_alg(arr):
    n = len(arr)
    for i in range(1, n):
        j = i - 1
        while j >= 0 and arr[i] < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = arr[i]

# Insertion Sort
def insertion_sort(arr):
    n = len(arr)
    step_counter = 0
    colors = ['blue'] * n
    explanation = "Sortiert Element für Element, indem es wiederholt das nächste Element auswählt und an der richtigen Stelle einfügt."
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        colors[i] = 'red'
        step_counter += 1
        draw_array(arr, colors, f'Insertion Sort\n{explanation}\nSchritte: {step_counter}')
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            colors[j] = 'red'
            step_counter += 1
            draw_array(arr, colors, f'Insertion Sort\n{explanation}\nSchritte: {step_counter}')
            colors[j] = 'blue'
            j -= 1
        arr[j + 1] = key
        colors[i] = 'blue'
    colors = ['green'] * n
    draw_array(arr, colors, f'Insertion Sort - Sortiert\n{explanation}\nSchritte: {step_counter}')

def insertion_sort_alg(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        
# Selection Sort
def selection_sort(arr):
    n = len(arr)
    step_counter = 0
    colors = ['blue'] * n
    explanation = "Wählt wiederholt das kleinste verbleibende Element aus und tauscht es mit dem ersten unsortierten Element."
    for i in range(n):
        min_idx = i
        colors[i] = 'red'
        for j in range(i+1, n):
            colors[j] = 'red'
            step_counter += 1
            draw_array(arr, colors, f'Selection Sort\n{explanation}\nSchritte: {step_counter}')
            if arr[min_idx] > arr[j]:
                min_idx = j
            colors[j] = 'blue'
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        colors[min_idx] = 'blue'
        colors[i] = 'green'
    draw_array(arr, colors, f'Selection Sort - Sortiert\n{explanation}\nSchritte: {step_counter}')

# Quick Sort
def quick_sort(arr, low, high, draw_array, explanation, colors, step_counter):
    if low < high:
        pi, step_counter = partition(arr, low, high, draw_array, explanation, colors, step_counter)
        step_counter = quick_sort(arr, low, pi-1, draw_array, explanation, colors, step_counter)
        step_counter = quick_sort(arr, pi+1, high, draw_array, explanation, colors, step_counter)
    return step_counter

def partition(arr, low, high, draw_array, explanation, colors, step_counter):
    i = low - 1
    pivot = arr[high]
    colors[high] = 'yellow'
    for j in range(low, high):
        colors[j] = 'red'
        step_counter += 1
        draw_array(arr, colors, f'Quick Sort\n{explanation}\nSchritte: {step_counter}')
        if arr[j] < pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
            colors[i] = 'green'
        colors[j] = 'blue'
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    colors[high] = 'blue'
    colors[i + 1] = 'green'
    draw_array(arr, colors, f'Quick Sort\n{explanation}\nSchritte: {step_counter}')
    return i + 1, step_counter

# Main function to execute sorting and visualize
def visualize_sorting():
    n = 40
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
    #plt.clf()
    #selection_sort(arr_copy2)
    #time.sleep(1)
    
    # Quick Sort
    plt.clf()
    explanation = "Teilt das Array in kleinere Teilarrays um ein Pivot-Element auf und sortiert die Teilarrays rekursiv."
    colors = ['blue'] * len(arr_copy3)
    step_counter = 0
    step_counter = quick_sort(arr_copy3, 0, len(arr_copy3)-1, draw_array, explanation, colors, step_counter)
    colors = ['green'] * len(arr_copy3)
    draw_array(arr_copy3, colors, f'Quick Sort - Sortiert\n{explanation}\nSchritte: {step_counter}')
    time.sleep(10)
    plt.show()

if __name__ == "__main__":
    visualize_sorting()
