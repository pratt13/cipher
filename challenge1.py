from BaseCipher import BaseCipher
from Utils import UtilMixin


class ChallengeOne(BaseCipher, UtilMixin):
    def encoding_data(self, data, shift):
        return self.shuffle_str_by_n(data, shift)

    def decoding_data(self, data, shift):
        return self.shuffle_str_by_n(data, -shift)
