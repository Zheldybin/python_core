for i in range(1, 31):
    if i % 3 == 0 and i % 5 == 0:
        print("BugTest")
    elif i % 5 == 0:
        print("Test")
    elif i % 3 == 0:
        print("Bug")
    else:
        print(i)
