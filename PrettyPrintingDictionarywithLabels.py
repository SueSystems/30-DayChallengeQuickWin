"""Pretty printing dictionary with labels"""


import sys, pprint


def main():
    """Printing Dictionary with labels"""
    data = {"status": "success", "results": {"id": 1, "score": 95}}
    print("Full Report:")
    pprint.pprint(data)


if __name__ == "__main__":
    main()