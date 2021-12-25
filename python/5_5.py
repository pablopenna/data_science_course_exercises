import sys

string = sys.argv[1].lower()


def getUniqueChars(s):
    unique_chars = []
    for ch in string:
        if ch not in unique_chars:
            unique_chars.append(ch)
    print(f"unique chars: {unique_chars}")
    print(f"# of unique chars: {len(unique_chars)}")
    return unique_chars

def countUniqueCharOccurrences(string):
    unique_chars_counters = {}
    # uniqChars = getUniqueChars(string)

    for uc in string:
        if unique_chars_counters.get(uc) == None:
            unique_chars_counters.update({uc: 1})
        else:
            unique_chars_counters[uc] = unique_chars_counters[uc]+1
    print(f"unique chars counters: {unique_chars_counters}")
    return unique_chars_counters


getUniqueChars(string)
countUniqueCharOccurrences(string)
