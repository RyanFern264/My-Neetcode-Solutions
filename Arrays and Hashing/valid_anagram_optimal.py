def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t): #if strings are not the same length then they can't be anagrams
        return False

    countS, countT = {}, {} #create empty dicts

    for i in range(len(s)): #both same length
        countS[s[i]] = 1 + countS.get(s[i], 0) #every time we see a character, increment its count by 1
        #we use the .get since if the letter doesn't exist in the hash map yet, we'd get a key error
        #the ", 0" part of the .get basically says that if that key doesn't exist already, return zero
        countT[t[i]] = 1 + countT.get(t[i], 0)
    for c in countS:
        if countS[c] != countT.get(c, 0): #if counts are not the same (aka not an anagram, return false)
            return False
    return True

string1 = "jar"
string2 = "jam"

print(isAnagram(string1, string2))