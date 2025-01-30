from fpdf import FPDF

# Create instance of FPDF
pdf = FPDF()

# Add a page
pdf.add_page()

# Set font: Arial, bold, size 12
pdf.set_font("Arial", style="B", size=12)

# Add a title
pdf.cell(200, 10, txt="Career Guidance Web App", ln=True, align="C")

# Add a subtitle
pdf.set_font("Arial", style="", size=10)
pdf.cell(200, 10, txt="Created by sukhdeep Singh", ln=True, align="C")

# Add some content
pdf.ln(10)  # Line break
pdf.set_font("Arial", size=12)
content = (
    "Welcome to the Career Guidance Web App! This app provides personalized career advice, "
    "mentorship programs, and resources to help students make informed career choices."
)
pdf.multi_cell(0, 10, txt=content)

# Add another section
pdf.ln(10)
pdf.set_font("Arial", style="B", size=12)
pdf.cell(200, 10, txt="Features:", ln=True)

pdf.set_font("Arial", size=12)
features = [
    "1. Interactive career exploration tools",
    "2. AI-powered personalized recommendations",
    "3. Comprehensive career resource portal",
]
for feature in features:
    pdf.cell(200, 10, txt=feature, ln=True)

# Save the PDF to a file
pdf.output("Career_Guidance.pdf")

print("PDF created successfully!")
