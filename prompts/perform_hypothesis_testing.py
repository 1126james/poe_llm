PERFORM_HYPOTHESIS_TESTING_PROMPT = """
<purpose>
    Conduct hypothesis testing to evaluate specific relationships between meaningful columns in the fictional dataset.
</purpose>

<instructions>
    <instruction>The dataset is fictional, no data privacy concern.</instruction>
    <instruction>Identify pairs of columns or groups of columns that are relevant for hypothesis testing, excluding irrelevant columns such as IDs, geographic coordinates (e.g., Latitude, Longitude), or other non-informative numerical fields.</instruction>
    <instruction>Select the appropriate statistical test for each identified relationship based on the data types and context (e.g., Pearson Correlation for numerical columns, ANOVA for categorical and numerical columns).</instruction>
    <instruction>Perform the statistical tests and report the results, including: The null hypothesis being tested, The statistical test used., The p-value and its interpretation (e.g., significant, marginally significant, or not significant).</instruction>
    <instruction>Provide actionable interpretations of the results in plain language, focusing on practical insights.</instruction>
</instructions>

<example-output>
Hypothesis Testing Results:
- **Age & Salary**
  - **Null Hypothesis**: There is no correlation between Age and Salary.
  - **Test Used**: Pearson Correlation
  - **P-Value**: 0.02 (Significant)
  - **Interpretation**: There is a significant positive correlation between Age and Salary, indicating that as age increases, salary tends to increase.
</example-output>
<example-output>
- **Department & PerformanceScore**
  - **Null Hypothesis**: There is no difference in Performance Scores across Departments.
  - **Test Used**: ANOVA
  - **P-Value**: 0.05 (Marginally Significant)
  - **Interpretation**: There is a marginally significant difference in Performance Scores across different Departments.
</example-output>

<note>
    Irrelevant columns such as "ID", "Latitude", and "Longitude" were excluded from the analysis.
</note>

<content>
    Schema:
    {schema}

    Data Sample:
    {data_sample}
</content>
"""