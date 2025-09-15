# Python-Advanced

This repository contains experiments and projects exploring advanced Python concepts and libraries. It is a work-in-progress for learning and practicing new Python skills.

---

## Topics & Libraries Explored

- **Email Handling:** Sending and reading emails using `smtplib`, `imapclient`, and `pyzmail`.  
- **Security:** Handling passwords securely with `getpass`.  
- **GUI Automation:**  
  - Controlling the keyboard and mouse using `pyautogui`.  
  - Automate repetitive tasks like filling out forms, pressing buttons, and navigating applications.  
  - Use screen color checks and screenshots to help the program stay on track.  
  - Best practice: make programs fail quickly on invalid instructions to prevent unintended actions.  
  - Simulate human-like actions and watch the mouse move while text appears automatically.  
- **Data Analysis & Visualization:**  
  - Analyze COVID-19 datasets using `pandas`.  
  - Visualize global confirmed, recovered, and death cases with interactive Plotly charts.  
  - Enhanced visualizations with styled pie/donut charts, annotations, and color-coded segments.  
- **Natural Language Processing & Deep Learning:**  
  - Build deep learning models using `TensorFlow` and `Keras`.  
  - Text preprocessing with tokenization, padding, and GloVe embeddings.  
  - Convolutional layers (Conv1D) to detect local patterns in text.  
  - LSTM layers to capture long-term dependencies in sequences.  
  - Binary classification models for tasks like fake news detection.  

---

## Projects Included

### Fake News Detection Model (TensorFlow & NLP)

- Reads a news dataset containing titles, text, and labels (FAKE/REAL).  
- Preprocesses data by combining title and text, tokenizing, and padding sequences.  
- Encodes labels into numerical format for model training.  
- Uses pre-trained GloVe embeddings to represent words in real-valued vector space.  
- Model architecture:  
  - **Embedding Layer:** Maps words to dense vectors using GloVe embeddings.  
  - **Conv1D + MaxPooling:** Detects local textual patterns and highlights important features.  
  - **LSTM Layer:** Captures context and long-term dependencies in the text.  
  - **Dense + Sigmoid:** Outputs final classification probability (Fake or Real).  
- Trains on a subset of the dataset and validates on a test set.  
- Makes predictions on new articles by combining title and text, tokenizing, padding, and feeding to the trained model.  
- Saves the trained model for reuse (`.h5` format).  
- Provides tokenized sequences and prediction probability for transparency.  

### GUI Automation Projects

- Python automation bot for **Sushi Go Round**:  
  - Detects customer orders in real time.  
  - Manages ingredient inventory automatically.  
  - Prepares sushi by interacting with the game interface.  
  - Uses screen color checks, keyboard/mouse automation, and failsafe mechanisms to prevent errors.  

### Data Analysis Projects

- **COVID-19 Global Analysis with Plotly:**  
  - Reads time-series CSV datasets for confirmed, recovered, and death cases.  
  - Computes total active, recovered, and dead cases.  
  - Generates interactive donut charts with custom colors, annotations, and hover information.  
  - Produces shareable HTML chart files for visualization.  

---

## Tech Stack

- **Programming Language:** Python 3.x  
- **Data Analysis & Visualization:** `pandas`, `numpy`, `plotly`, `matplotlib`, `seaborn`  
- **Machine Learning & Deep Learning:** `tensorflow`, `keras`, `scikit-learn`  
- **Text Processing & NLP:** `keras.preprocessing.text.Tokenizer`, `pad_sequences`, GloVe embeddings  
- **Automation & GUI Interaction:** `pyautogui`  
- **Email Handling & Security:** `smtplib`, `imapclient`, `pyzmail`, `getpass`  
- **File Handling & I/O:** CSV, HTML export for interactive visualizations  

---

## Purpose

The goal of this repository is to gradually build experience with advanced Python functionality, including:

- Natural language processing and deep learning model development  
- Automation of repetitive tasks on your computer  
- Email interaction and handling  
- Secure handling of sensitive information  
- Data analysis and interactive visualization  

New projects and experiments will be added over time as skills progress.
