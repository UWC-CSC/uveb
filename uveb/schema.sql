USE uveb;

-- Create c_videos table
CREATE TABLE c_videos (
	id smallint unsigned not null auto_increment,

	title varchar(255) not null,
	description varchar(1024),
	resolution_w smallint unsigned,
	resolution_h smallint unsigned,
	size int unsigned,
	uri varchar(2083),
	path varchar(2083),
	
	constraint pk_c_videos primary key(id)
);
