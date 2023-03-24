"""
File: stats.py
Computes the median and mode of a set of numbers.

"""
from collections import Counter


def mode(numbers):
    """Computes the mode of a list of numbers."""
    if not numbers:
        return 0
    count = Counter(numbers)
    return count.most_common(1)[0][0]


def median(numbers):
    """Computes the median of a list of numbers."""
    if not numbers:
        return 0
    sorted_numbers = sorted(numbers)
    n = len(numbers)
    if n % 2 == 0:
        return (sorted_numbers[n//2-1] + sorted_numbers[n//2]) / 2
    else:
        return sorted_numbers[n//2]
    
def mean(numbers):
    """Computes the average of a set of numbers."""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

    
def main():
    """Tests the mean, median, and mode functions with the given list."""
    numbers = [45,66, 22, 10, 15, 88, 15, 31, 90]
    print(f"Numbers: {numbers}")
    print(f"The Mode is {mode(numbers)}")
    print(f"The Median is {median(numbers)}")
    print(f"The Mean is {mean(numbers)}")


if __name__ == '__main__':
    main()
