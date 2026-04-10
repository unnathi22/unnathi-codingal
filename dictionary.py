student_data = {
    "id1": {"name": "Sara",  "class": "V", "subject_integration": "english, math, science"},
    "id2": {"name": "David", "class": "V", "subject_integration": "english, math, science"},
    "id3": {"name": "Sara",  "class": "V", "subject_integration": "english, math, science"},  # duplicate of id1
    "id4": {"name": "Surya", "class": "V", "subject_integration": "english, math, science"},
}

result={}
seen_keys=[]
for student_data, details in student_data.items():
    unique_key=(details["name"],details["class"],details["subject_integration"])
    if unique_key not in seen_keys:
        seen_keys.append(unique_key)
        result[student_data]=details
print(result)
        


#    a) If unique_key is not in seen_keys:
#       - append unique_key to seen_keys
#       - store this student in result using student_id as key.
#    b) If unique_key already exists, skip (duplicate record).

# 6) Print the final unique dictionary:
#    a) Loop through result items.
#    b) Print each student_id and its details line by line.