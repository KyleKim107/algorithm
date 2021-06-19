{% tabs %}
{% tab title='LC_5.md' %}

> Question

* Given a string s, return the longest palindromic substring in s

{% endtab %}
{% tab title='LC_5.java' %}

```java
// Time: O(N^2), Space : O(N)
public String longestPalindrome(String s) {
  int max = 0, idx = 0;
  for (int i = 0; i < s.length(); i++) {
    int len1 = extend(s, i, i), len2 = extend(s, i, i + 1);
    if (max < Math.max(len1, len2)) {
      idx = (len1 > len2) ? (i - len1 / 2) : (i - len2 / 2 + 1);
      max = Math.max(len1, len2);
    }
  }
  return s.substring(idx, idx + max);
}

private int extend(String s, int i, int j) {
  for (; i >= 0 && j < s.length(); i--, j++)
    if (s.charAt(i) != s.charAt(j)) break;
  return j - i - 2 + 1; // 2 means current two unmatched char
}
```

{% endtab %}
{% tab title='LC_5.py' %}

```py
# Time: O(N), Space : O(N)
def longestPalindrome(self, s): # Manacher algorithm
  T = '#'.join(f'^{s}$') # (example, S = "abba", T = "^#a#b#b#a#$")
  P = [0] * len(T)
  C = R = 0
  for i in range (1, len(T)-1):
    P[i] = (R > i) and min(R - i, P[2 * C - i]) # equals to i' = C - (i-C)
    while T[i + 1 + P[i]] == T[i - 1 - P[i]]: # Attempt to expand palindrome centered at i
      P[i] += 1

    # If palindrome centered at i expand past R, adjust center based on expanded palindrome.
    if i + P[i] > R:
      C, R = i, i + P[i]

  max_len, center_i = max(in, i) for i, n in enumerate(P)) # Find the maximum element in P
  return s[(center_i  - max_len) // 2: (center_i  + maxien)//2]

```

{% endtab %}
{% endtabs %}
