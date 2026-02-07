from flask import Flask, request, render_template_string, redirect
from tinydb import TinyDB

app = Flask(__name__)
db = TinyDB("comments.json")


@app.route("/")
def index():
    comments_html = ""
    for c in db.all():
        comments_html += f"""
        <div>
            <b>{c['username']}</b>: {c['comment']}
        </div>
        """

    return render_template_string(f"""
    <h1>Komen dong</h1>

    <h3>Comments</h3>
    {comments_html}

    <hr>
    <form method="POST" action="/comment">
        Username: <input name="username"><br><br>
        Comment: <textarea name="comment"></textarea><br><br>
        <button type="submit">Submit</button>
    </form>

    <hr>
    <form action="/search">
        <input name="q" placeholder="Search">
        <button type="submit">Search</button>
    </form>
    """)

# =====================
# ADD COMMENT
# =====================
@app.route("/comment", methods=["POST"])
def comment():
    db.insert({
        "username": request.form.get("username"),
        "comment": request.form.get("comment")
    })
    return redirect("/")


@app.route("/search")
def search():
    q = request.args.get("q", "")
    return render_template_string(f"""
        <h1>Search Result</h1>
        You searched for: {q}
        <br><br>
        <a href="/">Back</a>
    """)

if __name__ == "__main__":
    app.run(debug=True)
