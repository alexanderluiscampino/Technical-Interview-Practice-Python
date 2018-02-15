"""
Question 2
Given a string a, find the longest palindromic substring contained in a.
Your function definition should look like question2(a), and return a string.
"""

def isPalindrome(string):
    """
    # @param string s input string
    # @return bool if string is palindrome or not
    """
    if not string:
        return False
    # reverse compare
    return string == string[::-1]


def question2(string):
    """
    # @param string s input string
    # @return string the longest palindromic substring
    """
    if not string: # if null entry
        return ""

    n = len(string)
    longest, left, right = 0, 0, 0
    for i in range(0, n):
        for j in range(i + 1, n + 1):
            substr = string[i:j]
            if isPalindrome(substr) and len(substr) > longest:
                longest = len(substr)
                left, right = i, j
    # construct longest substr
    result = string[left:right]
    return result

# Main program
def main():
    unit_tests = ["abuttuba",
                 "acaramanamaraca",
                 "adogaplanacanalpagoda",
                 "anutforajaroftuna",
                 "asantaatnasa",
                 "amoreroma",
                 "ABCBACADCBBCDA",
                 "iriwmairanariairie",
                 "anaannaanne",
                 "",
                 "1234432"]

    for test in unit_tests:
        print("{} -> {}".format(test,question2(test)))



if __name__ == '__main__':
    main()
