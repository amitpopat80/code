# file: split_python_files.py

import os 

def split_file_into_tokens(file_path: str, output_directory: str, tokens_per_file: int = 2000):
    """Split a Python file into multiple files, each containing a specified number of tokens."""
    with open(file_path, 'r') as file:
        content = file.read()
    
    # Split content into tokens (assuming whitespace as a delimiter)
    tokens = content.split()
    
    # Create output directory if it doesn't exist
    os.makedirs(output_directory, exist_ok=True)
    
    # Split tokens into chunks
    for i in range(0, len(tokens), tokens_per_file):
        chunk = tokens[i:i + tokens_per_file]
        output_file_path = os.path.join(output_directory, f"{os.path.basename(file_path).replace('.py', '')}_part_{i // tokens_per_file + 1}.py")
        
        with open(output_file_path, 'w') as output_file:
            output_file.write(' '.join(chunk))


def process_directory(directory: str, output_directory: str):
    """Process all Python files in the specified directory and its subdirectories."""
    for root, _, filenames in os.walk(directory):
        for filename in filenames:
            if filename.endswith('.py'):
                file_path = os.path.join(root, filename)
                # Calculate the number of tokens in the file
                with open(file_path, 'r') as file:
                    content = file.read()
                    token_count = len(content.split())
                
                # Split the file if it has more than 2000 tokens
                if token_count > 2000:
                    relative_path = os.path.relpath(root, directory)
                    output_dir = os.path.join(output_directory, relative_path)
                    split_file_into_tokens(file_path, output_dir)

# Example usage
if __name__ == "__main__":
    input_directory = "path/to/your/python/files"  # Change this to your input directory
    output_directory = "path/to/output/directory"  # Change this to your desired output directory
    process_directory(input_directory, output_directory)
