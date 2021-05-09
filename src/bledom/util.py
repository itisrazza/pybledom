from typing import Optional, Tuple, Callable, List


def title(heading: str):
    print()
    print()
    print(" %s" % heading)
    print((2 + len(heading)) * "=")
    print()


def choose(heading: str, prompt: str = "Select an option", options: List[str] = []) -> Optional[int]:
    title(heading)

    index = 1
    for entry in options:
        print(" %4d -> %s" % (index, entry))
        index += 1

    print()

    user_choice = None
    try:
        user_choice = int(input(" %s: " % prompt)) - 1
    except ValueError:
        pass    # do nothing, just pass down None

    print()

    return user_choice
