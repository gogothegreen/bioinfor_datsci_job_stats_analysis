#!/usr/bin/env Rscript
library(ggplot2)

LangCounts.df=read.table("bioinformatics_job_stats/combined_job_skills_counts.txt", header = TRUE, sep = ",", stringsAsFactors = TRUE, comment.char="")

pdf("bioinformatics_job_stats/combined_job_skills_counts.pdf")
myPlot=ggplot(data = LangCounts.df, aes(x = reorder(language, counts), y = counts, fill = group))
myPlot +
  geom_bar(stat = "identity", position = position_dodge()) +
  ggtitle("Job skills\nBioinformatics vs Datascience") +
  labs(y= "Number of jobs", x = "Software skills") +
  coord_flip() +
  theme_bw() +
  theme(axis.text.y = element_text(size = 5, vjust = 0.5, hjust=1),
        legend.position = c(0.9, 0.9),
        legend.title = element_blank(),
        plot.title = element_text(hjust = 0.5),
        axis.line = element_line(color='black'),
        plot.background = element_blank(),
        panel.grid.major = element_blank(),
        panel.grid.minor = element_blank(),
        panel.border = element_blank())
dev.off()