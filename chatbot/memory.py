chat_log = []

def save_chat(user_input, bot_reply, emotion_label):
    """
    Save a single chat turn to memory.
    """
    chat_log.append({
        "user": user_input,
        "emotion": emotion_label,
        "bot": bot_reply
    })

def show_history():
    """
    Return full chat history (list of dicts).
    """
    return chat_log

def clear_memory():
    """
    Clears chat memory.
    """
    global chat_log
    chat_log = []