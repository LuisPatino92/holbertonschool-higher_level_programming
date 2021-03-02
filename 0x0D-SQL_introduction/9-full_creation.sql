-- Creates a TABLE named second_table and adds some rows
-- The database name should be especified in the calling of the script

CREATE TABLE IF NOT EXISTS second_table(
	`id` INTEGER,
	`name` VARCHAR(256),
	`score` INTEGER
);

INSERT INTO second_table (`id`, `name`, `score`) VALUES
	(1, "Jhon", 10),
	(2, "Alex", 3),
	(3, "Bob", 14),
	(4, "George", 8);
