# test_env.py
import os
from dotenv import load_dotenv

# TODO: Load .env file
# Hint: use load_dotenv()
load_dotenv('exercise-01-environment-setup/sentiment-classifier/.env')

# TODO: Read and print environment variables
model_name = os.getenv("MODEL_NAME")
batch_size = os.getenv("BATCH_SIZE")
device = os.getenv("DEVICE")

print(f"Model: {model_name}")
print(f"Batch Size: {batch_size}")
print(f"Device: {device}")

# TODO: Handle missing variables
db_password = os.getenv("DB_PASSWORD")
if db_password == "changeme":
    print("WARNING: Using default database password. Change in production!")

# TODO: Type conversion
batch_size_int = int(os.getenv("BATCH_SIZE", "32"))
print(f"Batch size as integer: {batch_size_int}")