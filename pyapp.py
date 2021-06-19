import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import altair as alt

# ------------------------------------------------------------------------------
# Setting CSS style containner-width and padding
st.markdown(
        f'''
        <style>
            .reportview-container .main .block-container{{
                max-width: 70%;
                padding-top: 5rem;
                padding-right: 1rem;
                padding-left: 1rem;
                padding-bottom: 1rem;
            }}
        </style>
        ''',
        unsafe_allow_html=True
    )

st.markdown(
        f'''
        <style>
            a:link {{
              color: bule;
              background-color: transparent;
              text-decoration: none;
            }},
        </style>
        ''',
        unsafe_allow_html=True
    )

# ------------------------------------------------------------------------------
# Display bar chart race from flourish studio
html_bar_race ='''
    <div class="flourish-embed flourish-bar-chart-race" data-src="visualisation/6453087">
        <script src="https://public.flourish.studio/resources/embed.js">
        </script>
    </div>
    '''
components.html(html_bar_race, height=700)

# ------------------------------------------------------------------------------
# Display World map from Tapleau-public
html_map = f'''
    <div class='tableauPlaceholder' id='viz1623978522231' style='position: relative'>
        <noscript><a href='#'>
            <img alt='แผนที่แสดงสัดส่วนการใช้พลังงานทางเลือกต่อพลังงานทั้งหมดระหว่างปี 2015-2019 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;He&#47;HeatMap2_16239342073290&#47;Sheet1&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' />
            <param name='embed_code_version' value='3' />
            <param name='site_root' value='' />
            <param name='name' value='HeatMap2_16239342073290&#47;Sheet1' />
            <param name='tabs' value='no' /><param name='toolbar' value='yes' />
            <param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;He&#47;HeatMap2_16239342073290&#47;Sheet1&#47;1.png' />
            <param name='animate_transition' value='yes' />
            <param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' />
            <param name='display_overlay' value='yes' />
            <param name='display_count' value='yes' />
            <param name='language' value='en-US' />
        </object>
    </div>
    <script type='text/javascript'>
        var divElement = document.getElementById('viz1623978522231');
        var vizElement = divElement.getElementsByTagName('object')[0];
        vizElement.style.width = '100%';
        vizElement.style.height = '550px';
        var scriptElement = document.createElement('script');
        scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';
        vizElement.parentNode.insertBefore(scriptElement, vizElement);
    </script>
    '''
components.html(html_map, height=600)

# Data source link
st.write(f'''
    <div color: gray;">
        <p>แหล่งที่มา : <a href="https://ourworldindata.org/energy" target="_blank">Our World in Data</a></p>
    </div>
''',unsafe_allow_html=True )

# ------------------------------------------------------------------------------
# Display ratio in Asean from Power BI
st.header('เปรียบเทียบสัดส่วนการใช้พลังงานทางเลือกภายในกลุ่มประเทศอาเซียน')

html_ratio_indi = '<iframe width="100%" height="550" src="https://app.powerbi.com/view?r=eyJrIjoiZGZhNDUxYzMtZTc5Yi00ZGMyLWIxM2MtMTNkYjhkNTc1ODJiIiwidCI6ImRiNWRlZjZiLThmZDgtNGEzZS05MWRjLThkYjI1MDFhNjgyMiIsImMiOjEwfQ%3D%3D" frameborder="0" allowFullScreen="true"></iframe>'
st.markdown(html_ratio_indi,unsafe_allow_html=True)

html_ratio_sum = '<iframe width="100%" height="500" src="https://app.powerbi.com/view?r=eyJrIjoiMWI2MzEzZDItOWU5Yy00MzA0LWFhZTYtYmQ0OGY2OGZhYTRiIiwidCI6ImRiNWRlZjZiLThmZDgtNGEzZS05MWRjLThkYjI1MDFhNjgyMiIsImMiOjEwfQ%3D%3D" frameborder="0" allowFullScreen="true"></iframe>'
st.markdown(html_ratio_sum ,unsafe_allow_html=True)

