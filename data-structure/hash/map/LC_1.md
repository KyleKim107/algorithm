{% tabs %}
{% tab title='LC_1.md' %}

> Question

* Find two index that sums up to target

```txt
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
```

{% endtab %}
{% tab title='LC_1.py' %}

```py
def twoSum(self, nums, target):
  d = {}
  for i, num in enumerate(nums):
    if target - num in d:
      return d[target - num], i
    d[num] = i
```

{% endtab %}
{% endtabs %}
