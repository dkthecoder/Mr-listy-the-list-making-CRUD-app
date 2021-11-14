--Creates table for Users:
CREATE TABLE `users` (
  `idusers` int NOT NULL AUTO_INCREMENT,
  `username` varchar(45) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(300) NOT NULL,
  PRIMARY KEY (`idusers`),
  UNIQUE KEY `idusers_UNIQUE` (`idusers`),
  UNIQUE KEY `username_UNIQUE` (`username`),
  UNIQUE KEY `email_UNIQUE` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


--Creates table for Lists:
CREATE TABLE `lists` (
  `idlists` int NOT NULL AUTO_INCREMENT,
  `list_name` varchar(45) NOT NULL,
  `userid` int NOT NULL,
  `description` varchar(500) DEFAULT NULL,
  `date_created` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`idlists`),
  UNIQUE KEY `idlists_UNIQUE` (`idlists`),
  KEY `iduser_idx` (`userid`)
) ENGINE=InnoDB AUTO_INCREMENT=113 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


--Creates table for Items:
CREATE TABLE `items` (
  `iditems` int NOT NULL AUTO_INCREMENT,
  `item_name` varchar(500) NOT NULL,
  `list_owner` int NOT NULL,
  `date_created` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`iditems`),
  UNIQUE KEY `iditems_UNIQUE` (`iditems`)
) ENGINE=InnoDB AUTO_INCREMENT=2939 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
