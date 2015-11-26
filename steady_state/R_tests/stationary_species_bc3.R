
library('fractal')
library('astsa')
library('locits')
library(tseries)

output_pops_long <- read.csv("~/Documents/phd files/habitat_loss_project/python_analysis_scripts/steady_state/test_files/highIM/output_pops_long.csv", header=F)

## looking at how the number of stationary species varies with window length:
winlens <- seq(1000,49000,by=wl)

wl = 1000

adf <- list()
kpss <- list()
for (t in seq(2000,50000,by=wl)){
  
  adf_stable = 0
  kpss_stable = 0
  
  for (s in seq(1,60)){ 
    sp = output_pops_long[[paste('V',s,sep='')]]
    hi_sb <- sp[(1000):(t)];
    
    ans <- adf.test(hi_sb);
    pv <- ans$p.value
    if (pv[[1]]<=0.05){adf_stable = adf_stable + 1}
    
    ans <- kpss.test(hi_sb);
    pv <- ans$p.value
    if (pv[[1]]>=0.05){kpss_stable = kpss_stable + 1}
  }
  
  adf[[length(adf)+1]] = adf_stable;
  kpss[[length(kpss)+1]] = kpss_stable;
  
}

output = cbind(winlens, adf, kpss)
#write.table(output, file = "sp1_stat_tests_v_length_hi_long.csv",row.names=FALSE, na="",col.names=FALSE, sep=",")
#write.table(output, file = "sp2_stat_tests_v_length_hi_long.csv",row.names=FALSE, na="",col.names=FALSE, sep=",")
#write.table(output, file = "sp3_stat_tests_v_length_hi_long.csv",row.names=FALSE, na="",col.names=FALSE, sep=",")
#write.table(output, file = "sp58_stat_tests_v_length_hi_long.csv",row.names=FALSE, na="",col.names=FALSE, sep=",")
#write.table(output, file = "sp59_stat_tests_v_length_hi_long.csv",row.names=FALSE, na="",col.names=FALSE, sep=",")
write.table(output, file = "sp60_stat_tests_v_length_hi_long.csv",row.names=FALSE, na="",col.names=FALSE, sep=",")

plot(1:length(output[,3]), output[,2],col='blue')
par(new=TRUE)
plot(1:length(output[,3]), output[,3], axes=FALSE, col='red')
