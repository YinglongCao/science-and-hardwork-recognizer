import numpy as np
import cv2
from baike_crawler import parse_baike
import re
import time
from ocr import OCRDetector
import streamlit as st


st.header("科技与狠活识别系统")
st.subheader("识别生活中的科技与狠活")

uploaded_file = st.file_uploader("上传配料表")

if uploaded_file is not None:
    bytes_file = uploaded_file.getvalue()
    cv2_img = cv2.imdecode(np.frombuffer(
        bytes_file, np.uint8), cv2.IMREAD_COLOR)

    st.image(bytes_file)

    # ocr识别配料表
    ocr = OCRDetector()
    ocr_pred = ocr.predict(cv2_img)
    print(ocr_pred)

    # 返回结果为空，则未识别
    if not ocr_pred:
        st.markdown('# 未识别出配料表，请重新上传')
    else:
        # 抓取配料信息
        items = re.split('，|、|,|、', ocr_pred)
        st.markdown(f'# 识别出 {len(items)} 种配料，以下是科技介绍：')
        for i, item in enumerate(items):

            sub_title, desc = parse_baike(item)

            if desc != '':
                st.markdown(f'## {item}')
                st.markdown(f'### {sub_title}')
                desc = desc.replace('防腐剂', '`防腐剂`')
                desc = desc.replace('甜味剂', '`甜味剂`')
                desc = desc.replace('着色剂', '`着色剂`')
                desc = desc.replace('食品添加剂', '`食品添加剂`')
                desc = desc.replace('增稠剂', '`增稠剂`')
                st.markdown(desc)
                
            time.sleep(1)
    st.markdown('# 识别结束')
