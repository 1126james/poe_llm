SUGGEST_TRANSFORMATIONS_PROMPT = """
<purpose>
    Provide detailed, column-specific data transformations and enrichment steps tailored to each column in the dataset.
</purpose>

<instructions>
    <instruction>Analyze the provided dataset schema in detail, focusing on each column's name, data type, and potential context.</instruction>
    <instruction>For each column, suggest specific data transformations based on its data type and context. Be detailed in your recommendations.</instruction>
    <instruction>Recommend column-specific data enrichment steps, such as deriving new features by combining columns, or filling missing values using domain-specific logic.</instruction>
    <instruction>Ensure the suggestions are practical and aligned with real-world use cases.</instruction>
</instructions>

<example-output>
Data Transformation and Enrichment Suggestions:
- **Age**: Normalize to have a mean of 0 and standard deviation of 1 to facilitate comparison across scales.
- **Gender**: Apply one-hot encoding to convert the categorical data into numerical format for machine learning.
- **Salary**: Log-transform to reduce skewness and handle outliers effectively.
- **HireDate**: Extract features such as year of hire, month of hire, and ISO calendar week to analyze temporal trends.
- **FullName (FirstName, LastName)**: Concatenate FirstName and LastName into a single column "FullName" for easier analysis.
- **Latitude & Longitude**: Derive a new "Region" column by mapping Latitude and Longitude to predefined geographic regions.
- **Department**: Merge with external industry standards to enrich the categorical variable with additional context.
- **PerformanceScore**: Create bins (e.g., Low, Medium, High) to categorize scores into meaningful performance levels.
</example-output>

<content>
    Schema:
    {schema}
</content>
"""