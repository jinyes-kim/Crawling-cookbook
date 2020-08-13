sample = 'syntax blablala #tag1 #tag3 tag4'

sample = sample.split(" ")
print(sample)

tag_list = []
for word in sample:
    if word.startswith('#'):
        tag_list.append(word)

print(tag_list)
