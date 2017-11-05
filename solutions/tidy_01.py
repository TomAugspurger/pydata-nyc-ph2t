df['point_spread'] = df.home_points - df.away_points
df['home_win'] = df['point_spread'] > 0
df.head()
