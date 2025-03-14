
def isAnagram(s: str, t: str) -> bool:
    char_list_1 = sorted(s)
    char_list_2 = sorted(t)

    if char_list_1 == char_list_2:
        return True
    return False

def isAnagram_shorter(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)


string1 = "jam"
string2 = "jam"

print(isAnagram(string1, string2))