-- Get a list of all the languages, from the language table.
SELECT * FROM language;

-- Get a list of all films joined with their languages – select the following details : film title, description, and language name.
SELECT fi.title, fi.description, la.name AS "Language"
FROM film as fi
JOIN language As la ON fi.language_id = la.language_id
ORDER BY title ASC;
	
-- Get all languages, even if there are no films in those languages – select the following details : film title, description, and language name.
SELECT fi.title, fi.description, la.name AS "Language"
FROM language AS la
LEFT JOIN film as fi ON la.language_id = fi.language_id
ORDER BY fi.title DESC;

-- Create a new table called new_film with the following columns : id, name. Add some new films to the table.
CREATE TABLE new_film (
	id SERIAL PRIMARY KEY,
	name VARCHAR(100) NOT NULL
);

INSERT INTO new_film (name) VALUES
('The Lost Journey'),
('Mystery in the Shadows'),
('Sunset Boulevard Dream'),
('The Enchanted Garden'),
('Whispering Pines'),
('Echoes of the Past'),
('Moonlit Serenade'),
('The Silent Witness'),
('A Tale of Two Cities'),
('Journey to the Unknown'),
('The Hidden Fortress'),
('Whisper of the Wind'),
('Echoes in the Mist'),
('The Forgotten Temple'),
('Chasing the Horizon'),
('The Golden Age'),
('Realm of Shadows'),
('The Crystal Cavern'),
('Voices in the Dark'),
('The Phantom’s Lament'),
('The Eternal Flame'),
('The Hidden Kingdom'),
('Nightfall'),
('The Forbidden Island'),
('Shattered Memories'),
('Rise of the Phoenix'),
('The Last Crusade'),
('Midnight in Paris'),
('Whispers in the Rain'),
('The Scarlet Letter'),
('Echoes of Eternity'),
('Whispering Shadows'),
('The Secret Garden'),
('The Silent Guardian'),
('The Lost Treasure'),
('Mystic Falls'),
('The Haunted Manor'),
('Whisper of the Heart'),
('Echoes in the Valley'),
('The Forgotten City'),
('Chasing Dreams'),
('The Golden Compass'),
('Realm of the Unknown'),
('The Crystal Palace'),
('Voices of the Sea'),
('The Phantom’s Revenge'),
('The Eternal Quest'),
('The Hidden Path'),
('Nightmare Alley'),
('The Forbidden Forest'),
('Shattered Dreams'),
('Rise of the Titans'),
('The Last Stand'),
('Midnight Sun'),
('Whispers of the Night'),
('The Scarlet Pimpernel'),
('Echoes of Destiny'),
('Whispering Echoes'),
('The Secret Passage'),
('The Silent Storm'),
('The Lost Horizon'),
('Mystic River'),
('The Haunted Castle'),
('Whisper of the Trees'),
('Echoes in the Canyon'),
('The Forgotten Kingdom'),
('Chasing Shadows'),
('The Golden Sword'),
('Realm of the Spirits'),
('The Crystal Lake'),
('Voices of the Night'),
('The Phantom’s Curse'),
('The Eternal Journey'),
('The Hidden Realm'),
('Nightshade'),
('The Forbidden Cave'),
('Shattered Worlds'),
('Rise of the Guardians'),
('The Last Voyage'),
('Midnight Riders');

SELECT * FROM new_film;
SELECT * FROM film;
SELECT * FROM language;
SELECT * FROM customer_review;

-- Create a new table called customer_review, which will contain film reviews that customers will make
CREATE TABLE customer_review (
	review_id SERIAL PRIMARY KEY,
	film_id INT NOT NULL,
	language_id INT NOT NULL,
	title VARCHAR(100) NOT NULL,
	score INT CHECK(score BETWEEN 1 AND 10) NOT NULL,
	review_text VARCHAR(250) NOT NULL,
	last_update DATE DEFAULT CURRENT_DATE,
	FOREIGN KEY (film_id) REFERENCES new_film(id) ON DELETE SET NULL
);

-- had to remove the not null from film_id as I got an error when deleting
ALTER TABLE customer_review ALTER COLUMN film_id DROP NOT NULL;

-- Add movie reviews. Make sure you link them to valid objects in the other tables.
INSERT INTO customer_review (film_id, language_id, title, score, review_text) VALUES
(2, 6, 'Terrible Movie, dont watch!', 1, 'Worst film in the universe, advise to save money'),
(52, 3, 'Awesome film!', 9, 'Best film of the year to date!'),
(14, 5, 'Wonderful', 7, 'Really nice film to watch'),
(22, 1, 'Gross!', 2, 'Not for the faint hearted');

-- Delete a film that has a review from the new_film table, what happens to the customer_review table? the film_id column now shows as null
DELETE FROM new_film WHERE id = 22;