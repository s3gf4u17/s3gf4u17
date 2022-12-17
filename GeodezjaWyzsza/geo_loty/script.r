# > dataset <- read.csv(file.choose(),header=TRUE,sep=",")
# > View(dataset)
# > library(stringr)
# > dataset[c('phi','lambda')] <- str_split_fixed(dataset$Position,',', 2)
# > dataset[c('phi')] <- as.numeric(dataset$phi)
# > dataset[c('lambda')] <- as.numeric(dataset$lambda)
# > class(dataset$lambda)
# > dataset[c('Altitude')] <- dataset$Altitude*0.3048+135.4
# > dataset[c('phi')] <- dataset$phi/180*pi
# > dataset[c('lambda')] <- dataset$lambda/180*pi
# > a <- 6378137
# > e2 <- 0.00669438002290
# > dataset[c('N')] <- (a/sqrt(1-e2*sin(dataset$phi)*sin(dataset$phi)))
# > dataset[c('X')] <- ((dataset$N+dataset$Altitude)*cos(dataset$phi)*cos(dataset$lambda))
# > dataset[c('Y')] <- ((dataset$N+dataset$Altitude)*cos(dataset$phi)*sin(dataset$lambda))
# > dataset[c('Z')] <- ((dataset$N*(1-e2)+dataset$Altitude)*sin(dataset$phi))
# > x <- dataset$X[1]
# > y <- dataset$Y[1]
# > z <- dataset$Z[1]
# > dataset[c('X')] <- dataset$X-x
# > dataset[c('Y')] <- dataset$Y-y
# > dataset[c('Z')] <- dataset$Z-z
# > plot(dataset$Timestamp,dataset$Altitude)
# > plot(dataset$Timestamp,dataset$Speed)
# > plot(dataset$Timestamp,dataset$X)
# > plot(dataset$Timestamp,dataset$Y)
# > plot(dataset$Timestamp,dataset$Z)
# > phi <- dataset$phi[1]
# > lambda <- dataset$lambda[1]
# > rneu <- matrix(c(-sin(phi)*cos(lambda),-sin(phi)*sin(lambda),cos(phi),-sin(lambda),cos(lambda),0,cos(phi)*cos(lambda),cos(phi)*sin(lambda),sin(phi)),ncol=3,nrow=3)
# > rneut <- t(rneu)


# > dataset[c('n')] <- dataset$X*rneut[1]+dataset$Y*rneut[4]+dataset$Z*rneut[7]
# > dataset[c('e')] <- dataset$X*rneut[2]+dataset$Y*rneut[5]+dataset$Z*rneut[8]
# > dataset[c('u')] <- dataset$X*rneut[3]+dataset$Y*rneut[6]+dataset$Z*rneut[9]
# > dataset[c('s')] <- sqrt(dataset$n*dataset$n+dataset$e*dataset$e+dataset$u*dataset$u)
# > dataset[c('az')] <- atan(dataset$e/dataset$n)
# > dataset[c('h')] <- asin(dataset$u/sqrt(dataset$n*dataset$n+dataset$e*dataset$e+dataset$u*dataset$u))
# > attach(dataset)













# The following objects are masked _by_ .GlobalEnv:

#     lambda, phi

# The following objects are masked from dataset (pos = 3):

#     Altitude, az, Callsign, Direction, e, h, lambda, n, N, phi, Position, s, Speed, Timestamp, u, UTC, X, Y, Z

# > plot(Timestamp,s)
# > plot(Timestamp,h)
# > plot(Timestamp,az)
# > write.csv(dataset,file="exported2.csv")



# > dataset <- read.csv(file.choose(),header=TRUE,sep=",")
# > View(dataset)
# > dataset[c('phi','lambda')] <- str_split_fixed(dataset$Position,',', 2)
# Error in str_split_fixed(dataset$Position, ",", 2) : 
#   could not find function "str_split_fixed"
# > library(stringr)
# > dataset[c('phi','lambda')] <- str_split_fixed(dataset$Position,',', 2)
# > dataset[c('phi')] <- as.numeric(dataset$phi)
# > dataset[c('lambda')] <- as.numeric(dataset$lambda)
# > class(dataset$lambda)

# > dataset[c('Altitude')] <- dataset$Altitude*0.3048+135.4
# > dataset[c('phi')] <- dataset$phi/180*pi
# > dataset[c('lambda')] <- dataset$lambda/180*pi

# dataset[c('X')] <- ((dataset$N+dataset$Altitude)*cos(dataset$Position1)*cos(dataset$Position2))
# dataset[c('Y')] <- ((dataset$N+dataset$Altitude)*cos(dataset$Position1)*sin(dataset$Position2))
# dataset[c('Z')] <- ((dataset$N*(1-e2)+dataset$Altitude)*sin(dataset$Position1))

# > x <- dataset$X[1]
# > y <- dataset$Y[1]
# > z <- dataset$Z[1]

# > dataset[c('X')] <- dataset$X-x
# > dataset[c('Y')] <- dataset$Y-y
# > dataset[c('Z')] <- dataset$Z-z
# > rm(x,y,z)