# Data source link
st.write(f'''
    <div color: gray;">
        <p>แหล่งที่มา : <a href="https://ourworldindata.org/energy" target="_blank">Our World in Data</a></p>
    </div>
''',unsafe_allow_html=True )
# ------------------------------------------------------------------------------
# Thailand Electric Generation
st.header('รายละเอียดการผลิตพลังงานไฟฟ้าจากพลังงานชนิดต่างๆภายในประเทศไทย และแผนการพัฒนาการผลิตไฟฟ้าจากพลังงานทางเลือก')
html_thai_gen = '<iframe width="100%" height="550" src="https://app.powerbi.com/view?r=eyJrIjoiZjJkM2VlOTktYTdkMy00MGY1LTlmYzAtMTE2MzMxZDk5MWNlIiwidCI6ImRiNWRlZjZiLThmZDgtNGEzZS05MWRjLThkYjI1MDFhNjgyMiIsImMiOjEwfQ%3D%3D&pageName=ReportSection5de7c14c100a03822cde" frameborder="0" allowFullScreen="true"></iframe>'
st.markdown(html_thai_gen ,unsafe_allow_html=True)

# ------------------------------------------------------------------------------
# Thailand PDP2018
html_thai_pdp = '<iframe width="100%" height="550" src="https://app.powerbi.com/view?r=eyJrIjoiODc3MjY0YjMtNTUzNC00YzdjLTk3ZTgtN2U2ZjMxMjFhOTU1IiwidCI6ImRiNWRlZjZiLThmZDgtNGEzZS05MWRjLThkYjI1MDFhNjgyMiIsImMiOjEwfQ%3D%3D" frameborder="0" allowFullScreen="true"></iframe>'
st.markdown(html_thai_pdp ,unsafe_allow_html=True)

# Data source link
st.write(f'''
    <div style="margin: 2rem 2rem 0 0; color: gray;">
            <p style="margin-bottom: 0">แหล่งที่มา : <a href="http://www.eppo.go.th/index.php/th/informationservices/ct-menu-item-56" target="_blank">สำนักงานนโยบายและแผนพลังงาน (สนพ.) สังกัตกระทรวงพลังงาน</a></p>
            <p style="margin: 0 0 0 5rem;"><a href="https://www.egat.co.th/images/businessop/PDP2018-Rev1-Oct2020.pdf" target="_blank">แผนพัฒนาพลังงาน</a></p>
            <p style="margin: 0 0 0 5rem;"><a href="https://www.egat.co.th/index.php?option=com_content&view=article&id=76&Itemid=116" target="_blank">การไฟฟ้าฝ่ายผลิตแห่งประเทศไทย</a></p>
    </div>
''',unsafe_allow_html=True )

# ------------------------------------------------------------------------------
# Read data
# install_cap = pd.read_csv('data/Install_Capacity_of_Alternative_Energy.csv')
cf = pd.read_csv('data/Alternative_Energy_Capacity_Factor.csv')
# generation = pd.read_csv('data/Alternative_Energy_Generation.csv')
world_cf = pd.read_csv('data/World_capacity_factors.csv')

