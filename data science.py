import numpy as np
data_type = [("name", "S15"),("class", int), ("height", float)]
student_details = [("Samiya",8, 5.2),("Alex", 4, 5.1),("Hafsa",4,5.2),("Maha",7,5.1)]

x = np.array(student_details, dtype=data_type)
print(x)

print(np.sort(x,order="height"))

