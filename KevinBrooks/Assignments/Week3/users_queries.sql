use users;

select u.first_name, u.last_name, u2.first_name as 'friend_first_name', u2.last_name as 'friend_last_name' 
from users u 
join friendships f on u.id = f.user_id
join users u2 on f.friend_id = u2.id;