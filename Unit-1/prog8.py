def count_vowels(text):
    """Count the number of vowels in the string."""
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

def string_length(text):
    """Calculate the length of the string without using len()."""
    length = 0
    for _ in text:
        length += 1
    return length

def reverse_string(text):
    """Reverse the given string."""
    return text[::-1]

def find_and_replace(text, find_str, replace_str):
    """Find and replace a substring in the string."""
    return text.replace(find_str, replace_str)

def is_palindrome(text):
    """Check if the string is a palindrome."""
    cleaned_text = ''.join(text.split()).lower()
    return cleaned_text == cleaned_text[::-1]

def main():
    print("STRING OPERATIONS PROGRAM")
    
    text = input("Enter a string: ")
    
    print("RESULTS:")
    
    vowel_count = count_vowels(text)
    print(f"a) Number of vowels: {vowel_count}")
    
    length = string_length(text)
    print(f"b) Length of string: {length}")
    
    reversed_text = reverse_string(text)
    print(f"c) Reversed string: {reversed_text}")
    
    print("\nd) Find and Replace Operation:")
    find_str = input("   Enter text to find: ")
    replace_str = input("   Enter text to replace with: ")
    modified_text = find_and_replace(text, find_str, replace_str)
    print(f"   Original: {text}")
    print(f"   Modified: {modified_text}")
    
    palindrome_result = is_palindrome(text)
    print(f"\ne) Palindrome check: {'Yes' if palindrome_result else 'No'}")
    
    print("ADDITIONAL STATISTICS:")
    print(f"Original string: '{text}'")
    print(f"String length (using built-in len() for verification): {len(text)}")
    print(f"Vowel percentage: {(vowel_count/length)*100:.2f}%" if length > 0 else "Vowel percentage: 0%")

if __name__ == "__main__":
    main()
