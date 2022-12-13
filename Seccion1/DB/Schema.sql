CREATE TABLE IF NOT EXISTS companies (
    company_id VARCHAR(45) PRIMARY KEY NOT NULL,
    company_name VARCHAR(15) UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS charges (
    id_charge VARCHAR(45) PRIMARY KEY NOT NULL,
    amount DECIMAL(40,2) NOT NULL,
    status VARCHAR(30) NOT NULL,
    created_at DATE NOT NULL,
    paid_at DATE
);

CREATE TABLE IF NOT EXISTS charges_company (
    id_charge VARCHAR(45) PRIMARY KEY NOT NULL,
    company_id VARCHAR(45),
    company_name VARCHAR(15)
);

ALTER TABLE charges_company
ADD CONSTRAINT fk_charges_company_id
FOREIGN KEY (company_id)
REFERENCES companies (company_id)
ON DELETE CASCADE;

ALTER TABLE charges_company
ADD CONSTRAINT fk_charges_company_name
FOREIGN KEY (company_name)
REFERENCES companies (company_name)
ON DELETE CASCADE;

ALTER TABLE charges_company
ADD CONSTRAINT fk_id_charges_company
FOREIGN KEY (id_charge)
REFERENCES charges (id_charge)
ON DELETE CASCADE;