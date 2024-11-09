# Facebook Data Analysis Report

## Introduction

This report details the creation and population of a Facebook-like database schema, including users, posts, comments, and friendships. It also includes SQL queries executed to retrieve specific data, alongside performance metrics for each query.

## Tables Created

### 1. Users Table
- **Purpose:** To store user profiles, including personal information such as name, email, and age.
- **Structure:**
    - `user_id` (INT): Primary key, auto-incremented identifier for each user.
    - `name` (VARCHAR): The name of the user.
    - `email` (VARCHAR): The email address of the user.
    - `age` (INT): The age of the user.

### 2. Posts Table
- **Purpose:** To store posts created by users, including content and timestamps.
- **Structure:**
    - `post_id` (INT): Primary key, auto-incremented identifier for each post.
    - `user_id` (INT): Foreign key referencing the user who created the post.
    - `content` (TEXT): The content of the post.
    - `created_at` (TIMESTAMP): Timestamp of when the post was created.

### 3. Comments Table
- **Purpose:** To store comments made on posts, linking them back to both the user and the post.
- **Structure:**
    - `comment_id` (INT): Primary key, auto-incremented identifier for each comment.
    - `post_id` (INT): Foreign key referencing the post being commented on.
    - `user_id` (INT): Foreign key referencing the user who made the comment.
    - `content` (TEXT): The content of the comment.
    - `created_at` (TIMESTAMP): Timestamp of when the comment was made.

### 4. Friendships Table
- **Purpose:** To store friendships between users, allowing for social connections in the platform.
- **Structure:**
    - `user1_id` (INT): Foreign key referencing the first user in the friendship.
    - `user2_id` (INT): Foreign key referencing the second user in the friendship.
    - Primary key composed of `(user1_id, user2_id)`.

## SQL Queries and Performance

### Query 1: Users Older Than 30
```sql
SELECT * FROM users WHERE age > 30;
```
- **Purpose:** To retrieve all users older than 30 years.
- **Execution Time for 1000 records:** 0.0049 seconds
- **Execution Time for 10000 records:** 0.0072 seconds
- **Execution Time for 100000 records:** 0.0655 seconds
- **Execution Time for 1000000 records:** 0.6422 seconds

### Query 2: Posts Containing 'post'
```sql
SELECT * FROM posts WHERE content LIKE '%post%';
```
- **Purpose:** To retrieve all posts that contain the word 'post'.
- **Execution Time for 1000 records:** 0.0016 seconds
- **Execution Time for 10000 records:** 0.0131 seconds
- **Execution Time for 100000 records:** 0.1119 seconds
- **Execution Time for 1000000 records:** 1.2394 seconds

### Query 3: Users and Their Posts
```sql
SELECT u.name, p.content 
FROM users u
JOIN posts p ON u.user_id = p.user_id
WHERE u.age > 30;
```
- **Purpose:** To retrieve the names and posts of users older than 30.
- **Execution Time for 1000 records:** 0.0014 seconds
- **Execution Time for 10000 records:** 0.0142 seconds
- **Execution Time for 100000 records:** 0.1415 seconds
- **Execution Time for 1000000 records:** 3.3855 seconds

### Query 4: Users, Their Posts, and Comments
```sql
SELECT u.name, p.content, c.content AS comment_content 
FROM users u
JOIN posts p ON u.user_id = p.user_id
JOIN comments c ON p.post_id = c.post_id
WHERE u.age > 30;
```
- **Purpose:** To retrieve user names, their posts, and the associated comments for users older than 30.
- **Execution Time for 1000 records:** 0.0020 seconds
- **Execution Time for 10000 records:** 0.0250 seconds
- **Execution Time for 100000 records:** 0.2947 seconds
- **Execution Time for 1000000 records:** 12.0672 seconds

## Conclusion

This report outlines the successful creation and population of tables simulating a Facebook-like platform. The SQL queries provided demonstrate the ability to extract meaningful data from the database, with performance metrics indicating response times across varying data sizes. Further analysis and query optimization may be conducted to improve performance as the dataset grows.