from flask import render_template, request, jsonify, send_from_directory
from app import app, AUDIO_FOLDER
from app.services.spelling import (
    start_spelling_test,
    grade_spelling_test,
    cleanup_audio_files,
)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/start_test", methods=["POST"])
def start_test():
    try:
        num_words = int(request.form["num_words"])
        result = start_spelling_test(num_words)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/grade_test", methods=["POST"])
def grade_test():
    results = request.json
    graded_results = grade_spelling_test(results)
    return jsonify(graded_results)


@app.route("/audio/<filename>")
def serve_audio(filename):
    return send_from_directory(AUDIO_FOLDER, filename)


@app.route("/cleanup", methods=["POST"])
def cleanup():
    files = request.json["files"]
    cleanup_audio_files(files)
    return jsonify({"status": "success"})
