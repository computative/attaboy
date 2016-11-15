library(mgcv)

t = "2T4"
################
data = read.table(paste("../resources/S20_", t, ".txt", sep=""),col.names=c("n","E"))
ns = as.numeric(names(table(data$n)))
tmp = rep(0,length(ns))
tmp2 = rep(0,length(ns))
target = data[data$n > 100000,]$E
print(var(target))
print(mean(target))
g = 10
cats = seq(min(target) , max(target), (max(target) - min(target) )/g )
groups = cut(target, breaks = g)
P = as.numeric(table( groups ))/length(target)
i = 1
for (n in ns) {
  X = as.numeric(table(cut(data[data$n==n,]$E, breaks = cats)))
  if(sum(X) == 0) {X[1] = 1}
  tmp[i] = var(data[data$n == n,]$E)
  tmp2[i] = chisq.test(x=X,p=P)$p.value
  i = i + 1
}
fit = gam(tmp2 ~ s(ns, fx=FALSE, k=-1, bs="cr"), family = binomial(link="logit") )
pred = predict(fit, newdata=data.frame("ns"=ns), se=TRUE, type="response")
plot(ns,tmp, log = "x")
plot(ns,tmp2, log = "x")
lines(ns,pred$fit, type="l")
plot(ns,pred$fit, type="l", log ="x", ylim = c(0,1))
ns[which( as.numeric( tmp2 ) > 0.05 )[1]]


################
data = read.table(paste("../resources/S60_", t, ".txt", sep=""),col.names=c("n","E"))
ns = as.numeric(names(table(data$n)))
tmp = rep(0,length(ns))
tmp2 = rep(0,length(ns))
target = data[data$n > 100000,]$E
print(var(target))
print(mean(target))
g = 10
cats = seq(min(target) , max(target), (max(target) - min(target) )/g )
groups = cut(target, breaks = g)
P = as.numeric(table( groups ))/length(target)
i = 1
for (n in ns) {
  X = as.numeric(table(cut(data[data$n==n,]$E, breaks = cats)))
  if(sum(X) == 0) {X[1] = 1}
  tmp[i] = var(data[data$n == n,]$E)
  tmp2[i] = chisq.test(x=X,p=P)$p.value
  i = i + 1
}
fit = gam(tmp2 ~ s(ns, fx=FALSE, k=-1, bs="cr"), family = binomial(link="logit") )
pred = predict(fit, newdata=data.frame("ns"=ns), se=TRUE, type="response")
plot(ns,tmp, log = "x")
plot(ns,tmp2, log = "x")
lines(ns,pred$fit, type="l")
plot(ns,pred$fit, type="l", log ="x", ylim = c(0,1))
ns[which( as.numeric( tmp2 ) > 0.05 )[1]]


#################


data = read.table(paste("../resources/S100_", t, ".txt", sep=""),col.names=c("n","E"))
ns = as.numeric(names(table(data$n)))
tmp = rep(0,length(ns))
tmp2 = rep(0,length(ns))
target = data[data$n > 100000,]$E
print(var(target))
print(mean(target))
g = 10
cats = seq(min(target) , max(target), (max(target) - min(target) )/g )
groups = cut(target, breaks = g)
P = as.numeric(table( groups ))/length(target)
i = 1
for (n in ns) {
  X = as.numeric(table(cut(data[data$n==n,]$E, breaks = cats)))
  if(sum(X) == 0) {X[1] = 1}
  tmp[i] = var(data[data$n == n,]$E)
  tmp2[i] = chisq.test(x=X,p=P)$p.value
  i = i + 1
}

fit = gam(tmp2 ~ s(ns, fx=FALSE, k=-1, bs="cr"), family = binomial(link = "logit"))
pred = predict(fit, newdata=data.frame("ns"=ns), se=TRUE, type="response")
plot(ns,tmp, log = "x")
plot(ns,tmp2, log = "x")
lines(ns,pred$fit, type="l")
plot(ns,pred$fit, type="l", log ="x", ylim = c(0,1))
ns[which( as.numeric( tmp2 ) > 0.05 )[1]]

##############
  
    data = read.table(paste("../resources/S140_", t, ".txt", sep=""),col.names=c("n","E"))
    ns = as.numeric(names(table(data$n)))
    tmp = rep(0,length(ns))
    tmp2 = rep(0,length(ns))
    target = data[data$n > 100000,]$E
    print(var(target))
    print(mean(target))
    g = 10
    cats = seq(min(target) , max(target), (max(target) - min(target) )/g )
    groups = cut(target, breaks = g)
    P = as.numeric(table( groups ))/length(target)
    i = 1
    for (n in ns) {
      X = as.numeric(table(cut(data[data$n==n,]$E, breaks = cats)))
      if(sum(X) == 0) {X[1] = 1}
      tmp[i] = var(data[data$n == n,]$E)
      tmp2[i] = chisq.test(x=X,p=P)$p.value
      i = i + 1
    }
    
    fit = gam(tmp2 ~ s(ns, fx=FALSE, k=-1, bs="cr"), family = binomial(link = "logit"))
    pred = predict(fit, newdata=data.frame("ns"=ns), se=TRUE, type="response")
    plot(ns,tmp, log = "x")
    plot(ns,tmp2, log = "x")
    lines(ns,pred$fit, type="l")
    plot(ns,pred$fit, type="l", log ="x", ylim = c(0,1))
    ns[which( as.numeric( tmp2 ) > 0.05 )[1]]

