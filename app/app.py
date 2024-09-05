from flask import Flask, render_template, request, jsonify, send_from_directory
import time
import random
from gtts import gTTS
import os
import tempfile

app = Flask(__name__)

AUDIO_FOLDER = os.path.join(app.static_folder, "audio")
os.makedirs(AUDIO_FOLDER, exist_ok=True)


def read_words_from_file(filename):
    with open(filename, "r") as file:
        return [line.strip() for line in file if line.strip()]


words = read_words_from_file("app/static/top_100.txt")


def speak_word(word):
    tts = gTTS(text=word, lang="en")
    filename = f"{word}_{time.time()}.mp3"
    filepath = os.path.join(AUDIO_FOLDER, filename)
    tts.save(filepath)
    return filename


def cleanup_old_files():
    for filename in os.listdir(AUDIO_FOLDER):
        file_path = os.path.join(AUDIO_FOLDER, filename)
        if os.path.getmtime(file_path) < time.time() - 300:  # 5 minutes old
            os.remove(file_path)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/start_test", methods=["POST"])
def start_test():
    cleanup_old_files()
    num_words = int(request.form["num_words"])
    test_words = random.sample(words, num_words)
    audio_files = [f"/audio/{speak_word(word)}" for word in test_words]
    return jsonify({"words": test_words, "audio_files": audio_files})


@app.route("/grade_test", methods=["POST"])
def grade_test():
    results = request.json
    correct = sum(1 for result in results if result["correct"])
    incorrect = [result["word"] for result in results if not result["correct"]]
    percentage = (correct / len(results)) * 100
    return jsonify(
        {"correct": correct, "incorrect": incorrect, "percentage": percentage}
    )


@app.route("/audio/<filename>")
def serve_audio(filename):
    return send_from_directory(AUDIO_FOLDER, filename)


@app.route("/cleanup", methods=["POST"])
def cleanup():
    files = request.json["files"]
    for file in files:
        file_path = os.path.join(AUDIO_FOLDER, os.path.basename(file))
        if os.path.exists(file_path):
            os.remove(file_path)
    return jsonify({"status": "success"})


if __name__ == "__main__":
    app.run(debug=True)
