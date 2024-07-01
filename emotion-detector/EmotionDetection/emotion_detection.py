import requests
import json

def emotion_detector(text_to_analyse):
    if not text_to_analyse:
        return {
        'anger': None,
        'disgust': None,
        'fear': None,
        'joy': None,
        'sadness': None,
        'dominant_emotion': None
    }

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = myobj, headers=header)
    formatted_response = json.loads(response.text)

    if response.status_code == 200:
        anger_score = formatted_response["emotionPredictions"][0]["emotion"]["anger"]
        disgust_score = formatted_response["emotionPredictions"][0]["emotion"]["disgust"]
        fear_score = formatted_response["emotionPredictions"][0]["emotion"]["fear"]
        joy_score = formatted_response["emotionPredictions"][0]["emotion"]["joy"]
        sadness_score = formatted_response["emotionPredictions"][0]["emotion"]["sadness"]

        if anger_score >= disgust_score and anger_score >= fear_score and anger_score >= joy_score and anger_score >= sadness_score:
            dominant_emotion = 'anger'
        elif disgust_score >= anger_score and disgust_score >= fear_score and disgust_score >= joy_score and disgust_score >= sadness_score:
            dominant_emotion = 'disgust'
        elif fear_score >= anger_score and fear_score >= disgust_score and fear_score >= joy_score and fear_score >= sadness_score:
            dominant_emotion = 'fear'
        elif joy_score >= anger_score and joy_score >= disgust_score and joy_score >= fear_score and joy_score >= sadness_score:
            dominant_emotion = 'joy'
        else:
            dominant_emotion = 'sadness'

    elif response.status_code == 200:
        anger_score = None
        disgust_score = None 
        fear_score = None 
        joy_score = None 
        sadness_score = None 
        dominant_emotion = None
        

    return {'anger': anger_score, 'disgust': disgust_score, 'fear': fear_score, 'joy': joy_score, 'sadness': sadness_score, 'dominant_emotion': dominant_emotion}

