# RPI
city_rpi = rpi.RPI.rename(mapping)
df['home_strength'] = df.home_team.map(city_rpi)
df['away_strength'] = df.away_team.map(city_rpi)
df.head()
