from typing import List
import re


def replaceWord():
    temporaryText: List[str] = []
    file = input("Give me file: ")

    temp = "###ABABA###"
    with open(file, 'r', encoding='utf8') as fin:
        for line in fin:
            line = re.sub(r'\bi\b', temp, line)
            line = re.sub(r'\boraz\b', 'i', line)
            line = re.sub(temp, 'oraz', line)
            line = re.sub(r'\bnigdy\b', 'prawie nigdy', line)
            line = re.sub(r'\bdlaczego\b', 'czemu', line)
            temporaryText.append(line)

    with open(file, 'w+') as fout:
        for line in temporaryText:
            fout.write(line)


if __name__ == "__main__":
    replaceWord()
