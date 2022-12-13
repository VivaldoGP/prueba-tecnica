--Inser to companies tables

COPY companies(company_id, company_name)
FROM 'C:\Users\Public\data_prueba_tecnica_companies.csv'
DELIMITER ','
CSV HEADER;

COPY charges(id_charge, amount, status, created_at, paid_at)
FROM 'C:\Users\Public\data_prueba_tecnica_charges.csv'
DELIMITER ','
CSV HEADER;

COPY charges_company(id_charge, company_id, company_name)
FROM 'C:\Users\Public\data_prueba_tecnica_charges_company.csv'
DELIMITER ','
CSV HEADER;