-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 10 Jan 2024 pada 17.26
-- Versi server: 10.4.27-MariaDB
-- Versi PHP: 8.1.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `my_toko`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `addproduct`
--

CREATE TABLE `addproduct` (
  `id` int(11) NOT NULL,
  `name` varchar(80) NOT NULL,
  `price` int(11) NOT NULL,
  `discount` int(11) NOT NULL,
  `stok` int(11) NOT NULL,
  `brand_id` int(11) NOT NULL,
  `category_id` int(11) NOT NULL,
  `colors` text NOT NULL,
  `description` text NOT NULL,
  `pub_date` datetime NOT NULL,
  `image_1` varchar(150) NOT NULL,
  `image_2` varchar(150) NOT NULL,
  `image_3` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `addproduct`
--

INSERT INTO `addproduct` (`id`, `name`, `price`, `discount`, `stok`, `brand_id`, `category_id`, `colors`, `description`, `pub_date`, `image_1`, `image_2`, `image_3`) VALUES
(3, 'iPhone 14', 14000000, 10, 100, 1, 3, 'Purple', 'iPhone 14 512GB Purple', '2024-01-10 13:13:54', '48d0641e6c0e6f302b40.jpg', '8181b6bff515798979d9.jpg', '06098bc33341a52b050d.png'),
(4, 'Macbook Pro M2', 21000000, 0, 10, 1, 5, 'Silver', 'Apple Macbook Pro M2', '2024-01-10 13:16:40', '83713bc76832a8c67338.jpg', '19c4e2e6f266a1103454.jpg', '75578b7638297191397f.jpg'),
(5, 'iPad Pro', 9000000, 0, 15, 1, 2, 'Grey, Gold', 'Apple iPad Pro', '2024-01-10 13:17:36', '377ef22251a094c8777e.jpg', '4e3da1a3a767cad028fd.jpg', '2db7fbbf2b5f2cfd2bf5.jpeg'),
(6, 'Samsung Galaxy S23 Ultra', 22000000, 0, 9, 2, 3, 'Grey', 'Samsung Galaxy S23 Ultra', '2024-01-10 13:21:27', '5bab38be850c3eb911d4.jpg', '005ecd97d5c0c4a4d29e.jpeg', '8c156ecc0ddf0c7e1407.jpg');

-- --------------------------------------------------------

--
-- Struktur dari tabel `brand`
--

CREATE TABLE `brand` (
  `id` int(11) NOT NULL,
  `name` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `brand`
--

INSERT INTO `brand` (`id`, `name`) VALUES
(1, 'Apple'),
(2, 'Samsung'),
(3, 'Lenovo');

-- --------------------------------------------------------

--
-- Struktur dari tabel `category`
--

CREATE TABLE `category` (
  `id` int(11) NOT NULL,
  `name` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `category`
--

INSERT INTO `category` (`id`, `name`) VALUES
(2, 'Mobile'),
(3, 'Phone'),
(4, 'Desktop'),
(5, 'Laptop');

-- --------------------------------------------------------

--
-- Struktur dari tabel `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `name` varchar(30) NOT NULL,
  `username` varchar(80) NOT NULL,
  `email` varchar(120) NOT NULL,
  `password` varchar(180) NOT NULL,
  `profile` varchar(180) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `user`
--

INSERT INTO `user` (`id`, `name`, `username`, `email`, `password`, `profile`) VALUES
(1, 'Tegar Rakasiwi', 'Tegaaar', 'Tegar@gmail.com', '$2b$12$EB.mZJ2qFdNdbXQL7.IsSeD8sM8730TZL.HtFE/TCXYgRJKfKBcZ2', 'profile.jpg'),
(3, 'Admin', 'Admin', 'Admin@gmail.com', '$2b$12$GNlTw3EhKBxAqZOmLMYkI.anlxmTSRgIzmnSCycsfKJF.tFq5qBfe', 'profile.jpg');

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `addproduct`
--
ALTER TABLE `addproduct`
  ADD PRIMARY KEY (`id`);

--
-- Indeks untuk tabel `brand`
--
ALTER TABLE `brand`
  ADD PRIMARY KEY (`id`);

--
-- Indeks untuk tabel `category`
--
ALTER TABLE `category`
  ADD PRIMARY KEY (`id`);

--
-- Indeks untuk tabel `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `addproduct`
--
ALTER TABLE `addproduct`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT untuk tabel `brand`
--
ALTER TABLE `brand`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT untuk tabel `category`
--
ALTER TABLE `category`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT untuk tabel `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
