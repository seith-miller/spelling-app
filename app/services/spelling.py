import random
import os
from app import AUDIO_FOLDER
from app.utils.helpers import (
    read_words_from_file,
    speak_word_and_sentence,
    cleanup_old_files,
)

words = read_words_from_file("app/static/top_100.txt")


def start_spelling_test(num_words):
    cleanup_old_files()
    test_words = random.sample(words, num_words)
    audio_files = []
    sentences = []
    for word in test_words:
        try:
            audio_file, sentence = speak_word_and_sentence(word)
            audio_files.append(f"/audio/{audio_file}")
            sentences.append(sentence)
        except Exception as e:
            print(f"Error processing word '{word}': {str(e)}")
            continue
    return {"words": test_words, "audio_files": audio_files, "sentences": sentences}


def grade_spelling_test(results):
    correct = sum(1 for result in results if result["correct"])
    incorrect = [result["word"] for result in results if not result["correct"]]
    percentage = (correct / len(results)) * 100
    return {"correct": correct, "incorrect": incorrect, "percentage": percentage}


def cleanup_audio_files(files):
    for file in files:
        file_path = os.path.join(AUDIO_FOLDER, os.path.basename(file))
        if os.path.exists(file_path):
            os.remove(file_path)