# ------------------------------------------------------------------------------
st.write(f'''
<div style="width: 90%; align-content: center; margin: 5rem 2rem 2rem 2rem;">
    <b>กำลังการผลิตไฟฟ้าติดตั้ง (Installed power generation capacity)</b> หรือเรียกสั้น ๆ เป็นภาษาอังกฤษว่า Installed Capacity นั้น คือกำลังการผลิตไฟฟ้าที่โรงไฟฟ้าสามารถผลิตได้เมื่อเดินเครื่องเต็มกำลัง มีหน่วยเป็น กิโลวัตต์ (kW) หรือ เมกะวัตต์ (MW) <br>
    <br>
    <b>อัตราความสามารถในการผลิตของโรงไฟฟ้า (Capacity Factor)</b> คือ อัตราส่วนพลังงานไฟฟ้าที่ผลิตได้จริงในช่วงเวลาที่กำหนดต่อพลังงานไฟฟ้าสูงสุดที่สามารถผลิตได้ในช่วงเวลานั้น <br>
    <br>
    แต่โดยข้อเท็จจริงในทางปฏิบัติ โรงไฟฟ้าทุกโรงไม่สามารถเดินเครื่องหรือผลิตไฟฟ้าได้เต็มตามกำหนดได้ตลอดเวลา 24 ชั่วโมง 365/366 วัน ด้วยเหตุผลดังต่อไปนี้
    <br>
    <ol>
        <li>
        โรงไฟฟ้าทุกโรงจะต้องมีการหยุดเดินเครื่องเพื่อซ่อมบำรุงใหญ่ (Planned Outages) อย่างน้อยปีละ 1 ครั้ง ๆ ละ 20-30 วัน ดังนั้น เวลาที่หยุดซ่อมบำรุงใหญ่นี้คิดเป็นร้อยละประมาณ 8.33 ของจำนวนชั่วโมงทั้งหมดใน 1 ปี ถ้าคิดรวมถึงการหยุดซ่อมบำรุงที่อาจเกิดขึ้นโดยไม่ได้วางกำหนดเวลาซ่อมบำรุงไว้ล่วงหน้า (Unplanned Outages) ก็เฉลี่ยอยู่ที่ร้อยละ 10-12
        </li>
        <li>
        ความสมบูรณ์หรือประสิทธิภาพของอุปกรณ์เครื่องจักรและอุปกรณ์ในโรงไฟฟ้า ไม่ว่าจะเป็นหม้อไอน้ำ กังหันไอน้ำ และ ชุดปั่นไฟ (Generator) ย่อมต้องสึกหรอไปตามอายุการใช้งาน ประสิทธิภาพก็ลดลงไปอีกราวร้อยละ 5-10 แล้วแต่กรณี
        </li>
        <li>
        ประสิทธิภาพการบริหารจัดการรวมถึงสภาพแวดล้อมของโรงไฟฟ้า ได้แก่ การบริหารจัดการเชื้อเพลิง กำลังคน รวมถึงสภาพแวดล้อม ยกตัวอย่างเช่น โรงไฟฟ้าพลังน้ำจากเขื่อนขนาดใหญ่ ถ้าน้ำเหนือเขื่อนมีน้อย ความสามารถในการจ่ายน้ำเพื่อเดินเครื่องกังหันน้ำก็ลดลง ไฟฟ้าที่ผลิตได้ก็ไม่เต็มกำลังเครื่อง หรือในทางกลับกัน ถ้าพื้นที่ใต้เขื่อนมีน้ำท่วมขัง ก็ไม่สามารถปล่อยน้ำเพื่อผลิตไฟฟ้าได้เช่นกัน เพราะจะไปซ้ำเติมปัญหาอุทกภัย ซึ่งหลาย ๆ ปัจจัยที่กล่าวถึงข้างต้นนี้ ก็อาจอยู่นอกเหนือความสามารถในการควบคุมของฝ่ายบริหารเพราะเป็นปัจจัยภายนอก
        </li>
    </ol>
    ปัจจุบันเรามีกำลังการผลิตไฟฟ้าติดตั้งจากพลังงานหมุนเวียนรวมกันประมาณ 8,900 เมกะวัตต์ ประกอบด้วยโรงไฟฟ้าชีวมวลและก๊าซชีวภาพ 3,940 เมกะวัตต์ พลังงานแสงอาทิตย์ 2,982 เมกะวัตต์ พลังงานลม 1507 เมกะวัตต์ และอื่นๆ <br>
    <br>
    ตัวอย่างเช่นการผลิตไฟฟ้าจากพลังงานแสงอาทิตย์เป็นที่ทราบดีว่า พลังงานแสงอาทิตย์ที่ผลิตไฟฟ้าได้โดยผ่านแผงโซลาร์เซลล์นั้น ผลิตได้เฉพาะเวลาที่มีแสงแดดเท่านั้น ซึ่งค่าเฉลี่ยของแผงโซลาร์เซลล์จะผลิตไฟฟ้าได้ประมาณ 5 ชั่วโมงต่อวัน เมื่อเทียบจำนวนชั่วโมงที่ผลิตได้ในหนึ่งวัน (5 ชั่วโมง) กับจำนวนชั่วโมงที่มีในหนึ่งวัน (24 ชั่วโมง) เราจะได้ค่าประสิทธิภาพที่ร้อยละ 20.8 แต่ถ้านับรวมวันที่ฝนตกหรือท้องฟ้ามีเมฆหมอกมาก ปริมาณไฟฟ้าที่ผลิตได้จริงในหนึ่งปี (Plant Capacity Factor) เฉลี่ยของแผงโซลาร์เซลล์ก็จะลดลงเหลือประมาณร้อยละ 12-15 เท่านั้น <br>
    <br>
    ดังนั้น การผลิตไฟฟ้าจากพลังงานทางเลือกรวมทั้งพลังงานในรูปแบบอื่นๆจึงไม่สามารถมองที่สัดส่วนกำลังการผลิตติดตั้ง (Installed Capacity) เพียงอย่างเดียวได้ หากต้องการคำนวณปริมาณการผลิตไฟฟ้าให้เพียงพอต่อความต้องการเราจึงจำเป็นต้องดูควบคู่กันกับ <b>"อัตราความสามารถในการผลิตของโรงไฟฟ้า (Capacity Factor)"</b> ด้วยเช่นกัน <br>
</div>
''',unsafe_allow_html=True)

