import re # regular expressions
import urllib.request  # the lib that handles the url stuff
import json as j # for dictionary dumping

def parse_lexicon():
    #big python dictionary representing the lexicon
    lexicon_dict = {}
    # opens the Specialist Lexicon
    data = urllib.request.urlopen("https://lsg3.nlm.nih.gov/LexSysGroup/Projects/lexicon/2019/release/LEX/LEXICON")
    # data is a file-like object and works just like a file
    # i = 1
    curr_base_key = ""
    for line in data:
        # i+=1
        # print("my line is " + str(line) + "\n")
        baseObj = re.search(r'(\w*)=(.*)\\n', str(line))
        if baseObj:
            # print(str(line))
            curr_group_one = str(baseObj.group(1))
            if (curr_group_one == "base"):
                print(curr_group_one)
                # print(str(baseObj.group(2)))
                if str(baseObj.group(2)) not in lexicon_dict:
                    #name of the main dictionary key
                    curr_base_key = str(baseObj.group(2))
                    # print("my base key " + curr_base_key)
                else: #do something here (should only have one unique base key though)
                    print("multiple current base keys")
            elif str(baseObj.group(1) != "base"):
                # print("my curr key is " + curr_base_key)
                new_add_key = str(baseObj.group(1))  # new key
                new_add_value = str(baseObj.group(2))  # new value
                # print("my new key is " + new_add_key)
                # print("my new value is " + new_add_value)
                if curr_base_key not in lexicon_dict:
                    lexicon_dict[curr_base_key] = {}
                if new_add_key not in lexicon_dict[curr_base_key]:
                    lexicon_dict[curr_base_key][new_add_key] = [new_add_value]
                else:
                    lexicon_dict[curr_base_key][new_add_key].append(new_add_value)
        else:
            # do nothing, since this is a '}'
            print("no object found on this line")
    print(len(lexicon_dict))
    with open('my_lexicon.json', 'w') as file:
        j.dump(lexicon_dict, file)

if __name__ == '__main__':
    parse_lexicon()


