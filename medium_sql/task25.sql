--https://www.codewars.com/kata/686cf5d8ebcff30d8b051b06/train/sql
--One House, Many Claims: Detect Duplicate Address Applications
--6 kyu

SELECT
  CONCAT(da.count, 
         ' applications (applicant_ids: ',
         (SELECT STRING_AGG(applicant_id::text, ', ' ORDER BY applicant_id) 
          FROM  energy_rebate_applications 
          WHERE house_no = da.house_no AND street_name = da.street_name
          ),
         ') already filed at ', 
         da.house_no::text, 
         ' ', 
         da.street_name
        ) AS audit_note
FROM
  (
    SELECT
      COUNT(*) as count,
      house_no,
      street_name
    FROM
      energy_rebate_applications
    GROUP BY
      house_no,
      street_name
    HAVING
      COUNT(*) > 1     
  ) da --Duplicate Address
ORDER BY
  da.count DESC, da.street_name, da.house_no  

  
