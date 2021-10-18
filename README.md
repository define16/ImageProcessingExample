# ImageProcessingExample
이미지 프로세싱 관련 예제 코드를 모으기 위해 만든 Repository입니다.

## Tesseract 세팅 방법
### Mac인 경우
```$ brew install tesseract```<br>
```$ brew install tesseract-lang```<br><br>
원하는 언어가 있는지 확인하고 없는 경우 다운을 받아야한다.<br>
```$ tesseract --list-langs```<br>

환경 변수 추가: ```~/.bash_profile``` 파일에 ```TESSDATA_PREFIX=/usr/local/Cellar/tesseract/4.0.0_1/share/tessdata``` 행을 추가합니다.<br>
환경 변수 추가: ```~/.bash_profile``` 파일에 ```ESSERACT_PATH=/usr/local/Cellar/tesseract/4.0.0_1/share``` 행을 추가합니다.<br>

TESSDATA_PREFIX="/usr/share/tesseract-ocr/4.00/tessdata"

### Docker인 경우
```$ docker build --no-cache -t ocr_test_image .```