from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    result = None

    if request.method == "POST":

        name = request.form["name"]

        english = int(request.form["english"])
        tamil = int(request.form["tamil"])
        maths = int(request.form["maths"])
        science = int(request.form["science"])
        social = int(request.form["social"])

        marks = [english, tamil, maths, science, social]
        subjects = ["English", "Tamil", "Maths", "Science", "Social"]

        total = sum(marks)
        average = total / len(marks)

        failed_subjects = []

        for i in range(len(marks)):
            if marks[i] < 40:
                failed_subjects.append(subjects[i])

        if average >= 90:
            grade = "O"
        elif average >= 80:
            grade = "A+"
        elif average >= 70:
            grade = "A"
        elif average >= 60:
            grade = "B"
        elif average >= 50:
            grade = "C"
        elif average >= 40:
            grade = "D"
        else:
            grade = "F"

        result = {
            "name": name,
            "total": total,
            "max": max(marks),
            "min": min(marks),
            "grade": grade,
            "failed": failed_subjects,
            "status": "FAIL" if failed_subjects else "PASS"
        }

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)