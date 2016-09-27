-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema posts
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema posts
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `posts` DEFAULT CHARACTER SET utf8 ;
USE `posts` ;

-- -----------------------------------------------------
-- Table `posts`.`posts`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `posts`.`posts` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `description` TEXT(1000) NULL,
  `created_at` DATETIME NOT NULL,
  `updated_at` DATETIME NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC))
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
