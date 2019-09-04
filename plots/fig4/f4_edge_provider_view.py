import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

#sorted increase by mean
# use prepare.sh script to generate these array
#for all
labels= ['UZ','ME','CG','IR','FJ','SV','BB','BW','KG','MM','KN','KZ','BQ','BY','TJ','HT','JM','PK','NI','MN','NP','VI','LT','TZ','TG','NZ','AM','VU','GH','HN','SD','MZ','AR','UG','UA','RW','LB','BD','PR','HR','CD','TR','AU','ZW','BR','LV','CN','CL','MT','CI','IN','AL','TN','RO','RU','MK','ID','KR','GT','NG','PA','FI','CY','EC','PE','PY','PT','TT','JP','MD','CR','GR','GE','KE','BA','BO','PL','TH','AF','CM','RS','BH','SA','BN','LS','UY','KH','EE','US','LA','SK','EG','HU','VN','LU','SI','MX','IQ','MY','BG','PH','DO','MA','IS','PS','CA','DZ','CO','QA','BT','DK','AZ','JO','TW','AO','CZ','ES','AE','BM','HK','ZA','IE','SE','IT','AT','KW','CW','NO','VE','IL','MU','FR','LK','DE','SG','BE','CH','GB','OM','GU','NA','MG','NL','LI','BZ','JE','GI']

def readfile(fn):
    f = []
    with open(fn,'r') as fi:
        reader = fi.readlines()
        for line in reader:
            s = line.split(';')
            m = float(s[2])
            if m > 0.5:  #removing some exceptional points
                f.append(m)
    return f

data = []
means = []
for i in range(len(labels)):
    fname = './data/'+labels[i]+'_avg1'
    c = readfile(fname)
    data.append(c)

# fig, axes = plt.subplots(1, 1)
fig, axes = plt.subplots(figsize=(16, 4))

#showing outliers
axes.boxplot(data, labels=labels,showmeans='True', sym='+', whis=[0.1, 99.9])
axes.set_title('')
axes.set_ylabel('MITM robustness metric')

for labl in axes.get_xticklabels():
    labl.set_rotation(90)
    labl.set_horizontalalignment("center")
    labl.set_fontsize(8)	
    labl.set_verticalalignment("top")

fig.savefig('f4_edge_provider_view.png')
