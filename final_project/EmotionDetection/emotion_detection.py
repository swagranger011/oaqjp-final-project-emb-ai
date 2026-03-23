import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = {"raw_document": {"text": text_to_analyze}}

    response = requests.post(url, json=input_json, headers=headers)
    formatted_response = json.loads(response.text)

    # The fix: Drill down into the nested dictionary
    # 'emotionPredictions' is a list, so we take the first item [0]
    emotions = formatted_response['emotionPredictions'][0]['emotion']

    # Extracting the scores
    anger_score = emotions['anger']
    disgust_score = emotions['disgust']
    fear_score = emotions['fear']
    joy_score = emotions['joy']
    sadness_score = emotions['sadness']

    # Create a dictionary to easily find the max value
    emotion_dict = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score
    }

    # Find the emotion with the highest score
    dominant_emotion = max(emotion_dict, key=emotion_dict.get)

    # Add the dominant emotion to the final output
    emotion_dict['dominant_emotion'] = dominant_emotion

    return emotion_dict
