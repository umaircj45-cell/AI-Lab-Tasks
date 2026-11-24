def scholarship_check(score, documents, attendance, disciplinary):
    if score >= 70 and documents == True and attendance >= 75 and disciplinary == True:
        return "Review"
    else:
        return "Hold"


print("Test Case 1: All conditions satisfied")
print("Input: score=85, documents=True, attendance=90, disciplinary=True")
result = scholarship_check(85, True, 90, True)
print("Expected: Review")
print("Actual:", result)
print("Reason: The score, documents, attendance, and disciplinary conditions are all satisfied.")
print()

print("Test Case 2: Attendance condition fails")
print("Input: score=82, documents=True, attendance=65, disciplinary=True")
result = scholarship_check(82, True, 65, True)
print("Expected: Hold")
print("Actual:", result)
print("Reason: Attendance is below the required 75 percent.")
print()

print("Test Case 3: Disciplinary condition fails")
print("Input: score=88, documents=True, attendance=85, disciplinary=False")
result = scholarship_check(88, True, 85, False)
print("Expected: Hold")
print("Actual:", result)
print("Reason: The disciplinary record is not clear.")
print()

print("Test Case 4: Boundary test")
print("Input: score=70, documents=True, attendance=75, disciplinary=True")
result = scholarship_check(70, True, 75, True)
print("Expected: Review")
print("Actual:", result)
print("Reason: The score and attendance are exactly at their minimum thresholds, so the conditions pass.")
