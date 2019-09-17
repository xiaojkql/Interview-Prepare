with open('./citation.txt') as in_f:
    text = []
    for line in in_f.readlines():
        text.append(line[2:].strip())
    text = sorted(text)
    with open('./new_ci.txt','a') as out_f:
        for line in text:
            out_f.write(line+'\n')
