FROM sonarqube
RUN apk update && apk add --update python3 py3-pip && \
    wget https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-4.0.0.1744.zip && \
    unzip sonar-scanner-cli-4.0.0.1744.zip
ENV PATH $PATH:sonar-scanner/bin