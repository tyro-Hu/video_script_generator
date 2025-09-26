import streamlit as st
from utils import generate_script

st.title("🎬视频脚本生成器")

# 添加侧边栏
with st.sidebar:
    deepseek_api_key = st.text_input("请输入你的DeepSeek API密钥", type="password")
    st.markdown("[获取DeepSeek API密钥](https://platform.deepseek.com/api_keys)")
    st.write("测试密钥：sk-e24ba93f8f204f34a2ade604b8ebecf0")

subject = st.text_input("💡请输入视频的主题")
video_length = st.number_input("🕒请输入视频的大致时长（单位：分钟）", min_value=0.1, step=0.1, value=1.0)
creavity = st.slider("✨请输入视频脚本的创造力（数字小说明更严谨，数字大说明更多样）", min_value=0.0, max_value=1.0, step=0.1, value=0.2)

submit = st.button("🚀生成脚本")

# 检查密钥
if submit and not deepseek_api_key:
    st.info("请输入你的DeepSeek API密钥")
    st.stop()

# 检查主题
if submit and not subject:
    st.info("请输入视频的主题")
    st.stop()

# 检查时长
if submit and not video_length >= 0.1:
    st.info("视频长度需要大于或等于0.1")
    st.stop()

if submit:
    # 生成脚本
    with st.spinner(("AI正在思考中，请稍等...")):
        wiki_result, title, script = generate_script(subject, video_length, creavity, deepseek_api_key)
    st.success("视频脚本已生成！")

    st.subheader("🔥标题：")
    st.write(title)
    st.subheader("📝视频脚本：")
    st.write(script)
    with st.expander("📚维基百科搜索结果👀"):
        st.info(wiki_result)


