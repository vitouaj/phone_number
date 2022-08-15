import os
headlist = ['088',
            '097',
            '071',
            '031',
            '060',
            '066',
            '067',
            '068',
            '090',
    ]
def phNumGenerater():

    with open('metfone.txt', 'w') as f:
        for head in headlist:
            for tail in range(999999):
                tail = str(tail)
                num = head + tail.zfill(6) + '\n'
                f.write(num)

if __name__ == '__main__':
    phNumGenerater()
