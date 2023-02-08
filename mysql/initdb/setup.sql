-- ************************************** `races`

CREATE TABLE `races`
(
    `id`                varchar(45) NOT NULL ,
    `race_name`         varchar(45) NOT NULL ,
    `race_place`        varchar(45) NOT NULL ,
    `number_of_entries` int NOT NULL ,
    `race_state`        varchar(45) NOT NULL,
    `date`              varchar(45) NOT NULL ,

    PRIMARY KEY (`id`)
);

-- ************************************** `race_results`

CREATE TABLE `race_results`
(
    `id`             int NOT NULL ,
    `rank`           int NOT NULL ,
    `box`            int NOT NULL ,
    `horse_order`    int NOT NULL ,
    `horse_name`     varchar(45) NOT NULL ,
    `sex_and_age`    varchar(45) NOT NULL ,
    `burden_weight`  int NOT NULL ,
    `jockey`         varchar(45) NOT NULL ,
    `time`           varchar(45) NOT NULL ,
    `difference`     varchar(45) NOT NULL ,
    `transit`        varchar(45) NOT NULL ,
    `climb`          decimal NOT NULL ,
    `odds`           decimal NOT NULL ,
    `popularity`     int NOT NULL ,
    `horse_weight`   varchar(45) NOT NULL ,
    `horse_trainer`  varchar(45) NOT NULL ,
    `horce_owner`    varchar(45) NOT NULL ,
    `prize`          decimal NULL ,

    PRIMARY KEY (`id`),
    KEY `FK_1` (`id`),
    CONSTRAINT `FK_2` FOREIGN KEY `FK_1` (`id`) REFERENCES `races` (`id`)
);