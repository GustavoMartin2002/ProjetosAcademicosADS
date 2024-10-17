create database MaterialConstrucao;

use MaterialConstrucao;

create table cliente(
ID int not null identity,
nome varchar(30) not null, 
RG int not null,
CPF int not null,
idade smallint default 18,
nascimento int not null,
endereco varchar(100),
telefone int null,
desconto int null,
primary key(ID)
);

create table funcionario(
ID int not null identity,
nome varchar(30) not null,
primary	key(ID)
);

create table produto(
ID int not null identity,
descricao varchar(max) not null,
preco smallmoney not null,
quantidade int null default 1,
primary key(ID)
);

create table compra(
ID int not null identity,
ID_cliente int not null,
ID_funcionario int not null,
data date null default getdate(),
primary key(ID),
constraint fk_cliente_compra foreign key(ID_cliente)
references cliente(ID),
constraint fk_funcionario_compra foreign key(ID_funcionario)
references funcionario(ID)
);

create table compraHasProduto(
ID int not null identity,
ID_compra int not null,
ID_produto int not null,
quantidade int null default 1,
primary key(ID),
constraint fk_chp_compra foreign key(ID_compra)
references compra(ID),
constraint fk_chp_produto foreign key(ID_produto)
references produto(ID)
);

insert into cliente(nome,idade,RG,CPF,nascimento)
values('Gustavo',20,202020,404040,2002);

select*from cliente

insert into funcionario(nome)
values('Pietro');

select*from funcionario

insert into produto
values('Cimento',34.90,2);

select*from produto

insert into compra
values(12,1,getdate());

select*from compra

insert into compraHasProduto
values(1,1,2);

select*from compraHasProduto