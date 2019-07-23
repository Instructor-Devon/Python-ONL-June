def allSubstrings(string, substr="", count=0, strings=[]):

    # string "ant" => [a, an, ant, nt, n, t]
    # string "banana" => [anana, nana, ana, na, a, banan, bana, ban, ba, b, anan, na]

    # let's see the string this time
    print(string)

    if count == len(string):
        return strings

    # base case: empty string
    # we need to move closer to base case
    if len(substr) == 0:
        # use count to progress the string from 'banana' to 'anana' (for ex.)
        substr = string[count:]
        count += 1
    
    strings.append(substr)
    # slice one off the end of substr (banana banan bana etc)
    return allSubstrings(string, substr[:len(substr)-1], count, strings)


    # # string[x:x] => n
    # allSubstrings(string[x:x], strings)
    # # string[:x] => an, a, 
    # allSubstrings(string[x:], strings)

substrs = allSubstrings("banana")
print(substrs)