/*
Navicat MySQL Data Transfer

Source Server         : mysql
Source Server Version : 50505
Source Host           : localhost:3306
Source Database       : spotify_api

Target Server Type    : MYSQL
Target Server Version : 50505
File Encoding         : 65001

Date: 2021-08-16 07:14:03
*/

SET FOREIGN_KEY_CHECKS=0;
-- ----------------------------
-- Table structure for `albums`
-- ----------------------------
DROP TABLE IF EXISTS `albums`;
CREATE TABLE `albums` (
  `id` varchar(30) NOT NULL,
  `name` varchar(45) NOT NULL,
  `label` varchar(45) NOT NULL,
  `popularity` int(11) NOT NULL,
  `total_tracks` int(11) NOT NULL,
  `release_date` date NOT NULL,
  `uri` varchar(45) NOT NULL,
  `url` varchar(45) NOT NULL,
  `href` varchar(45) NOT NULL,
  `img` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of albums
-- ----------------------------

-- ----------------------------
-- Table structure for `tracks`
-- ----------------------------
DROP TABLE IF EXISTS `tracks`;
CREATE TABLE `tracks` (
  `id` varchar(30) NOT NULL,
  `name` varchar(45) NOT NULL,
  `popularity` int(11) NOT NULL,
  `duration_ms` int(11) NOT NULL,
  `type` varchar(45) NOT NULL,
  `uri` varchar(45) NOT NULL,
  `url` varchar(45) NOT NULL,
  `href` varchar(45) NOT NULL,
  `album_id` varchar(30) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_tracks_albums` (`album_id`),
  CONSTRAINT `fk_tracks_albums` FOREIGN KEY (`album_id`) REFERENCES `albums` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of tracks
-- ----------------------------

-- ----------------------------
-- Table structure for `artists`
-- ----------------------------
DROP TABLE IF EXISTS `artists`;
CREATE TABLE `artists` (
  `id` varchar(30) NOT NULL,
  `name` varchar(45) NOT NULL,
  `followers` int(11) NOT NULL,
  `popularity` int(11) NOT NULL,
  `type` varchar(45) NOT NULL,
  `uri` varchar(45) NOT NULL,
  `url` varchar(45) NOT NULL,
  `href` varchar(45) NOT NULL,
  `img` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of artists
-- ----------------------------

-- ----------------------------
-- Table structure for `genres`
-- ----------------------------
DROP TABLE IF EXISTS `genres`;
CREATE TABLE `genres` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of genres
-- ----------------------------

-- ----------------------------
-- Table structure for `users`
-- ----------------------------
DROP TABLE IF EXISTS `users`;
CREATE TABLE `users` (
  `id` varchar(45) NOT NULL,
  `name` varchar(45) NOT NULL,
  `followers` int(11) NOT NULL,
  `type` varchar(45) NOT NULL,
  `uri` varchar(45) NOT NULL,
  `url` varchar(45) NOT NULL,
  `href` varchar(45) NOT NULL,
  `img` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of users
-- ----------------------------

-- ----------------------------
-- Table structure for `playlists`
-- ----------------------------
DROP TABLE IF EXISTS `playlists`;
CREATE TABLE `playlists` (
  `id` varchar(30) NOT NULL,
  `name` varchar(45) NOT NULL,
  `description` text DEFAULT NULL,
  `followers` int(11) NOT NULL DEFAULT 0,
  `type` varchar(45) NOT NULL,
  `uri` varchar(45) NOT NULL,
  `url` varchar(45) NOT NULL,
  `href` varchar(45) NOT NULL,
  `img` varchar(45) NOT NULL,
  `user_id` varchar(45) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_playlists_users` (`user_id`),
  CONSTRAINT `fk_playlists_users` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of playlists
-- ----------------------------

-- ----------------------------
-- Table structure for `albums_artists`
-- ----------------------------
DROP TABLE IF EXISTS `albums_artists`;
CREATE TABLE `albums_artists` (
  `album_id` varchar(30) NOT NULL,
  `artist_id` varchar(30) NOT NULL,
  PRIMARY KEY (`album_id`,`artist_id`),
  KEY `fk_albums_artists_artists` (`artist_id`),
  CONSTRAINT `fk_albums_artists_albums` FOREIGN KEY (`album_id`) REFERENCES `albums` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_albums_artists_artists` FOREIGN KEY (`artist_id`) REFERENCES `artists` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of albums_artists
-- ----------------------------

-- ----------------------------
-- Table structure for `artists_genres`
-- ----------------------------
DROP TABLE IF EXISTS `artists_genres`;
CREATE TABLE `artists_genres` (
  `artist_id` varchar(30) NOT NULL,
  `genre_id` int(11) NOT NULL,
  PRIMARY KEY (`artist_id`,`genre_id`),
  KEY `fk_artists_genres_genres` (`genre_id`),
  CONSTRAINT `fk_artists_genres_artists` FOREIGN KEY (`artist_id`) REFERENCES `artists` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_artists_genres_genres` FOREIGN KEY (`genre_id`) REFERENCES `genres` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of artists_genres
-- ----------------------------

-- ----------------------------
-- Table structure for `artists_tracks`
-- ----------------------------
DROP TABLE IF EXISTS `artists_tracks`;
CREATE TABLE `artists_tracks` (
  `artist_id` varchar(30) NOT NULL,
  `track_id` varchar(30) NOT NULL,
  PRIMARY KEY (`artist_id`,`track_id`),
  KEY `fk_artists_tracks_tracks` (`track_id`),
  CONSTRAINT `fk_artists_tracks_artists` FOREIGN KEY (`artist_id`) REFERENCES `artists` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_artists_tracks_tracks` FOREIGN KEY (`track_id`) REFERENCES `tracks` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of artists_tracks
-- ----------------------------

-- ----------------------------
-- Table structure for `playlists_tracks`
-- ----------------------------
DROP TABLE IF EXISTS `playlists_tracks`;
CREATE TABLE `playlists_tracks` (
  `playlist_id` varchar(30) NOT NULL,
  `track_id` varchar(30) NOT NULL,
  PRIMARY KEY (`playlist_id`,`track_id`),
  KEY `fk_playlists_tracks_tracks` (`track_id`),
  CONSTRAINT `fk_playlists_tracks_playlists` FOREIGN KEY (`playlist_id`) REFERENCES `playlists` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_playlists_tracks_tracks` FOREIGN KEY (`track_id`) REFERENCES `tracks` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of playlists_tracks
-- ----------------------------
