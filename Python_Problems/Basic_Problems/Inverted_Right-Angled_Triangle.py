def inverted_right_angled_triangle(n):
    for i in range(n, 0, -1):
        print('* ' * i)
inverted_right_angled_triangle(5)   

# | Part | Meaning                        |
# | ---- | ------------------------------ |
# | `n`  | Start value                    |
# | `0`  | Stop value (0 is NOT included) |
# | `-1` | Step (decreasing by 1)         |
