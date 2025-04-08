def group_anagrams(strs):
    str_dict = {}
    for string in strs:
        sorted_str = "".join(sorted(string))
        if sorted_str in str_dict:
            str_dict[sorted_str].append(string)
        else:
            str_dict[sorted_str] = [string]
        print(list(str_dict.values()))

strings = ["act","pots","tops","cat","stop","hat"]
group_anagrams(strings)