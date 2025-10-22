create table if not exists hospitals(
	id serial primary key,
	name varchar not null,
	inn varchar(12) not null unique check(length(inn) = 12),
	address varchar not null
);

create table if not exists departments(
	id serial primary key,
	hospital_id int not null references hospitals(id) on delete cascade,
	name varchar not null,
	boss_id int,
	constraint name_hospital_unique unique(hospital_id, name)
);

create table if not exists specs(
	id serial primary key,
	name varchar not null unique
);

create table if not exists doctors(
	id serial primary key,
	full_name varchar not null,
	age int not null,
	hospital_id int references hospitals(id) on delete set null,
	department_id int references departments(id) on delete set null,
	inn varchar(12) not null unique check(length(inn) = 12),
	spec_id int not null references specs(id) on delete set null
);

alter table departments
	drop constraint if exists foreign_boss_id,
	add constraint foreign_boss_id foreign key (boss_id) references doctors(id);
	
create table if not exists medical_books(
	id serial primary key,
	diagnosis_array integer[] not null default '{0}'::int[]
);

create table if not exists clients(
	id serial primary key,
	full_name varchar not null,
	age int not null,
	inn varchar(12) not null unique check(length(inn) = 12),
	medical_book_id int references medical_books(id) on delete set null unique
);

create table if not exists diagnosis(
	id serial primary key,
	name varchar not null unique,
	heal_method varchar not null default 'Нет необходимости',
	data timestamp not null default '0001-01-01 00:00:00'
);

create table if not exists hospitalizations(
	id serial primary key,
	client_id int not null,
	cabinet_num int not null,
	data_start timestamp not null default '0001-01-01 00:00:00',
	data_end timestamp not null default '0001-01-01 00:00:00',
	descrip varchar default 'Без описания'
);

create table if not exists visits(
	id serial primary key,
	data_start timestamp not null,
	data_end timestamp not null,
	client_id int not null references clients(id) on delete cascade,
	doctor_id int not null references doctors(id) on delete cascade,
	cabinet_num int not null,
	hospital_id int not null references hospitals(id) on delete cascade,
	department_id int not null references departments(id) on delete cascade,
	hospitalization_id int not null references hospitalizations(id) on delete cascade default 0,
	final_diagnosis_id int not null references diagnosis(id) on delete cascade default 0
);


