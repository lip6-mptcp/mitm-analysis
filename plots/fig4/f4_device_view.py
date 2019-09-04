import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# sorted increasing average
# use prepare.sh to generate these array
labels = ['UZ','ME','CG','IR','FJ','MN','SV','MM','BW','PK','BB','KG','BY','LT','KZ','KR','BQ','KN','TZ','CN','LB','NZ','AM','NI','NP','TR','TG','JM','HR','TJ','LV','HT','UA','AU','MZ','SD','GH','VU','BD','AR','CL','MT','QA','CY','HN','UG','VI','RO','BR','MD','CD','IN','TH','AE','PR','CI','SA','FI','PT','GR','ID','ZW','AZ','RU','NG','TN','BA','GE','GT','PY','MK','PE','BH','EE','JP','KE','RS','SI','US','VN','CM','AL','EC','IQ','PA','TT','PH','DK','MY','TW','BO','RW','HU','BG','CO','PL','KH','CR','SK','IS','UY','MX','HK','JO','BN','EG','ZA','LS','CA','ES','PS','IL','SE','LU','DO','IT','AT','DE','LA','AO','LK','KW','IE','CZ','NO','MA','SG','AF','MU','BE','BT','FR','BM','OM','VE','GB','DZ','CW','CH','GU','NL','NA','MG','BZ','LI','GI','JE']

def readfile(fn):
    f = []
    with open(fn,'r') as fi:
        reader = fi.readlines()
        for line in reader:
            s = line.split(';')
            m = float(s[2])
            if m > 0.8: #removing some exceptional points
                f.append(m)
    return f

data = []
means = []
for i in range(len(labels)):
    fname = './data/'+labels[i]+'_avg2'
    c = readfile(fname)

    data.append(c)


#fig, axes = plt.subplots(1, 1)
fig, axes = plt.subplots(figsize=(16, 4))

#showing outliers
axes.boxplot(data, labels=labels, showmeans=True, sym='+', whis=[0.1, 99.9])

# plt.ylim([1,2])
axes.set_title('')
axes.set_ylabel('MITM robustness metric')
#top
#axes.xaxis.tick_top()

for labl in axes.get_xticklabels():
    labl.set_rotation(90)
    labl.set_horizontalalignment("center")
    labl.set_fontsize(8)
    labl.set_verticalalignment("top")

#all
fig.savefig('f4_device_view.png')
