# Cipher

## Challenge 1

Given a large string, decipher the message knowing that it has been shifted by 4 each time.

```sh
python3 cipher_challenge.py --type constant --value 4 -i example.txt -o encoded_constant.txt -e
python3 cipher_challenge.py --type constant --value 4 -i encoded_constant.txt -o decoded_constant.txt
```

## Challenge 2
Decipher the message, given that each letter has been shifted by the words position in the list. The first position is position 1.

Example,
```sh
A bat -> B dcv
```

```sh
python3 cipher_challenge.py --type increasing -i example.txt -o encoded_shift.txt -e
python3 cipher_challenge.py --type increasing  -i encoded_shift.txt -o decoded_shift.txt
```
## Challenge 3

The message has been shifted by a constant amount, but you don't know what. All you know is the word, kermit appears at most once.


```sh
python3 cipher_challenge.py --type random -i example.txt -o encoded_random.txt -e
python3 cipher_challenge.py --type random  -i encoded_random.txt -o decoded_random.txt --key-word kermit
```

## Challenge 4
Write a program to encode a message by a julius cipher.


## Concepts


### Functions/Classes
Reusable code

### CLI
Use argparse to make it a command line tool

### Context Managers
Use context managers for writing and reading files

### Testing
Unit testing
