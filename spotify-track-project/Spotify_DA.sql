use spotify ;
select * from track_data;
select * from track_data order by popularity desc limit 1;
select Avg(popularity) as Average_Popularity  from track_data;
select * from track_data where duration_min > 4.0 ;

select 
case 
   when popularity > 80 then "Very Popular"
   when popularity > 50 then "Popular"
   when popularity <50 then "Low popular"
end as Catagory,
count(*)  as tracks
 from track_data   group by  Catagory  ;
 
 
 select * ,
 case 
 when popularity > 80 then "Very Popular"
 when popularity > 50 then "Popular"
 else 
 "Less Popular"
 end as catogory  from track_data order by popularity desc;
 