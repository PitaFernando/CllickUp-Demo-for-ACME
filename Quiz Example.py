from Preguntas import Question

question_prompts = [
    "What color are apples?\n(a) Red/Greed\n(b) Purple\n(c) Orange\n\n",
    "What color are bananas?\n(a) Yellow\n(b) Magenta\n(c) Teal\n\n",
    "What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Green\n\n"
]
preguntas = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "a"),
    Question(question_prompts[2], "b")
]

def run_test(preguntas):
    score = 0
    for test in preguntas:
        answer = input(test.prompt)
        if answer == test.answer:
            score += 1
    print(f"You answered {score} out of {len(preguntas)} preguntas.")

run_test(preguntas)