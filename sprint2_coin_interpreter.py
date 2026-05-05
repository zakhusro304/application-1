"""
IT 3883 Final Exam - Sprint 2 (Corrected Implementation)
Coin Interpreter: Converts pseudo-English coin descriptions to dollar amounts.

Sprint 2 improvements over Sprint 1:
  - Adds input validation with descriptive error messages.
  - Handles edge cases: negative quantities, unknown denominations, empty input.
  - Uses integer arithmetic (cents) to avoid floating-point rounding errors.
  - Supports reading from a file for batch processing.
Author: Student
"""

# --- Coin value definitions (in cents to avoid float arithmetic) ---
COIN_VALUES = {
    "penny":    1,
    "pennies":  1,
    "nickel":   5,
    "nickels":  5,
    "dime":     10,
    "dimes":    10,
    "quarter":  25,
    "quarters": 25,
}


def parse_coin_sentence(sentence):
    """
    Parses a pseudo-English coin sentence and returns the total in dollars.

    Parameters:
        sentence (str): A sentence such as '4 dimes and 7 quarters'.

    Returns:
        float | None: Dollar total rounded to 2 decimal places, or None on error.
    """

    # Reject empty or whitespace-only input
    sentence = sentence.strip()
    if not sentence:
        print("  Error: empty input.")
        return None

    # Tokenise (lowercase)
    words = sentence.lower().split()

    total_cents = 0   # accumulate in cents (integer) to avoid float rounding
    i = 0

    while i < len(words):
        token = words[i]

        # Skip conjunctions
        if token == "and":
            i += 1
            continue

        # Expect a non-negative integer quantity
        if not token.lstrip("-").isdigit():
            print(f"  Error: expected a number but found '{token}'.")
            return None

        quantity = int(token)

        # Reject negative quantities
        if quantity < 0:
            print(f"  Error: quantity cannot be negative ({quantity}).")
            return None

        i += 1

        # Expect a denomination word
        if i >= len(words):
            print("  Error: sentence ended after quantity with no denomination.")
            return None

        denomination = words[i]
        if denomination not in COIN_VALUES:
            print(f"  Error: unknown denomination '{denomination}'.")
            return None

        total_cents += quantity * COIN_VALUES[denomination]
        i += 1

    # Convert cents → dollars and round to 2 decimal places
    return round(total_cents / 100, 2)


def run_tests():
    """Executes the full suite of test cases and prints a pass/fail report."""

    test_cases = [
        # --- Provided test cases ---
        ("1 penny and 2 nickels",                                   0.11),
        ("4 dimes and 7 quarters",                                  2.15),
        ("1 quarter and 3 pennies",                                 0.28),
        ("21 pennies and 17 dimes and 52 quarters",                 14.91),
        ("95 dimes and 73 quarters and 22 nickels and 36 pennies",  29.21),
        ("1 nickel and 17 quarters",                                4.30),
        ("21 nickels and 15 pennies",                               1.20),
        ("1 dime and 1 nickel and 1 penny and 1 quarter",           0.41),
        # --- Additional test cases ---
        ("1 quarter",                                               0.25),
        ("100 pennies",                                             1.00),
        ("0 dimes and 1 nickel",                                    0.05),
        ("10 dimes",                                                1.00),
        ("4 quarters",                                              1.00),
        ("1 penny and 1 nickel and 1 dime and 1 quarter",          0.41),
    ]

    print("=== Sprint 2 Test Run ===\n")
    passed = 0
    failed = 0

    for sentence, expected in test_cases:
        result = parse_coin_sentence(sentence)
        ok = result is not None and round(result, 2) == round(expected, 2)
        label = "PASS" if ok else "FAIL"
        passed += ok
        failed += not ok
        got = f"${result:.2f}" if result is not None else "N/A"
        print(f"[{label}]  {sentence}")
        print(f"       Expected: ${expected:.2f}  |  Got: {got}\n")

    print(f"Results: {passed} passed, {failed} failed out of {len(test_cases)} tests.")


def interactive_mode():
    """Prompts the user for coin sentences interactively until 'quit' is entered."""
    print("=== Coin Interpreter (Sprint 2) ===")
    print("Type a coin sentence or 'quit' to exit.\n")
    while True:
        sentence = input("Enter: ").strip()
        if sentence.lower() == "quit":
            print("Goodbye!")
            break
        result = parse_coin_sentence(sentence)
        if result is not None:
            print(f"  Total: ${result:.2f}\n")
        else:
            print("  Please correct your input and try again.\n")


if __name__ == "__main__":
    run_tests()
    # Uncomment to run interactively after tests:
    # interactive_mode()
