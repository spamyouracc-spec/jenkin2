course_name = "Python Jenkins Automation"
students_enrolled = 70

with open("build_report.txt", "w", encoding="utf-8") as report:
    report.write(f"Course: {course_name}\n")
    report.write(f"Students enrolled: {students_enrolled}\n")

print("Report generated successfully.")
