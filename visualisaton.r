pacman::p_load(pacman, caret, lars, tidyverse, rio)
library(dplyr)
library(ggplot2)

data <- import("Datasets/mbti_1.csv")

categories <- (data %>% group_by(type) %>% summarize(count = n()))

ggplot(categories, aes(x = type, y = count)) +
    geom_col() +
    geom_text(aes(label = count), vjust = -0.3)

p_unload(all)
