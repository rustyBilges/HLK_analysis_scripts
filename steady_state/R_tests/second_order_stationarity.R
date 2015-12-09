
# From Guy Nason : http://www.maths.bris.ac.uk/~guy/Research/LSTS/TOS.html

library('fractal')
library('astsa')
library('locits')
library(tseries)

output_pops_long <- read.csv("~/Documents/phd files/habitat_loss_project/python_analysis_scripts/steady_state/test_files/highIM/output_pops_long.csv", header=F)
hi = rowSums(output_pops_long)
normal_series <- read.table("~/Documents/phd files/habitat_loss_project/python_analysis_scripts/steady_state/test_files/normal_series.csv", quote="\"")
ns = normal_series[1:50000,]
random_walk <- read.table("~/Documents/phd files/habitat_loss_project/python_analysis_scripts/steady_state/test_files/random_walk.csv", quote="\"")
rw = random_walk[1:50000,]

st = 1000
en = 50000

### first loading all 3 series (hi,rw,ns) and cutting out transience so all are length 49001, then:
stationarity(hi[st:en])
stationarity(rw[st:en])
stationarity(ns)[st:en])
kpss.test(hi[st:en])
kpss.test(rw[st:en])
kpss.test(ns[st:en])
adf.test(hi[st:en])
adf.test(rw[st:en])
adf.test(ns[st:en])

## now looking at increasing window lengths for stationarity (forwards and backwards):
wl = 1000
psr <- list()
adf_p <- list()
adf_s <- list()
kpss_p <- list()
kpss_s <- list()
for (t in seq(2000,50000,by=wl)){
    
    #hi_sb <- hi[(1000):(t)];
    #hi_sb <- rw[(1000):(t)];
    hi_sb <- ns[(1000):(t)];
    #hi_sb <- hi[(49001-t):49001];
    
    ans <- stationarity(hi_sb);
    pv <- attr(ans,"pvals");
    psr[[length(psr)+1]] = pv[[1]];
    
    ans <- adf.test(hi_sb);
    pv <- ans$p.value
    st <- ans$statistic
    adf_p[[length(adf_p)+1]] = pv[[1]];
    adf_s[[length(adf_s)+1]] = st[[1]];
    
    ans <- kpss.test(hi_sb);
    pv <- ans$p.value
    st <- ans$statistic
    kpss_p[[length(kpss_p)+1]] = pv[[1]];
    kpss_s[[length(kpss_s)+1]] = st[[1]];
}

output = cbind(seq(1000,49000,by=wl), adf_s, adf_p, kpss_s, kpss_p)
#write.table(output, file = "stat_tests_v_length_hi_long.csv",row.names=FALSE, na="",col.names=FALSE, sep=",")
#write.table(output, file = "stat_tests_v_length_rw_long.csv",row.names=FALSE, na="",col.names=FALSE, sep=",")
write.table(output, file = "stat_tests_v_length_ns_long.csv",row.names=FALSE, na="",col.names=FALSE, sep=",")

plot(1:length(adf_s), adf_s)
plot(1:length(kpss_s), kpss_s)

plot(1:length(adf_p), adf_p)
plot(1:length(kpss_p), kpss_p)

########################################################################
## using the above to determine a fixed wondow length, then exploring this window length moving across the time series:
## take wl = 2000, then wl = 10000, then wl = 25000
#wl = 2000
wl = 3000
#wl = 10000
#wl = 25000
psr <- list()
adf_p <- list()
adf_s <- list()
kpss_p <- list()
kpss_s <- list()

