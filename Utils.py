import string

ALPHABET = [s for s in string.ascii_lowercase]
CAPITAL_LETTERS = [s for s in string.ascii_uppercase]


class UtilMixin:
    def load_file(self, filename):
        with open(filename, mode="r") as file:
            lines = [line for line in file]
        return lines

    def shuffle_letter(self, letter, shuffle):
        if shuffle > 26:
            raise ValueError(f"Unable to shuffle amount by '{shuffle}' as it is greater than 26")

        is_capital = letter in CAPITAL_LETTERS
        current_position = ALPHABET.index(letter.lower())
        sandwich_alphabet = ALPHABET + ALPHABET + ALPHABET
        new_letter = sandwich_alphabet[len(ALPHABET) + current_position + shuffle]
        return new_letter.capitalize() if is_capital else new_letter

    def shuffle_str_by_n(self, lines, shift):
        shuffle = shift if shift <= len(ALPHABET) else shift % len(ALPHABET)
        print(f"Shuffling by {shuffle}")
        return " ".join(
            [
                "".join(
                    [self.shuffle_letter(s, shuffle) if s.lower() in ALPHABET else s for s in word]
                )
                for word in lines
            ]
        )

    def save_file(self, filename, str):
        with open(filename, mode="w") as file:
            file.write(str)
