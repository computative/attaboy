library(mgcv)

################
data = read.table("../resources/20_2T0.txt",col.names=c("n","E"))
ns = as.numeric(names(table(data$n)))
tmp = rep(0,length(ns))
tmp2 = rep(0,length(ns))
target = data[data$n > 100000,]$E
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

library(tikzDevice)
tikz("/home/marius/Dokumenter/fys4150/attaboy/sampling.tex", width = 1.6*4, height = 1.6*3, pointsize=11)
par(mfrow=c(2,2))
par(ps=8, cex=1, cex.main=1.25, cex.lab=1.25, cex.sub=1, cex.axis=1.25, font.main=1)

par(mgp=c(2,0.5,0), mar=c(1.5, 3.3, 1, 1.3))
plot(ns,tmp, log = "x", xlab="",ylab = "Var($E$)", main = "",  xaxt = 'n')
axis(1, c(10,1000,100000) , c("", "" ,""))
N = ns[which( as.numeric( tmp2 ) > 0.05 )[1]]
lines( c(N,N), c(0,5000), lty=4, lwd=2)
text(6, 4300, "(a)", cex=1.25)
text(N + 150, 3400, "Sampling point", cex=1.25, srt=-90)

par(mgp=c(2,0.5,0), mar=c(1.5, 3.6, 1, 0.5))
hist(target,xlim=c(-800,-500), xlab = "$E$", ylab = "P($E$)", freq=F, ylim = c(0,0.015), main = "",  xaxt = 'n',  yaxt = 'n')
axis(1, c(-800,-750,-700,-650,-600,-550,-500) , c("", "" ,"" ,"" ,"" ,"" ,""))
axis(2, c(0, 0.005, 0.01, 0.015) , c("0\\%", "5\\%" ,"10\\%" ,"15\\%"))
text(-780, 0.014, "(c)", cex=1.25)

par(mgp=c(2,0.5,0), mar=c(3,3.3,0.1,1.3))
plot(ns,pred$fit, type="l", log = "x", ylim=c(0,1), xlab = "Iteration no $n$", ylab = "$p$-value", main = "")
lines( c(N,N), c(0,1), lty=4, lwd=2)
text(6, 0.93, "(b)", cex=1.25)


par(mgp=c(2,0.5,0), mar=c(3,3.6,0.1,0.5))
hist(data[data$n==N,]$E, xlim=c(-800,-500), xlab = "$E$", ylab = "P($E$)",freq = F, ylim = c(0,0.015), main = "",  yaxt = 'n')
axis(2, c(0, 0.005, 0.01, 0.015) , c("0\\%", "5\\%" ,"10\\%" ,"15\\%"))
text(-780, 0.014, "(d)", cex=1.25)

dev.off()
ns[which( as.numeric( tmp2 ) > 0.05 )[1]]
