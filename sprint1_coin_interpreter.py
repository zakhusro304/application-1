"""
IT 3883 Final Exam - Sprint 1
Coin Interpreter: Converts pseudo-English coin descriptions to dollar amounts.
Author: Student
"""

# --- Coin value definitions (in cents) ---
COIN_VALUES = {
    "penny":   1,
    "pennies": 1,
    "nickel":  5,
    "nickels": 5,
    "dime":    10,
    "dimes":   10,
    "quarter": 25,
    "quarters": 25,
}


def parse_coin_sentence(sentence):
    """
    Parses a pseudo-English sentence describing coins and returns
    the total value in dollars.

    Expected input format (examples):
        "1 penny and 2 nickels"
        "4 dimes and 7 quarters"
        "21 pennies and 17 dimes and 52 quarters"

    Returns:
        float: total value in dollars, or None if input is invalid.
    """

    # Convert to lowercase and split into words
    words = sentence.lower().split()

    total_cents = 0      # Running total in cents
    i = 0                # Word index pointer

    while i < len(words):
        word = words[i]

        # Skip connector words like "and"
        if word == "and":
            i += 1
            continue

        # Expect a numeral at this position
        if word.isdigit():
            quantity = int(word)
            i += 1

            # The next word should be a coin denomination
            if i < len(words) and words[i] in COIN_VALUES:
                denomination = words[i]
                coin_value = COIN_VALUES[denomination]
                total_cents += quantity * coin_value
                i += 1
            else:
                # Found a number but no valid denomination after it
                print(f"  Warning: expected a coin name after '{quantity}', got '{words[i] if i < len(words) else 'end of input'}'")
                return None
        else:
            # Unexpected word found
            print(f"  Warning: unexpected token '{word}' at position {i}")
            return None

    # Convert cents to dollars
    total_dollars = total_cents / 100.0
    return total_dollars


def main():
    """
    Main function: prompts the user for coin sentences and prints dollar totals.
    Type 'quit' to exit.
    """

    print("=== Coin Interpreter ===")
    print("Enter a coin description (e.g. '1 penny and 2 nickels') or 'quit' to exit.\n")

    while True:
        sentence = input("Enter sentence: ").strip()

        if sentence.lower() == "quit":
            print("Goodbye!")
            break

        if not sentence:
            print("  (empty input, try again)")
            continue

        result = parse_coin_sentence(sentence)

        if result is not None:
            print(f"  Result: ${result:.2f}\n")
        else:
            print("  Could not parse that sentence. Please check your input.\n")


# --- Run tests automatically when the file is executed directly ---
if __name__ == "__main__":
    # Sprint 1 test cases (from assignment)
    test_cases = [
        ("1 penny and 2 nickels",                              0.11),
        ("4 dimes and 7 quarters",                             2.15),
        ("1 quarter and 3 pennies",                            0.28),
        ("21 pennies and 17 dimes and 52 quarters",            14.91),
        ("95 dimes and 73 quarters and 22 nickels and 36 pennies", 29.21),
        ("1 nickel and 17 quarters",                           4.30),
        ("21 nickels and 15 pennies",                          1.20),
        ("1 dime and 1 nickel and 1 penny and 1 quarter",      0.41),
        # Additional test cases
        ("1 quarter",                                          0.25),
        ("100 pennies",                                        1.00),
        ("0 dimes and 1 nickel",                               0.05),
    ]

    print("=== Sprint 1 Test Run ===\n")
    passed = 0
    failed = 0

    for sentence, expected in test_cases:
        result = parse_coin_sentence(sentence)
        status = "PASS" if result is not None and round(result, 2) == round(expected, 2) else "FAIL"
        if status == "PASS":
            passed += 1
        else:
            failed += 1
        print(f"[{status}]  Input:    {sentence}")
        got_str = f"${result:.2f}" if result is not None else "N/A"
        print(f"        Expected: ${expected:.2f}  |  Got: {got_str}")
        print()

    print(f"Results: {passed} passed, {failed} failed out of {len(test_cases)} tests.")
    print()

    # Uncomment to run interactive mode after tests:
    # main()
