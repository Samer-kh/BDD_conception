-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1
-- Généré le : lun. 02 jan. 2023 à 21:30
-- Version du serveur : 10.4.27-MariaDB
-- Version de PHP : 8.1.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `bibliotheque`
--

-- --------------------------------------------------------

--
-- Structure de la table `author`
--

CREATE TABLE `author` (
  `author_id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `author`
--

INSERT INTO `author` (`author_id`, `name`) VALUES
(1, 'Samer');

-- --------------------------------------------------------

--
-- Structure de la table `categories`
--

CREATE TABLE `categories` (
  `Category_id` int(11) NOT NULL,
  `name_category` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `categories`
--

INSERT INTO `categories` (`Category_id`, `name_category`) VALUES
(1, 'SF and Documentary');

-- --------------------------------------------------------

--
-- Structure de la table `cost`
--

CREATE TABLE `cost` (
  `cost_id` int(11) NOT NULL,
  `value` float NOT NULL,
  `currancy` varchar(10) NOT NULL,
  `id_echange` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `cost`
--

INSERT INTO `cost` (`cost_id`, `value`, `currancy`, `id_echange`) VALUES
(5, 588, 'Dollar', 1),
(6, 400, 'Euro', 1),
(7, 100, 'Pound', 1);

-- --------------------------------------------------------

--
-- Structure de la table `ecl_thesis`
--

CREATE TABLE `ecl_thesis` (
  `Id_thesis` int(11) NOT NULL,
  `Author_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `ecl_thesis`
--

INSERT INTO `ecl_thesis` (`Id_thesis`, `Author_id`) VALUES
(9, 1);

-- --------------------------------------------------------

--
-- Structure de la table `exchange`
--

CREATE TABLE `exchange` (
  `exchange_id` int(11) NOT NULL,
  `euro_to_dollar` float NOT NULL,
  `pound_to_dollar` float NOT NULL,
  `euro_to_pound` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `exchange`
--

INSERT INTO `exchange` (`exchange_id`, `euro_to_dollar`, `pound_to_dollar`, `euro_to_pound`) VALUES
(1, 1, 1, 1);

-- --------------------------------------------------------

--
-- Structure de la table `internal_reports`
--

CREATE TABLE `internal_reports` (
  `report_id` int(11) NOT NULL,
  `title` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `internal_reports`
--

INSERT INTO `internal_reports` (`report_id`, `title`) VALUES
(9, 'Physics EM'),
(10, 'Math in Quantum Physics');

-- --------------------------------------------------------

--
-- Structure de la table `keyword`
--

CREATE TABLE `keyword` (
  `key_id` int(11) NOT NULL,
  `value` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `keyword`
--

INSERT INTO `keyword` (`key_id`, `value`) VALUES
(1, 'Math'),
(2, 'Phy');

-- --------------------------------------------------------

--
-- Structure de la table `keyword_publication`
--

CREATE TABLE `keyword_publication` (
  `id` int(11) NOT NULL,
  `key_id` int(11) DEFAULT NULL,
  `publication_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `keyword_user`
--

CREATE TABLE `keyword_user` (
  `id` int(11) NOT NULL,
  `key_id` int(11) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `lab`
--

CREATE TABLE `lab` (
  `lab_id` int(11) NOT NULL,
  `lab_name` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `lab`
--

INSERT INTO `lab` (`lab_id`, `lab_name`) VALUES
(1, 'LIRIS');

-- --------------------------------------------------------

--
-- Structure de la table `periodics`
--

CREATE TABLE `periodics` (
  `periodic_id` int(11) NOT NULL,
  `volume` int(11) NOT NULL,
  `publisher` varchar(50) NOT NULL,
  `edition` varchar(50) NOT NULL,
  `book_shop` varchar(50) NOT NULL,
  `cost_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `periodics`
--

INSERT INTO `periodics` (`periodic_id`, `volume`, `publisher`, `edition`, `book_shop`, `cost_id`) VALUES
(7, 27, 'LaRousse', '2000', 'ECL Books', 5),
(8, 45, 'Adrien Yves', '1995', 'Ecully books', 6);

-- --------------------------------------------------------

--
-- Structure de la table `publication`
--

CREATE TABLE `publication` (
  `publication_id` int(11) NOT NULL,
  `year_publication` date NOT NULL,
  `state` varchar(50) NOT NULL,
  `lab_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `publication`
--

INSERT INTO `publication` (`publication_id`, `year_publication`, `state`, `lab_id`) VALUES
(1, '2022-12-31', 'On rack', 1),
(2, '2022-11-29', 'lost', 1),
(3, '2022-02-16', 'issued to', 1),
(5, '1990-03-01', 'to be bought', 1),
(6, '2018-02-02', 'On rack', 1),
(7, '2019-04-18', 'issued to', 1),
(8, '2021-05-06', 'to be bought', 1),
(9, '2022-01-13', 'On rack', 1),
(10, '2022-02-17', 'to be bought', 1);

-- --------------------------------------------------------

--
-- Structure de la table `pub_lab_hascppy`
--

CREATE TABLE `pub_lab_hascppy` (
  `id` int(11) NOT NULL,
  `publication_id` int(11) DEFAULT NULL,
  `lab_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `pub_lab_hascppy`
--

INSERT INTO `pub_lab_hascppy` (`id`, `publication_id`, `lab_id`) VALUES
(1, 1, 1);

-- --------------------------------------------------------

--
-- Structure de la table `regularbooks`
--

CREATE TABLE `regularbooks` (
  `ISBN` int(11) NOT NULL,
  `title` varchar(50) NOT NULL,
  `publisher` varchar(50) NOT NULL,
  `edition` varchar(50) NOT NULL,
  `book_shop` varchar(50) NOT NULL,
  `cost_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `regularbooks`
--

INSERT INTO `regularbooks` (`ISBN`, `title`, `publisher`, `edition`, `book_shop`, `cost_id`) VALUES
(5, 'Les misérables', 'LaLib', '2020', 'ECL Biblio', 5),
(6, 'Math pour les debs', 'LaRousse', '1987', 'Ecl bib', 5);

-- --------------------------------------------------------

--
-- Structure de la table `regular_books_author`
--

CREATE TABLE `regular_books_author` (
  `id` int(11) NOT NULL,
  `author_id` int(11) DEFAULT NULL,
  `ISBN` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `regular_books_author`
--

INSERT INTO `regular_books_author` (`id`, `author_id`, `ISBN`) VALUES
(1, 1, 5),
(2, 1, 6);

-- --------------------------------------------------------

--
-- Structure de la table `regular_books_category`
--

CREATE TABLE `regular_books_category` (
  `id` int(11) NOT NULL,
  `ISBN` int(11) DEFAULT NULL,
  `Category_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `regular_books_category`
--

INSERT INTO `regular_books_category` (`id`, `ISBN`, `Category_id`) VALUES
(1, 6, 1),
(2, 5, 1);

-- --------------------------------------------------------

--
-- Structure de la table `scientific_author`
--

CREATE TABLE `scientific_author` (
  `id` int(11) NOT NULL,
  `author_id` int(11) DEFAULT NULL,
  `Id_Report` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `scientific_author`
--

INSERT INTO `scientific_author` (`id`, `author_id`, `Id_Report`) VALUES
(1, 1, 10);

-- --------------------------------------------------------

--
-- Structure de la table `scientific_reports`
--

CREATE TABLE `scientific_reports` (
  `Id_Report` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `scientific_reports`
--

INSERT INTO `scientific_reports` (`Id_Report`) VALUES
(10);

-- --------------------------------------------------------

--
-- Structure de la table `user`
--

CREATE TABLE `user` (
  `user_id` int(11) NOT NULL,
  `email` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `user`
--

INSERT INTO `user` (`user_id`, `email`) VALUES
(1, 'samer@gmail.com');

-- --------------------------------------------------------

--
-- Structure de la table `user_lab_auth`
--

CREATE TABLE `user_lab_auth` (
  `id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `lab_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `user_lab_auth`
--

INSERT INTO `user_lab_auth` (`id`, `user_id`, `lab_id`) VALUES
(1, 1, 1);

-- --------------------------------------------------------

--
-- Structure de la table `user_lab_notif`
--

CREATE TABLE `user_lab_notif` (
  `id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `lab_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `user_publication`
--

CREATE TABLE `user_publication` (
  `id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `publication_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `user_publication`
--

INSERT INTO `user_publication` (`id`, `user_id`, `publication_id`) VALUES
(1, 1, 1),
(2, 1, 2),
(3, 1, 5);

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `author`
--
ALTER TABLE `author`
  ADD PRIMARY KEY (`author_id`);

--
-- Index pour la table `categories`
--
ALTER TABLE `categories`
  ADD PRIMARY KEY (`Category_id`);

--
-- Index pour la table `cost`
--
ALTER TABLE `cost`
  ADD PRIMARY KEY (`cost_id`),
  ADD KEY `id_echange` (`id_echange`);

--
-- Index pour la table `ecl_thesis`
--
ALTER TABLE `ecl_thesis`
  ADD PRIMARY KEY (`Id_thesis`);

--
-- Index pour la table `exchange`
--
ALTER TABLE `exchange`
  ADD PRIMARY KEY (`exchange_id`);

--
-- Index pour la table `internal_reports`
--
ALTER TABLE `internal_reports`
  ADD PRIMARY KEY (`report_id`);

--
-- Index pour la table `keyword`
--
ALTER TABLE `keyword`
  ADD PRIMARY KEY (`key_id`);

--
-- Index pour la table `keyword_publication`
--
ALTER TABLE `keyword_publication`
  ADD PRIMARY KEY (`id`),
  ADD KEY `key_id` (`key_id`),
  ADD KEY `publication_id` (`publication_id`);

--
-- Index pour la table `keyword_user`
--
ALTER TABLE `keyword_user`
  ADD PRIMARY KEY (`id`),
  ADD KEY `key_id` (`key_id`),
  ADD KEY `user_id` (`user_id`);

--
-- Index pour la table `lab`
--
ALTER TABLE `lab`
  ADD PRIMARY KEY (`lab_id`);

--
-- Index pour la table `periodics`
--
ALTER TABLE `periodics`
  ADD PRIMARY KEY (`periodic_id`),
  ADD KEY `cost_id` (`cost_id`);

--
-- Index pour la table `publication`
--
ALTER TABLE `publication`
  ADD PRIMARY KEY (`publication_id`),
  ADD KEY `lab_id` (`lab_id`);

--
-- Index pour la table `pub_lab_hascppy`
--
ALTER TABLE `pub_lab_hascppy`
  ADD PRIMARY KEY (`id`),
  ADD KEY `publication_id` (`publication_id`),
  ADD KEY `lab_id` (`lab_id`);

--
-- Index pour la table `regularbooks`
--
ALTER TABLE `regularbooks`
  ADD PRIMARY KEY (`ISBN`),
  ADD KEY `cost_id` (`cost_id`);

--
-- Index pour la table `regular_books_author`
--
ALTER TABLE `regular_books_author`
  ADD PRIMARY KEY (`id`),
  ADD KEY `author_id` (`author_id`),
  ADD KEY `ISBN` (`ISBN`);

--
-- Index pour la table `regular_books_category`
--
ALTER TABLE `regular_books_category`
  ADD PRIMARY KEY (`id`),
  ADD KEY `ISBN` (`ISBN`),
  ADD KEY `Category_id` (`Category_id`);

--
-- Index pour la table `scientific_author`
--
ALTER TABLE `scientific_author`
  ADD PRIMARY KEY (`id`),
  ADD KEY `author_id` (`author_id`),
  ADD KEY `Id_Report` (`Id_Report`);

--
-- Index pour la table `scientific_reports`
--
ALTER TABLE `scientific_reports`
  ADD PRIMARY KEY (`Id_Report`);

--
-- Index pour la table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`user_id`);

--
-- Index pour la table `user_lab_auth`
--
ALTER TABLE `user_lab_auth`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`),
  ADD KEY `lab_id` (`lab_id`);

--
-- Index pour la table `user_lab_notif`
--
ALTER TABLE `user_lab_notif`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`),
  ADD KEY `lab_id` (`lab_id`);

--
-- Index pour la table `user_publication`
--
ALTER TABLE `user_publication`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`),
  ADD KEY `publication_id` (`publication_id`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `author`
--
ALTER TABLE `author`
  MODIFY `author_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT pour la table `categories`
--
ALTER TABLE `categories`
  MODIFY `Category_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT pour la table `cost`
--
ALTER TABLE `cost`
  MODIFY `cost_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT pour la table `exchange`
--
ALTER TABLE `exchange`
  MODIFY `exchange_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT pour la table `keyword`
--
ALTER TABLE `keyword`
  MODIFY `key_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT pour la table `keyword_publication`
--
ALTER TABLE `keyword_publication`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `keyword_user`
--
ALTER TABLE `keyword_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `lab`
--
ALTER TABLE `lab`
  MODIFY `lab_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT pour la table `publication`
--
ALTER TABLE `publication`
  MODIFY `publication_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT pour la table `pub_lab_hascppy`
--
ALTER TABLE `pub_lab_hascppy`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT pour la table `regular_books_author`
--
ALTER TABLE `regular_books_author`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT pour la table `regular_books_category`
--
ALTER TABLE `regular_books_category`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT pour la table `scientific_author`
--
ALTER TABLE `scientific_author`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT pour la table `user`
--
ALTER TABLE `user`
  MODIFY `user_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT pour la table `user_lab_auth`
--
ALTER TABLE `user_lab_auth`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT pour la table `user_lab_notif`
--
ALTER TABLE `user_lab_notif`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `user_publication`
--
ALTER TABLE `user_publication`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table `cost`
--
ALTER TABLE `cost`
  ADD CONSTRAINT `cost_ibfk_1` FOREIGN KEY (`id_echange`) REFERENCES `exchange` (`exchange_id`);

--
-- Contraintes pour la table `ecl_thesis`
--
ALTER TABLE `ecl_thesis`
  ADD CONSTRAINT `ecl_thesis_ibfk_1` FOREIGN KEY (`Id_thesis`) REFERENCES `internal_reports` (`report_id`);

--
-- Contraintes pour la table `internal_reports`
--
ALTER TABLE `internal_reports`
  ADD CONSTRAINT `internal_reports_ibfk_1` FOREIGN KEY (`report_id`) REFERENCES `publication` (`publication_id`);

--
-- Contraintes pour la table `keyword_publication`
--
ALTER TABLE `keyword_publication`
  ADD CONSTRAINT `keyword_publication_ibfk_1` FOREIGN KEY (`key_id`) REFERENCES `keyword` (`key_id`),
  ADD CONSTRAINT `keyword_publication_ibfk_2` FOREIGN KEY (`publication_id`) REFERENCES `publication` (`publication_id`);

--
-- Contraintes pour la table `keyword_user`
--
ALTER TABLE `keyword_user`
  ADD CONSTRAINT `keyword_user_ibfk_1` FOREIGN KEY (`key_id`) REFERENCES `keyword` (`key_id`),
  ADD CONSTRAINT `keyword_user_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `user` (`user_id`);

--
-- Contraintes pour la table `periodics`
--
ALTER TABLE `periodics`
  ADD CONSTRAINT `periodics_ibfk_1` FOREIGN KEY (`periodic_id`) REFERENCES `publication` (`publication_id`),
  ADD CONSTRAINT `periodics_ibfk_2` FOREIGN KEY (`cost_id`) REFERENCES `cost` (`cost_id`);

--
-- Contraintes pour la table `publication`
--
ALTER TABLE `publication`
  ADD CONSTRAINT `publication_ibfk_1` FOREIGN KEY (`lab_id`) REFERENCES `lab` (`lab_id`);

--
-- Contraintes pour la table `pub_lab_hascppy`
--
ALTER TABLE `pub_lab_hascppy`
  ADD CONSTRAINT `pub_lab_hascppy_ibfk_1` FOREIGN KEY (`publication_id`) REFERENCES `publication` (`publication_id`),
  ADD CONSTRAINT `pub_lab_hascppy_ibfk_2` FOREIGN KEY (`lab_id`) REFERENCES `lab` (`lab_id`);

--
-- Contraintes pour la table `regularbooks`
--
ALTER TABLE `regularbooks`
  ADD CONSTRAINT `regularbooks_ibfk_1` FOREIGN KEY (`ISBN`) REFERENCES `publication` (`publication_id`),
  ADD CONSTRAINT `regularbooks_ibfk_2` FOREIGN KEY (`cost_id`) REFERENCES `cost` (`cost_id`);

--
-- Contraintes pour la table `regular_books_author`
--
ALTER TABLE `regular_books_author`
  ADD CONSTRAINT `regular_books_author_ibfk_1` FOREIGN KEY (`author_id`) REFERENCES `author` (`author_id`),
  ADD CONSTRAINT `regular_books_author_ibfk_2` FOREIGN KEY (`ISBN`) REFERENCES `regularbooks` (`ISBN`);

--
-- Contraintes pour la table `regular_books_category`
--
ALTER TABLE `regular_books_category`
  ADD CONSTRAINT `regular_books_category_ibfk_1` FOREIGN KEY (`ISBN`) REFERENCES `regularbooks` (`ISBN`),
  ADD CONSTRAINT `regular_books_category_ibfk_2` FOREIGN KEY (`Category_id`) REFERENCES `categories` (`Category_id`);

--
-- Contraintes pour la table `scientific_author`
--
ALTER TABLE `scientific_author`
  ADD CONSTRAINT `scientific_author_ibfk_1` FOREIGN KEY (`author_id`) REFERENCES `author` (`author_id`),
  ADD CONSTRAINT `scientific_author_ibfk_2` FOREIGN KEY (`Id_Report`) REFERENCES `scientific_reports` (`Id_Report`);

--
-- Contraintes pour la table `scientific_reports`
--
ALTER TABLE `scientific_reports`
  ADD CONSTRAINT `scientific_reports_ibfk_1` FOREIGN KEY (`Id_Report`) REFERENCES `internal_reports` (`report_id`);

--
-- Contraintes pour la table `user_lab_auth`
--
ALTER TABLE `user_lab_auth`
  ADD CONSTRAINT `user_lab_auth_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`user_id`),
  ADD CONSTRAINT `user_lab_auth_ibfk_2` FOREIGN KEY (`lab_id`) REFERENCES `lab` (`lab_id`);

--
-- Contraintes pour la table `user_lab_notif`
--
ALTER TABLE `user_lab_notif`
  ADD CONSTRAINT `user_lab_notif_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`user_id`),
  ADD CONSTRAINT `user_lab_notif_ibfk_2` FOREIGN KEY (`lab_id`) REFERENCES `lab` (`lab_id`);

--
-- Contraintes pour la table `user_publication`
--
ALTER TABLE `user_publication`
  ADD CONSTRAINT `user_publication_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`user_id`),
  ADD CONSTRAINT `user_publication_ibfk_2` FOREIGN KEY (`publication_id`) REFERENCES `publication` (`publication_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
