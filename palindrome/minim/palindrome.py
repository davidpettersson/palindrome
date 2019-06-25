def _relax(message: str) -> str:
    return ''.join(
        filter(
            lambda c: c.isalpha() or c.isdigit(),
            map(
                lambda c: c.lower(),
                list(message)
            )
        )
    )


def is_strict_palindrome(message: str) -> bool:
    if not message:
        return False

    reversed_message = ''.join(reversed(message))
    return message == reversed_message


def is_relaxed_palindrome(message: str) -> bool:
    if not message:
        return False

    relaxed_message = _relax(message)
    relaxed_list = list(relaxed_message)
    reversed_relaxed_list = list(
        reversed(list(relaxed_message)))  # make sure to make a list to avoid iterators/generators
    return relaxed_list == reversed_relaxed_list
