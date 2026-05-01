import os
import random
from datetime import date
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_RIGHT, TA_LEFT
from reportlab.lib import colors


# -------- BASE PATH --------
# Get current file directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Define report folder path
REPORT_DIR = os.path.join(BASE_DIR, "reports")

# Create reports folder if not exists
os.makedirs(REPORT_DIR, exist_ok=True)


# -------- BORDER FUNCTION --------
# Draw border around the PDF page
def draw_border(canvas, doc):
    width, height = letter
    margin = 20
    canvas.setStrokeColor(colors.black)
    canvas.setLineWidth(2)
    canvas.rect(margin, margin, width - 2 * margin, height - 2 * margin)


# -------- MAIN REPORT FUNCTION --------
# Generate CKD medical PDF report
def generate_ckd_report(
    name=None, age=None, place=None,
    bp=None, sg=None, albumin=None, sugar=None, glucose=None, urea=None, creatinine=None,
    sodium=None, potassium=None, hemoglobin=None, pcv=None, wbc=None, rbc=None,
    risk=None, stage=None, details=None
):

    # -------- SAFE FILE NAME --------
    # Replace spaces with underscore to avoid file errors
    safe_name = str(name).replace(" ", "_")

    # Create full file path
    file_name = os.path.join(REPORT_DIR, f"CKD_{safe_name}.pdf")

    # Generate random IDs
    report_id = "CKD" + str(random.randint(1000, 9999))
    patient_id = "PID" + str(random.randint(1000, 9999))

    # Create PDF document
    pdf = SimpleDocTemplate(file_name, pagesize=letter)

    # Load default styles
    styles = getSampleStyleSheet()

    # -------- CUSTOM STYLES --------
    # Add custom styles only if not already present

    if 'MyTitle' not in styles:
        styles.add(ParagraphStyle(name='MyTitle', alignment=TA_CENTER, fontSize=20, textColor=colors.darkblue))

    if 'MySubTitle' not in styles:
        styles.add(ParagraphStyle(name='MySubTitle', alignment=TA_LEFT, fontSize=10))

    if 'MyRight' not in styles:
        styles.add(ParagraphStyle(name='MyRight', alignment=TA_RIGHT, fontSize=10, leading=14))

    if 'MySection' not in styles:
        styles.add(ParagraphStyle(name='MySection', fontSize=13, textColor=colors.darkblue, spaceAfter=6))

    if 'MyReportTitle' not in styles:
        styles.add(ParagraphStyle(name='MyReportTitle', alignment=TA_CENTER, fontSize=16, textColor=colors.darkblue, spaceAfter=8))

    if 'MyText' not in styles:
        styles.add(ParagraphStyle(name='MyText', fontSize=11))

    if 'MyGreen' not in styles:
        styles.add(ParagraphStyle(name='MyGreen', fontSize=12, textColor=colors.green))

    if 'MyRed' not in styles:
        styles.add(ParagraphStyle(name='MyRed', fontSize=12, textColor=colors.red))

    # Store all PDF elements
    content = []

    # -------- HEADER SECTION --------
    content.append(Spacer(1, 10))

    header_table = Table([
        [
            Paragraph("<b>CITY CARE HOSPITAL & DIAGNOSTIC CENTER</b>", styles['MyTitle']),
            ''
        ],
        [
            Paragraph("Amravati, Maharashtra | 9876543210", styles['MySubTitle']),
            Paragraph("<b>Dr. Amit Patil</b><br/>MD (Nephrology)<br/>Kidney Specialist", styles['MyRight'])
        ]
    ], colWidths=[4.2 * inch, 2.8 * inch], rowHeights=[0.40 * inch, 0.30 * inch])

    header_table.setStyle(TableStyle([
        ('SPAN', (0, 0), (1, 0)),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('ALIGN', (0, 0), (1, 0), 'CENTER'),
        ('ALIGN', (0, 1), (0, 1), 'LEFT'),
        ('ALIGN', (1, 1), (1, 1), 'RIGHT'),
        ('LEFTPADDING', (0, 0), (-1, -1), 6),
        ('RIGHTPADDING', (0, 0), (-1, -1), 6),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (1, 0), 14),
    ]))

    content.append(header_table)
    content.append(Spacer(1, 22))

    # Report title
    content.append(Paragraph("Chronic Kidney Disease Medical Report", styles['MyReportTitle']))
    content.append(Spacer(1, 10))

    # -------- PATIENT DETAILS TABLE --------
    patient_table = Table([
        ["Patient ID", patient_id, "Report ID", report_id],
        ["Name", name, "Visit Date", str(date.today())],
        ["Age", age, "Place", place]
    ], colWidths=[90, 150, 90, 150])

    # Table styling
    patient_table.setStyle(TableStyle([
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('BACKGROUND', (0, 0), (0, -1), colors.lightgrey),
        ('BACKGROUND', (2, 0), (2, -1), colors.lightgrey),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
        ('FONTNAME', (2, 0), (2, -1), 'Helvetica-Bold'),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('LEFTPADDING', (0, 0), (-1, -1), 6),
        ('RIGHTPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
    ]))

    content.append(patient_table)
    content.append(Spacer(1, 18))

    # -------- LAB TEST RESULTS --------
    content.append(Paragraph("Laboratory Test Results", styles['MySection']))

    # Table data
    lab_data = [
        ["Test", "Result", "Normal Range"],
        ["Blood Pressure", bp, "80–120 mmHg"],
        ["Specific Gravity", sg, "1.005–1.025"],
        ["Albumin", albumin, "3.5–5.0 g/dL"],
        ["Sugar", sugar, "0–5 mg/dL"],
        ["Glucose", glucose, "70–140 mg/dL"],
        ["Urea", urea, "15–40 mg/dL"],
        ["Creatinine", creatinine, "0.6–1.2 mg/dL"],
        ["Sodium", sodium, "135–145 mmol/L"],
        ["Potassium", potassium, "3.5–5.0 mmol/L"],
        ["Hemoglobin", hemoglobin, "12–16 g/dL"],
        ["PCV", pcv, "36–46 %"],
        ["WBC", wbc, "4000–11000"],
        ["RBC", rbc, "Normal"]
    ]

    lab_table = Table(lab_data, colWidths=[170, 120, 160])

    lab_table.setStyle(TableStyle([
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('ALIGN', (1, 1), (1, -1), 'CENTER'),
        ('ALIGN', (2, 1), (2, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('LEFTPADDING', (0, 0), (-1, -1), 6),
        ('RIGHTPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.whitesmoke]),
    ]))

    content.append(lab_table)
    content.append(Spacer(1, 18))

    # -------- RISK & STAGE --------
    stage_num = int(stage.split()[-1])
    risk_style = styles['MyGreen'] if stage_num <= 2 else styles['MyRed']

    stage_table = Table([
        [Paragraph("<b>Risk Level</b>", styles['MyText']), Paragraph(risk, risk_style)],
        [Paragraph("<b>CKD Stage</b>", styles['MyText']), Paragraph(stage, styles['MyText'])]
    ], colWidths=[120, 330])

    stage_table.setStyle(TableStyle([
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('LEFTPADDING', (0, 0), (-1, -1), 6),
        ('RIGHTPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
    ]))

    content.append(stage_table)
    content.append(Spacer(1, 12))

    # -------- DESCRIPTION --------
    content.append(Paragraph("<b>Description:</b>", styles['MySection']))
    content.append(Paragraph(details['desc'], styles['MyText']))

    content.append(Spacer(1, 10))

    # -------- PREVENTIVE MEASURES --------
    content.append(Paragraph("Preventive Measures", styles['MySection']))
    content.append(Spacer(1, 6))

    for p in details['precautions']:
        content.append(Paragraph(f"• {p}", styles['MyText']))
        content.append(Spacer(1, 3))

    content.append(Spacer(1, 24))

    # -------- SIGNATURE --------
    signature_table = Table([
        ["", Paragraph("<b>Dr. Amit Patil</b>", styles['MyRight'])],
        ["", Paragraph("Signature: ____________________", styles['MyRight'])]
    ], colWidths=[3.5 * inch, 2.5 * inch])

    signature_table.setStyle(TableStyle([
        ('ALIGN', (1, 0), (1, -1), 'RIGHT'),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 0),
        ('TOPPADDING', (0, 0), (-1, -1), 0),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
    ]))

    content.append(signature_table)

    # -------- BUILD PDF --------
    pdf.build(content, onFirstPage=draw_border, onLaterPages=draw_border)

    return file_name