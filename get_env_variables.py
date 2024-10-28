from dotenv import dotenv_values
from os import path

def load_environment_variables(file_path):
    try:
        # Check if the file path exists
        if not path.exists(file_path):
            raise FileNotFoundError(f"The file {file_path} does not exist.")
        config = dotenv_values(file_path)
        return config
    except FileNotFoundError as e:
        print(f"File not found error: {e}")  # Print the error to the console
        return {} 
    except Exception as e:
        print(f"Error loading environment variables from {file_path}: {e}")  # Print the error
        return {}