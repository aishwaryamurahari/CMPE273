const express = require('express');
const axios = require('axios');
const app = express();
const cors = require('cors');

app.use(cors());

app.use(express.json({ limit: '10mb' }));  // Set the limit to 10MB or larger if necessary
app.use(express.urlencoded({ limit: '10mb', extended: true }));

const subscriptionKey = process.env.REACT_APP_AZURE_COMPUTER_VISION_SUBSCRIPTION_KEY;
const endpoint = process.env.REACT_APP_AZURE_COMPUTER_VISION_ENDPOINT;


app.post('/api/analyze', async (req, res) => {
  const { base64Image } = req.body;
  const url = `${endpoint}/vision/v3.2/read/analyze`;

  try {
    // Convert base64 to binary
    const binaryImage = Buffer.from(base64Image, 'base64');

    // Initiate OCR analysis
    const response = await axios({
      method: 'post',
      url: url,
      headers: {
        'Ocp-Apim-Subscription-Key': subscriptionKey,
        'Content-Type': 'application/octet-stream',
      },
      data: binaryImage,  // Send the binary image
    });

    // Azure returns a URL to check the status
    const statusUrl = response.headers['operation-location'];
    console.log('Status URL:', statusUrl);

    // Poll the status URL until the operation is complete
    const result = await pollOcrResult(statusUrl);
    res.json(result);  // Send the final OCR result to the frontend

  } catch (error) {
    console.error('Error during OCR analysis:', error.response ? error.response.data : error.message);
    res.status(500).send({ error: 'Error analyzing image' });
  }
});

const pollOcrResult = async (statusUrl) => {
  try {
    let isProcessing = true;
    let result = null;

    // Poll the status URL until the operation is complete
    while (isProcessing) {
      const response = await axios({
        method: 'get',
        url: statusUrl,
        headers: {
          'Ocp-Apim-Subscription-Key': subscriptionKey,
        },
      });

      // Check the status
      if (response.data.status === 'succeeded') {
        isProcessing = false;
        result = response.data.analyzeResult;  // Extract the OCR result
      } else if (response.data.status === 'failed') {
        throw new Error('OCR analysis failed');
      } else {
        // Wait for a moment before checking again
        await new Promise(resolve => setTimeout(resolve, 2000));  // 2-second delay
      }
    }

    return result;  // Return the OCR result once the analysis is complete
  } catch (error) {
    throw error;
  }
};


app.listen(5003, () => {
  console.log('Server running on port 5000');
});
