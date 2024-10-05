import hashlib
import argparse

def calculate_md5(file_path):
    """Calculate MD5 hash of a file."""
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def calculate_sha256(file_path):
    """Calculate SHA-256 hash of a file."""
    hash_sha256 = hashlib.sha256()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_sha256.update(chunk)
    return hash_sha256.hexdigest()

def main():
    parser = argparse.ArgumentParser(description="Digital Evidence Integrity Checker")
    parser.add_argument("file_path", help="Path to the file to be hashed")
    args = parser.parse_args()
    
    file_path = args.file_path

    try:
        md5_hash = calculate_md5(file_path)
        sha256_hash = calculate_sha256(file_path)
        
        print(f"MD5 Hash: {md5_hash}")
        print(f"SHA-256 Hash: {sha256_hash}")

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except PermissionError:
        print(f"Error: Permission denied for file '{file_path}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
