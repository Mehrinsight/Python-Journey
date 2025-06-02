import re  # Regular expression module

# Function to split a block of text into individual sentences
def split_into_sentences(text):
    # Compile a regular expression pattern to find sentence boundaries
    # Pattern: Look for punctuation (., !, ?) followed by whitespace and a capital letter
    sentence_endings = re.compile(r'(?<=[.!?])\s+(?=[A-Z])')
    
    # Split the text at those boundaries
    sentences = sentence_endings.split(text)
    
    # Strip whitespace from each sentence and remove any empty results
    cleaned_sentences = [s.strip() for s in sentences if s.strip()]
    
    return cleaned_sentences  # Return the list of clean sentences

# Example usage
text = "Hello! This is a test. Can it handle abbreviations like Dr. Smith? Yes, it can!"
sentences = split_into_sentences(text)

# Print each sentence with its index
for i, sentence in enumerate(sentences, 1):
    print(f"Sentence {i}: {sentence}")
