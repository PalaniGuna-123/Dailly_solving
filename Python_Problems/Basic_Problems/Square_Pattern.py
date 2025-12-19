def square_pattern(rows: int) -> None:
    for i in range(rows):
        print("* " * rows)

square_pattern(5)

# | Part | Meaning                        |
# | ---- | ------------------------------ |
# | `rows` | Number of rows in the square pattern |
# | `*`  | Character to print             |         

def square(rows: int) -> None:
    for i in range(rows):
        print("*" * rows )
square(8)