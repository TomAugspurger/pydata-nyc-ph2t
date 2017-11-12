origin_counts = flights['origin'].value_counts()
top5 = origin_counts.index[:5]
mask = flights.origin.isin(top5)
flights.loc[mask, ['origin', 'dest']]