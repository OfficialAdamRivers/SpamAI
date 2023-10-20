from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, confusion_matrix

def naive_bayes_spam_detection(emails, labels):
    try:
        # Preprocessing - CountVectorizer for feature extraction
        vectorizer = CountVectorizer(stop_words='english')
        emails_vectorized = vectorizer.fit_transform(emails)

        # Split dataset into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(emails_vectorized, labels, test_size=0.2, random_state=42)

        # Train Naive Bayes classifier
        nb_classifier = MultinomialNB()
        nb_classifier.fit(X_train, y_train)

        # Make prediction on the test set
        y_pred = nb_classifier.predict(X_test)

        # Evaluate the model
        accuracy = accuracy_score(y_test, y_pred)
        confusion = confusion_matrix(y_test, y_pred)

        print(f'Accuracy: {accuracy}')
        print(f'Confusion Matrix: \n{confusion}')

    except Exception as e:
        print(f"Error during Naive Bayes classification: {e}")

# To use the function, provide the emails (text data) and labels (spam or not spam) as lists.
# emails = ['email1 text', 'email2 text', ..., 'emailN text']
# labels = ['spam', 'not spam', ..., 'spam']
# Ensure that both emails and labels are provided and of the same length.

# Example usage:
# emails = ['email1 text', 'email2 text', ..., 'emailN text']
# labels = ['spam', 'not spam', ..., 'spam']
# naive_bayes_spam_detection(emails, labels)

# Additional Notes:
# 1. Ensure you have imported necessary libraries (sklearn).
# 2. Customize preprocessing steps if needed, such as lowercasing or special character removal.
# 3. For non-binary classification, adapt the script accordingly.
# 4. Consider hyperparameter tuning for improved model performance.
