def bell_number(n):
    """
    Calculate the Bell number for a set of size n.

    The Bell number is the number of ways to partition a set of n elements
    into non-empty subsets.

    Parameters:
    n (int): The number of elements in the set.

    Returns:
    int: The Bell number for the set.
    """
    # Create a 2D array to store the Bell numbers.
    bell = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

    # Bell(0, 0) is 1
    bell[0][0] = 1

    # Fill the table using the recurrence relation.
    for i in range(1, n + 1):
        # Explicitly put Bell(i, 0).
        bell[i][0] = bell[i - 1][i - 1]

        # Fill for remaining values of j.
        for j in range(1, i + 1):
            bell[i][j] = bell[i - 1][j - 1] + bell[i][j - 1]

    return bell[n][0]


if __name__ == "__main__":
    n = int(input("Enter the number of elements in the set: "))
    print(
        f"The number of partitions of a set with {n} elements (Bell number) is: {bell_number(n)}"
    )


