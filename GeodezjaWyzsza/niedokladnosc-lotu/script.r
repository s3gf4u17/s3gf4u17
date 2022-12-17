# punkt poczatkowy P1
# phi: 53 deg
# lam: 22 deg

# linie geodezyjne (dl, A)
# 20 km, 0 deg
# 35 km, 90 deg
# 20 km, 180 deg

P1 <- c(53,22)
a <- 6378137
e2 <- 0.00669438002290

# glowne promienie krzywizny M i N w punkcie wyjsciowym P1
M1 <- (a*(1-e2))/sqrt((1-e2*sin(P1[1])^2)^3)
N1 <- a/sqrt(1-e2*sin(P1[1])^2)

# pierwsze przyblizenie przyrostu szerokosci i azymutu
dphi <- 20000*cos(0)/M1
dAzm <- 20000*sin(0)*tan(P1[1])/N1

# szerokosc i azymut w punkcie srodkowym (m)
mphi <- P1[1]+0.5*dphi
mAzm <- 0+0.5*dAzm

# glowne promienie krzywizny w punkcie m
M1 <- (a*(1-e2))/sqrt((1-e2*sin(mphi)^2)^3)
N1 <- a/sqrt(1-e2*sin(mphi)^2)

# ostateczne przyrosty szerokosci, dlugosci i azymutu
dphim <- 20000*cos(mAzm)/M1
dlamm <- 20000*sin(mAzm)/N1/cos(mphi)
dAzmm <- 20000*sin(mAzm)*tan(mphi)/N1

# wspolrzedne konca odcinka oraz azymut na koncu odcinka linii geodezyjnej
final_phi <- P1[1] +dphim
final_lam <- P1[2] +dlamm
final_Azm <- 0 +dAzmm

response <- c(P1[1],P1[2],final_phi,final_lam)
View(response)
write.csv(response,file="exported.csv")