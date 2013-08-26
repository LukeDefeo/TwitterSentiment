import re
from NLP.Common.tokeniser import contains_url

__author__ = 'Luke'

emotive_trigger_words = ['shit', 'fucking', 'fuck', 'crap', 'terrible', 'amazing', 'omg', 'zomg', 'omfg', 'wtf', 'wth',
                         'lol', 'rolf']

"Code for this function " \
" from http://stackoverflow.com/questions/323750/how-to-access-previous-next-element-while-for-looping"


def neighborhood(iterable):
    iterator = iter(iterable)
    prev = None
    item = iterator.next()
    for next in iterator:
        yield (prev, item, next)
        prev = item
        item = next
    yield (prev, item, None)


def contains_caps(tweet, threshold=0.35):
    tokens = [token for token in tweet.split() if not contains_url(token)]
    tweet = ' '.join(tokens)
    upper_ascii = 0.0
    lower_ascii = 0.0
    for char in tweet:
        if 65 <= ord(char) <= 90:
            upper_ascii += 1
        if 97 <= ord(char) <= 122:
            lower_ascii += 1

    result = 0
    try:
         result = float(upper_ascii / lower_ascii) > threshold
    except Exception as e:
        pass

    return result


def contains_rolling_letters(word, pos=0):
    if len(word) == pos:
        return False

    if len(word) - pos >= 3:
        if word[pos] == word[pos + 1] == word[pos + 2]:
            return True
        else:
            return contains_rolling_letters(word, pos + 1)
    else:
        return False


'''must pass in lower case words with punctionuation removed'''
def contains_trigger_words(tweet_tokens):
    for word in tweet_tokens:
        if word in emotive_trigger_words:
            return True

    return False


'''loosely based on http://stackoverflow.com/questions/5862490/how-to-match-emoticons-with-regular-expressions'''
def contains_emoticons(tweet):
    pattern = ur'((?::|;|=)(?:-)?(?:\)|D|P|p|\/|\(|\[|\]|\{|S|s))'
    return re.search(pattern, tweet)


def contains_positive_emoticon(tweet):
    pattern = ur'(?::|;|=)(?:-)?(?:\)|D|P|p|\]|\))'
    return re.search(pattern, tweet)


def contains_negative_emoticon(tweet):
    pattern = ur'((?::|;|=)(?:-)?(?:\/|\(|\[|\{|S|s))'
    return re.search(pattern, tweet)

