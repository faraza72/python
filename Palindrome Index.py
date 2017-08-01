def isPalindrome(s):
    for i in range(len(s) / 2):
        if s[i] != s[len(s) - i - 1]:
            return False
    return True


def palindromeIndex(s):
    for i in range(len(s) / 2):

        if s[i] != s[len(s) - i - 1]:
            print s[i+1:]
            if isPalindrome(s[:i] + s[i + 1:]):
                return i
            else:
                return len(s) - i - 1
    return -1



t = int(raw_input())
for _ in xrange(t):
    s = raw_input()
    print palindromeIndex(s)
