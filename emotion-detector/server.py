'''Back-end code for emotion detector website'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detection():
    '''Function for sent detection result to the web'''
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    anger_score = response['anger']
    disgust_score = response['disgust']
    fear_score = response['fear']
    joy_score = response['joy']
    sadness_score = response['sadness']
    dominant_emotion = response['dominant_emotion']

    if dominant_emotion is None:
        return "Invalid input! Try again."

    return (
        f"For the given statement, the system response is 'anger': {anger_score}, " 
        f"'disgust': {disgust_score}, 'fear': {fear_score}, 'joy': {joy_score} " 
        f"and 'sadness': {sadness_score}. The dominant emotion is {dominant_emotion} "
    )

@app.route("/")
def render_index_page():
    '''Function to run the render_template on HTML file "index.html"'''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
