-- Populating tables
INSERT INTO users (first_name, last_name) Values(Chris, Baker)
INSERT INTO users (first_name, last_name) Values(James, Johnson)
INSERT INTO users (first_name, last_name) Values(Jessica, Davidson)
INSERT INTO users (first_name, last_name) Values(Diana, Smith)
INSERT INTO friendships (user_id, friend_id) Values(1, 2)
INSERT INTO friendships (user_id, friend_id) Values(1, 3)
INSERT INTO friendships (user_id, friend_id) Values(1, 4)
INSERT INTO friendships (user_id, friend_id) Values(4, 1);
INSERT INTO friendships (user_id, friend_id) Values(3, 1);
INSERT INTO friendships (user_id, friend_id) Values(2, 1);

-- Displaying friendships
SELECT 
    users.first_name,
    users.last_name,
    user2.first_name AS friend_first_name,
    user2.last_name AS friend_last_name
FROM
    users
        JOIN
    friendships ON friendships.user_id = users.id
        JOIN
    users AS user2 ON user2.id = friendships.friend_id