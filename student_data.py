def get_student_data():
    student = {
        "name": "Rahul",
        "roll_no": 101,
        "marks": 87.5
    }
    return student

if __name__ == "__main__":
    data = get_student_data()
    print(f"Name: {data['name']} | Roll: {data['roll_no']} | Marks: {data['marks']}")
