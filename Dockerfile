FROM python:3.10
ENV PYTHONUNBUFFERED=1
WORKDIR /home/blog_interview_task
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . /app
RUN useradd testuser
RUN chown -R testuser:testuser ./
RUN chmod -R 755 ./
USER testuser
EXPOSE 8000