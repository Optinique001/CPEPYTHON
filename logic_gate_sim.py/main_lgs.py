# Logic Gate Simulator

# Logic Input Function
def logic_input():
    while True:
        try:
            x = int(input("Enter value for x (0 or 1): "))
            y = int(input("Enter value for y (0 or 1): "))

            if x in (0, 1) and y in (0, 1):
                return x, y
            else:
                print("Please enter only 0 or 1.\n")

        except ValueError:
            print("Invalid input. Please enter numbers only.\n")


# Logic Gate Functions
def AND(x, y):
    if x == 1 and y == 1:
        return 1
    else:
        return 0


def OR(x, y):
    if x == 1 or y == 1:
        return 1
    else:
        return 0


def NOT(x):
    if x == 1:
        return 0
    else:
        return 1


def XOR(x, y):
    if (x == 1 and y == 0) or (x == 0 and y == 1):
        return 1
    else:
        return 0


# Half Adder Function
def half_adder(x, y):
    total = XOR(x, y)
    carry = AND(x, y)
    return total, carry


# Step 3: Test Half Adder
def test_half_adder():
    test_cases = [(0, 0), (0, 1), (1, 0), (1, 1)]

    # List comprehension
    results = [(x, y, *half_adder(x, y)) for x, y in test_cases]

    print("\nHALF ADDER TRUTH TABLE")
    print("=" * 35)
    print(f"{'X':<5}{'Y':<5}{'SUM':<8}{'CARRY':<8}")
    print("-" * 35)

    for x, y, total, carry in results:
        print(f"{x:<5}{y:<5}{total:<8}{carry:<8}")

    print("=" * 35)


# MAIN PROGRAM
while True:
    print("\n=== Logic Gate Simulator ===")
    print("1. AND")
    print("2. OR")
    print("3. NOT")
    print("4. XOR")
    print("5. Half Adder")
    print("6. Test Half Adder")
    print("7. All Operations")
    print("8. Exit")

    choice = input("Enter your choice (1-8): ")

    if choice == '1':
        x, y = logic_input()
        result = AND(x, y)
        print(f"Result of ({x} AND {y}) = {result}")

    elif choice == '2':
        x, y = logic_input()
        result = OR(x, y)
        print(f"Result of ({x} OR {y}) = {result}")

    elif choice == '3':
        while True:
            try:
                x = int(input("Enter value for x (0 or 1): "))
                if x in (0, 1):
                    break
                print("Please enter only 0 or 1.")
            except ValueError:
                print("Invalid input.")

        result = NOT(x)
        print(f"Result of (NOT {x}) = {result}")

    elif choice == '4':
        x, y = logic_input()
        result = XOR(x, y)
        print(f"Result of ({x} XOR {y}) = {result}")

    elif choice == '5':
        x, y = logic_input()
        total, carry = half_adder(x, y)

        print(f"\nHalf Adder ({x}, {y})")
        print(f"Sum   = {total}")
        print(f"Carry = {carry}")

    elif choice == '6':
        test_half_adder()

    elif choice == '7':
        x, y = logic_input()

        total, carry = half_adder(x, y)

        gates = [
            ("AND", AND(x, y)),
            ("OR", OR(x, y)),
            ("NOT X", NOT(x)),
            ("NOT Y", NOT(y)),
            ("XOR", XOR(x, y)),
            ("HA SUM", total),
            ("HA CARRY", carry)
        ]

        print("\n" + "=" * 40)
        print(f"{'X':<5}{'Y':<5}{'GATE':<15}{'RESULT':<10}")
        print("-" * 40)

        for gate, result in gates:
            print(f"{x:<5}{y:<5}{gate:<15}{result:<10}")

        print("=" * 40)

    elif choice == '8':
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 8.")

print("Thank you for using the Logic Gate Simulator!")