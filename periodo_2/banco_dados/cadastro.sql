create database cadastro
default character set utf8
default collate utf8_general_ci;

create table pessoas(
id int not null auto_increment,
nome varchar(30) not null,
nascimento date,
sexo enum ('M', 'F'),
peso decimal(5,2),
altura decimal(3,2), 
nacionalidade varchar(20) default 'Brasil',
primary key(id)
)default charset = utf8;

insert into pessoas
(nome, nascimento, sexo, peso, altura, nacionalidade)
values
('Godofredo', '1984-01-02', 'M', '78.6', '1.83', 'Brasil');
('Pedro', '2001-08-18', 'M', '65.0', '1.82', 'Brasil'),
('Creuza', '1985-08-18', 'F', '80.0', '1.32', 'Holanda'),


select * from pessoas;
