# python3
B = 13
Q = 256

def read_input():
    text = input("I vai F: ")
    if "I" in text[:1]:
        P = input("Pattern: ").rstrip()
        T = input("Text: ").rstrip()
    elif "F" in text[:1]:
        filename = "test/" + input("Fails: ")
        file = open(filename, "r")
        P = file.readline()
        T = file.readline()
    return (P, T)

def get_hash(pattern: str) -> int:
    global B, Q
    m = len (pattern)
    result = 0
    for i in range (m):
        result = (B* result + ord (pattern[i])) % Q
    return result

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    answer = []
    pattern_len = int(len (pattern))
    text_len = int(len(text))

    pattern_hesh = get_hash(pattern)

    for i in range(text_len - pattern_len + 1):
        text_hesh = get_hash(text[i:i + pattern_len])

        if pattern_hesh == text_hesh:
            answer.append(i)

    return answer


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

