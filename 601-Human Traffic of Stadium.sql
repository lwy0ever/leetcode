# Write your MySQL query statement below
SELECT DISTINCT S1.*
FROM stadium AS S1,stadium AS S2,stadium AS S3
WHERE S1.people>=100 AND S2.people>=100 AND S3.people>=100 AND (
	S1.id +1 = S2.id AND S1.id+2=S3.id OR
	S1.id +1 = S2.id AND S1.id-1=S3.id OR
	S1.id -1 = S2.id AND S1.id-2=S3.id
)
ORDER BY S1.id