--This is a library of UEs imported by the user
--It can include EPWING dictionaries, Anki Decks,
--Sentence corpuses, etc.
CREATE TABLE Libraries (
	id INTEGER NOT NULL,
	name TEXT NOT NULL UNIQUE,
	PRIMARY KEY (id)
);

--Represents a 'word' which is contained in a Library.
--If imported from a Dictionary-type library (rather than a
--list of sentences), there may be meanings attached to it.
CREATE TABLE Entries (
	id INTEGER NOT NULL,
	library INTEGER NOT NULL, --Every entry must have a source
	word TEXT NOT NULL,	--the actual word, eg. teacher
	PRIMARY KEY (id),
	FOREIGN KEY (library) REFERENCES Libraries(id)
);

--One of the dictionary meanings of a single word (entry).
--Corresponds to an entry that comes from a Library
CREATE TABLE Meanings (
	id INTEGER NOT NULL,
	kana TEXT, --phonetic reading
	morphemeType TEXT, --eg noun, verb, particle
	definition TEXT,
	PRIMARY KEY (id)
);


-- An entry can have many different kanji
CREATE TABLE HasKanji (
	id INTEGER NOT NULL,
	entry INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY (entry) REFERENCES Entries(id)
);


--Relationship between entries and meaning
--Entries may have many (or none) meanings
CREATE TABLE EntriesHasAMeaning (
	entry INTEGER,
	meaning INTEGER,
	PRIMARY KEY (entry, meaning),
	FOREIGN KEY (entry) REFERENCES Entries(id),
	FOREIGN KEY (meaning) REFERENCES Meanings(id)
);

--A usage example is either a sentence or phrase
--set isSentence 1 if it's a sentence, 0 if phrase
CREATE TABLE UsageExamples (
	id INTEGER NOT NULL,
	expression TEXT,
	meaning TEXT,
	reading TEXT,
	isSentence INTEGER NOT NULL,
	meaning INTEGER, --A UE can only have ONE corresponding meaning
	PRIMARY KEY (id),
	FOREIGN KEY (meaning) REFERENCES Meanings(id)
);

--A usage example can have many sources, avoiding duplication
--by having this table.
--This is the 'part of' relationship between and usageExample
--UsageExample must be part of Library not strictly enforced
--CREATE TABLE UESource (
--	usageExample INTEGER NOT NULL,
--	library INTEGER NOT NULL,
--	PRIMARY KEY (usageExample, library),
--	FOREIGN KEY (usageExample) REFERENCES UsageExamples(id), 
--	FOREIGN KEY (library) REFERENCES Libraries(id)
--);

--Relationship between usageExample and Entries
--Usage Examples must consist of Entries not strictly enforced
CREATE TABLE UEConsistsOf (
	usageExample INTEGER NOT NULL,
	entry INTEGER NOT NULL,
	position INTEGER NOT NULL,
	wordLength INTEGER NOT NULL,
	PRIMARY KEY (usageExample, entry),
	FOREIGN KEY (usageExample) REFERENCES UsageExamples(id),
	FOREIGN KEY (entry) REFERENCES Entries(id)
);
	
--User and System created lists of UEs
CREATE TABLE Lists (
	id INTEGER NOT NULL,
	name TEXT, 
	listType TEXT, --might change this in the future
	PRIMARY KEY (id)
);

--relationship between usageExample and List
CREATE TABLE UEPartOfList (
	list INTEGER NOT NULL,
	usageExample INTEGER NOT NULL,
	toLearn TEXT,
	PRIMARY KEY (list, usageExample),
	FOREIGN KEY (usageExample) REFERENCES UsageExamples(id),
	FOREIGN KEY (list) REFERENCES Lists(id)
);
