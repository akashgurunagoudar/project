import os
import sys


def calculate_health_status(avg):
    if avg >= 85:
        return "Excellent"
    elif avg >= 70:
        return "Good"
    elif avg >= 55:
        return "Moderate"
    elif avg >= 40:
        return "Risk"
    else:
        return "Critical"


def get_int_env(var_name, default):
    """Read integer env variable with safe default"""
    try:
        return int(os.getenv(var_name, default))
    except ValueError:
        return default


def main():
    # Defaults (used if Jenkins parameters are missing)
    name = os.getenv("PATIENT_NAME", "Default Patient")
    age = get_int_env("AGE", 30)

    bp = get_int_env("BP_SCORE", 75)
    sugar = get_int_env("SUGAR_SCORE", 70)
    heart = get_int_env("HEART_SCORE", 80)

    avg_score = (bp + sugar + heart) / 3
    status = calculate_health_status(avg_score)

    print("----- Patient Health Report -----")
    print(f"Name        : {name}")
    print(f"Age         : {age}")
    print(f"BP Score    : {bp}")
    print(f"Sugar Score : {sugar}")
    print(f"Heart Score : {heart}")
    print(f"Health Avg  : {avg_score:.2f}")
    print(f"Status      : {status}")


if __name__ == "__main__":
    main()
