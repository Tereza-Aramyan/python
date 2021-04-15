from smtplib import SMTP_SSL
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import ssl
import os
from getpass import getpass
from models import Course

current = os.getcwd()

def send_email_for(course_name_ids, session):

    courses = session.query(Course).filter(Course.course_id.in_(course_name_ids)).all()
    passwd = getpass()
    context = ssl.create_default_context()

    with SMTP_SSL('smtp.synopsys.com', context=context, port=465) as smtp_server:
        smtp_server.login('tereza@synopsys.com', password=passwd)
        text_courses = "\n".join(f'course_name : {str(course.course_name)}'
                                 f' course_id: {course.course_id}'
                                 f' course_url: {course.course_url}'
                                 f' price": {course.price}'
                                 f' level: {course.level}'
                                 f' teachers {course.teachers}' for course in courses)
        text = f"""
        Hi, this is list of new courses...,
        {text_courses}
        Have a nice day.
        """

        content_text = MIMEText(text, 'plane')
        message = MIMEMultipart('multipart')
        message.attach(content_text)
        message['Subject'] = 'New courses'
        message['From'] = 'aramyantereza98.ta@gmail.com'
        message['To'] = 'aramyantereza98.ta@gmail.com'

        smtp_server.sendmail('aramyantereza98.ta@gmail.com', ['aramyantereza98.ta@gmail.com'],
                             msg=message.as_string())

if __name__ == '__main__':
    send_email_for(None)

