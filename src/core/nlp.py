import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.sentiment import SentimentIntensityAnalyzer
from typing import List, Dict, Any

class NLPProcessor:
    def __init__(self):
        """Initialize NLP components and download required NLTK data"""
        try:
            nltk.data.find('tokenizers/punkt')
        except LookupError:
            nltk.download('punkt')
        try:
            nltk.data.find('corpora/stopwords')
        except LookupError:
            nltk.download('stopwords')
        try:
            nltk.data.find('sentiment/vader_lexicon')
        except LookupError:
            nltk.download('vader_lexicon')
        
        self.stop_words = set(stopwords.words('english'))
        self.sia = SentimentIntensityAnalyzer()

    def analyze_text(self, text: str) -> Dict[str, Any]:
        """Perform comprehensive text analysis"""
        return {
            "tokens": self.tokenize(text),
            "sentences": self.sentence_split(text),
            "sentiment": self.analyze_sentiment(text),
            "word_count": len(self.tokenize(text)),
            "sentence_count": len(self.sentence_split(text))
        }

    def tokenize(self, text: str) -> List[str]:
        """Tokenize text into words and remove stop words"""
        tokens = word_tokenize(text.lower())
        return [token for token in tokens if token not in self.stop_words]

    def sentence_split(self, text: str) -> List[str]:
        """Split text into sentences"""
        return sent_tokenize(text)

    def analyze_sentiment(self, text: str) -> Dict[str, float]:
        """Analyze sentiment of text"""
        return self.sia.polarity_scores(text)

    def extract_keywords(self, text: str, top_n: int = 5) -> List[str]:
        """Extract key terms from text"""
        tokens = self.tokenize(text)
        freq_dist = nltk.FreqDist(tokens)
        return [word for word, _ in freq_dist.most_common(top_n)]

    def detect_language(self, text: str) -> str:
        """Detect language of text (basic implementation)"""
        try:
            from langdetect import detect
            return detect(text)
        except:
            return "en"  # Default to English if langdetect not installed
