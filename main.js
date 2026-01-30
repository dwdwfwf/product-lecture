document.addEventListener('DOMContentLoaded', () => {
    const introSection = document.getElementById('intro-section');
    const quizSection = document.getElementById('quiz-section');
    const startQuizButton = document.getElementById('start-quiz-button');
    const questionText = document.getElementById('question-text');
    const optionsContainer = document.getElementById('options-container');
    const prevButton = document.getElementById('prev-button');
    const nextButton = document.getElementById('next-button');
    const submitButton = document.getElementById('submit-button');
    const progressBarFill = document.getElementById('progress-bar-fill');
    const loadingOverlay = document.getElementById('loading-overlay'); // Get loading overlay

    let currentQuestionIndex = 0;
    let userAnswers = []; // Stores the index of the selected option for each question

    const questions = [
        {
            question: "자신을 재충전하는 방법은?",
            options: [
                { text: "사람들과 어울리면서 에너지를 얻는다.", value: "E" },
                { text: "혼자만의 시간을 보내며 에너지를 충전한다.", value: "I" }
            ]
        },
        {
            question: "새로운 정보를 접했을 때 당신의 반응은?",
            options: [
                { text: "구체적인 사실과 경험에 집중한다.", value: "S" },
                { text: "전체적인 맥락과 가능성을 탐색한다.", value: "N" }
            ]
        },
        {
            question: "중요한 결정을 내릴 때 가장 중요하게 생각하는 것은?",
            options: [
                { text: "논리와 객관적인 분석을 우선시한다.", value: "T" },
                { text: "사람들과의 관계와 개인적인 가치를 고려한다.", value: "F" }
            ]
        },
        {
            question: "삶의 방식을 선호하는 것은?",
            options: [
                { text: "계획적이고 체계적인 생활을 선호한다.", value: "J" },
                { text: "유연하고 즉흥적인 생활을 선호한다.", value: "P" }
            ]
        },
        {
            question: "모임에서 당신은 주로 어떤 역할을 하나요?",
            options: [
                { text: "적극적으로 대화를 주도하고 에너지를 발산한다.", value: "E" },
                { text: "주로 듣고 관찰하며 조용히 참여한다.", value: "I" }
            ]
        },
        {
            question: "어떤 이야기를 할 때 더 편안함을 느끼나요?",
            options: [
                { text: "현재 벌어지고 있는 사실이나 구체적인 경험.", value: "S" },
                { text: "미래의 가능성, 아이디어, 이론적인 이야기.", value: "N" }
            ]
        },
        {
            question: "다른 사람을 평가할 때 어떤 점을 주로 보나요?",
            options: [
                { text: "합리성, 효율성, 공정성.", value: "T" },
                { text: "친절함, 이해심, 공감 능력.", value: "F" }
            ]
        },
        {
            question: "일을 처리하는 당신의 스타일은?",
            options: [
                { text: "정해진 계획에 따라 체계적으로 진행한다.", value: "J" },
                { text: "상황에 따라 유연하게 대처하며 즉흥적으로 해결한다.", value: "P" }
            ]
        },
        {
            question: "스트레스를 받았을 때 어떻게 해소하나요?",
            options: [
                { text: "외부 활동을 통해 기분 전환을 한다.", value: "E" },
                { text: "혼자 조용히 생각하고 감정을 정리한다.", value: "I" }
            ]
        },
        {
            question: "당신에게 더 흥미로운 분야는?",
            options: [
                { text: "실용적이고 현실적인 기술이나 정보.", value: "S" },
                { text: "추상적이고 이론적인 개념이나 아이디어.", value: "N" }
            ]
        },
        {
            question: "누군가 힘들어할 때 당신의 반응은?",
            options: [
                { text: "문제의 원인을 분석하고 해결책을 제시하려 한다.", value: "T" },
                { text: "상대방의 감정에 공감하고 위로해 준다.", value: "F" }
            ]
        },
        {
            question: "주말 계획을 세울 때 당신의 모습은?",
            options: [
                { text: "미리 계획을 세우고 일정대로 움직인다.", value: "J" },
                { text: "즉흥적으로 할 일을 정하고 여유롭게 보낸다.", value: "P" }
            ]
        }
    ];

    function updateProgressBar() {
        const progress = ((currentQuestionIndex) / questions.length) * 100;
        progressBarFill.style.width = `${progress}%`;
    }

    function displayQuestion() {
        if (currentQuestionIndex < 0) currentQuestionIndex = 0;
        if (currentQuestionIndex >= questions.length) currentQuestionIndex = questions.length - 1;

        questionText.textContent = questions[currentQuestionIndex].question;
        optionsContainer.innerHTML = ''; // Clear previous options

        questions[currentQuestionIndex].options.forEach((option, index) => {
            const button = document.createElement('button');
            button.textContent = option.text;
            button.dataset.value = option.value;
            button.classList.add('option-button');
            if (userAnswers[currentQuestionIndex] === index) {
                button.classList.add('selected');
            }
            button.addEventListener('click', () => selectOption(index, option.value));
            optionsContainer.appendChild(button);
        });

        updateNavigationButtons();
        updateProgressBar();
    }

    function selectOption(optionIndex, optionValue) {
        userAnswers[currentQuestionIndex] = optionIndex;

        // Remove 'selected' class from all options for the current question
        Array.from(optionsContainer.children).forEach(button => {
            button.classList.remove('selected');
        });
        // Add 'selected' class to the clicked option
        optionsContainer.children[optionIndex].classList.add('selected');

        // Enable next/submit button
        if (currentQuestionIndex < questions.length - 1) {
            nextButton.disabled = false;
        } else {
            submitButton.disabled = false;
        }
    }

    function updateNavigationButtons() {
        prevButton.style.display = currentQuestionIndex > 0 ? 'inline-block' : 'none';
        nextButton.style.display = currentQuestionIndex < questions.length - 1 ? 'inline-block' : 'none';
        submitButton.style.display = currentQuestionIndex === questions.length - 1 ? 'inline-block' : 'none';

        // Disable next/submit if no answer is selected for the current question
        nextButton.disabled = userAnswers[currentQuestionIndex] === undefined;
        submitButton.disabled = userAnswers[currentQuestionIndex] === undefined;
    }

    function goToNextQuestion() {
        if (userAnswers[currentQuestionIndex] !== undefined && currentQuestionIndex < questions.length - 1) {
            currentQuestionIndex++;
            displayQuestion();
        }
    }

    function goToPrevQuestion() {
        if (currentQuestionIndex > 0) {
            currentQuestionIndex--;
            displayQuestion();
        }
    }

    function calculateMBTI() {
        const scores = { E: 0, I: 0, S: 0, N: 0, T: 0, F: 0, J: 0, P: 0 };

        userAnswers.forEach((answerIndex, qIndex) => {
            if (answerIndex !== undefined) {
                const selectedValue = questions[qIndex].options[answerIndex].value;
                scores[selectedValue]++;
            }
        });

        let mbtiResult = "";
        mbtiResult += scores.E > scores.I ? "E" : "I";
        mbtiResult += scores.S > scores.N ? "S" : "N";
        mbtiResult += scores.T > scores.F ? "T" : "F";
        mbtiResult += scores.J > scores.P ? "J" : "P";

        return mbtiResult;
    }

    function showResult() {
        if (userAnswers[questions.length - 1] === undefined) {
            alert("마지막 질문에 답변해주세요!");
            return;
        }

        loadingOverlay.style.display = 'flex'; // Show loading overlay
        
        setTimeout(() => {
            const mbti = calculateMBTI();
            // Redirect to the specific MBTI result page
            window.location.href = `results/${mbti.toLowerCase()}.html`;
        }, 1500); // Show loading for 1.5 seconds
    }

    // Event Listeners
    startQuizButton.addEventListener('click', () => {
        introSection.classList.add('fade-out');

        setTimeout(() => {
            introSection.style.display = 'none';
            quizSection.style.display = 'block';
            quizSection.classList.add('fade-in');
            
            currentQuestionIndex = 0;
            userAnswers = Array(questions.length).fill(undefined);
            displayQuestion();
        }, 500); // Match animation duration (0.5s)
    });

    prevButton.addEventListener('click', goToPrevQuestion);
    nextButton.addEventListener('click', goToNextQuestion);
    submitButton.addEventListener('click', showResult);

    // Initial display setup (only intro section visible)
    introSection.style.display = 'block';
    quizSection.style.display = 'none';
});