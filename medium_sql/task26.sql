--best practice

SELECT CONCAT(
  COUNT(*),
  ' applications (applicant_ids: ',
  STRING_AGG(applicant_id::text, ', ' ORDER BY applicant_id),
  ') already filed at ',
  house_no,
  ' ',
  street_name
) audit_note 
FROM energy_rebate_applications
GROUP BY (street_name, house_no)
HAVING COUNT(*) > 1
ORDER BY COUNT(*) DESC, street_name, house_no;