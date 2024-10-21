OCR Analytics Web App
# OCR Analytics Web Application

This project is a web application that uses Azure Vision API to perform Optical Character Recognition (OCR) on uploaded images. The app allows users to upload an image, sends it to Azure for analysis, and displays the detected text in JSON format.

## Features
- Upload an image (PNG, JPG, etc.) for OCR analysis.
- Utilizes Azure's Computer Vision API to extract text from images.
- Displays OCR results in a formatted JSON structure.
- React-based frontend with an Express backend.

## Tech Stack
- Frontend: React
- Backend: Node.js, Express
- OCR API: Azure Computer Vision API

## Getting Started
### Prerequisites
Before running this application, make sure you have the following installed:
- Node.js (LTS version recommended)
- An active Azure account with access to the Computer Vision API

### Setup Instructions
1. Clone the repository:
```bash
git clone
cd ocr-analytics-webapp
```

2. Install dependencies: Navigate to the project directory and install the required dependencies for both the frontend and backend.
```bash
# Install backend dependencies
npm install express axios cors

# Install frontend dependencies
cd client
npm install
```

3. Set up Azure Vision API:
- Go to your Azure Portal and create a new Cognitive Services resource for Computer Vision.
- Copy the Subscription Key and Endpoint URL for the Computer Vision API.

4. Configure the backend: In the server.js file, add your Azure Subscription Key and Endpoint URL.
```javascript
const subscriptionKey = 'YOUR_AZURE_SUBSCRIPTION_KEY';
const endpoint = 'https://YOUR_ENDPOINT.cognitiveservices.azure.com/vision/v3.2/read/analyze';
```

5. Start the backend server: Run the backend Express server on port 5003.
```bash
node server.js
```

6. Start the React frontend: In a separate terminal window, navigate to the frontend folder and start the React development server.
```bash
cd client
npm start
```

7. Open your browser and go to http://localhost:3000.