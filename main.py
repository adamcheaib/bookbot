def main():
    file_contents = get_file_contents()
    texts_separated = file_contents.split()

    recurring_characters = get_chars(file_contents)

    characters_list = []

    for letter in recurring_characters:
        if letter.isalpha():
            characters_list.append({"letter": letter, "amount": recurring_characters[letter]})
    characters_list.sort(reverse=True, key=key_condition)

    for obj in characters_list:
        print(f"The character {obj['letter']} was found {obj['amount']} times")


def get_file_contents():
    with open("./books/frankenstein.txt") as text:
        return text.read()


def print_word_count(str_arr):
    print(len(str_arr))


def get_chars(text):
    chars_amount = {}
    for letter in text:
        if letter.lower() in chars_amount:
            chars_amount[letter.lower()] += 1
        else:
            chars_amount[letter.lower()] = 1
    return chars_amount


def key_condition(dict):
    return dict["amount"]


main()
