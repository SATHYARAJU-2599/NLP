# Write a Python script that:
# 1. Tokenizes a sample paragraph into words and sentences.
import nltk
import spacy
from gensim.utils import simple_preprocess
from collections import Counter

# Download necessary NLTK data
nltk.download('stopwords')
nltk.download('punkt')
# Download the 'punkt_tab' data package
nltk.download('punkt_tab')

stop_words = nltk.corpus.stopwords.words('english')
nlp = spacy.load("en_core_web_sm")

def preprocess_text(text):
    # 1. Tokenization using Gensim
    tokens = simple_preprocess(text.lower())

    # 2. Remove stopwords
    tokens = [token for token in tokens if token not in stop_words]

    # 3. Lemmatization using spaCy
    doc = nlp(" ".join(tokens))
    lemmas = [token.lemma_ for token in doc]

    return lemmas

def tokenize_sentences(text):
    sentences = nltk.sent_tokenize(text)
    return sentences

# Example usage
sample_paragraph = "This is a sample paragraph. It contains multiple sentences. Tokenization is important."

# Tokenize into words and lemmatize
preprocessed_tokens = preprocess_text(sample_paragraph)
print("Lemmatized Tokens:", preprocessed_tokens)

# Tokenize into sentences
sentences = tokenize_sentences(sample_paragraph)
print("\nSentences:", sentences)

# Word counts (optional)
word_counts = Counter(preprocessed_tokens)
print("\nWord Counts:")
for word, count in word_counts.items():
    print(f"{word}: {count}")

