select * from employees where salary in (
select max(salary) from employees where salary < 
(select max(salary) from employees where salary < (
select max(salary) from employees)));


SELECT emp.employee_id, emp.department_id, emp.first_name, emp.last_name, emp.job_id, dep.department_name
FROM employees as emp LEFT JOIN departments as dep 
     ON emp.department_id =  dep.department_id
WHERE dep.department_name  = "Human Resources"


SELECT e.employee_id, e.first_name, e.last_name, e.department_id, e.salary
FROM employees as e
WHERE e.salary < (
    SELECT avg(e1.SALARY)
    from employee as e1
    WHERE e1.department_id = e.department_id 
)


SELECT emp.employee_id, dp.department_name, jb.job_id, jb.job_title, jb.min_salary
FROM employees as emp LEFT JOIN job_history as jbh 
     ON emp.employee_id = jbh.employee_id 
     LEFT JOIN jobs as jb 
     ON jbh.job_id = jb.job_id 
     LEFT JOIN departments as dp 
     ON emp.department_id = dp.department_id
WHERE jb.job_title LIKE "%sales%" OR jb.job_title LIKE "%Account%"
      AND 
      jb.min_salary >= 6000



SELECT e1.employee_id, e1.first_name, e1.last_name
FROM employees as e1 JOIN employees as e2
     ON e1.manager_id = e2.employee_id
     JOIN departments as dept
     ON e2.department_id = dept.department_id
     JOIN locations as loc
     ON dept.location_id = loc.location_id
WHERE loc.country_id = "US"
order by e1.employee_id


SELECT emp.employee_id, emp.first_name, emp.last_name, emp.salary, dep.department_name, loc.city
FROM employees as emp LEFT JOIN departments as dep
     ON emp.department_id =  dep.department_id
     LEFT JOIN locations as loc
     ON dep.location_id = loc.location_id 
WHERE emp.salary IN (

SELECT MIN(salary)
FROM employees
WHERE hire_date BETWEEN "1998-01-01" AND "2003-12-31" )



SELECT coun.country_name
FROM employees as emp LEFT JOIN departments as dep
     ON emp.department_id = dep.department_id 
     LEFT JOIN locations as loc 
     ON dep.location_id = loc.location_id
     LEFT JOIN countries as coun 
     ON loc.country_id = coun.country_id 
GROUP BY coun.country_name 
HAVING AVG(salary) > 8000


SELECT CONCAT(emp1.first_name, " ", emp1.last_name) AS full_name
FROM employees as emp1 JOIN employees as emp2
     ON emp1.employee_id = emp2.manager_id
GROUP BY emp1.employee_id
HAVING COUNT(emp2.employee_id) >= 4

#Same as above

select concat(first_name, ' ', last_name) as 'full_name' 
from employees where employee_id in  
(select manager_id from employees 
group by manager_id having count(*) >= 4);



SELECT dep.*
FROM employees as emp JOIN departments as dep
     ON emp.department_id  = dep.department_id 
GROUP BY dep.department_id 
HAVING MIN(salary) >= 9000



SELECT emp1.employee_id, emp1.first_name, emp1.last_name 
FROM employees as emp1 JOIN employees as emp2
     ON emp1.manager_id = emp2.employee_id 
WHERE emp1.hire_date < emp2.hire_date 




SELECT dept.department_name,
      COUNT(DISTINCT employee_id) AS No_of_Employees,
      SUM(emp.salary) AS Total_Salary 
FROM employees as emp JOIN departments as dept 
     ON emp.department_id = dept.department_id 
GROUP BY dept.department_id
ORDER BY dept.department_name 



SELECT dep.department_id, dep.department_name 
FROM departments as dep LEFT JOIN employees as emp 
     ON dep.department_id = emp.department_id
GROUP BY dep.department_id 
HAVING COUNT(emp.employee_id) = 0


SELECT emp.employee_id,
       CONCAT(emp.first_name," ", emp.last_name) as full_name,
       emp.salary,
       emp.phone_number,
       dep.department_id,
       dep.department_name,
       loc.street_address,
       loc.city,
       con.country_name,
       reg.region_id,
       reg.region_name 
FROM employees as emp JOIN departments as dep
     ON emp.department_id = dep.department_id 
     JOIN locations as loc
     ON dep.location_id = loc.location_id
     JOIN countries as con 
     ON loc.country_id = con.country_id 
     JOIN regions as reg 
     ON con.region_id = reg.region_id 
WHERE reg.region_name = "Europe"
ORDER BY emp.salary DESC, emp.employee_id ASC 



SELECT  department_id AS Department,
        COUNT(employee_id) AS No_of_employees,
        CASE 
            WHEN COUNT(DISTINCT employee_id) = 1 THEN "Junior department"
            WHEN COUNT(DISTINCT employee_id) <= 4 THEN "Intermediate department"
            WHEN COUNT(DISTINCT employee_id) > 4 THEN "Senior department"
        END AS Department_level
FROM employees as emp
GROUP BY department_id 
ORDER BY No_of_employees


