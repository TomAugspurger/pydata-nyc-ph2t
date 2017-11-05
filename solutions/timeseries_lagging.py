lagged = pd.concat([y_prime.shift(i) for i in range(9)],
                   axis='columns',
                   keys=['y', 'L1', 'L2', 'L3', 'L4',
                         'L5', 'L6', 'L7', 'L8'])
lagged