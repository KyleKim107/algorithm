# Python

> import re

* re.sub('패턴', 교체함수, '문자열')

* EX)  st = re.sub('[^a-z0-9-_.]', '', st)

* 숫자, 소문자, '-' , '_', '.'가 아닌 문자들은 ""로 삭제함

* ^ : Matches the start of the string, and in MULTILINE mode also matches immediately after each newline.

* '+' :Causes the resulting RE to match 1 or more repetitions of the preceding RE.

  * ab+ will match ‘a’ followed by any non-zero number of ‘b’s;

* \ :Regular expressions use the backslash character ('\') to indicate special forms or

  * to allow special characters to be used without invoking their special meaning.

* []: Used to indicate a set of characters. In a set:

  * Ranges of characters can be indicated by giving two characters and separating

    * them by a '-', for example [a-z] will match any lowercase ASCII letter,

  * [0-5][0-9] will match all the two-digits numbers from 00 to 59, and [0-9A-Fa-f] will match any hexadecimal digit.

  * If - is escaped (e.g. [a\-z]) or if it’s placed as the first or last character

    * (e.g. [-a] or [a-]), it will match a literal '-'.

* ? : Causes the resulting RE to match 0 or 1 repetitions of the preceding RE. ab? will match either ‘a’ or ‘ab’.

'''py

import re

def solution(new_id):
    st = new_id
    st = st.lower()
    print(st)
    st = re.sub('[^a-z0-9-_.]', '', st)
    st = re.sub('\.+', '.', st)
    print(st)
    st = re.sub('^[.]|[.]$', '', st)
    print(st)
    st = 'a' if len(st) == 0 else st[:15]
    st = re.sub('^[.]|[.]$', '', st)
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
    return st

'''
