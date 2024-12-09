import random
import math
import matplotlib.pyplot as plt

# Step 1: Generate a list of K random numbers within limit N
def generate_random_numbers(K, N):
    if K < 10:
        raise ValueError("Minimum value of K should be 10.")
    return [random.randint(1, N) for _ in range(K)]

# Step 2: Check if a number is prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

# Step 3: Separate prime and composite numbers
def separate_primes_and_composites(numbers):
    primes = [num for num in numbers if is_prime(num)]
    composites = [num for num in numbers if num > 1 and not is_prime(num)]
    return primes, composites

# Step 4: Compute squares of primes and square roots of composites
def compute_squares_and_roots(primes, composites):
    prime_squares = [num ** 2 for num in primes]
    composite_roots = [math.sqrt(num) for num in composites]
    return prime_squares, composite_roots

# Step 5: Scatter plots
def plot_data(primes, prime_squares, composites, composite_roots):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    # Scatter plot for primes vs their squares
    ax1.scatter(primes, prime_squares, color='blue', label='Prime Squares')
    ax1.set_title("Prime Numbers vs Their Squares")
    ax1.set_xlabel("Prime Numbers")
    ax1.set_ylabel("Squares")
    ax1.legend()

    # Scatter plot for composites vs their square roots
    ax2.scatter(composites, composite_roots, color='green', label='Composite Roots')
    ax2.set_title("Composite Numbers vs Their Square Roots")
    ax2.set_xlabel("Composite Numbers")
    ax2.set_ylabel("Square Roots")
    ax2.legend()

    plt.tight_layout()
    plt.show()

# Main script
try:
    # Input from the user
    K = int(input("Enter the number of random numbers (K, minimum 10): "))
    N = int(input("Enter the upper limit (N): "))

    # Generate random numbers
    numbers = generate_random_numbers(K, N)
    print(f"Generated List: {numbers}")

    # Separate primes and composites
    primes, composites = separate_primes_and_composites(numbers)
    print(f"Primes: {primes}")
    print(f"Composites: {composites}")

    # Compute squares and roots
    prime_squares, composite_roots = compute_squares_and_roots(primes, composites)

    # Plot the results
    plot_data(primes, prime_squares, composites, composite_roots)

except ValueError as e:
    print(e)
