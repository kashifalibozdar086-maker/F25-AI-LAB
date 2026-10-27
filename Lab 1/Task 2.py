def check(score, documents, eligible, verified):
    if score >= 70 and documents and eligible and verified:
        return "Review"
    return "Hold"

cases = [
    (85, True, True, True),
    (85, True, False, True),
    (85, True, True, False),
    (70, True, True, True)
]

for case in cases:
    print(case, "->", check(*case))