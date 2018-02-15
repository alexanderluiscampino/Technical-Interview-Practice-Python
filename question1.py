"""
Question 1
Given two strings s and t, determine whether some anagram of t is a substring
of s. For example: if s = "udacity" and t = "ad", then the function returns
True. Your function definition should look like: question1(s, t) and return a
boolean True or False.
"""

# Turn on/off to enable/disable debugging
debug = True


def is_anagram(s, t):
    """
    # Find if strings are anagram. t anagram of s
    # @param {string, string} input strings
    # @return bool if strings are anagram of each other or not
    """
    s = list(s)
    # Sort a string and then compare with each other
    s.sort()   # Quick sort O(n*log(n))
    return s == t


def question1(s,t):
    """
    # Find out sorted(possible substring of s) and compare with sorted(t)
    # @param main_string, ana_string input strings
    # @return bool Question1 answer
    """
    global debug
    sort_t = list(t)
    sort_t.sort()     # Quick sort O(n*log(n))

    for i in range(len(s) - len(t) + 1):
        if debug:
            print (s[i: i+len(t)], t)
        if is_anagram(s[i: i+len(t)], sort_t):
            return True
    return False

# Main program
def main():
    unit_tests = [("udacity", "ad"),
                 ("udacity", "da"),
                 ("udacity", "au"),
                 ("udacity", "dacity"),
                 ("banana", "anana"),
                 ("panama", "panmt"),
                 ("udacity", "ciy"),
                 ("udacity", "xyz"),
                 ("udacity", ""),
                 ("udacity", "12863742302323232746"),
                 ("ad", "udacity" )]

    for test in unit_tests:
        print("{} -> {}".format(test,question1(test[0],test[1])))


if __name__ == '__main__':
    main()


"""
Case 1: ("udacity", "ad") -> True
string with 2 characters reversed from order in S

Case 2: ("udacity", "da") -> True
string with 2 characters same as in order in S

Case 3: ("udacity", "au") -> False
string with 2 alternative characters and reversed from order in S

Case 4: ("udacity, dacity") -> True
string with 6 characters same as in order in S

Case 5: ("udacity", "ciy") -> False
string with 2 characters same as in order in S and 1 character out of order.

Case 6: ("udacity", "xyz") -> False
string with new characters not in string S.

Case 7: ("udacity", "") -> True
empty string.

Case 8: ("ad", "udacity" ) -> False
string t's length is greater than string S.
"""
