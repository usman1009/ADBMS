create database company;
use company;


CREATE TABLE jobs (
    job_id VARCHAR(10),
    job_title VARCHAR(50),
    min_salary INT(10),
    max_salary INT(10),
    PRIMARY KEY (job_id)
);


CREATE TABLE regions (
    region_id VARCHAR(10),
    region_name VARCHAR(30),
    PRIMARY KEY (region_id)
);


CREATE TABLE countries (
    country_id VARCHAR(10),
    country_name VARCHAR(30),
    region_id VARCHAR(10),
    PRIMARY KEY (country_id),
    FOREIGN KEY (region_id)
        REFERENCES regions (region_id)
);
CREATE TABLE locations (
    location_id VARCHAR(10),
    street_address VARCHAR(30),
    postal_code INT(10),
    city VARCHAR(30),
    state_province VARCHAR(30),
    country_id VARCHAR(10),
    PRIMARY KEY (location_id),
    FOREIGN KEY (country_id)
        REFERENCES countries (country_id)
);


CREATE TABLE departments (
    department_id VARCHAR(10),
    department_name VARCHAR(30),
    location_id VARCHAR(10),
    PRIMARY KEY (department_id),
    FOREIGN KEY (location_id)
        REFERENCES locations (location_id)
);
CREATE TABLE employees (
    employee_id VARCHAR(10),
    first_name VARCHAR(30),
    last_name VARCHAR(30),
    email VARCHAR(30),
    phone_number INT(10),
    hire_date VARCHAR(30),
    job_id VARCHAR(10),
    salary INT(10),
    manager_id VARCHAR(10),
    department_id VARCHAR(10),
    PRIMARY KEY (employee_id),
    FOREIGN KEY (job_id)
        REFERENCES jobs (job_id),
    FOREIGN KEY (manager_id)
        REFERENCES employees (employee_id),
    FOREIGN KEY (department_id)
        REFERENCES departments (department_id)
);


CREATE TABLE dependents (
    dependent_id VARCHAR(10),
    first_name VARCHAR(30),
    last_name VARCHAR(30),
    relationship VARCHAR(30),
    employee_id VARCHAR(10),
    PRIMARY KEY (dependent_id),
    FOREIGN KEY (employee_id)
        REFERENCES employees (employee_id)
);

show tables;
alter table countries modify region_id varchar(10) not null;
alter table locations modify country_id varchar(10) not null;
alter table employees modify job_id varchar(10) not null;
alter table dependents modify employee_id varchar(10) not null;
