create table profiles_roles(

    id int auto_increment,
    roleProfile varchar(50),
    primary key(id)
    
);

create table users(

    id int auto_increment,
    userName varchar(50),
    userPassword varchar(255),
    name varchar(50),
    lastName varchar(50),
    email varchar(100),
    number varchar(20),
    identification varchar(50),
    profileId int,
    primary key(id),
    foreign key(profileId) references profiles_roles(id)

);