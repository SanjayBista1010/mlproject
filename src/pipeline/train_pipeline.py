import sys
import os
import pandas as pd

from src.exception import CustomException
from src.logger import logging
from src.utils import load_data, save_object, preprocess_data
from src.components.model_trainer import ModelTrainer

def run_training_pipeline():
    try:
        logging.info("Starting training pipeline")

        # Step 1: Load raw data (adjust path and loading method as needed)
        data_path = os.path.join("artifacts", "train.csv")
        data = pd.read_csv(data_path)
        logging.info(f"Loaded training data from {data_path}")

        # Step 2: Preprocess the data (cleaning, encoding, scaling, etc.)
        # Assume preprocess_data returns processed numpy array or DataFrame ready for training
        processed_data = preprocess_data(data)
        logging.info("Data preprocessing completed")

        # Step 3: Split data into train and test arrays
        # Here, for example, you split inside preprocess_data or do it here explicitly
        # For illustration, assume preprocess_data returns numpy arrays train_array, test_array
        train_array, test_array = processed_data['train'], processed_data['test']

        # Step 4: Initialize and run model trainer
        trainer = ModelTrainer()
        r2_score = trainer.initiate_model_trainer(train_array=train_array, test_array=test_array)

        logging.info(f"Training completed with R2 score: {r2_score}")

    except Exception as e:
        logging.error("Error occurred in training pipeline")
        raise CustomException(e, sys)

if __name__ == "__main__":
    run_training_pipeline()
