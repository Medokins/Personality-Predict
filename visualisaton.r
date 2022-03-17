pacman::p_load(pacman, caret, lars, tidyverse, rio, cowplot)
library(ggplot2)

data1 <- import("Datasets/MBTI 500.csv")
categories1 <- (data1 %>% group_by(type) %>% summarize(count = n()))

data2 <- import("Datasets/mbti_1.csv")
categories2 <- (data2 %>% group_by(type) %>% summarize(count = n()))

barplot1 <- ggplot(categories1, aes(x = type, y = count)) +
    geom_col() +
    geom_text(aes(label = count), vjust = -0.3)

barplot2 <- ggplot(categories2, aes(x = type, y = count)) +
    geom_col() +
    geom_text(aes(label = count), vjust = -0.3)

plot_grid(barplot1, barplot2, labels = "AUTO")

p_unload(all)
