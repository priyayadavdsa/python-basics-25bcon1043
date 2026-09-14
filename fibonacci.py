def fibonacci(term_count):
    sequence = []
    current_term, next_term = 0, 1
    for _ in range(term_count):
        sequence.append(current_term)
        current_term, next_term = next_term, current_term + next_term
    return sequence


if __name__ == "__main__":
    term_count = 8
    print(f"Fibonacci sequence ({term_count} terms): {fibonacci(term_count)}")
