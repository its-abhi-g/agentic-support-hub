CREATE DATABASE IF NOT EXISTS supporthub;

USE supporthub;

CREATE TABLE cases (
    id INT PRIMARY KEY AUTO_INCREMENT,
    case_id VARCHAR(50),
    product VARCHAR(100),
    category VARCHAR(100),
    status VARCHAR(50),
    question TEXT,
    response LONGTEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE knowledge (
    id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(255),
    product VARCHAR(100),
    content LONGTEXT,
    embedding LONGTEXT
);

CREATE TABLE escalations (
    id INT PRIMARY KEY AUTO_INCREMENT,
    case_id VARCHAR(50),
    reason TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);