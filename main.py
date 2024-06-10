
from flask import Flask, render_template

app = Flask(__name__)

articles = [
    {
        "id": 1,
        "headline": "Headline 1",
        "snippet": "Snippet 1",
    },
    {
        "id": 2,
        "headline": "Headline 2",
        "snippet": "Snippet 2",
    },
    # ...
]

@app.route('/')
def index():
    return render_template('index.html', articles=articles)

@app.route('/article/<article_id>')
def article(article_id):
    article = next((article for article in articles if article["id"] == int(article_id)), None)
    if article is None:
        return render_template('404.html'), 404
    return render_template('article.html', article=article)

if __name__ == '__main__':
    app.run(debug=True)
