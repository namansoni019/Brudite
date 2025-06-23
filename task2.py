def read_lines(filename: str) -> list[str]:

    try:
        with open(filename, 'r') as f:
            return f.readlines()
    except Exception as e:
        if isinstance(e, FileNotFoundError):
            print(f"File '{filename}' not found.")
        elif isinstance(e, PermissionError):
            print(f"Permission denied while accessing '{filename}'.")
        else:
            print(f"An unexpected error occurred: {e}")
        return []

def main():
    file_name = input("Enter the file name: ")
    lines = read_lines(file_name)

    if lines:
        print(f"The file has {len(lines)} lines.")
    else:
        print("No lines to display.")

if __name__ == "__main__":
    main()
