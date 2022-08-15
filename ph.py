import os
headlist = ['012',
        '011',
        '014',
        '017',
        '061',
        '076',
        '077',
        '078',
        '085',
        '089',
        '095',
        '092',
        '095',
        '099'
    ]
def phNumGenerater():

    with open('phone_012.txt', 'w') as f:
        for head in headlist:
            for tail in range(999999):
                tail = str(tail)
                num = head + tail.zfill(6) + '\n'
                f.write(num)

if __name__ == '__main__':
    phNumGenerater()