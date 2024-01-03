import pandas as pd
from sdv.single_table import GaussianCopulaSynthesizer
from sdv.metadata import SingleTableMetadata
from sdv.evaluation.single_table import run_diagnostic
from sdv.evaluation.single_table import evaluate_quality

# Assume 'real_data' is your original dataset
real_data = pd.read_csv('sample.csv')  # Your original dataset

metadata = SingleTableMetadata()
metadata.detect_from_dataframe(real_data)

metadata.update_column(
    column_name='Gender',
    sdtype='categorical'
)

metadata.update_column(
    column_name='Diagnosis',
    sdtype='categorical'
)

metadata.update_column(
    column_name='Treatment',
    sdtype='categorical'
)

metadata.update_column(
    column_name='Outcome',
    sdtype='categorical'
)

# Define metadata
'''
metadata = {
    'fields': {
        'Patient ID': {'type': 'id', 'subtype': 'integer'},
        'Age': {'type': 'numerical', 'subtype': 'integer'},
        'Gender': {'type': 'categorical'},
        'Diagnosis': {'type': 'categorical'},
        'Treatment': {'type': 'categorical'},
        'Outcome': {'type': 'categorical'}
    },
    'primary_key': 'Patient ID'
}
'''

synthesizer = GaussianCopulaSynthesizer(metadata)
synthesizer.fit(real_data)


# Sample synthetic data
synthetic_data = synthesizer.sample(num_rows=500)
print(synthetic_data.head(20))

diagnostic = run_diagnostic(
    real_data=real_data,
    synthetic_data=synthetic_data,
    metadata=metadata
)

quality_report = evaluate_quality(
    real_data,
    synthetic_data,
    metadata
)

print(quality_report.get_details('Column Shapes'))

# Basic validation
# Example: Compare mean and standard deviation of a numerical column
#real_mean = real_data['Age'].mean()
#synthetic_mean = synthetic_data['Age'].mean()
#real_std = real_data['Age'].std()
#synthetic_std = synthetic_data['Age'].std()

#print(f"Real Data - Mean Age: {real_mean}, Std Age: {real_std}")
#print(f"Synthetic Data - Mean Age: {synthetic_mean}, Std Age: {synthetic_std}")


