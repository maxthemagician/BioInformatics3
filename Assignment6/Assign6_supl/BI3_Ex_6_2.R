# needed to install impute using bioclite
# source("https://bioconductor.org/biocLite.R")
# biocLite("impute")
# biocLite("preprocessCore")
if(!require(data.table)){
  install.packages("data.table")
}
if(!require(samr)){
  install.packages("samr")
}
if(!require(preprocessCore)){
  install.packages("preprocessCore")
}

# read data
dat = fread("ms_data.txt")

#### log2-transfrom ####
dat[,1:9] = log2(dat[,1:9])

#### quantile normalization ####
mat = normalize.quantiles(as.matrix(dat[,1:9]))


#### SAM ####

y<-c(rep(1,3),rep(2,6))   #define classes, 3 controles, 6 rnas
####  FDR ####
# frd 5%
samfit5 = SAM(mat,y,resp.type ="Two class unpaired", fdr.output = 0.05, nperms = 1000, genenames = dat$Gene.names)
plot(samfit5)

#down and up regulated genes
samfit5$siggenes.table$genes.up[1:10,]
samfit5$siggenes.table$genes.lo[1:10,]


# frd 20%
samfit20 = SAM(mat,y,resp.type ="Two class unpaired", fdr.output = 0.20, nperms = 1000, genenames = dat$Gene.names)
plot(samfit20)

#down and up regulated genes
samfit20$siggenes.table$genes.up[1:10,]
samfit20$siggenes.table$genes.lo[1:10,]

samfit20$siggenes.table$ngenes.up
samfit5$siggenes.table$ngenes.up

samfit20$siggenes.table$ngenes.lo
samfit5$siggenes.table$ngenes.lo

# -> fdr does not change anything in top 10 up and down
#    changes the number of dregulated genes drastically

#### nperms ####
# nperms 1000
samfit1000 = SAM(mat,y,resp.type ="Two class unpaired", fdr.output = 0.20, nperms = 1000, genenames = dat$Gene.names)
plot(samfit1000)

#down and up regulated genes
samfit1000$siggenes.table$genes.up[1:10,]
samfit1000$siggenes.table$genes.lo[1:10,]

# nperms 100
samfit100 = SAM(mat,y,resp.type ="Two class unpaired", fdr.output = 0.20, nperms = 100, genenames = dat$Gene.names)
plot(samfit100)

#down and up regulated genes
samfit100$siggenes.table$genes.up[1:10,]
samfit100$siggenes.table$genes.lo[1:10,]

# -> nperms does not influence the top 10 up and down, 
#    but the overall distribution of the extreme values -> plots