CREATE database twittermldata;

use twittermldata;

create table twittermldata.users(
	user_id bigint not null,
    user_id_string varchar(50),
    user_name varchar(50),
    twitter_display_name varchar(15),
    primary key (user_id)
);

create table tweets(
	tweet_id bigint not null,
    tweet_id_string varchar(100),
    tweet_content varchar(280),
    classification varchar(15),
    fk_score int,
    media_id bigint not null,
    hashtags_id bigint not null,
    user_id bigint not null,
    foreign key (user_id) references users(user_id),
    foreign key (tweet_id) references tweet_hashtags(tweet_id)
);

create table tweet_hashtags(
    tweet_id bigint not null,
    hashtags_id bigint not null,
    primary key (tweet_id, hashtags_id)
);