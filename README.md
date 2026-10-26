# Bug Fixing Using Cursor AI

This learning project shows a buggy program and a corrected version. It is designed to help explain the debugging process during an assessment.

## Files
- `buggy_example.py`: contains intentional bugs
- `fixed_program.py`: corrected implementation

## Run the fixed program
```bash
python fixed_program.py
```

## Bugs to identify in the example
1. The loop stops before processing the last item.
2. The average divides by the total instead of the number of items.
3. Empty input can cause division by zero.

## Fixes
- Iterate over every value
- Divide the total by the number of values
- Check for an empty list before calculating the average

You can open this folder in Cursor AI and ask it to identify and explain the bugs. Review the suggestions and compare them with `fixed_program.py`.
