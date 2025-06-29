"""
Example of a simple Python file that Setta will be able to run.
"""


def calculate_fibonacci(n):
    """Calculate the nth Fibonacci number."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b


def process_data(data):
    """Example data processing function."""
    result = []
    for item in data:
        processed = {
            "original": item,
            "squared": item**2,
            "is_even": item % 2 == 0,
            "fibonacci": calculate_fibonacci(item),
        }
        result.append(processed)
    return result


# Example usage
if __name__ == "__main__":
    print("Simple Python Example for Setta")
    print("=" * 40)

    # Some example data
    numbers = [1, 2, 3, 5, 8, 13, 21]

    print(f"Processing numbers: {numbers}")
    results = process_data(numbers)

    for r in results:
        print(f"\nNumber: {r['original']}")
        print(f"  Squared: {r['squared']}")
        print(f"  Is even: {r['is_even']}")
        print(f"  Fibonacci: {r['fibonacci']}")

    print("\n" + "=" * 40)
    print("In production, Setta will:")
    print("1. Find this code and other Python files")
    print("2. Provide a web UI to interact with your functions")
    print("3. Handle all the web serving complexity")
    print("4. Let users run your code through the browser")
