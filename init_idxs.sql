create index clients_name_idx
	on clients(full_name);
create index visits_date_idx
	on visits(data_start, data_end);
create index doctors_name_idx
	on doctors(full_name);
create index doctors_spec_idx
	on doctors(spec_id);
create index hosp_data_idx
	on hospitalizations(data_start, data_end);