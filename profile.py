def create_profile(name, student_id, bio):
    with open('student_profile.txt', 'w') as f:
        f.write(f"Name: {name}\n")
        f.write(f"Student ID: {student_id}\n")
        f.write(f"Bio: {bio}\n")
    print("Profile created successfully")

if __name__ == "__main__":
    create_profile("Hassam Hidayat", "22SE22", "I am a student learning software construction.")
