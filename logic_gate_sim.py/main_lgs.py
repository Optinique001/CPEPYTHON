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


def half_adder(x, y):
    total = XOR(x, y)
    carry = AND(x, y)
    return total, carry


# MAIN PROGRAM
while True:
    print("\n=== Logic Gate Simulator ===")
    print("1. AND")
    print("2. OR")
    print("3. NOT")
    print("4. XOR")
    print("5. Half Adder")
    print("6. All Operations")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

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
        print(f"Half Adder ({x}, {y})")
        print(f"Sum   = {total}")
        print(f"Carry = {carry}")

    elif choice == '6':
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

    elif choice == '7':
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 7.")

print("Thank you for using the Logic Gate Simulator!")