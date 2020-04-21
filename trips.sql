# Write your MySQL query statement below
SELECT Date(a.request_at) as "Day",
       ROUND(Count(DISTINCT CASE
                        WHEN a.status LIKE '%cancelled%'
                             AND a.banned <> "yes" THEN a.id
                        ELSE NULL
                      END) / Count(CASE
                                     WHEN a.banned <> "yes" THEN a.id
                                     ELSE NULL
                                   END),2) AS "Cancellation Rate"
FROM   (SELECT a.*,
               b.role,
               b.banned
        FROM   trips a
               INNER JOIN users b
                       ON a.client_id = b.users_id
                          AND role = 'client'
        WHERE  Date(request_at) >= '2013-10-01'
               AND Date(request_at) <= '2013-10-03') a
       INNER JOIN (SELECT a.*,
                          b.role,
                          b.banned
                   FROM   trips a
                          INNER JOIN users b
                                  ON a.driver_id = b.users_id
                                     AND role = 'driver'
                   WHERE  Date(request_at) >= '2013-10-01'
                          AND Date(request_at) <= '2013-10-03') b
               ON a.id = b.id
GROUP  BY 1 