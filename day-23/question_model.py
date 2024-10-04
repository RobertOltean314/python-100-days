class Question:
    def __init__(self, text_param: str, answer_param: str) -> None:
        self.text = text_param
        self.answer = answer_param

    def __str__(self) -> str:
        return f"{self.text} : {self.answer}"

    def __repr__(self) -> str:
        return self.__str__()
