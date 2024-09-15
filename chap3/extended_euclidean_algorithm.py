def euclideanAlgorithm(a, b):
    """
    The Euclidean algorithm is a way to find the greatest common divisor (GCD) of two numbers.

    This is basically a continuous process of dividing the larger number by the smaller number and then replacing the larger number with the remainder.

    The process is repeated until the remainder is 0, at which point the divisor is the GCD.

    Let us take an example to understand the algorithm. We have two numbers, 102 and 38. The GCD can be found as follows:
        102 = 38 * 2 + 26
        38 = 26 * 1 + 12
        26 = 12 * 2 + 2
        12 = 2 * 6 + 0

    The GCD is 2 because it is the last non-zero remainder.
    """
    if b == 0:
        return a

    return euclideanAlgorithm(b, a % b)


print(euclideanAlgorithm(102, 38))  # Output: 2


def extendedEuclideanAlgorithm(a, b):
    """
    The Euclidean algorithm is a way to find the greatest common divisor (GCD) of two numbers.

    The extended Euclidean algorithm is an extension of the Euclidean algorithm, and it computes not only the GCD of two numbers but also the coefficients of Bézout's identity:
        a.x + b.y = gcd(a, b)

    For example, given a = 55 and b = 80, the GCD is 5, and the coefficients are x = 3 and y = -2 such that:
        55 * 3 + 80 * (-2) = 5

    Let us demonstrate the extended Euclidean algorithm. Let us assume we found the coefficients (x1, y1) for (b, a mod b):
        b.x1 + (a mod b).y1 = gcd(b, a mod b)

    We want to find the coefficients (x, y) for (a, b):
        a.x + b.y = gcd(a, b)

    We know that a mod b can be rewritten as:
        a mod b = a - (a // b) * b where // is the integer division operator

    Substituting this into the equation above, we get:
        b.x1 + (a - (a // b) * b).y1 = gcd(b, a mod b)

    Simplifying this, we get:
        gcd(b, a mod b) = a.y1 + b.(x1 - (a // b) * y1)

    We can now identify the coefficients (x, y) for (a, b) as:
        x = y1
        y = x1 - (a // b) * y1

    This function implements the Extended Euclidean Algorithm to compute:
        1. The greatest common divisor (GCD) of two numbers a and b.
        2. The coefficients (x, y) such that a * x + b * y = gcd(a, b), which is known as Bézout's identity.

        The algorithm works recursively by reducing the problem at each step and eventually finding the GCD.
    """

    # Base case: If 'a' is 0, then the GCD is 'b', and the Bézout coefficients are (0, 1),
    # because b * 1 + 0 * 0 = b, which gives us the GCD as 'b'.
    if a == 0:
        return b, 0, 1

    # Recursive step: Calculate the GCD of 'b % a' and 'a'.
    #
    # This follows the recursive structure of the Euclidean algorithm, which says:
    # gcd(a, b) = gcd(b % a, a).
    #
    # It also finds the Bézout coefficients (x1, y1) for the smaller problem.
    gcd, x1, y1 = extendedEuclideanAlgorithm(b % a, a)

    # Using the Bézout coefficients (x1, y1) from the smaller problem to compute the new coefficients (x, y):
    #
    # From the recursive structure:
    # a * x + b * y = gcd(a, b), we can deduce:
    # x = y1 (from the recursive call),
    # y = x1 - (b // a) * y1 (this formula comes from rearranging terms in the identity involving mod and quotient).
    x = y1 - (b // a) * x1  # Update x based on the recursive result.
    y = x1  # Update y based on the recursive result.

    # Return the GCD and the Bézout coefficients (x, y).
    return gcd, x, y


print(extendedEuclideanAlgorithm(1914, 899))  # Output: (29, 8, -17)
print(extendedEuclideanAlgorithm(45, 10))  # Output: (5, 1, -4)
print(extendedEuclideanAlgorithm(13, 11))  # Output: (1, -5, 6)
print(extendedEuclideanAlgorithm(13, 12))  # Output: (1, 1, -1)
