import os
import re
import html

def clean_html(raw_html):
    """Remove HTML tags from a string."""
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return html.unescape(cleantext)

# Helper function to wrap compatibility types in links
def create_compatibility_links(types_str):
    if not types_str:
        return ""
    
    # Split by comma and space, then filter out empty strings
    types = [t.strip() for t in re.split(r'[,\s]+', types_str) if t.strip()]
    
    links = []
    for t in types:
        # Ensure the type is a valid 4-letter MBTI code before creating a link
        if len(t) == 4 and t.upper() in mbti_data:
            links.append(f'<a href="{t.lower()}.html" class="type-link">{t}</a>')
        else:
            links.append(t) # Append as plain text if not a valid type
            
    return ', '.join(links)

mbti_data = {
    "INTJ": {
        "name": "용의주도한 전략가",
        "description": "INTJ는 <strong>상상력</strong>이 풍부하고 <strong>전략적인 사색가</strong>로, 모든 것 뒤에 숨겨진 패턴을 파악하는 데 능숙합니다. <strong>독립적</strong>이고 <strong>결단력</strong>이 있으며, 높은 <strong>지적 호기심</strong>을 바탕으로 복잡한 문제 해결에 탁월한 능력을 발휘합니다. 지식을 끊임없이 탐구하며, 목표 달성을 위한 <strong>혁신적인 해결책</strong>을 찾는 데 주력합니다.",
        "image": "https://www.16personalities.com/static/images/personality-types/avatars/intj-architect.svg",
        "pros": [
            "분석적 사고: 복잡한 문제를 논리적으로 분석하고 해결하는 데 능합니다.",
            "전략적 사고: 장기적인 관점에서 목표를 설정하고 효율적인 전략을 수립합니다.",
            "독립성: 스스로 판단하고 결정하며, 타인의 의견에 쉽게 휘둘리지 않습니다.",
            "결단력: 한번 결정한 일은 망설임 없이 추진하는 추진력이 있습니다.",
            "지적 호기심: 새로운 지식과 개념을 탐구하는 데 열정적입니다."
        ],
        "cons": [
            "오만함: 자신의 지적 능력을 과신하여 타인을 무시하는 경향이 있을 수 있습니다.",
            "사회성 부족: 감정 표현이 서툴고 타인과의 정서적 교류에 어려움을 느낄 수 있습니다.",
            "비판적: 자신뿐만 아니라 타인에게도 높은 기준을 적용하여 비판적으로 볼 수 있습니다.",
            "고집스러움: 자신의 신념과 판단이 옳다고 확신하면 좀처럼 생각을 바꾸지 않습니다.",
            "지나친 합리성 추구: 때로는 인간적인 감성이나 가치를 간과할 수 있습니다."
        ],
        "compatibility_good": "ENFP, ENTP",
        "compatibility_good_desc": "INTJ의 지적인 면을 존중하고, 활발하고 개방적인 성향으로 INTJ가 세상과 소통하는 데 도움을 줍니다.",
        "compatibility_so_so": "INFP, INFJ, ENTJ, INTP, ISTP, ESTP",
        "compatibility_so_so_desc": "유사한 사고방식을 공유하거나 상호 보완적인 관계를 형성할 수 있습니다.",
        "compatibility_bad": "ESFP, ISFP, ESTJ, ISTJ",
        "compatibility_bad_desc": "현실적이고 즉흥적인 이들 유형은 INTJ의 추상적이고 계획적인 성향과 충돌할 수 있습니다.",
        "celebrities": [
            "아이작 뉴턴", "일론 머스크", "마크 주커버그", "제인 오스틴", "미셸 오바마"
        ],
        "jobs": [
            "과학자, 연구원", "엔지니어, 프로그래머", "변호사, 판사", "경영 컨설턴트, 전략 기획자", "건축가"
        ]
    },
    "INTP": {
        "name": "논리적인 사색가",
        "description": "INTP는 끊임없이 <strong>지식</strong>을 탐구하고 <strong>분석</strong>하며, 복잡한 문제에 대한 <strong>논리적인 해결책</strong>을 찾는 데 즐거움을 느낍니다. 이들은 조용하고 사색적이지만, 내면에는 <strong>아이디어와 가능성</strong>으로 가득 찬 세상을 품고 있습니다. <strong>비판적 사고</strong>와 뛰어난 <strong>분석 능력</strong>을 바탕으로 혁신적인 이론을 제시하는 데 능합니다.",
        "image": "https://www.16personalities.com/static/images/personality-types/avatars/intp-logician.svg",
        "pros": [
            "탁월한 분석력: 복잡한 정보를 빠르게 이해하고 핵심을 파악합니다.",
            "객관적: 감정에 휩쓸리지 않고 논리적이고 객관적으로 상황을 판단합니다.",
            "창의적: 독창적인 아이디어와 해결책을 제시하는 데 능합니다.",
            "독립적: 스스로 생각하고 결정하며, 타인의 간섭을 싫어합니다.",
            "지적 호기심: 끊임없이 배우고 새로운 지식을 탐구합니다."
        ],
        "cons": [
            "비실용적: 추상적인 사고에 몰두하여 현실적인 문제에 둔감할 수 있습니다.",
            "사회성 부족: 감정 표현이 서툴고 타인과의 정서적 교류에 어려움을 느낄 수 있습니다.",
            "게으름: 흥미 없는 일에는 집중하지 못하고 미루는 경향이 있습니다.",
            "지나친 비판: 타인의 아이디어나 의견에 대해 지나치게 비판적일 수 있습니다.",
            "회의적: 모든 것을 의심하고 쉽게 믿지 않는 경향이 있습니다."
        ],
        "compatibility_good": "ENTJ, ESTJ",
        "compatibility_good_desc": "INTP의 아이디어를 현실로 구현할 수 있는 실천력과 리더십을 가진 유형입니다.",
        "compatibility_so_so": "INFP, INFJ, ENTP, INTJ, ISTP, ESTP",
        "compatibility_so_so_desc": "유사한 지적 호기심을 공유하거나 서로의 부족한 부분을 보완해 줄 수 있습니다.",
        "compatibility_bad": "ESFJ, ISFJ, ENFJ, INFJ",
        "compatibility_bad_desc": "감성적이고 관계 중심적인 이들 유형은 INTP의 논리적이고 객관적인 성향을 이해하기 어려울 수 있습니다.",
        "celebrities": [
            "알베르트 아인슈타인", "빌 게이츠", "이사카 뉴턴", "마리 퀴리", "스티븐 호킹"
        ],
        "jobs": [
            "과학자, 이론 물리학자", "프로그래머, 소프트웨어 개발자", "대학교수, 연구원", "철학자", "경제학자"
        ]
    },
    "ENTJ": {
        "name": "대담한 통솔자",
        "description": "ENTJ는 타고난 <strong>리더</strong>로, <strong>비전</strong>을 제시하고 목표를 향해 사람들을 이끄는 데 탁월한 능력을 가지고 있습니다. 이들은 <strong>강한 의지</strong>와 <strong>결단력</strong>을 바탕으로 어떤 어려움도 극복하며, <strong>효율성</strong>과 <strong>생산성</strong>을 중요하게 생각합니다. <strong>논리적</strong>이고 <strong>체계적인 사고</strong>를 통해 복잡한 문제를 해결하고 조직을 성공으로 이끌어갑니다.",
        "image": "https://www.16personalities.com/static/images/personality-types/avatars/entj-commander.svg",
        "pros": [
            "강력한 리더십: 목표를 설정하고 사람들을 이끄는 데 능합니다.",
            "효율적: 시간과 자원을 효과적으로 사용하여 목표를 달성합니다.",
            "전략적 사고: 장기적인 관점에서 계획을 수립하고 실행합니다.",
            "결단력: 빠르고 정확하게 결정을 내리고 실행합니다.",
            "자신감: 자신의 능력과 판단에 대한 강한 확신을 가지고 있습니다."
        ],
        "cons": [
            "권위적: 자신의 의견을 강요하고 타인의 의견을 무시하는 경향이 있습니다.",
            "공감 능력 부족: 타인의 감정을 이해하고 공감하는 데 어려움을 느낄 수 있습니다.",
            "성급함: 결과를 빨리 얻으려 하여 성급하게 행동할 수 있습니다.",
            "지나친 경쟁심: 모든 것을 경쟁으로 보고 이기려 하는 경향이 있습니다.",
            "워커홀릭: 일에 지나치게 몰두하여 번아웃되기 쉽습니다."
        ],
        "compatibility_good": "INFP, INTP",
        "compatibility_good_desc": "ENTJ의 비전을 이해하고 지지하며, 감성적이고 창의적인 아이디어를 제공하여 균형을 맞춰줍니다.",
        "compatibility_so_so": "INFJ, ENFJ, INTJ, ENTP, ISTP, ESTP",
        "compatibility_so_so_desc": "유사한 목표 지향적인 성향을 공유하거나 서로에게 새로운 관점을 제시할 수 있습니다.",
        "compatibility_bad": "ISFJ, ESFJ, ISTJ, ESTJ",
        "compatibility_bad_desc": "전통을 중시하고 변화를 꺼리는 이들 유형은 ENTJ의 혁신적이고 추진력 있는 성향과 갈등할 수 있습니다.",
        "celebrities": [
            "스티브 잡스", "고든 램지", "나폴레옹 보나파르트", "마가렛 대처", "카리스마 넘치는 CEO들"
        ],
        "jobs": [
            "기업 CEO, 경영자", "변호사, 판사", "정치인", "컨설턴트", "프로젝트 매니저"
        ]
    },
    "ENTP": {
        "name": "논쟁을 즐기는 변론가",
        "description": "ENTP는 <strong>똑똑</strong>하고 <strong>호기심</strong>이 많으며, 새로운 <strong>아이디어</strong>와 <strong>도전</strong>을 즐기는 <strong>혁신가</strong>입니다. 이들은 뛰어난 <strong>논리력</strong>과 <strong>언변</strong>으로 어떤 주제에 대해서도 열정적으로 토론하며, <strong>고정관념</strong>을 깨고 새로운 가능성을 탐색하는 데 능합니다. 틀에 얽매이지 않는 <strong>자유로운 사고방식</strong>으로 항상 새로운 것을 추구합니다.",
        "image": "https://www.16personalities.com/static/images/personality-types/avatars/entp-debater.svg",
        "pros": [
            "뛰어난 문제 해결 능력: 복잡한 문제에 대한 독창적인 해결책을 제시합니다.",
            "민첩한 사고: 정보를 빠르게 처리하고 즉흥적으로 대응하는 데 능합니다.",
            "넓은 지식: 다양한 분야에 대한 폭넓은 지식과 흥미를 가지고 있습니다.",
            "유머러스함: 재치 있고 유머러스한 말솜씨로 사람들을 즐겁게 합니다.",
            "도전 정신: 새로운 아이디어와 도전에 두려움 없이 뛰어듭니다."
        ],
        "cons": [
            "산만함: 한 가지 일에 꾸준히 집중하기 어려워 쉽게 질려 합니다.",
            "논쟁적: 논쟁을 즐기며 타인의 의견을 반박하는 데 익숙하여 갈등을 유발할 수 있습니다.",
            "비판적: 타인의 아이디어나 의견에 대해 지나치게 비판적일 수 있습니다.",
            "무책임: 흥미 없는 일에는 무책임하게 행동하거나 마무리가 부족할 수 있습니다.",
            "지나친 자신감: 자신의 능력을 과신하여 실수를 저지를 수 있습니다."
        ],
        "compatibility_good": "INFJ, INTJ",
        "compatibility_good_desc": "ENTP의 아이디어를 이해하고 지지하며, 깊이 있는 통찰력으로 ENTP의 생각에 깊이를 더해줍니다.",
        "compatibility_so_so": "INFP, ENFP, ENFJ, INTP, ISTP, ESTP",
        "compatibility_so_so_desc": "유사한 지적 호기심을 공유하거나 서로에게 새로운 관점을 제시할 수 있습니다.",
        "compatibility_bad": "ISFJ, ESFJ, ISTJ, ESTJ",
        "compatibility_bad_desc": "전통과 규칙을 중시하는 이들 유형은 ENTP의 자유롭고 혁신적인 성향과 충돌할 수 있습니다.",
        "celebrities": [
            "마크 트웨인", "스티브 워즈니악", "톰 행크스", "셀린 디온", "조지 클루니"
        ],
        "jobs": [
            "변호사, 검사", "엔지니어, 발명가", "컨설턴트", "마케터, 홍보 전문가", "대학교수"
        ]
    },
    "INFJ": {
        "name": "선의의 옹호자",
        "description": "INFJ는 <strong>통찰력</strong> 있고 <strong>신비로운</strong> 유형으로, 타인의 감정을 깊이 이해하고 세상을 더 나은 곳으로 만들고자 하는 강한 <strong>열망</strong>을 가지고 있습니다. 이들은 조용하고 내향적이지만, 내면에는 확고한 <strong>신념</strong>과 <strong>이상</strong>을 품고 있습니다. 복잡한 인간 관계와 사회 문제에 깊은 관심을 가지며, <strong>영감</strong>을 통해 타인에게 긍정적인 영향을 미칩니다.",
        "image": "https://www.16personalities.com/static/images/personality-types/avatars/infj-advocate.svg",
        "pros": [
            "통찰력: 타인의 감정과 동기를 깊이 이해하고 미래를 예측하는 데 능합니다.",
            "공감 능력: 타인의 고통에 깊이 공감하고 돕고자 하는 마음이 강합니다.",
            "이상주의: 더 나은 세상을 만들고자 하는 확고한 신념과 열정이 있습니다.",
            "창의력: 독창적인 아이디어와 해결책을 제시하는 데 능합니다.",
            "인내심: 목표를 달성하기 위해 꾸준히 노력하고 인내심을 발휘합니다."
        ],
        "cons": [
            "과도한 이상주의: 현실과 타협하는 것을 어려워하며, 때로는 비현실적일 수 있습니다.",
            "상처받기 쉬움: 비판에 민감하고 쉽게 상처받는 경향이 있습니다.",
            "고립감: 자신의 깊은 생각과 감정을 이해해 주는 사람을 찾기 어려워 외로움을 느낄 수 있습니다.",
            "지나친 완벽주의: 스스로에게 너무 높은 기준을 적용하고 자책하기 쉽습니다.",
            "번아웃: 타인을 돕는 데 에너지를 너무 많이 소모하여 지치기 쉽습니다."
        ],
        "compatibility_good": "ENFP, ENTP",
        "compatibility_good_desc": "INFJ의 깊은 통찰력을 이해하고 지지하며, 밝고 긍정적인 에너지로 INFJ에게 활력을 불어넣어 줍니다.",
        "compatibility_so_so": "INFP, INTJ, ENTJ, INTP, ENFJ, ISTP",
        "compatibility_so_so_desc": "유사한 가치관을 공유하거나 서로에게 새로운 관점을 제시할 수 있습니다.",
        "compatibility_bad": "ESTP, ESFP, ISTJ, ESTJ",
        "compatibility_bad_desc": "현실적이고 즉흥적인 이들 유형은 INFJ의 이상주의적이고 미래 지향적인 성향을 이해하기 어려울 수 있습니다.",
        "celebrities": [
            "마틴 루터 킹 주니어", "넬슨 만델라", "마더 테레사", "오프라 윈프리", "존 크라신스키"
        ],
        "jobs": [
            "상담사, 심리학자", "작가, 예술가", "사회복지사, 자선 활동가", "교사, 교수", "의사, 간호사"
        ]
    },
    "ENFJ": {
        "name": "정의로운 사회운동가",
        "description": "ENFJ는 <strong>따뜻하고</strong> <strong>카리스마 넘치는 리더</strong>로, 사람들의 잠재력을 끌어내고 공동체를 이끄는 데 능숙합니다. 이들은 뛰어난 <strong>공감 능력</strong>과 <strong>의사소통 능력</strong>을 바탕으로 타인과 깊은 관계를 맺으며, 세상을 더 나은 곳으로 만들고자 하는 강한 <strong>열망</strong>을 가지고 있습니다. <strong>긍정적인 영향력</strong>을 통해 사람들에게 영감을 주고 변화를 만들어냅니다.",
        "image": "https://www.16personalities.com/static/images/personality-types/avatars/enfj-protagonist.svg",
        "pros": [
            "뛰어난 리더십: 사람들을 이끌고 동기를 부여하는 데 능합니다.",
            "공감 능력: 타인의 감정을 깊이 이해하고 공감하는 능력이 뛰어납니다.",
            "의사소통 능력: 명확하고 설득력 있게 자신의 생각을 전달합니다.",
            "이타심: 타인을 돕고 공동체에 기여하고자 하는 마음이 강합니다.",
            "카리스마: 사람들을 끌어당기는 매력과 영향력을 가지고 있습니다."
        ],
        "cons": [
            "지나친 책임감: 타인의 문제에 지나치게 개입하여 스트레스를 받을 수 있습니다.",
            "과도한 이상주의: 현실과 타협하는 것을 어려워하며, 때로는 비현실적일 수 있습니다.",
            "갈등 회피: 갈등 상황을 싫어하여 자신의 의견을 제대로 표현하지 못할 수 있습니다.",
            "지나친 자기희생: 타인을 돕기 위해 자신을 희생하는 경향이 있습니다.",
            "비판에 취약: 타인의 비판에 민감하게 반응하고 상처받기 쉽습니다."
        ],
        "compatibility_good": "INFP, INTP",
        "compatibility_good_desc": "ENFJ의 따뜻함과 이상주의를 이해하고 지지하며, 깊이 있는 사고와 통찰력으로 ENFJ에게 영감을 줍니다.",
        "compatibility_so_so": "INFJ, ENTJ, ENTP, ESFJ, ISFJ, ESTJ",
        "compatibility_so_so_desc": "유사한 가치관을 공유하거나 서로에게 새로운 관점을 제시할 수 있습니다.",
        "compatibility_bad": "ISTP, ISFP, ESTP, ESFP",
        "compatibility_bad_desc": "즉흥적이고 현실 중심적인 이들 유형은 ENFJ의 계획적이고 관계 중심적인 성향과 충돌할 수 있습니다.",
        "celebrities": [
            "오프라 윈프리", "버락 오바마", "마야 안젤루", "조 바이든", "벤 애플렉"
        ],
        "jobs": [
            "교사, 교수", "상담사, 심리학자", "정치인, 사회 운동가", "기업 임원, 인사 담당자", "성직자"
        ]
    },
    "ENFP": {
        "name": "재기발랄한 활동가",
        "description": "ENFP는 <strong>열정적</strong>이고 <strong>창의적</strong>이며, 새로운 <strong>가능성</strong>을 탐색하고 사람들과 깊은 관계를 맺는 것을 즐깁니다. 이들은 <strong>밝고 긍정적인 에너지</strong>로 주변을 활기차게 만들며, 뛰어난 <strong>상상력</strong>과 <strong>직관</strong>을 바탕으로 독창적인 아이디어를 제시합니다. <strong>자유롭고 즉흥적인 삶</strong>을 추구하며, 세상을 더 재미있고 의미 있는 곳으로 만들고자 합니다.",
        "image": "https://www.16personalities.com/static/images/personality-types/avatars/enfp-campaigner.svg",
        "pros": [
            "열정적: 모든 일에 열정적으로 임하고 긍정적인 에너지를 발산합니다.",
            "창의력: 독창적인 아이디어와 상상력이 풍부합니다.",
            "사교적: 사람들과 쉽게 어울리고 깊은 관계를 맺는 데 능합니다.",
            "낙천적: 어떤 상황에서도 긍정적인 면을 찾고 희망을 잃지 않습니다.",
            "개방적: 새로운 아이디어와 경험에 대해 개방적이고 유연한 사고를 합니다."
        ],
        "cons": [
            "산만함: 한 가지 일에 꾸준히 집중하기 어려워 쉽게 질려 합니다.",
            "비체계적: 계획성이 부족하고 즉흥적으로 행동하는 경향이 있습니다.",
            "과도한 감정 표현: 자신의 감정을 솔직하게 표현하지만, 때로는 과할 수 있습니다.",
            "지나친 낙천주의: 현실적인 문제를 간과하고 비현실적인 기대를 할 수 있습니다.",
            "결정의 어려움: 여러 가지 가능성 중에서 하나를 선택하는 데 어려움을 느낄 수 있습니다."
        ],
        "compatibility_good": "INFJ, INTJ",
        "compatibility_good_desc": "ENFP의 열정과 아이디어를 이해하고 지지하며, 안정감과 통찰력으로 ENFP에게 균형을 맞춰줍니다.",
        "compatibility_so_so": "INFP, ENFJ, ENTP, ISTP, ESFP, ISFP",
        "compatibility_so_so_desc": "유사한 에너지를 공유하거나 서로의 새로운 관점을 제시할 수 있습니다.",
        "compatibility_bad": "ISTJ, ESTJ, ISFJ, ESFJ",
        "compatibility_bad_desc": "규칙과 전통을 중시하는 이들 유형은 ENFP의 자유롭고 즉흥적인 성향과 충돌할 수 있습니다.",
        "celebrities": [
            "로빈 윌리엄스", "윌 스미스", "오프라 윈프리", "엘렌 드제너러스", "박나래"
        ],
        "jobs": [
            "예술가, 배우, 음악가", "작가, 기자", "컨설턴트, 마케터", "상담사, 코치", "이벤트 플래너"
        ]
    },
    "ISTJ": {
        "name": "청렴결백한 논리주의자",
        "description": "ISTJ는 <strong>책임감</strong>이 강하고 <strong>현실적인</strong> 유형으로, <strong>신뢰</strong>할 수 있고 <strong>체계적인 방식</strong>으로 주어진 임무를 수행합니다. 이들은 <strong>전통</strong>과 <strong>규칙</strong>을 중요하게 생각하며, 세부 사항에 주의를 기울이고 실용적인 해결책을 찾는 데 능합니다. 겉으로는 조용하고 진지해 보이지만, 내면에는 강한 <strong>의무감</strong>과 <strong>헌신</strong>을 가지고 있습니다.",
        "image": "https://www.16personalities.com/static/images/personality-types/avatars/istj-logistician.svg",
        "pros": [
            "책임감: 맡은 일을 성실하게 수행하고 약속을 지킵니다.",
            "현실적: 현실적인 관점에서 문제를 바라보고 실용적인 해결책을 찾습니다.",
            "체계적: 논리적이고 체계적으로 일을 처리하며, 계획성이 뛰어납니다.",
            "신뢰성: 믿을 수 있고 일관성 있는 행동으로 타인에게 신뢰를 줍니다.",
            "정확성: 세부 사항에 주의를 기울이고 오류를 줄이려 노력합니다."
        ],
        "cons": [
            "변화에 대한 저항: 새로운 아이디어나 변화를 받아들이는 데 어려움을 느낄 수 있습니다.",
            "융통성 부족: 규칙과 원칙을 너무 중요하게 생각하여 융통성이 부족할 수 있습니다.",
            "감정 표현 어려움: 자신의 감정을 잘 표현하지 못하고 타인의 감정을 이해하는 데 어려움을 느낄 수 있습니다.",
            "비판적: 타인의 실수나 비효율적인 행동에 대해 비판적일 수 있습니다.",
            "지나친 완벽주의: 스스로에게 너무 높은 기준을 적용하고 자책하기 쉽습니다."
        ],
        "compatibility_good": "ESFP, ESTP",
        "compatibility_good_desc": "ISTJ의 진지함을 이해하고, 밝고 긍정적인 에너지로 ISTJ에게 활력을 불어넣어 줍니다.",
        "compatibility_so_so": "ISTP, ISFP, INTJ, ENTJ, INTP, ENTP",
        "compatibility_so_so_desc": "유사한 현실 중심적인 성향을 공유하거나 서로의 부족한 부분을 보완해 줄 수 있습니다.",
        "compatibility_bad": "INFP, ENFP, INFJ, ENFJ",
        "compatibility_bad_desc": "이상주의적이고 감성적인 이들 유형은 ISTJ의 현실적이고 논리적인 성향을 이해하기 어려울 수 있습니다.",
        "celebrities": [
            "조지 워싱턴", "앙겔라 메르켈", "제프 베이조스", "워렌 버핏", "빌 게이츠"
        ],
        "jobs": [
            "회계사, 재정 전문가", "경찰관, 군인", "공무원", "데이터 분석가", "엔지니어"
        ]
    },
     "ISFJ": {
        "name": "용감한 수호자",
        "description": "ISFJ는 따뜻하고 <strong>헌신적</strong>이며, 주변 사람들을 <strong>보호</strong>하고 돕는 데 최선을 다합니다. 이들은 <strong>책임감</strong>이 강하고 <strong>성실</strong>하며, 세부 사항에 주의를 기울여 <strong>안정적</strong>이고 <strong>조화로운</strong> 환경을 만듭니다. 겉으로는 조용하고 겸손해 보이지만, 내면에는 강한 의지와 <strong>배려심</strong>을 가지고 있습니다.",
        "image": "https://www.16personalities.com/static/images/personality-types/avatars/isfj-defender.svg",
        "pros": [
            "헌신적: 주변 사람들을 보호하고 돕는 데 헌신적입니다.",
            "책임감: 맡은 일을 성실하게 수행하고 약속을 지킵니다.",
            "세심함: 세부 사항에 주의를 기울이고 타인의 필요를 잘 파악합니다.",
            "친절함: 따뜻하고 친절한 태도로 타인에게 편안함을 줍니다.",
            "실용적: 현실적인 관점에서 문제를 바라보고 실용적인 해결책을 찾습니다."
        ],
        "cons": [
            "지나친 겸손: 자신의 능력이나 성과를 과소평가하는 경향이 있습니다.",
            "갈등 회피: 갈등 상황을 싫어하여 자신의 의견을 제대로 표현하지 못할 수 있습니다.",
            "변화에 대한 저항: 새로운 아이디어나 변화를 받아들이는 데 어려움을 느낄 수 있습니다.",
            "자기희생: 타인을 돕기 위해 자신을 희생하는 경향이 있습니다.",
            "스트레스에 취약: 타인의 어려움이나 부정적인 감정에 쉽게 영향을 받고 스트레스를 받을 수 있습니다."
        ],
        "compatibility_good": "ESTP, ESFP",
        "compatibility_good_desc": "ISFJ의 따뜻함과 헌신을 이해하고, 밝고 긍정적인 에너지로 ISFJ에게 활력을 불어넣어 줍니다.",
        "compatibility_so_so": "ISTP, ISFP, ENTJ, ENFJ, ESTJ, ISTJ",
        "compatibility_so_so_desc": "유사한 책임감을 공유하거나 서로의 부족한 부분을 보완해 줄 수 있습니다.",
        "compatibility_bad": "INFP, ENFP, INFJ, ENTP",
        "compatibility_bad_desc": "이상주의적이고 즉흥적인 이들 유형은 ISFJ의 현실적이고 계획적인 성향을 이해하기 어려울 수 있습니다.",
        "celebrities": [
            "엘리자베스 2세", "셀레나 고메즈", "비욘세", "캡틴 아메리카 (가상)", "닥터 왓슨 (가상)"
        ],
        "jobs": [
            "간호사, 의료 종사자", "교사, 보육교사", "사회복지사, 상담사", "사서", "행정직"
        ]
    },
    "ESTJ": {
        "name": "엄격한 관리자",
        "description": "ESTJ는 <strong>실용적</strong>이고 <strong>체계적</strong>이며, <strong>규칙</strong>과 <strong>질서</strong>를 중요하게 생각하여 조직을 효율적으로 <strong>관리</strong>하고 이끌어갑니다. 이들은 <strong>책임감</strong>이 강하고 <strong>솔직</strong>하며, 현실적인 목표를 설정하고 이를 달성하기 위해 꾸준히 노력합니다. 뛰어난 <strong>추진력</strong>과 <strong>리더십</strong>으로 어떤 상황에서도 안정적인 결과를 만들어냅니다.",
        "image": "https://www.16personalities.com/static/images/personality-types/avatars/estj-executive.svg",
        "pros": [
            "강한 책임감: 맡은 일을 완벽하게 수행하고 약속을 지킵니다.",
            "실용적: 현실적인 관점에서 문제를 바라보고 효율적인 해결책을 찾습니다.",
            "체계적: 논리적이고 체계적으로 일을 처리하며, 계획성이 뛰어납니다.",
            "리더십: 사람들을 이끌고 조직을 관리하는 데 능합니다.",
            "솔직함: 솔직하고 직접적으로 자신의 생각을 표현합니다."
        ],
        "cons": [
            "융통성 부족: 규칙과 원칙을 너무 중요하게 생각하여 융통성이 부족할 수 있습니다.",
            "권위적: 자신의 의견을 강요하고 타인의 의견을 무시하는 경향이 있습니다.",
            "감정 표현 어려움: 자신의 감정을 잘 표현하지 못하고 타인의 감정을 이해하는 데 어려움을 느낄 수 있습니다.",
            "변화에 대한 저항: 새로운 아이디어나 변화를 받아들이는 데 어려움을 느낄 수 있습니다.",
            "지나친 업무 몰두: 일에 지나치게 몰두하여 번아웃되기 쉽습니다."
        ],
        "compatibility_good": "INTP, ISTP",
        "compatibility_good_desc": "ESTJ의 현실적인 계획을 이해하고, 논리적이고 객관적인 사고로 ESTJ의 결정에 도움을 줍니다.",
        "compatibility_so_so": "ISTJ, ISFJ, ENTJ, ENFJ, ESTP, ESFP",
        "compatibility_so_so_desc": "유사한 책임감을 공유하거나 서로의 부족한 부분을 보완해 줄 수 있습니다.",
        "compatibility_bad": "INFP, ENFP, INFJ, ENTP",
        "compatibility_bad_desc": "이상주의적이고 즉흥적인 이들 유형은 ESTJ의 현실적이고 계획적인 성향을 이해하기 어려울 수 있습니다.",
        "celebrities": [
            "힐러리 클린턴", "존 D. 록펠러", "조지 W. 부시", "오윤아", "박명수"
        ],
        "jobs": [
            "기업 임원, 경영자", "군 장교, 경찰 간부", "공무원", "교사, 교육 행정가", "변호사"
        ]
    },
    "ESFJ": {
        "name": "사교적인 외교관",
        "description": "ESFJ는 따뜻하고 <strong>사교적</strong>이며, 주변 사람들과의 <strong>조화로운 관계</strong>를 중요하게 생각합니다. 이들은 뛰어난 <strong>공감 능력</strong>과 <strong>친화력</strong>을 바탕으로 사람들에게 편안함을 주며, 공동체에 봉사하고 타인을 돕는 데 기쁨을 느낍니다. <strong>책임감</strong>이 강하고 <strong>배려심</strong>이 깊어 어디에서나 환영받는 존재입니다.",
        "image": "https://www.16personalities.com/static/images/personality-types/avatars/esfj-consul.svg",
        "pros": [
            "사교적: 사람들과 쉽게 어울리고 깊은 관계를 맺는 데 능합니다.",
            "친절함: 따뜻하고 친절한 태도로 타인에게 편안함을 줍니다.",
            "공감 능력: 타인의 감정을 깊이 이해하고 공감하는 능력이 뛰어납니다.",
            "책임감: 맡은 일을 성실하게 수행하고 약속을 지킵니다.",
            "헌신적: 주변 사람들을 보호하고 돕는 데 헌신적입니다."
        ],
        "cons": [
            "타인의 시선 의식: 타인의 평가에 민감하게 반응하고 자신을 희생하는 경향이 있습니다.",
            "갈등 회피: 갈등 상황을 싫어하여 자신의 의견을 제대로 표현하지 못할 수 있습니다.",
            "변화에 대한 저항: 새로운 아이디어나 변화를 받아들이는 데 어려움을 느낄 수 있습니다.",
            "지나친 오지랖: 타인의 문제에 지나치게 개입하여 스트레스를 받을 수 있습니다.",
            "감정적: 논리보다는 감정에 기반하여 판단하는 경향이 있습니다."
        ],
        "compatibility_good": "ISTP, INTP",
        "compatibility_good_desc": "ESFJ의 따뜻함과 배려를 이해하고, 객관적이고 논리적인 사고로 ESFJ에게 현실적인 조언을 줍니다.",
        "compatibility_so_so": "ISTJ, ISFJ, ENFJ, ESTJ, ESFP, ISFP",
        "compatibility_so_so_desc": "유사한 책임감을 공유하거나 서로에게 새로운 관점을 제시할 수 있습니다.",
        "compatibility_bad": "INFP, ENFP, INFJ, ENTJ",
        "compatibility_bad_desc": "이상주의적이고 개인주의적인 이들 유형은 ESFJ의 관계 중심적이고 조화로운 성향을 이해하기 어려울 수 있습니다.",
        "celebrities": [
            "앤 해서웨이", "제니퍼 가너", "테일러 스위프트", "박보검", "이효리"
        ],
        "jobs": [
            "교사, 보육교사", "간호사, 의료 종사자", "사회복지사, 상담사", "이벤트 플래너", "고객 서비스"
        ]
    },
    "ISTP": {
        "name": "만능 재주꾼",
        "description": "ISTP는 <strong>호기심</strong> 많고 <strong>실용적인</strong> 유형으로, 주변 세상을 탐색하고 직접 손으로 문제를 해결하는 것을 즐깁니다. 이들은 조용하고 <strong>관찰력</strong>이 뛰어나며, <strong>논리적</strong>이고 <strong>객관적인 사고</strong>를 통해 효율적인 해결책을 찾아냅니다. <strong>자유롭고 즉흥적인 삶</strong>을 추구하며, 새로운 기술과 경험에 대한 <strong>탐구심</strong>이 강합니다.",
        "image": "https://www.16personalities.com/static/images/personality-types/avatars/istp-virtuoso.svg",
        "pros": [
            "실용적: 현실적인 관점에서 문제를 바라보고 효율적인 해결책을 찾습니다.",
            "뛰어난 문제 해결 능력: 복잡한 문제를 논리적으로 분석하고 해결하는 데 능합니다.",
            "적응력: 어떤 상황에도 빠르게 적응하고 유연하게 대처합니다.",
            "독립적: 스스로 판단하고 결정하며, 타인의 간섭을 싫어합니다.",
            "호기심: 새로운 기술과 경험에 대한 탐구심이 강합니다."
        ],
        "cons": [
            "감정 표현 어려움: 자신의 감정을 잘 표현하지 못하고 타인의 감정을 이해하는 데 어려움을 느낄 수 있습니다.",
            "무관심: 흥미 없는 일에는 무관심하고 집중하지 못하는 경향이 있습니다.",
            "충동적: 즉흥적이고 충동적으로 행동하여 후회할 수 있습니다.",
            "규칙 무시: 규칙이나 원칙에 얽매이는 것을 싫어하여 무시하는 경향이 있습니다.",
            "갈등 회피: 갈등 상황을 싫어하여 자신의 의견을 제대로 표현하지 못할 수 있습니다."
        ],
        "compatibility_good": "ESFJ, ESTJ",
        "compatibility_good_desc": "ISTP의 실용적인 능력을 이해하고, 안정적이고 체계적인 방식으로 ISTP에게 현실적인 조언을 줍니다.",
        "compatibility_so_so": "INTP, ENTJ, INFP, ENTP, ISFP, ESTP",
        "compatibility_so_so_desc": "유사한 실용적인 사고방식을 공유하거나 서로에게 새로운 관점을 제시할 수 있습니다.",
        "compatibility_bad": "ENFJ, INFJ, ESFP, ISFJ",
        "compatibility_bad_desc": "감성적이고 관계 중심적인 이들 유형은 ISTP의 논리적이고 독립적인 성향을 이해하기 어려울 수 있습니다.",
        "celebrities": [
            "클린트 이스트우드", "스티브 잡스", "브루스 리", "올리비아 와일드", "정우성"
        ],
        "jobs": [
            "엔지니어, 기술자", "정비사", "프로그래머", "경찰관, 소방관", "운동선수"
        ]
    },
    "ISFP": {
        "name": "호기심 많은 예술가",
        "description": "ISFP는 따뜻하고 겸손하며, 자신의 내면세계와 <strong>아름다움</strong>을 추구하는 <strong>예술가</strong>입니다. 이들은 <strong>자유롭고 즉흥적인 삶</strong>을 즐기며, 현재의 순간을 소중히 여깁니다. 뛰어난 <strong>미적 감각</strong>과 <strong>감수성</strong>을 바탕으로 예술적인 표현에 능하며, 타인의 감정을 깊이 이해하고 공감하는 능력이 뛰어납니다.",
        "image": "https://www.16personalities.com/static/images/personality-types/avatars/isfp-adventurer.svg",
        "pros": [
            "예술적 감각: 뛰어난 미적 감각과 창의력을 가지고 있습니다.",
            "따뜻함: 따뜻하고 친절한 태도로 타인에게 편안함을 줍니다.",
            "공감 능력: 타인의 감정을 깊이 이해하고 공감하는 능력이 뛰어납니다.",
            "겸손함: 자신의 능력이나 성과를 과소평가하는 경향이 있습니다.",
            "개방적: 새로운 경험과 아이디어에 대해 개방적이고 유연한 사고를 합니다."
        ],
        "cons": [
            "비판에 취약: 타인의 비판에 민감하게 반응하고 상처받기 쉽습니다.",
            "계획성 부족: 계획성이 부족하고 즉흥적으로 행동하는 경향이 있습니다.",
            "갈등 회피: 갈등 상황을 싫어하여 자신의 의견을 제대로 표현하지 못할 수 있습니다.",
            "지나친 겸손: 자신의 능력이나 성과를 과소평가하는 경향이 있습니다.",
            "스트레스에 취약: 타인의 어려움이나 부정적인 감정에 쉽게 영향을 받고 스트레스를 받을 수 있습니다."
        ],
        "compatibility_good": "ESFJ, ESTJ",
        "compatibility_good_desc": "ISFP의 따뜻함과 예술적 감각을 이해하고, 안정적이고 체계적인 방식으로 ISFP에게 현실적인 조언을 줍니다.",
        "compatibility_so_so": "ISTP, ENFP, ESFP, INFP, ENTP, INFJ",
        "compatibility_so_so_desc": "유사한 자유로운 영혼을 공유하거나 서로에게 새로운 관점을 제시할 수 있습니다.",
        "compatibility_bad": "INTJ, ENTJ, ISTJ, INTP",
        "compatibility_bad_desc": "논리적이고 계획적인 이들 유형은 ISFP의 즉흥적이고 감성적인 성향을 이해하기 어려울 수 있습니다.",
        "celebrities": [
            "마이클 잭슨", "아브릴 라빈", "레이디 가가", "브리트니 스피어스", "유재석"
        ],
        "jobs": [
            "예술가, 음악가, 디자이너", "사진작가", "작가", "수의사", "자유로운 직업"
        ]
    },
    "ESTP": {
        "name": "모험을 즐기는 사업가",
        "description": "ESTP는 <strong>에너지</strong> 넘치고 <strong>즉흥적</strong>이며, 현재의 순간을 즐기고 새로운 경험에 <strong>도전</strong>하는 것을 좋아합니다. 이들은 현실적인 문제 해결에 능숙하고, 뛰어난 <strong>관찰력</strong>과 <strong>빠른 판단력</strong>으로 어떤 상황에서도 유연하게 대처합니다. 사람들과 어울리는 것을 즐기며, <strong>유머러스</strong>하고 <strong>매력적인</strong> 태도로 주변을 활기차게 만듭니다.",
        "image": "https://www.16personalities.com/static/images/personality-types/avatars/estp-entrepreneur.svg",
        "pros": [
            "실용적: 현실적인 문제 해결에 능숙하고 효율적인 방법을 찾습니다.",
            "적응력: 어떤 상황에도 빠르게 적응하고 유연하게 대처합니다.",
            "에너지 넘침: 활기차고 긍정적인 에너지로 주변을 즐겁게 합니다.",
            "사교적: 사람들과 쉽게 어울리고 대화하는 것을 즐깁니다.",
            "모험심: 새로운 경험과 도전에 두려움 없이 뛰어듭니다."
        ],
        "cons": [
            "충동적: 즉흥적이고 충동적으로 행동하여 후회할 수 있습니다.",
            "무관심: 흥미 없는 일에는 무관심하고 집중하지 못하는 경향이 있습니다.",
            "규칙 무시: 규칙이나 원칙에 얽매이는 것을 싫어하여 무시하는 경향이 있습니다.",
            "지나친 경쟁심: 모든 것을 경쟁으로 보고 이기려 하는 경향이 있습니다.",
            "장기 계획 부족: 현재에 집중하여 장기적인 계획을 소홀히 할 수 있습니다."
        ],
        "compatibility_good": "ISFJ, ISTJ",
        "compatibility_good_desc": "ESTP의 활기찬 에너지를 이해하고, 안정감과 책임감으로 ESTP에게 현실적인 조언을 줍니다.",
        "compatibility_so_so": "ISTP, ESFP, ENTJ, ENTP, INTP, ESTJ",
        "compatibility_so_so_desc": "유사한 실용적인 사고방식을 공유하거나 서로에게 새로운 관점을 제시할 수 있습니다.",
        "compatibility_bad": "INFJ, INFP, ENFJ, ENFP",
        "compatibility_bad_desc": "이상주의적이고 감성적인 이들 유형은 ESTP의 현실적이고 즉흥적인 성향을 이해하기 어려울 수 있습니다.",
        "celebrities": [
            "도널드 트럼프", "마돈나", "제임스 본드 (가상)", "잭 니콜슨", "이서진"
        ],
        "jobs": [
            "영업, 마케터", "경찰관, 소방관", "운동선수, 코치", "사업가, 기업가", "요리사"
        ]
    },
    "ESFP": {
        "name": "자유로운 연예인",
        "description": "ESFP는 <strong>사교적</strong>이고 <strong>활기차며</strong>, 주변 사람들을 즐겁게 하고 <strong>현재의 순간</strong>을 만끽하는 것을 좋아합니다. 이들은 뛰어난 <strong>유머 감각</strong>과 <strong>친화력</strong>을 바탕으로 사람들과 쉽게 어울리며, <strong>즉흥적</strong>이고 <strong>자유로운 삶</strong>을 추구합니다. 따뜻하고 관대하며, 타인의 필요를 잘 파악하고 돕는 데 기쁨을 느낍니다.",
        "image": "https://www.16personalities.com/static/images/personality-types/avatars/esfp-entertainer.svg",
        "pros": [
            "사교적: 사람들과 쉽게 어울리고 대화하는 것을 즐깁니다.",
            "활기참: 밝고 긍정적인 에너지로 주변을 즐겁게 합니다.",
            "유머러스함: 재치 있고 유머러스한 말솜씨로 사람들을 즐겁게 합니다.",
            "관대함: 따뜻하고 관대한 태도로 타인에게 편안함을 줍니다.",
            "적응력: 어떤 상황에도 빠르게 적응하고 유연하게 대처합니다."
        ],
        "cons": [
            "산만함: 한 가지 일에 꾸준히 집중하기 어려워 쉽게 질려 합니다.",
            "충동적: 즉흥적이고 충동적으로 행동하여 후회할 수 있습니다.",
            "계획성 부족: 계획성이 부족하고 즉흥적으로 행동하는 경향이 있습니다.",
            "갈등 회피: 갈등 상황을 싫어하여 자신의 의견을 제대로 표현하지 못할 수 있습니다.",
            "지나친 타인의식: 타인의 평가에 민감하게 반응하고 자신을 희생하는 경향이 있습니다."
        ],
        "compatibility_good": "ISTJ, ISFJ",
        "compatibility_good_desc": "ESFP의 활기찬 에너지를 이해하고, 안정감과 책임감으로 ESFP에게 현실적인 조언을 줍니다.",
        "compatibility_so_so": "ISTP, ESTP, ENFP, ESFJ, ISFP, ENFJ",
        "compatibility_so_so_desc": "유사한 낙천적인 성향을 공유하거나 서로에게 새로운 관점을 제시할 수 있습니다.",
        "compatibility_bad": "INTJ, ENTJ, INFP, INFJ",
        "compatibility_bad_desc": "논리적이고 계획적인 이들 유형은 ESFP의 즉흥적이고 감성적인 성향을 이해하기 어려울 수 있습니다.",
        "celebrities": [
            "엘비스 프레슬리", "마릴린 먼로", "레오나르도 디카프리오", "정준하", "수지"
        ],
        "jobs": [
            "배우, 연예인", "가수, 음악가", "이벤트 플래너", "유치원 교사", "여행 가이드"
        ]
    },
    "INFP": {
        "name": "열정적인 중재자",
        "description": "INFP는 <strong>이상주의적</strong>이고 <strong>창의적인</strong> 성향을 가진 사람들로, 자신의 <strong>가치관</strong>과 <strong>신념</strong>에 따라 살아갑니다. 이들은 깊은 <strong>감수성</strong>과 <strong>공감 능력</strong>을 바탕으로 다른 사람들을 돕고자 하는 열망이 강하며, 세상에 긍정적인 영향을 미치고 싶어 합니다. 겉으로는 조용하고 수줍어 보일 수 있지만, 내면에는 강렬한 <strong>열정</strong>과 불꽃을 품고 있습니다.",
        "image": "https://www.16personalities.com/static/images/personality-types/avatars/infp-mediator.svg",
        "pros": [
            "공감 능력: 타인의 감정을 깊이 이해하고 공감하는 능력이 뛰어납니다.",
            "창의력: 상상력이 풍부하고 독창적인 아이디어를 많이 가지고 있습니다.",
            "이상주의: 더 나은 세상을 만들고자 하는 강한 신념과 열정이 있습니다.",
            "개방성: 새로운 아이디어와 경험에 대해 개방적이고 유연한 사고를 합니다.",
            "강한 가치관: 자신의 신념과 가치관을 중요하게 생각하며, 이에 따라 행동합니다."
        ],
        "cons": [
            "지나친 이상주의: 현실과 타협하는 것을 어려워하며, 때로는 비현실적일 수 있습니다.",
            "상처받기 쉬움: 비판에 민감하고 쉽게 상처받는 경향이 있습니다.",
            "실용성 부족: 일상적이고 세부적인 일을 처리하는 데 어려움을 겪을 수 있습니다.",
            "과도한 자기 비판: 스스로에게 너무 높은 기준을 적용하고 자책하기 쉽습니다.",
            "결정의 어려움: 중요한 결정을 내리는 데 오랜 시간이 걸릴 수 있습니다."
        ],
        "compatibility_good": "ENFJ, ENTJ",
        "compatibility_good_desc": "INFP의 이상과 가치를 이해하고 지지해주며, 현실적인 실행력을 더해줄 수 있는 유형입니다. 이들은 INFP가 자신의 잠재력을 최대한 발휘하도록 돕습니다.",
        "compatibility_so_so": "INFP, ENFP, INFJ, INTJ, INTP, ENTP",
        "compatibility_so_so_desc": "유사한 가치관이나 사고방식을 공유하여 편안함을 느끼지만, 때로는 서로의 단점을 보완해주지 못할 수도 있습니다.",
        "compatibility_bad": "ISTJ, ESTJ, ISFJ, ESFJ",
        "compatibility_bad_desc": "현실적이고 실용적인 이들 유형은 INFP의 이상주의적인 면을 이해하기 어려워하며, 가치관의 차이로 인해 갈등이 발생할 수 있습니다.",
        "celebrities": [
            "윌리엄 셰익스피어", "J.R.R. 톨킨", "조니 뎁", "아이유", "톰 히들스턴"
        ],
        "jobs": [
            "작가, 시인, 예술가", "상담사, 심리학자, 사회복지사", "디자이너, 영상 제작자", "교사, 교수", "비영리 단체 활동가"
        ]
    }
}


