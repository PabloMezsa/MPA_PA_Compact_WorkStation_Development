create table profiles_roles(

    id int auto_increment,
    roleProfile varchar(50),
    primary key(id)
    
);

create table users(

    id int auto_increment,
    userName varchar(50),
    name varchar(50),
    lastName varchar(50),
    number varchar(20),
    email varchar(100),
    identification varchar(50),
    profileId int,
    userPassword varchar(255),
    primary key(id),
    foreign key(profileId) references profiles_roles(id)

);