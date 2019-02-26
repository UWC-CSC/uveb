USE uveb;

-- Create c_videos table
CREATE TABLE c_videos (
	id smallint unsigned not null auto_increment,

	title varchar(255) not null,
	description varchar(1024),
	thumbnail_uri varchar(2083),
	resolution_w smallint unsigned,
	resolution_h smallint unsigned,
	size int unsigned,
	uri varchar(2083),
	path varchar(2083),

	primary key(id)
);

-- Create users table
CREATE TABLE users (
	id SMALLINT UNSIGNED NOT NULL auto_increment,

	username VARCHAR(255) NOT NULL,
	password_hash VARCHAR(128) NOT NULL,

	PRIMARY KEY (id)
);
