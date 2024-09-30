import time
import random

def get_me_random_list(n):
    """Generate a list of n elements in random order."""
    a_list = list(range(n))  # Create a list from 0 to n-1
    random.shuffle(a_list)  # Shuffle it up for randomness
    return a_list

def sequential_search(a_list, item):
    """Simple linear search, checking each item."""
    pos = 0
    found = False

    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
            pos += 1  # Move to the next position

    return found

def ordered_sequential_search(a_list, item):
    """Search through a sorted list. Stop if we go past the item."""
    pos = 0
    found = False
    stop = False
    while pos < len(a_list) and not found and not stop:
        if a_list[pos] == item:
            found = True  
            if a_list[pos] > item:
                stop = True  
            else:
                pos += 1  # Keep going

    return found

def binary_search_iterative(a_list, item):
    """Binary search using a loop. Fast if the list is sorted."""
    first = 0
    last = len(a_list) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2  # Find the middle point
        if a_list[midpoint] == item:
            found = True  # Found it!
        else:
            if item < a_list[midpoint]:
                last = midpoint - 1  # Search left
            else:
                first = midpoint + 1  # Search right

    return found

def binary_search_recursive(a_list, item):
    """Binary search using recursion. It’s elegant but uses more memory."""
    if len(a_list) == 0:
        return False  #  empty list means not found
    else:
        midpoint = len(a_list) // 2
        if a_list[midpoint] == item:
            return True  # Found it
        else:
            if item < a_list[midpoint]:
                return binary_search_recursive(a_list[:midpoint], item)  # Search left
            else:
                return binary_search_recursive(a_list[midpoint + 1:], item)  # Search right

def average_search_time(search_func, size, target):
    """Run the search function 100 times and calculate average time."""
    total_time = 0
    for _ in range(100):
        mylist = get_me_random_list(size)  # Generate random list
        sorted_list = sorted(mylist)  # Sort the list for search functions that need it

        start = time.time()  # Start timing
        search_func(sorted_list, target)  # Run the search
        total_time += time.time() - start  # Calculate elapsed time
    
    return total_time / 100  # Return average time

if __name__ == "__main__":
    """Main entry point."""
    list_sizes = [500, 1000, 5000]  # Different sizes to test
    target = 99999999  # Something we know won't be in the list (worst case)

    for size in list_sizes:
        # Run each search function and get the average time
        avg_time_sequential = average_search_time(sequential_search, size, target)
        avg_time_ordered = average_search_time(ordered_sequential_search, size, target)
        avg_time_binary_iterative = average_search_time(binary_search_iterative, size, target)
        avg_time_binary_recursive = average_search_time(binary_search_recursive, size, target)

        # Print the results in a nice format
        print(f"\nList Size: {size}")
        print(f"Sequential Search took {avg_time_sequential:10.7f} seconds to run, on average")
        print(f"Ordered Sequential Search took {avg_time_ordered:10.7f} seconds to run, on average")
        print(f"Binary Search Iterative took {avg_time_binary_iterative:10.7f} seconds to run, on average")
        print(f"Binary Search Recursive took {avg_time_binary_recursive:10.7f} seconds to run, on average")
