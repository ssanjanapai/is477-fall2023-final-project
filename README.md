# IS-477 Fall 2023 Final Project

## Overview

This repository contains the final project for the IS-477: Data Management, Curation, and Reproducibility course for the Fall 2023 semester. The project applies various techniques learned throughout the course to create an end-to-end reproducible analysis.

### Dataset

The selected dataset for this project is [choose_dataset_name_here], sourced from the UCI Machine Learning archive.

## Analysis and Visualization

### Summary Statistics

The dataset underwent a thorough analysis to derive summary statistics, which are available in the [summary_statistics.csv](./results/summary_statistics.csv) file.

### Class Distribution Visualization

A bar chart illustrating the distribution of car evaluation classes is presented below. This visualization is saved as [class_distribution.png](./results/class_distribution.png).

![Class Distribution](./results/class_distribution.png)

### Decision Tree Classification

A Decision Tree classifier was trained on the dataset to predict car evaluation classes. The classifier achieved an accuracy of [accuracy_value] on the test set. The confusion matrix, depicting the performance of the classifier, is saved as [confusion_matrix.png](./results/confusion_matrix.png), and the detailed results are available in [classification_results.txt](./results/classification_results.txt).

#### Confusion Matrix

![Confusion Matrix](./results/confusion_matrix.png)

For further details and insights, refer to the [classification_results.txt](./results/classification_results.txt) file.


## Contributions

For teams working on this project, the contributions of each team member are outlined below:

- **Team Member 1:** [Description of contributions]
- **Team Member 2:** [Description of contributions]

## Analysis Section

The analysis of the dataset resulted in [brief_summary_of_results]. 

## Workflow

The workflow for this project is visualized in the [Workflow Image](workflow.png) located in the Workflow section.

## Reproducing

To reproduce the analysis, follow these steps:

1. Clone the repository:

   ```
   git clone https://github.com/your-username/is477-fall2023-final-project.git
   cd is477-fall2023-final-project
   ```

2. Execute workflow:

   ```snakemake --rulegraph analyze```

3. Build and run docker image:

   ```docker build -t username/is477-fall2023-final-project:v1 .
      docker push username/is477-fall2023-final-project:v1
   ```



