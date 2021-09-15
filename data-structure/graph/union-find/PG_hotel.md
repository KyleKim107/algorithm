{% tabs %}
{% tab title='LC_547.md' %}

> Question

* Given adjacency matrix, find total number of SCC

```txt
Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2
```

{% endtab %}
{% tab title='PG_hotel.java' %}

```java
import java.util.*;

class Solution {
    HashMap<Long, Long> map = new HashMap<>();

        public long[] solution(long k, long[] room_number) {
            long[] answer = new long[room_number.length];

            for(int i = 0; i < room_number.length; i++){
                System.out.println(room_number[i]);
                answer[i] = findEmptyRood(room_number[i]);
                Iterator it = map.entrySet().iterator();
                while(it.hasNext()){
                     Map.Entry tmp = (Map.Entry)it.next();
                    System.out.println( "tmp.getKey() : "+tmp.getKey() + " " + " tmp.getValue() : "+tmp.getValue() );
                }
                System.out.println();
            }
            return answer;
        }

        long findEmptyRood(long request){

            if(!map.containsKey(request)){
                map.put(request, request+1);
                return request;
            }

            long next_room = map.get(request);
            long empty_room = findEmptyRood(next_room);
            map.put(request, empty_room);
            return empty_room;
        }
}
```

{% endtab %}
{% endtabs %}
