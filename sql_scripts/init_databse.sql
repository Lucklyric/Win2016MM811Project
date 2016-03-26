DROP DATABASE IF EXISTS mm811project; 
CREATE DATABASE mm811project;
USE mm811project;
CREATE TABLE IF NOT EXISTS app_metadata (
  APP_NAME varchar(30) NOT NULL,
  VERSION float(5,2) NOT NULL,
  CREATE_TS timestamp NOT NULL 
      DEFAULT CURRENT_TIMESTAMP,
  UPDATE_TS timestamp NULL
      ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1 ;

CREATE TABLE IF NOT EXISTS users (
  ID int(9) unsigned NOT NULL AUTO_INCREMENT PRIMARY KEY,
  LAST_NAME varchar(30) NOT NULL,
  FIRST_NAME varchar(30) NOT NULL,
  USER_NAME varchar(30) unique NOT NULL,
  USER_PWD varchar(30) NOT NULL,
  CREATE_TS timestamp NOT NULL 
      DEFAULT CURRENT_TIMESTAMP,
  UPDATE_TS timestamp NULL
      ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

CREATE TABLE IF NOT EXISTS relative_dataset (
  ID int(9) unsigned NOT NULL AUTO_INCREMENT PRIMARY KEY,
  DATASET_NAME varchar(30) NOT NULL,
  DATASET_URL varchar(300) NOT NULL,
  DATASET_LASTUPADE timestamp NOT NULL,
  DATASET_MAX_VALUE int(9) unsigned NOT NULL,
  CREATE_TS timestamp NOT NULL 
      DEFAULT CURRENT_TIMESTAMP,
  UPDATE_TS timestamp NULL
      ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

CREATE TABLE IF NOT EXISTS major_dataset (
  ID int(9) unsigned NOT NULL PRIMARY KEY,
  NEIGHBOURHOOD_NAME varchar(30) NOT NULL,
  NUM_PLAYGROUNDS int(9) unsigned NOT NULL,
  NUM_PUBLIC_SCHOOLS int(9) unsigned NOT NULL,
  NUM_CATHOLIC_SCHOOLS int(9) unsigned NOT NULL,
  NUM_TENNIS_COUNT int(9) unsigned NOT NULL,
  NUM_TREE int(9) unsigned NOT NULL,
  NUM_SINGLE int(9) unsigned NOT NULL,
  NUM_DUPLEX int(9) unsigned NOT NULL,
  NUM_ROW_HOUSE int(9) unsigned NOT NULL,
  NUM_APARTMENT_FIVE int(9) unsigned NOT NULL,
  NUM_APARTMENT_FOUR int(9) unsigned NOT NULL,
  NUM_HOTEL int(9) unsigned NOT NULL,
  CREATE_TS timestamp NOT NULL 
      DEFAULT CURRENT_TIMESTAMP,
  UPDATE_TS timestamp NULL
      ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

CREATE TABLE IF NOT EXISTS user_query (
  ID int(9) unsigned NOT NULL AUTO_INCREMENT PRIMARY KEY,
  NUM_PLAYGROUNDS bool  NOT NULL,
  NUM_PUBLIC_SCHOOLS bool  NOT NULL,
  NUM_CATHOLIC_SCHOOLS bool  NOT NULL,
  NUM_TENNIS_COUNT bool  NOT NULL,
  NUM_TREE bool NOT NULL,
  NUM_SINGLE bool NOT NULL,
  NUM_DUPLEX bool NOT NULL,
  NUM_ROW_HOUSE bool NOT NULL,
  NUM_APARTMENT_FIVE bool NOT NULL,
  NUM_APARTMENT_FOUR bool NOT NULL,
  NUM_HOTEL bool NOT NULL,
  DATASET_LASTUPADE timestamp NOT NULL,
  DATASET_MAX_VALUE int(9) unsigned NOT NULL,
  CREATE_TS timestamp NOT NULL 
      DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

INSERT INTO app_metadata
(APP_NAME, VERSION) 
VALUES 
("MM801 Project", 1.00);

INSERT INTO users
(LAST_NAME,FIRST_NAME,USER_NAME,USER_PWD)
VALUES 
("Sun","Alvin","admin1","admin");
INSERT INTO users
(LAST_NAME,FIRST_NAME,USER_NAME,USER_PWD)
VALUES 
("Li","Hongzu","admin2","admin");

