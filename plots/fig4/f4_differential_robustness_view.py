import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

labels= ['UZ','ME','CG','IR','FJ','SV','BB','BW','KG','MM','KN','KZ','BQ','BY','TJ','HT','JM','PK','NI','MN','NP','VI','LT','TZ','TG','NZ','AM','VU','GH','HN','SD','MZ','AR','UG','UA','RW','LB','BD','PR','HR','CD','TR','AU','ZW','BR','LV','CN','CL','MT','CI','IN','AL','TN','RO','RU','MK','ID','KR','GT','NG','PA','FI','CY','EC','PE','PY','PT','TT','JP','MD','CR','GR','GE','KE','BA','BO','PL','TH','AF','CM','RS','BH','SA','BN','LS','UY','KH','EE','US','LA','SK','EG','HU','VN','LU','SI','MX','IQ','MY','BG','PH','DO','MA','IS','PS','CA','DZ','CO','QA','BT','DK','AZ','JO','TW','AO','CZ','ES','AE','BM','HK','ZA','IE','SE','IT','AT','KW','CW','NO','VE','IL','MU','FR','LK','DE','SG','BE','CH','GB','OM','GU','NA','MG','NL','LI','BZ','JE','GI']

def readfile(fn1, fn2):
    f1 = []
    f2 = []
    f3 = []
    with open(fn1,'r') as fi:
        reader = fi.readlines()
        for line in reader:
            s = line.split(';')
            m = float(s[2])
            if m > 0.5:  #removing some exceptional points
                f1.append(m)

    with open(fn2,'r') as fi:
        reader = fi.readlines()
        for line in reader:
            s = line.split(';')
            m = float(s[2])
            if m > 0.5:  #removing some exceptional points
                f2.append(m)

    for i in range(0,len(f1)):
	m = f1[i] - f2[i]
        f3.append(m)
	    	
    return f3

data = []
means = []
for i in range(len(labels)):
    fname1 = './data/'+labels[i]+'_avg1'
    fname2 = './data/'+labels[i]+'_avg2'
    c = readfile(fname1,fname2)
    data.append(c)

fig, axes = plt.subplots(figsize=(16, 4))

#showing outliers
bp = axes.boxplot(data, labels=labels,showmeans='True', sym='+', whis=[0.1, 99.9])
axes.set_title('')
axes.set_ylabel('MITM differential robustness')
#axes.xaxis.tick_top()

for labl in axes.get_xticklabels():
    labl.set_rotation(90)
    labl.set_horizontalalignment("center")
    labl.set_fontsize(8)	
    labl.set_verticalalignment("center")

fig.savefig('f4_differential_robustness_view.png')
