import matplotlib.pyplot as plt

labels = ['fully internal',
        'continental-oriented',
        'sea-oriented',
        'inter-continental cables',
        'cross-ocean']

subdata = dict()
for reg in labels:
    subdata[reg] = []

def readfile(fn):    
    f = []
    with open(fn,'r') as fi:
        reader = fi.readlines()
        for line in reader:    
            s = line.split(';')
            m = float(s[2])
            if m > 0:
                f.append(m)
    avg = sum(f) / float(len(f))
    return avg

ctry = dict()


with open('country_classifications.dat','r') as fi:
    reader = fi.readlines()
    for line in reader:
        s = line.split("\t")
        if (s[1] in labels):
            if(s[0] not in ctry):
                ctry[s[0]] = []
            ctry[s[0]].append(s[1])
        else:
            print('Error',s)

for country in ctry:
    fname = './data/'+country+'_avg2'
    avg = readfile(fname)
    for reg in ctry[country]:    
        subdata[reg].append(avg)

data = []
for reg in labels:
    data.append(subdata[reg])

fig, axes = plt.subplots(1, 1)

axes.boxplot(data, labels=labels, showmeans=True,widths=(0.3,0.3,0.3,0.3,0.3),sym='+' ) 
plt.ylim(0.9,1.6)
axes.set_title('')
axes.set_ylabel('MITM robustness metric')

axes.tick_params(axis='x', labelsize=10)
axes.set_aspect(3.9) 


for labl in axes.get_xmajorticklabels():
    labl.set_rotation(40)
    labl.set_horizontalalignment("right")

plt.subplots_adjust(bottom=0.35)

fig.savefig('f6_b.png')
