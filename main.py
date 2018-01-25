from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def display_scores():
    """displays scores"""
    scores = [
        [71611995, 5, 5, 5, 6, 7, 7, 9],
        [71611995, 5, 5, 5, 6, 7, 7, 9],
        [71611995, 5, 5, 5, 6, 7, 7, 9],
        [71611995, 5, 5, 5, 6, 7, 7, 9],
        [71611995, 5, 5, 5, 6, 7, 7, 9],
        [71611995, 5, 5, 5, 6, 7, 7, 9],
    ]
    return render_template('template.html', scores=scores)


if __name__ == '__main__':
    app.run(port=8080, debug=True)
