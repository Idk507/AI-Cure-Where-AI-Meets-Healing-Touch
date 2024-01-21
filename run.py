import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler, LabelEncoder
import argparse

def predict_heart_rate(model, test_data_file):
    # Load test data
    test_data = pd.read_csv(test_data_file)

    # Preprocess the test data (you might need to adjust this based on your preprocessing steps)
    test_data['condition'] = label_encoder.fit_transform(test_data['condition'])
    test_data_scaled = scaler.fit_transform(test_data.drop(['uuid', 'datasetId'], axis=1))

    # Make predictions
    test_predictions = model.predict(test_data_scaled)

    # Create a DataFrame with the predictions
    results_df = pd.DataFrame({'uuid': test_data['uuid'], 'predicted_HR': test_predictions})

    # Save predictions to results.csv
    results_df.to_csv('results.csv', index=False)

if __name__ == "__main__":
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Predict Heart Rate from test data')
    parser.add_argument('test_data_file', type=str, help='./sample_test_data.csv')
    args = parser.parse_args()

    # Load the final model
    best_model = joblib.load('best_model.pkl')

    # Encode categorical variables
    label_encoder = LabelEncoder()

    # Standardize features
    scaler = StandardScaler()

    # Make predictions on the test data
    predict_heart_rate(best_model, args.test_data_file)

#To run : python run.py test_data.csv
