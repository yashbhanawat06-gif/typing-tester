from flask import Flask, render_template, request
import random

app = Flask(__name__)


sentences = [
    "You know nothing John Snow!",
    "Mitochondria is the powerhouse of the cell.",
    "The quick brown fox jumps over the lazy dog.",
    "A journey of a thousand miles begins with a single step.",
    "This is the way for us to reference the object of the class.",
    "Time and tide waits for none.",
    "I woke up, I saw her. Thats all I know."
]


def measure_accuracy(user_input, original_text):
    user_words = user_input.split()
    original_words = original_text.split()

    correct = sum(1 for uw, ow in zip(user_words, original_words) if uw == ow)
    total = len(original_words)

    return round((correct / total) * 100, 2) if total > 0 else 0



@app.route('/')
def home():
    text = random.choice(sentences)
    return render_template('index.html', text=text)



@app.route('/result', methods=['POST'])
def result():
    user_input = request.form.get('user_input', '')
    original_text = request.form.get('original_text', '')

   
    time_taken = float(request.form.get('time_taken', 0))

  
    word_count = len(user_input.split())

  
    if time_taken > 0:
        wpm = round((word_count / time_taken) * 60, 2)
    else:
        wpm = 0


    accuracy = measure_accuracy(user_input, original_text)

    return render_template(
        'result.html',
        original=original_text,
        typed=user_input,
        time_taken=round(time_taken, 2),
        wpm=wpm,
        accuracy=accuracy
    )



import os

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Render gives PORT, local uses 5000
    app.run(host='0.0.0.0', port=port, debug=True)