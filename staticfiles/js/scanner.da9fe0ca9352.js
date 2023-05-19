// Get the video container element
const videoContainer = document.getElementById('video-container');

// Set up the configuration for barcode scanning
const config = {
  inputStream: {
    type: 'LiveStream',
    constraints: {
      facingMode: 'environment', // Rear camera on mobile devices
    },
    target: videoContainer,
  },
  decoder: {
    readers: ['ean_reader'], // You can add more barcode formats here
  },
};

// Start the barcode scanner
Quagga.init(config, function(err) {
  if (err) {
    console.error('Error initializing Quagga:', err);
    return;
  }
  console.log('Quagga initialized.');

  // Set up listener for successful barcode detection
  Quagga.onDetected(function(result) {
    console.log('Barcode:', result.codeResult.code);
    // Perform any required actions with the barcode value

    // Stop the scanner after a barcode is detected
    Quagga.stop();
  });
});

// Stop the scanner when the user leaves the page
window.addEventListener('beforeunload', function() {
  Quagga.stop();
});
