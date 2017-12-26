# Host: localhost  (Version: 5.5.53)
# Date: 2017-10-13 10:20:25
# Generator: MySQL-Front 5.3  (Build 4.234)

/*!40101 SET NAMES utf8 */;

#
# Structure for table "news_list"
#

DROP TABLE IF EXISTS `news_list`;
CREATE TABLE `news_list` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `flag` varchar(255) DEFAULT NULL COMMENT '标识列',
  `news_type` varchar(255) DEFAULT NULL COMMENT '新闻类型',
  `news_type_china` varchar(255) DEFAULT NULL COMMENT '中文类型',
  PRIMARY KEY (`Id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COMMENT='新闻类别';

#
# Data for table "news_list"
#

/*!40000 ALTER TABLE `news_list` DISABLE KEYS */;
INSERT INTO `news_list` VALUES (1,'1','http://en.people.cn/','人民网'),(2,'2','http://www.chinadaily.com.cn/china/','中国日报网'),(3,'3','http://www.xinhuanet.com/english/china/index.htm','新华网');
/*!40000 ALTER TABLE `news_list` ENABLE KEYS */;
