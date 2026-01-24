// main.js for NASA APOD Viewer

// --- Theme Toggle Logic ---
const themeToggle = document.getElementById('theme-toggle');
const body = document.body;

// Apply saved theme on load
const savedTheme = localStorage.getItem('theme');
if (savedTheme) {
    body.classList.add(savedTheme);
    themeToggle.textContent = '☀️';
}

themeToggle.addEventListener('click', () => {
    body.classList.toggle('dark-mode');
    
    // Save theme and update button icon
    if (body.classList.contains('dark-mode')) {
        localStorage.setItem('theme', 'dark-mode');
        themeToggle.textContent = '☀️'; // Sun icon for light mode
    } else {
        localStorage.removeItem('theme');
        themeToggle.textContent = '🌙'; // Moon icon for dark mode
    }
});

// --- NASA APOD Fetch Logic & Teachable Machine Integration ---
document.addEventListener('DOMContentLoaded', () => {
    const apiKey = 'DEMO_KEY'; // Using NASA's demo key
    const apiUrl = `https://api.nasa.gov/planetary/apod?api_key=${apiKey}`;
    
    const apodContainer = document.getElementById('apod-container');
    const loadingMessage = document.getElementById('loading-message');

    let model, labelContainer;
    const analysisSection = document.getElementById('analysis-section');
    const analyzeButton = document.getElementById('analyze-button');

    fetch(apiUrl)
        .then(response => response.json())
        .then(data => {
            loadingMessage.style.display = 'none';
            
            let mediaElement;
            const imageAltText = `NASA 오늘의 천문학 사진: ${data.title}`;

            if (data.media_type === 'image') {
                // Use a proxy for the image to avoid CORS issues with Teachable Machine
                const imageUrl = `https://images.weserv.nl/?url=${encodeURIComponent(data.hdurl)}`;
                mediaElement = `<img src="${imageUrl}" alt="${imageAltText}" class="apod-image" crossorigin="anonymous">`;
                
                // Show and initialize the analysis section only for images
                analysisSection.style.display = 'block';
                initTeachableMachine();
            } else if (data.media_type === 'video') {
                mediaElement = `<iframe src="${data.url}" title="${data.title}" frameborder="0" allowfullscreen class="apod-video"></iframe>`;
            }

            const contentHtml = `
                <figure>
                    ${mediaElement}
                    <figcaption>
                        <h2>${data.title}</h2>
                        <p class="date">${data.date}</p>
                    </figcaption>
                </figure>
                <section class="apod-explanation">
                    <h3>설명:</h3>
                    <p>${data.explanation}</p>
                </section>
            `;
            apodContainer.innerHTML = contentHtml;
        })
        .catch(error => {
            loadingMessage.style.display = 'none';
            apodContainer.innerHTML = `<p style="text-align: center; color: red;">데이터를 불러오는 데 실패했습니다: ${error.message}</p>`;
            console.error('Error fetching APOD data:', error);
        });

    async function initTeachableMachine() {
        // IMPORTANT: Replace this with your actual Teachable Machine model URL
        const modelURL = "https://teachablemachine.withgoogle.com/models/YOUR_MODEL_ID/model.json";
        const metadataURL = "https://teachablemachine.withgoogle.com/models/YOUR_MODEL_ID/metadata.json";

        try {
            analyzeButton.textContent = "모델 로딩 중...";
            model = await tmImage.load(modelURL, metadataURL);
            labelContainer = document.getElementById("label-container");
            
            // Model loaded, enable the button
            analyzeButton.disabled = false;
            analyzeButton.textContent = "이 사진은 무엇일까요?";
            analyzeButton.onclick = predict; // Assign predict function to button click
        } catch (error) {
            analyzeButton.textContent = "모델 로딩 실패";
            console.error("Could not load Teachable Machine model:", error);
        }
    }

    async function predict() {
        analyzeButton.disabled = true;
        analyzeButton.textContent = "분석 중...";

        const apodImage = document.querySelector('.apod-image');
        const prediction = await model.predict(apodImage);
        
        labelContainer.innerHTML = ""; // Clear previous results
        prediction.forEach(p => {
            const probability = (p.probability * 100).toFixed(1);
            const classDiv = document.createElement("div");
            classDiv.innerHTML = `${p.className}: ${probability}%`;
            labelContainer.appendChild(classDiv);
        });

        analyzeButton.disabled = false;
        analyzeButton.textContent = "다시 분석하기";
    }
});