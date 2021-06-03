-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema tweet_data
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema tweet_data
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `tweet_data` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `tweet_data` ;

-- -----------------------------------------------------
-- Table `tweet_data`.`user`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `tweet_data`.`user` (
  `user_id` BIGINT NOT NULL,
  `user_id_string` VARCHAR(255) NOT NULL,
  `name_of_user` VARCHAR(255) NULL DEFAULT NULL,
  `display_name` VARCHAR(255) NULL DEFAULT NULL,
  PRIMARY KEY (`user_id`),
  UNIQUE INDEX `user_id_UNIQUE` (`user_id` ASC) VISIBLE,
  UNIQUE INDEX `user_id_string_UNIQUE` (`user_id_string` ASC) VISIBLE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `tweet_data`.`tweet`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `tweet_data`.`tweet` (
  `tweet_id` BIGINT NOT NULL,
  `tweet_id_string` VARCHAR(255) NOT NULL,
  `tweet_text` VARCHAR(300) NULL DEFAULT NULL,
  `user_id` BIGINT NOT NULL,
  PRIMARY KEY (`tweet_id`),
  INDEX `user_id` (`user_id` ASC) VISIBLE,
  UNIQUE INDEX `user_id_UNIQUE` (`user_id` ASC) VISIBLE,
  UNIQUE INDEX `tweet_id_UNIQUE` (`tweet_id` ASC) VISIBLE,
  UNIQUE INDEX `tweet_id_string_UNIQUE` (`tweet_id_string` ASC) VISIBLE,
  CONSTRAINT `tweet_ibfk_1`
    FOREIGN KEY (`user_id`)
    REFERENCES `tweet_data`.`user` (`user_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `tweet_data`.`tweetanalysis`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `tweet_data`.`tweetanalysis` (
  `tweet_id` BIGINT NOT NULL,
  `tfidf_score` DOUBLE NULL DEFAULT NULL,
  `tokens` JSON NULL DEFAULT NULL,
  INDEX `tweet_id` (`tweet_id` ASC) VISIBLE,
  PRIMARY KEY (`tweet_id`),
  UNIQUE INDEX `tweet_id_UNIQUE` (`tweet_id` ASC) VISIBLE,
  CONSTRAINT `tweetanalysis_ibfk_1`
    FOREIGN KEY (`tweet_id`)
    REFERENCES `tweet_data`.`tweet` (`tweet_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `tweet_data`.`tweetentities`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `tweet_data`.`tweetentities` (
  `tweet_id` BIGINT NOT NULL,
  `created_at` TEXT NULL DEFAULT NULL,
  `in_reply_to_user_id` BIGINT NULL DEFAULT NULL,
  `in_reply_to_user_id_string` VARCHAR(255) NULL DEFAULT NULL,
  `in_reply_to_screen_name` VARCHAR(255) NULL DEFAULT NULL,
  `location` TEXT NULL DEFAULT NULL,
  `favourite_count` INT NULL DEFAULT NULL,
  `retweet_count` INT NULL DEFAULT NULL,
  INDEX `tweet_id` (`tweet_id` ASC) VISIBLE,
  UNIQUE INDEX `tweet_id_UNIQUE` (`tweet_id` ASC) VISIBLE,
  PRIMARY KEY (`tweet_id`),
  CONSTRAINT `tweetentities_ibfk_1`
    FOREIGN KEY (`tweet_id`)
    REFERENCES `tweet_data`.`tweet` (`tweet_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
