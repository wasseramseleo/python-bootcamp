"""--------------1-------------------"""
# Check for missing values
missing_count = df.isna().sum()

# Strategy 1: Remove birds with unknown sex
clean_df = df.dropna(subset=['sex'])

# Strategy 2: Impute missing weight with species average (Risky!)
# Only use if you understand the bias introduced
mean_weight = df['weight_g'].mean()
df['weight_g'] = df['weight_g'].fillna(mean_weight)

"""--------------2-------------------"""
# Calculate statistics per species
species_stats = df.groupby('species')['weight_g'].agg(['mean', 'count', 'std'])

print(species_stats)
# Output example:
#               mean  count   std
# Parus major   18.2    150   1.1
# Cyanistes...  11.5    120   0.9

"""--------------3-------------------"""
# Concatenation (Stacking days)
all_captures = pd.concat([monday_df, tuesday_df])

# Merging (Enriching data)
# capt_df has 'site_id', sites_df has 'site_id' + 'coordinates'
enriched_df = pd.merge(
    capt_df,
    sites_df,
    on='site_id',
    how='left' # Keep all captures, add coords where known
)

"""--------------4-------------------"""
# Create a summary matrix
# Rows: Species, Columns: Sex, Values: Average Wing Length
summary = df.pivot_table(
    values='wing_len',
    index='species',
    columns='sex',
    aggfunc='mean',
    margins=True # Adds 'All' row/col
)

"""--------------5-------------------"""
# Complex logic requiring row-by-row inspection
def classify_age(row):
    if row['plumage_code'] == 'J' and row['month'] < 6:
        return 'Juvenile'
    return 'Adult'

df['age_class'] = df.apply(classify_age, axis=1)

# Time Series: Resample daily captures to weekly sums
weekly_counts = df.set_index('date').resample('W').size()
