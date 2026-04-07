
from flask import Flask, render_template, request
from logic.risk_engine import compute_risk, explain_risk
from logic.recovery_plan import generate_recovery_plan

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    explanation = None
    plan = None

    if request.method == "POST":
        data = {
            "study_hours": float(request.form["study_hours"]),
            "sleep_hours": float(request.form["sleep_hours"]),
            "screen_time": float(request.form["screen_time"]),
            "stress_level": int(request.form["stress_level"]),
            "backlog_size": int(request.form["backlog_size"]),
            "topic_clarity": int(request.form["topic_clarity"]),
            "planning_confidence": int(request.form["planning_confidence"]),
        }

        score, level = compute_risk(data)
        result = f"{level} ({score})"
        explanation = explain_risk(level)
        plan = generate_recovery_plan(data)

    return render_template("index.html", result=result, explanation=explanation, plan=plan)

if __name__ == "__main__":
    app.run(debug=True, port=5001)
