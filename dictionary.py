w = {
    "id1": {"name": "sara", "class": "V" , "subject": "computerscience"},
    "id2": {"name": "fatima", "class": "X" , "subject": "english"},
    "id3": {"name": "sara", "class": "V" , "subject": "computerscience"},
    "id4": {"name": "samiiya", "class": "VII" , "subject": "maths"}
}
result = {}
seen_keys = []
for student_id , detail in w.items():
  unique_key = (detail["name"],detail["class"], detail["subject"])
  if unique_key not in seen_keys:
    seen_keys.append(unique_key)
    result[student_id]= detail
for x,y in result.items():
  print(x, ":" , y)


test_dict = {"codingal" : 2, "is" : 2, "best" : 2, "for" : 2, "coding" : 1}
print("the original dictionary : " + str(test_dict))

k = 2
res = 0
for key in test_dict:
  if test_dict[key] == k:
    res = res + 1
print("frequency of k is : " + str(res))

