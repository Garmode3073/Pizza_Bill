-- phpMyAdmin SQL Dump
-- version 4.9.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 24, 2019 at 08:30 AM
-- Server version: 10.4.10-MariaDB
-- PHP Version: 7.3.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `pizza_bill`
--

-- --------------------------------------------------------

--
-- Table structure for table `bill_o`
--

CREATE TABLE `bill_o` (
  `name` varchar(20) DEFAULT NULL,
  `mobile` varchar(10) DEFAULT NULL,
  `p1` int(2) DEFAULT NULL,
  `p2` int(2) DEFAULT NULL,
  `p3` int(2) DEFAULT NULL,
  `p4` int(2) DEFAULT NULL,
  `p5` int(2) DEFAULT NULL,
  `p6` int(2) DEFAULT NULL,
  `p7` int(2) DEFAULT NULL,
  `total` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `bill_o`
--

INSERT INTO `bill_o` (`name`, `mobile`, `p1`, `p2`, `p3`, `p4`, `p5`, `p6`, `p7`, `total`) VALUES
('Gaurav Vijay Garmode', '9665634810', 2, 2, 1, 1, 2, 2, 1, 2277),
('Bhushan', '9156216896', 2, 0, 1, 0, 2, 0, 0, 1483),
('James Howlett', '9191919191', 2, 1, 2, 0, 1, 1, 1, 1949),
('Vaishali Garmode', '9923919089', 1, 3, 1, 1, 1, 1, 2, 1926),
('Peter Parker', '7098765432', 3, 0, 0, 2, 0, 1, 0, 1012),
('Gaurav', '9665634810', 2, 0, 2, 1, 0, 0, 0, 1173),
('Gaurav', '1111111111', 2, 0, 1, 0, 1, 0, 0, 1127);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
