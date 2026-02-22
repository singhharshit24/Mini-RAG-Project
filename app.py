from flask import Flask, render_template, request, redirect
import os
from rag_core import build_index, ask, DOCUMENTS_PATH, add_manual_text, get_manual_text_count

app = Flask(__name__)

# Build index at startup
build_index()

@app.route("/", methods=["GET", "POST"])
def home():
    answer = None

    if request.method == "POST":

        # File upload
        if "file" in request.files:
            file = request.files["file"]
            if file.filename != "":
                file_path = os.path.join(DOCUMENTS_PATH, file.filename)
                file.save(file_path)
                build_index()
                return redirect("/")

        # Manual text input (in-memory)
        if "manual_text" in request.form:
            manual_text = request.form["manual_text"]
            if manual_text.strip():
                add_manual_text(manual_text)
                return redirect("/")

        # Question
        if "question" in request.form:
            question = request.form["question"]
            answer = ask(question)

    return render_template("index.html", answer=answer, manual_count=get_manual_text_count())

if __name__ == "__main__":
    app.run(debug=True)