win_cen <- list()
#for (t in seq(0,47000,by=1000)){  ## for use with wl=2000
for (t in seq(0,46000,by=1000)){  ## for use with wl=3000
#for (t in seq(0,39000,by=1000)){  ## for use with wl=10000
#for (t in seq(0,24000,by=1000)){  ## for use with wl=25000
  
  hi_sb <- hi[(1000+t):(1000+t+wl)];
  #hi_sb <- rw[(1000):(t)];
  #hi_sb <- ns[(1000):(t)];
  #hi_sb <- hi[(49001-t):49001];
  
  win_cen[[length(win_cen)+1]] = (2*t + wl)/2;
  
  ans <- stationarity(hi_sb);
  pv <- attr(ans,"pvals");
  psr[[length(psr)+1]] = pv[[1]];
  
  ans <- adf.test(hi_sb);
  pv <- ans$p.value
  st <- ans$statistic
  adf_p[[length(adf_p)+1]] = pv[[1]];
  adf_s[[length(adf_s)+1]] = st[[1]];
  
  ans <- kpss.test(hi_sb);
  pv <- ans$p.value
  st <- ans$statistic
  kpss_p[[length(kpss_p)+1]] = pv[[1]];
  kpss_s[[length(kpss_s)+1]] = st[[1]];
}

output = cbind(win_cen, adf_s, adf_p, kpss_s, kpss_p)
#write.table(output, file = "stat_tests_v_time_hi_wl2000.csv",row.names=FALSE, na="",col.names=FALSE, sep=",")
write.table(output, file = "stat_tests_v_time_hi_wl3000.csv",row.names=FALSE, na="",col.names=FALSE, sep=",")
#write.table(output, file = "stat_tests_v_time_hi_wl10000.csv",row.names=FALSE, na="",col.names=FALSE, sep=",")
#write.table(output, file = "stat_tests_v_time_hi_wl25000.csv",row.names=FALSE, na="",col.names=FALSE, sep=",")

########################################################################
## repeating above analysis for the three most abundant (and least abundant species)
## most abundant are 20,6,59
## least abundant are 58,3,2

sp1 = output_pops_long$V20
sp2 = output_pops_long$V6
sp3 = output_pops_long$V59

sp58 = output_pops_long$V2
sp59 = output_pops_long$V3
sp60 = output_pops_long$V58

st=0
en=10000
par(mfrow=c(2,1))
plot(1:length(sp1[st:en]), sp1[st:en], type="n")
lines(1:length(sp1[st:en]), sp1[st:en])
plot(1:length(sp2[st:en]), sp2[st:en], type="n")
lines(1:length(sp2[st:en]), sp2[st:en])

wl = 1000
psr <- list()
adf_p <- list()
adf_s <- list()
kpss_p <- list()
kpss_s <- list()
for (t in seq(2000,50000,by=wl)){
  
  #hi_sb <- sp1[(1000):(t)];
  #hi_sb <- sp2[(1000):(t)];
  #hi_sb <- sp3[(1000):(t)];
  #hi_sb <- sp58[(1000):(t)];
  #hi_sb <- sp59[(1000):(t)];
  hi_sb <- sp60[(1000):(t)];
  
  
  ans <- stationarity(hi_sb);
  pv <- attr(ans,"pvals");
  psr[[length(psr)+1]] = pv[[1]];
  
  ans <- adf.test(hi_sb);
  pv <- ans$p.value
  st <- ans$statistic
  adf_p[[length(adf_p)+1]] = pv[[1]];
  adf_s[[length(adf_s)+1]] = st[[1]];
  
  ans <- kpss.test(hi_sb);
  pv <- ans$p.value
  st <- ans$statistic
  kpss_p[[length(kpss_p)+1]] = pv[[1]];
  kpss_s[[length(kpss_s)+1]] = st[[1]];
}

