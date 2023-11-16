import random
import string

def generate_word() -> str:
    alphabet = list(string.ascii_lowercase + ' ')
    # return "".join(random.sample(alphabet, 27))
    final = ''
    for i in range(27):
        final += alphabet[random.randint(0,26)]
    return final


def check_eq(word: str, ideal: str = 'methinks it is like a weasel') -> int:
    diff = 0
    for i in range(len(word)):
        if word[i] != ideal[i]:
            diff += 1
    return diff


def start() -> None:
    start_diff = 27
    while start_diff != 0:
        word = generate_word()
        difference = check_eq(word)
        if start_diff > difference:
            print(word, difference)
        start_diff = min(start_diff, difference)
        # print(start_diff)

if __name__ == '__main__':
    start()