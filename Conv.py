def arange(start,end,step):
    return [(1/step)*i for i in range(start,end)]

def conv(xn,hn):
    data = []
    conv = []
    for i in range(len(hn)+len(xn)-1):
        try:
            if len(hn)==len(data):
                data.pop(-1)
            data.insert(0,xn.pop(0))
        except:
            data.insert(0,0)
        conv.append(sum([data[i]*hn[i] for i in range(len(data))]))
    return conv

def conv2(xn,hn):
    conv = []
    data = []
    for i in range(len(hn)+len(xn)-1):
        try:
            if len(hn)==len(data):
                data.pop(-1)
            data.insert(0,xn.pop(0))
        except:
            data.insert(0,0)
        conv.append(sum([hn[i] if data[i]!=0 else 0 for i in range(len(data))]))
    return conv


if __name__ == '__main__':
    import matplotlib.pyplot as plt
    from nptdms import TdmsFile,TdmsWriter
    import random
    import time

    tdms = TdmsFile.read('Coef8.tdms')

    chan_data = tdms["A"]['Mask']

    listconv = list(map(int,chan_data[:]))
    hn = [-1 if listconv[i]==0 else 1 for i in range(len(listconv))]

    xn = [random.randint(0,1) for i in range(0,400000)]

    xn[1000:1000+len(hn)],xn[90000:90000+len(hn)] = hn,hn

    range_ = arange(0,400255,400000)
    hn = hn[::-1]

    start = time.time()
    a = conv(xn,hn)
    end = time.time()

    print(end-start)

    # start = time.time()

    # b = conv2(xn,listconv)

    # end = time.time()

    # print(end-start)

    plt.plot(range_,a)

    # plt.plot(range_,b)
    plt.show()