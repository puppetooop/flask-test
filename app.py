from flask import Flask, request
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def index():
    return """
    <h1>GM AppSec Lab</h1>
    <p>Try /search?q=your+input</p>
    """

# VULNERABLE VERSION (reflected XSS)
@app.route("/search")
def search():
    q = request.args.get("q", "")
    # Intentional vulnerability: unsanitized user input in HTML
    return f"<h1>Results for: {q}</h1>"

# SECURE VERSION (for later, after you demo the vuln)
# @app.route("/search")
# def search():
#     q = request.args.get("q", "")
#     return f"<h1>Results for: {escape(q)}</h1>"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
