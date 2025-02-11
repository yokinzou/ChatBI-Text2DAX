import streamlit as st
import pandas as pd
from langchain.prompts import PromptTemplate
from Prompt.Text2DAX.prompt_1st_part import prompt_template_1st_part_fix
from Prompt.Text2DAX.prompt_2nd_part import prompt_template_2nd_part

def PBI_Semantic():
    def main():
        st.title("PBI Semantic Management")
        
        # 上传三个 CSV 文件
        uploaded_file1 = st.file_uploader("选择第一个 PowerBI Measure( KPI) Meta Data CSV 文件", type="csv")
        uploaded_file2 = st.file_uploader("选择第二个 BI Table Relationship CSV 文件 ", type="csv")
        uploaded_file3 = st.file_uploader("选择第三个 BI Table Columns CSV 文件", type="csv")
        uploaded_file4 = st.file_uploader("选择第四个 BI Calculated Tables CSV 文件", type="csv")
        uploaded_file5 = st.file_uploader("选择第五个 BI Calculated Groups CSV 文件", type="csv")
        uploaded_file6 = st.file_uploader("选择第六个 BI 数据样本 CSV 文件", type="csv")
        uploaded_file7 = st.file_uploader("选择第七个 BI 数据样本 CSV 文件", type="csv")
        # 初始化数据框
        df1, df2, df3, df4, df5,df6,df7= None, None, None, None, None,None,None
        # 显示文件内容并嵌入到提示模板中
        if uploaded_file1 is not None:
            df1 = pd.read_csv(uploaded_file1)

        if uploaded_file2 is not None:
            df2 = pd.read_csv(uploaded_file2)


        if uploaded_file3 is not None:
            df3 = pd.read_csv(uploaded_file3)

        if uploaded_file4 is not None:
            df4 = pd.read_csv(uploaded_file4)

        if uploaded_file5 is not None:
            df5 = pd.read_csv(uploaded_file5)

        if uploaded_file6 is not None:
            df6 = pd.read_csv(uploaded_file6)
            
        if uploaded_file7 is not None:
            df7 = pd.read_csv(uploaded_file7)

        return df1,df2,df3,df4,df5,df6,df7

    df1,df2,df3,df4,df5,df6,df7=main()

    text_to_dax_prompt_template=prompt_template_1st_part_fix+prompt_template_2nd_part


    prompt_template_text_to_dax = PromptTemplate(
                input_variables=["BI_Measure_Meta_Data", "BI_Table_Relationship", "BI_Table_Columns", "BI_Calculated_Tables","BI_Calculated_Groups","BI_Dimensional_Columns_Sample_Data","measure_definition"],
                template=text_to_dax_prompt_template)

    response = prompt_template_text_to_dax.format(
        BI_Measure_Meta_Data=df1.to_markdown() if df1 is not None else " ",
        BI_Table_Relationship=df2.to_markdown() if df2 is not None else " ",
        BI_Table_Columns=df3.to_markdown() if df3 is not None else " ",
        BI_Calculated_Tables=df4.to_markdown() if df4 is not None else " ",
        BI_Calculated_Groups=df5.to_markdown() if df5 is not None else " ",
        BI_Dimensional_Columns_Sample_Data=df6.to_markdown() if df6 is not None else " ",
        BI_Measure_Definition=df7.to_markdown() if df7 is not None else " "

    )


    structure_requirement= """
    DEFINE

    VAR __DS0FilterTable=TREATAS({<your_filter_condition_value>}, 'BI_table'[filtered_column])

    VAR __DS0FilterTable2=TREATAS({<your_filter_condition2_value>}, 'BI_table'[filtered_column2])

    如果还有其他筛选条件，请继续添加__DS0FilterTable3, __DS0FilterTable4等

    EVALUATE
    SUMMARIZECOLUMNS(
                
                'BI_Table'[groupby_column1], '[3] Org'[groupby_column2]
                ,
                __DS0FilterTable,
                __DS0FilterTable2,
                "KPI_measure_renamed_name", 'measure_table_name'[measure_name]
            )


    ##举例
    # 根据第一个步骤的举例问题（ 8月份的baby的ecom发货总价值）识别：时间维度：202408，product表涉及的维度category="baby"，org表涉及的维度channel="ecom"
    则对应的dax query应该返回
    DEFINE
        VAR __DS0FilterTable = 
            TREATAS({"202408"}, '[2] Date'[YearMonth])

        VAR __DS0FilterTable2 = 
            TREATAS({"iOMNI eCom"}, '[3] Org'[Channel Name])

    EVALUATE
        SUMMARIZECOLUMNS(
                
                '[4] Product'[Brand], '[3] Org'[Channel Name]
                ,
                __DS0FilterTable,
                __DS0FilterTable2,
                "GIV_Composed", '[1] Shipment'[GIV Composed]
            )

    #Step4: 检查dax query中的measure是否存在measure meta data中，以及维度字段和维度字段的值是否在元数据中。注意，第三步骤的条件的值大小写敏感。

    """



    st.code(response, language='markdown')  # 以代码形式显示内容