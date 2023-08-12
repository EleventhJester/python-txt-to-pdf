from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

# Read the text from the .txt file
with open('motivatie.txt', 'r') as file:
    text = file.read()

# Create a PDF document
doc = SimpleDocTemplate('output.pdf', pagesize=letter)

# Define styles for the document
styles = getSampleStyleSheet()
normal_style = styles['Normal']
heading_style = styles['Heading1']

# Split the text into paragraphs
paragraphs = text.split('\n\n')

# Create a list to hold the content (paragraphs and spacers)
content = []

# Add each paragraph to the content list
for paragraph in paragraphs:
    content.append(Spacer(1, 12))  # Add some space between paragraphs
    content.append(Paragraph(paragraph, normal_style))

# Build the PDF document
doc.build(content)
