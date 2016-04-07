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
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ;

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
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

CREATE TABLE IF NOT EXISTS relative_data (
  ID int(9) unsigned NOT NULL AUTO_INCREMENT PRIMARY KEY,
  DATA_NAME varchar(50) NOT NULL,
  DATA_MAX_VALUE int(9) unsigned NOT NULL,
  CREATE_TS timestamp NOT NULL 
      DEFAULT CURRENT_TIMESTAMP,
  UPDATE_TS timestamp NULL
      ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

CREATE TABLE IF NOT EXISTS relative_dataset (
  ID int(9) unsigned NOT NULL AUTO_INCREMENT PRIMARY KEY,
  DATASET_NAME varchar(1000) NOT NULL,
  DATASET_URL varchar(3000) NOT NULL,
  DATASET_LASTUPADE bigint(20) NOT NULL,
  CREATE_TS timestamp NOT NULL 
      DEFAULT CURRENT_TIMESTAMP,
  UPDATE_TS timestamp NULL
      ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;


CREATE TABLE IF NOT EXISTS major_dataset (
  ID int(9) unsigned NOT NULL AUTO_INCREMENT PRIMARY KEY,
  NEIGHBOURHOOD_NAME varchar(30) NOT NULL,
  NUM_PLAYGROUNDS int(9) unsigned NOT NULL,
  NUM_PUBLIC_SCHOOLS int(9) unsigned NOT NULL,
  NUM_CATHOLIC_SCHOOLS int(9) unsigned NOT NULL,
  NUM_SINGLE int(9) unsigned NOT NULL,
  NUM_DUPLEX int(9) unsigned NOT NULL,
  NUM_ROW_HOUSE int(9) unsigned NOT NULL,
  NUM_APARTMENT_FIVE int(9) unsigned NOT NULL,
  NUM_APARTMENT_FOUR int(9) unsigned NOT NULL,
  NUM_HOTEL int(9) unsigned NOT NULL,
  NUM_AGE_FOURTEEN   int(9) unsigned NOT NULL,
  NUM_AGE_THIRTYFIVE   int(9) unsigned NOT NULL,
  NUM_AGE_SIXTY  int(9) unsigned NOT NULL,
  NUM_AGE_SIXTYPLUS   int(9) unsigned NOT NULL,
  NUM_EMPLOYMENT_STUDENT   int(9) unsigned NOT NULL,
  NUM_EMPLOYMENT_UNEMPLOYED   int(9) unsigned NOT NULL,
  NUM_EMPLOYMENT_EMPLOYED   int(9) unsigned NOT NULL,
  CREATE_TS timestamp NOT NULL 
      DEFAULT CURRENT_TIMESTAMP,
  UPDATE_TS timestamp NULL
      ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

CREATE TABLE IF NOT EXISTS user_query (
  ID int(9) unsigned NOT NULL AUTO_INCREMENT PRIMARY KEY,
  NUM_PLAYGROUNDS int  NOT NULL,
  NUM_PUBLIC_SCHOOLS int  NOT NULL,
  NUM_CATHOLIC_SCHOOLS int  NOT NULL,
  NUM_SINGLE int NOT NULL,
  NUM_DUPLEX int NOT NULL,
  NUM_ROW_HOUSE int NOT NULL,
  NUM_APARTMENT_FIVE int NOT NULL,
  NUM_APARTMENT_FOUR int NOT NULL,
  NUM_HOTEL int NOT NULL,
  NUM_AGE_FOURTEEN   int  NOT NULL,
  NUM_AGE_THIRTYFIVE   int  NOT NULL,
  NUM_AGE_SIXTY  int  NOT NULL,
  NUM_AGE_SIXTYPLUS   int  NOT NULL,
  NUM_EMPLOYMENT_STUDENT   int  NOT NULL,
  NUM_EMPLOYMENT_UNEMPLOYED   int  NOT NULL,
  NUM_EMPLOYMENT_EMPLOYED   int  NOT NULL,
  CREATE_TS timestamp NOT NULL 
      DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

CREATE TABLE IF NOT EXISTS neighbourhood_tmp (
  NEIGHBOURHOOD_NAME varchar(80)  NOT NULL PRIMARY KEY,
  NEIGHBOURHOOD_AREA varchar(100000),
  NEIGHBOURHOOD_LATI float(30)  ,
  NEIGHBOURHOOD_LONG float(30) 
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ;

CREATE TABLE IF NOT EXISTS daily_query (
  ID int(9) unsigned NOT NULL AUTO_INCREMENT PRIMARY KEY,
  NUM_PLAYGROUNDS int(9)  NOT NULL,
  NUM_PUBLIC_SCHOOLS int(9)  NOT NULL,
  NUM_CATHOLIC_SCHOOLS int(9)  NOT NULL,
  NUM_SINGLE int(9) NOT NULL,
  NUM_DUPLEX int(9) NOT NULL,
  NUM_ROW_HOUSE int(9) NOT NULL,
  NUM_APARTMENT_FIVE int(9) NOT NULL,
  NUM_APARTMENT_FOUR int(9) NOT NULL,
  NUM_HOTEL int(9) NOT NULL,
  NUM_AGE_FOURTEEN   int(9)  NOT NULL,
  NUM_AGE_THIRTYFIVE   int(9)  NOT NULL,
  NUM_AGE_SIXTY  int(9)  NOT NULL,
  NUM_AGE_SIXTYPLUS   int(9)  NOT NULL,
  NUM_EMPLOYMENT_STUDENT   int(9)  NOT NULL,
  NUM_EMPLOYMENT_UNEMPLOYED   int(9)  NOT NULL,
  NUM_EMPLOYMENT_EMPLOYED   int(9)  NOT NULL,
  CREATE_TS timestamp NOT NULL 
      DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

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
