# qa_engine.py
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class QAEngine:
    def __init__(self, data_path='data/weapons.json'):
        with open(data_path, 'r', encoding='utf-8') as f:
            self.data = json.load(f)
        self.questions = [item['question'] for item in self.data]
        self.answers = [item['answer'] for item in self.data]
        self.vectorizer = TfidfVectorizer()
        self.question_vectors = self.vectorizer.fit_transform(self.questions)

    def get_answer(self, query):
        query_vec = self.vectorizer.transform([query])
        similarity = cosine_similarity(query_vec, self.question_vectors).flatten()
        idx = similarity.argmax()
        if similarity[idx] > 0.2:
            return self.answers[idx]
        return "Sorry, I don't have information on that weapon."
