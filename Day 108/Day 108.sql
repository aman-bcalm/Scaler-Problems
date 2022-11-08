SELECT CONCAT(first_name," ",last_name) AS full_name,
       salary
FROM employees
WHERE salary NOT BETWEEN 6000 AND 18000
ORDER BY full_name ASC


SELECT emp.employee_id,
       CONCAT(emp.first_name," ",emp.last_name) AS full_name,
       emp.salary
FROM employees as emp LEFT JOIN departments as d 
     ON emp.department_id = d.department_id
WHERE d.department_name IN ('Administration', 'Marketing', 'Human Resources')



SELECT  first_name,  last_name, job_id, hire_date
FROM employees
WHERE hire_date BETWEEN "1998/11/15" AND  "2001/08/25"


SELECT employee_id,
       CONCAT(first_name," ",last_name) AS full_name,
       phone_number
FROM employees
WHERE first_name LIKE "%n"


SELECT  employee_id,first_name, last_name,job_id,manager_id
FROM employees
WHERE department_id IS NULL

SELECT employee_id,
       CONCAT(first_name," ",last_name) AS full_name,
       salary
FROM employees
WHERE manager_id IN (
      SELECT employee_id
      FROM employees
      WHERE first_name = "Adam"
      )


SELECT CONCAT(first_name," ",last_name) AS full_name,
       salary,
       department_id,
       job_id
FROM employees
WHERE job_id IN (
      SELECT job_id
      FROM employees
      WHERE employee_id = 107
      )


SELECT employee_id, 
       first_name,
       last_name,
       salary
FROM employees
WHERE department_id IN (50,10,80)
      AND 
      salary BETWEEN 5000 AND 10000
      AND
      commission_pct IS NULL 


select employee_id, first_name, last_name, salary, 
CASE when job_id in ('AC_ACCOUNT', 'FI_ACCOUNT') then 1 
else 0 
end as 'Accountant' 
from employees;



SELECT employee_id,
       salary,
       CASE
        WHEN salary < 10000 THEN 'Class C'
        WHEN salary BETWEEN 10000 AND 20000 THEN 'Class B'
        ELSE 'Class A'
       END AS Salary_bin
FROM employees


SELECT emp.first_name,
        emp.last_name,
        emp.employee_id,
        emp.job_id
FROM employees AS emp LEFT JOIN departments AS dep 
     ON emp.department_id = dep.department_id
     LEFT JOIN locations AS loc 
     ON  loc.location_id = dep.location_id
WHERE loc.city = "Seattle"



SELECT employee_id, first_name, last_name, email, phone_number, hire_date, job_id, salary, commission_pct, manager_id, department_id
FROM employees
WHERE employee_id NOT IN (
    SELECT employee_id
    FROM job_history
)
