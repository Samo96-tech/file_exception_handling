#!/usr/bin/env python3

def main():
    filename = input("Enter the filename to read: ")

    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return
    except PermissionError:
        print(f"Error: Permission denied when accessing '{filename}'.")
        return
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return

    print(f"Contents of '{filename}' (first 500 characters):")
    print(content[:500])

if __name__ == '__main__':
    main()
