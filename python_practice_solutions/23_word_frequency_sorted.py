
from collections import Counter
def word_freq(text):
    return dict(sorted(Counter(text.split()).items(), key=lambda x:x[1], reverse=True))
