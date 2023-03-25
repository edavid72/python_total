text = input('Enter a text to analyze please: '.lower())
print('I need 3 letters to start the analysis\n')
letter1 = input('First letter: '.lower())
letter2 = input('Second letter: '.lower())
letter3 = input('Third letter: '.lower())


def text_parser(text, letter1, letter2, letter3):
    # Count repetitions of a letter entered by the user
    text_list = list(text)
    repeat_l1 = text_list.count(letter1)
    repeat_l2 = text_list.count(letter2)
    repeat_l3 = text_list.count(letter3)
    print(f'The letter {letter1} is repeated {repeat_l1} times.')
    print(f'The letter {letter2} is repeated {repeat_l2} times.')
    print(f'The letter {letter3} is repeated {repeat_l3} times.\n')

    # Count the number of word in the text
    count_words = text.split()
    print(f'This text contain {len(count_words)} words\n')

    # First and last letter in the text
    print(f'The first letter in this text is {text_list[0]}')
    print(f'The last letter in this text is {text_list[-1]}\n')

    # Word in reverse
    words_reverse = count_words.reverse()
    print(count_words)

    # The text contain thw word "python"?
    if 'python' in count_words:
        print("The word 'python' is in this text.")
    else:
        print("The word 'python' is not in this text.")


print(text_parser(text, letter1, letter2, letter3))
