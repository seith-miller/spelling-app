import os
import time
from gtts import gTTS
from app import AUDIO_FOLDER, anthropic


def generate_sentence(word):
    prompt = f"Create a clear, engaging sentence that correctly uses the word '{word}'. The sentence should provide context clues to help understand the word's meaning. Aim for a natural, conversational tone suitable for everyday use."

    response = anthropic.messages.create(
        model="claude-3-sonnet-20240229",
        max_tokens=100,
        messages=[{"role": "user", "content": prompt}],
    )
    return response.content[0].text


def read_words_from_file(filename):
    with open(filename, "r") as file:
        return [line.strip() for line in file if line.strip()]


def speak_word_and_sentence(word):
    sentence = generate_sentence(word)
    text_to_speak = f"{word}. {sentence} {word}."
    tts = gTTS(text=text_to_speak, lang="en")
    filename = f"{word}_{time.time()}.mp3"
    filepath = os.path.join(AUDIO_FOLDER, filename)
    tts.save(filepath)
    return filename, sentence


def cleanup_old_files():
    for filename in os.listdir(AUDIO_FOLDER):
        file_path = os.path.join(AUDIO_FOLDER, filename)
        if os.path.getmtime(file_path) < time.time() - 300:  # 5 minutes old
            os.remove(file_path)
