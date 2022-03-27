# method 1
names = ["Rohit Sharma", "KL Rahul", "Virat Kohli", "Surya Kumar Yadav"]
names.reverse()
print(names)


# method 2
print("\nMethod #2\n", names)

# method 3
print("\nMethod #3\n", names)
print(names[::-1])

# method 4
print("\nMethod #4\n", names)
for o in reversed(names):
    print(o, end=", ")

# method 5
print("\nMethod #5\n", names)
for index in range(len(names)//2):
    names[index], names[-index-1] = names[-index-1], names[index]
print("reverse list ==>", names)