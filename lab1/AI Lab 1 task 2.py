
def scholarship_check(score, documents, attendance, disciplinary):
    if score >= 70 and documents == True and attendance >= 75 and disciplinary == True:
        return "Review"
    else:
        return "Hold"


print("Test Case 1: All conditions satisfied")
result = scholarship_check(85, True, 90, True)
print("Expected: Review")
print("Actual:", result)
print()

print("Test Case 2: Low attendance")
result = scholarship_check(82, True, 65, True)
print("Expected: Hold")
print("Actual:", result)
print()

print("Test Case 3: Disciplinary record not clear")
result = scholarship_check(88, True, 85, False)
print("Expected: Hold")
print("Actual:", result)
print()

print("Test Case 4: Boundary test")
result = scholarship_check(70, True, 75, True)
print("Expected: Review")
print("Actual:", result)
