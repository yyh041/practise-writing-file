#coding:utf-8
import docx
with docx.Document(docx = "D:\同济事物\选课\选课前输入.docx") as doc:
    doc.add_table(2, 2, style=None)
    doc.save("D:\同济事物\选课\选课前输入.docx")