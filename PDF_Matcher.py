import hashlib
import sys


def hash_file(filename):
    """Return the SHA-1 hash of the given file."""
    h = hashlib.sha1()
    try:
        with open(filename, "rb") as file:
            while chunk := file.read(1024):
                h.update(chunk)
        return h.hexdigest()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file '{filename}': {e}")
        sys.exit(1)


def compare_files(file1, file2):
    """Compare two files by their SHA-1 hash."""
    hash1 = hash_file(file1)
    hash2 = hash_file(file2)

    if hash1 == hash2:
        print("✅ These files are identical")
    else:
        print("❌ These files are not identical")


if __name__ == "__main__":
    file1 = "pd1.pdf"
    file2 = "pd1.pdf"
    compare_files(file1, file2)
