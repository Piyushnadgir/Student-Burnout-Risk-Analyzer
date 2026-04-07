
def compute_risk(data):
    stress = data["stress_level"] / 10
    backlog = data["backlog_size"] / 15
    sleep = 1 - (data["sleep_hours"] / 9)
    clarity = 1 - (data["topic_clarity"] / 10)
    planning = 1 - (data["planning_confidence"] / 10)

    score = (
        0.30 * stress +
        0.25 * backlog +
        0.20 * sleep +
        0.15 * clarity +
        0.10 * planning
    )

    score = round(score, 3)

    if score < 0.4:
        level = "Low"
    elif score < 0.65:
        level = "Medium"
    else:
        level = "High"

    return score, level

def explain_risk(level):
    if level == "Low":
        return "Current patterns suggest manageable academic pressure."
    elif level == "Medium":
        return "Sustained workload detected. Small adjustments recommended."
    else:
        return "High strain detected. Early recovery actions advised."
