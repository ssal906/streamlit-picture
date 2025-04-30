import streamlit as st

st.set_page_config (
    page_title="Streamlit Album",
    page_icon="./images/free-icon-photo-gallery-4503859.png"
)

st.markdown("""
<style>
img { 
    max-height: 300px;
}
.streamlit-expanderContent div {
    display: flex;
    justify-content: center;
    font-size: 20px;
}
[data-testid="StyledFullScreenButton"] {
    visibility: hidden;
}
</style>
""", unsafe_allow_html=True)

st.title("사진첩")
st.markdown("사진을 하나씩 추가해서 앨범을 완성해보세요.")

type_list = [
    "인물",
    "풍경",
    "여행",
    "접사",
    "패션",
    "음식",
    "거리",
    "스포츠",
    "연예인",
    "기타"
]

initial_pics = [
    {
        "name": "스위스 - 베르너 오버란트",
        "type": ["풍경", "여행"],
        "year": "2012",
        "image_url": "https://i.namu.wiki/i/BfPUMdeiCo67JoRIP8-zZVTF75vajLbriH5j2IGvlzjf8JPUbgntPq_9v_vvkuvB1BJxfnSdtH42JZgD69unLamNq8SWVO7UyJfTsbxeePsNnUw4bHhjgBeG38tCWfjHgpG3zj-7IUHd4CmxWhOIkQ.webp"
    },
    {
        "name": "정조",
        "type": ["인물"],
        "year": "1989",
        "image_url": "https://i.namu.wiki/i/j1yThHRi_xA6Bs5JGS78-NuiVZ3fb2_R2QgskA5rfyM66X5lpaO_uFyntmHwiflIVt8_7gWrvYDrSIqAsX1j8QTKVb5DBAhbS5ty2iyqwVxG002_JR3ShVy10lFW36trzuUdfCH1TtnhZ-EbZotWxw.webp"
    },
    {
        "name": "까르보나라",
        "type": ["음식"],
        "year": "2015",
        "image_url": "https://i.namu.wiki/i/Ao9GHsaeOAIPi5IOSW1Ggrz0ASrXb4aSLltktz8BFQXG3bbqVeAvFYO2ncpzTYsDSYX8TbvhnCrf7_E7VwS1vqjl9zd8oQerS4j-QDf51Bpt80sxmv2T2oq5sxvg8YYnCMQ1ao3gIhcozuooNpnA5g.webp"
    },
    {
        "name": "농구",
        "type": ["스포츠"],
        "year": "2014",
        "image_url": "https://i.namu.wiki/i/64PDiP90B1meB6V_p6Y5DmHtV_p8zoN9C_kPfSWhZ4iFAFFUiiJ15mZhZ4n0Mps7j7Fguo-MJtAdNaPWelvvLnV87GZfvmL0ee6p-mwaH0UGcy5HCId9XoMp8sM0LjSCKtYv3phI9vxrkNiRFC85_g.webp"
    },
]

example_picture = {
    "name": "토마토",
    "type": ["음식"],
    "year": "2019",
    "image_url": "https://i.namu.wiki/i/6oBodLyMxx098g-KBJER9e7rVgm1UulM2LwpYu7owbDx3ZQ9BBSfU63fgaXz0qACxAcIckk3fv09i1FDmerpeG_bV8BfZDbKtrZOPCGzMdiNn2qjn8MXsW-iLeMA2oBAPwgRaltcDli-3Q9f87xjdg.webp"
}

if "pictures" not in st.session_state:
    st.session_state.pictures = initial_pics

auto_complete = st.toggle("예시 사진")
with st.form(key="form"):
    col1, col2, col3 = st.columns(3)
    with col1:
        name = st.text_input(
            label="사진 이름",
            value=example_picture["name"] if auto_complete else ""
        )
    with col2:
        type = st.multiselect(
            label="사진 종류",
            options= type_list,
            max_selections=2,
            default=example_picture["type"] if auto_complete else []
        )
    with col3:
        year = st.text_input(
            label="사진 연도",
            value=example_picture["year"] if auto_complete else ""
        )
    image_url = st.text_input(
        label="사진 URL",
        value=example_picture["image_url"] if auto_complete else ""
    )
    submit = st.form_submit_button(label="등록")
    if submit:
        if not name:
            st.error("사진의 이름을 입력해주세요.")
        elif len(type) == 0:
            st.error("사진의 종류를 선택해주세요.")
        elif not year:
            st.error("사진의 연도를 입력해주세요.")
        else:
            st.success("사진을 추가합니다.")
            st.session_state.pictures.append({
                "name": name,
                "type": type,
                "year": year,
                "image_url": image_url if image_url else "./images/free-icon-photo-gallery-4503859.png"
            })

for i in range(0, len(st.session_state.pictures), 2):
    row_pictures = st.session_state.pictures[i:i+2]
    cols = st.columns(2)
    for j in range(len(row_pictures)):
        with cols[j]:
            picture = row_pictures[j]
            with st.expander(label=f"**{i+j+1}. {picture['name']}**", expanded=True):
                st.image(picture["image_url"])
                st.text(" / ".join(picture["type"]))
                st.text(picture["year"])
                delete_button = st.button(label="삭제", key=i+j, use_container_width=True)
                if delete_button:
                    del st.session_state.pictures[i+j]
                    st.rerun()