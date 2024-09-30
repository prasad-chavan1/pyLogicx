from pyLogix.logger import logger, set_log_level

# Set the log level to DEBUG to capture all logs
set_log_level('DEBUG')

# Function to count the number of words in a given text
def count_words(text):
    """
    Count the number of words in a given text.

    :param text: The input text to process.
    :return: The count of words in the text.
    """
    logger.info("Count Words function called.")
    if not isinstance(text, str):
        logger.error("Invalid input: Input must be a string.")
        return 0
    
    word_count = len(text.split())
    logger.info(f"Word count calculated: {word_count}")
    return word_count

# Function to reverse the given text
def reverse_text(text):
    """
    Reverse the given text.

    :param text: The input text to reverse.
    :return: The reversed text.
    """
    logger.info("Reverse Text function called.")
    if not isinstance(text, str):
        logger.error("Invalid input: Input must be a string.")
        return ""
    
    reversed_text = text[::-1]
    logger.info(f"Reversed text: {reversed_text}")
    return reversed_text

# Function to check if a substring exists within the given text
def find_substring(text, substring):
    """
    Check if a substring exists within the given text.

    :param text: The input text to search.
    :param substring: The substring to find.
    :return: True if the substring exists, otherwise False.
    """
    logger.info("Find Substring function called.")
    if not isinstance(text, str) or not isinstance(substring, str):
        logger.error("Invalid input: Both inputs must be strings.")
        return False

    exists = substring in text
    logger.info(f"Substring '{substring}' found: {exists}")
    return exists

# Test the functions
if __name__ == "__main__":
    # Sample text and substring for testing
    text = "Hello, this is a sample text for testing."
    substring = "sample"

    # Count words
    word_count = count_words(text)
    print(f"Word Count: {word_count}")

    # Reverse text
    reversed_text = reverse_text(text)
    print(f"Reversed Text: {reversed_text}")

    # Find substring
    exists = find_substring(text, substring)
    print(f"Does the substring exist? {exists}")
