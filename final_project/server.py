"""
These are imports from flask and from the EmotionDetection package
"""
from flask import Flask, render_template, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emo_detector():
    """
    This is a function that returns the dominant emotion along 
    with other emotion values for the customer to look at. 
    """
    try:
        # 1. Capture the text from the request arguments
        text_to_analyze = request.args.get('text_to_analyze')

        # 2. Pass text to the detector
        response = emotion_detector(text_to_analyze)

        # 3. Handle the 'None' case for dominant_emotion
        # This occurs if the input was blank or the API returned a 400 error
        if response['dominant_emotion'] is None:
            return "Invalid text! Please try again!"

        # 4. If valid, format the successful response string
        return (
            f"For the given statement, the system response is: "
            f"anger: {response['anger']}, "
            f"disgust: {response['disgust']}, "
            f"fear: {response['fear']}, "
            f"joy: {response['joy']}, "
            f"sadness: {response['sadness']}. "
            f"The dominant emotion is '{response['dominant_emotion']}'."
        )

    except (ValueError, KeyError) as e:
        # Catch-all for unexpected issues
        return jsonify({"error": str(e)}), 500

@app.route("/")
def render_index_page():
    """
    This function calls the index.html file so that the application can load.
    """
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
