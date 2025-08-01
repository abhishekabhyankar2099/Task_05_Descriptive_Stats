import pandas as pd

# Loading the dataset
file_path = "C:/Users/Hp/Downloads/sportsref_download.xlsx"  
df = pd.read_excel(file_path)

# 1. Who has the most points per match?
df['Points_per_match'] = df['PTS'] / df['G']
most_points_per_match = df.loc[df['Points_per_match'].idxmax(), ['Player', 'Points_per_match']]

# 2. Who has the most awards? (count distinct awards, assume comma separates)
df['Awards_count'] = df['Awards'].fillna('').apply(lambda x: len([a for a in x.split(',') if a.strip() != '']))
most_awards = df.loc[df['Awards_count'].idxmax(), ['Player', 'Awards_count', 'Awards']]

# 3. Who has the greatest free throw percentage? (ignore missing or zero games)
df_nonan_ft = df[df['FT%'].notna() & (df['G'] > 0)]
most_ft = df_nonan_ft.loc[df_nonan_ft['FT%'].idxmax(), ['Player', 'FT%']]

# 4. What is the average age of each team?
avg_age_by_team = df.groupby('Team')['Age'].mean().round(2)

# 5. Which player has played the most minutes in total?
most_minutes = df.loc[df['MP'].idxmax(), ['Player', 'MP']]

# Print results
print("1. Most Points Per Match:")
print(f"   {most_points_per_match['Player']} - {most_points_per_match['Points_per_match']:.2f} points per match\n")

print("2. Most Awards:")
print(f"   {most_awards['Player']} - {most_awards['Awards_count']} awards")
print(f"   Awards: {most_awards['Awards']}\n")

print("3. Greatest Free Throw Percentage:")
print(f"   {most_ft['Player']} - {most_ft['FT%']:.2%}\n")

print("4. Average Age by Team:")
print(avg_age_by_team)
print()

print("5. Most Minutes Played:")
print(f"   {most_minutes['Player']} - {most_minutes['MP']} minutes\n")
