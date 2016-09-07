INSERT INTO users (first_name, last_name, created_at, updated_at) VALUES ("Chris", "Baker", NOW(), NOW());
INSERT INTO users (first_name, last_name, created_at, updated_at) VALUES ("Diana", "Smith", NOW(), NOW());
INSERT INTO users (first_name, last_name, created_at, updated_at) VALUES ("James", "Johnson", NOW(), NOW());
INSERT INTO users (first_name, last_name, created_at, updated_at) VALUES ("Jessica", "Davidson", NOW(), NOW());

INSERT into friendships (user_id, friend_id, created_at, updated_at) VALUES (2, 5, NOW(), NOW());
INSERT into friendships (user_id, friend_id, created_at, updated_at) VALUES (2, 4, NOW(), NOW());
INSERT into friendships (user_id, friend_id, created_at, updated_at) VALUES (2, 1, NOW(), NOW());
INSERT into friendships (user_id, friend_id, created_at, updated_at) VALUES (1, 2, NOW(), NOW());
INSERT into friendships (user_id, friend_id, created_at, updated_at) VALUES (4, 2, NOW(), NOW());
INSERT into friendships (user_id, friend_id, created_at, updated_at) VALUES (5, 2, NOW(), NOW());

SELECT users.first_name, users.last_name, users2.first_name as friend_first_name, users2.last_name as friend_last_name FROM users
LEFT JOIN friendships ON friendships.user_id = users.id
LEFT JOIN users as users2 ON friendships.friend_id = users2.id
ORDER BY users.first_name ASC