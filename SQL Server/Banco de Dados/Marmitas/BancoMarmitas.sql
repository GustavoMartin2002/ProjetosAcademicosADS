create database BancoMarmitas;

use BancoMarmitas;

create table login(
id int not null identity,
email varchar(max) null,
senha varchar(max) not null,
nivel_acesso int not null,
primary key(id)
);

create table empresa(
id int not null identity,
nome varchar(max) not null,
cnpj varchar(max) null,
email varchar(max) null,
telefone varchar(max) not null,
endereco varchar (max) not null,
primary key(id)
);

create table cliente(
telefone int not null,
nome varchar(max) not null,
endereco varchar(max) not null,
pontoReferencia varchar(max) null,
nascimento date null,
primary key(telefone)
);

create table marmita(
id int not null identity,
nome varchar(max) not null,
descricao text null,
tamanho varchar(max) not null,
valor varchar(max) not null,
primary key(id)
);

create table entregador(
id int not null identity,
id_empresa int not null,
nome varchar(max) not null,
cpf varchar(max) null,
rg varchar (max) null,
celular varchar(max) not null,
primary key(id),
constraint fk_empresa_entregador foreign key(id_empresa)
references empresa(id)
);

create table pedido(
id int not null identity,
id_entregador int not null,
telefone_cliente int not null,
status varchar(max) null,
taxa_entrega varchar(max) not null,
data datetime null default getdate(),
primary key(id),
constraint fk_entregador_pedido foreign key(id_entregador)
references entregador(id),
constraint fk_telefone_cliente foreign key(telefone_cliente)
references cliente(telefone)
);

create table item_pedido(
id_marmita int not null,
id_pedido int not null,
quantidade int null default 1
constraint fk_ip_marmita foreign key(id_marmita)
references marmita(id),
constraint fk_ip_pedido foreign key(id_pedido)
references pedido(id)
);

--LOGIN
insert into login(email,senha,nivel_acesso)
values('gustavo@gmail.com','senha',2020);

update login
set senha = '13456'
where nivel_acesso = 2020;

select*from login

delete from login


--EMPRESA
insert into empresa(nome,telefone,endereco)
values('empresa','71900000000','endereco');

update empresa
set endereco = 'stiep'
where nome = 'empresa';

select*from empresa

delete from empresa


--CLIENTE
insert into cliente(telefone,nome,endereco,pontoReferencia,nascimento)
values(719,'Gustavo','endereco','referencia','29-06-2002');

update cliente
set pontoReferencia = 'stiep'
where telefone = 719;

select*from cliente

delete from cliente


--ENTREGADOR
insert into entregador(id_empresa,nome,celular)
values(1,'entregador','719800000000');

update entregador
set celular = '71988888888'
where nome = 'entregador';

select*from entregador

delete from entregador


--PEDIDO
insert into pedido(id_entregador,telefone_cliente,status,taxa_entrega)
values(1,719,'preparando','7.50');

update pedido
set status = 'pronto'
where telefone_cliente = 719

select*from pedido

delete from pedido


--MARMITA
insert into marmita(nome,tamanho,valor)
values('macarrao','grande','25,00');

update marmita
set nome = 'lasanha'
where valor = '25,00'

select*from marmita

delete from marmita


--ITEM_PEDIDO
insert into item_pedido(id_marmita,id_pedido,quantidade)
values(1,1,2);

update item_pedido
set quantidade = 3
where id_marmita = 1 

select*from item_pedido
