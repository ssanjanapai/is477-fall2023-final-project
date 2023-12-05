rule prepare:
    output: "data/car_evaluation_dataset.csv"
    shell: "python scripts/prepare_data.py"
    

rule profile:
    input: "data/car_evaluation_dataset.csv"
    output: "profiling/report.html"
    shell: "python scripts/my_profile.py"

rule analyze:
    input: "data/car_evaluation_dataset.csv"
    output: 
      "results/class_distribution.png",
      "results/classification_results.txt",
      "results/confusion_matrix.png",
      "results/summary_statistics.csv"
    shell: "python scripts/analysis.py"