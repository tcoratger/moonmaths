def binaryRepresentation(n, bits=32):
    """
    Converts an integer `n` into its binary representation using bitwise operations.

    Args:
    n (int): The number to be converted.
    bits (int): The number of bits to represent (default is 32 bits).

    Returns:
    str: A binary string representation of the number.

    Explanation:
    - The function initializes `binary_str` to "0" to account for leading zeros.
    - It loops from the highest bit down to 0, checking if each bit is set.
    - The ith bit is checked using the expression `n & (1 << i)`.
      This uses a left shift to create a mask for the ith bit, then bitwise AND (`&`) to check whether that bit in `n` is 1 or 0.
    - If the bit is 1, '1' is added to `binary_str`; otherwise, '0' is added.

    Example:
    Suppose n = 110110001000001 (binary: 0b110110001000001).
    The function will check each bit starting from bit 32 down to 0.
    If n = 0b00000000000000000110110001000001:
      - For bits 32 to 15: All bits are 0.
      - From bit 14: The first 1 is encountered.
      - Continue checking all bits until bit 0 is reached.
    """

    # Initialize the result string with "0"
    # This will eventually hold the binary representation of the number
    binary_str = "0"

    # Loop from number of bits down to 0.
    for i in range(bits, -1, -1):
        # Use bitwise AND to check if the ith bit of n is set to 1
        #
        # `1 << i` shifts 1 to the ith bit position.
        #
        # The bitwise AND `n & (1 << i)` checks if the ith bit of `n` is 1.
        if n & (1 << i):
            # If the ith bit is 1, append '1' to the binary string
            binary_str += "1"
        else:
            # If the ith bit is 0, append '0' to the binary string
            binary_str += "0"

    # Return the full binary string
    return binary_str


print(binaryRepresentation(27713))
