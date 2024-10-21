import React, { useState } from 'react';

const OcrAnalyticsPage = () => {
  const [selectedImage, setSelectedImage] = useState(null);
  const [previewImage, setPreviewImage] = useState(null);
  const [ocrResult, setOcrResult] = useState('');


  const handleImageChange = (e) => {
    if (e.target.files && e.target.files[0]) {
      const file = e.target.files[0];
      setSelectedImage(file);  // Set the actual file instead of a URL
  
      const reader = new FileReader();
      reader.onloadend = () => {
        setPreviewImage(reader.result);  // Store the image as base64 for preview
      };
      reader.readAsDataURL(file);
    }
  };
  
  const handleOcrAnalyze = async () => {
    if (!selectedImage) return;
  
    // Convert file to base64
    const reader = new FileReader();
    reader.readAsDataURL(selectedImage);
    reader.onloadend = async () => {
      const base64Image = reader.result.split(',')[1];  // Get the base64 part
  
      // Call Azure AI Vision OCR API with base64 image
      const response = await fetch('http://localhost:5003/api/analyze', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ base64Image }),  // Send base64 image
      });
  
      const data = await response.json();
      console.log('OCR result:', data);  
      setOcrResult(data);  // Assuming API returns OCR result
    };
  };

  return (
    <div>
      <h2>OCR Analytics Page</h2>
      <div style={{ display: 'flex', justifyContent: 'space-around' }}>
        {/* Step 1 */}
        <div>
          <h3>Step 1</h3>
          <input type="file" accept="image/*" onChange={handleImageChange} />
          {selectedImage && <img src={selectedImage} alt="Selected" style={{ width: '200px', marginTop: '10px' }} />}
          {previewImage && <img src={previewImage} alt="Preview" style={{ width: '200px', marginTop: '10px' }} />} 
        </div>

        {/* Step 2 */}
        <div>
          <h3>Step 2</h3>
          <button onClick={handleOcrAnalyze}>OCR Analyze</button>
        </div>

        {/* Step 3 */}
        <div>
          <h3>Step 3</h3>
          <div>{ocrResult && <pre>{JSON.stringify(ocrResult, null, 2)}</pre>}</div>
        </div>
      </div>
    </div>
  );
};

export default OcrAnalyticsPage;