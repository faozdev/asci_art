import os

def validate_file_path(file_path):
    
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File does not found {file_path}")
    return True

def create_output_directory(directory_path):
    
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
