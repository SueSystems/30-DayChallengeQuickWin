"""Updates Dictionary value"""


import sys


def main():
    """Updates Dictionary value
    settings = {"volume": 5}

    Overwrite "volume" with 10 and print\n
    the dictionary.
    """
    settings = {"volume": 5}

    settings["volume"] = 10
    print(settings)

    settings[10] = settings.pop("volume")
    print(settings)
    return 0


if __name__ == "__main__":
    sys.exit(main())