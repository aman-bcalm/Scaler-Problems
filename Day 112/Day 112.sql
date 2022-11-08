SELECT e1.manager_id,
       CONCAT(e2.first_name, " ", e2.last_name) AS Manager ,
       CONCAT(e1.first_name," ",e1.last_name) AS Employee   
FROM employees AS e1  JOIN employees AS e2
     ON e1.manager_id = e2.employee_id 
ORDER BY manager_id, Employee ASC 



WITH net_sal AS (
    SELECT *,
           salary + 5000 AS Net_Salary
    FROM employees

)


SELECT employee_id,
       first_name,
       last_name,
       salary,
       Net_Salary 
FROM net_sal
WHERE Net_Salary > 5000






WITH net_sal AS (
    SELECT *,
           salary + (salary * ifnull(commission_pct, 0)) AS Net_Salary
    FROM employees

)


SELECT employee_id,
       first_name,
       last_name,
       salary,
       Net_Salary 
FROM net_sal
WHERE Net_Salary > 15000





SELECT *
FROM employees
WHERE department_id = 80
UNION
SELECT *
FROM employees
WHERE salary > 10000






CREATE VIEW emp_view AS 
SELECT e.employee_id,
       e.first_name,
       e.last_name,
       e.salary,
       e.department_id,
       d.department_name,
       l.location_id,
       l.street_address,
       l.city AS city
FROM employees AS e JOIN departments AS d 
     ON e.department_id = d.department_id 
     JOIN locations AS l 
     ON d.location_id = l.location_id;


SELECT *
FROM emp_view
WHERE city = "Seattle"
      OR
      city = "Southlake"






SELECT manager_id FROM employees
UNION
SELECT manager_id FROM departments 




with t as
(select distinct salary 
from employees 
order by salary desc 
limit 12)
select salary from t 
order by salary ASC limit 1;



Alternate solution 


CREATE VIEW tbl  AS 
SELECT DENSE_RANK() OVER( ORDER BY salary DESC) AS dense,
       salary
FROM employees;
    

SELECT salary 
FROM tbl
WHERE dense = 12   




