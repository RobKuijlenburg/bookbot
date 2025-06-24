def count_words(text):
    """
    Counts the number of words in a given text.

    Args:
        text (str): The text to count words in.

    Returns:
        int: The number of words in the text.
    """
    words = text.split()
    return len(words)

def count_lowercase_letters(text):
    result = {}
    for c in text:
        if c.isalpha():
            key = c.lower()
            if key in result:
                result[key] += 1
            else:
                result[key] = 1
    return result

def sort_dict(dict):
    result = []
    for key in dict:
        result.append({"char": key, "count": dict[key]})
    result.sort(key=lambda x: x["count"], reverse=True)
    return result
