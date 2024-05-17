from BaseCipher import BaseCipher
from Utils import UtilMixin
from random import randrange


class ChallengeThree(BaseCipher, UtilMixin):
    def find_key_word(self, data, key_word):
        is_found = False
        for shift in range(1, 27):
            result = self.shuffle_str_by_n(data, shift)
            if key_word in result:
                print(f"found with random shift {shift}")
                break
        if not is_found:
            raise Exception(f"Cannot find possible solution for key word: {key_word}")
        return result

    def encoding_data(self, data, shift):
        return self.shuffle_str_by_n(data, shift)

    def decoding_data(self, data, key_word):
        return self.find_key_word(data, key_word)

    def encode_file(self, input_file, output_file):
        data = self.load_file(input_file)
        rand_shift = randrange(100)
        print(f"Encoding with shift: {rand_shift}")
        encoded_data = self.shuffle_str_by_n(data, rand_shift)
        self.save_file(output_file, encoded_data)
