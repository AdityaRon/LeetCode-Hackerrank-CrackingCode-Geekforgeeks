select Id from (
select Id, RecordDate, Temperature, LAG(Temperature,1,NULL) over(order by RecordDate) as previous_temp, LAG(RecordDate,1,NULL) over(order by RecordDate) as prev_date
from Weather ) x where Temperature > previous_temp
and datediff(day,prev_date,RecordDate) = 1