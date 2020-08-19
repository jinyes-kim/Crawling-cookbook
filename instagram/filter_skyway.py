import pandas as pd
import pprint

file_name = input('file name: ')
file = pd.read_csv(file_name, encoding='unicode_escape')

df = pd.DataFrame(file)

checker = list(df['pp_text'])

bool_list = []
stopword = ['Bugak25', 'bike' 'skyway', 'cycling', 'cyclinglife', 'namsan', 'bugakskyway', 'riding', 'roadbike', 'palgakjeong', 'bycycle',
            'wangsamaju', 'Skyway']

for data in checker:
    tmp_list = []
    for word in stopword:
        if word in data:
            tmp_list.append(1)

    if 1 in tmp_list:
        bool_list.append(1)
    else:
        bool_list.append(0)

pprint.pprint(bool_list)
print(len(bool_list))
print(bool_list.count(1))

df['check'] = bool_list


drop_index = df[df['check'] == 1].index
new_df = df.drop(drop_index)
new_df = new_df.drop('check', axis='columns')
new_df.to_csv(file_name + '_complete.csv', header=True, encoding='utf-8-sig')