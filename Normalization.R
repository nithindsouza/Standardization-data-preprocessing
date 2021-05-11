

#Stansardization and normalization
library(readr)

seed <- read.csv("C:\\Users\\hp\\Desktop\\DataSets\\Seeds_data.csv")

summary(seed)
str(seed)

#Standardization

std_seed <-scale(seed)

#Normalization

#function

normalize <-function(x){
    return((x-min(x))/max(x)-min(x))
}

norm_seed <-as.data.frame(lapply(seed, normalize))

summary(norm_seed)


#Now we have a normalized data

















