create database TwitterMachineLearningDatabase;

use TwitterMachineLearningDatabase;

create table User(
	user_id bigint not null,
    user_id_string varchar(255) not null,
    name_of_user varchar(50),
    display_name varchar(15),
    primary key (user_id)
);

create table Tweet(
	tweet_id bigint not null,
    tweet_id_string text not null,
    tweet_text varchar(200) not null,
    user_id bigint not null,
    foreign key (user_id) references User(user_id),
    primary key (tweet_id)
);

create table TweetEntities(
	tweet_id bigint not null,
    created_at text not null,
    in_reply_to_user_id bigint,
    in_reply_to_user_id_string varchar(50),
    in_reply_to_screen_name varchar(50),
    country tinytext default null,
    country_code char(2) default null,
    city_state text default null,
    favourite_count int,
    retweet_count int,
    withheld_in json,
    foreign key (tweet_id) references Tweet(tweet_id)
);

create table TweetAnalysis(
	tweet_id bigint not null,
    fk_score double,
    tfidf_score double,
    tokens json,
    foreign key (tweet_id) references Tweet(tweet_id)
);