#!/bin/bash
# Espera o PostgreSQL estar pronto
until nc -z -v -w30 postgres 5432
do
  echo "Aguardando o PostgreSQL iniciar..."
  sleep 1
done
echo "PostgreSQL está disponível. Iniciando o Django..."
exec "$@"
