CREATE TABLE libraries (
	id INTEGER NOT NULL,
	name TEXT,
	PRIMARY KEY (id)
);

CREATE TABLE entries (
	id INTEGER NOT NULL,
	library INTEGER NOT NULL, --Every entry must have a source
	word TEXT,	--the actual word, eg. teacher
	PRIMARY KEY (id),
	FOREIGN KEY (library) REFERENCES libraries(id)
);

CREATE TABLE meanings (
	id INTEGER NOT NULL,
	entry INTEGER,
	kana TEXT, --phonetic reading
	kanji TEXT,
	morpheneType TEXT, --eg noun, verb, particle
	definition TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY (entry) REFERENCES entries(id)
);

--Relationship between entries and meaning
--entries may have many (or none) meanings
CREATE TABLE entriesHasAMeaning (
	entry INTEGER,
	meaning INTEGER,
	PRIMARY KEY (entry, meaning),
	FOREIGN KEY (entry) REFERENCES entries(id),
	FOREIGN KEY (meaning) REFERENCES meanings(id)
);

--A usage example is either a sentence or phrase
--set phrase NULL if it's a sentence, and vice versa
CREATE TABLE usageExamples (
	id INTEGER NOT NULL,
	expression TEXT,
	meaning TEXT,
	reading TEXT,
	sentence TEXT,
	phrase TEXT,
	PRIMARY KEY (id)
);

--A usage example can have many sources, avoiding duplication
--by having this table.
--This is the 'part of' relationship between library and usageExample
CREATE TABLE usageExampleSource (
	usageExample INTEGER NOT NULL,
	library INTEGER NOT NULL,
	PRIMARY KEY (usageExample, library),
	FOREIGN KEY (usageExample) REFERENCES usageExamples(id), 
	FOREIGN KEY (library) REFERENCES libraries(id)
);

--Relationship between usageExample and Entries
CREATE TABLE usageConsistsOf (
	usageExample INTEGER NOT NULL,
	entry INTEGER,
	position INTEGER,
	wordLength INTEGER,
	PRIMARY KEY (usageExample),
	FOREIGN KEY (usageExample) REFERENCES usageExamples(id),
	FOREIGN KEY (entry) REFERENCES entries(id)
);
	
CREATE TABLE lists (
	id INTEGER NOT NULL,
	name TEXT, 
	listType TEXT,
	PRIMARY KEY (id)
);

--relationship between usageExample and List
CREATE TABLE usageApartOfList (
	id INTEGER NOT NULL,
	toLearn TEXT,
	list INTEGER,
	usageExample INTEGER,
	PRIMARY KEY (id)
);