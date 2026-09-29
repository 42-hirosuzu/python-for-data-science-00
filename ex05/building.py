import sys


def is_punctuation(c: str) -> bool:
    """Check whether the character is an ASCII punctuation mark."""
    return c.isascii() and c.isprintable() and not c.isalnum() and c != " "


def count_chars(text: str) -> None:
    """Print the number of characters in each category."""
    print(f"The text contains {len(text)} characters:")
    print(f"{sum(c.isupper() for c in text)} upper letters")
    print(f"{sum(c.islower() for c in text)} lower letters")
    print(f"{sum(is_punctuation(c) for c in text)} punctuation marks")
    print(f"{sum(c.isspace() for c in text)} spaces")
    print(f"{sum(c.isdigit() for c in text)} digits")


def main():
    """Count the characters of the argument or of the prompted text."""
    try:
        assert len(sys.argv) <= 2, "more than one argument is provided"
        text = sys.argv[1] if len(sys.argv) == 2 else ""
        if not text:
            print("What is the text to count?")
            text = sys.stdin.readline()
        count_chars(text)
    except AssertionError as e:
        print(f"AssertionError: {e}")
    except KeyboardInterrupt:
        print()


if __name__ == "__main__":
    main()