# ------------------------------------------------------------------------------
# Boxplot of Alternative Energy Capacity Factor in Thailand
st.header('อัตราความสามารถในการผลิตของโรงไฟฟ้า (Capacity Factor) พลังงานทางเลือกในไทยตั้งแต่ปี ค.ศ.2012 - 2019')

cf_pivot = cf.set_index("ปี").stack().to_frame().reset_index()
cf_pivot = cf_pivot.set_axis(['ปี', 'ชนิด', 'Capacity Factor'], axis='columns')
boxs = alt.Chart(cf_pivot).mark_boxplot(
    size=50,
    extent=0.5
).encode(
    x='ชนิด:O',
    y=alt.Y('Capacity Factor:Q',scale=alt.Scale(zero=False))
).properties(
    height=500
).configure_axis(
    labelFontSize=16,
    titleFontSize=16
)

col1, col2, col3 = st.beta_columns((1,3,1))
with col2:
    st.altair_chart(boxs, use_container_width = True)

# ------------------------------------------------------------------------------
st.header('Capacity Factor ของการผลิตไฟฟ้าจากพลังงานรูปแบบต่างๆของไทยเมื่อเทียบกับภูมิภาคอื่น')
row1_1, row1_2 = st.beta_columns((1,1))
row2_1, row2_2 = st.beta_columns((1,1))
row3_1, row3_2 = st.beta_columns((1,1))
row4_1, row4_2 = st.beta_columns((1,1))

rows = [row1_1,row1_2,row2_1,row2_2,row3_1,row3_2,row4_1,row4_2]
tpys = ["นิวเคลียร์", "เชื้อเพลิงฟอสซิล", "ปิโตรเลี่ยม", "ถ่านหิน", "ก๊าซธรรมชาติ", "น้ำ", "แสงอาทิตย์", "ลม"]

for idx in range(0,8):
    with rows[idx]:
        st.vega_lite_chart(world_cf, {
            "width": 100,
            "layer":[
                {"mark": "bar"},
                {"mark": {
                    "type": "text",
                    "fontWeight": "bold",
                    "align": "left",
                    "baseline": "middle",
                    "dx": 3
                    },
                 "encoding": {"text": {"field": tpys[idx], "type": "quantitative", "format": ".1f"}}
                }
            ],
            "encoding": {
                "x": {
                    "field": tpys[idx],
                    "type": "quantitative",
                    "scale":{"domain":[0,100]},
                    "title": f"Capacity factor - {tpys[idx]} (%)"
                },
                "y": {
                    "field": "ภูมิภาค",
                    "type": "nominal",
                    # "axis": {"labels": False},
                    "sort": "-x"
                },
                "color": {
                    "field": "ภูมิภาค",
                    "scale": {"range": ["#4C78A8"]},
                    "condition": {
                        "test": "datum['ภูมิภาค'] === 'Thailand'",
                        "value": "#ED553B"
                    },
                    "legend": False
                }
            }
        },use_container_width = True)

# Data source link
st.write(f'''
    <div style="margin: 2rem 2rem 0 0; color: gray;">
            <p style="margin-bottom: 0">แหล่งที่มา :  <a href="http://services.dede.go.th/opendata/" target="_blank">กรมพัฒนาพลังงานทดแทนและอนุรักษ์พลังงาน สังกัตกระทรวงพลังงาน</a></p>
            <p style="margin: 0 0 3rem 5rem;"><a href="https://www.eia.gov/todayinenergy/detail.php?id=22832" target="_blank">U.S. Energy Information Administration</a></p>
    </div>
''',unsafe_allow_html=True )
