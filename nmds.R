#this R module calculates NMDS ordination and uses ggplot to display results 
#also calculates species richness 


#change this path to folder with asv table and sample data 
setwd("~/Desktop/Software_Engineering/project/final-project-swe4s_aerosols/aeroDADA2")
require(vegan)
require(ggplot2)

df = read.csv('asv_table_corrected.csv', header = T) 
data = df[,2:length(colnames(df))]
NMDS = metaMDS(data, trymax = 50, na.rm = T, autotransform = TRUE)


points = NMDS$points
df$points = points
p = data.frame(points)
flight = m$Characteristics..Flight.Name
location = m$characteristic
MDS1 = p$MDS1
MDS2 = p$MDS2

#plot NMDS scores, colored by flight and shaped by location
ggplot(p)+geom_point(aes(MDS1, MDS2, col = flight, shape = location), size = 6)+
  theme_bw()+ggtitle('NMDS scores')

#import sample information 
info = read.csv('sample_data.csv', header = T)

#ANOVA to check whether flight groups explain MDS1 axis
flight.aov = aov(MDS1~flight)
summary(flight.aov) #shows that it is significant



#merge data frame with sample data to make plotting easier 
m = merge(df,info,by.x ="X",by.y ="Sample.Name", all.x = TRUE)

#plot MDS pts, colored by flight characteristics
ggplot(m)+geom_point(aes(points[,1], points[,2], col = m$characteristic, size = 3))

#plot beta diversity colored by characteristic 
#beta diversity was calculated in diversity.py module
ggplot(m)+geom_col(aes(m$X,m$correctedBdiv, fill = m$characteristic))



###make a barchart of spp  richness
#first, calculate spp richness of each sample
c = apply(data, 1, function(x) x > 0)
s = apply(c, 2, sum)
df$counts = s
richness = df$counts
sample = seq(1,16,1)

#plot sample * richness 
location = m$characteristic
ggplot(df)+geom_col(aes(sample, richness, fill = location))+
  theme(axis.ticks.x=element_blank())+theme_bw()+
  scale_fill_brewer(palette="Set1")+
  ggtitle('Species richness per flight')


#alternatively, could show richness via boxplot
characteristic = m$characteristic
counts = df$counts
ggplot(df, aes(characteristic, counts))+geom_boxplot() + 
  theme_bw() + 
  geom_jitter(col = 'red', width = .001)
                    