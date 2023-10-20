# SpamAI
Email spam filtering using AI and naive bayes algorithm

This Python script is designed to perform spam email detection using the Naive Bayes classification algorithm. It takes a list of emails (text data) and their corresponding labels (spam or not spam) as input and provides accuracy and a confusion matrix as output.

## How to Use

1. Ensure you have Python and the required libraries installed, including scikit-learn (sklearn).

2. Clone this repository or download the script directly.

3. Create a list of emails in the `emails` variable, and a list of labels (either 'spam' or 'not spam') in the `labels` variable.

   Example:
   ```python
   emails = ['email1 text', 'email2 text', ..., 'emailN text']
   labels = ['spam', 'not spam', ..., 'spam']

	4.	Run the script, and it will perform the following steps:
	•	Text preprocessing using CountVectorizer.
	•	Splitting the dataset into training and testing sets.
	•	Training a Naive Bayes classifier.
	•	Making predictions on the test set.
	•	Displaying the accuracy and a confusion matrix.
	5.	Customize preprocessing steps if needed, such as lowercase conversion or special character removal.
	6.	If you have more than two classes for labels, adapt the script accordingly.
	7.	For improved model performance, consider hyperparameter tuning.

Example Usage

emails = ['email1 text', 'email2 text', ..., 'emailN text']
labels = ['spam', 'not spam', ..., 'spam']
naive_bayes_spam_detection(emails, labels)

Notes

	•	Ensure that both emails and labels are provided and of the same length.
	•	This script assumes that you have imported the necessary libraries, including scikit-learn.
	•	Customize the preprocessing steps to suit your specific data.
	•	For non-binary classification, adapt the script accordingly.
	•	Hyperparameter tuning may be necessary for optimal model performance.

Feel free to use this script as a starting point for spam email detection and make any necessary modifications to meet your specific requirements

## credits:
Adam Rivers - https://abtzpro.github.io
