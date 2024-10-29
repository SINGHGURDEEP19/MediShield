document.getElementById('predictBtn').addEventListener('click', function() {
    // Get the image input element
    const fileInput = document.getElementById('fileInput');
    
    if (fileInput.files.length > 0) {
        const file = fileInput.files[0];

        // Validate if the file is an image
        if (file && file.type.startsWith('image/')) {
            // Create a file reader to read the image
            const reader = new FileReader();
            
            reader.onload = function(e) {
                // Open the image in a new tab
                const imageWindow = window.open();
                imageWindow.document.write('<img src="' + e.target.result + '" style="max-width:100%;height:auto;">');
            };
            
            reader.readAsDataURL(file);
        } else {
            alert('Please upload a valid image file.');
        }
    } else {
        alert('Please select an image.');
    }
});