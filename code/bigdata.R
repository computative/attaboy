data = read.table("../resources/bigdata.txt",col.names=c("dim","temp","E","M","Cv","X"))
library(mgcv)
dims = c(20,60,100,140)
par(mfrow=c(1,1))

M = matrix(rep(0,201*4*4+201),ncol = 17, nrow = 201)
#Xs = matrix(rep(0,201*4),ncol = 4, nrow=201)
for (i in 4:1) {
  X = data[data$dim==dims[i],]$X
  T = data[data$dim==dims[i],]$temp
  fit = gam(X ~ s(T, fx=FALSE, k=20, bs="cr") )
  Ts = seq(2,2.4,0.002)
  pred = predict(fit, newdata=data.frame("T"=Ts), se=TRUE, type="response")
  #Xs[,i] = as.numeric(pred$fit)
  M[,1] = Ts
  M[,i+1] = as.numeric(pred$fit)
  if (i == 4) {plot(Ts, pred$fit, type ="l")}
  else{lines(Ts, pred$fit, type ="l")}
}

#Cvs = matrix(rep(0,201*4),ncol = 4, nrow=201)
for (i in 4:1) {
  X = data[data$dim==dims[i],]$Cv
  T = data[data$dim==dims[i],]$temp
  fit = gam(X ~ s(T, fx=FALSE, k=20, bs="cr") )
  Ts = seq(2,2.4,0.002)
  pred = predict(fit, newdata=data.frame("T"=Ts), se=TRUE, type="response")
  M[,4+i+1] = as.numeric(pred$fit)
  if (i == 4) {plot(Ts, pred$fit, type ="l")}
  else{lines(Ts, pred$fit, type ="l")}
}

#Ms = matrix(rep(0,201*4),ncol = 4, nrow=201)
for (i in 4:1) {
  X = data[data$dim==dims[i],]$M
  T = data[data$dim==dims[i],]$temp
  fit = gam(X ~ s(T, fx=FALSE, k=20, bs="cr") )
  Ts = seq(2,2.4,0.002)
  pred = predict(fit, newdata=data.frame("T"=Ts), se=TRUE, type="response")
  M[,8+i+1] = as.numeric(pred$fit)
  if (i == 4) {plot(Ts, pred$fit, type ="l")}
  else{lines(Ts, pred$fit, type ="l")}
}


#Es = matrix(rep(0,201*4),ncol = 4, nrow=201)
for (i in 4:1) {
  X = data[data$dim==dims[i],]$E
  T = data[data$dim==dims[i],]$temp
  fit = gam(X ~ s(T, fx=FALSE, k=20, bs="cr") )
  Ts = seq(2,2.4,0.002)
  pred = predict(fit, newdata=data.frame("T"=Ts), se=TRUE, type="response")
  M[,12+i+1] = as.numeric(pred$fit)
  if (i == 4) {plot(Ts, pred$fit, type ="l")}
  else{lines(Ts, pred$fit, type ="l")}
}

write.table(M, file="biggdat.txt", row.names=FALSE, col.names=FALSE)
