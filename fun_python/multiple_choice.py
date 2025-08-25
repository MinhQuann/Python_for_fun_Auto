from quiz import Quiz


question = [
    "Câu 1. Đội bóng nào về nhì WC?\nA. Brazil\nB. Italia\nC. Đức",
    "Câu 2. Đội bóng nào vô địch WC?\nA. Arg\nB. Pháp\nC. Brazil"
]


quizzes = [
    Quiz(question[0], "B"),
    Quiz(question[1], "B")
]


def run_quiz(quizzes):
    score = 0
    for quiz  in quizzes:
        print(quiz.question)
        user_input = input("Nhập câu trả lời của bạn: ")
        if user_input.lower() == quiz.ans.lower():
            score += 1
    print(f"\n --> Kết quả bạn đã trả lời đúng {score}/{len(quizzes)}")

run_quiz(quizzes)