# Write your MySQL query statement below
# 方法1
DELETE p1 FROM Person p1,
    Person p2
WHERE
    p1.Email = p2.Email AND p1.Id > p2.Id

# 方法2
#delete from Person
# where id not in(
#     select id from(
#         select min(id) as id
#         from Person
#         group by Email
#     ) as tmp
# )