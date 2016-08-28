-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema walldb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema walldb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `walldb` DEFAULT CHARACTER SET utf8 ;
USE `walldb` ;

-- -----------------------------------------------------
-- Table `walldb`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `walldb`.`users` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(45) NOT NULL,
  `last_name` VARCHAR(45) NOT NULL,
  `email` VARCHAR(45) NOT NULL,
  `password` VARCHAR(255) NULL,
  `created_at` DATETIME NOT NULL,
  `updated_at` DATETIME NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `walldb`.`messages`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `walldb`.`messages` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `user_id` INT UNSIGNED NOT NULL,
  `message` TEXT(1000) NULL,
  `created_at` DATETIME NOT NULL,
  `updated_at` DATETIME NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC),
  INDEX `fk_messages_users_user_id_idx` (`user_id` ASC),
  CONSTRAINT `fk_messages_users_user_id`
    FOREIGN KEY (`user_id`)
    REFERENCES `walldb`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `walldb`.`comments`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `walldb`.`comments` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `message_id` INT UNSIGNED NOT NULL,
  `user_id` INT UNSIGNED NOT NULL,
  `comment` TEXT(1000) NULL,
  `created_at` DATETIME NOT NULL,
  `updated_at` DATETIME NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `message_id_UNIQUE` (`id` ASC),
  INDEX `fk_comments_messages_message_id_idx` (`message_id` ASC),
  INDEX `fk_comments_users_user_id_idx` (`user_id` ASC),
  CONSTRAINT `fk_comments_users_user_id`
    FOREIGN KEY (`user_id`)
    REFERENCES `walldb`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_comments_messages_message_id`
    FOREIGN KEY (`message_id`)
    REFERENCES `walldb`.`messages` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
