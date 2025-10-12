import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pickle
import os

# Parameters (same as training)
max_length = 54
padding_type = 'post'
trunc_type = 'post'
oov_tok = "<OOV>"

def create_tokenizer_if_needed():
    """Create tokenizer from dataset if it doesn't exist"""
    tokenizer_path = 'fakenews/tokenizer.pkl'
    
    if not os.path.exists(tokenizer_path):
        print("Tokenizer not found. Creating from dataset...")
        
        # Load dataset
        try:
            data = pd.read_csv("fakenews/news.csv")
            data = data.drop(["Unnamed: 0"], axis=1, errors='ignore')
            
            # Create combined text from a sample (to avoid memory issues)
            sample_size = min(5000, len(data))
            titles = data['title'][:sample_size].fillna('')
            texts = data['text'][:sample_size].fillna('')
            combined_text = [f"{t} {tx}" for t, tx in zip(titles, texts)]
            
            # Create and fit tokenizer
            tokenizer = Tokenizer(oov_token=oov_tok)
            tokenizer.fit_on_texts(combined_text)
            
            # Save tokenizer
            with open(tokenizer_path, 'wb') as f:
                pickle.dump(tokenizer, f)
            
            print(f"Tokenizer created and saved to {tokenizer_path}")
            return tokenizer
            
        except Exception as e:
            print(f"Error creating tokenizer: {e}")
            print("Please make sure 'fakenews/news.csv' exists")
            return None
    else:
        # Load existing tokenizer
        with open(tokenizer_path, 'rb') as f:
            tokenizer = pickle.load(f)
        print("Tokenizer loaded successfully")
        return tokenizer

def load_model_and_tokenizer():
    """Load the trained model and tokenizer"""
    try:
        # Load model
        model = tf.keras.models.load_model("fakenews/fakenews_model.h5")
        print("Model loaded successfully")
        
        # Load or create tokenizer
        tokenizer = create_tokenizer_if_needed()
        
        if tokenizer is None:
            return None, None
            
        return model, tokenizer
        
    except Exception as e:
        print(f"Error loading model: {e}")
        print("Make sure 'fakenews/fakenews_model.h5' exists")
        print("Run the training script first: python fakenews/news.py")
        return None, None

def predict_news(title, text, model, tokenizer):
    """Predict if news is real or fake"""
    try:
        # Combine title and text
        combined = f"{title} {text}"
        
        # Convert to sequence and pad
        sequence = tokenizer.texts_to_sequences([combined])
        padded = pad_sequences(sequence, maxlen=max_length, padding=padding_type, truncating=trunc_type)
        
        # Make prediction
        prediction = model.predict(padded, verbose=0)[0][0]
        
        # ADD DEBUGGING INFO
        print(f"Raw prediction value: {prediction}")
        print(f"Prediction >= 0.5: {prediction >= 0.5}")
        
        if prediction >= 0.5:
            result = "FAKE"
            confidence = prediction * 100
        else:
            result = "REAL"
            confidence = (1 - prediction) * 100
        
        print(f"Title: {title}")
        print(f"Text: {text}")
        print(f"Prediction: {result}")
        print(f"Raw Score: {prediction:.4f}")
        print(f"Confidence: {confidence:.1f}%")
        print("-" * 50)
        
        return result, prediction
        
    except Exception as e:
        print(f"Error making prediction: {e}")
        return None, None

def interactive_test(model, tokenizer):
    """Interactive testing mode"""
    print("\nInteractive News Testing")
    print("Enter 'quit' to exit")
    
    while True:
        print("\nEnter news article details:")
        title = input("Title: ").strip()
        
        if title.lower() == 'quit':
            break
            
        text = input("Text: ").strip()
        
        if text.lower() == 'quit':
            break
            
        if title and text:
            predict_news(title, text, model, tokenizer)
        else:
            print("Enter both title and text")

# Test different articles
if __name__ == "__main__":
    print("Fake News Detection System")
    
    # Load model and tokenizer
    model, tokenizer = load_model_and_tokenizer()
    
    if model is None or tokenizer is None:
        print("Failed to load model or tokenizer. Exiting")
        exit(1)
    
    # Predefined test cases
    print("\n=== Running Predefined Tests ===")
    test_cases = [
        ("Biden Announces New Policy", "President Biden announced a comprehensive new healthcare policy today during a White House briefing"),
        ("Aliens Land in New York", "Green creatures from Mars have landed in Central Park according to multiple eyewitnesses who claim to have seen flying saucers"),
        ("Stock Market Update", "The Dow Jones Industrial Average closed up 200 points following positive economic reports from the Federal Reserve"),
        ("Breaking: Celebrity Dies", "Famous actor found dead in mysterious circumstances, sources claim government conspiracy involved"),
        ("Weather Alert", "National Weather Service issues severe thunderstorm warning for downtown area with potential flooding expected"),
        ("Miracle Cure Found", "Scientists claim to have discovered a miracle cure that can heal any disease within 24 hours using common household items")
    ]
    
    for title, text in test_cases:
        predict_news(title, text, model, tokenizer)
    
    # Interactive mode
    try:
        interactive_test(model, tokenizer)
    except KeyboardInterrupt:
        print("\nExiting...")
