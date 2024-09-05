from flask import Flask
from anthropic import Anthropic
import os

app = Flask(__name__)

AUDIO_FOLDER = os.path.join(app.static_folder, "audio")
os.makedirs(AUDIO_FOLDER, exist_ok=True)

anthropic = Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

from app import routes
