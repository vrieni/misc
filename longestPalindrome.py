

#finds palindrome substring in n^3
def find_palindrome(input_str):

    palindrome = ''
    for start_idx in xrange(len(input_str)):
        end_idx = start_idx+1
        for end_idx in xrange(len(input_str)+1):
            tmp_string = input_str[start_idx:end_idx]
            if tmp_string == tmp_string[::-1] and len(tmp_string) > len(palindrome):
                palindrome = tmp_string

    return palindrome


#finds palindrome substring in n^2
def fp_dp_n2(input_str):
    def longest_palindrome(s):
        n = len(s)
        start = end = 0

        for i in range(n):
            len1 = current_range(s, i, i)
            len2 = current_range(s, i, i+1)
            max_len = max(len1, len2)

            if max_len > end - start:
                start = i - ((max_len-1) / 2)
                end = i + (max_len / 2)

        return s[start:end + 1]
    def current_range(s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left-=1
            right+=1
        return right - left - 1

    return longest_palindrome(input_str)
