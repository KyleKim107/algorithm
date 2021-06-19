{% tabs %}
{% tab title='HR_html-attributes.md' %}

> Question

* tag-n:attribute-1,attribute-2,attribute-3...
* Where tag-1 is lexicographically smaller than tag-2 and attribute-1 is lexicographically smaller than attribute-2

```txt
Input:
2
<p><a href="http://www.quackit.com/html/tutorial/html_links.cfm">Example Link</a></p>
<div class="more-info"><a href="http://www.quackit.com/html/examples/html_links_examples.cfm">More Link Examples...</a></div>

Output:
a:href
div:class
p:
```

{% endtab %}
{% tab title='HR_html-attributes.py' %}

```py
import re
from collections import defaultdict

tags = defaultdict(set)

for _ in range(int(input())):
  for tag, attrs in re.findall(r'<(\w+)(.*?)?>', input()):
    tags[tag].update(re.findall(r'\s(\w+)=', attrs))

for tag, attrs in sorted(tags.items()):
  print(f"{tag}:{','.join(sorted(attrs))}")
```

{% endtab %}
{% endtabs %}
