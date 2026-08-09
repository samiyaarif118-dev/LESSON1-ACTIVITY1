student_data ={
    "id1": {"name": "fatima", "class": "IV" , "subject": "science"},
    "id2": {"name": "ayesha", "class": "III", "subject": "geography"},
    "id3": {"name": "fatima", "class": "IV" , "subject": "science"},
    "id4": {"name": "alex", "class": "V", "subject": "geography"},
    }
print("Original student data : ", student_data)

print("detail of id1 : ", student_data.get("id1" , "not found"))
print("detail of id5 : ", student_data.get("id5" , "not found"))

student_data ["id5"] = {"name": "yesmeen", "class": "X" , "subject": "maths"}

print("id5 student data : ", student_data)

student_data["id2"] = {"name": "ayesha", "class": "VII" , "subject": "chemistry"}
print("updated student data : ", student_data)

cleaned_data = {}
seen_record = []
for student_id , detail in student_data.items():
    unique_record = (detail["name"], detail["class"], detail["subject"])
    if unique_record not in seen_record:
        seen_record.append(unique_record)
        cleaned_data[student_id] = detail
print("cleaned student data : ", cleaned_data)

student_data.pop("id4",None)
print(len(student_data))

for student_id, detail in student_data.items():
    print(student_id, ":", detail)






      
      
