from transformers import pipeline

# Load Hugging Face emotion classification pipeline (TensorFlow backend)
emotion_classifier = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base", return_all_scores=False, framework="tf")

def detect_emotion(text):
    """
    Detect emotion from text using Hugging Face emotion classification model.
    Returns: (label, confidence_score)
    """
    result = emotion_classifier(text)[0]
    label = result['label']
    score = result['score']
    return label, score