from docxtpl import DocxTemplate
from datetime import datetime
doc = DocxTemplate("original.docx")

date = datetime.today().strftime("%b %d, %Y")
recruiter_name = "Dr. Ed Murphy"
recruiter_job_title = "Supervisor"
website_name = "Habndshake"
company_name ="Tesla"
company_address = "123 main st"
company_city = "Boston"
company_state = "MA"
company_zipcode= "12345"
job_title ="Sofwtare Developer"
job_type = "internship"

replacements = {"date":date,
                "recruiter_name":recruiter_name,
                "recruiter_job_title":recruiter_job_title,
                "company_name": company_name,
                "website_name":website_name,
               "company_zipcode":company_zipcode,
                "company_city": company_city,
               "company_address":company_address,
                "company_state":company_state,
               "job_type":job_type,
               "job_title":job_title}

doc.render(replacements)
doc.save("generated.docx")