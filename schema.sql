--This is a library of UEs imported by the user
--It can include EPWING dictionaries, Anki Decks,
--Sentence corpuses, etc.
CREATE TABLE Libraries (
	id INTEGER NOT NULL,
	name TEXT NOT NULL UNIQUE,
    type INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY (type) REFERENCES LibraryTypes(id)
);

CREATE TABLE LibraryTypes (
	id INTEGER NOT NULL,
	type TEXT NOT NULL UNIQUE,
	PRIMARY KEY (id)
);

CREATE TABLE Entries (
	id INTEGER NOT NULL,
    library INTEGER NOT NULL,
    number INTEGER,
    kana INTEGER NOT NULL,
    meaning INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY (library) REFERENCES Libraries(id),
	FOREIGN KEY (meaning) REFERENCES Meanings(id),
	FOREIGN KEY (kana) REFERENCES Morphemes(id)
);

CREATE TABLE EntryHasKanji (
	entry INTEGER NOT NULL,
	kanji INTEGER NOT NULL,
	PRIMARY KEY (entry, kanji),
	FOREIGN KEY (entry) REFERENCES Entries(id),
	FOREIGN KEY (kanji) REFERENCES Morphemes(id)
);

CREATE TABLE Meanings (
	id INTEGER NOT NULL,
	meaning TEXT,
	entry INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY (entry) REFERENCES Entries(id)
);

--A usage example is either a sentence or phrase
--set isSentence 1 if it's a sentence, 0 if phrase
CREATE TABLE UsageExamples (
	id INTEGER NOT NULL,
	expression TEXT NOT NULL,
	meaning TEXT,
	reading TEXT,
	isSentence INTEGER NOT NULL,
	PRIMARY KEY (id)
);

CREATE TABLE MeaningHasUEs (
	usageExample INTEGER NOT NULL,
    meaning INTEGER NOT NULL,
	PRIMARY KEY (usageExample, meaning),
	FOREIGN KEY (meaning) REFERENCES Meanings(id),
	FOREIGN KEY (usageExample) REFERENCES usageExamples(id)
);

--Fill with all possible types of morphemes
CREATE TABLE MorphemeTypes (
	id INTEGER NOT NULL,
	type TEXT NOT NULL UNIQUE,
	PRIMARY KEY (id)
);

CREATE TABLE Morphemes (
	id INTEGER NOT NULL,
	morpheme TEXT,
	morphemeType INTEGER, --might make not null in future
	PRIMARY KEY (id),
	FOREIGN KEY (morphemeType) REFERENCES morphemeTypes(id)
);

CREATE TABLE UEConsistsOf (
	id INTEGER NOT NULL,
	usageExample INTEGER NOT NULL,
	morpheme INTEGER NOT NULL,
	wordLength INTEGER,
	position INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY (usageExample) REFERENCES UsageExamples(id),
	FOREIGN KEY (morpheme) REFERENCES Morphemes(id)
);

--User and System created lists of UEs
CREATE TABLE Lists (
	id INTEGER NOT NULL,
	name TEXT, 
	listType INTEGER NOT NULL, --might change this in the future
	PRIMARY KEY (id),
	FOREIGN KEY (listType) REFERENCES ListTypes(id)
);

CREATE TABLE ListTypes (
	id INTEGER NOT NULL,
	type TEXT, 
	PRIMARY KEY (id)
);

--relationship between usageExample and List
CREATE TABLE UEPartOfList (
	list INTEGER NOT NULL,
	usageExample INTEGER NOT NULL,
	toLearn TEXT, --may link to morpheme in future
	PRIMARY KEY (list, usageExample),
	FOREIGN KEY (usageExample) REFERENCES UsageExamples(id),
	FOREIGN KEY (list) REFERENCES Lists(id)
);
