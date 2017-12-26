#建立数据库
CREATE DATABASE `news_all` /*!40100 DEFAULT CHARACTER SET utf8 */;
#人民网详细新闻页
CREATE TABLE `en_people_message` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `NEWS_ID` varchar(255) DEFAULT NULL COMMENT '新闻编号',
  `NEWS_TITLE` varchar(255) DEFAULT NULL COMMENT '新闻标题',
  `NEWS_TIME` varchar(12) DEFAULT NULL COMMENT '新闻发布时间',
  `NEWS_IMG` varchar(2048) DEFAULT NULL COMMENT '新闻图片',
  `NEWS_IMG_TITLE` varchar(2048) DEFAULT NULL COMMENT '新闻图片标题',
  `NEWS_BODY` mediumtext COMMENT '新闻内容',
  `Storage_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP COMMENT '入库时间',
  PRIMARY KEY (`Id`),
  UNIQUE KEY `NEWS_id` (`NEWS_ID`)
) ENGINE=MyISAM AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COMMENT='所有新闻内容表';
#所有新闻
CREATE TABLE `news` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `news_id` varchar(255) DEFAULT NULL COMMENT '新闻编号',
  `news_title` varchar(1024) DEFAULT NULL COMMENT '新闻标题',
  `news_url` varchar(255) DEFAULT NULL COMMENT '新闻链接',
  `news_author` varchar(255) DEFAULT NULL COMMENT '作者',
  `news_pubtime` varchar(255) DEFAULT NULL COMMENT '发布时间',
  `news_img_arr` varchar(255) DEFAULT NULL COMMENT '图片',
  `news_keyword` varchar(255) DEFAULT NULL COMMENT '新闻关键字',
  `flag` varchar(255) DEFAULT NULL COMMENT '新闻标识',
  `storage_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP COMMENT '入库时间',
  PRIMARY KEY (`Id`),
  UNIQUE KEY `news_id` (`news_id`)
) ENGINE=MyISAM AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COMMENT='三个网站所有新闻';
#新闻类型
CREATE TABLE `news_list` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `flag` varchar(255) DEFAULT NULL COMMENT '标识列',
  `news_type` varchar(255) DEFAULT NULL COMMENT '新闻类型',
  `news_type_china` varchar(255) DEFAULT NULL COMMENT '中文类型',
  PRIMARY KEY (`Id`)
) ENGINE=MyISAM AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COMMENT='新闻类别';
