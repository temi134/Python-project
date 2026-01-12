
maths = {"Alice", "Bob", "Charlie", "David"}
english = {"Alice", "Charlie", "Eva", "Frank"}
science = {"Bob", "Charlie", "David", "George"}

print("Students who have taken both Maths and Science:")
print(maths.intersection(science))

print("\nStudents who have taken all three subjects:")
print(maths.intersection(english).intersection(science))

print("\nAll student names:")
print(maths.union(english).union(science))

print("\nStudents who have taken English but not Maths:")
print(english.difference(maths))
