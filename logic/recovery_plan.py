
def generate_recovery_plan(data):
    plan = []

    if data["backlog_size"] > 7:
        plan.append("Clear one backlog topic (30 minutes).")

    if data["topic_clarity"] < 5:
        plan.append("Revise fundamentals of one weak topic.")

    if data["sleep_hours"] < 6:
        plan.append("Prioritize at least 7 hours of sleep tonight.")

    if data["planning_confidence"] < 5:
        plan.append("Create a simple 3-day study plan.")

    return plan[:3]