# > phi <- dataset$phi[1]
# > lambda <- dataset$lambda[1]
# > rneu <- matrix(c(-sin(phi)*cos(lamda),-sin(phi)*sin(lambda),cos(phi),-sin(lambda),cos(lambda),0,cos(phi)*cos(lambda),cos(phi)*sin(lambda),sin(phi)),ncol=3,nrow=3)
# Error in matrix(c(-sin(phi) * cos(lamda), -sin(phi) * sin(lambda), cos(phi),  : 
#   object 'lamda' not found
# > rneu <- matrix(c(-sin(phi)*cos(lambda),-sin(phi)*sin(lambda),cos(phi),-sin(lambda),cos(lambda),0,cos(phi)*cos(lambda),cos(phi)*sin(lambda),sin(phi)),ncol=3,nrow=3)

# > rm(lambda,phi)
# rneut <- t(rneu)

# > dataset[c('n')] <- dataset$X*rneut[1]+dataset$Y*rneut[4]+dataset$Z*rneut[7]
# > dataset[c('e')] <- dataset$X*rneut[2]+dataset$Y*rneut[5]+dataset$Z*rneut[8]
# > dataset[c('u')] <- dataset$X*rneut[3]+dataset$Y*rneut[6]+dataset$Z*rneut[9]

# > dataset[c('s')] <- sqrt(dataset$n*dataset$n+dataset$e*dataset$e+dataset$u*dataset$u)
# > dataset[c('az')] <- atan(dataset$e/dataset$n)
# > dataset[c('h')] <- asin(dataset$u/sqrt(dataset$n*dataset$n+dataset$e*dataset$e+dataset$u*dataset$u))

#  attach(dataset)
# > plot(Timestamp,s)
# > plot(Timestamp,az)
# > plot(Timestamp,h)
# > dataset[c('h')] <- arcsin(dataset$u/sqrt(dataset$n*dataset$n+dataset$e*dataset$e+dataset$u*dataset$u))
# Error in arcsin(dataset$u/sqrt(dataset$n * dataset$n + dataset$e * dataset$e +  : 
#   could not find function "arcsin"
# > dataset[c('h')] <- dataset$u/sqrt(dataset$n*dataset$n+dataset$e*dataset$e+dataset$u*dataset$u)
# > dataset[c('h')] <- asin(dataset$u/sqrt(dataset$n*dataset$n+dataset$e*dataset$e+dataset$u*dataset$u))
# > plot(Timestamp,az)
# > plot(Timestamp,h)
# > plot(Timestamp,s)
# > plot(Timestamp,Direction)
# > plot(Timestamp,Speed)
# > write.csv(dataset,file="exported.csv")

dataset <- read.csv(file.choose(),header=TRUE,sep=",")
View(dataset)

# install and load stringr to modify strings
install.packages("stringr", repos='http://cran.us.r-project.org')
library(stringr)

dataset[c('phi', 'lambda')] <- str_split_fixed(dataset$Position, ',', 2)
dataset[c('Altitude')] <- dataset$Altitude*0.3048+135.4

a <- 6378137
e2 <- 0.00669438002290

dataset[c('Position1')] <- as.numeric(dataset$Position1)
dataset[c('Position2')] <- as.numeric(dataset$Position2)
class(dataset$Position1)
class(dataset$Position2)

dataset[c('N')] <- (a/sqrt(1-e2*sin(dataset$Position1)*sin(dataset$Position1)))

dataset[c('X')] <- ((dataset$N+dataset$Altitude)*cos(dataset$Position1)*cos(dataset$Position2))
dataset[c('Y')] <- ((dataset$N+dataset$Altitude)*cos(dataset$Position1)*sin(dataset$Position2))
dataset[c('Z')] <- ((dataset$N*(1-e2)+dataset$Altitude)*sin(dataset$Position1))

# wspolrzedne lotniska
XL <- dataset$X[1]
YL <- dataset$Y[1]
ZL <- dataset$Z[1]

dataset[c('XSL')] <- (dataset$X-XL)
dataset[c('YSL')] <- (dataset$Y-YL)
dataset[c('ZSL')] <- (dataset$Z-ZL)

phiL <- dataset$Position1[1]
lamL <- dataset$Position2[1]

rNEU <- c(-sin(phiL)*cos(lamL),-sin(phiL)*sin(lamL),cos(phiL),-sin(lamL),cos(lamL),0,cos(phiL)*cos(lamL),cos(phiL)*sin(lamL),sin(phiL))
dim(rNEU) <- c(3,3)
rNEUt <- t(rNEU)

dataset[c('n')] <- (dataset$XSL*rNEUt[1]+dataset$YSL*rNEUt[2]+dataset$ZSL*rNEUt[3])
dataset[c('e')] <- (dataset$XSL*rNEUt[4]+dataset$YSL*rNEUt[5]+dataset$ZSL*rNEUt[6])
dataset[c('u')] <- (dataset$XSL*rNEUt[7]+dataset$YSL*rNEUt[8]+dataset$ZSL*rNEUt[9])

dataset[c('s')] <- sqrt(dataset$n*dataset$n+dataset$e*dataset$e+dataset$u*dataset$u)
dataset[c('az')] <- atan(dataset$e/dataset$n)
dataset[c('h')] <- asin(dataset$u/sqrt(dataset$n*dataset$n+dataset$e*dataset$e+dataset$u*dataset$u))