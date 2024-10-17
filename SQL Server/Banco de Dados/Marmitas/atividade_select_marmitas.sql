create database AtividadeSelect;

use AtividadeSelect;

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
valor smallmoney not null,
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
taxa_entrega smallmoney not null,
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
quantidade int null default 1,
constraint fk_id_marmita foreign key(id_marmita)
references marmita(id),
constraint fk_id_pedido foreign key(id_pedido)
references pedido(id)
);

--LOGIN
insert into login(email,senha,nivel_acesso)
values('Gustavo@gmail.com','Senha',2023);

select*from login

--EMPRESA
insert into empresa(nome,telefone,endereco)
values('Empresa','71900000000','endereco');

select*from empresa

--CLIENTE
insert into cliente(telefone,nome,endereco,pontoReferencia,nascimento)
values(719,'Gustavo','Stiep','Estacio','29-06-2002');

insert into cliente(telefone,nome,endereco,pontoReferencia,nascimento)
values(7198,'Cliente3','Stiep3','Estacio3','11-03-2000');

insert into cliente(telefone,nome,endereco,pontoReferencia,nascimento)
values(7197,'Cliente2','Stiep2','Estacio2','15-09-1998');

insert into cliente(telefone,nome,endereco,pontoReferencia,nascimento)
values(7199,'Marcio','Stiep4','Estacio4','06-04-1995');

select*from cliente

--ENTREGADOR
insert into entregador(id_empresa,nome,celular)
values(1,'Daniel','71912345678');

insert into entregador(id_empresa,nome,celular)
values(1,'Vitoria','71987654321');

insert into entregador(id_empresa,nome,celular)
values(1,'Pietro','71912312378');

insert into entregador(id_empresa,nome,cpf,celular)
values(1,'Julia','100.200.300-40','71932112345');

select*from entregador

--PEDIDO
insert into pedido(id_entregador,telefone_cliente,status,taxa_entrega)
values(1,719,'Preparando',7.50);

insert into pedido(id_entregador,telefone_cliente,status,taxa_entrega)
values(2,7197,'Preparando',10.00);

insert into pedido(id_entregador,telefone_cliente,status,taxa_entrega)
values(3,7198,'Preparando',15.00);

select*from pedido

--MARMITA
insert into marmita(nome,tamanho,valor)
values('Macarrao','Grande',25.00);

insert into marmita(nome,tamanho,valor)
values('Carne com fritas','Grande',35.00);

insert into marmita(nome,tamanho,valor)
values('Strogonoff','Grande',30.00);

select*from marmita

--ITEM_PEDIDO
insert into item_pedido(id_marmita,id_pedido,quantidade)
values(1,1,2);

insert into item_pedido(id_marmita,id_pedido,quantidade)
values(2,2,1);

insert into item_pedido(id_marmita,id_pedido,quantidade)
values(3,3,1);

select*from item_pedido

--Atividade pontuada SELECTs
--1. Telefone e data dos pedidos, com IDs entre 1 e 4.
select telefone_cliente, data
from pedido
where id between 1 and 4;

--2. Telefone e data dos pedidos cujo a taxa esteja fora da faixa de 15,00 e 20,00 reais.
select telefone_cliente, data
from pedido
where taxa_entrega between 15.00 and 20.00

--3. Nome e endere�o de clientes que come�am com as letras "MAR".
select nome, endereco
from cliente
where nome like 'MAR%';

--4. Nome, CPF e celular dos entregadores com id na lista (1,2,3).
select nome, cpf, celular
from entregador
where id in(1,2,3);

--5. Nome, CPF e celular dos entregadores com id fora da lista(1,2,3).
select nome, cpf, celular
from entregador
where id not in(1,2,3);

--6. ID e nome de entregadores, cujo ID seja 1 e o nome Daniel.
select id, nome
from entregador
where id = 1 and nome = 'Daniel';

--7. ID e nome de entregadores, cujo id seja 1 ou o nome Vitoria.
select id, nome
from entregador
where id = 1 or nome = 'Vitoria';

--8. Qual � a media de taxa_entrega dos pedidos.
--a) Por telefone do cliente?
select cli.telefone,avg(taxa_entrega) as 'Media taxa de entrega dos pedidos:'
from pedido ped
inner join item_pedido it on it.id_pedido = ped.id
inner join marmita mar on mar.id = it.id_pedido
inner join cliente cli on cli.telefone = ped.telefone_cliente
group by cli.telefone;
--b) Por id_entregador?
select id_entregador,avg(taxa_entrega) as 'Media taxa de entrega dos pedidos:'
from pedido ped
inner join item_pedido it on it.id_pedido = ped.id
inner join marmita mar on mar.id = it.id_pedido
inner join cliente cli on cli.telefone = ped.telefone_cliente
group by id_entregador;

