insert into hospitals(id, name, inn, address) values
	(1, 'Больница №1', '685324104020', 'г. А, ул. Б, д. 1');

insert into departments(id, hospital_id, name) values
	(1, 1, 'Хирургическое'),
	(2, 1, 'Терапевтическое'),
	(3, 1, 'Реанимационное');

insert into specs(id, name) values
	(1, 'Врач-педиатр'),
	(2, 'Врач-хирург'),
	(3, 'Врач-стоматолог'),
	(4, 'Врач-психиатр'),
	(5, 'Врач-дерматолог');

insert into doctors(id, full_name, age, hospital_id, department_id, inn, spec_id) values
	(1, 'Федотова Олеся Георгиевна', 43, 1, 2, '603259763795', 1),
	(2, 'Максимов Мирон Ильич', 38, 1, 3, '336870962834', 4),
	(3, 'Сахарова София Дмитриевна', 54, 1, 2, '217479281479', 1),
	(4, 'Шишкин Артём Алексеевич', 29, 1, 1, '358436272279', 2),
	(5, 'Кочеткова Анна Ильинична', 40, 1, 3, '537651544743', 5),
	(6, 'Степанова Эмилия Артуровна', 41, 1, 2, '423974506812', 1),
	(7, 'Зотова Таисия Андреевна', 39, 1, 3, '754462771550', 5);

insert into diagnosis(id, name, heal_method, data) values
	(0, 'Отсутствие', 'Нет необходимости', '0001-01-01 00:00:00');

insert into hospitalizations(id, client_id, cabinet_num, data_start, data_end) values
	(0, 0, 0, '0001-01-01 00:00:00', '0001-01-01 00:00:00');

insert into medical_books(id, diagnosis_array) values
	(1, '{0}'::integer[]),
	(2, '{0}'::integer[]),
	(3, '{0}'::integer[]),
	(4, '{0}'::integer[]);

insert into clients(id, full_name, age, inn, medical_book_id) values
	(1, 'Васильева Злата Ярославовна', 26, '203833271060', 1),
	(2, 'Гладков Егор Егорович', 34, '694173504290', 2),
	(3, 'Акимов Даниил Степанович', 15, '523754921301', 3),
	(4, 'Ильина Ева Марковна', 58, '777265541266', 4);

insert into visits(id, data_start, data_end, client_id, doctor_id, cabinet_num, hospital_id, department_id, hospitalization_id, final_diagnosis_id) values
	(1, '2025-10-15 10:30:00', '2025-10-15 11:30:00', 3, 5, 233, 1, 3, 0, 0);


