PhishGuard: AI-Powered Risk Scoring for Digital LiteracyBYOP Capstone Project
AI & ML Fundamentals

Project Overview
PhishGuard is a Natural Language Processing (NLP) tool designed to protect vulnerable populations (such as the elderly or non-tech-savvy users) from phishing and SMS scams. Unlike standard filters that simply block messages, PhishGuard provides a transparency-focused Risk Score, explaining why a message might be dangerous.

This project addresses the real-world problem of social engineering by using machine learning to identify patterns of urgency, suspicious links, and malicious intent in text.

Key FeaturesText
Vectorization: Uses TF-IDF (Term Frequency-Inverse Document Frequency) to extract meaningful features from raw text.

Probabilistic Classification: Implements a Multinomial Naive Bayes model to calculate the likelihood of a scam.

Intuitive Risk Scoring: Converts complex ML outputs into a simple 0-100% risk scale with actionable advice.

Lightweight & Fast: Designed to run on low-resource devices without needing heavy cloud APIs.

Technical Stack

Language: Python 3.x

Libraries:

        pandas: For data manipulation and structured storage.
        scikit-learn: For TF-IDF vectorization and the Naive Bayes classifier.
        re: For Regular Expression based URL and pattern detection.

How It Works (The Engineering Logic)

Preprocessing: The input text is cleaned (removing punctuation, converting to lowercase) to ensure the model focuses on the core message.

Feature Extraction ($TF-IDF$): The importance of words like "Urgent" or "Suspended" is weighted against their frequency in common language.

Classification: The model compares the input against a trained dataset of thousands of "Spam" and "Ham" (Safe) messages.

Result Generation:
Low Risk (<40%): Likely a standard personal message.
Caution (40-70%): Contains some suspicious patterns; users should verify the sender.
High Risk (>70%): Strong indicators of phishing (e.g., sense of urgency + suspicious links).

project.py # Main Python script with ML logic
README.md # Project documentation
requirements.txt # List of required Python packages

Future Enhancements

URL Analysis: Integration with a database of known malicious domains.

Multi-language Support: Expanding the filter to detect scams in regional languages.

Browser Extension: Porting the logic to a Chrome extension to filter emails in real-time.

Author

Name: Akash Kumar Gautam
Course: AI & Machine Learning Fundamentals
Platform: VITyarthi BYOP Submission
