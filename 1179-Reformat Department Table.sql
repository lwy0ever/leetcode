# Write your MySQL query statement below
select id,
 sum(case month when 'Jan' then revenue else NULL end) as 'Jan_Revenue',
 sum(case month when 'Feb' then revenue else NULL end) as 'Feb_Revenue',
 sum(case month when 'Mar' then revenue else NULL end) as 'Mar_Revenue',
 sum(case month when 'Apr' then revenue else NULL end) as 'Apr_Revenue',
 sum(case month when 'May' then revenue else NULL end) as 'May_Revenue',
 sum(case month when 'Jun' then revenue else NULL end) as 'Jun_Revenue',
 sum(case month when 'Jul' then revenue else NULL end) as 'Jul_Revenue',
 sum(case month when 'Aug' then revenue else NULL end) as 'Aug_Revenue',
 sum(case month when 'Sep' then revenue else NULL end) as 'Sep_Revenue',
 sum(case month when 'Oct' then revenue else NULL end) as 'Oct_Revenue',
 sum(case month when 'Nov' then revenue else NULL end) as 'Nov_Revenue',
 sum(case month when 'Dec' then revenue else NULL end) as 'Dec_Revenue'
 from Department
 group by id