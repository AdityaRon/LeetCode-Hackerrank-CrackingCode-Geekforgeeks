select distinct a.N, case when a.P is null then 'Root'
when a.N = b.P then 'Inner' 
else 'Leaf' end as cat
from bst a left join bst b on a.N = b.P order by a.N;