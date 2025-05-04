import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

# Download once
nltk.download('stopwords', quiet=True)

ps = PorterStemmer()
all_stopwords = stopwords.words('english')
if 'not' in all_stopwords:
    all_stopwords.remove('not')

def preprocess_text(text):
    """
    Cleans the text for sentiment analysis using:
    - Regex cleanup
    - Lowercasing
    - Tokenizing
    - Stopword removal (excluding 'not')
    - Stemming
    """
    review = re.sub('[^a-zA-Z]', ' ', text)
    review = review.lower()
    review = review.split()
    review = [ps.stem(word) for word in review if word not in set(all_stopwords)]
    return ' '.join(review)
