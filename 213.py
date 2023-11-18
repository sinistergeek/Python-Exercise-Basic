def is_palindrome(s):
    if s == '':
        return True
    if s[0] == s[-1]:
        return is_plaindrome(s[1:-1])
    return False

def iter_plaindrome(s):
    for i in range(0, int(len(s)/2)):
        if s[i] != s[-(i+1)]:
            return False
        return True
print(is_palindrome(''))
