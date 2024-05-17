from abc import ABC


class BaseCipher(ABC):
    def _load_file(self, filename):
        with open(filename, mode="r") as file:
            lines = [line for line in file]
        return lines

    def _save_file(self, filename, str):
        with open(filename, mode="w") as file:
            file.write(str)

    def decoding_data(self, *args, **kwargs):
        raise NotImplementedError

    def decode_file(self, input_file, output_file, *args, **kwargs):
        """
        Take an input file and decode it by the decoding_data method
        """
        data = self._load_file(input_file)
        decoded_data = self.decoding_data(data, *args, **kwargs)
        self._save_file(output_file, decoded_data)
