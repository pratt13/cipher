from BaseCipher import BaseCipher
from Utils import ALPHABET, UtilMixin


class ChallengeTwo(BaseCipher, UtilMixin):
    def encoding_data(self, data):
        return self.shuffle_str(data)

    def decoding_data(self, data):
        return self.shuffle_str(data, encode=False)

    def shuffle_str(self, lines, encode=True):
        factor = 1 if encode else -1
        result = []
        for shift, word in enumerate(lines, start=1):
            result += [
                "".join(
                    [
                        self.shuffle_letter(w.lower(), factor * shift)
                        if w.lower() in ALPHABET
                        else w
                        for w in word
                    ]
                )
            ]
        return " ".join(result)
