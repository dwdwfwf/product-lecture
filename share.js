document.addEventListener('DOMContentLoaded', () => {
    // 1. Kakao SDK Initialization
    try {
        const KAKAO_APP_KEY = '6e2ffc8b4e5748eb04db8f93a2063e98';
        Kakao.init(KAKAO_APP_KEY);
        console.log('Kakao SDK initialized:', Kakao.isInitialized());
    } catch (e) {
        console.error("Error initializing Kakao SDK:", e);
        alert('카카오 SDK를 초기화하는 데 실패했습니다. 잠시 후 다시 시도해주세요.');
    }

    // 2. Element Selectors
    const kakaoShareBtn = document.getElementById('kakao-share-btn');
    const copyUrlBtn = document.getElementById('copy-url-btn');

    if (kakaoShareBtn) {
        kakaoShareBtn.addEventListener('click', () => {
            if (!Kakao.isInitialized()) {
                alert('카카오 SDK가 초기화되지 않았습니다. 페이지를 새로고침 후 다시 시도해주세요.');
                return;
            }

            // Extract MBTI info from the page
            const mbtiType = document.querySelector('.mbti-type-intro h2')?.innerText.split(':')[0] || 'MBTI';
            const mbtiName = document.querySelector('.mbti-type-intro h2')?.innerText.split(':')[1]?.trim() || '성격 유형';
            const mbtiDescription = document.querySelector('.mbti-description')?.innerText;
            const mbtiImage = document.querySelector('.mbti-avatar')?.src;
            const pageUrl = window.location.href;

            const shareData = {
                objectType: 'feed',
                content: {
                    title: `내 MBTI 결과는? ${mbtiType} ${mbtiName}`,
                    description: mbtiDescription,
                    imageUrl: mbtiImage,
                    link: {
                        mobileWebUrl: pageUrl,
                        webUrl: pageUrl,
                    },
                },
                buttons: [
                    {
                        title: '결과 자세히 보기',
                        link: {
                            mobileWebUrl: pageUrl,
                            webUrl: pageUrl,
                        },
                    },
                    {
                        title: '나도 검사하기',
                        link: {
                            mobileWebUrl: window.location.origin,
                            webUrl: window.location.origin,
                        },
                    },
                ],
            };
            
            console.log("Sending data to Kakao:", JSON.stringify(shareData, null, 2));

            try {
                Kakao.Share.sendDefault(shareData);
            } catch(err) {
                console.error("Kakao.Share.sendDefault error:", err);
                alert("카카오톡 공유에 실패했습니다. 잠시 후 다시 시도해주세요.");
            }
        });
    }

    if (copyUrlBtn) {
        copyUrlBtn.addEventListener('click', () => {
            const urlToCopy = window.location.href;

            navigator.clipboard.writeText(urlToCopy).then(() => {
                const originalText = copyUrlBtn.innerHTML;
                copyUrlBtn.innerHTML = '✅ 복사 완료!';
                copyUrlBtn.disabled = true;

                setTimeout(() => {
                    copyUrlBtn.innerHTML = originalText;
                    copyUrlBtn.disabled = false;
                }, 2000);
            }).catch(err => {
                console.error('Failed to copy URL:', err);
                alert('URL 복사에 실패했습니다.');
            });
        });
    }
});
