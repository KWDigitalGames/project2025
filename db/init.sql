CREATE USER rpgapp_user WITH encrypted password 'password';
CREATE DATABASE rpgapp;
GRANT ALL PRIVILEGES ON DATABASE rpgapp TO rpgapp_user;
grant ALL PRIVILEGES on schema public to rpgapp_user;
ALTER DATABASE rpgapp OWNER TO rpgapp_user;
