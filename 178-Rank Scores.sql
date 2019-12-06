# Write your MySQL query statement below
select Score,Rank from
(
select Score,@rank := if(@preScore = Score,@rank + 0,@rank := @rank + 1) as Rank,@preScore := Score
  from Scores,(select @rank := 0,@preScore := NULL) r
  order by Score desc
) r
# select s.Score,r.Rank from Scores s
# join
# (select @rank := @rank + 1 as Rank,a.Score from
# (select Score from Scores
#  group by Score
#  order by Score desc) a,(select @rank := 0) b) r on s.Score = r.Score
#  order by s.Score desc
