-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 23, 2025 at 04:03 AM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `sm_ubm`
--

-- --------------------------------------------------------

--
-- Table structure for table `account`
--

CREATE TABLE `account` (
  `email` varchar(100) NOT NULL,
  `username` varchar(50) NOT NULL,
  `fullname` varchar(200) NOT NULL,
  `bio` varchar(200) DEFAULT NULL,
  `password` varchar(300) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `account`
--

INSERT INTO `account` (`email`, `username`, `fullname`, `bio`, `password`) VALUES
('s123456@student.ac.id', 'lisa', 'Lisa Hartanto', 'Berpikir Positif', '25d55ad283aa400af464c76d713c07ad'),
('s123457@student.ac.id', 'sarahsmith', 'Sarah Smith', 'Designer, coffee lover, traveler.', 'a5beb6624e092adf7be31176c3079e64'),
('s123488@student.ac.id', 'janedoe', 'Lisa Hartanto', 'Tetap Berusaha Berpikir Positif', '83cbbd381252d74d77a3ec135966d15e'),
('s123765@student.ac.id', 'emilyb', 'Emily Brown', 'Content writer and blogger', '33d5b76b6bb9ec7d55c1f2998559e0fa');

-- --------------------------------------------------------

--
-- Table structure for table `posting`
--

CREATE TABLE `posting` (
  `idposting` int(12) NOT NULL,
  `title` varchar(100) NOT NULL,
  `image` varchar(200) NOT NULL,
  `content` text NOT NULL,
  `publish_date` datetime NOT NULL DEFAULT current_timestamp(),
  `userpost` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `posting`
--

INSERT INTO `posting` (`idposting`, `title`, `image`, `content`, `publish_date`, `userpost`) VALUES
(1, 'Kehidupan di Kampus: Antara Tugas dan Sosialisasi', 'tugas_dan_sosialisasi.jpg', 'Kehidupan mahasiswa penuh dengan tugas kuliah, tetapi juga ada waktu untuk bersosialisasi', '2025-03-05 12:11:50', 'lisa'),
(2, 'Menghadapi Ujian: Strategi Jitu', 'ujian_mahasiswa.jpg', 'Menjelang ujian, mahasiswa harus mempersiapkan diri dengan baik dan menjaga kesehatan', '2025-03-09 12:12:39', 'sarahsmith'),
(3, 'Rencana Karir Setelah Lulus: Perspektif Mahasiswa', 'rencana_karir.jpg', 'Mahasiswa mulai memikirkan langkah-langkah karir mereka setelah lulus, baik itu melanjutkan studi atau terjun ke dunia kerja', '2025-03-11 12:13:18', 'janedoe'),
(4, 'The Best Travel Destinations', 'travel_destinations.jpg', 'Traveling opens our minds to new cultures, ideas, and experiences', '2025-03-12 12:14:09', 'sarahsmith'),
(5, 'The Future of Artificial Intelligence', 'ai_future.jpg', 'AI is transforming industries in ways we never imagined', '2025-03-04 12:15:12', 'sarahsmith'),
(9, 'Cara Mengatur Keuangan Pribadi', 'finance_tips.jpg', 'Artikel ini menjelaskan cara-cara mudah mengatur keuangan pribadi untuk mencapai kebebasan finansial', '2025-03-10 00:00:00', NULL);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `account`
--
ALTER TABLE `account`
  ADD PRIMARY KEY (`email`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `posting`
--
ALTER TABLE `posting`
  ADD PRIMARY KEY (`idposting`),
  ADD UNIQUE KEY `title` (`title`),
  ADD KEY `userpost` (`userpost`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `posting`
--
ALTER TABLE `posting`
  MODIFY `idposting` int(12) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `posting`
--
ALTER TABLE `posting`
  ADD CONSTRAINT `posting_ibfk_1` FOREIGN KEY (`userpost`) REFERENCES `account` (`username`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
