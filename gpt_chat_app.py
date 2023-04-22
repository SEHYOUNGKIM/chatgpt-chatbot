import openai
import streamlit as st


def show_messages(text):
    messages_str = [
        f"{_['role']}: {_['content']}" for _ in st.session_state["messages"][-2:]
    ]
    text.text_area("Messages", value=str("\n".join(messages_str)), height=400)


API_KEY = st.sidebar.text_input(":blue[Enter Your OPENAI API-KEY :]", 
                placeholder="Paste your OpenAI API key here (sk-...)",
                type="password") # Session state storage would be ideal

openai.api_key = API_KEY

BASE_PROMPT = [
        {"role": "system", "content": "이 프로그램은 글에서 최신 기술 용어를 {용어: 의미} 형태로 설명해주는 어시스턴트야."},
        {"role": "user", "content": """
        5세대 이동통신(5G) 상용망이 도심항공교통(UAM)을 위한 통신 수단으로 쓰일 것 같지는 않다. 신용식 SK텔레콤 부사장은 지난 19일 서울 강남구 코엑스에서 열린 '월드 IT쇼'에 참석해 이렇게 말했다. 지상에 보편적으로 쓰이는 3.5기가헤르츠(㎓) 대역의 5G 상용망을 상공 300~600미터에 뜨는 UAM에 당장 적용하기엔 어렵다는 고민이 묻어났다. 정해진 게 없는 UAM 항공망
UAM은 수직 이착륙하는 항공기를 통해 사람이나 화물을 운송하는 무인 교통체계를 뜻한다. UAM은 초고속·초저지연 통신망을 연결한 상태로 운용돼야 하는데, UAM이 마주할 수 있는 위험 상황에 즉각적으로 반응해야 하기 때문이다. SK텔레콤 관계자는 "아직 UAM망에 대한 표준화가 이뤄지지 않은 상태여서 신 부사장이 그렇게 말한 것"이라고 말했다. 실제로 신 부사장은 지난해 7월 과학기술정보통신부가 주최한 '제6차 디지털 국정과제 연속 현장 간담회'에서 "UAM을 운항하려면 관제, 통신, 안전, 엔터테인먼트 등을 위한 주파수가 필수적인데 아직 어느 하나 정해진 것이 없다"며 "정부가 산업계와 고민하며 만들어나가야 한다"고 했다. "지상용 통신망으론 어려워" UAM에 적용할 국제 표준이 없는 데다 현재 5G 상용망 기술을 UAM에 바로 쓰기에도 어려운 상황이다. 배재성 한국항공대 항공우주·기계공학부 교수는 "LTE, 5G 외에 현재 원거리용 민간 통신망으로 쓸 수 있는 게 없다고 봐야 한다"며 "두 망 모두 스마트폰과 같은 일반 단말기용으로 쓰이는 지상 통신이기에 UAM에 적합하다고 볼 수 없다"고 말했다.
또 사람과 물건을 실어 나르는 UAM의 기본 기능 외에 타 교통수단과 연계 등의 부가적인 서비스의 원활한 제공도 어려울 수 있다. 가령 SK텔레콤의 경우 자사의 내비게이션 서비스인 '티맵'을 활용해 UAM에서 내리면 다른 교통수단을 예약할 수 있는 서비스형모빌리티(MaaS)를 계획 중인데, 현재 상용망으론 지상에서 느끼는 쾌적한 속도만큼은 누릴 수 없다는 것이다.
배 교수는 "UAM에 다양한 서비스가 결합되는 것은 당연하다"면서도 "시스템이 복잡해질수록 통신 속도가 느려질 수 있기 때문에 그 문제점을 잡는 것이 관건"이라고 말했다.
결국 답은 위성통신?
지상통신에 최적화된 3.5㎓ 5G 상용망의 대안으로 C대역 이상의 고주파 활용 가능성이 부각되고 있다. 주파수 대역이 높으면 높을수록 정보를 빠르게 주고 받을 수 있는 장점이 있기 때문이다.
C대역은 미국 전기전자학회에서 정한 4~8㎓까지의 주파수 대역을 의미한다. 지상 통신과 더불어 위성통신, 기상 관측 레이더 등의 분야에서 쓰이고 있다.
올해 2분기에 국내 서비스 예정으로 알려진 저궤도 위성통신 '스타링크'는 C대역보다 더 높은 주파수 대역인 케이유(Ku)대역을 쓴다. Ku대역은 12~18㎓ 대역으로 UAM, 원양 선박 등 지상망을 쓸 수 없는 이동 수단에 활용될 전망이다.
과기정통부 관계자는 "현재 C대역을 통해 드론이나 무인 항공기의 상태를 볼 수 있지만 운송 외의 부가적 기능을 쓰긴 어려울 수 있다"며 "차후 나올 저궤도 위성통신을 통해 UAM 내에서 유튜브 시청 등의 다양한 서비스를 쓸 수 있을 것"이라고 했다.
        """},
        {"role": "assistant", "content": """
5세대 이동통신(5G): 다음 세대 이동통신 기술로서, 초고속 대역폭과 저지연성 등의 특징을 갖추고 있음
도심항공교통(UAM): 수직 이착륙하는 항공기를 이용해 사람이나 화물을 운송하는 무인 교통체계를 뜻함
3.5기가헤르츠(㎓): 무선 통신에서 사용되는 대역폭 단위로, 현재 지상용 5G 상용망에서 사용 중인 대역임
초고속·초저지연 통신망: 대역폭이 높고 지연시간이 낮은 통신망을 의미함
표준화: 비슷한 목적이나 기능을 갖는 기술이나 제품들이 상호 호환성을 갖도록 하는 것을 말함
LTE: 4세대 이동통신(4G) 중 하나로, 고속 대역폭과 전송 속도를 갖추고 있음
스마트폰: 모바일 기기 중 하나로, 인터넷 검색, SNS, 영상 시청 등 다양한 기능을 갖추고 있음
서비스형모빌리티(MaaS): 공유 모빌리티 서비스를 활용해 여러 교통 수단을 하나의 통합된 서비스로 제공하는 것을 의미함
위성통신: 인공위성을 이용해 통신을 하는 기술을 의미함. 지상 통신망과는 달리 지리적인 제약을 받지 않는다는 장점이 있음.
        """}
]

if "messages" not in st.session_state:
    st.session_state["messages"] = ""

st.header("세형 채팅봇")

text = st.empty()
show_messages(text)

prompt = st.text_input("Prompt", placeholder="Enter your message here...")

if st.button("Send"):
    st.session_state["messages"] = BASE_PROMPT
    with st.spinner("Generating response..."):
        st.session_state["messages"] += [{"role": "user", "content": prompt}]
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=st.session_state["messages"]
        )
        message_response = response["choices"][0]["message"]["content"]
        st.session_state["messages"] += [
            {"role": "system", "content": message_response}
        ]
        show_messages(text)

if st.button("Clear"):
    st.session_state["messages"] = ""
    