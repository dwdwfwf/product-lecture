document.addEventListener('DOMContentLoaded', () => {
    // 1. Kakao SDK Initialization
    try {
        // --- 중요 ---
        // ※ 실제 배포 시, 본인의 카카오 개발자 앱 키를 입력해야 합니다. ※
        // ※ This is a placeholder key. You must use your own Kakao developer app key for production. ※
        const KAKAO_APP_KEY = '6e2ffc8b4e5748eb04db8f93a2063e98'; // 여기에 실제 키를 입력하세요.
        
        if (KAKAO_APP_KEY === 'YOUR_KAKAO_JAVASCRIPT_KEY') {
            console.warn('Kakao SDK가 초기화되지 않았습니다. 실제 앱 키를 입력해주세요.');
        } else {
            Kakao.init(KAKAO_APP_KEY);
            console.log('Kakao SDK in itialized:', Kakao.isInitialized());
        }
    } catch (e) {
        console.error("Kakao SDK 초기화 중 오류 발생", e);
    }

    // 2. Element Selectors
    const kakaoShareBtn = document.getElementById('kakao-share-btn');
    const copyUrlBtn = document.getElementById('copy-url-btn');

    if (kakaoShareBtn) {
        kakaoShareBtn.addEventListener('click', () => {
            if (!Kakao.isInitialized()) {
                alert('카카오 SDK가 초기화되지 않았습니다. 앱 키를 확인해주세요.');
                return;
            }

            // Extract MBTI info from the page
            const mbtiType = document.querySelector('.mbti-type-intro h2')?.innerText.split(':')[0] || 'MBTI';
            const mbtiName = document.querySelector('.mbti-type-intro h2')?.innerText.split(':')[1]?.trim() || '성격 유형';
            const mbtiDescription = document.querySelector('.mbti-description')?.innerText;
            const mbtiImage = document.querySelector('.mbti-avatar')?.src;

            Kakao.Share.sendDefault({
                objectType: 'feed',
                content: {
                    title: `내 MBTI 결과는? ${mbtiType} ${mbtiName}`,
                    description: mbtiDescription,
                    imageUrl: mbtiImage,
                    link: {
                        mobileWebUrl: window.location.href,
                        webUrl: window.location.href,
                    },
                },
                buttons: [
                    {
                        title: '결과 자세히 보기',
                        link: {
                            mobileWebUrl: window.location.href,
                            webUrl: window.location.href,
                        },
                    },
                    {
                        title: '나도 검사하기',
                        link: {
                            // Assuming the main page is at the root
                            mobileWebUrl: window.location.origin,
                            webUrl: window.location.origin,
                        },
                    },
                ],
            });
        });
    }

    if (copyUrlBtn) {
        copyUrlBtn.addEventListener('click', () => {
            const urlToCopy = window.location.href;

            navigator.clipboard.writeText(urlToCopy).then(() => {
                // --- Visual Feedback ---
                const originalText = copyUrlBtn.innerHTML;
                copyUrlBtn.innerHTML = '✅ 복사 완료!';
                copyUrlBtn.disabled = true;

                setTimeout(() => {
                    copyUrlBtn.innerHTML = originalText;
                    copyUrlBtn.disabled = false;
                }, 2000); // Revert after 2 seconds
            }).catch(err => {
                console.error('URL 복사 실패:', err);
                alert('URL 복사에 실패했습니다.');
            });
        });
    }
});
