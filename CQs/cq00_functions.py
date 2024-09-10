"""CQ00"""

__author__ = "730467229"


def mimic(message: str) -> str:
    """This function mimics whtaever message you input"""
    return message


def main() -> None:
    """Main function that pulls together the other functions"""
    print(mimic(message=input("What is your message?")))


if __name__ == "__main__":
    main()
