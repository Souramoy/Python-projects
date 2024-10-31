# Python-projects

## PDF Insight Assistant

The PDF Insight Assistant is a graphical user interface (GUI) application developed using the Tkinter library in Python. This tool allows users to interactively perform question-answering tasks on PDF documents and image files. It integrates a pre-trained BERT model from Hugging Face’s Transformers library to offer precise answers based on the context extracted from the documents.

### Features

1. User-friendly interface  
   A clean, modern interface with themed widgets ensures ease of use and a pleasant user experience.
   
2. File selection  
   Users can select PDF documents or image files (e.g., .jpg, .png) through an intuitive file browsing feature.

3. Dynamic content display  
   The selected document’s content is automatically extracted and displayed in a text widget, allowing users to easily review the material.

4. Question-answering functionality  
   Users can input any question related to the document, and the BERT model will analyze the context of the text and provide accurate answers.

5. Answer display  
   The application displays the answer to the user’s question directly within the GUI.

6. Developer information  
   A section within the GUI offers information about the developer, adding a personal touch to the project.

### How to Use

1. File selection  
   Click the "Browse File" button to select a PDF or image file.

2. Question entry  
   Enter your question in the input field provided.

3. Question-answering  
   Click the "Ask Question" button to start the process, and the model will generate an answer based on the file content.

4. Answer display  
   The application displays the answer to the user’s question directly in the output field.

### Enhancements and Customization

- Themed style  
  The application uses ThemedStyle to apply different themes, offering users a choice in the visual appearance.

- Content display  
  Extracted content from the PDF or image is displayed in a text widget, offering a clear review of the document.

- Developer information  
  Information about the developer is included, adding a personalized aspect to the interface.

### Future Improvements

- Additional file formats  
  Expand the application to support more file types such as Word, Excel, and plain text documents.

- Advanced styling  
  Explore additional customization options to improve the visual appearance and functionality of the GUI.

- Integration with external APIs  
  Integrate APIs like Google Vision to enhance text extraction accuracy, especially for handwritten documents.

### Disclaimer:

## - Educational Use Only
## - Verification Responsibility
## - No Guarantees or Warranties
## - Caution with Sensitive Data
## - Not a Substitute for Professional Advice
## - No Liability for Damages

### To run the PDF Insight Assistant code, the following libraries need to be installed. You can use pip to install them by running the commands in your terminal or command prompt:

pip install Pillow
pip install pytesseract
pip install PyPDF2
pip install transformers
pip install ttkthemes

Make sure you have Tesseract OCR installed on your system, as it is required for the text extraction from image files. You can download it from here - https://github.com/tesseract-ocr/tesseract 

### Feel free to customize this project according to your needs and preferences. Your feedback and improvements are always welcome—thank me later for the inspiration! Enjoy coding! - Souramoy 😉