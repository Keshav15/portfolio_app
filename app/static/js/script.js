document.addEventListener('DOMContentLoaded', () => {
    const fileInput = document.getElementById('resume-upload');
    const fileLabel = document.getElementById('file-label');
    const uploadButton = document.getElementById('upload-button');
  
    fileLabel.addEventListener('click', () => {
      fileInput.click();
    });
  
    fileInput.addEventListener('change', () => {
      const fileName = fileInput.value.split('\\').pop();
      fileLabel.innerHTML = fileName;
    });
  
    uploadButton.addEventListener('click', () => {
      const file = fileInput.files[0];
      if (file) {
        const formData = new FormData();
        formData.append('resume', file);
  
        fetch('/upload', {
          method: 'POST',
          body: formData,
        })
          .then((response) => response.json())
          .then((data) => {
            showResult(data);
          })
          .catch((error) => {
            console.error('Error:', error);
          });
      }
    });
  
    function showResult(data) {
      const resultContainer = document.getElementById('result-container');
      const resultData = document.getElementById('result-data');
  
      resultData.innerHTML = JSON.stringify(data, null, 2);
      resultContainer.style.display = 'block';
    }
  });
  