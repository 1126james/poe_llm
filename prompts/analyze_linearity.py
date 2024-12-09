ANALYZE_LINEARITY_PROMPT = """
<purpose>
    Analyze and interpret linear relationships between meaningful numerical columns in the dataset.
</purpose>

<instructions>
    <instruction>Identify numerical columns that are suitable for correlation analysis. Exclude columns that are identifiers (e.g., "ID") or unrelated numerical data (e.g., "Latitude" and "Longitude").</instruction>
    <instruction>For each pair of relevant numerical columns, calculate the Pearson correlation coefficient.</instruction>
    <instruction>Assess the strength and direction of each correlation.</instruction>
    <instruction>Determine the statistical significance of each correlation using p-values.</instruction>
    <instruction>Provide a clear interpretation of each significant result, focusing on practical insights.</instruction>
</instructions>

<example-output>
Linearity Analysis Results:
- **Age & Salary**
  - **Correlation Coefficient**: 0.68
  - **P-Value**: 0.001 (Significant Positive Correlation)
  - **Interpretation**: There is a strong, significant positive linear relationship between Age and Salary.
</example-output>

<example-output>
- **YearsOfExperience & PerformanceScore**
  - **Correlation Coefficient**: 0.45
  - **P-Value**: 0.03 (Moderate Positive Correlation)
  - **Interpretation**: There is a moderate, significant positive linear relationship between Years of Experience and Performance Score.
</example-output>

<note>
    Columns such as "ID", "Latitude", and "Longitude" were excluded as they are not meaningful for correlation analysis.
</note>

<content>
    Schema:
    {schema}
    
    Correlation Results:
    {correlation_results}
</content>
"""