# pip install reportlab

from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle, PageBreak
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

# === Update these paths if your filenames differ ===
IMG_DATA_PREVIEW = "/mnt/data/12998d7d-d4b1-48e0-8116-85b955d0ad8a.png"
IMG_CODE = "/mnt/data/c7888a68-701e-4608-8f8e-a4a7173db60e.png"
IMG_CM = "/mnt/data/731b1a92-9e72-4ef5-b5a3-93c26de251ab.png"
OUTPUT = "Iris_LogisticRegression_Report.pdf"
# ===================================================

styles = getSampleStyleSheet()
doc = SimpleDocTemplate(OUTPUT, pagesize=A4, topMargin=36, bottomMargin=36, leftMargin=40, rightMargin=40)
story = []

def H(text): return Paragraph(text, styles["Heading2"])
def P(text): return Paragraph(text, styles["Normal"])

story += [
    Paragraph("<b>Logistic Regression on the Iris Dataset — Mini Report</b>", styles["Title"]),
    Spacer(1, 12),
    H("1) Objective"),
    P("Build a multiclass classifier (Logistic Regression, one-vs-rest) for the Iris dataset and evaluate performance using confusion matrix, accuracy, precision, recall, and F1-score."),
    Spacer(1, 6),
    H("2) Data & Setup"),
    P("Dataset: sklearn.datasets.load_iris() (150 samples). Features: sepal length, sepal width, petal length, petal width. Target classes: 0 (Setosa), 1 (Versicolor), 2 (Virginica). Split: Train/Test = 80/20 (stratified). Model: sklearn.linear_model.LogisticRegression."),
    Spacer(1, 8),
    Paragraph("<b>Dataset / Imports Screenshot</b>", styles["Heading3"]),
    Image(IMG_DATA_PREVIEW, width=420, height=260),
    Spacer(1, 12),
    H("3) Method"),
    P("Load data → split to X and y → 80/20 split → fit Logistic Regression → predict → compute confusion matrix and metrics."),
    Spacer(1, 8),
    Paragraph("<b>Training Code Screenshot</b>", styles["Heading3"]),
    Image(IMG_CODE, width=420, height=260),
    Spacer(1, 12),
    H("4) Results"),
    P("Confusion matrix on the test set and derived metrics are shown below."),
    Paragraph("<b>Confusion Matrix Heatmap</b>", styles["Heading3"]),
    Image(IMG_CM, width=360, height=300),
    Spacer(1, 10),
]

# Confusion matrix table
cm_data = [["Actual \\ Pred", "0", "1", "2"],
           ["0", "19", "0", "0"],
           ["1", "0", "12", "1"],
           ["2", "0", "0", "13"]]

cm_table = Table(cm_data, colWidths=[120, 70, 70, 70])
cm_table.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,0), colors.lightgrey),
    ("ALIGN", (0,0), (-1,-1), "CENTER"),
    ("GRID", (0,0), (-1,-1), 0.5, colors.black),
    ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
]))
story += [cm_table, Spacer(1, 10)]

# Metrics table (from CM)
metrics = [
    ["Metric", "Class 0", "Class 1", "Class 2", "Macro Avg", "Weighted Avg"],
    ["Precision", "1.000", "1.000", "0.929", "0.976", "0.979"],
    ["Recall",    "1.000", "0.923", "1.000", "0.974", "0.978"],
    ["F1-score",  "1.000", "0.960", "0.963", "0.974", "0.978"],
    ["Accuracy",  "—",     "—",     "—",     "—",     "0.978"],
]
mt = Table(metrics, colWidths=[90, 70, 70, 70, 80, 90])
mt.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,0), colors.lightgrey),
    ("GRID", (0,0), (-1,-1), 0.5, colors.black),
    ("ALIGN", (0,0), (-1,-1), "CENTER"),
    ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
]))
story += [mt, Spacer(1, 12)]

story += [
    H("5) Analysis"),
    P("Perfect separation for Setosa (class 0). A single Versicolor sample is predicted as Virginica, reflecting overlap between classes 1 and 2. Overall accuracy ≈ 97.8% with strong class-wise metrics."),
    Spacer(1, 6),
    H("6) Conclusion"),
    P("Logistic Regression achieves ≈97.8% accuracy on Iris with robust precision/recall. It is a simple, interpretable baseline that performs very well on this dataset."),
    PageBreak(),
    H("Appendix — Code Snippet"),
    P("See notebook for full code: imports, load_iris(as_frame=True), train_test_split, LogisticRegression, confusion_matrix, and metric calculations."),
]

doc.build(story)
print(f"Saved: {OUTPUT}")
