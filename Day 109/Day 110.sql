SELECT e.first_name,
       MIN(jbh.start_date) AS first_day_job 
FROM employees AS e  JOIN job_history AS jbh 
     ON e.employee_id = jbh.employee_id
GROUP BY e.employee_id
ORDER BY e.first_name ASC 


ELECT e.first_name,
       MAX(jbh.start_date) AS first_day_job 
FROM employees AS e  JOIN job_history AS jbh 
     ON e.employee_id = jbh.employee_id
GROUP BY e.employee_id
ORDER BY e.first_name ASC 


select distinct first_name,
first_value(start_date) over(partition by jhist.employee_id 
order by start_date) as 'first_day_job'
from job_history jhist 
join employees emp 
on jhist.employee_id=emp.employee_id;


SELECT DISTINCT e.first_name,
       e.last_name,
       FIRST_VALUE(max_salary) OVER(PARTITION BY jbh.employee_id ORDER BY jbh.start_date) AS 'first_job_sal'
FROM employees AS e JOIN job_history AS jbh 
     ON e.employee_id =  jbh.employee_id
     JOIN jobs AS j 
     on jbh.job_id = j.job_id 
ORDER BY e.first_name 




select first_name,
       last_name,
       j.job_title,
       lag(j.job_title, 1) over(partition by e.employee_id order by start_date) 'previous_job'
from employees e join job_history jh
               on e.employee_id=jh.employee_id
               join jobs j
               on j.job_id=jh.job_id;



select e.employee_id,
       first_name,
       last_name,
       j.job_title AS first_job,
       lead(j.job_title, 1) over(partition by e.employee_id order by start_date) AS promoted_to
from employees e join job_history jh
               on e.employee_id=jh.employee_id
               join jobs j
               on j.job_id=jh.job_id;



SELECT e.first_name,
       e.last_name,
       e.department_id,
       e.salary,
       ROUND(CUME_DIST() OVER(PARTITION BY department_id ORDER BY salary DESC) AS cume_dist_sal, 3) 
FROM employees as e 



select department_name, first_name, last_name, salary 
from (
select department_name, dense_rank() over (partition by department_name 
order by salary desc) as rank_value, first_name, 
last_name, salary 
from employees e 
join departments d on d.department_id = e.department_id) t 
where 
rank_value = 1;



SELECT employee_id,
       first_name,
       department_id,
       job_id,
       salary,
       NTILE(4) OVER(ORDER BY salary) AS Quartile
FROM employees 


SELECT d.department_id,
       d.department_name,
       AVG(e.salary) OVER(PARTITION BY d.department_id ORDER BY e.hire_date ASC) AS Average_salary
FROM employees as e JOIN departments as d
     ON e.department_id = d.department_id 


SELECT CONCAT(first_name, " ", last_name) AS full_name,
       department_id,
       salary,
       ROW_NUMBER() OVER(PARTITION BY department_id ORDER BY salary DESC) AS emp_row_no,
       RANK() OVER(PARTITION BY department_id ORDER BY salary DESC) AS emp_rank,
       DENSE_RANK() OVER(PARTITION BY department_id ORDER BY salary DESC) AS emp_dense_rank
FROM employees 
       


select employee_id,department_id,job_id, 
nth_value(first_name,5) over(partition by job_id order by 
salary desc range between 
unbounded preceding and unbounded following) 'fifth_highest' 
from employees;



select job_id , avg(diff) from
(select  * , abs(salary-s) diff from
(select job_id , salary , lag(salary) 
over(partition by job_id order by job_id) as s
from employees) t )tt group by job_id;




