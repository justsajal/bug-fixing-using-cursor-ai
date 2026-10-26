# Intentionally buggy code for a debugging exercise.
def calculate_average(numbers):
    total = 0
    for index in range(0, len(numbers) - 1):  # Bug: skips the last item
        total += numbers[index]
    average = total / total  # Bug: wrong denominator; also fails when total is zero
    return average


values = [10, 20, 30]
print("Average:", calculate_average(values))
