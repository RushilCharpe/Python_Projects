import os

# Clear the terminal screen
os.system('cls' if os.name == 'nt' else 'clear')

# Colors for UI
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
BOLD = "\033[1m"
RESET = "\033[0m"

WIDTH = 50

# Header
print(CYAN + BOLD + "=" * WIDTH)
print("          NUMBER SYSTEM CONVERTER")
print("=" * WIDTH + RESET)

print(YELLOW + "\n  Available Number Systems" + RESET)
print("  [1] Binary       (Base 2)")
print("  [2] Octal        (Base 8)")
print("  [3] Decimal      (Base 10)")
print("  [4] Hexadecimal  (Base 16)")
print("-" * WIDTH)

# Original input section
a = input("  Enter Number       : ")
in_form = input("  Convert From       : ")
out_form = input("  Convert To         : ")

print("-" * WIDTH)

# Original conversion logic
try:
    if in_form.lower() == "binary":
        val = int(a, 2)
    elif in_form.lower() == "octal":
        val = int(a, 8)
    elif in_form.lower() == "decimal":
        val = int(a, 10)
    elif in_form.lower() == "hexadecimal":
        val = int(a, 16)
    else:
        print(RED + "\n  Invalid Input Format!" + RESET)
        raise SystemExit

    # Original output logic
    if out_form.lower() == "binary":
        result = bin(val)[2:]
        label = "Binary"
    elif out_form.lower() == "octal":
        result = oct(val)[2:]
        label = "Octal"
    elif out_form.lower() == "decimal":
        result = str(val)
        label = "Decimal"
    elif out_form.lower() == "hexadecimal":
        result = hex(val)[2:].upper()
        label = "Hexadecimal"
    else:
        print(RED + "\n  Invalid Output Format!" + RESET)
        raise SystemExit

    # Improved result display
    print(GREEN + BOLD + "\n" + "=" * WIDTH)
    print("              CONVERSION RESULT")
    print("=" * WIDTH + RESET)

    print(f"  Original Number : {a}")
    print(f"  From Format     : {in_form.capitalize()}")
    print(f"  To Format       : {out_form.capitalize()}")

    print("-" * WIDTH)
    print(f"  {YELLOW}Converted Result:{RESET}")
    print(f"\n  {GREEN}{BOLD}{result}{RESET}")
    print(GREEN + "=" * WIDTH + RESET)

except ValueError:
    print(RED + "\n  Error: Invalid number for the selected base!" + RESET)
    print("  Please check your number and try again.")
    print("=" * WIDTH)
