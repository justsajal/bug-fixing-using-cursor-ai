"""Corrected average calculator with basic input validation."""


def calculate_average(numbers: list[float]) -> float:
    """Return the arithmetic mean of a non-empty list of numbers."""
    if not numbers:
        raise ValueError("Cannot calculate an average for an empty list.")

    return sum(numbers) / len(numbers)


def main() -> None:
    values = [10, 20, 30]
    print("Values:", values)
    print("Average:", calculate_average(values))


if __name__ == "__main__":
    main()