output = cbind(seq(1000,49000,by=wl), adf_s, adf_p, kpss_s, kpss_p)
#write.table(output, file = "sp1_stat_tests_v_length_hi_long.csv",row.names=FALSE, na="",col.names=FALSE, sep=",")
#write.table(output, file = "sp2_stat_tests_v_length_hi_long.csv",row.names=FALSE, na="",col.names=FALSE, sep=",")
#write.table(output, file = "sp3_stat_tests_v_length_hi_long.csv",row.names=FALSE, na="",col.names=FALSE, sep=",")
#write.table(output, file = "sp58_stat_tests_v_length_hi_long.csv",row.names=FALSE, na="",col.names=FALSE, sep=",")
#write.table(output, file = "sp59_stat_tests_v_length_hi_long.csv",row.names=FALSE, na="",col.names=FALSE, sep=",")


## so far we do not implement the stationarity testing with a sliding window per species. Perhaps this would be informative


########################################################################
## repeating above analysis for each trophic level
species <- read.csv("~/Documents/phd files/habitat_loss_project/python_analysis_scripts/steady_state/test_files/highIM/output_species_long.csv", header=T)
names(species)
species$species[[60]]
species$init_tl

## aggregate time series by trophic level
tl0 <- rep(0,50001)
tl1 <- rep(0,50001)
tl2 <- rep(0,50001)
tl3 <- rep(0,50001)
for (i in seq(1,60)){
  nam = paste('V',species$species[[i]],sep='')
  
  tl = species$init_tl[[i]]
  if (tl==0){tl0 = tl0 + output_pops_long[[nam]]}
  if (tl==1){tl1 = tl1 + output_pops_long[[nam]]}
  if (tl==2){tl2 = tl2 + output_pops_long[[nam]]}
  if (tl==3){tl3 = tl3 + output_pops_long[[nam]]}
}

## plot to check trophic levels aggregated correctly
par(mfrow=c(1,1))
st = 0
en = 5000
plot(1:length(hi[st:en]), hi[st:en], type="n", ylim=range(c(0,40000)))
lines(1:length(hi[st:en]), hi[st:en])
lines(1:length(tl0[st:en]), tl0[st:en], col='green')
lines(1:length(tl1[st:en]), tl1[st:en], col='yellow')
lines(1:length(tl1[st:en]), tl2[st:en], col='blue')
lines(1:length(tl1[st:en]), tl3[st:en], col='red')

## phase space??
st=1000
en = 50000
off = 500
plot(hi[st:en], hi[(st+off):(en+off)],type='l')

plot(tl0[st:en], tl1[st:en])
library(scatterplot3d)
st = 1000
en = 50000
scatterplot3d(tl0[st:en], tl1[st:en], tl2[st:en], type='l')


wl = 1000
psr <- list()
adf_p <- list()
adf_s <- list()
kpss_p <- list()
kpss_s <- list()
for (t in seq(2000,50000,by=wl)){
  
  #hi_sb <- tl0[(1000):(t)];
  #hi_sb <- tl1[(1000):(t)];
  #hi_sb <- tl2[(1000):(t)];
  hi_sb <- tl3[(1000):(t)];
  
  ans <- stationarity(hi_sb);
  pv <- attr(ans,"pvals");
  psr[[length(psr)+1]] = pv[[1]];
  
  ans <- adf.test(hi_sb);
  pv <- ans$p.value
  st <- ans$statistic
  adf_p[[length(adf_p)+1]] = pv[[1]];
  adf_s[[length(adf_s)+1]] = st[[1]];
  
  ans <- kpss.test(hi_sb);
  pv <- ans$p.value
  st <- ans$statistic
  kpss_p[[length(kpss_p)+1]] = pv[[1]];
  kpss_s[[length(kpss_s)+1]] = st[[1]];
}

output = cbind(seq(1000,49000,by=wl), adf_s, adf_p, kpss_s, kpss_p)
#write.table(output, file = "tl0_stat_tests_v_length_hi_long.csv",row.names=FALSE, na="",col.names=FALSE, sep=",")
#write.table(output, file = "tl1_stat_tests_v_length_hi_long.csv",row.names=FALSE, na="",col.names=FALSE, sep=",")
#write.table(output, file = "tl2_stat_tests_v_length_hi_long.csv",row.names=FALSE, na="",col.names=FALSE, sep=",")
write.table(output, file = "tl3_stat_tests_v_length_hi_long.csv",row.names=FALSE, na="",col.names=FALSE, sep=",")

