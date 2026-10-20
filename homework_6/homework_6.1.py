result = ["PASS", "FAIL", "SKIP", "PASS", "FAIL", "SKIP", "PASS"]


def passed(n):
    if n == len(result):
        return 0
    else:
        if result[n] == "PASS":
            return passed(n + 1) + 1
        if result[n] != "PASS":
            return passed(n + 1)


passed_count = passed(0)
print(passed_count)
