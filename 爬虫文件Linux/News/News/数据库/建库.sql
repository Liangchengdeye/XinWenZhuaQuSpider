#建立数据库
CREATE DATABASE `news` /*!40100 DEFAULT CHARACTER SET utf8 */;
#business表单
CREATE TABLE `en_people_business` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `business_id` varchar(255) CHARACTER SET utf8 DEFAULT NULL COMMENT '新闻ID',
  `business_title` varchar(1024) COLLATE utf8_bin DEFAULT NULL COMMENT '文章标题',
  `business_url` varchar(255) COLLATE utf8_bin DEFAULT NULL COMMENT '文章链接',
  `business_time` varchar(255) CHARACTER SET utf8 DEFAULT NULL COMMENT '发布时间',
  `Storage_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP COMMENT '入库时间',
  PRIMARY KEY (`Id`),
  UNIQUE KEY `business_id` (`business_id`)
) ENGINE=MyISAM AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COLLATE=utf8_bin COMMENT='business';
#culture表单
CREATE TABLE `en_people_culture` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `culture_id` varchar(255) CHARACTER SET utf8 DEFAULT NULL COMMENT '新闻ID',
  `culture_title` varchar(1024) COLLATE utf8_bin DEFAULT NULL COMMENT '文章标题',
  `culture_url` varchar(255) COLLATE utf8_bin DEFAULT NULL COMMENT '文章链接',
  `culture_time` varchar(255) COLLATE utf8_bin DEFAULT NULL COMMENT '发布时间',
  `Storage_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP COMMENT '入库时间',
  PRIMARY KEY (`Id`),
  UNIQUE KEY `culture_id` (`culture_id`)
) ENGINE=MyISAM AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COLLATE=utf8_bin COMMENT='culture';
#health表单
CREATE TABLE `en_people_health` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `health_id` varchar(255) CHARACTER SET utf8 DEFAULT NULL COMMENT '新闻ID',
  `health_title` varchar(1024) COLLATE utf8_bin DEFAULT NULL COMMENT '文章标题',
  `health_url` varchar(255) COLLATE utf8_bin DEFAULT NULL COMMENT '文章链接',
  `health_time` varchar(255) COLLATE utf8_bin DEFAULT NULL COMMENT '发布时间',
  `Storage_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP COMMENT '入库时间',
  PRIMARY KEY (`Id`),
  UNIQUE KEY `health_id` (`health_id`)
) ENGINE=MyISAM AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COLLATE=utf8_bin COMMENT='health';
#首页home表单
CREATE TABLE `en_people_home` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `home_id` varchar(255) CHARACTER SET utf8 DEFAULT NULL COMMENT '新闻ID',
  `home_title` varchar(1024) COLLATE utf8_bin DEFAULT NULL COMMENT '文章标题',
  `home_url` varchar(255) COLLATE utf8_bin DEFAULT NULL COMMENT '文章链接',
  `Storage_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP COMMENT '入库时间',
  PRIMARY KEY (`Id`),
  UNIQUE KEY `home_id` (`home_id`)
) ENGINE=MyISAM AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COLLATE=utf8_bin COMMENT='home';
 #最新新闻latest1表单
