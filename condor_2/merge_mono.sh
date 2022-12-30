
nof_file=0

resourcedir=/eos/cms/store/group/dpg_hgcal/comm_hgcal/geomval/ntuples
outdir=$resourcedir/merged
for PU in 00 100 200
do
    for pT in 25 50 100 150 200
    do
        for eta in 1.7 1.95 2.2 2.45 2.7
        do
	    indir=$resourcedir/muplus_PU_${PU}_pT_${pT}_eta_${eta}
	    pre_eta=`echo $eta | cut -d '.' -f 1`
	    post_eta=`echo $eta | cut -d '.' -f 2`
	    outfile=$outdir/Raw_Hits_Mono_Mu_Plus_PU_${PU}_Pt_${pT}_Eta_${pre_eta}pt${post_eta}.root
	    unset array
	    declare -a array
	    for ifile in `find $indir -name "ml_ntuplemuplus_PU_${PU}_pT_${pT}_eta_${eta}*.root"`
	    do
		array[$nof_file]=$ifile
		nof_file=$[$nof_file+1]
	    done
	    echo files are ${array[@]}
	    echo Output file name $outfile
	    if [ -f $outfile ] ; then
		rm $outfile
	    fi
            hadd $outfile ${array[@]}
            sleep 10
        done
    done
done