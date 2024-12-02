from collections import Counter

def calculate_total_absolute_difference(file_path):
   
    try:       
        with open(file_path, "r") as file:            
            tokens = file.read().split()
        
        numbers = [int(token) for token in tokens]

        left = numbers[::2]   # Even indices: 0, 2, 4, ...
        right = numbers[1::2] # Odd indices: 1, 3, 5, ...

        left_sorted = sorted(left)
        right_sorted = sorted(right)

        if len(left_sorted) != len(right_sorted):
            raise ValueError("The 'left' and 'right' lists have different lengths.")

        total_abs_diff = sum(abs(l - r) for l, r in zip(left_sorted, right_sorted))

        return total_abs_diff, left_sorted, right_sorted

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except ValueError as ve:
        print(f"Value Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def calculate_sim(left, right):    
    right_counter = Counter(right)
    sim = 0
    for element in left:
        if element in right_counter:
            sim += element * right_counter[element]

    return sim