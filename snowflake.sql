select distinct t.table_schema, 
       t.table_name,
       c.column_name
from information_schema.tables t
inner join information_schema.columns c on 
       c.table_schema = t.table_schema and c.table_name = t.table_name
where  column_name like '%ACV%'
       --and column_name ilike '%fulfulliment'
order by t.table_schema, 
       t.table_name;
