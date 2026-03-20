CREATE TABLE airports (id SERIAL PRIMARY KEY, code VARCHAR(10) UNIQUE, name VARCHAR(255));
CREATE TABLE departments (id SERIAL PRIMARY KEY, airport_id INTEGER, code VARCHAR(50), name VARCHAR(255));
CREATE TABLE roles (id SERIAL PRIMARY KEY, code VARCHAR(50) UNIQUE, name VARCHAR(255));
CREATE TABLE users (id SERIAL PRIMARY KEY, email VARCHAR(255) UNIQUE, password_hash VARCHAR(255), first_name VARCHAR(100), last_name VARCHAR(100), role_id INTEGER);
INSERT INTO airports (code, name) VALUES ('OPO', 'Porto'), ('LIS', 'Lisbon'), ('FAO', 'Faro'), ('FNC', 'Funchal');
INSERT INTO roles (code, name) VALUES ('ADMIN', 'Administrator'), ('USER', 'User');