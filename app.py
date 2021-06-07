class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer


question_asked = [
    "How many cards are there in a pack of cards (not incl. jokers)?\n(a)75\n(b)52\n(c)71\n\n",
    "Who is the South African born CEO of SpaceX and the brains behind Tesla?\n(a)Elan Musk\n(b)Elon Must\n(c)Elon Musk\n\n",
    "What is the largest country by area in the world? \n(a)China\n(b)India\n(c)Russia\n\n",
    "What mountain range would you find in India, China and Nepal (amongst other countries)?\n(a)Mount K2\n(b)Mount Himalayas\n(c)Kanchanjunga\n\n",
    "Who was assassinated, leading to the start of the First World War?\n(a)King Arthur\n(b)Archduke Franz Ferdinand\n(c)King Artharus VII\n\n",
]

questions = [
    Question(question_asked[0], "b"),
    Question(question_asked[1], "c"),
    Question(question_asked[2], "c"),
    Question(question_asked[3], "b"),
    Question(question_asked[4], "b")
]


def take_quiz(questions):
    score = 0
    for q in questions:
        answer = input(q.prompt)
        if answer == q.answer:
            score += 1
            print(f'You have answered {str(score)} out of {str(len(questions))} correctly./nThankyou visit again.')


take_quiz(questions)
