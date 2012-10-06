--This is a library of UEs imported by the user
--It can include EPWING dictionaries, Anki Decks,
--Sentence corpuses, etc.
CREATE TABLE Libraries (
	id INTEGER NOT NULL,
	name TEXT NOT NULL UNIQUE,
	PRIMARY KEY (id)
);

CREATE TABLE Entries (
	id INTEGER NOT NULL,
	word TEXT,
	PRIMARY KEY (id)
);

--A usage example is either a sentence or phrase
--set isSentence 1 if it's a sentence, 0 if phrase
CREATE TABLE UsageExamples (
	id INTEGER NOT NULL,
	expression TEXT,
	reading TEXT,
	isSentence INTEGER NOT NULL,
	PRIMARY KEY (id)
);

CREATE TABLE UEHasMeanings (
	id INTEGER NOT NULL,
	usageExample INTEGER,
	entry INTEGER, --The corresponding entry
	meaning INTEGER, --A UE can only have ONE corresponding meaning
					 --or the value can be null
	PRIMARY KEY (id),
	FOREIGN KEY (entry) REFERENCES Entries(id),
	FOREIGN KEY (usageExample) REFERENCES usageExamples(id)
);

--Fill with all possible types of morphemes
--eg 1 = noun
--   2 = verb
--   3 = particle
CREATE TABLE MorphemeTypes (
	id INTEGER NOT NULL,
	types TEXT NOT NULL UNIQUE,
	PRIMARY KEY (id)
);

CREATE TABLE Morpheme (
	id INTEGER NOT NULL,
	morpheme TEXT,
	morphemeType INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY (morphemeType) REFERENCES morphemeTypes(id)
);

CREATE TABLE EntryHasMorphemes (
	id INTEGER NOT NULL,
	kana TEXT,
	kanji TEXT,
	entry INTEGER,
	morpheme INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY (entry) REFERENCES Entries(id),
	FOREIGN KEY (morpheme) REFERENCES Morphemes(id)
);

CREATE TABLE UEConsistsOf (
	id INTEGER NOT NULL,
	usageExample INTEGER NOT NULL,
	wordLength INTEGER,
	position INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY (usageExample) REFERENCES UsageExamples(id)
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