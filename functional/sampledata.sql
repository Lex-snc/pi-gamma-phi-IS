-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 02, 2024 at 04:34 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `sampledata`
--

-- --------------------------------------------------------

--
-- Table structure for table `adlogin`
--

CREATE TABLE `adlogin` (
  `admin_id` int(11) NOT NULL,
  `username` varchar(30) NOT NULL,
  `password` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `adlogin`
--

INSERT INTO `adlogin` (`admin_id`, `username`, `password`) VALUES
(1, 'admin', 'admin');

--
-- Triggers `adlogin`
--
DELIMITER $$
CREATE TRIGGER `prevent_delete` BEFORE DELETE ON `adlogin` FOR EACH ROW IF OLD.admin_id = 1 THEN
  SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Cannot delete this record';
END IF
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Table structure for table `archive`
--

CREATE TABLE `archive` (
  `arc_id` int(11) NOT NULL,
  `fname` text NOT NULL,
  `lname` text NOT NULL,
  `position` text NOT NULL,
  `age` int(11) NOT NULL,
  `chaptersurvived` varchar(60) NOT NULL,
  `datesurvived` varchar(60) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `archive`
--

INSERT INTO `archive` (`arc_id`, `fname`, `lname`, `position`, `age`, `chaptersurvived`, `datesurvived`) VALUES
(8, 'fdg', 'dg', 'treasurer', 22, 'fhgfh', '2024-05-31');

-- --------------------------------------------------------

--
-- Table structure for table `arc_chapter`
--

CREATE TABLE `arc_chapter` (
  `archap_id` int(11) NOT NULL,
  `chapname` varchar(60) NOT NULL,
  `chappres` varchar(50) NOT NULL,
  `chapplace` varchar(60) NOT NULL,
  `chapdate` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `arc_chapter`
--

INSERT INTO `arc_chapter` (`archap_id`, `chapname`, `chappres`, `chapplace`, `chapdate`) VALUES
(19, 'dfg', 'dgdg', 'dgd', '2024-05-31');

-- --------------------------------------------------------

--
-- Table structure for table `chapter`
--

CREATE TABLE `chapter` (
  `chapter_id` int(11) NOT NULL,
  `chapter` varchar(50) NOT NULL,
  `pres` varchar(50) NOT NULL,
  `place` varchar(60) NOT NULL,
  `datecreated` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `chapter`
--

INSERT INTO `chapter` (`chapter_id`, `chapter`, `pres`, `place`, `datecreated`) VALUES
(25, 'dg', 'dg', 'dgd', '2024-05-31'),
(26, 'Agusan', 'Cyril Hubay', 'Butuan City', '2024-05-28');

-- --------------------------------------------------------

--
-- Table structure for table `officials`
--

CREATE TABLE `officials` (
  `official_id` int(11) NOT NULL,
  `fname` text NOT NULL,
  `lname` text NOT NULL,
  `position` varchar(50) NOT NULL,
  `age` int(11) NOT NULL,
  `chaptersurvived` varchar(60) NOT NULL,
  `datesurvived` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `officials`
--

INSERT INTO `officials` (`official_id`, `fname`, `lname`, `position`, `age`, `chaptersurvived`, `datesurvived`) VALUES
(20, 'Cyril', 'Hubay', 'president', 22, 'Agusan', '2024-05-28'),
(21, 'Mark Angelo', 'Yakit', 'vice president', 24, 'Agusan', '2024-05-28');

-- --------------------------------------------------------

--
-- Table structure for table `reports`
--

CREATE TABLE `reports` (
  `report_id` int(11) NOT NULL,
  `fname` text NOT NULL,
  `lname` text NOT NULL,
  `gender` text NOT NULL,
  `email` varchar(60) NOT NULL,
  `phone` varchar(11) NOT NULL,
  `datejoin` date NOT NULL,
  `status` text NOT NULL,
  `chapter` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `reports`
--

INSERT INTO `reports` (`report_id`, `fname`, `lname`, `gender`, `email`, `phone`, `datejoin`, `status`, `chapter`) VALUES
(28, 'Alex Janross', 'Sinoc', 'Male', 'alexjanross@gmail.com', '2147483647', '2024-05-28', 'Active', 'Agusan'),
(29, 'Hanna', 'Balberan', 'Female', 'hanna@gmail.com', '15545454', '2024-05-28', 'Active', 'Agusan');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `adlogin`
--
ALTER TABLE `adlogin`
  ADD PRIMARY KEY (`admin_id`);

--
-- Indexes for table `archive`
--
ALTER TABLE `archive`
  ADD PRIMARY KEY (`arc_id`);

--
-- Indexes for table `arc_chapter`
--
ALTER TABLE `arc_chapter`
  ADD PRIMARY KEY (`archap_id`);

--
-- Indexes for table `chapter`
--
ALTER TABLE `chapter`
  ADD PRIMARY KEY (`chapter_id`);

--
-- Indexes for table `officials`
--
ALTER TABLE `officials`
  ADD PRIMARY KEY (`official_id`);

--
-- Indexes for table `reports`
--
ALTER TABLE `reports`
  ADD PRIMARY KEY (`report_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `adlogin`
--
ALTER TABLE `adlogin`
  MODIFY `admin_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `archive`
--
ALTER TABLE `archive`
  MODIFY `arc_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `arc_chapter`
--
ALTER TABLE `arc_chapter`
  MODIFY `archap_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- AUTO_INCREMENT for table `chapter`
--
ALTER TABLE `chapter`
  MODIFY `chapter_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=27;

--
-- AUTO_INCREMENT for table `officials`
--
ALTER TABLE `officials`
  MODIFY `official_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;

--
-- AUTO_INCREMENT for table `reports`
--
ALTER TABLE `reports`
  MODIFY `report_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=35;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
