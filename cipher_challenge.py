"""
Entrypoint for the cipher challenge
"""

import argparse

from challenge1 import ChallengeOne
from challenge2 import ChallengeTwo
from challenge3 import ChallengeThree

CHOICES = ("constant", "increasing", "random")
if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="A program to use a Julius Caesar Cipher." + "There are multiple challenges"
    )
    parser.add_argument(
        "--type",
        "-t",
        default="poisson",
        help="Cipher type. Options are constant, increasing or random shift as per the README.md",
        type=str,
        choices=CHOICES,
    )
    parser.add_argument(
        "--value",
        "-v",
        type=int,
        help="The amount of shift required for the constant shift ype, default is 1.",
    )
    parser.add_argument(
        "--key-word",
        type=str,
        help="The word being searched for the random shift.",
    )
    parser.add_argument(
        "--input_filename",
        "-i",
        type=str,
        help="The input filename to encode/decode.",
        required=True,
    )
    parser.add_argument(
        "--output_filename",
        "-o",
        type=str,
        help="The filename to output the encoded/decoded data into.",
        required=True,
    )
    args = parser.parse_args()
    if args.type == "constant":
        challengeOne = ChallengeOne()
        # Constant shift value is required
        if not args.value:
            raise ValueError(f"When choosing {args.type} is selected, value must be provided")
        challengeOne.decode_file(args.input_filename, args.output_filename, args.value)
    elif args.type == "increasing":

        challengeTwo = ChallengeTwo()
        challengeTwo.decode_file(args.input_filename, args.output_filename)
    elif args.type == "random":
        challengeThree = ChallengeThree()
        if not args.key_word:
            raise ValueError(
                f"Cannot decode a message using {args.type} with no `--key-word` argument"
            )
        challengeThree.decode_file(args.input_filename, args.output_filename, args.key_word)
    else:
        raise ValueError(f"Unexpected type: {args.type}")
