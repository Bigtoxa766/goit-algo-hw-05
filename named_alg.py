import timeit

'''
Текст 1 (довгий текст з великим алфавітом):
Боєр-Мур буде найефективнішим через можливість великих стрибків при невідповідностях.
КМП працюватиме швидше за лінійний час після побудови префікс-функції.
Рабін-Карп може бути менш ефективним, якщо часто виникатимуть колізії хешів.

Текст 2 (короткий текст з малим алфавітом):
Боєр-Мур може бути менш ефективним через часті повторення символів, що зменшить його можливість здійснювати великі стрибки.
КМП буде стабільно ефективним завдяки своїй лінійній складності.
Рабін-Карп може виявитися менш надійним через часті колізії хешів, проте для дуже коротких текстів він буде прийнятним.
'''

def kmp_search(pattern, text):
    def compute_prefix_function(pattern):
        m = len(pattern)
        lps = [0] * m
        length = 0
        i = 1
        while i < m:
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps

    n = len(text)
    m = len(pattern)
    lps = compute_prefix_function(pattern)
    i = 0
    j = 0
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == m:
            return i - j
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return -1

def rabin_karp_search(pattern, text, prime=101):

    m = len(pattern)
    n = len(text)
    d = 256
    p_hash = 0
    t_hash = 0
    h = 1

    for i in range(m - 1):
        h = (h * d) % prime

    for i in range(m):
        p_hash = (d * p_hash + ord(pattern[i])) % prime
        t_hash = (d * t_hash + ord(text[i])) % prime

    for i in range(n - m + 1):
        if p_hash == t_hash:
            if text[i:i + m] == pattern:
                return i
        if i < n - m:
            t_hash = (d * (t_hash - ord(text[i]) * h) + ord(text[i + m])) % prime
            if t_hash < 0:
                t_hash += prime
    return -1


    def bad_char_heuristic(pattern):
        bad_char = [-1] * 256
        for i in range(len(pattern)):
            bad_char[ord(pattern[i])] = i
        return bad_char

    m = len(pattern)
    n = len(text)
    bad_char = bad_char_heuristic(pattern)
    s = 0

    while s <= n - m:
        j = m - 1
        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1
        if j < 0:
            return s
        else:
            s += max(1, j - bad_char[ord(text[s + j])])
    return -1

def boyer_moore_search(pattern, text):
    def bad_char_heuristic(pattern):
        bad_char = {}
        for i in range(len(pattern)):
            bad_char[pattern[i]] = i
        return bad_char

    m = len(pattern)
    n = len(text)
    bad_char = bad_char_heuristic(pattern)
    s = 0

    while s <= n - m:
        j = m - 1
        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1
        if j < 0:
            return s
        else:
            # Якщо символ відсутній у bad_char, використовуємо зсув на всю довжину підрядка
            s += max(1, j - bad_char.get(text[s + j], -1))
    return -1

text1 = "абзац тексту англійською мовою або інший великий текст"
text2 = "abababababababababababababababababababababab"

existing_substring1 = "тексту"
fake_substring1 = "підрядок"

existing_substring2 = "ababab"
fake_substring2 = "abcabc"

# Вимірювання часу для тексту 1 (існуючий підрядок)
print("КМП (існуючий підрядок):", timeit.timeit(lambda: kmp_search(existing_substring1, text1), number=1000))
print("Рабін-Карп (існуючий підрядок):", timeit.timeit(lambda: rabin_karp_search(existing_substring1, text1), number=1000))
print("Боєр-Мур (існуючий підрядок):", timeit.timeit(lambda: boyer_moore_search(existing_substring1, text1), number=1000))

# Вимірювання часу для тексту 1 (вигаданий підрядок)
print("КМП (вигаданий підрядок):", timeit.timeit(lambda: kmp_search(fake_substring1, text1), number=1000))
print("Рабін-Карп (вигаданий підрядок):", timeit.timeit(lambda: rabin_karp_search(fake_substring1, text1), number=1000))
print("Боєр-Мур (вигаданий підрядок):", timeit.timeit(lambda: boyer_moore_search(fake_substring1, text1), number=1000))

# Вимірювання часу для тексту 2 (існуючий підрядок)
print("КМП (існуючий підрядок):", timeit.timeit(lambda: kmp_search(existing_substring2, text2), number=1000))
print("Рабін-Карп (існуючий підрядок):", timeit.timeit(lambda: rabin_karp_search(existing_substring2, text2), number=1000))
print("Боєр-Мур (існуючий підрядок):", timeit.timeit(lambda: boyer_moore_search(existing_substring2, text2), number=1000))

# Вимірювання часу для тексту 2 (вигаданий підрядок)
print("КМП (вигаданий підрядок):", timeit.timeit(lambda: kmp_search(fake_substring2, text2), number=1000))
print("Рабін-Карп (вигаданий підрядок):", timeit.timeit(lambda: rabin_karp_search(fake_substring2, text2), number=1000))
print("Боєр-Мур (вигаданий підрядок):", timeit.timeit(lambda: boyer_moore_search(fake_substring2, text2), number=1000))