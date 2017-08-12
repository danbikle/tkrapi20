--
-- cr_tkrapi.sql
--

-- This script should create both a role named tkrapi and db named tkrapi.
-- Then I should be able to connect via python-sqlalchemy using this string:
-- db_s = 'postgres://tkrapi:tkrapi@127.0.0.1/tkrapi'

-- Demo:
-- sudo su - postgres
-- psql -f cr_tkrapi.sql

create role tkrapi with login superuser password 'tkrapi';
create database tkrapi;

