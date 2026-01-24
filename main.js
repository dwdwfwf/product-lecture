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

// --- NASA APOD Fetch Logic ---
document.addEventListener('DOMContentLoaded', () => {
    const apiKey = 'DEMO_KEY'; // Using NASA's demo key
    const apiUrl = `https://api.nasa.gov/planetary/apod?api_key=${apiKey}`;
    
    const apodContainer = document.getElementById('apod-container');
    const loadingMessage = document.getElementById('loading-message');

    fetch(apiUrl)
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            loadingMessage.style.display = 'none'; // Hide loading message
            
            let mediaElement = '';
            const imageAltText = `NASA 오늘의 천문학 사진: ${data.title}`;

            if (data.media_type === 'image') {
                mediaElement = `<img src="${data.hdurl}" alt="${imageAltText}" class="apod-image">`;
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
            loadingMessage.style.display = 'none'; // Hide loading message
            apodContainer.innerHTML = `<p style="text-align: center; color: red;">데이터를 불러오는 데 실패했습니다: ${error.message}</p>`;
            console.error('Error fetching APOD data:', error);
        });
});