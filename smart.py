import os
headlist = ['010',
            '015',
            '016',
            '069',
            '061',
            '070',
            '081',
            '086',
            '087',
            '093',
            '096',
            '098',
    ]
def phNumGenerater():

    with open('smart.txt', 'w') as f:
        for head in headlist:
            for tail in range(999999):
                tail = str(tail)
                num = head + tail.zfill(6) + '\n'
                f.write(num)

if __name__ == '__main__':
    phNumGenerater()
