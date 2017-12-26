#建立数据库
CREATE DATABASE `chinadaily` /*!40100 DEFAULT CHARACTER SET utf8 */;
#首页建立
CREATE TABLE `china_home` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `home_id` varchar(255) DEFAULT NULL COMMENT '新闻ID',
  `home_title` varchar(255) DEFAULT NULL COMMENT '新闻标题',
  `home_url` varchar(255) DEFAULT NULL COMMENT '新闻链接',
  `home_pubtime` varchar(255) DEFAULT NULL COMMENT '新闻发布时间',
  `inster_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP COMMENT '入库时间',
  PRIMARY KEY (`Id`),
  UNIQUE KEY `home_id` (`home_id`)
) ENGINE=MyISAM AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COMMENT='首页';
#最新新闻页
CREATE TABLE `china_latest` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `latest_id` varchar(255) DEFAULT NULL COMMENT '新闻ID',
  `latest_title` varchar(255) DEFAULT NULL COMMENT '新闻标题',
  `latest_url` varchar(255) DEFAULT NULL COMMENT '新闻链接',
  `latest_pubtime` varchar(255) DEFAULT NULL COMMENT '新闻发布时间',
  `inster_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP COMMENT '入库时间',
  PRIMARY KEY (`Id`),
  UNIQUE KEY `latest_id` (`latest_id`)
) ENGINE=MyISAM AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COMMENT='最新新闻';
#新闻页一
CREATE TABLE `china_news1` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `news1_id` varchar(255) DEFAULT NULL COMMENT '新闻ID',
  `news1_title` varchar(255) DEFAULT NULL COMMENT '新闻标题',
  `news1_url` varchar(255) DEFAULT NULL COMMENT '新闻链接',
  `news1_pubtime` varchar(255) DEFAULT NULL COMMENT '新闻发布时间',
  `inster_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP COMMENT '入库时间',
  PRIMARY KEY (`Id`),
  UNIQUE KEY `news1_id` (`news1_id`)
) ENGINE=MyISAM AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COMMENT='规则栏一';
#新闻页二
CREATE TABLE `china_news2` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `news2_id` varchar(255) DEFAULT NULL COMMENT '新闻ID',
  `news2_title` varchar(255) DEFAULT NULL COMMENT '新闻标题',
  `news2_url` varchar(255) DEFAULT NULL COMMENT '新闻链接',
  `news2_pubtime` varchar(255) DEFAULT NULL COMMENT '新闻发布时间',
  `inster_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP COMMENT '入库时间',
  PRIMARY KEY (`Id`),
  UNIQUE KEY `news2_id` (`news2_id`)
) ENGINE=MyISAM AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COMMENT='规则栏二';
#图片新闻
CREATE TABLE `china_photos` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `photos_id` varchar(255) DEFAULT NULL COMMENT '新闻ID',
  `photos_title` varchar(255) DEFAULT NULL COMMENT '新闻标题',
  `photos_url` varchar(255) DEFAULT NULL COMMENT '新闻链接',
  `photos_pubtime` varchar(255) DEFAULT NULL COMMENT '新闻发布时间',
  `inster_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP COMMENT '入库时间',
  PRIMARY KEY (`Id`),
  UNIQUE KEY `photos_id` (`photos_id`)
) ENGINE=MyISAM AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COMMENT='照片栏';
