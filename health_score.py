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


def main():
    name = input("Enter Patient Name: ")
    age = int(input("Enter Age: "))

    bp = int(input("Enter BP Score (0-100): "))
    sugar = int(input("Enter Sugar Level Score (0-100): "))
    heart = int(input("Enter Heart Rate Score (0-100): "))

    avg_score = (bp + sugar + heart) / 3
    status = calculate_health_status(avg_score)

    print("\n----- Patient Health Report -----")
    print(f"Name        : {name}")
    print(f"Age         : {age}")
    print(f"Health Avg  : {avg_score:.2f}")
    print(f"Status      : {status}")


if __name__ == "__main__":
    main()