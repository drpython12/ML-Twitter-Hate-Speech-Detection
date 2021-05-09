use TwitterMachineLearningDatabase;

create table user(
	user_id bigint,
    user_id_string varchar(50),
    name_of_user varchar(50),
    display_name varchar(15),
    primary key (user_id)
);

create table tweet(
	tweet_id bigint,
    tweet_id_string varchar(100),
    tweet_text varchar(200),
    user_id bigint,
    foreign key (user_id) references user (user_id)
);