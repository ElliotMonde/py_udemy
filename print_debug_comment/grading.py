students = {
    "hermoine": 91,
    "potter": 55,
    "weasley": 61,
    "draco": 44,
    "neville": 1
}

for student in students:
    match(students[student]):
        case f_grade if 0 <= f_grade <= 25:
            students[student] = {f_grade,"F"}
            print(f"{student} scored an F.")
        case d_grade if 25 < d_grade <=50:
            students[student] = {"score":f_grade,"grade":"D"}
            print(f"{student} scored a D.")
        case e_grade if 50< e_grade <= 60:
            print(f"{student} scored a C.")
        case e_grade if 60 < e_grade <= 70:
            print(f"{student} scored a B.")
        case a_grade if 70 < a_grade:
            print(f"{student} scored an A.")
        case _:
            print("invalid grade.")
print(students)

new_dict = {
    "some list" : [2,"this", "is"],
    1:5
}
print(new_dict)
