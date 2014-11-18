import sys
import getopt


def main():
    number = parse_arguments()
    determine_palindrome(number)


def determine_palindrome(number):
    """
    Determine whether the given number is a palindrome. If it isn't, then find
    the closest palindrome. Prints the results.
    """
    if is_palindrome(number):
        print("Yes, {} is a palindrome.".format(number))
    else:
        print("No {} isn't a palindrome.".format(number))
        lesser_palindrome, greater_palindrome = find_closest_palindrome(
            number - 1, number + 1)

        if lesser_palindrome and greater_palindrome:
            print("But {} and {} are the closest and are the same distance from"
                  " the original number.".format(lesser_palindrome, greater_palindrome))
        elif lesser_palindrome:
            print("But {} is the closest palindrome.".format(lesser_palindrome))
        else:
            print("But {} is the closest palindrome.".format(greater_palindrome))


def is_palindrome(number):
    """
    The definition of a palindromic number is from [1] and includes all natural
    numbers and 0. For simplicity, I am assuming that base 10 numbers are the
    only type to be tested.

    [1]: http://en.wikipedia.org/wiki/Palindromic_number

    :return Boolean
    """
    if number < 0:
        return False

    as_string = str(number)
    first_pointer = 0
    second_pointer = len(as_string) - 1

    while first_pointer < second_pointer:
        if as_string[first_pointer] != as_string[second_pointer]:
            return False

        first_pointer += 1
        second_pointer -= 1

    return True


def find_closest_palindrome(lesser_number, greater_number):
    """
    Searches for the closest palindrome(s) to the given number.

    :return tuple (int|None, int|None): a palindrome less than the given number,
     and a palindrome that is greater
    """
    is_lesser_palindrome = False
    is_greater_palindrome = False

    # Can't do recursion because, with high numbers, the stack could be exceeded
    while not is_lesser_palindrome and not is_greater_palindrome:
        is_lesser_palindrome = is_palindrome(lesser_number)
        is_greater_palindrome = is_palindrome(greater_number)

        if not is_lesser_palindrome and not is_greater_palindrome:
            lesser_number -= 1
            greater_number += 1

    if is_lesser_palindrome and is_greater_palindrome:
        return lesser_number, greater_number
    elif is_lesser_palindrome:
        return lesser_number, None
    else:
        return None, greater_number


def parse_arguments():
    """
    Returns an integer or exits the program with a message
    """
    try:
        opts, args = getopt.getopt(
            sys.argv[1:],
            "n:h",
            ["number=", "help"])

        for opt, arg in opts:
            if opt in ("-h", "--help"):
                print_help_text()
            elif opt in ("-n", "--number"):
                return int(arg)
            else:
                print("Incorrect arguments, -h for help")
    except getopt.GetoptError:
        print("Invalid arguments")
    except ValueError:
        print("The number you entered is not an integer")

    sys.exit(2)


def print_help_text():
    print("""
    Lets you know whether a given number is a palindrome. If it isn't, then
    the closest palindrome(s) will be printed.

    Example usage: $ python ./code_challenge -n 121

        -n      --number        is this number a palindrome?
        -h      --help          display this message
    """)


if __name__ == "__main__":
    main()
