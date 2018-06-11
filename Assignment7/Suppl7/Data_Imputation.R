if(!require(data.table)){
  install.packages("data.table")
}
if(!require(ggplot2)){
  install.packages("ggplot2")
}

dat = fread("ms_toy.txt") #read data
dat = as.matrix(dat)      #transform fo better plotting

org_dat = dat[,1]

c1 = org_dat
  #plot of inital dist of col 1

s = sd(org_dat, na.rm = T)    # compute standart deviation
s = 1/4 *s                    # take fraction

q = quantile(org_dat, na.rm = T)  # compute quantiles
nm = as.numeric(q[2])             # set new mean to 25% quantile 

filles = list()
for(i in 1:length(org_dat)){
  if(is.na(org_dat[i])){
    org_dat[i] = rnorm(1, nm, s)
    filles[length(filles)+1]= org_dat[i]
  }
}

hist(org_dat, col = "Green", xlab = "Expression Value")
hist(c1, col = "Blue", add = T)
hist(as.numeric(filles), col = "Red", add=T)




