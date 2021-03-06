library(biwavelet)

li_output_pops_long <- read.csv("~/Documents/phd files/habitat_loss_project/python_analysis_scripts/steady_state/test_files/lowIM/output_pops_long.csv", header=F)
li_pops = rowSums(li_output_pops_long)
li_pops = li_pops[1:50000]

output_pops_long <- read.csv("~/Documents/phd files/habitat_loss_project/python_analysis_scripts/steady_state/test_files/highIM/output_pops_long.csv", header=F)
hi_pops = rowSums(output_pops_long)

hi_pops = rowSums(output_pops_long)
hi_pops = rowSums(output_pops)
hi_pops = hi_pops[1:2000]

normal_series <- read.table("~/Documents/phd files/habitat_loss_project/python_analysis_scripts/steady_state/test_files/normal_series.csv", quote="\"")
ns_pops = normal_series[1:50000,]

random_walk <- read.table("~/Documents/phd files/habitat_loss_project/python_analysis_scripts/steady_state/test_files/random_walk.csv", quote="\"")
rw_pops = random_walk[1:50000,]
plot(rw_pops)

par(mfrow=c(3,1))
toll = FALSE
wvlt="dog"  ##paul, dog, morlet
wt1=wt(cbind(1:1000, hi_pops[49001:50000]), mother=wvlt)
wt2=wt(cbind(1:1000, rw_pops[49001:50000]), mother=wvlt)
wt3=wt(cbind(1:1000, ns_pops[49001:50000]), mother=wvlt)
plot(wt1, type="power.corr.norm", main="High IR", plot.sig =toll)
plot(wt2, type="power.corr.norm", main="Rand.walk", plot.sig =toll)
plot(wt3, type="power.corr.norm", main="Normal dist", plot.sig =toll)

wvlt="paul"  ##paul, dog, morlet
wt1=wt(cbind(1:10000, hi_pops[40001:50000]), mother=wvlt, s0=16, max.scale=1024)
wt2=wt(cbind(1:10000, rw_pops[40001:50000]), mother=wvlt, s0=16, max.scale=1024)
wt3=wt(cbind(1:10000, ns_pops[40001:50000]), mother=wvlt, s0=16, max.scale=1024)
plot(wt1, type="power.corr.norm", main="High IR", plot.sig =toll)
plot(wt2, type="power.corr.norm", main="Rand.walk", plot.sig =toll)
plot(wt3, type="power.corr.norm", main="Normal dist", plot.sig =toll)

wvlt="paul"  ##paul, dog, morlet
wt1=wt(cbind(1:50001, hi_pops), mother=wvlt, s0=16, max.scale=1024)
wt2=wt(cbind(1:50000, rw_pops), mother=wvlt, s0=16, max.scale=1024)
wt3=wt(cbind(1:50000, ns_pops), mother=wvlt, s0=16, max.scale=1024)
plot(wt1, type="power.corr.norm", main="High IR", plot.sig =toll)
plot(wt2, type="power.corr.norm", main="Rand.walk", plot.sig =toll)
plot(wt3, type="power.corr.norm", main="Normal dist", plot.sig =toll)


wt0=wt(cbind(1:50000, li_pops))
wt1=wt(cbind(1:50001, hi_pops), s0=4, max.scale=1024)
wt2=wt(cbind(1:50000, rw_pops) , s0=4, max.scale=1024)
wt3=wt(cbind(1:50000, ns_pops), s0=4, max.scale=1024)

par(mfrow=c(1,3))
toll = FALSE

plot(li_pops)


plot(wt0, type="power.corr.norm", main="Low IR", plot.sig =toll)
plot(wt1, type="power.corr.norm", main="High IR", plot.sig =toll)
plot(wt2, type="power.corr.norm", main="Rand.walk", plot.sig =toll)
plot(wt3, type="power.corr.norm", main="Normal dist", plot.sig =toll)

minY=0
maxY=1000
par(mfrow=c(1,1))
plot(1:length(output_pops[,sp]), output_pops[,sp], type="n", ylim=c(minY,maxY))
for (sp in 1:10){
lines(1:length(output_pops[,sp]), output_pops[,sp], col=sp)
}
plot(1:length(output_pops[,sp]), output_pops[,sp], type="n", ylim=c(minY,maxY))
for (sp in 11:20){
  lines(1:length(output_pops[,sp]), output_pops[,sp], col=sp, ylim=c(minY,maxY))
}
plot(1:length(output_pops[,sp]), output_pops[,sp], type="n", ylim=c(minY,maxY))
for (sp in 21:30){
  lines(1:length(output_pops[,sp]), output_pops[,sp], col=sp, ylim=c(minY,maxY))
}
plot(1:length(output_pops[,sp]), output_pops[,sp], type="n", ylim=c(minY,maxY))
for (sp in 31:40){
  lines(1:length(output_pops[,sp]), output_pops[,sp], col=sp, ylim=c(minY,maxY))
}
plot(1:length(output_pops[,sp]), output_pops[,sp], type="n", ylim=c(minY,maxY))
for (sp in 41:50){
  lines(1:length(output_pops[,sp]), output_pops[,sp], col=sp, ylim=c(minY,maxY))
}
plot(1:length(output_pops[,sp]), output_pops[,sp], type="n", ylim=c(minY,maxY))
for (sp in 51:60){
  lines(1:length(output_pops[,sp]), output_pops[,sp], col=sp, ylim=c(minY,maxY))
}


sp1 = output_pops_long$V20
sp2 = output_pops_long$V6
sp3 = output_pops_long$V59

par(mfrow=c(3,1))
toll = FALSE
wvlt="paul"  ##paul, dog, morlet
wt1=wt(cbind(1:4000, sp1[0:4000]), mother=wvlt, s0=16, max.scale=1024)
wt2=wt(cbind(1:4000, sp2[0:4000]), mother=wvlt, s0=16, max.scale=1024)
wt3=wt(cbind(1:4000, sp3[0:4000]), mother=wvlt, s0=16, max.scale=1024)
plot(wt1, type="power.corr.norm", main="Most abundant species", plot.sig =toll)
plot(wt2, type="power.corr.norm", main="Second species", plot.sig =toll)
plot(wt3, type="power.corr.norm", main="Third species", plot.sig =toll)



par(mfrow=c(3,1))
toll = FALSE
wvlt="paul"  ##paul, dog, morlet
wt1=wt(cbind(1:10000, sp1[40001:50000]), mother=wvlt, s0=16, max.scale=1024)
wt2=wt(cbind(1:10000, sp2[40001:50000]), mother=wvlt, s0=16, max.scale=1024)
wt3=wt(cbind(1:10000, sp3[40001:50000]), mother=wvlt, s0=16, max.scale=1024)
plot(wt1, type="power.corr.norm", main="Most abundant species", plot.sig =toll)
plot(wt2, type="power.corr.norm", main="Second species", plot.sig =toll)
plot(wt3, type="power.corr.norm", main="Third species", plot.sig =toll)


par(mfrow=c(3,1))
toll = FALSE
wvlt="paul"  ##paul, dog, morlet
wt1=wt(cbind(1:50001, sp1), mother=wvlt, s0=16, max.scale=1024)
wt2=wt(cbind(1:50001, sp2), mother=wvlt, s0=16, max.scale=1024)
wt3=wt(cbind(1:50001, sp3), mother=wvlt, s0=16, max.scale=1024)
plot(wt1, type="power.corr.norm", main="Most abundant species", plot.sig =toll)
plot(wt2, type="power.corr.norm", main="Second species", plot.sig =toll)
plot(wt3, type="power.corr.norm", main="Third species", plot.sig =toll)
