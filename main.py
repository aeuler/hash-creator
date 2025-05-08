import hashlib

def create_hash(text, algorithm='sha256'):
    """
    Creates a hash of the given text using the specified algorithm.

    Parameters:
    - text (str): The input string to hash.
    - algorithm (str): The hashing algorithm (e.g., 'sha256', 'md5', 'sha1').

    Returns:
    - str: Hexadecimal hash string.
    """
    try:
        hash_func = hashlib.new(algorithm)
        hash_func.update(text.encode('utf-8'))
        return hash_func.hexdigest()
    except ValueError:
        return f"Error: Unsupported hash algorithm '{algorithm}'"

# Example usage:
if __name__ == "__main__":
    message = input("Enter text to hash: ")
    algo = input("Enter hash algorithm (e.g., sha256, md5, sha1): ").lower()
    hash_output = create_hash(message, algo)
    print(f"Hashed output:\n{hash_output}")
