import re
import pandas as pd


def only_eng_num(word):
    word = re.sub('[^0-9a-zA-Z]', ' ', word).strip()
    return word


def pp(word):
    spaces = [' ' * x for x in range(2, 10)]
    for space in spaces:
        if space in word:
            word = word.replace(space, '')
    return word


def extract_tag(text):
    res = []
    data = text.split(' ')
    for word in data:
        if word.startswith('#'):
            res.append(word)

    return res


def extract_like(text):
    if '좋아요' in text:
        start_location = text.find('좋아요')
        end_location = text.find('개')
        return text[start_location + 3: end_location]
    else:
        return 0


# pre-processing
file = open("file name: ")
data = pd.read_csv(file, 'r', encoding='uft-8-sig')
df = pd.DataFrame(data)

pp_text_col = list(map(only_eng_num, df['text']))
pp_text_col = list(map(pp, pp_text_col))
df['pp_text'] = pp_text_col

tag_col = df['text']
tag_col = list(map(extract_tag, tag_col))
df['tag'] = tag_col

like_col = df['like']
like_col = list(map(extract_like, like_col))
df['like_point'] = like_col

print(df)


df.to_csv(file + '_pp.csv', header=True)


