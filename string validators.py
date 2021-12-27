# This method checks if all the characters of a string are alphanumeric (a-z, A-Z and 0-9).
#You are given a string s.Your task is to find out if the string s contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.

if __name__ == '__main__':
    s = input()
    print(any([a.isalnum() for a in s]))
    print(any([a.isalpha() for a in s]))
    print(any([a.isdigit() for a in s]))
    print(any([a.islower() for a in s]))
    print(any([a.isupper() for a in s]))
