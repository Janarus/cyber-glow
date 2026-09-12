from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Cyber Glow K-Beauty сайты сәтті іске қосылды!"
