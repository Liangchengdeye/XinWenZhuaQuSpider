--create table ytz6 select zi,nr from ytz5 group by zi,nr order by id asc
CREATE TABLE `en_people_business` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `business_id` varchar(255) CHARACTER SET utf8 DEFAULT NULL COMMENT '新闻ID',
  `business_title` varchar(1024) COLLATE utf8_bin DEFAULT NULL COMMENT '文章标题',
  `business_url` varchar(255) COLLATE utf8_bin DEFAULT NULL COMMENT '文章链接',
  PRIMARY KEY (`Id`),
  UNIQUE KEY `business_id` (`business_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_bin COMMENT='business';


select latest_new1_id from en_people_latest_new1

create table yiti2 select * from yitizi group by zi order by id asc
delete from testtable where id=1672;
select * from testtable
select * from testtable where new_id = '20170911900009267300'
select count(id) from en_people_opinions
select * from en_people_opinions where opinions_id = '20170823900009259116'
insert into testtable(name,url,new_id) values('test3','test3','1002')
select now()
select count(id) from en_people_opinions
select count(id) from en_people_latest_new1
select * from en_people_latest_new1 where latest_new1_id = '20170920900009271248'
select NEWS_BODY from en_people_message where NEWS_ID = '20170924900009273006'
select * from en_people_message where NEWS_BODY is NULL
select * from en_people_message where NEWS_TITLE = 'High on mountain: Yoga enthusiasts practice on cliff'
--新闻首页查询 带跳转查询
select en_people_message.NEWS_ID,en_people_home.home_id,en_people_home.home_title,en_people_message.NEWS_TITLE,en_people_message.NEWS_TIME,en_people_message.NEWS_IMG 
from en_people_home,en_people_message 
where en_people_home.home_id = left(NEWS_ID,length(NEWS_ID)-1)
union all
--新闻首页查询 原地址查询
select en_people_message.NEWS_ID,en_people_home.home_id,en_people_home.home_title,en_people_message.NEWS_TITLE,en_people_message.NEWS_TIME,en_people_message.NEWS_IMG 
from en_people_home,en_people_message 
where en_people_home.home_id = NEWS_ID
union all
--新闻首页查询 带跳转大于10
select en_people_message.NEWS_ID,en_people_home.home_id,en_people_home.home_title,en_people_message.NEWS_TITLE,en_people_message.NEWS_TIME,en_people_message.NEWS_IMG 
from en_people_home,en_people_message 
where en_people_home.home_id = left(NEWS_ID,length(NEWS_ID)-2);


--关键字查询
select NEWS_ID from news.en_people_message where NEWS_TITLE='Miss Tourism Asia crowned in Ningxia (2)' 
--截取
select left(NEWS_ID,length(NEWS_ID)-1) from en_people_message where NEWS_ID='201709259000092734353'
--关键字查询
select NEWS_IMG from en_people_message where NEWS_ID = '20170926900009273664' 
--home筛选
select en_people_home.home_id, NEWS_ID from en_people_home,en_people_message where en_people_home.home_id = left(NEWS_ID,length(NEWS_ID)-1)
select left(NEWS_ID,length(NEWS_ID)-1) from en_people_message where NEWS_ID = '20170925900009273083' or NEWS_ID = '201709259000092734357'


select * from en_people_message where  length(NEWS_ID) = 21
SELECT *   
FROM  en_people_message  
WHERE IF( length(NEWS_ID)==21,  select NEWS_IMG from en_people_message where NEWS_ID = '20170926900009273664'  ,  select NEWS_IMG_TITLE from en_people_message where NEWS_ID = '20170926900009273664'  )   
LIMIT 0 , 30 
SELECT NEWS_ID
from en_people_message
where IF(length(NEWS_ID)=21,'select NEWS_IMG from en_people_message where NEWS_ID = '20170926900009273664'',3);

select 47+109+22;
