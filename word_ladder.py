#!/bin/python3

from collections import deque


def word_ladder(start_word, end_word, dictionary_file='words5.dict'):
    '''
    Returns a list satisfying the following properties:

    1. the first element is `start_word`
    2. the last element is `end_word`
    3. elements at index i and i+1 are `_adjacent`
    4. all elements are entries in the `dictionary_file` file

    For example, running the command
    ```
    word_ladder('stone','money')
    ```
    may give the output
    ```
    ['stone', 'shone', 'phone', 'phony', 'peony', 'penny', 'benny',
    'bonny', 'boney', 'money']
    ```
    but the possible outputs are not unique,
    so you may also get the output
    ```
    ['stone', 'shone', 'shote', 'shots', 'soots', 'hoots', 'hooty',
    'hooey', 'honey', 'money']
    ```
    (We cannot use doctests here because the outputs are not unique.)

    Whenever it is impossible to generate a word ladder between the two words,
    the function returns `None`.
    '''
    stack = []
    stack.append(start_word)
    queue = deque()
    queue.append(stack)
    with open('words5.dict') as dictionary_file:
        dictionarytext = dictionary_file.readlines()
        dictionary = list(set([word.strip() for word in dictionarytext]))
    if start_word == end_word:
        return stack
    if _adjacent(start_word, end_word) is True:
        stack.append(end_word)
        return stack
    while len(queue) > 0:
        next_stack = queue.popleft()
        for word in dictionary:
            if _adjacent(word, next_stack[-1]) is True and word not in next_stack:
                if word == end_word:
                    next_stack.append(word)
                    print(next_stack)
                    return next_stack
                    
                stack_copy = next_stack[:]
                stack_copy.append(word)
                queue.append(stack_copy)
                dictionary.remove(word)
    return None


def verify_word_ladder(ladder):
    '''
    Returns True if each entry of the input list is adjacent to its neighbors;
    otherwise returns False.

    >>> verify_word_ladder(['stone', 'shone', 'phone', 'phony'])
    True
    >>> verify_word_ladder(['stone', 'shone', 'phony'])
    False
    '''
    if ladder is None:
        return True
    elif ladder == []:
        return False
    for i in range(len(ladder) - 1):
        if _adjacent(ladder[i], ladder[i + 1]) is False:
            return False
    return True


def _adjacent(word1, word2):
    '''
    Returns True if the input words differ by only a single character;
    returns False otherwise.

    >>> _adjacent('phone','phony')
    True
    >>> _adjacent('stone','money')
    False
    '''
    diff = 0
    if len(word1) != len(word2):
        return False
    for i in range(0, len(word1)):
        if word1[i] != word2[i]:
            diff += 1
    if diff<=1:
        return True
    else:
        return False

word_ladder('stone','money')
