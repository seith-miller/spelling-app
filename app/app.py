import time
import random
from gtts import gTTS
import os


def read_words_from_file(filename):
    with open(filename, "r") as file:
        return [line.strip() for line in file if line.strip()]


words = read_words_from_file("top_100.txt")


def speak_word(word):
    tts = gTTS(text=word, lang="en")
    tts.save("temp.mp3")
    os.system("afplay temp.mp3")  # This works on macOS
    os.remove("temp.mp3")


def run_spelling_test(num_words):
    print("Welcome to the Handwritten Spelling Assessment Program!")
    print(f"You will hear {num_words} words, one at a time.")
    print("Write each word on your paper. You'll have 15 seconds per word.")
    print("After the test, you'll grade your own responses.")
    input("Press Enter when you're ready to begin...")

    test_words = random.sample(words, num_words)
    for i, word in enumerate(test_words, 1):
        print(f"\nWord {i}:")
        speak_word(word)
        time.sleep(2)
        speak_word(word)
        time.sleep(8)  # Time to write on paper

    print("\nTest complete! Please grade your responses now.")
    input("Press Enter when you're ready to input your results...")
    return test_words


def grade_test(test_words):
    correct = 0
    incorrect = []
    for i, word in enumerate(test_words, 1):
        print(f"\nWord {i}: {word}")
        is_correct = (
            input("Did you spell it correctly? (Press Enter for yes, or 'n' for no): ")
            .lower()
            .strip()
        )
        if is_correct != "n":
            correct += 1
        else:
            incorrect.append(word)

    return correct, incorrect


def main():
    while True:
        try:
            num_words = int(
                input("How many words would you like in this test? (1-100): ")
            )
            if 1 <= num_words <= 100:
                break
            else:
                print("Please enter a number between 1 and 100.")
        except ValueError:
            print("Please enter a valid number.")

    test_words = run_spelling_test(num_words)
    correct, incorrect = grade_test(test_words)

    percentage = (correct / num_words) * 100
    print(f"\nYour score: {correct}/{num_words}")
    print(f"Percentage: {percentage:.2f}%")

    if incorrect:
        print("\nWords spelled incorrectly:")
        for word in incorrect:
            print(word)


if __name__ == "__main__":
    main()
