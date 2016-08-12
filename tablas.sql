BEGIN;
# Creacion de tablas para Sqlite3
CREATE TABLE temperatura (fecha DATE, hora TIME, medidad NUMERIC);
CREATE TABLE humedadT (fecha DATE, hora TIME, medida NUMERIC);
CREATE TABLE humedadS (fecha DATE, hora TIME, medidad NUMERIC);

#Para visualizar los datos select * from nombreTabla;
#Para borrar unos datos de la tabla delete from nombreTabla where atributo=

#Para ver las tablas que tengo .schema
COMMIT;
