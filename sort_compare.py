import time
import random


def get_me_random_list(n):
    """Generate a list of n elements in random order please."""
    a_list = list(range(n))
    random.shuffle(a_list)
    return a_list



def insertion_sort(a_list):
    """Perform Insertion Sort."""
    for i in range(1, len(a_list)):
        key = a_list[i]
        j = i - 1
        while j >= 0 and key < a_list[j]:
            a_list[j + 1] = a_list[j]
            j -= 1
        a_list[j + 1] = key
    return a_list


def shell_sort(a_list):
    """Perform Shell Sort."""
    n = len(a_list)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = a_list[i]
            j = i
            while j >= gap and a_list[j - gap] > temp:
                a_list[j] = a_list[j - gap]
                j -= gap
            a_list[j] = temp
        gap //= 2
    return a_list

def python_sort(a_list):
    """Wrapper for Python's built-in sort."""
    a_list.sort()
    return a_list

def average_sort_time(sort_func, size):
    """Calculate average time taken by the sort function."""
    total_time = 0
    for _ in range(100):
        mylist = get_me_random_list(size)
        start = time.time()
        sort_func(mylist)
        total_time += time.time() - start
    
    return total_time / 100

def main():
    list_sizes = [500, 1000, 5000]

    for size in list_sizes:
        avg_time_insertion = average_sort_time(insertion_sort, size)
        avg_time_shell = average_sort_time(shell_sort, size)
        avg_time_python = average_sort_time(python_sort, size)

        print(f"\nList Size: {size}")
        print(f"Insertion Sort took {avg_time_insertion:10.7f} seconds to run, on average")
        print(f"Shell Sort took {avg_time_shell:10.7f} seconds to run, on average")
        print(f"Python Sort took {avg_time_python:10.7f} seconds to run, on average")

print("Python Sort took")
if __name__ == "__main__":
    main()
