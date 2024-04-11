-- Adminer 4.8.1 MySQL 8.3.0 dump

SET NAMES utf8;
SET time_zone = '+00:00';
SET foreign_key_checks = 0;
SET sql_mode = 'NO_AUTO_VALUE_ON_ZERO';

SET NAMES utf8mb4;

CREATE DATABASE `Cafe_App` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `Cafe_App`;

DROP TABLE IF EXISTS `Couriers`;
CREATE TABLE `Couriers` (
  `Couriers_id` int NOT NULL AUTO_INCREMENT,
  `Couriers_name` varchar(255) NOT NULL,
  `Couriers_number` varchar(255) NOT NULL,
  PRIMARY KEY (`Couriers_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `Couriers` (`Couriers_id`, `Couriers_name`, `Couriers_number`) VALUES
(1,	'FastTrack Couriers',	'1-800-FAST-TRK'),
(2,	'Swift Delivery Services',	'1-888-SWIFT-DEL'),
(3,	'Express Logistics Inc.',	'1-877-EXP-LOGS'),
(4,	'Rapid Dispatch Solutions',	'1-855-RAPID-DS'),
(5,	'Speedy Shipments LLC',	'1-844-SPEEDY-SHIP');

DROP TABLE IF EXISTS `Order_status`;
CREATE TABLE `Order_status` (
  `Order_status_id` int NOT NULL AUTO_INCREMENT,
  `order_status` varchar(255) NOT NULL,
  PRIMARY KEY (`Order_status_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `Order_status` (`Order_status_id`, `order_status`) VALUES
(1,	'PREPARING'),
(2,	'SHIPPED'),
(3,	'DELIVERED'),
(4,	'CANCELLED');

DROP TABLE IF EXISTS `Orders`;
CREATE TABLE `Orders` (
  `Order_id` int NOT NULL AUTO_INCREMENT,
  `Customer_name` varchar(255) NOT NULL,
  `Customer_address` varchar(255) NOT NULL,
  `Customer_phone` varchar(255) NOT NULL,
  `Couriers_id` int DEFAULT NULL,
  `Order_status_id` int DEFAULT NULL,
  `Product_id` int DEFAULT NULL,
  PRIMARY KEY (`Order_id`),
  KEY `Couriers_id` (`Couriers_id`),
  KEY `Order_status_id` (`Order_status_id`),
  KEY `Product_id` (`Product_id`),
  CONSTRAINT `Orders_ibfk_1` FOREIGN KEY (`Couriers_id`) REFERENCES `Couriers` (`Couriers_id`),
  CONSTRAINT `Orders_ibfk_2` FOREIGN KEY (`Order_status_id`) REFERENCES `Order_status` (`Order_status_id`),
  CONSTRAINT `Orders_ibfk_3` FOREIGN KEY (`Product_id`) REFERENCES `Products` (`Product_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `Orders` (`Order_id`, `Customer_name`, `Customer_address`, `Customer_phone`, `Couriers_id`, `Order_status_id`, `Product_id`) VALUES
(1,	'John Smith',	'123 Main Street, London, SW1A 1AA',	'020 1234 XXXX',	1,	1,	1),
(2,	'Emily Johnson',	'456 Elm Avenue, Manchester, M1 1AA',	'0161 234 XXXX',	1,	1,	1),
(3,	'David Brown',	'789 Oak Lane, Birmingham, B1 1AA',	'0121 345 XXXX',	1,	1,	1),
(4,	'Sarah Taylor',	'101 Maple Street, Leeds, LS1 1AA',	'0113 456 XXXX',	1,	1,	1),
(5,	'Michael Wilson',	'202 Pine Road, Liverpool, L1 1AA',	'0151 567 XXXX',	1,	1,	1),
(6,	'Jessica Martinez',	'303 Cedar Court, Bristol, BS1 1AA',	'0117 678 XXXX',	1,	1,	1),
(7,	'Christopher Anderson',	'404 Birch Drive, Glasgow, G1 1AA',	'0141 789 XXXX',	1,	1,	1),
(8,	'Amanda Thompson',	'505 Walnut Circle, Edinburgh, EH1 1AA',	'0131 890 XXXX',	1,	1,	1),
(9,	'Daniel Garcia',	'606 Spruce Street, Cardiff, CF1 1AA',	'029 9012 XXXX',	1,	1,	1),
(10,	'Laura Rodriguez',	'707 Ash Avenue, Belfast, BT1 1AA',	'028 0123 XXXX',	1,	1,	1);

DROP TABLE IF EXISTS `Products`;
CREATE TABLE `Products` (
  `Product_id` int NOT NULL AUTO_INCREMENT,
  `Product_name` varchar(255) NOT NULL,
  `Price` decimal(10,2) NOT NULL,
  PRIMARY KEY (`Product_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `Products` (`Product_id`, `Product_name`, `Price`) VALUES
(1,	'Espresso',	2.00),
(2,	'Cappuccino',	2.40),
(3,	'Latte',	2.80),
(4,	'Mocha',	3.20),
(5,	'Americano',	2.20),
(6,	'Croissant',	1.80),
(7,	'Bagel with Cream Cheese',	2.20),
(8,	'Blueberry Muffin',	2.00),
(9,	'Avocado Toast',	4.00),
(10,	'Fruit Parfait',	3.30),
(11,	'Pespi',	2.50),
(12,	'Hot chocolate',	2.00);

-- 2024-03-12 00:16:46
