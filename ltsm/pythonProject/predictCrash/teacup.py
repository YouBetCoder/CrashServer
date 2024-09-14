def detect_enders_teacup(numbers):
    """Detects the 'Ender's Teacup' pattern in a list of numbers, ensuring in-order.

    Args:
      numbers: A list of numbers.

    Returns:
      True if the pattern is detected, False otherwise.
    """

    # Check for sufficient length
    if len(numbers) < 4:
        return False

    # Extract large and small numbers
    large_numbers = numbers[:2]
    small_numbers = numbers

    # # Check if large numbers are greater than 30
    # if not all(num > 10 for num in large_numbers):
    #     return False

    # Check if small numbers are between 1 and 2
    if not all(1 <= num <= 2 for num in small_numbers):
        return False

    # Check for descending order
    if not all(numbers[i] >= numbers[i + 1] for i in range(len(numbers) - 1)):
        return False

    return True
