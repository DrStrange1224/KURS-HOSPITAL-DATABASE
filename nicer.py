niceTableNames = {
    "visits" : "Посещения",
    "diagnosis" : "Диагнозы",
    "hospitalizations" : "Госпитализации",
    "hospitals" : "Больницы",
    "departments" : "Отделения",
    "doctors" : "Доктора",
    "specs" : "Специализации",
    "medical_books" : "Медицинские книги",
    "clients" : "Клиенты",
}

niceTableHeaders = {
    "visits":{
        "id" : "ID",
        "data_start" : "Дата начала",
        "data_end" : "Дата конца",
        "client_id" : "ID клиента",
        "doctor_id" : "ID доктора",
        "cabinet_num" : "Номер кабинета",
        "hospital_id" : "ID больницы",
        "department_id" : "ID отделения",
        "hospitalization_id" : "ID госпитализации",
        "final_diagnosis_id" : "ID итогового диагноза",
    },
    "diagnosis":{
        "id" : "ID диагноза",
        "name" : "Название диагноза",
        "heal_method" : "Метод лечения",
        "data" : "Дата диагноза",
    },
    "hospitalizations":{
        "id" : "ID госпитализации",
        "client_id" : "ID клиента",
        "cabinet_num" : "Номер кабинета госпитализации",
        "data_start" : "Дата начала госпитализации",
        "data_end" : "Дата выписки",
        "descrip" : "Доп. описание",
    },
    "hospitals":{
        "id" : "ID больницы",
        "name" : "Название больницы",
        "inn" : "ИНН организации",
        "address" : "Адрес",
    },
    "departments":{
        "id" : "ID отделения",
        "hospital_id" : "ID больницы",
        "name" : "Название отделения",
        "boss_id" : "ID заведующего",
    },
    "doctors":{
        "id" : "ID доктора",
        "full_name" : "ФИО",
        "age" : "Возраст",
        "hospital_id" : "ID больницы",
        "department_id" : "ID отделения",
        "inn" : "ИНН",
        "spec_id" : "ID специальности"
    },
    "specs":{
        "id" : "ID специальности",
        "name" : "Название специальности",
    },
    "medical_books":{
        "id" : "ID мед книжки",
        "diagnosis_array" : "ID диагнозов",
    },
    "clients":{
        "id" : "ID клиента",
        "full_name" : "ФИО",
        "age" : "Возраст",
        "inn" : "ИНН",
        "medical_book_id" : "ID мед книжки"
    }
}