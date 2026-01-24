// analyze.js - Logic for the standalone Teachable Machine tool

document.addEventListener('DOMContentLoaded', () => {
    let model, imagePreview, labelContainer, analyzeButton;

    const modelURL = "https://teachablemachine.withgoogle.com/models/oi0yvsIQu/model.json";
    const metadataURL = "https://teachablemachine.withgoogle.com/models/oi0yvsIQu/metadata.json";

    const imageUpload = document.getElementById('image-upload');
    const imagePreviewContainer = document.getElementById('image-preview-container');
    imagePreview = document.getElementById('image-preview');
    analyzeButton = document.getElementById('analyze-button');
    labelContainer = document.getElementById('label-container');

    // Load the model
    async function loadModel() {
        try {
            analyzeButton.textContent = "모델 로딩 중...";
            model = await tmImage.load(modelURL, metadataURL);
            // Model loaded, ready for uploads
            analyzeButton.textContent = "분석하기";
            console.log("Teachable Machine model loaded.");
        } catch (error) {
            analyzeButton.textContent = "모델 로딩 실패";
            console.error("Could not load Teachable Machine model:", error);
        }
    }
    loadModel();

    // Handle file upload
    imageUpload.addEventListener('change', (event) => {
        const file = event.target.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = (e) => {
                imagePreview.src = e.target.result;
                imagePreviewContainer.style.display = 'block';
                analyzeButton.disabled = false;
                labelContainer.innerHTML = ""; // Clear previous results
            };
            reader.readAsDataURL(file);
        }
    });

    // Handle prediction
    analyzeButton.addEventListener('click', async () => {
        if (!model || !imagePreview.src) return;

        analyzeButton.disabled = true;
        analyzeButton.textContent = "분석 중...";

        const prediction = await model.predict(imagePreview);
        
        labelContainer.innerHTML = ""; // Clear previous results
        prediction.forEach(p => {
            const probability = (p.probability * 100).toFixed(1);
            const classDiv = document.createElement("div");
            // Example: "Galaxy: 87.1%"
            classDiv.innerHTML = `${p.className}: <span class="probability">${probability}%</span>`;
            labelContainer.appendChild(classDiv);
        });

        analyzeButton.disabled = false;
        analyzeButton.textContent = "다시 분석하기";
    });
});
