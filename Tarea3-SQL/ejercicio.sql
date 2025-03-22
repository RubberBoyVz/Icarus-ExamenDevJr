create table Usuarios(
    id int primary key,
    nombre varchar(50) not null,
    email varchar(50) not null,
    fecha_de_registro timestamp not null default current_timestamp
);

insert into Usuarios(nombre,email) values
("Humberto Vazquez","humberto@correo.com"), 
("Jose Perez","jose@correo.com"), 
("Juan Martinez","juan@correo.com");