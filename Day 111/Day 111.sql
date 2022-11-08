SELECT employee_id,
       first_name,
       last_name,
        DATEDIFF("2022/06/08", hire_date) / 365 AS Total_years 
FROM employees
WHERE DATEDIFF( "2022/06/08", hire_date)/365 >= 28 



SELECT employee_id,
       first_name,
       last_name,
       salary,
       hire_date,
       Day,
       Month,
       Year
FROM   ( SELECT employee_id,
            first_name,
            last_name,
            salary,
            hire_date,
            EXTRACT(DAY FROM hire_date) AS Day,
            EXTRACT(MONTH FROM hire_date) AS Month,
            EXTRACT(YEAR FROM hire_date) AS Year
        FROM employees) t
WHERE  Year = 2000
        AND
       Month = 1
       AND
       salary > 5000 


SELECT employee_id,
       first_name,
       last_name
FROM employees
WHERE EXTRACT(MONTH FROM hire_date) = 10
      AND 
      salary > 4000



SELECT DISTINCT e1.first_name,
       e1.last_name,
       e1.employee_id,
       e1.salary,
       d.department_name,
       DATEDIFF("2022/06/08", e1.hire_date) / 365 AS Experience
FROM employees as e1 JOIN  departments as d
     ON e1.employee_id = d.manager_id 
WHERE DATEDIFF("2022/06/08", e1.hire_date) / 365 > 25


SELECT Year ,
       Employees
FROM (
(SELECT YEAR,
       COUNT(employee_id) AS Employees 
       
FROM 
(SELECT EXTRACT(YEAR FROM hire_date) AS YEAR,
       employee_id
FROM employees) t
GROUP BY YEAR ) ) tt 
ORDER BY Employees DESC 


select extract(year from hire_date) 'Year', 
count(employee_id) 'Employees' 
from employees 
group by extract(year from hire_date) 
order by Employees desc;


SELECT employee_id,
       first_name,
       last_name,
       salary,
       department_name,
       hire_date,
       city
FROM employees as e JOIN departments as d
     ON e.department_id = d.department_id 
     JOIN locations as loc 
     ON d.location_id = loc.location_id 
WHERE hire_date BETWEEN "1998-01-01" AND DATE_ADD("1998-01-01", INTERVAL 90 DAY);



select employee_id, first_name, last_name,salary, hire_date, department_id 
from(
select employee_id, first_name, last_name, salary, hire_date, department_id, 
dense_rank() 
over(partition by department_id 
order by salary desc) 'Salary_rank' 
from employees 
where hire_date 
between '1998-01-01' and  DATE_SUB('1998-01-01', INTERVAL -180 DAY))t 
where Salary_rank=1;