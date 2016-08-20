use lead_gen_business;

select concat('$',format(sum(b.amount),2)) as 'March_2012_Revenue'
from billing b 
where month(b.charged_datetime) = 3 and year(b.charged_datetime) = '2012';

select concat('$',format(sum(b.amount),2)) as 'Client_ID_2_Revenue'
from billing b 
where b.client_id = 2;

select s.domain_name
from sites s 
where s.client_id = 10;


select c.client_id, concat_ws('/',month(s.created_datetime), year(s.created_datetime)) as 'date', count(1) as 'sites'
	from clients c 
	join sites s on c.client_id = s.client_id
	where c.client_id in (1,20)
	group by concat_ws('/',month(s.created_datetime), year(s.created_datetime))
    order by concat_ws('/',month(s.created_datetime), year(s.created_datetime));

select s.domain_name, sum(1) as 'lead_count'
from sites s 
left join leads l on s.site_id = l.site_id
where date(l.registered_datetime) between '2011-01-01' and '2011-02-15'
group by s.site_id
order by lead_count desc;

select c.first_name, c.last_name, sum(1) as 'lead_count'
from sites s 
join clients c on s.client_id = c.client_id
left join leads l on s.site_id = l.site_id
where date(l.registered_datetime) between '2011-01-01' and '2011-12-31'
group by c.client_id
order by lead_count desc;

select c.first_name, c.last_name, month(l.registered_datetime) 'month_num', sum(1) as 'lead_count'
from sites s 
join clients c on s.client_id = c.client_id
left join leads l on s.site_id = l.site_id
where month(l.registered_datetime) between 1 and 6
	and year(l.registered_datetime) = 2011
group by c.client_id, month_num
order by month_num;

select concat_ws(' ',c.first_name, c.last_name) as 'client_name', s.domain_name, sum(1) as 'lead_count'
from sites s 
join clients c on s.client_id = c.client_id
left join leads l on s.site_id = l.site_id
where date(l.registered_datetime) between '2011-01-01' and '2011-12-31'
group by c.client_id, s.site_id
order by client_name, s.domain_name ;

select concat_ws(' ',c.first_name, c.last_name) as 'client_name', s.domain_name, sum(1) as 'lead_count'
from sites s 
join clients c on s.client_id = c.client_id
left join leads l on s.site_id = l.site_id
group by c.client_id, s.site_id
order by client_name, s.domain_name ;

select concat_ws(' ', c.first_name, c.last_name) as 'client_name', month(b.charged_datetime) 'month_num', concat('$',format(sum(b.amount),2)) 'revenue'
from clients c 
join billing b on c.client_id = b.client_id
group by c.client_id, concat_ws((b.charged_datetime), year(b.charged_datetime));

select concat_ws(' ', c.first_name, c.last_name) as 'client_name', trim(group_concat(' ', s.domain_name)) as 'sites'
from clients c 
join sites s on c.client_id = s.client_id
group by c.client_id;
