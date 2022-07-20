create database hotel;
use hotel;
create table hotel(h_id int primary key,no_of_rooms int,rate int);
alter table hotel add column h_name varchar(20);
create table guest(g_id int,g_name varchar(20),address varchar(20),phone int,no_of_days int,h_id int,foreign key(h_id) references hotel(h_id));
create table staff(s_id int,s_name varchar(20),h_id int,salary int,design varchar(20));

insert into hotel values(1,15,10000,"samudra"),(2,30,10000,"meridian"),(3,20,20000,"hyatt");

insert into guest values(1,"sankar","calicut",123456,30,1),(2,"arun","malappuram",76327462,20,2),(3,"rahul","mumbai",6453453,15,1),(4,"ramu","bombay",55343456,5,3);
insert into staff values(1,"abc",1,10000,"manager"),(2,"erweabc",2,20000,"hr"),(3,"nvbdsdasds",3,30000,"manager");
insert into staff values(4,"sdasds",3,300000,"hr");

select guest.g_name,guest.g_id,guest.address,hotel.h_name from guest inner join hotel on guest.h_id=hotel.h_id where guest.address="mumbai" and hotel.h_name="samudra";
select (guest.no_of_days*hotel.rate) as paid_amount from guest inner join hotel on guest.h_id=hotel.h_id where guest.g_name="sankar";  

select staff.s_name,staff.salary,staff.design from staff inner join hotel on staff.h_id=hotel.h_id where hotel.h_name="hyatt" order by staff.salary desc;
select hotel.h_name from hotel where no_of_rooms=(select max(hotel.no_of_rooms) from hotel);