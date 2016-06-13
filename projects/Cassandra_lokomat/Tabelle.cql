use db2;

create table if not exists Patient(
	ID int primary key,
	Surname text,
	name text,
	dateOfBirth text,
	address text,
	telepthon text,
	email text
);

create table if not exists Affect(
	id_health_state int,
	id_observation int,
	primary key(id_health_state, id_observation)
);

create table if not exists Device(
	id int primary key,
	manufacturer text,
	model text
);

create table if not exists Doctor(
	id int primary key,
	name text,
	surname text
);

create table if not exists Evaluate(
	id_doctor int,
	id_health_state int,
	primary key(id_health_state, id_doctor)
);

create table if not exists Health_state(
	id int primary key,
	timestamp int,
	disease_type text,
	disease_degree text
);

create table if not exists Install(
	id_patient int,
	id_device int,
	when text,
	where_ text,
	primary key(id_patient, id_device)
);

create table if not exists Measurement(
	id_parameter int,
	id_device int,
	primary key (id_parameter, id_device)
);

create table if not exists Monitoring(
	id_parameter int,
	id_observation int,
	primary key (id_parameter, id_observation)
);

create table if not exists Observation(
	id int primary key,
	timestamp int,
	value text,
	uom text
);

create table if not exists Parameter(
	id int primary key,
	description text,
	frequency text
);

create table if not exists Related(
	id_patient int,
	id_health_state int,
	primary key(id_patient, id_health_state)
);

create table if not exists Set_(
	id_healt_state int,
	id_therapy int,
	primary key (id_healt_state, id_therapy )
);

create table if not exists therapy(
	id int primary key,
	starting_time int,
	duration int,
	medicine text,
	posology text
);