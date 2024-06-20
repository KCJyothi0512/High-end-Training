'''
i/p: abdbsdabca
o/p: bdb  print the longest palindromic substring      [subsequence-jumping(use dp)]
     if not available print -1
'''
'''def longest_palindrome(s):
  n = len(s)
  if n < 2:
    return s

  # dp[i][j] = True if the substring s[i:j+1] is a palindrome
  dp = [[False] * n for _ in range(n)]
  for i in range(n):
    dp[i][i] = True

  # Length of the longest palindrome
  max_len = 1
  start = 0
  for l in range(2, n + 1):
    for i in range(n - l + 1):
      j = i + l - 1
      if s[i] == s[j]:
        if l == 2:
          dp[i][j] = True
        else:
          dp[i][j] = dp[i + 1][j - 1]
        if dp[i][j] and l > max_len:
          max_len = l
          start = i
  return s[start:start + max_len]

# Example usage
s =input()
print(longest_palindrome(s))  # Output: "bab" '''
'''
ip:abdbsdabca
op:bdb

print the longest palindromic substring(we will not skip the letters--all together)
op:if not available -1
  if available print it
  
subsequence--->jumping  the letters
'''

str=input()
res=[]
def ispal_rev(left,right):
    n=len(str)
    while left>=0 and right<n and str[left]==str[right]:
        left-=1
        right+=1
    return str[left+1:right]
    


for i in range(len(str)):
    
    pal1=ispal_rev(i,i)
    
    if len(pal1)>1:
        res.append(pal1)
        print(res)
    pal2=ispal_rev(i,i+1)
    if len(pal2)>1:
        res.append(pal2)
        print(res)
    print(res)
    

print(res)
print(max(res))
        


# abbbcbbba
# abbbabcbabbba