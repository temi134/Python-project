names = {}
maths = {}
science = {}

while True:
    roll = input("Enter student number (or type 'stop' to finish): ")

    if roll == "stop":
        break

    name = input("Enter student name: ")
    maths_mark = int(input("Enter maths marks: "))
    science_mark = int(input("Enter science marks: "))

    names[roll] = name
    maths[roll] = maths_mark
    science[roll] = science_mark

print("\n--- Stored Data ---")
print("Roll → Name:", names)
print("Roll → Maths:", maths)
print("Roll → Science:", science)
print()


print("Name | Maths | Science | Total | Percentage")


for roll in names:
    m = maths[roll]
    s = science[roll]
    total = m + s
    percentage = total / 2

    print(names[roll], m, s, total, percentage)
