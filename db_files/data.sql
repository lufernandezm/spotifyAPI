-- ----------------------------
-- Records of albums
-- ----------------------------
INSERT INTO `albums` VALUES ('41MnTivkwTO3UUJ8DrqEJJ', 'The Best Of Keane (Deluxe Edition)', 'album', 'spotify:album:41MnTivkwTO3UUJ8DrqEJJ', 'https://open.spotify.com/album/41MnTivkwTO3UU', 'https://api.spotify.com/v1/albums/41MnTivkwTO', 'https://i.scdn.co/image/ab67616d0000b273adde6', '2013-01-01', '0');

-- ----------------------------
-- Records of artists
-- ----------------------------
INSERT INTO `artists` VALUES ('0oSGxfWSnnOXhD2fKuz2Gy', 'David Bowie', 'artist', 'spotify:artist:0oSGxfWSnnOXhD2fKuz2Gy', 'https://open.spotify.com/artist/0oSGxfWSnnOXh', 'https://api.spotify.com/v1/artists/0oSGxfWSnn', 'https://i.scdn.co/image/ab6761610000e5eb0db3b', '7113161', '82');
INSERT INTO `artists` VALUES ('53A0W3U0s8diEn9RhXQhVz', 'Keane', 'artist', 'spotify:artist:53A0W3U0s8diEn9RhXQhVz', 'https://open.spotify.com/artist/53A0W3U0s8diE', 'https://api.spotify.com/v1/artists/53A0W3U0s8', 'https://i.scdn.co/image/ab6761610000e5eb6fa4f', '2273982', '73');

-- ----------------------------
-- Records of genres
-- ----------------------------
INSERT INTO `genres` VALUES ('1', 'rock');
INSERT INTO `genres` VALUES ('2', 'art rock');
INSERT INTO `genres` VALUES ('3', 'classic rock');
INSERT INTO `genres` VALUES ('4', 'glam rock');
INSERT INTO `genres` VALUES ('5', 'permanent wave');

-- ----------------------------
-- Records of albums_artists
-- ----------------------------
INSERT INTO `albums_artists` VALUES ('41MnTivkwTO3UUJ8DrqEJJ', '53A0W3U0s8diEn9RhXQhVz');

-- ----------------------------
-- Records of artists_genres
-- ----------------------------
INSERT INTO `artists_genres` VALUES ('0oSGxfWSnnOXhD2fKuz2Gy', '1');
