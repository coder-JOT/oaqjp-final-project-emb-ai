"""Flask App for Emotion Detection."""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")
@app.route("/emotionDetector")

def detect_emotion():
    """Function to detect emotion using the entered text."""
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    if dominant_emotion is None :
        return "Invalid text! Please try again!."
    result_str = ("For the given statement, the system response is "
    "'anger': {}, 'disgust': {}, 'fear': {}, 'joy': {} and 'sadness': {}."
    " The dominant emotion is {}.")

    return result_str.format(anger, disgust, fear, joy, sadness, dominant_emotion)

@app.route("/")
def render_index_page():
    """Renders the main page of the App."""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
