def longDivision(dividend, divisor):
    """
    Performs long division on the given `dividend` and `divisor`.

    Args:
        dividend (int): The number to be divided.
        divisor (int): The number by which the `dividend` is divided.

    Returns:
        dict: A dictionary with two keys:
            - 'quot' (int): The quotient, which is the result of the division.
            - 'rem' (int): The remainder, which is the leftover after division.

    Raises:
        ValueError: If the `divisor` is 0, indicating division by zero.

    Example:
        >>> longDivision(12345, 7)
        {'quot': 1763, 'rem': 4}

        This means 12345 divided by 7 gives a quotient of 1763 and a remainder of 4.
    """

    # Check if the divisor is zero and raise an error
    #
    # Division by zero is undefined, so we handle this edge case.
    if divisor == 0:
        raise ValueError("Division by zero error")

    # If the divisor is 1, return the dividend itself as the quotient, and 0 as the remainder
    #
    # Dividing by 1 returns the number unchanged, so no calculation is needed.
    if divisor == 1:
        return {"quot": dividend, "rem": 0}

    # Convert the dividend (number to be divided) into a list of digits (as strings)
    #
    # Example: 12345 becomes ['1', '2', '3', '4', '5']
    #
    # This will allow us to process each digit of the number individually.
    digits = list(str(dividend))

    # Initialize result and carry for the quotient and remainder process
    result = 0
    carry = 0

    # Loop through each digit in the list of digits
    for digit in digits:
        # Update carry by "shifting" the current value and adding the next digit
        carry = carry * 10 + int(digit)

        # Now we need to determine how many times we can subtract the divisor from `carry`.
        #
        # We initialize `count` to 0, which will store how many times the divisor fits into carry.
        count = 0

        # Subtract divisor from carry as many times as possible
        #
        # We repeatedly subtract the divisor from the carry until the carry is less than the divisor.
        #
        # This gives us the count of how many times the divisor fits into the carry.
        while carry >= divisor:
            carry -= divisor
            count += 1

        # Update result (quotient) by shifting it and adding count
        result = result * 10 + count

    return {"quot": result, "rem": carry}


print(longDivision(6894, 23))
