from transformers import pipeline, set_seed

# Load text generation model (TensorFlow backend)
generator = pipeline("text-generation", model="gpt2", framework="tf")
set_seed(42)

def generate_response(prompt):
    """
    Generate a chatbot response using GPT-2 style generation.
    Returns: generated text (string)
    """
    generated = generator(prompt, max_length=100, num_return_sequences=1)
    return generated[0]['generated_text'].strip()