import scipy.stats

#Defining Variables
dolM=float(input('Enter mean of dolomite'))
shaM=float(input('Enter mean of shale'))
dolC=float(input('Enter number of dolomite'))
shaC=float(input('Enter number of shale'))
dolSD=float(input('Enter standard deviation of dolomite'))
shaSD=float(input('Enter standard deviation of shale'))

#Futhermore.....
Tcore=771
pd=dolC/Tcore
ps=shaC/Tcore
pdg=1-scipy.stats.norm(dolM, dolSD).cdf(60)
psg=1-scipy.stats.norm(shaM, shaSD).cdf(60)

#A BREAK DOWN
one=pd*pdg
two=(pd*pdg)+(ps*psg)
twwo=one/two

#OR
ogsensei=(pd*pdg)/((pd*pdg)+(ps*psg))

if ogsensei>=0.5:
    print('value is',  ogsensei)
    print('value is',  twwo)
    print('The Interval is dolomite')
else:
    print('value is', ogsensei)
    print('value is',  twwo)
    print('The interval is shale')