def generate_mbti_page(mbti_type, data):
    # This function is now defined at the top level
    # so it can be used inside generate_mbti_page
    
    clean_description = clean_html(data['description'])
    page_url = f"https://product-lecture.pages.dev/results/{mbti_type.lower()}.html"
    
    template = f"""<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MBTI 유형: {mbti_type} - {data['name']}</title>
    <link rel="canonical" href="{page_url}">
    <meta http-equiv="content-language" content="ko">
    <meta name="description" content="MBTI 성격 유형 {mbti_type}({data['name']})의 특징, 장단점, 궁합, 추천 직업, 유명인 등 상세 정보를 확인해보세요.">
    <meta name="keywords" content="MBTI, {mbti_type}, {data['name']}, 성격 유형, 성격 테스트, MBTI 검사">
    
    <!-- Open Graph / Facebook -->
    <meta property="og:type" content="article">
    <meta property="og:url" content="{page_url}">
    <meta property="og:title" content="MBTI 유형: {mbti_type} - {data['name']}">
    <meta property="og:description" content="{clean_description}">
    <meta property="og:image" content="{data['image']}">

    <!-- Twitter -->
    <meta property="twitter:card" content="summary_large_image">
    <meta property="twitter:url" content="{page_url}">
    <meta property="twitter:title" content="MBTI 유형: {mbti_type} - {data['name']}">
    <meta property="twitter:description" content="{clean_description}">
    <meta property="twitter:image" content="{data['image']}">

    <link rel="stylesheet" href="../style.css">

    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "Article",
      "headline": "MBTI 유형: {mbti_type} - {data['name']}",
      "image": "{data['image']}",
      "author": {{
        "@type": "Organization",
        "name": "MBTI 성격 유형 검사"
      }},
      "publisher": {{
        "@type": "Organization",
        "name": "MBTI 성격 유형 검사",
        "logo": {{
          "@type": "ImageObject",
          "url": "https://product-lecture.pages.dev/assets/logo.png"
        }}
      }},
      "url": "{page_url}",
      "description": "{clean_description}"
    }}
    </script>
</head>
<body>
    <header>
        <div class="container">
            <h1><a href="../index.html">MBTI 성격 유형 검사</a></h1>
            <nav>
                <ul>
                    <li><a href="../index.html">검사하기</a></li>
                    <li><a href="../results/all_types.html">모든 유형 보기</a></li>
                    <li><a href="../pages/about.html">소개</a></li>
                    <li><a href="../pages/contact.html">문의하기</a></li>
                </ul>
            </nav>
        </div>
    </header>
    <main class="result-page">
        <section class="mbti-type-intro">
            <h2>{mbti_type}: {data['name']}</h2>
            <img src="{data['image']}" alt="{mbti_type} ({data['name']})" class="mbti-avatar" loading="lazy">
            <p class="mbti-description">
                {data['description']}
            </p>
        </section>

        <section class="mbti-details">
            <h3>{mbti_type}의 장점과 단점</h3>
            <div class="pros-cons">
                <div class="pros">
                    <h4>✅ 장점</h4>
                    <ul>
                        {''.join(f'<li><strong>{p.split(":")[0]}:</strong> {p.split(":")[1].strip()}</li>' for p in data['pros'])}
                    </ul>
                </div>
                <div class="cons">
                    <h4>⚠️ 단점</h4>
                    <ul>
                        {''.join(f'<li><strong>{c.split(":")[0]}:</strong> {c.split(":")[1].strip()}</li>' for c in data['cons'])}
                    </ul>
                </div>
            </div>
        </section>

        <section class="mbti-compatibility">
            <h3>❤️ 궁합이 잘 맞는 유형</h3>
            <div class="compatibility-grid">
                <div class="type-card good">
                    <h4>최고의 궁합</h4>
                    <p class="comp-types">{create_compatibility_links(data['compatibility_good'])}</p>
                    <p>{data['compatibility_good_desc']}</p>
                </div>
                <div class="type-card so-so">
                    <h4>나쁘지 않은 궁합</h4>
                    <p class="comp-types">{create_compatibility_links(data['compatibility_so_so'])}</p>
                    <p>{data['compatibility_so_so_desc']}</p>
                </div>
                <div class="type-card bad">
                    <h4>최악의 궁합</h4>
                    <p class="comp-types">{create_compatibility_links(data['compatibility_bad'])}</p>
                    <p>{data['compatibility_bad_desc']}</p>
                </div>
            </div>
        </section>

        <section class="mbti-celebs">
            <h3>✨ {mbti_type} 유명인</h3>
            <ul>
                {''.join(f'<li>{celeb}</li>' for celeb in data['celebrities'])}
            </ul>
        </section>

        <section class="mbti-jobs">
            <h3>💼 추천 직업</h3>
            <ul>
                {''.join(f'<li>{job}</li>' for job in data['jobs'])}
            </ul>
        </section>

        <section class="share-result">
            <h3>📈 결과 공유하기</h3>
            <div class="share-buttons">
                <button id="kakao-share-btn" class="share-btn kakao">
                    카카오톡으로 공유
                </button>
                <button id="copy-url-btn" class="share-btn url-copy">
                    🔗 URL 복사
                </button>
            </div>
        </section>
    </main>
    <footer>
        <p>&copy; 2026 MBTI Personality Test. All rights reserved.</p>
        <p><a href="../pages/privacy.html">개인정보처리방침</a> | <a href="../pages/terms.html">이용약관</a></p>
    </footer>
    
    <!-- Kakao SDK -->
    <script src="https://t1.kakaocdn.net/kakao_js_sdk/2.7.0/kakao.min.js"></script>
    <!-- Custom Share Script -->
    <script src="../share.js"></script>
    <script defer src="../scripts/ui.js"></script>
</body>
</html>
"""
    return template

if not os.path.exists("results"):
    os.makedirs("results")

# This populates the pages for all 16 types from the dictionary
for mbti_type, data in mbti_data.items():
    file_path = os.path.join("results", f"{mbti_type.lower()}.html")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(generate_mbti_page(mbti_type, data))
    print(f"Generated {file_path}")

print("All MBTI pages generated successfully!")
