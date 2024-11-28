from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from core.nlp import NLPProcessor
from core.ml import MLProcessor

router = APIRouter()
nlp = NLPProcessor()
ml = MLProcessor()

class TextInput(BaseModel):
    text: str

class TextsInput(BaseModel):
    texts: List[str]
    labels: Optional[List[str]] = None

class IntentTrainingInput(BaseModel):
    texts: List[str]
    intents: List[str]

@router.post("/analyze")
async def analyze_text(input_data: TextInput):
    """Analyze text using NLP processor"""
    try:
        result = nlp.analyze_text(input_data.text)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/classify")
async def classify_texts(input_data: TextsInput):
    """Classify or cluster texts using ML processor"""
    try:
        result = ml.process_text_classification(input_data.texts, input_data.labels)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/train-intent")
async def train_intent(input_data: IntentTrainingInput):
    """Train intent classifier"""
    try:
        ml.train_intent_classifier(input_data.texts, input_data.intents)
        return {"message": "Intent classifier trained successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/predict-intent")
async def predict_intent(input_data: TextInput):
    """Predict intent of input text"""
    try:
        result = ml.predict_intent(input_data.text)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/keywords")
async def extract_keywords(input_data: TextInput):
    """Extract keywords from text"""
    try:
        keywords = nlp.extract_keywords(input_data.text)
        return {"keywords": keywords}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/sentiment")
async def analyze_sentiment(input_data: TextInput):
    """Analyze sentiment of text"""
    try:
        sentiment = nlp.analyze_sentiment(input_data.text)
        return {"sentiment": sentiment}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/language")
async def detect_language(input_data: TextInput):
    """Detect language of text"""
    try:
        language = nlp.detect_language(input_data.text)
        return {"language": language}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
