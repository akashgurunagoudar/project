from health_score import calculate_health_status

def test_excellent():
    assert calculate_health_status(90) == "Excellent"

def test_good():
    assert calculate_health_status(75) == "Good"

def test_moderate():
    assert calculate_health_status(60) == "Moderate"

def test_risk():
    assert calculate_health_status(45) == "Risk"

def test_critical():
    assert calculate_health_status(30) == "Critical"