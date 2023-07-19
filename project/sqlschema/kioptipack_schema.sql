

CREATE TABLE "Additive" (
	name TEXT, 
	description TEXT, 
	PRIMARY KEY (name, description)
);

CREATE TABLE "Material" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "NamedThing" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	PRIMARY KEY (id)
);
