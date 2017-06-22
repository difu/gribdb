root=ftp://ftp-cdc.dwd.de/pub/REA/COSMO_REA6/hourly/2D
for var in PS T_2M {U,V}_10M; do
  wget -N $root/"$var"/"$var".2D.199501.grb.bz2 &
done
wait
for f in *bz2; do
  bzip2 -d $f &
done
wait
