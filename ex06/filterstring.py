import sys
from ft_filter import ft_filter


def main():
    """Print the words of S that are longer than N."""
    try:
        assert len(sys.argv) == 3
        s = sys.argv[1]
        n = int(sys.argv[2])
        print([w for w in ft_filter(lambda w: len(w) > n, s.split())])
    except (AssertionError, ValueError):
        print("AssertionError: the arguments are bad")


if __name__ == "__main__":
    main()
