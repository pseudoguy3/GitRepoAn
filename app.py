from flask import Flask, request, render_template
from services.Validator import RepoValidator   

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def repo_form():
    error = None
    owner = None
    contributors = None
    repo_url = None

    if request.method == "POST":
        repo_url = request.form.get("repo_url")
        if not repo_url:
            error = "Repo URL required"
        else:
            validator = RepoValidator()
            print(f"-->Validating repo URL: {repo_url}")
            try:
                result = validator.validate_repo(repo_url)
                owner = result.get("creator")
                contributors = result.get("contributors")
                languages = result.get("languages")
                issues = result.get("issues")
            except Exception as e:
                error = str(e)
        if not error:
            # If no error, show analysis page
            return render_template("Analysis.html", owner=owner, contributors=contributors, repo_url=repo_url, languages=languages, issues=issues)
    # On GET or error, show form
    return render_template("repoForm.html", error=error)

if __name__ == "__main__":
    app.run(debug=True)