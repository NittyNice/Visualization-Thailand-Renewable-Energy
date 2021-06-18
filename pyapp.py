import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns
import altair as alt

# # Setting seaborn plot theme
# sns.set_theme(style="whitegrid")

st.markdown(
        f"""
        <style>
            .reportview-container .main .block-container{{
                max-width: 70%;
                padding-top: 5rem;
                padding-right: 1rem;
                padding-left: 1rem;
                padding-bottom: 1rem;
            }}
        </style>
        """,
        unsafe_allow_html=True
    )

# ------------------------------------------------------------------------------
# Bar chart race from flourish studio
html_bar_race ='''
    <div class="flourish-embed flourish-bar-chart-race" data-src="visualisation/6453087">
        <script src="https://public.flourish.studio/resources/embed.js">
        </script>
    </div>
    '''
components.html(html_bar_race, height=700)

# ------------------------------------------------------------------------------
# Bar chart race from flourish studio
html_map = '''
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
            vizElement.style.height = '500px';
            var scriptElement = document.createElement('script');
            scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';
            vizElement.parentNode.insertBefore(scriptElement, vizElement);
        </script>
    '''
components.html(html_map, height=600)

# ------------------------------------------------------------------------------
# Ratio in Asean

html_ratio_indi = '<iframe width="100%" height="500" src="https://app.powerbi.com/view?r=eyJrIjoiZGZhNDUxYzMtZTc5Yi00ZGMyLWIxM2MtMTNkYjhkNTc1ODJiIiwidCI6ImRiNWRlZjZiLThmZDgtNGEzZS05MWRjLThkYjI1MDFhNjgyMiIsImMiOjEwfQ%3D%3D" frameborder="0" allowFullScreen="true"></iframe>'
st.markdown(html_ratio_indi,unsafe_allow_html=True)

html_ratio_sum = '<iframe width="100%" height="500" src="https://app.powerbi.com/view?r=eyJrIjoiMWI2MzEzZDItOWU5Yy00MzA0LWFhZTYtYmQ0OGY2OGZhYTRiIiwidCI6ImRiNWRlZjZiLThmZDgtNGEzZS05MWRjLThkYjI1MDFhNjgyMiIsImMiOjEwfQ%3D%3D" frameborder="0" allowFullScreen="true"></iframe>'
st.markdown(html_ratio_sum ,unsafe_allow_html=True)

# ------------------------------------------------------------------------------
# Thailand Electric Generation
html_thai_gen = '<iframe width="100%" height="500" src="https://app.powerbi.com/view?r=eyJrIjoiZjJkM2VlOTktYTdkMy00MGY1LTlmYzAtMTE2MzMxZDk5MWNlIiwidCI6ImRiNWRlZjZiLThmZDgtNGEzZS05MWRjLThkYjI1MDFhNjgyMiIsImMiOjEwfQ%3D%3D&pageName=ReportSection5de7c14c100a03822cde" frameborder="0" allowFullScreen="true"></iframe>'
st.markdown(html_thai_gen ,unsafe_allow_html=True)

# ------------------------------------------------------------------------------
# Thailand PDP2018
html_thai_pdp = '<iframe width="100%" height="500" src="https://app.powerbi.com/view?r=eyJrIjoiODc3MjY0YjMtNTUzNC00YzdjLTk3ZTgtN2U2ZjMxMjFhOTU1IiwidCI6ImRiNWRlZjZiLThmZDgtNGEzZS05MWRjLThkYjI1MDFhNjgyMiIsImMiOjEwfQ%3D%3D" frameborder="0" allowFullScreen="true"></iframe>'
st.markdown(html_thai_pdp ,unsafe_allow_html=True)

# ------------------------------------------------------------------------------
# Read data
# install_cap = pd.read_csv('Install_Capacity_of_Alternative_Energy.csv')
cf = pd.read_csv('data\Alternative_Energy_Capacity_Factor.csv')
# generation = pd.read_csv('Alternative_Energy_Generation.csv')
world_cf = pd.read_csv('data\World_capacity_factors.csv')

# ------------------------------------------------------------------------------
components.html("""<b>กำลังการผลิตไฟฟ้าติดตั้ง (Installed power generation capacity)</b> หรือเรียกสั้น ๆ เป็นภาษาอังกฤษว่า Installed Capacity นั้น คือกำลังการผลิตไฟฟ้าที่โรงไฟฟ้าสามารถผลิตได้เมื่อเดินเครื่องเต็มกำลัง มีหน่วยเป็น กิโลวัตต์ (kW) หรือ เมกะวัตต์ (MW) <br>
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



""", height=500)

