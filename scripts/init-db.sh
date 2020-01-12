#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username postgres <<-EOSQL
    CREATE DATABASE email_sender;
    \c email_sender
    CREATE TABLE emails (
        id serial not null,
        data timestamp not null default current_timestamp,
        assunto varchar(100) not null,
        mensagem varchar(250) not null
    );
EOSQL