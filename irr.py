"""
  IRR calculation
"""

__author__ = 'Pavel Popov'

import datetime

THRESHOLD = 1e-8
NUM_ITER = 100


def to_date(x):
  """Returns datetime from string in DD.MM.YYYY format"""  
  day, month, year = map(int, x.split('.'))
  return datetime.datetime(year=year, month=month, day=day)


def dd(d1, d2):
  """Returns difference in days between d1 and d2
     in part of year (365 days):
       (d2 - d1) / 365
  """
  diff = d2 - d1
  return diff.days / 365.0


def irr(p, d, g):
  """Returns inner rate of return.
     p - list of payments
     d - list of dates
     g - guess of rate
  """  
  return sum([p[i] / pow(1 + g, dd(d[0], d[i])) for i in range(len(p))])


def file2data(filename):
  """Return data to irr calculation from datafile.
     Assumes that file is tab-separated with header in
     first line and ends with empty line.
     Line ends with \n.
  """
  f = open(filename,'r')
  payments = []
  dates = []
  data = filter(lambda x: x != [''],
                map(lambda x: x.strip('\n').split('\t'), f.readlines()))
  for row in data:
    dates.append(row[0])
    payments.append(row[1])

  return map(to_date, dates[1:]), map(float, payments[1:])


def iteration(p, d, g1, g2, n=None):
  """Performs iteration in irr calculation
     via bisection of interval [g1, g2].
     Iterates why difference became smaller then THRESHOLD
     or when NUM_ITER occured.
     Returns calculated irr value.
  """
  n = 0 if n is None else n
  g = (g1 + g2)/2.0
  r = irr(p, d, g)  
  print('step %d: %10.10f' % (n, r))  
  if abs(r) < THRESHOLD or n >= NUM_ITER:
    return g
  else:
    g1 = g if r > 0 else g1
    g2 = g if r < 0 else g2
    print('new guess: %0.20f' % g)
    g = iteration(p, d, g1, g2, n+1)
    return g
  

if __name__ == "__main__":
  d, p = file2data('irr.dat')
  r = iteration(p, d, 0, 1)
  print('Result is %0.20f' % r)
