select ch.id_charge, ch.amount, ch.created_at, chc.id_charge, chc.company_id, chc.company_name
from charges ch
inner join charges_company chc on ch.id_charge=chc.id_charge
where ch.id_charge = '48ba4bdbfb56ceebb32f2bd0263e759be942af3d'