import string
class Alphabet:
    def __init__(self, lang, letters):
        self.lang = lang
        self.letters = letters

    def print_letters(self):
        print(f'Буквы алфавита: {self.letters}')

    def letters_num(self):
        return len(self.letters)


class EngAlphabet(Alphabet):
    def __init__(self):
        super().__init__(lang="Eng", letters=string.ascii_uppercase)
        self.__letters_num = len(string.ascii_uppercase)

    def is_en_letter(self, letter):
        if letter.upper() in self.letters:
            return f"Буква '{letter}' относится к английскому алфавиту."
        else:
            return f"Буква '{letter}' НЕотносится к английскому алфавиту."

    def letters_num(self):
        super().letters_num()
        return self.__letters_num

    @staticmethod
    def example():
        return "Just text."


obj_alpha = EngAlphabet()
print(obj_alpha.letters_num())
print(obj_alpha.is_en_letter('f'))
print(obj_alpha.is_en_letter('М'))
print(obj_alpha.example())



