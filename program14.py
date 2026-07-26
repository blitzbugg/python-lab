# python program with function find "largest" which accepts a file name as parameter and return the longest line in the file. If the file is empty, return None. If the file does not exist, return -1.
def find_largest(file_name):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            if not lines:
                return None
            longest_line = max(lines, key=len)
            return longest_line.strip()
    except FileNotFoundError:
        return -1

print("Enter the file name:")
file_name = input()
result = find_largest(file_name)
if result == -1:
    print("Error: File does not exist.")
elif result is None:
    print("The file is empty.")
else:
    print("The longest line in the file is:")
    print(result)