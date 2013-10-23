# -*- encoding: utf-8 -*-

PCT = 14.99/100
YEARS = 3
m = 12   # number of payments in year


SUM = 1000000
extra = 0  # extra payment each month

K = (PCT/m)/(1-(1+(PCT/m))**(-1*YEARS*m))  # annuity quotient

def iterate():
  global SUM, K, YEARS, m, extra
  remainder = SUM
  totals = {'percents': 0, 'payments': 0}
  print('{:<10}\t{:<10}\t{:<10}\t{:<10}\t{:<10}'.format('MONTH', 'PERCENT', 'PAYMENT',
                                                        'REMAINDER', 'EXTRA'))
  for i in range(YEARS*m):
    percent = remainder*PCT/m
    remainder += percent    
    
    payment = min(K*SUM + extra, remainder)
    remainder = max(0, remainder - payment)
    totals['percents'] += percent
    totals['payments'] += payment
    print('{:<10}\t{:<10.2f}\t{:<10.2f}\t{:<10.2f}\t{:<10.2f}'.format(i+1, percent, payment,
                                                                      remainder, extra))
    if remainder == 0: break
  print('-'*80)
  print('{:<10}\t{:<10.2f}\t{:<10.2f}'.format('TOTAL', totals['percents'],
                                              totals['payments']))

iterate()
