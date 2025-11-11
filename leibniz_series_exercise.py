def approximate_pi(n_terms):
  l_series=[]
  for n in range(n_terms):
    term=((-1)**n)/(2*n+1)
    l_series.append(term)
  l_series_sum=sum(l_series)
  l_series_sum*=4
  return l_series_sum