###############################################################################
## now for moving window analysis by trophic length: DO ONE WINDOW LENGTH BECAUSE FOUR TLS TO COMPARE
## take wl = 2000, then wl = 10000, then wl = 25000
#wl = 2000
#wl = 3000
wl = 10000
#wl = 25000
psr <- list()
adf_p <- list()
adf_s <- list()
kpss_p <- list()
kpss_s <- list()

win_cen <- list()
#for (t in seq(0,47000,by=1000)){  ## for use with wl=2000
#for (t in seq(0,46000,by=1000)){  ## for use with wl=3000
for (t in seq(0,39000,by=1000)){  ## for use with wl=10000
  #for (t in seq(0,24000,by=1000)){  ## for use with wl=25000
  
  hi_sb <- tl0[(1000+t):(1000+t+wl)];
  #hi_sb <- tl1[(1000+t):(1000+t+wl)];
  #hi_sb <- tl2[(1000+t):(1000+t+wl)];
  #hi_sb <- tl3[(1000+t):(1000+t+wl)];
  
  win_cen[[length(win_cen)+1]] = (2*t + wl)/2;
  
  ans <- stationarity(hi_sb);
  pv <- attr(ans,"pvals");
  psr[[length(psr)+1]] = pv[[1]];
  
  ans <- adf.test(hi_sb);
  pv <- ans$p.value
  st <- ans$statistic
  adf_p[[length(adf_p)+1]] = pv[[1]];
  adf_s[[length(adf_s)+1]] = st[[1]];
  
  ans <- kpss.test(hi_sb);
  pv <- ans$p.value
  st <- ans$statistic
  kpss_p[[length(kpss_p)+1]] = pv[[1]];
  kpss_s[[length(kpss_s)+1]] = st[[1]];
}

output = cbind(win_cen, adf_s, adf_p, kpss_s, kpss_p)
#write.table(output, file = "tl0_stat_tests_v_time_hi_wl3000.csv",row.names=FALSE, na="",col.names=FALSE, sep=",")
#write.table(output, file = "tl1_stat_tests_v_time_hi_wl3000.csv",row.names=FALSE, na="",col.names=FALSE, sep=",")
#write.table(output, file = "tl2_stat_tests_v_time_hi_wl3000.csv",row.names=FALSE, na="",col.names=FALSE, sep=",")
#write.table(output, file = "tl3_stat_tests_v_time_hi_wl3000.csv",row.names=FALSE, na="",col.names=FALSE, sep=",")

write.table(output, file = "tl0_stat_tests_v_time_hi_wl10000.csv",row.names=FALSE, na="",col.names=FALSE, sep=",")
#write.table(output, file = "tl1_stat_tests_v_time_hi_wl10000.csv",row.names=FALSE, na="",col.names=FALSE, sep=",")
#write.table(output, file = "tl2_stat_tests_v_time_hi_wl10000.csv",row.names=FALSE, na="",col.names=FALSE, sep=",")
#write.table(output, file = "tl3_stat_tests_v_time_hi_wl10000.csv",row.names=FALSE, na="",col.names=FALSE, sep=",")


########################################################################
dat = read.csv("output_pops_long.csv", header = FALSE)

biomass = rowSums(dat)
biomass_no_transience = biomass[1000:50000]
mean(biomass_no_transience)
sqrt(var(biomass_no_transience))

ts.plot(biomass[1000:50000])

td = biomass[33617:50000]
td = biomass[2000:5000]
stationarity(td)
ts.plot(td)
length(td)
ans <- hwtos2(td)
ans

plot(ans)


st = 2000
en = 5000
adf.test(sp1[st:en])
adf.test(sp2[st:en])
adf.test(sp3[st:en])