CREATE TABLE `en_people_latest_new1` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `latest_new1_id` varchar(255) CHARACTER SET utf8 DEFAULT NULL COMMENT '新闻ID',
  `latest_new1_title` varchar(1024) COLLATE utf8_bin DEFAULT NULL COMMENT '文章标题',
  `latest_new1_url` varchar(255) COLLATE utf8_bin DEFAULT NULL COMMENT '文章链接',
  `latest_new1_time` varchar(255) COLLATE utf8_bin DEFAULT NULL COMMENT '发布时间',
  `Storage_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP COMMENT '入库时间',
  PRIMARY KEY (`Id`),
  UNIQUE KEY `latest_new1_id` (`latest_new1_id`)
) ENGINE=MyISAM AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COLLATE=utf8_bin COMMENT='latest_new1';
#最新新闻latest2表单
CREATE TABLE `en_people_latest_new2` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `latest_new2_id` varchar(255) CHARACTER SET utf8 DEFAULT NULL COMMENT '新闻ID',
  `latest_new2_title` varchar(1024) COLLATE utf8_bin DEFAULT NULL COMMENT '文章标题',
  `latest_new2_url` varchar(255) COLLATE utf8_bin DEFAULT NULL COMMENT '文章链接',
  `latest_new2_time` varchar(255) COLLATE utf8_bin DEFAULT NULL COMMENT '发布时间',
  `Storage_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP COMMENT '入库时间',
  PRIMARY KEY (`Id`),
  UNIQUE KEY `latest_new2_id` (`latest_new2_id`)
) ENGINE=MyISAM AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COLLATE=utf8_bin COMMENT='latest_new2';
#新闻详情页表单
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
#military表单
CREATE TABLE `en_people_military` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `military_id` varchar(255) CHARACTER SET utf8 DEFAULT NULL COMMENT '新闻ID',
  `military_title` varchar(1024) COLLATE utf8_bin DEFAULT NULL COMMENT '文章标题',
  `military_url` varchar(255) COLLATE utf8_bin DEFAULT NULL COMMENT '文章链接',
  `military_time` varchar(255) COLLATE utf8_bin DEFAULT NULL COMMENT '发布时间',
  `Storage_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP COMMENT '入库时间',
  PRIMARY KEY (`Id`),
  UNIQUE KEY `military_id` (`military_id`)
) ENGINE=MyISAM AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COLLATE=utf8_bin COMMENT='military';
#odds表单
CREATE TABLE `en_people_odds` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `odds_id` varchar(255) CHARACTER SET utf8 DEFAULT NULL COMMENT '新闻ID',
  `odds_title` varchar(1024) COLLATE utf8_bin DEFAULT NULL COMMENT '文章标题',
  `odds_url` varchar(255) COLLATE utf8_bin DEFAULT NULL COMMENT '文章链接',
  `odds_time` varchar(255) COLLATE utf8_bin DEFAULT NULL COMMENT '发布时间',
  `Storage_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP COMMENT '入库时间',
  PRIMARY KEY (`Id`),
  UNIQUE KEY `odds_id` (`odds_id`)
) ENGINE=MyISAM AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COLLATE=utf8_bin COMMENT='odds';
#opinions表单
CREATE TABLE `en_people_opinions` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `opinions_id` varchar(255) CHARACTER SET utf8 DEFAULT NULL COMMENT '新闻ID',
  `opinions_title` varchar(1024) COLLATE utf8_bin DEFAULT NULL COMMENT '文章标题',
  `opinions_url` varchar(255) COLLATE utf8_bin DEFAULT NULL COMMENT '文章链接',
  `opinions_time` varchar(255) COLLATE utf8_bin DEFAULT NULL COMMENT '发布时间',
  `Storage_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP COMMENT '入库时间',
  PRIMARY KEY (`Id`),
  UNIQUE KEY `opinions_id` (`opinions_id`)
) ENGINE=MyISAM AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COLLATE=utf8_bin COMMENT='opinions';
#photo表单
CREATE TABLE `en_people_photo` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `photo_id` varchar(255) CHARACTER SET utf8 DEFAULT NULL COMMENT '新闻ID',
  `photo_title` varchar(1024) COLLATE utf8_bin DEFAULT NULL COMMENT '文章标题',
  `photo_url` varchar(255) COLLATE utf8_bin DEFAULT NULL COMMENT '文章链接',
  `photo_time` varchar(255) COLLATE utf8_bin DEFAULT NULL COMMENT '发布时间',
  `Storage_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP COMMENT '入库时间',
  PRIMARY KEY (`Id`),
  UNIQUE KEY `photo_id` (`photo_id`)
) ENGINE=MyISAM AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COLLATE=utf8_bin COMMENT='photo';
#science表单
CREATE TABLE `en_people_science` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `science_id` varchar(255) CHARACTER SET utf8 DEFAULT NULL COMMENT '新闻ID',
  `science_title` varchar(1024) COLLATE utf8_bin DEFAULT NULL COMMENT '文章标题',
  `science_url` varchar(255) COLLATE utf8_bin DEFAULT NULL COMMENT '文章链接',
  `science_time` varchar(255) COLLATE utf8_bin DEFAULT NULL COMMENT '发布时间',
  `Storage_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP COMMENT '入库时间',
  PRIMARY KEY (`Id`),
  UNIQUE KEY `science_id` (`science_id`)
) ENGINE=MyISAM AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COLLATE=utf8_bin COMMENT='science';
#society表单
CREATE TABLE `en_people_society` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `society_id` varchar(255) CHARACTER SET utf8 DEFAULT NULL COMMENT '新闻ID',
  `society_title` varchar(1024) COLLATE utf8_bin DEFAULT NULL COMMENT '文章标题',
  `society_url` varchar(255) COLLATE utf8_bin DEFAULT NULL COMMENT '文章链接',
  `society_time` varchar(255) COLLATE utf8_bin DEFAULT NULL COMMENT '发布时间',
  `Storage_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP COMMENT '入库时间',
  PRIMARY KEY (`Id`),
  UNIQUE KEY `society_id` (`society_id`)
) ENGINE=MyISAM AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COLLATE=utf8_bin COMMENT='society';
#special表单
CREATE TABLE `en_people_special` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `special_id` varchar(255) CHARACTER SET utf8 DEFAULT NULL COMMENT '新闻ID',
  `special_title` varchar(1024) COLLATE utf8_bin DEFAULT NULL COMMENT '文章标题',
  `special_url` varchar(255) COLLATE utf8_bin DEFAULT NULL COMMENT '文章链接',
  `special_time` varchar(255) COLLATE utf8_bin DEFAULT NULL COMMENT '发布时间',
  `Storage_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP COMMENT '入库时间',
  PRIMARY KEY (`Id`),
  UNIQUE KEY `special_id` (`special_id`)
) ENGINE=MyISAM AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COLLATE=utf8_bin COMMENT='special';
#sports表单
CREATE TABLE `en_people_sports` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `sports_id` varchar(255) CHARACTER SET utf8 DEFAULT NULL COMMENT '新闻ID',
  `sports_title` varchar(1024) COLLATE utf8_bin DEFAULT NULL COMMENT '文章标题',
  `sports_url` varchar(255) COLLATE utf8_bin DEFAULT NULL COMMENT '文章链接',
  `sports_time` varchar(255) COLLATE utf8_bin DEFAULT NULL COMMENT '发布时间',
  `Storage_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP COMMENT '入库时间',
  PRIMARY KEY (`Id`),
  UNIQUE KEY `sports_id` (`sports_id`)
) ENGINE=MyISAM AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COLLATE=utf8_bin COMMENT='sports';
#stories表单
CREATE TABLE `en_people_stories` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `stories_id` varchar(255) CHARACTER SET utf8 DEFAULT NULL COMMENT '新闻ID',
  `stories_title` varchar(1024) COLLATE utf8_bin DEFAULT NULL COMMENT '文章标题',
  `stories_url` varchar(255) COLLATE utf8_bin DEFAULT NULL COMMENT '文章链接',
  `stories_time` varchar(255) COLLATE utf8_bin DEFAULT NULL COMMENT '发布时间',
  `Storage_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP COMMENT '入库时间',
  PRIMARY KEY (`Id`),
  UNIQUE KEY `stories_id` (`stories_id`)
) ENGINE=MyISAM AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COLLATE=utf8_bin COMMENT='stories';
#travel表单
CREATE TABLE `en_people_travel` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `travel_id` varchar(255) CHARACTER SET utf8 DEFAULT NULL COMMENT '新闻ID',
  `travel_title` varchar(1024) COLLATE utf8_bin DEFAULT NULL COMMENT '文章标题',
  `travel_url` varchar(255) COLLATE utf8_bin DEFAULT NULL COMMENT '文章链接',
  `travel_time` varchar(255) COLLATE utf8_bin DEFAULT NULL COMMENT '发布时间',
  `Storage_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP COMMENT '入库时间',
  PRIMARY KEY (`Id`),
  UNIQUE KEY `travel_id` (`travel_id`)
) ENGINE=MyISAM AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COLLATE=utf8_bin COMMENT='travel';
#video表单
CREATE TABLE `en_people_video` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `video_id` varchar(255) CHARACTER SET utf8 DEFAULT NULL COMMENT '新闻ID',
  `video_title` varchar(1024) COLLATE utf8_bin DEFAULT NULL COMMENT '文章标题',
  `video_url` varchar(255) COLLATE utf8_bin DEFAULT NULL COMMENT '文章链接',
  `video_time` varchar(255) COLLATE utf8_bin DEFAULT NULL COMMENT '发布时间',
  `Storage_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP COMMENT '入库时间',
  PRIMARY KEY (`Id`),
  UNIQUE KEY `video_id` (`video_id`)
) ENGINE=MyISAM AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COLLATE=utf8_bin COMMENT='video';
#world表单
CREATE TABLE `en_people_world` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `world_id` varchar(255) CHARACTER SET utf8 DEFAULT NULL COMMENT '新闻ID',
  `world_title` varchar(1024) COLLATE utf8_bin DEFAULT NULL COMMENT '文章标题',
  `world_url` varchar(255) COLLATE utf8_bin DEFAULT NULL COMMENT '文章链接',
  `world_time` varchar(255) COLLATE utf8_bin DEFAULT NULL COMMENT '发布时间',
  `Storage_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP COMMENT '入库时间',
  PRIMARY KEY (`Id`),
  UNIQUE KEY `world_id` (`world_id`)
) ENGINE=MyISAM AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COLLATE=utf8_bin COMMENT='world';


