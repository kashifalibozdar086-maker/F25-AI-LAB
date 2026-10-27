def conversational_test(answer):
    if len(answer) > 20:
        return "Fluent response"
    return "Short response"

answers = [
    "The scholarship deadline is tomorrow.",
    "The deadline is tomorrow because today is yesterday."
]

for answer in answers:
    print("Answer:", answer)
    print("Result:", conversational_test(answer))
    print()