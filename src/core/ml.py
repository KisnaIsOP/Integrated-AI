from typing import List, Dict, Any
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

class MLProcessor:
    def __init__(self):
        """Initialize ML components"""
        self.vectorizer = TfidfVectorizer()
        self.scaler = StandardScaler()
        self.text_classifier = None
        self.intent_classifier = None

    def process_text_classification(self, texts: List[str], labels: List[str] = None) -> Dict[str, Any]:
        """Process text classification task"""
        # Convert texts to TF-IDF features
        features = self.vectorizer.fit_transform(texts)
        
        if labels is None:
            # If no labels provided, perform clustering
            return self._cluster_texts(features)
        else:
            # If labels provided, perform classification
            return self._classify_texts(features, labels)

    def _cluster_texts(self, features, n_clusters: int = 3) -> Dict[str, Any]:
        """Cluster texts using K-means"""
        kmeans = KMeans(n_clusters=n_clusters, random_state=42)
        clusters = kmeans.fit_predict(features)
        
        return {
            "clusters": clusters.tolist(),
            "centroids": kmeans.cluster_centers_.tolist(),
            "inertia": kmeans.inertia_
        }

    def _classify_texts(self, features, labels: List[str]) -> Dict[str, Any]:
        """Classify texts using a simple classifier"""
        from sklearn.naive_bayes import MultinomialNB
        
        if self.text_classifier is None:
            self.text_classifier = MultinomialNB()
            self.text_classifier.fit(features, labels)
        
        predictions = self.text_classifier.predict(features)
        probabilities = self.text_classifier.predict_proba(features)
        
        return {
            "predictions": predictions.tolist(),
            "probabilities": probabilities.tolist()
        }

    def train_intent_classifier(self, texts: List[str], intents: List[str]):
        """Train intent classification model"""
        features = self.vectorizer.fit_transform(texts)
        from sklearn.linear_model import LogisticRegression
        
        self.intent_classifier = LogisticRegression(max_iter=1000)
        self.intent_classifier.fit(features, intents)

    def predict_intent(self, text: str) -> Dict[str, Any]:
        """Predict intent of input text"""
        if self.intent_classifier is None:
            return {"error": "Intent classifier not trained"}
        
        features = self.vectorizer.transform([text])
        intent = self.intent_classifier.predict(features)[0]
        proba = self.intent_classifier.predict_proba(features)[0]
        
        return {
            "intent": intent,
            "confidence": float(max(proba))
        }

    def preprocess_numerical_data(self, data: np.ndarray) -> np.ndarray:
        """Preprocess numerical data"""
        return self.scaler.fit_transform(data)
