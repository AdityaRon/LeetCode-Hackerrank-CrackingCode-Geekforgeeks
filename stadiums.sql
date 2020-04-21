SELECT id, visit_date, currentPeople as people
FROM   (SELECT id, 
               visit_date, 
               people                   AS currentPeople, 
               Lead(people, 1) 
                 OVER ( 
                   ORDER BY visit_date) AS next_1, 
               Lead(people, 2) 
                 OVER ( 
                   ORDER BY visit_date) AS next_2, 
               Lag(people, 1) 
                 OVER ( 
                   ORDER BY visit_date) AS prev_1, 
               Lag(people, 2) 
                 OVER ( 
                   ORDER BY visit_date) AS prev_2 
        FROM   stadium) x 
WHERE  ( currentpeople >= 100 
         AND prev_1 >= 100 
         AND prev_2 >= 100 ) 
        OR ( currentpeople >= 100 
             AND prev_1 >= 100 
             AND next_1 >= 100 ) 
        OR ( currentpeople >= 100 
             AND next_1 >= 100 
             AND next_2 >= 100 ) 