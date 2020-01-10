from math import sqrt, pi
from files.part1 import add, subtract, multiply, divide, pow, pythagoras, dist, quad, degtorad, isprime, sum, fact, sumofsquares
from files.part2 import contains as contains_2, add as add_2, remove as remove_2, find, clear, printall as printall_2
from files.part3 import contains as contains_3, add as add_3, remove as remove_3, get, printall as printall_3, sortkeys, reordercontacts

def test(func, t):
    return func == t


def print_text(functions):
    failed = []
    successful = []
    print("-" * 30)
    for name in functions.keys():
        if(not functions.get(name)):
            failed.append(name)
        else:
            successful.append(name)

    print("Failed: %d\nSuccessful: %d" % (len(failed), len(successful)))
    print("-" * 30)
    if(len(successful) != 0):
        for name in successful:
            print("%s successful!" % name)
        print("-" * 30)
    if(len(failed) != 0):
        for name in failed:
            print("%s failed, try this one again!" % name)
        print("-" * 30)


def part_1_check():
    print("-" * 30)
    print("\nPart 1 Check\n")

    functions = {"Add Function": test(add(1, 2), 3),
                 "Subtract Function": test(subtract(1, 2), -1),
                 "Multiply Function": test(multiply(10, 5), 50),
                 "Divide Function": test(divide(1, 2), 0.5),
                 "Divide Function with 0 Denominator": test(divide(1, 0), 0),
                 "Power Function": test(pow(3, 2), 9),
                 "Pythagoras Function": test(pythagoras(3, 4), 5),
                 "Distance Function": test(dist(0, 0, 1, 1), sqrt(2)),
                 "Quadratic Function": test(quad(1, 0, -1), [1.0, -1.0]),
                 "Quadratic Function with 0 as a": test(quad(0, 0, -1), 0),
                 "Degrees to Radians Function": test(degtorad(90), pi / 2),
                 "Is Prime Function": test(isprime(151), True),
                 "Summation Function": test(sum(10), 55),
                 "Factorial Function": test(fact(5), 120),
                 "Sum of Squares Function": test(sumofsquares(5), 55)
                 }
    print_text(functions)


def part_2_check():
    print("Part 2 Check\n")
    functions = {"Food Addition": test(add_2("Food"), True),
                 "Food Contains": test(contains_2("Food"), True),
                 "Socks Addition": test(add_2("Socks"), True),
                 "Food Addition Exists": test(add_2("Food"), False),
                 "Drinks Addition": test(add_2("Drinks"), True),
                 "Socks Remove": test(remove_2("Socks"), "Socks"),
                 "Food Find": test(find("Food"), 0),
                 "Removed Find": test(find("Socks"), -1)
                 }
    print_text(functions)
    print("Clear and Print All tested separately")
    print("Interactive components tested separately")
    print("-" * 30)


def part_3_check():
    print("Part 3 Check\n")
    functions = {
        "First Contact Addition": test(add_3("Wendy Son", "1238293784", "1 Arguello Street", "wson@email.com"), True),
        "Second Contact Addition": test(add_3("John Doe", "4151234567", "1 Main Street", "JDoe@email.com"), True),
        "Third Contact Addition": test(add_3("Lisa Cheung", "9382392833", "31 Clement Street", "lcheung@email.com"), True),
        "First Contact Readdition Failure": test(add_3("Wendy Son", "1238293784", "1 Arguello Street", "wson@email.com"), False),
        "First Contact Contains": test(contains_3("Wendy Son"), True),
        "Contact Does Not Exist": test(contains_3("Jacob Lee"), False),
        "Remove Third Contact":  test(remove_3("Lisa Cheung"), True),
        "Remove Not Found Contact": test(remove_3("Yadan Noerdin"), False),
        "Get First Contact": test(get("John Doe"), ["4151234567", "1 Main Street", "JDoe@email.com"]),
        "Get Contact Not Found": test(get("Jacob Jones"), [])
    }
    print_text(functions)

    print("Sorting functions tested separately")
    print("Print All Functions tested separately")
    print("-" * 30)


def main():
    part_1_check()
    print()
    part_2_check()
    print()
    part_3_check()


main()
