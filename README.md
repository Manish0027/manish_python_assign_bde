# manish_return_dep_people
TO retrive no of people working in department    //////

-- FUNCTION: test_sch.manish_return_dep_people()

-- DROP FUNCTION IF EXISTS test_sch.manish_return_dep_people();

CREATE OR REPLACE FUNCTION test_sch.manish_return_dep_people(
	)
    RETURNS void
    LANGUAGE 'sql'
    COST 100
    VOLATILE PARALLEL UNSAFE
AS $BODY$
CREATE OR REPLACE FUNCTION manish_return_dep_people(passed_organisation_id text)
RETURNS text AS
$$
DECLARE
   dep_people text;
BEGIN
   SELECT CONCAT(department,':',SUM(no_people)) into dep_people                   
from test_sch.apollo_org_job_function 
WHERE organization_id=passed_organisation_id and no_people>0
GROUP BY department;
   RETURN dep_people;
END;
$$ LANGUAGE plpgsql;
$BODY$;

ALTER FUNCTION test_sch.manish_return_dep_people()
    OWNER TO postgres;

