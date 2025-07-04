# app.py
from flask import Flask, render_template, request
from qa_engine import QAEngine

app = Flask(__name__)
qa = QAEngine()

@app.route('/', methods=['GET', 'POST'])
def index():
    answer = ""
    if request.method == 'POST':
        question = request.form['question']
        answer = qa.get_answer(question)
    return render_template('index.html', answer=answer)

if __name__ == '__main__':
    app.run(debug=True)
