{% tabs %}
{% tab title='HR_detect-the-domain.name.md' %}

> Question

* One line, containing the list of detected domains, separated by semi-colons, in lexicographical order
* Do not leave any leading or trailing spaces either at the ends of the line, or before and after the individual domain names

```txt
10
<div class="reflist" style="list-style-type: decimal;">
<ol class="references">
<li id="cite_note-1"><span class="mw-cite-backlink"><b>^
["Train (noun)"](http://www.askoxford.com/concise_oed/train?view=uk).
<i>(definition – Compact OED)</i>. Oxford University Press<span class="reference-accessdate">.
Retrieved 2008-03-18</span>.</span>
<span title="ctx_ver=Z39.88-2004&rfr_id=info%3Asid%2Fen.wikipedia.org%3ATrain&rft.atitle=Train+%28noun%29&rft.genre=article
&rft_id=http%3A%2F%2Fwww.askoxford.com%2Fconcise_oed%2Ftrain%3Fview%3Duk&rft.jtitle=%28definition+%E2%80%93+Compact+OED%29
&rft.pub=Oxford+University+Press&rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Ajournal" class="Z3988">
<span style="display:none;"> </span></span></span></li>
...
</div>

Output: askoxford.com;bnsf.com;hydrogencarsnow.com;mrvc.indianrail.gov.in;web.archive.org
```

{% endtab %}
{% tab title='HR_detect-the-domain.name.py' %}

```py
import re, sys

page = sys.stdin.read()
re_patt = r"https?:\/\/(?:ww[w\d]\.)?([\w\.-]+\.[a-zA-Z]*)"
print(";".join(sorted(set(re.findall(re_patt, page, re.DOTALL)))))
```

{% endtab %}
{% endtabs %}
