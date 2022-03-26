-- phpMyAdmin SQL Dump
-- version 4.8.4
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1
-- Généré le :  sam. 26 mars 2022 à 10:42
-- Version du serveur :  10.1.37-MariaDB
-- Version de PHP :  7.3.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données :  `resi_db`
--

-- --------------------------------------------------------

--
-- Structure de la table `authtoken_token`
--

CREATE TABLE `authtoken_token` (
  `key` varchar(40) NOT NULL,
  `created` datetime(6) NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add Token', 7, 'add_token'),
(26, 'Can change Token', 7, 'change_token'),
(27, 'Can delete Token', 7, 'delete_token'),
(28, 'Can view Token', 7, 'view_token'),
(29, 'Can add token', 8, 'add_tokenproxy'),
(30, 'Can change token', 8, 'change_tokenproxy'),
(31, 'Can delete token', 8, 'delete_tokenproxy'),
(32, 'Can view token', 8, 'view_tokenproxy'),
(33, 'Can add ajout de sejour', 9, 'add_ajoutdesejour'),
(34, 'Can change ajout de sejour', 9, 'change_ajoutdesejour'),
(35, 'Can delete ajout de sejour', 9, 'delete_ajoutdesejour'),
(36, 'Can view ajout de sejour', 9, 'view_ajoutdesejour'),
(37, 'Can add client', 10, 'add_client'),
(38, 'Can change client', 10, 'change_client'),
(39, 'Can delete client', 10, 'delete_client'),
(40, 'Can view client', 10, 'view_client'),
(41, 'Can add commande', 11, 'add_commande'),
(42, 'Can change commande', 11, 'change_commande'),
(43, 'Can delete commande', 11, 'delete_commande'),
(44, 'Can view commande', 11, 'view_commande'),
(45, 'Can add note residence', 12, 'add_noteresidence'),
(46, 'Can change note residence', 12, 'change_noteresidence'),
(47, 'Can delete note residence', 12, 'delete_noteresidence'),
(48, 'Can view note residence', 12, 'view_noteresidence'),
(49, 'Can add proprietaire', 13, 'add_proprietaire'),
(50, 'Can change proprietaire', 13, 'change_proprietaire'),
(51, 'Can delete proprietaire', 13, 'delete_proprietaire'),
(52, 'Can view proprietaire', 13, 'view_proprietaire'),
(53, 'Can add residence', 14, 'add_residence'),
(54, 'Can change residence', 14, 'change_residence'),
(55, 'Can delete residence', 14, 'delete_residence'),
(56, 'Can view residence', 14, 'view_residence'),
(57, 'Can add piecesresi', 15, 'add_piecesresi'),
(58, 'Can change piecesresi', 15, 'change_piecesresi'),
(59, 'Can delete piecesresi', 15, 'delete_piecesresi'),
(60, 'Can view piecesresi', 15, 'view_piecesresi'),
(61, 'Can add imagepieceresi', 16, 'add_imagepieceresi'),
(62, 'Can change imagepieceresi', 16, 'change_imagepieceresi'),
(63, 'Can delete imagepieceresi', 16, 'delete_imagepieceresi'),
(64, 'Can view imagepieceresi', 16, 'view_imagepieceresi'),
(65, 'Can add historiqueresi', 17, 'add_historiqueresi'),
(66, 'Can change historiqueresi', 17, 'change_historiqueresi'),
(67, 'Can delete historiqueresi', 17, 'delete_historiqueresi'),
(68, 'Can view historiqueresi', 17, 'view_historiqueresi');

-- --------------------------------------------------------

--
-- Structure de la table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$260000$bC7kXXBkC2GNe8VGGtLWsp$A5bXUZwzv21zQfIjdBfVjzXDCcUr/1tMJZVEs5tOhk8=', '2022-03-11 10:52:23.267841', 1, 'presley', '', '', '', 1, 1, '2022-03-11 10:49:35.015546'),
(2, 'pbkdf2_sha256$260000$Upv2Nt7gQRU8YHKLBzXjdb$DOJx4hlfMmiPNuqf8V4lNMscsLrd7IXwydb/Zvba92o=', NULL, 1, 'root', '', '', '', 1, 1, '2022-03-26 09:40:58.728700');

-- --------------------------------------------------------

--
-- Structure de la table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `client_ajoutdesejour`
--

CREATE TABLE `client_ajoutdesejour` (
  `id` bigint(20) NOT NULL,
  `datefin` date DEFAULT NULL,
  `versementduclient` tinyint(1) NOT NULL,
  `dateajout` datetime(6) NOT NULL,
  `statudemande` varchar(100) NOT NULL,
  `idcommande_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `client_client`
--

CREATE TABLE `client_client` (
  `id` bigint(20) NOT NULL,
  `nom` varchar(25) NOT NULL,
  `prenoms` varchar(75) NOT NULL,
  `phone` varchar(10) NOT NULL,
  `photo` varchar(100) DEFAULT NULL,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `client_commande`
--

CREATE TABLE `client_commande` (
  `id` bigint(20) NOT NULL,
  `prixactuel` int(11) NOT NULL,
  `datedebut` date NOT NULL,
  `datefin` date NOT NULL,
  `versementduclient` tinyint(1) NOT NULL,
  `cleauclient` tinyint(1) NOT NULL,
  `versementauproprio` tinyint(1) NOT NULL,
  `datecommande` datetime(6) NOT NULL,
  `statucommande` varchar(100) NOT NULL,
  `idclient_id` bigint(20) NOT NULL,
  `idresidence_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `client_noteresidence`
--

CREATE TABLE `client_noteresidence` (
  `id` bigint(20) NOT NULL,
  `note` int(11) NOT NULL,
  `date` datetime(6) NOT NULL,
  `idclient_id` bigint(20) NOT NULL,
  `idresidence_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(7, 'authtoken', 'token'),
(8, 'authtoken', 'tokenproxy'),
(9, 'client', 'ajoutdesejour'),
(10, 'client', 'client'),
(11, 'client', 'commande'),
(12, 'client', 'noteresidence'),
(5, 'contenttypes', 'contenttype'),
(17, 'proprio', 'historiqueresi'),
(16, 'proprio', 'imagepieceresi'),
(15, 'proprio', 'piecesresi'),
(13, 'proprio', 'proprietaire'),
(14, 'proprio', 'residence'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Structure de la table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2022-03-11 10:46:38.787153'),
(2, 'auth', '0001_initial', '2022-03-11 10:46:47.339938'),
(3, 'admin', '0001_initial', '2022-03-11 10:46:50.080199'),
(4, 'admin', '0002_logentry_remove_auto_add', '2022-03-11 10:46:50.167519'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2022-03-11 10:46:50.248663'),
(6, 'contenttypes', '0002_remove_content_type_name', '2022-03-11 10:46:52.144959'),
(7, 'auth', '0002_alter_permission_name_max_length', '2022-03-11 10:46:53.209755'),
(8, 'auth', '0003_alter_user_email_max_length', '2022-03-11 10:46:54.279739'),
(9, 'auth', '0004_alter_user_username_opts', '2022-03-11 10:46:54.431414'),
(10, 'auth', '0005_alter_user_last_login_null', '2022-03-11 10:46:54.939767'),
(11, 'auth', '0006_require_contenttypes_0002', '2022-03-11 10:46:55.104806'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2022-03-11 10:46:55.251293'),
(13, 'auth', '0008_alter_user_username_max_length', '2022-03-11 10:46:56.210053'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2022-03-11 10:46:57.029759'),
(15, 'auth', '0010_alter_group_name_max_length', '2022-03-11 10:46:57.840021'),
(16, 'auth', '0011_update_proxy_permissions', '2022-03-11 10:46:57.934956'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2022-03-11 10:46:58.809978'),
(18, 'authtoken', '0001_initial', '2022-03-11 10:47:01.109609'),
(19, 'authtoken', '0002_auto_20160226_1747', '2022-03-11 10:47:01.329727'),
(20, 'authtoken', '0003_tokenproxy', '2022-03-11 10:47:01.411029'),
(21, 'client', '0001_initial', '2022-03-11 10:47:03.399790'),
(22, 'proprio', '0001_initial', '2022-03-11 10:47:09.793825'),
(23, 'client', '0002_initial', '2022-03-11 10:47:15.279835'),
(24, 'client', '0003_alter_commande_options', '2022-03-11 10:47:15.404625'),
(25, 'proprio', '0002_proprietaire_isactivate_proprietaire_piece_identite', '2022-03-11 10:47:16.499679'),
(26, 'sessions', '0001_initial', '2022-03-11 10:47:16.979886');

-- --------------------------------------------------------

--
-- Structure de la table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('bzo1pbp91mi7u84jd8x1pffc7u50nj98', '.eJxVjEEOwiAQRe_C2pCBwhRduu8ZyMCAVA0kpV0Z765NutDtf-_9l_C0rcVvPS1-ZnERSpx-t0DxkeoO-E711mRsdV3mIHdFHrTLqXF6Xg_376BQL9_aAWQGS9baESMQodbKmqjM2VEcNMPgggKDmImYEoYxDoYRE6UcdBDvD8oOOBA:1nScsh:ctWZq5l91R2c-bHNPWwBH-DJ1FNdk5qdT6mmgyyeiBE', '2022-03-25 10:52:23.334819');

-- --------------------------------------------------------

--
-- Structure de la table `proprio_historiqueresi`
--

CREATE TABLE `proprio_historiqueresi` (
  `id` bigint(20) NOT NULL,
  `date` datetime(6) NOT NULL,
  `tempssurannonce` int(11) NOT NULL,
  `visite3D` tinyint(1) NOT NULL,
  `residencecommandé` tinyint(1) NOT NULL,
  `idclient_id` bigint(20) NOT NULL,
  `idresidence_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `proprio_imagepieceresi`
--

CREATE TABLE `proprio_imagepieceresi` (
  `id` bigint(20) NOT NULL,
  `image` varchar(100) NOT NULL,
  `idpiece_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `proprio_piecesresi`
--

CREATE TABLE `proprio_piecesresi` (
  `id` bigint(20) NOT NULL,
  `nompiece` varchar(100) NOT NULL,
  `idresidence_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `proprio_proprietaire`
--

CREATE TABLE `proprio_proprietaire` (
  `id` bigint(20) NOT NULL,
  `nom` varchar(25) NOT NULL,
  `prenoms` varchar(75) NOT NULL,
  `phone` varchar(10) NOT NULL,
  `photo` varchar(100) DEFAULT NULL,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `date` datetime(6) NOT NULL,
  `isactivate` tinyint(1) NOT NULL,
  `piece_identite` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `proprio_residence`
--

CREATE TABLE `proprio_residence` (
  `id` bigint(20) NOT NULL,
  `nbpieces` int(11) NOT NULL,
  `descriptifresidence` longtext NOT NULL,
  `ville` varchar(100) NOT NULL,
  `quartier` varchar(100) NOT NULL,
  `prixjournalier` int(11) NOT NULL,
  `disponibilité` tinyint(1) NOT NULL,
  `photocouverture` varchar(100) DEFAULT NULL,
  `date` datetime(6) NOT NULL,
  `idproprio_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `authtoken_token`
--
ALTER TABLE `authtoken_token`
  ADD PRIMARY KEY (`key`),
  ADD UNIQUE KEY `user_id` (`user_id`);

--
-- Index pour la table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Index pour la table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Index pour la table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Index pour la table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Index pour la table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Index pour la table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Index pour la table `client_ajoutdesejour`
--
ALTER TABLE `client_ajoutdesejour`
  ADD PRIMARY KEY (`id`),
  ADD KEY `client_ajoutdesejour_idcommande_id_66cf73eb_fk_client_co` (`idcommande_id`);

--
-- Index pour la table `client_client`
--
ALTER TABLE `client_client`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Index pour la table `client_commande`
--
ALTER TABLE `client_commande`
  ADD PRIMARY KEY (`id`),
  ADD KEY `client_commande_idclient_id_06de4620_fk_client_client_id` (`idclient_id`),
  ADD KEY `client_commande_idresidence_id_dce87bac_fk_proprio_residence_id` (`idresidence_id`);

--
-- Index pour la table `client_noteresidence`
--
ALTER TABLE `client_noteresidence`
  ADD PRIMARY KEY (`id`),
  ADD KEY `client_noteresidence_idclient_id_70b02b5c_fk_client_client_id` (`idclient_id`),
  ADD KEY `client_noteresidence_idresidence_id_2771983b_fk_proprio_r` (`idresidence_id`);

--
-- Index pour la table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Index pour la table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Index pour la table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Index pour la table `proprio_historiqueresi`
--
ALTER TABLE `proprio_historiqueresi`
  ADD PRIMARY KEY (`id`),
  ADD KEY `proprio_historiqueresi_idclient_id_c6d73889_fk_client_client_id` (`idclient_id`),
  ADD KEY `proprio_historiquere_idresidence_id_c536b3b4_fk_proprio_r` (`idresidence_id`);

--
-- Index pour la table `proprio_imagepieceresi`
--
ALTER TABLE `proprio_imagepieceresi`
  ADD PRIMARY KEY (`id`),
  ADD KEY `proprio_imagepiecere_idpiece_id_d4f90a12_fk_proprio_p` (`idpiece_id`);

--
-- Index pour la table `proprio_piecesresi`
--
ALTER TABLE `proprio_piecesresi`
  ADD PRIMARY KEY (`id`),
  ADD KEY `proprio_piecesresi_idresidence_id_3724a1e8_fk_proprio_r` (`idresidence_id`);

--
-- Index pour la table `proprio_proprietaire`
--
ALTER TABLE `proprio_proprietaire`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Index pour la table `proprio_residence`
--
ALTER TABLE `proprio_residence`
  ADD PRIMARY KEY (`id`),
  ADD KEY `proprio_residence_idproprio_id_2a2b020e_fk_proprio_p` (`idproprio_id`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=69;

--
-- AUTO_INCREMENT pour la table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT pour la table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `client_ajoutdesejour`
--
ALTER TABLE `client_ajoutdesejour`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `client_client`
--
ALTER TABLE `client_client`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `client_commande`
--
ALTER TABLE `client_commande`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `client_noteresidence`
--
ALTER TABLE `client_noteresidence`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT pour la table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=27;

--
-- AUTO_INCREMENT pour la table `proprio_historiqueresi`
--
ALTER TABLE `proprio_historiqueresi`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `proprio_imagepieceresi`
--
ALTER TABLE `proprio_imagepieceresi`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `proprio_piecesresi`
--
ALTER TABLE `proprio_piecesresi`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `proprio_proprietaire`
--
ALTER TABLE `proprio_proprietaire`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `proprio_residence`
--
ALTER TABLE `proprio_residence`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table `authtoken_token`
--
ALTER TABLE `authtoken_token`
  ADD CONSTRAINT `authtoken_token_user_id_35299eff_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Contraintes pour la table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Contraintes pour la table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Contraintes pour la table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Contraintes pour la table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Contraintes pour la table `client_ajoutdesejour`
--
ALTER TABLE `client_ajoutdesejour`
  ADD CONSTRAINT `client_ajoutdesejour_idcommande_id_66cf73eb_fk_client_co` FOREIGN KEY (`idcommande_id`) REFERENCES `client_commande` (`id`);

--
-- Contraintes pour la table `client_commande`
--
ALTER TABLE `client_commande`
  ADD CONSTRAINT `client_commande_idclient_id_06de4620_fk_client_client_id` FOREIGN KEY (`idclient_id`) REFERENCES `client_client` (`id`),
  ADD CONSTRAINT `client_commande_idresidence_id_dce87bac_fk_proprio_residence_id` FOREIGN KEY (`idresidence_id`) REFERENCES `proprio_residence` (`id`);

--
-- Contraintes pour la table `client_noteresidence`
--
ALTER TABLE `client_noteresidence`
  ADD CONSTRAINT `client_noteresidence_idclient_id_70b02b5c_fk_client_client_id` FOREIGN KEY (`idclient_id`) REFERENCES `client_client` (`id`),
  ADD CONSTRAINT `client_noteresidence_idresidence_id_2771983b_fk_proprio_r` FOREIGN KEY (`idresidence_id`) REFERENCES `proprio_residence` (`id`);

--
-- Contraintes pour la table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Contraintes pour la table `proprio_historiqueresi`
--
ALTER TABLE `proprio_historiqueresi`
  ADD CONSTRAINT `proprio_historiquere_idresidence_id_c536b3b4_fk_proprio_r` FOREIGN KEY (`idresidence_id`) REFERENCES `proprio_residence` (`id`),
  ADD CONSTRAINT `proprio_historiqueresi_idclient_id_c6d73889_fk_client_client_id` FOREIGN KEY (`idclient_id`) REFERENCES `client_client` (`id`);

--
-- Contraintes pour la table `proprio_imagepieceresi`
--
ALTER TABLE `proprio_imagepieceresi`
  ADD CONSTRAINT `proprio_imagepiecere_idpiece_id_d4f90a12_fk_proprio_p` FOREIGN KEY (`idpiece_id`) REFERENCES `proprio_piecesresi` (`id`);

--
-- Contraintes pour la table `proprio_piecesresi`
--
ALTER TABLE `proprio_piecesresi`
  ADD CONSTRAINT `proprio_piecesresi_idresidence_id_3724a1e8_fk_proprio_r` FOREIGN KEY (`idresidence_id`) REFERENCES `proprio_residence` (`id`);

--
-- Contraintes pour la table `proprio_residence`
--
ALTER TABLE `proprio_residence`
  ADD CONSTRAINT `proprio_residence_idproprio_id_2a2b020e_fk_proprio_p` FOREIGN KEY (`idproprio_id`) REFERENCES `proprio_proprietaire` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
