# Program Name: Assign2.py
# Course: IT3883/Section 01
# Name: Zara Khusro
# Assignment Number: Assignment 2
# Due Date: 02/18/2026
# Purpose: This program reads a file containing student names and six
#          numeric scores per student, calculates each student's
#          final average, and prints the results sorted in descending
#          order by average grade.
# Resources Used: Course notes, Python documentation


def calculate_average(scores):
    """Return the average of a list of numeric scores."""
    return sum(scores) / len(scores)


def main():
    # Ask user for input file name
    filename = input("Enter input file name: ")

    students = []  # list to store (name, average)

    try:
        with open(filename, 'r') as file:
            for line in file:
                # Remove extra whitespace and split fields
                parts = line.strip().split()

                # Skip empty lines
                if not parts:
                    continue

                name = parts[0]

                # Convert remaining fields to floats
                try:
                    scores = [float(x) for x in parts[1:]]
                except ValueError:
                    print(f"Invalid score detected for {name}. Skipping.")
                    continue

                # Ensure exactly 6 scores as required
                if len(scores) != 6:
                    print(f"Incorrect number of scores for {name}. Skipping.")
                    continue

                avg = calculate_average(scores)
                students.append((name, avg))

        # Sort students by average descending
        students.sort(key=lambda x: x[1], reverse=True)

        print("\nFinal Averages (Highest to Lowest):")
        for name, avg in students:
            print(f"{name} {avg:.2f}")

    except FileNotFoundError:
        print("File not found. Please check the filename.")


if __name__ == '__main__':
    main()
