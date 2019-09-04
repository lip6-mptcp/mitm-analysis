import matplotlib.pyplot as plt

labels = [  'Central Asia',
            'Australia and New Zealand',
            'Eastern Asia',
            'Southern Asia',
            'Latin America and the Caribbean',
            'Sub-Saharan Africa',
            'Southern Europe',
            'Eastern Europe',
            'Western Asia',
            'South-eastern Asia',
            'Northern Europe',
            'Northern Africa',
            'Northern America',
            'Western Europe']

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

with open('country_region.dat','r') as fi:
    reader = fi.readlines()
    for line in reader:
        s = line.split("\t")
        if (s[1] in labels):
            ctry[s[0]] = s[1]

for country in ctry:
    fname = './data/'+country+'_avg2'
    avg = readfile(fname)
    subdata[ctry[country]].append(avg)

data = []
for reg in labels:
    data.append(subdata[reg])

fig, axes = plt.subplots(1, 1)

axes.boxplot(data, labels=labels, showmeans=True,widths=(0.3,0.3,0.3,0.3,0.3,0.3,0.3,0.3,0.3,0.3,0.3,0.3,0.3,0.3),sym='+' ) 
plt.ylim(0.9,1.6,0.1)
axes.set_title('')
axes.set_ylabel('MITM robustness metric')

axes.tick_params(axis='x', labelsize=10)
axes.set_aspect(9.9) 


for labl in axes.get_xmajorticklabels():
    labl.set_rotation(40)
    labl.set_horizontalalignment("right")

plt.subplots_adjust(bottom=0.35)

fig.savefig('f6_a.png')
