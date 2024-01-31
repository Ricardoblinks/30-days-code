from sklearn.metrics import classification_report, accuracy_score

def evaluate_classification_model(y_true, y_pred):
    """
    Evaluate the performance of a classification model using metrics like accuracy, precision, recall, and F1 score.

    Parameters:
    - y_true: The true labels.
    - y_pred: The predicted labels.

    Returns:
    - Dictionary containing accuracy, precision, recall, and F1 score.
    """
    # Calculate accuracy
    accuracy = accuracy_score(y_true, y_pred)

    # Calculate precision, recall, and F1 score
    classification_metrics = classification_report(y_true, y_pred, output_dict=True)

    # Extract precision, recall, and F1 score from the classification report
    precision = classification_metrics['weighted avg']['precision']
    recall = classification_metrics['weighted avg']['recall']
    f1_score = classification_metrics['weighted avg']['f1-score']

    # Create a dictionary with the evaluation metrics
    evaluation_results = {
        'Accuracy': accuracy,
        'Precision': precision,
        'Recall': recall,
        'F1 Score': f1_score
    }

    return evaluation_results

# Example usage:
# Replace y_true and y_pred with your actual true labels and predicted labels
y_true = [1, 0, 1, 1, 0, 1, 0, 0, 1, 0]
y_pred = [1, 0, 1, 1, 0, 1, 0, 1, 1, 0]

results = evaluate_classification_model(y_true, y_pred)
print("Evaluation Results:")
for metric, value in results.items():
    print(f"{metric}: {value}")
