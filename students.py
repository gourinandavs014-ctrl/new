import matplotlib.pyplot as plt
import numpy as np

students = ["Arun","Bina", "Chetan","Divya" ,"Esha"]
marks = [75, 85, 90, 70, 95]

plt.plot(students,marks,marker='o')

plt.title("Students Marks Line Chart")
plt.xlabel("Students")
plt.ylabel("Marks")

plt.grid()

plt.show()