CREATE TABLE account_info (
    id  INT PRIMARY KEY,
    phone_number INT,
    age INT,
    sex VARCHAR(50)
    birthday INT
);

ALTER TABLE account_info ADD COLUMN emails VARCHAR(50);

SELECT * FROM account_info;