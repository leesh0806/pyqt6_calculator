import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import uic
from decimal import Decimal, ROUND_HALF_UP

# UI 파일 로드
from_class = uic.loadUiType("../data/calculator.ui")[0]

# 숫자/소수/음수 판별 함수
def is_number(token):
    try:
        float(token)
        return True
    except ValueError:
        return False


# 중위 → 후위 변환
def infix_to_postfix(tokens):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    output = []
    stack = []
    print(f"{'Token':^10} | {'Stack':^20} | {'Output':^20}")
    print("-" * 60)
    for token in tokens:
        if is_number(token):
            output.append(token)
        elif token in precedence:
            while stack and precedence.get(stack[-1], 0) >= precedence[token]:
                output.append(stack.pop())
            stack.append(token)
        print(f"{token:^10} | {str(stack):^20} | {str(output):^20}")
    while stack:
        output.append(stack.pop())
        print(f"{'POP':^10} | {str(stack):^20} | {str(output):^20}")

    return output


# 후위표기 계산
def evaluate_postfix(postfix_tokens):
    stack = []

    for token in postfix_tokens:
        if is_number(token):
            stack.append(Decimal(token))
        else:
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(a / b)

    result = stack[0]
    # 소수점 아래 10자리까지만 표시하고 반올림
    result = result.quantize(Decimal('0.0000000000'), rounding=ROUND_HALF_UP)
    
    # 정수인 경우 정수로 변환
    if result == result.to_integral_value():
        result = int(result)
    else:
        # 불필요한 0 제거
        result = result.normalize()
        
    return result


class Calculator(QMainWindow, from_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Calculator")

        self.current_number = ""
        self.result_number = ""
        self.is_new_number = True
        
        # 숫자 버튼
        for i in range(10):
            getattr(self, f"Button_{i}").clicked.connect(lambda _, x=str(i): self.number_clicked(x))
        
        # 소수점 버튼
        self.Button_point.clicked.connect(lambda: self.number_clicked("."))

        # 연산자 버튼
        self.Button_plus.clicked.connect(lambda: self.number_clicked("+"))
        self.Button_minus.clicked.connect(lambda: self.number_clicked("-"))
        self.Button_square.clicked.connect(lambda: self.number_clicked("*"))
        self.Button_divide.clicked.connect(lambda: self.number_clicked("/"))

        # = 버튼
        self.Button_equal.clicked.connect(self.calculate_result)

        # 클리어 버튼
        self.Button_AC.clicked.connect(self.all_clear)
        self.Button_C.clicked.connect(self.clear_current)



    def number_clicked(self, value):
        if self.is_new_number:
            if value == "0":
                self.current_number = "0"
            else:
                self.current_number = value
            self.is_new_number = False
        else:
            if self.current_number == "0" and value.isdigit():
                self.current_number = value
            else:
            #     # 연산자가 연속으로 들어가지 않도록 막기
            #     if value in "+-*/." and self.current_number[-1] in "+-*/.":
            #         pass  # 연산자 중복이면 아무것도 안 함
            #     else:
                self.current_number += value

        self.textEdit_eq.setText(self.current_number)

    def all_clear(self):
        self.current_number = ""
        self.is_new_number = True
        self.textEdit_eq.clear()
        #self.textEdit_result.clear()
        self.textEdit_result.setText('0')


    def clear_current(self):
        if self.current_number:
            self.current_number = self.current_number[:-1]
            self.textEdit_eq.setText(self.current_number)
        else:
            self.textEdit_eq.clear()


    def parse_input(self):
        user_input = self.current_number
        operator = ["+", "-", "*", "/", "="]
        string_list = []
        lop = 0

        if user_input and user_input[-1] not in operator:
            user_input += "="

        for i, s in enumerate(user_input):
            if s in operator:
                if user_input[lop:i].strip() != "":
                    string_list.append(user_input[lop:i])
                    string_list.append(s)
                    lop = i + 1

        return string_list[:-1]  # 마지막 '=' 제거


    def calculate_result(self):
        tokens = self.parse_input()
        try:
            postfix = infix_to_postfix(tokens)
            result = evaluate_postfix(postfix)
            self.result_number = str(result)
            self.textEdit_result.setText(self.result_number)
            # self.is_new_number = True

        except Exception:
            self.textEdit_result.setText("Error")
            self.current_number = ""
            self.is_new_number = True


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Calculator()
    window.show()
    sys.exit(app.exec())