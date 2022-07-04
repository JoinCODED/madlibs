def main():
    # write your code here
    print("Mad libs where libs get mad.")
    print("Start below:")

    time = input("Enter a number from 1 to 12: ")
    noun = input("Enter a noun (plural): ")
    name = input("Enter a name: stephen ")
    scream = input("Enter any sentence: ")
    action = input("Enter a verb: ")

    print(type(time))
    print("The story goes...")
    print("It was " + time + " o'clock when I heard a knock at the door.")
    print(
        f"I opened the door and there was a box full of {noun} with a note saying \"From Mr. {name.title()}.\"")
    print("Just as I closed the door I heard a scream " +
          f"{scream.capitalize()}.")
    print(f"I froze in place and all I could do was {action}.")


if __name__ == '__main__':
    main()