--9. Qual � a taxa de entrega mais baixa e mais alta dos pedidos?
select min(taxa_entrega) as 'Taxa mais baixa:'
from pedido;

select max(taxa_entrega) as 'Taxa mais alta:'
from pedido;

--10. Quantos pedidos cada entregador realizou?
select id_entregador,en.nome, count(*) as 'Viajens realizadas:'
from pedido ped
inner join entregador en on en.id = ped.id_entregador
group by id_entregador,en.nome;

--11. Quantos entregadores existem por empresa?
select id_empresa, count(*) as 'Entregadores da empresa:'
from empresa em
inner join entregador en on en.id_empresa = em.id
group by id_empresa;

--12. Qual � a marmita mais cara?
select max(valor) as 'Marmita mais cara:'
from marmita;

--13. Qual � a marmita mais barata?
select min(valor) as 'Marmita mais barata:'
from marmita;

--14. Listar nome do cliente, telefone do cliente, data do pedido, nome da marmita,
--valor da marmita, nome do entregador, taxa da entrega.
select cli.nome as 'Nome do Cliente:', cli.telefone as 'Telefone do Cliente:',
ped.data as 'Data do pedido:', mar.nome as 'Nome do pedido:', mar.valor as 'Valor do pedido:',
en.nome as 'Nome do entregador:', ped.taxa_entrega as 'Taxa da entrega:'
from pedido ped
inner join cliente cli on cli.telefone = ped.telefone_cliente
inner join item_pedido it on ped.id = it.id_pedido 
inner join marmita mar on mar.id = it.id_marmita
inner join entregador en on en.id = ped.id_entregador

--15. Listar o nome do entregador e o total recebido das entregas.
select en.nome as 'Nome do Entregador:', sum(ped.taxa_entrega*it.quantidade) as 'Total recebido:'
from entregador en
inner join pedido ped  on en.id = ped.id_entregador
inner join item_pedido it on ped.id = it.id_pedido
inner join marmita mar on mar.id = it.id_marmita
group by en.nome;

--16. Listar data dos pedidos e o valor total.
select ped.data as 'Data do pedido:', sum(mar.valor*it.quantidade+taxa_entrega) as 'Valor total:'
from pedido ped
inner join item_pedido it on ped.id = it.id_pedido
inner join marmita mar on mar.id = it.id_marmita 
group by ped.data, mar.valor;

--17. Listar o nome e a quantidade da marmita mais vendida.
select top 1 mar.nome, sum(it.quantidade) as 'Marmita Mais Vendida:'
from marmita mar
inner join item_pedido it on mar.id = it.id_marmita
group by mar.nome
order by sum(it.quantidade) desc

--18. Listar a m�dia de todas as marmitas vendidas.
select avg(mar.valor*it.quantidade) as 'Media de Todas Marmitas Vendidas:'
from marmita mar
inner join item_pedido it on mar.id = it.id_marmita

--19. Listar o total pago dos pedidos por cliente.
select sum(mar.valor*it.quantidade+ped.taxa_entrega) as 'Total Pago:', cli.nome as 'Cliente:' 
from cliente cli
inner join pedido ped on cli.telefone = ped.telefone_cliente
inner join item_pedido it on ped.id = it.id_pedido
inner join marmita mar on mar.id = it.id_marmita
group by mar.valor, it.quantidade, ped.taxa_entrega, cli.nome
order by sum(mar.valor*it.quantidade+ped.taxa_entrega) desc

--20. Listar nome do cliente, nome da marmita e o total pago.
select cli.nome as 'Cliente:', mar.nome as 'Marmita:',sum(mar.valor*it.quantidade+ped.taxa_entrega) as 'Total Pago:'
from cliente cli
inner join pedido ped on cli.telefone = ped.telefone_cliente
inner join item_pedido it on ped.id = it.id_pedido
inner join marmita mar on mar.id = it.id_marmita
group by cli.nome, mar.nome, mar.valor, it.quantidade, ped.taxa_entrega
order by sum(mar.valor*it.quantidade+ped.taxa_entrega) desc