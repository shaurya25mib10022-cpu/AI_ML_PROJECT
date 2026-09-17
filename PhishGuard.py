import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

data = {
    'text': [
        "Your account is suspended. Click here to login immediately!",
        "URGENT: Your prize of $1000 is waiting. Claim now.",
        "Hey, are we still meeting for coffee at 5?",
        "Final notice: Update your payment details or lose access.",
        "The weather today is quite nice, don't you think?",
        "Verify your identity at secure-bank-login.com to avoid fees."
    ],
    'label': [1, 1, 0, 1, 0, 1]  # 1 = Phishing/Spam, 0 = Safe/Ham
}

df = pd.DataFrame(data)

# 2. FEATURE EXTRACTION 
# TF-IDF converts text into a matrix of "importance scores" for each word.
tfidf = TfidfVectorizer(stop_words='english')
X = tfidf.fit_transform(df['text'])
y = df['label']

# 3. TRAIN THE MODEL
# Naive Bayes is excellent for text classification because it's fast and effective.
model = MultinomialNB()
model.fit(X, y)

# 4. THE "RISK SCORE" FUNCTION
def analyze_message(message):
    # Transform the new message using the same TF-IDF logic
    message_tfidf = tfidf.transform([message])
    
    # Get probability: [Prob of Safe, Prob of Phishing]
    probabilities = model.predict_proba(message_tfidf)[0]
    risk_score = round(probabilities[1] * 100, 2)
    
    print(f"--- Analysis for: '{message}' ---")
    print(f"Risk Score: {risk_score}%")
    
    if risk_score > 70:
        print("RESULT: HIGH RISK. This looks like a phishing attempt.")
    elif risk_score > 40:
        print("RESULT: CAUTION. Use a second pair of eyes.")
    else:
        print("RESULT: LOW RISK. Likely safe.")
    print("-" * 40)

# 5. TEST IT
test_msg = "URGENT: Your Netflix subscription has expired. Click to renew."
analyze_message(test_msg)

test_msg2 = "Hey, just wanted to check if you're free for lunch tomorrow?"
analyze_message(test_msg2)

test_msg3 = "Your bank account has been compromised. Verify your identity now!"
analyze_message(test_msg3)

test_msg4 = "Don't forget about the meeting at 3 PM today."
analyze_message(test_msg4)

test_msg5 = "Congratulations! You've won a free iPhone. Click here to claim."
analyze_message(test_msg5)
