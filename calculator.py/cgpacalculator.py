def calculate_cgpa():
    """Nigerian University CGPA Calculator"""
    
    grade_points = {
        'A': 5.0, 'B': 4.0, 'C': 3.0, 'D': 2.0, 'E': 1.0, 'F': 0.0
    }
    
    print("=== Nigerian University CGPA Calculator ===")
    print("Grades: A=5, B=4, C=3, D=2, E=1, F=0\n")

    try:
        no_of_courses = int(input("How many courses did you offer this semester? : "))
        if no_of_courses <= 0:
            print("Number of courses must be greater than zero!")
            return
    except ValueError:
        print("Invalid input! Please enter a valid number for courses.")
        return

    courses = []
    
    for _ in range(no_of_courses):
        course = input("Enter course code: ").strip().upper()
        
        try:
            units = int(input(f"Credit units for {course}: "))
            grade = input(f"Grade for {course} (A/B/C/D/E/F): ").strip().upper()
            
            if grade not in grade_points:
                print("Invalid grade! Use A, B, C, D, E, or F.")
                continue
            if units <= 0:
                print("Units must be positive!")
                continue
            
            courses.append((course, units, grade, grade_points[grade]))
            print(f"  Added: {course} | {units} units | Grade {grade} ({grade_points[grade]} points)\n")
        
        except ValueError:
            print("Invalid input! Please enter valid numbers for units.")
            continue
    
    if not courses:
        print("No courses entered.")
        return
    
    # Calculate CGPA
    total_units = sum(c[1] for c in courses)
    total_quality_points = sum(c[1] * c[3] for c in courses)
    cgpa = total_quality_points / total_units

    # Determine class of degree
    if cgpa >= 4.50:
        degree_class = "First Class Honours"
    elif cgpa >= 3.50:
        degree_class = "Second Class Upper (2:1)"
    elif cgpa >= 2.40:
        degree_class = "Second Class Lower (2:2)"
    elif cgpa >= 1.50:
        degree_class = "Third Class"
    elif cgpa >= 1.00:
        degree_class = "Pass"
    else:
        degree_class = "Fail"
    
    # Display results
    print("\n" + "="*45)
    print(f"{'COURSE':<20} {'UNITS':>5} {'GRADE':>6} {'POINTS':>7}")
    print("-"*45)
    for name, units, grade, points in courses:
        print(f"{name:<20} {units:>5} {grade:>6} {points:>7.1f}")
    print("="*45)
    print(f"Total Credit Units : {total_units}")
    print(f"Total Quality Points : {total_quality_points:.1f}")
    print(f"CGPA               : {cgpa:.2f} / 5.00")
    print(f"Class of Degree    : {degree_class}")
    print("="*45)

if __name__ == "__main__":
    calculate_cgpa()