create or replace view visits_info as
	select v.data_start,
		v.data_end, 
		c.full_name as client,
		doc.full_name as doctor,
		v.cabinet_num as cabinet,
		h.descrip as hospitalization_info,
		dia.name as diagnosis
	from ((((visits v join clients c on v.client_id = c.id)
		  join doctors doc on v.doctor_id = doc.id)
		  join hospitalizations h on v.hospitalization_id = h.id)
		  join diagnosis dia on v.final_diagnosis_id = dia.id)
	order by v.data_start;

create or replace view hospitalizations_info as
	select h.data_start,
		h.data_end,
		c.full_name as client,
		h.cabinet_num as cabinet,
		h.descrip as description
	from hospitalizations h join clients c on h.client_id = c.id
	order by h.data_start;

create or replace view doctor_info as
	select doc.full_name as name,
		doc.age as age,
		h.name as hospital,
		dep.name as department,
		doc.inn as inn,
		s.name as specialization
	from (((doctors doc join hospitals h on doc.hospital_id = h.id)
		  join departments dep on doc.department_id = dep.id)
		  join specs s on doc.spec_id = s.id)
	order by name;

create or replace view pediaters_cnt as
	select h.name as hospital,
		count(*)
	from ((doctors doc join hospitals h on doc.hospital_id = h.id)
		  join specs s on doc.spec_id = s.id)
	group by hospital, s.name
	having s.name = 'Врач-педиатр'
	order by hospital;
