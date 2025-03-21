# Vision-Text RAG

이 프로젝트는 이미지와 텍스트를 결합한 Multimodal RAG(Retrieval-Augmented Generation)를 Streamlit으로 제공합니다.

Multimodal RAG를 ipynb로 간단한 실험은 다음 [Link](https://github.com/PARKYUNSU/pytorch_imple/tree/main/Agentic_RAG/Multimodal_RAG)를 참고하세요.

## Prerequisites
- Python 3.8 이상
- Mac OS (Intel 혹은 Apple Silicon)
- [Homebrew](https://brew.sh/)

## Quick Inference Setup for Mac Users

### 1. Install Homebrew (if not already installed)

터미널에서 아래 명령어를 실행하여 Homebrew를 설치합니다.

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

설치 후, Homebrew를 사용하기 위해 PATH에 추가합니다.

```bash
eval "$(/opt/homebrew/bin/brew shellenv)"
```
### 2. Install Google Cloud SDK
Google Cloud SDK는 gsutil 명령어를 사용하기 위해 필요합니다. 터미널에서 아래 명령어를 실행합니다.

```bash
brew install --cask google-cloud-sdk
```

### 3. Download MagicLens Models
프로젝트에 필요한 모델들을 Google Cloud Storage에서 다운로드합니다.

```bash
gsutil cp -R gs://gresearch/magiclens/models ./
```

### 4. Install Python Dependencies
가상환경을 활성화한 후, 아래 명령어로 Python 의존성을 설치합니다.
```bash
pip install -r requirements.txt
```

### 5. Configure Environment Variables
프로젝트에서 .env 파일을 아래와 같이 필요한 API 키 및 환경 변수를 설정합니다.

```dotenv
# OpenAI API key (또는 Azure OpenAI 사용 시 해당 키들을 설정)
OPENAI_API_KEY=your_openai_api_key_here

# (Azure OpenAI 사용 시)
AZURE_OPENAI_KEY=your_azure_openai_api_key_here
AZURE_OPENAI_ENDPOINT=https://your_azure_endpoint.com
AZURE_OPENAI_DEPLOYMENT_NAME=your_deployment_name
```

### 6. Vectorizing Image and Text with CLIP
이미지와 텍스트를 벡터화 하기 위해서 다음의 코드를 실해합니다.

Export
```bash
export PYTHONPATH=./project/VRAG/scenic:$PYTHONPATH
```

이미지 다운로드
```bash
python data.py
```

Indexing
```bash
python index.py
```

### 7. Run the Application
모든 설정이 완료되면, Streamlit을 사용하여 앱을 실행합니다.

```bash
streamlit run app.py
```

---
## APP 설명서

### 1. 이미지를 업로드 합니다.
<img src='https://github.com/user-attachments/assets/227e4123-ba35-4008-a4ab-bcd8dcb93bbd' width=200>

### 2. Query(질문)을 작성합니다.
```text
Any item with theme of this image
```
<img src="https://github.com/user-attachments/assets/3366a833-4d02-4c6a-93ea-9275e9fb7e24" width=200>


### 3. 결과 이미지

<img src="https://github.com/user-attachments/assets/604fe4ed-b0cc-4f75-8b92-5f3803c81de9" width=600>

| 해당 예시 이미지는 로컬 용량 문제로 DB를 적게 설정한 이미지입니다.
