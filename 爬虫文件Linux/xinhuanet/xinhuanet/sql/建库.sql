CREATE DATABASE `xinhuanet` /*!40100 DEFAULT CHARACTER SET utf8 */;

CREATE TABLE `xinhuanet_all` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `news_id` varchar(255) DEFAULT NULL COMMENT '新闻编号',
  `news_title` varchar(255) DEFAULT NULL COMMENT '新闻标题',
  `news_pubtime` varchar(255) DEFAULT NULL COMMENT '发布时间',
  `news_author` varchar(255) DEFAULT NULL COMMENT '作者',
  `news_url` varchar(255) DEFAULT NULL COMMENT '新闻链接',
  `news_img_arr` varchar(255) DEFAULT NULL COMMENT '包含图片',
  `news_keyword` varchar(255) DEFAULT NULL COMMENT '包含关键字',
  `news_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP COMMENT '入库时间',
  PRIMARY KEY (`Id`),
  UNIQUE KEY `news_id` (`news_id`)
) ENGINE=MyISAM AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COMMENT='所有页面';
