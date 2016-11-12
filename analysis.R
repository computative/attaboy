data7 = read.table("data7.txt")
data2 = read.table("data2.txt")
data = read.table("data.txt")
data = rbind(data2,data,data7)
data = read.table("bigmatrixdata.txt")


#j beta 1,2.4  k matrix 0,1
#jk
#00,01,10,11

# T = 1, ordered matrix
# E
plot(data$V1,data$V2 ,log="x")
# M
plot(data$V1,data$V3 ,log="x")
# accept
plot(data$V1,data$V4 ,log="x")

# T = 1, random matrix
# E
plot(data$V5,data$V6 ,log="x")
# M
plot(data$V5,data$V7 ,log="x")
# accept
plot(data$V5,data$V8 ,log="x")

# T = 2.4, ordered matrix
# E

plot(data$V9,data$V10 ,log="x")
# M
plot(data$V9,data$V11 ,log="x")
# accept
plot(data$V9,data$V12 ,log="x")

# T = 2.4, random matrix
# E
plot(data$V13,data$V14 ,log="x")
# M
plot(data$V13,data$V15 ,log="x")
# accept
plot(data$V13,data$V16 ,log="x")



variance = read.table("variance_temp2.400000.txt")




A = variance$V1[sample(1:90000,size=8,replace=T)]
X = table(cut(A, c(seq(min(A,B), max(A,B), (max(A,B) - min(A,B))/4))))
O = table(cut(variance$V1, c(seq(min(A), max(A), (max(A) - min(A))/4))))
P = O/sum(O)
chisq.test(X, p=P)
