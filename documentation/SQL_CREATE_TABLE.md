# SQL CREATE TABLE -lauseet

```
CREATE TABLE role (
	id INTEGER NOT NULL, 
	name VARCHAR(5) NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE item (
	id INTEGER NOT NULL, 
	name VARCHAR(64) NOT NULL, 
	volume INTEGER, 
	PRIMARY KEY (id), 
	UNIQUE (name)
);
CREATE TABLE warehouse (
	id INTEGER NOT NULL, 
	name VARCHAR(32) NOT NULL, 
	volume INTEGER, 
	PRIMARY KEY (id), 
	UNIQUE (name)
);
CREATE TABLE account (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(32) NOT NULL, 
	username VARCHAR(32) NOT NULL, 
	password VARCHAR(32) NOT NULL, 
	role_id INTEGER, 
	PRIMARY KEY (id), 
	UNIQUE (username), 
	FOREIGN KEY(role_id) REFERENCES role (id)
);
CREATE TABLE warehouse_item (
	warehouse_id INTEGER NOT NULL, 
	item_id INTEGER NOT NULL, 
	amount INTEGER, 
	PRIMARY KEY (warehouse_id, item_id), 
	FOREIGN KEY(warehouse_id) REFERENCES warehouse (id), 
	FOREIGN KEY(item_id) REFERENCES item (id)
);
CREATE TABLE account_warehouse (
	account_id INTEGER NOT NULL, 
	warehouse_id INTEGER NOT NULL, 
	PRIMARY KEY (account_id, warehouse_id), 
	FOREIGN KEY(account_id) REFERENCES account (id), 
	FOREIGN KEY(warehouse_id) REFERENCES warehouse (id)
);
```