# ------------------------------------------------------------------------------
# Boxplot of Alternative Energy Capacity Factor in Thailand
st.header('อัตราความสามารถในการผลิตของโรงไฟฟ้า (Capacity Factor) พลังงานทางเลือกในไทยตั้งแต่ปี พ.ศ.2555 - 2562')

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
st.header('Capacity Factor ของการผลิตไฟฟ้าจากพลังงานของไทยเมื่อเทียบกับภูมิภาคอื่นๆ')
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
                # "color": {
                #     "field":"Region",
                #     "scale": {"scheme": "category20b"},
                #     "legend": False
                # }
            }
        },use_container_width = True)


# ------------------------------------------------------------------------------
# Bar charts of world power plant capacity factor
# sort_region = ['United States', 'Canada', 'Mexico and Chile', 'Brazil',
#                 'Other Central and South America', 'OECD Europe', 'Other non-OECD Europe and Eurasia',
#                 'Russia', 'China', 'India', 'Japan', 'South Korea', 'Other non-OECD Asia', 'Middle East',
#                 'Africa', 'Australia and New Zealand']
#
# bars = alt.Chart(world_cf).mark_bar().encode(
#     x=alt.X('Wind:Q', scale=alt.Scale(domain=(0,100))),
#     y=alt.Y('Region:N', sort='-x')
# )
#
# text = bars.mark_text(
#     align='left',
#     baseline='middle',
#     dx = 3
# ).encode(
#     text=alt.Text('Wind:Q', format='.1f')
# )
#
# st.altair_chart((bars + text), use_container_width = True)

# # ------------------------------------------------------------------------------
# # Small multiple bar charts of world power plant capacity factor
# mbars = alt.Chart(world_cf).mark_bar().encode(
#     x=alt.X(alt.repeat('column'), type='quantitative', scale=alt.Scale(domain=(0,100))),
#     y=alt.Y('Region:N', sort='-x')
# ).properties(
#     width=160,
#     height=160
# ).repeat(
#     column = ['Wind','Solar', 'Coal', 'Hydro']
# ).resolve_scale(x='independent')
#
# # text = mbars.mark_text(
# #     align='left',
# #     baseline='middle',
# #     dx = 3
# # ).encode(
# #     text=alt.Text('Wind:Q', format='.1f')
# # )
#
# st.altair_chart(mbars)

# ------------------------------------------------------------------------------
# # Setting figure with boxplot and swarmplot
# fig, ax = plt.subplots(figsize=(11,7))
# ax = sns.boxplot(data=cf.iloc[3:10,1:7])
# ax = sns.swarmplot(data=cf.iloc[3:10,1:7], color=".25")

# # Calculation and display medium on each boxplot
# medians = cf.iloc[3:10,1:7].median()
# for xtick in ax.get_xticks():
#     ax.text(xtick,
#             medians[xtick]+0.005,
#             medians[xtick],
#             horizontalalignment='center',
#             color='w',
#             weight='bold',
#             bbox=dict(facecolor='#445A64')
#            )

# # Display with matplotlib
# st.pyplot(fig)

# ------------------------------------------------------------------------------
# world_cf_pivot = world_cf.set_index('Region').stack().to_frame().reset_index()
# world_cf_pivot = world_cf_pivot.set_axis(['Region', 'Type', 'Generation'], axis='columns')

# st.vega_lite_chart(world_cf_pivot, {
#     "facet": {
#         "column": {"type": "nominal", "field": "Type"}
#     },
#     "spec": {
#         "width": 100,
#         "autosize": {
#             "type": "pad",
#             "contains": "padding"
#         },
#         "encoding": {
#             "x": {"type": "quantitative",
#                   "field": "Generation",
#                   "scale":{"domain":[0,100]},
#                   "title": "Generation (%)"
#                  },
#             "y": {"type": "nominal",
#                   "field": "Region",
#                   "transform": [{"filter": "datum.Type == Wind"}],
#                   "sort": "+x"
#                  }
#         },
#         "layer":[
#             {"mark": "bar"},
#             {"mark": {
#                 "type": "text",
#                 "align": {"expr": "datum.Generation < 0 ? 'right' : 'left'"},
#                 "dx": {"expr": "datum.Generation < 0 ? -2 : 2"}
#                 },
#              "encoding": {"text": {"field": "Generation", "type": "quantitative"}}
#             }
#         ],
#         "resolve": {
#             "scale": {
#                 "y": "shared"
#                 }
#         }
#     },
# })

# components.html(
#     """
#         <div class='tableauPlaceholder' id='viz1623864092650' style='position: relative'><noscript><a href='#'><img alt='Dashboard 1 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Wo&#47;World_Renewable&#47;Dashboard1&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='World_Renewable&#47;Dashboard1' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Wo&#47;World_Renewable&#47;Dashboard1&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1623864092650');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else { vizElement.style.width='100%';vizElement.style.height='777px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>
#     """
# )
