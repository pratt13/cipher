from abc import ABC


class BaseCipher(ABC):
    def encoding_data(self, *args, **kwargs):
        raise NotImplementedError

    def decoding_data(self, *args, **kwargs):
        raise NotImplementedError

    def encode_file(self, input_file, output_file, *args, **kwargs):
        """
        Take an input file and encode it by the encoding_data method
        """
        data = self.load_file(input_file)
        encoded_data = self.encoding_data(data, *args, **kwargs)
        self.save_file(output_file, encoded_data)

    def decode_file(self, input_file, output_file, *args, **kwargs):
        """
        Take an input file and decode it by the decoding_data method
        """
        data = self.load_file(input_file)
        decoded_data = self.decoding_data(data, *args, **kwargs)
        self.save_file(output_file, decoded_data)
