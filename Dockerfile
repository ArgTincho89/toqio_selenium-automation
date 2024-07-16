FROM python:3.9

WORKDIR /usr/src/app


COPY . .

# Instals the dependencies and drivers for Chrome, Firefox and Edge
RUN apt-get update -y && \
    apt-get install -y wget unzip zip firefox-esr && \
    pip install --upgrade pip && \
    pip install -r requirements.txt && \
    # Chrome
    wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/$(curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE)/chromedriver_linux64.zip && \
    unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/ && \
    curl -sS -o - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list && \
    apt-get update -y && \
    apt-get install -y google-chrome-stable && \
    # Firefox (Geckodriver)
    wget -O /tmp/geckodriver.tar.gz https://github.com/mozilla/geckodriver/releases/download/$(curl -s https://api.github.com/repos/mozilla/geckodriver/releases/latest | grep tag_name | cut -d '"' -f 4)/geckodriver-$(curl -s https://api.github.com/repos/mozilla/geckodriver/releases/latest | grep tag_name | cut -d '"' -f 4)-linux64.tar.gz && \
    tar -xzf /tmp/geckodriver.tar.gz -C /usr/local/bin/
    # Edge
    curl -s https://packages.microsoft.com/keys/microsoft.asc | apt-key add - && \
    echo "deb [arch=amd64] https://packages.microsoft.com/repos/edge stable main" > /etc/apt/sources.list.d/microsoft-edge-dev.list && \
    apt-get update -y && \
    apt-get install -y microsoft-edge-stable && \
    wget -O /tmp/edgedriver.zip https://msedgedriver.azureedge.net/$(curl -s https://msedgedriver.azureedge.net/LATEST_STABLE)/edgedriver_linux64.zip && \
    unzip /tmp/edgedriver.zip -d /usr/local/bin/


CMD ["pytest", "-rA", "-v", "--html=../reports/toqio_automation_report.html"]
